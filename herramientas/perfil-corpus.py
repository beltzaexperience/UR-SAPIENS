#!/usr/bin/env python3
"""Perfil de corpus: UR frente al canon de referencia (LINEA-EDITORIAL-REFERENTES.md).

Mide obras narrativas completas (PDF o TXT; los textos NO se incluyen en el repositorio)
con los indicadores de `perfil-frase.py` más una batería de rasgos de estilo, y compara
cada pieza de URS con el «corredor» del canon: el rango p10–p90 de los trozos de unas
2.000 palabras de las obras de referencia.

Método:
  1. Cada PDF se pasa por `pdftotext` (sin -layout); se reconstruyen los párrafos
     (línea corta que acaba en puntuación final = fin de párrafo; cabeceras y números
     de página repetidos se descartan).
  2. Se separan los párrafos de diálogo (raya o comillas angulares iniciales); se mide
     solo la narración. Con --hyph CLAVE el diálogo de esa obra empieza por guion.
  3. Se trocea la narración en bloques de ~2.000 palabras y se mide cada bloque.
  4. Se mide cada pieza de URS (cuerpo: los <p> de 1.0x rem) y se cuenta, por indicador,
     cuántas caen por debajo del p10 o por encima del p90 del corredor.

Uso:
    python3 herramientas/perfil-corpus.py \\
        --obra baroja_aurora=/ruta/aurora-roja.pdf --hyph baroja_aurora \\
        --obra orwell_1984=/ruta/1984.pdf \\
        --obra martin_santos=/ruta/tiempo-de-silencio.pdf --aparte martin_santos \\
        [--html urtz.html] [--matriz] [--pieza SUBCADENA]

  --aparte CLAVE   obra que se mide y se muestra pero no entra en el corredor
                   (p. ej. Martín Santos, referente de pico licenciado, no de línea).
  --matriz         lista las piezas de URS ordenadas por cuántas de las 8 señales
                   principales caen dentro del corredor.
  --pieza TEXTO    detalle de las piezas cuyo título contenga TEXTO.

Cautelas: Orwell está en traducción al español (la sintaxis es en parte del traductor);
Baroja y Martín Santos, en original. Las medidas son aproximadas (nombres propios y
abstractos se detectan por la forma de la palabra). Sirven como alarma para releer y
como contraste, no como cuota.
"""
import argparse
import collections
import importlib.util
import os
import re
import statistics as st
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('pf', os.path.join(AQUI, 'perfil-frase.py'))
pf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pf)
wc = pf.wc


# ---------- lectura y reconstrucción de párrafos ----------
def leer(ruta):
    if ruta.lower().endswith('.pdf'):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'o.txt')
            subprocess.run(['pdftotext', ruta, out], check=True)
            return open(out, encoding='utf-8').read().split('\n')
    return open(ruta, encoding='utf-8').read().split('\n')


def parrafos(lineas, guion=False):
    cab = collections.Counter(l.strip() for l in lineas if 0 < len(l.strip()) < 70)
    heads = {k for k, v in cab.items() if v >= 15 and not re.match(r'^[—–-]', k)}
    largos = sorted(len(l) for l in lineas if len(l.strip()) > 25)
    umbral = 0.80 * largos[int(len(largos) * 0.9)]
    out, cur = [], []

    def vuelca():
        nonlocal cur
        if cur:
            t = re.sub(r'\s+', ' ', ' '.join(cur)).strip()
            if t:
                out.append(t)
        cur = []

    for raw in lineas:
        s = raw.strip()
        if not s:
            continue
        if re.match(r'^[-–]?\s*\d{1,4}\s*[-–]?$', s) or s in heads:
            continue
        if re.match(r'^(\*|\*\s*\*\s*\*|[IVXLC]+\.?|CAP[IÍ]TULO.*|PARTE.*|LIBRO.*|SEGUNDA PARTE|PRIMERA PARTE|TERCERA PARTE|\d{1,3}\.?)$', s):
            vuelca()
            continue
        if (re.match(r'^[—–]\s?\S', s) or (guion and re.match(r'^-\s?[¿¡A-ZÁÉÍÓÚÑ«]', s))) and cur:
            vuelca()
        if cur and cur[-1].endswith('-') and re.match(r'^[a-záéíóúñü]', s) and re.search(r'[a-záéíóúñ]-$', cur[-1]):
            cur[-1] = cur[-1][:-1] + s
        else:
            cur.append(s)
        if len(s) < umbral and re.search(r'[\.\?\!»"”…]$', s):
            vuelca()
    vuelca()
    return out


