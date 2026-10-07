#!/usr/bin/env python3
"""Perfil de frase de las piezas de urtz.html (Norma 36.8 de NORMA-METODO.md).

Mide, pieza a pieza y sobre el cuerpo (los <p> de 1.0x rem; la glosa y las notas
quedan fuera), los indicadores de la Norma 36.8 y los compara con un texto de
referencia (en UR, Baroja sobre San Sebastián, aportado por Luis el 07/10/26).

Uso:
    python3 herramientas/perfil-frase.py [--html urtz.html] [--ref texto.txt]
                                         [--pieza SUBCADENA] [--min-palabras 450]

  --ref     texto de referencia, un párrafo por línea (no se incluye en el
            repositorio). Sin él, solo se informa del libro.
  --pieza   muestra el detalle de las piezas cuyo título contenga la subcadena.

Las medidas son aproximadas: frases separadas por puntuación final, ':' o ';'
seguidos de mayúscula; «abstracto» = sustantivo con sufijo -ción, -sión, -dad,
-tud, -miento, -ncia, -ismo, -aje; «ancla» = nombre propio en cualquier posición salvo la primera palabra de la frase (que siempre lleva mayúscula), año o cifra: es una cota inferior. Sirven
como alarma para releer, no como cifra exacta.
"""
import argparse
import html
import re
import statistics as st

ART = {'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas'}
STOP = set('''el la los las un una unos unas esta este estos estas esa ese eso aquel aquella en de del al con por para sin sobre entre desde hasta hacia tras ante bajo cuando donde mientras aunque como si pero y o ni que se lo le les su sus mi tu cada todo toda todos todas otro otra otros otras ningún ninguna hay es son era fue ha han hubo así también además luego después antes hoy ahora aquí allí ya no nunca siempre solo sólo más menos muy tan tanto tal cuál qué quién cuándo dónde cómo primero segundo tercero'''.split())
PREP = set('en de desde hasta hacia tras ante bajo con por para sin sobre entre durante según contra a al'.split())
ABS = re.compile(r'\b\w+(?:ción|sión|dad|tud|miento|ncia|ismo|aje)\b', re.I)
CLAVES = [
    ('sd', 'desv. típica de la longitud de frase'),
    ('art', '% frases con artículo inicial'),
    ('art_racha', '% de esas frases que siguen a otra con artículo'),
    ('art_misma', '% de esas frases con el mismo sustantivo inicial'),
    ('anch', '% frases ancladas (nombre propio, año, cifra)'),
    ('abs', 'abstractos por 100 palabras'),
    ('enum', '% frases con enumeración de 3 o más'),
    ('short', '% frases de 8 palabras o menos'),
]


def wc(s):
    return len(re.findall(r"[\wáéíóúñüÁÉÍÓÚÑ'’]+", s))


def frases(t):
    return [s.strip() for s in re.split(r'(?<=[\.\?\!:;])\s+(?=[A-ZÁÉÍÓÚÑ¿¡«])', t) if s.strip()]


def limpia(w):
    return w.strip('.,;:()«»"¿¡').lower()


def tipo_apertura(s):
    """artículo / nombre propio / cifra o fecha / preposición / otra."""
    toks = s.split()
    p = limpia(toks[0])
    if p in ART:
        return 'art'
    if re.match(r'^\d', toks[0]):
        return 'cifra'
    if p in PREP:
        return 'prep'
    return 'otra'