def es_dialogo(p, guion=False):
    return bool(re.match(r'^\s*[—–]\s?\S|^\s*«', p) or (guion and re.match(r'^-\s?[¿¡A-ZÁÉÍÓÚÑ«]', p)))


def cierres(paras):
    """(k, n): párrafos de 2+ frases cuya última frase tiene ≤8 palabras tras una de ≥20, y total de párrafos de 2+ frases."""
    k = n = 0
    for p in paras:
        f = [x for x in pf.frases(p) if wc(x) >= 2]
        if len(f) >= 2:
            n += 1
            if wc(f[-1]) <= 8 and wc(f[-2]) >= 20:
                k += 1
    return k, n


def trozos(paras, n=2000):
    out, cur, w = [], [], 0
    for p in paras:
        cur.append(p)
        w += wc(p)
        if w >= n:
            out.append(cur)
            cur, w = [], 0
    if cur and w >= n * 0.6:
        out.append(cur)
    return out


# ---------- rasgos adicionales ----------
def extras(paras):
    T = ' '.join(paras)
    W = wc(T)
    S = [s for p in paras for s in pf.frases(p) if wc(s) >= 2]
    L = [wc(s) for s in S]
    pw = [wc(p) for p in paras]
    una = sum(1 for p in paras if len([s for s in pf.frases(p) if wc(s) >= 2]) <= 1)
    cnt = lambda rx, fl=0: len(re.findall(rx, T, flags=fl))
    sino = cnt(r'\b[Nn]o\b(?![^.;:?!]{0,40}\bsolo\b)[^.;:?!]{0,90}?\bsino\b')
    ger = [g for g in re.findall(r'\b\w{3,}(?:ando|iendo|yendo)\b', T, flags=re.I)
           if g.lower() not in ('cuando', 'fernando', 'armando', 'orlando', 'hernando', 'amando', 'mando', 'comando', 'bando', 'grande')]
    pal = re.findall(r"[a-záéíóúñü]+", T.lower())
    per = lambda n: 10000 * n / W
    return dict(
        caus=1000 * cnt(r'\b(porque|pues|puesto que|ya que|de modo que|de manera que|así que|por eso|por lo tanto|es decir|o sea|dado que|por tanto|de ahí que|de ahí)\b', re.I) / W,
        adv=1000 * cnt(r'\b(pero|sin embargo|aunque|mientras|aun así|no obstante|en cambio|por el contrario)\b', re.I) / W,
        maxfr=max(L),
        pw_med=st.median(pw), par1=100 * una / len(paras), par_corto=100 * sum(1 for x in pw if x <= 25) / len(paras),
        sl_med=st.median(L), sl_p90=sorted(L)[int(len(L) * .9)], sl_largas=100 * sum(1 for x in L if x > 40) / len(L),
        sino=per(sino), cond=per(cnt(r'\b(podría|podrían|podríamos|sería|serían|parecería|parecerían)\b', re.I)),
        hedge=per(cnt(r'\b(quizá|quizás|tal vez|acaso|a lo mejor|puede que|parece que|al parecer)\b', re.I)),
        ger=per(len(ger)), mente=1000 * cnt(r'\b\w{4,}mente\b', re.I) / W,
        y100=100 * cnt(r'\by\b') / W, simil=per(cnt(r'\bcomo (?:si|un|una|el|la|los|las)\b', re.I)),
        wlen=st.mean(len(w) for w in pal) if pal else 0,
        semi=1000 * T.count(';') / W, colon=1000 * T.count(':') / W)


INDICADORES = [
    ('sd', 'desviación típica de la longitud de frase'),
    ('art', '% frases con artículo inicial'),
    ('art_racha', '% de ellas tras otra con artículo'),
    ('anch', '% frases ancladas'),
    ('abs', 'abstractos por 100 palabras'),
    ('enum', '% frases con enumeración de 3+'),
    ('short', '% frases de 8 palabras o menos'),
    ('pw_med', 'palabras por párrafo (mediana)'),
    ('sl_p90', 'longitud de frase (p90)'),
    ('sl_largas', '% frases de más de 40 palabras'),
    ('sino', '«no… sino» por 10.000 palabras'),
    ('ger', 'gerundios por 10.000'),
    ('mente', 'adverbios en -mente por 1.000'),
    ('y100', '«y» por 100 palabras'),
    ('simil', 'símiles («como un…») por 10.000'),
    ('wlen', 'longitud media de palabra (letras)'),
    ('semi', 'punto y coma por 1.000'),
    ('colon', 'dos puntos por 1.000'),
    ('caus', 'conectores causales y explicativos por 1.000'),
    ('adv', 'conectores adversativos y concesivos por 1.000'),
    ('par_corto', '% de párrafos de 25 palabras o menos'),
    ('cond', 'condicionales (podría, sería…) por 10.000'),
    ('hedge', 'cautelas (quizá, tal vez, parece que…) por 10.000'),
]
SENALES = ['sd', 'art', 'abs', 'colon', 'sl_largas', 'anch', 'enum', 'ger']


def valor(m, e, k):
    return m[k] if k in m else e[k]


def pct(vals, p):
    v = sorted(vals)
    k = (len(v) - 1) * p / 100
    f = int(k)
    return v[f] + (v[min(f + 1, len(v) - 1)] - v[f]) * (k - f)


def medir_obra(ruta, guion):
    P = parrafos(leer(ruta), guion)
    narr = [p for p in P if not es_dialogo(p, guion)]
    ch = []
    for t in trozos(narr):
        m = pf.metricas(t)
        if m:
            ch.append((m, extras(t)))
    return dict(W=sum(wc(p) for p in P), Wn=sum(wc(p) for p in narr), chunks=ch, cierre=cierres(narr))