def metricas(parrafos):
    # lista de frases por párrafo, conservando el límite de párrafo para las rachas
    P = []
    for p in parrafos:
        f = [re.sub(r'^[¿¡«"]+', '', s) for s in frases(p)]
        f = [s for s in f if wc(s) >= 2]
        if f:
            P.append(f)
    S = [s for f in P for s in f]
    if len(S) < 8:
        return None
    W = sum(wc(s) for s in S)
    L = [wc(s) for s in S]
    anch = 0
    for s in S:
        toks = s.split()
        caps = [w for w in toks[1:] if re.match(r'^[A-ZÁÉÍÓÚÑ][a-záéíóúñü]{2,}', w) and limpia(w) not in STOP]
        cifra = re.search(r'\b(1[0-9]{3}|20[0-9]{2}|\d{2,})\b', s)
        if caps or cifra:
            anch += 1
    art = racha = 0
    cabezas = {}
    for f in P:
        previa = False
        for s in f:
            toks = s.split()
            es_art = limpia(toks[0]) in ART
            if es_art:
                art += 1
                if previa:
                    racha += 1
                if len(toks) > 1:
                    c = limpia(toks[1])
                    cabezas[c] = cabezas.get(c, 0) + 1
            previa = es_art
    misma = sum(v for v in cabezas.values() if v >= 2)
    tipos = {}
    for s in S:
        k = tipo_apertura(s)
        tipos[k] = tipos.get(k, 0) + 1
    n = len(S)
    ab = len(ABS.findall(' '.join(S)))
    enum = sum(1 for s in S if re.search(r'(,[^,;:]+){2,}\s(y|o|ni)\s', s))
    return dict(
        W=W, S=n, sd=st.pstdev(L), art=100 * art / n,
        art_racha=100 * racha / art if art else 0.0,
        art_misma=100 * misma / art if art else 0.0,
        anch=100 * anch / n, abs=100 * ab / W, enum=100 * enum / n,
        short=100 * sum(1 for x in L if x <= 8) / n,
        tipos={k: 100 * v / n for k, v in tipos.items()},
        cabezas=sorted(cabezas.items(), key=lambda kv: -kv[1])[:5],
    )


def piezas(ruta):
    s = open(ruta, encoding='utf-8').read()
    frontera = s.find('FRONTERA REAL URS')
    out = []
    for m in re.finditer(r'<details class="pieza"[^>]*>(.*?)</details>', s, flags=re.S):
        blk = m.group(1)
        sm = re.search(r'<summary[^>]*>(.*?)</summary>', blk, flags=re.S)
        titulo = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', sm.group(1)))).strip().lstrip('▶').strip()
        ps = re.findall(r'<p style="[^"]*font-size:1\.0[0-9]*rem[^"]*">(.*?)</p>', blk, flags=re.S)
        paras = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', p))).strip() for p in ps]
        paras = [p for p in paras if p]
        mm = metricas(paras)
        out.append(('URS' if m.start() < frontera else 'URIM', titulo, mm))
    return out


def pct(vals, p):
    v = sorted(vals)
    k = (len(v) - 1) * p / 100
    f = int(k)
    return v[f] + (v[min(f + 1, len(v) - 1)] - v[f]) * (k - f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--html', default='urtz.html')
    ap.add_argument('--ref')
    ap.add_argument('--pieza')
    ap.add_argument('--min-palabras', type=int, default=450)
    a = ap.parse_args()

    ref = None
    if a.ref:
        ref = metricas([l.strip() for l in open(a.ref, encoding='utf-8') if l.strip()])
    rows = [r for r in piezas(a.html) if r[2] and r[2]['W'] >= a.min_palabras]
    urs = [r for r in rows if r[0] == 'URS']
    print('piezas medidas: %d (URS %d)' % (len(rows), len(urs)))
    print('\n%-48s %7s | %6s %6s %6s %6s %6s' % ('indicador', 'REF', 'p10', 'p25', 'p50', 'p75', 'p90'))
    for k, n in CLAVES:
        v = [r[2][k] for r in urs]
        print('%-48s %7s | %6.1f %6.1f %6.1f %6.1f %6.1f' % (
            n, '%.1f' % ref[k] if ref else '-', pct(v, 10), pct(v, 25), pct(v, 50), pct(v, 75), pct(v, 90)))
    print('\napertura de frase (% del total): artículo / cifra / preposición / otra')
    for etiqueta, d in [('referencia', ref)] + [('libro (mediana)', None)]:
        if d is None:
            ks = ['art', 'cifra', 'prep', 'otra']
            print('  %-18s' % etiqueta, ' / '.join('%4.0f' % st.median(r[2]['tipos'].get(k, 0) for r in urs) for k in ks))
        elif d:
            print('  %-18s' % etiqueta, ' / '.join('%4.0f' % d['tipos'].get(k, 0) for k in ['art', 'cifra', 'prep', 'otra']))
    if a.pieza:
        for z, t, m in rows:
            if a.pieza.lower() in t.lower():
                print('\n%s · %s' % (z, t))
                for k, n in CLAVES:
                    print('  %-48s %6.1f' % (n, m[k]))
                print('  apertura:', {k: round(v) for k, v in m['tipos'].items()})
                print('  sustantivos que más se repiten tras artículo inicial:', m['cabezas'])


if __name__ == '__main__':
    main()