def piezas_urs(html_ruta):
    """[(título, [párrafos del cuerpo])] de las piezas de URS (los <p> de 1.0x rem; sin glosa ni notas)."""
    import html as _h
    s = open(html_ruta, encoding='utf-8').read()
    frontera = s.find('FRONTERA REAL URS')
    out = []
    for m in re.finditer(r'<details class="pieza"[^>]*>(.*?)</details>', s, flags=re.S):
        if m.start() > frontera:
            continue
        blk = m.group(1)
        sm = re.search(r'<summary[^>]*>(.*?)</summary>', blk, flags=re.S)
        t = re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', '', sm.group(1)))).strip().lstrip('▶').strip()
        ps = re.findall(r'<p style="[^"]*font-size:1\.0[0-9]*rem[^"]*">(.*?)</p>', blk, flags=re.S)
        ps = [re.sub(r'<sup class="gr">.*?</sup>', '', p, flags=re.S) for p in ps]  # llamadas de glosa (n): no son texto
        paras = [re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', '', p))).strip() for p in ps]
        out.append((t.split('☠')[0].strip(), [p for p in paras if p]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--obra', action='append', required=True, help='clave=ruta (pdf o txt)')
    ap.add_argument('--hyph', action='append', default=[])
    ap.add_argument('--aparte', action='append', default=[])
    ap.add_argument('--html', default='urtz.html')
    ap.add_argument('--matriz', action='store_true')
    ap.add_argument('--pieza')
    ap.add_argument('--ordena', help='clave de un indicador: lista las piezas de URS ordenadas de mayor a menor valor')
    a = ap.parse_args()

    obras = {}
    for kv in a.obra:
        k, r = kv.split('=', 1)
        obras[k] = medir_obra(r, k in a.hyph)
        print('%-18s %7d palabras, narración %7d, %d trozos' % (k, obras[k]['W'], obras[k]['Wn'], len(obras[k]['chunks'])), file=sys.stderr)

    # UR: se miden las piezas con sus rasgos adicionales
    UR = []
    cierre_ur = [0, 0]
    for t, paras in piezas_urs(a.html):
        mm = pf.metricas(paras)
        if mm and mm['W'] >= 450:
            UR.append((t, mm, extras(paras)))
            k, n = cierres(paras)
            cierre_ur[0] += k
            cierre_ur[1] += n
    print('piezas de URS medidas: %d' % len(UR))

    canon = [k for k in obras if k not in a.aparte]
    pool = {k: [valor(m, e, k) for c in canon for m, e in obras[c]['chunks']] for k, _ in INDICADORES}
    cols = list(obras)
    print('\n%-44s' % 'indicador (mediana de trozos de ~2.000 palabras)', *['%11s' % c[:11] for c in cols],
          '| corredor p10 p50 p90 | UR p50 | piezas <p10 >p90')
    corr = {}
    for k, n in INDICADORES:
        lo, md, hi = pct(pool[k], 10), pct(pool[k], 50), pct(pool[k], 90)
        corr[k] = (lo, hi)
        u = [valor(m, e, k) for _, m, e in UR]
        fila = [st.median([valor(m, e, k) for m, e in obras[c]['chunks']]) for c in cols]
        print('%-44s' % n[:44], *['%11.1f' % x for x in fila],
              '| %6.1f %6.1f %6.1f | %6.1f | %3d %3d' % (lo, md, hi, pct(u, 50), sum(1 for x in u if x < lo), sum(1 for x in u if x > hi)))

    print('\ncierres aforísticos (último ≤8 palabras tras una de ≥20), % de los párrafos de 2+ frases:')
    for c in cols:
        k, n = obras[c]['cierre']
        print('  %-18s %5.1f %%  (%d de %d)' % (c, 100 * k / max(1, n), k, n))
    print('  %-18s %5.1f %%  (%d de %d)' % ('UR (66 piezas)', 100 * cierre_ur[0] / max(1, cierre_ur[1]), cierre_ur[0], cierre_ur[1]))

    if a.ordena:
        k = a.ordena
        if k not in [c for c, _ in INDICADORES] + ['maxfr']:
            sys.exit('indicador desconocido: %s' % k)
        print('\nPIEZAS DE URS por «%s» (mayor a menor)' % k)
        for t, m, e in sorted(UR, key=lambda x: -valor(x[1], x[2], k)):
            print('%8.1f  %-62s %5d pal.' % (valor(m, e, k), t.split('☠')[0].strip()[:62], m['W']))

    if a.matriz or a.pieza:
        print('\nPIEZAS DE URS: señales dentro del corredor (de %d: %s)' % (len(SENALES), ', '.join(SENALES)))
        filas = []
        for t, m, e in UR:
            fuera = []
            for k in SENALES:
                v = valor(m, e, k)
                if v < corr[k][0]:
                    fuera.append(k + '↓')
                elif v > corr[k][1]:
                    fuera.append(k + '↑')
            filas.append((len(SENALES) - len(fuera), t, m['W'], fuera))
        filas.sort(key=lambda x: (-x[0], x[1]))
        for d, t, w, fuera in filas:
            if a.matriz or (a.pieza and a.pieza.lower() in t.lower()):
                print('%d/%d  %-60s %5d pal.  fuera: %s' % (d, len(SENALES), t.split('☠')[0].strip()[:60], w, ' '.join(fuera)))


if __name__ == '__main__':
    main()
