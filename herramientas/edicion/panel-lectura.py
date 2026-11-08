#!/usr/bin/env python3
"""Panel único de lectura (ver lectura-rubrica.md, «Método único»).

Prepara y resume una ronda de ocho lectores independientes que leen, cada uno, TODAS las piezas del panel
(las que se evalúan y las dos anclas de calibración) en órdenes rotados.

Uso:
  python3 panel-lectura.py preparar CARPETA nombre=CLAVE [nombre=CLAVE ...]
      CARPETA  carpeta de trabajo (se crea; debe estar fuera del repositorio, p. ej. en $UR_TRABAJO)
      nombre   etiqueta corta de la pieza (ks, cultura…)
      CLAVE    comienzo del atributo data-s de la pieza en urtz.html (único), p. ej. «kurt shakur florecer»
      Extrae cuerpo y glosa en limpio, copia las anclas (angostura e islandia1), crea lector_1…lector_8 con
      texto_1…texto_N en orden rotado, guarda mapa.json y escribe encargo_k.txt (el encargo de cada lector).
  python3 panel-lectura.py resumir CARPETA
      Lee resultados/lector_k.txt, los traduce con mapa.json y muestra notas brutas y ajustadas por calibración,
      criterios, diferencias por lector y las líneas cualitativas de cada pieza.

Cada encargo lleva el aviso de terminología UR / 'T' del protocolo del 27/10/26 (restituido el 08/11/26: la primera versión del panel único lo había omitido).
Los lectores son subagentes del mismo modelo: sirven para ordenar piezas y sacar reparos, no para decir si una pieza
es buena en absoluto. Diferencias menores de ≈0,2 puntos de nota son ruido.
"""
import html, json, os, re, shutil, statistics as st, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.path.join(RAIZ, 'urtz.html')
CAL = os.path.join(RAIZ, 'herramientas', 'edicion', 'calibracion')
ANCLAS = ['angostura', 'islandia1']
OFICIAL = {'angostura': 3.50, 'islandia1': 3.16}
CRIT = ['aporte', 'prosa', 'evidencia', 'publico', 'editores', 'entrada', 'emocion', 'noespecialista', 'memorabilidad']
LECTORES = 8

ENCARGO = """Eres un lector independiente y exigente de ensayo en español. No conoces al autor, ni la historia de los textos, ni otras lecturas. Tu tarea: leer {n} textos de un mismo libro de ensayo, que están en estos archivos y debes leer en este orden:
{lista}
AVISO DE TERMINOLOGÍA (es lo único que se te da por adelantado): En este libro «UR» es el símbolo del agua y del origen (en euskera, ur significa «agua»); es el protagonista y no se explica en cada pieza. La «'T'» es el signo del poder que ordena, cobra y obliga: el Estado, la tablilla, el impuesto. No se te pide compartir esa lectura, solo saber a qué se refieren los dos signos.
Cada texto es una pieza con su cuerpo y, al final, su glosa (notas numeradas). Léelos enteros, uno tras otro, y puntúa cada uno por separado, sin dejarte arrastrar por el anterior. Las piezas tienen longitudes distintas; no puntúes por tamaño.

PUNTUACIÓN: de 1 a 5, con medios puntos (1 muy flojo, 3 correcto, 5 excepcional; usa toda la escala, sin inflar ni castigar por defecto, y sé coherente al comparar los {n} textos entre sí), en nueve criterios:
- aporte: aporte a la tesis del libro y originalidad
- prosa: voz, ritmo, imagen; se penalizan muletillas y relleno
- evidencia: hechos, fuentes, glosa; se penalizan la pseudociencia y las etimologías presentadas como hecho
- publico: gancho, claridad, carga emocional y política
- editores: singularidad, valor citable, papel en la estructura; baja si hay riesgo legal o reputacional o si es redundante
- entrada: las primeras frases
- emocion: intensidad sostenida
- noespecialista: lector que se salta los términos técnicos
- memorabilidad

FORMATO: escribe un único archivo {salida} con exactamente este contenido, sin nada más:
texto_1|a|b|c|d|e|f|g|h|i   (nueve números separados por «|», por ejemplo texto_1|3.5|3|4|3|3.5|4|3.5|3|3.5)
texto_2|…
(una línea por texto)
Después, para cada texto, cinco líneas cortas (máximo 50 palabras cada una): T1_ENGANCHA: frase que más engancha; T1_FRIO: tramos donde se enfría; T1_VIVO: tramo más vivo; T1_REPAROS: reparos repetidos; T1_SACA: frases que sacan al lector (cita literal breve). Lo mismo con T2_, T3_…

NORMAS: no uses internet ni ningún otro archivo (solo esos {n} textos); no leas las carpetas de otros lectores; no modifiques nada salvo el archivo de resultados; no pidas aclaraciones. Al terminar responde solo «hecho»."""


def plain(x):
    return html.unescape(re.sub(r'<[^>]*>', '', x)).strip()


def extraer(s, clave):
    ms = [m.start() for m in re.finditer(r'<details class="pieza" data-s="%s' % re.escape(clave), s)]
    if len(ms) != 1:
        sys.exit('La clave «%s» encuentra %d piezas; afínala.' % (clave, len(ms)))
    i = ms[0]
    seg = s[i:s.find('</details>', i)]
    h3 = re.search(r'<h3[^>]*>(.*?)</h3>', seg, re.S)
    out = [plain(h3.group(1)), '']
    m = re.search(r'</h3>\s*<div style="font-family:\'Courier Prime\',monospace; font-style:italic[^>]*>(.*?)</div>', seg, re.S)
    if m:
        out += [plain(m.group(1)), '']
    for tg, t in re.findall(r'<(p|h4)[^>]*>(.*?)</\1>', seg[seg.find('</h3>'):], re.S):
        tx = plain(t)
        if not tx or tx.startswith('Actualizado'):
            continue
        out += (['', '## ' + tx, ''] if tg == 'h4' else [tx + '\n'])
    lis = re.findall(r'<li[^>]*><span style="color:#b01a1a; font-size:0.78em;">\((\d+)\)</span>(.*?)</li>', seg, re.S)
    out += ['', 'GLOSA', '']
    out += ['(%s) %s\n' % (n, re.sub(r'\s+', ' ', plain(t))) for n, t in lis]
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out))


def ordenes(piezas):
    rot = [piezas[r:] + piezas[:r] for r in range(len(piezas))]
    inv = [list(reversed(o)) for o in rot]
    return (rot + inv)[:LECTORES] if len(rot + inv) >= LECTORES else (rot + inv) * 2


def preparar(carpeta, pares):
    s = open(HTML, encoding='utf-8').read()
    os.makedirs(os.path.join(carpeta, 'textos'), exist_ok=True)
    os.makedirs(os.path.join(carpeta, 'resultados'), exist_ok=True)
    nombres = []
    for p in pares:
        nombre, clave = p.split('=', 1)
        open(os.path.join(carpeta, 'textos', nombre + '.txt'), 'w', encoding='utf-8').write(extraer(s, clave))
        nombres.append(nombre)
    for a in ANCLAS:
        shutil.copy(os.path.join(CAL, a + '.txt'), os.path.join(carpeta, 'textos', a + '.txt'))
    todas = nombres + ANCLAS
    mapa = {}
    for k, o in enumerate(ordenes(todas), 1):
        d = os.path.join(carpeta, 'lector_%d' % k)
        os.makedirs(d, exist_ok=True)
        for pos, nombre in enumerate(o, 1):
            shutil.copy(os.path.join(carpeta, 'textos', nombre + '.txt'), os.path.join(d, 'texto_%d.txt' % pos))
        mapa[k] = o
        lista = '\n'.join('%d) %s' % (i, os.path.join(d, 'texto_%d.txt' % i)) for i in range(1, len(o) + 1))
        salida = os.path.join(carpeta, 'resultados', 'lector_%d.txt' % k)
        open(os.path.join(carpeta, 'encargo_%d.txt' % k), 'w', encoding='utf-8').write(
            ENCARGO.format(n=len(o), lista=lista, salida=salida))
    json.dump(mapa, open(os.path.join(carpeta, 'mapa.json'), 'w'), indent=1)
    print('Panel preparado en', carpeta, '·', len(todas), 'textos ·', LECTORES, 'lectores')
    for k, o in mapa.items():
        print(' lector', k, o)
    print('Lanza ocho subagentes con el contenido de encargo_1.txt … encargo_8.txt.')


def nota(v):
    q = sum(v[:3]) / 3
    i = (v[3] + v[4]) / 2
    return q, i, .6 * q + .4 * i


def resumir(carpeta):
    mapa = {int(k): v for k, v in json.load(open(os.path.join(carpeta, 'mapa.json'))).items()}
    D = {}
    for k, o in mapa.items():
        f = os.path.join(carpeta, 'resultados', 'lector_%d.txt' % k)
        if not os.path.exists(f):
            print('Falta el lector', k)
            continue
        t = open(f, encoding='utf-8').read()
        for pos, nombre in enumerate(o, 1):
            m = re.search(r'^\s*texto_%d\|([\d.|]+)\s*$' % pos, t, re.M)
            if m and len(m.group(1).split('|')) == 9:
                D.setdefault(k, {})[nombre] = [float(x) for x in m.group(1).split('|')]
    piezas = [p for p in mapa[1] if p not in ANCLAS]
    print('lectores con resultados: %d de %d\n' % (len(D), LECTORES))
    print('%-16s' % 'criterio' + ''.join('%11s' % p for p in mapa[1]))
    for i, c in enumerate(CRIT):
        print('%-16s' % c + ''.join('%11.2f' % st.mean(D[k][p][i] for k in D) for p in mapa[1]))
    print()
    aj = {k: st.mean(OFICIAL[a] - nota(D[k][a])[2] for a in ANCLAS) for k in D}
    for p in mapa[1]:
        ns = [nota(D[k][p])[2] for k in D]
        linea = '%-10s bruta %.2f (calidad %.2f, impacto %.2f; desv %.2f; %.2f a %.2f)' % (
            p, st.mean(ns), st.mean(nota(D[k][p])[0] for k in D), st.mean(nota(D[k][p])[1] for k in D),
            st.stdev(ns) if len(ns) > 1 else 0, min(ns), max(ns))
        if p not in ANCLAS:
            a = [nota(D[k][p])[2] + aj[k] for k in D]
            linea += ' · AJUSTADA %.2f (%.2f a %.2f)' % (st.mean(a), min(a), max(a))
        print(linea)
    print('\nAjuste medio de calibración por lector:', ', '.join('%d:%+.2f' % (k, v) for k, v in aj.items()))
    if len(piezas) > 1:
        a, b = piezas[0], piezas[1]
        dif = [nota(D[k][a])[2] - nota(D[k][b])[2] for k in D]
        print('\nDiferencia %s − %s: media %+.2f (desv %.2f); a favor de %s: %d, empates: %d, a favor de %s: %d' % (
            a, b, st.mean(dif), st.stdev(dif), a, sum(x > 0.05 for x in dif), sum(abs(x) <= 0.05 for x in dif), b, sum(x < -0.05 for x in dif)))
    print('\nLetra: α desde 3,34 de nota ajustada; β de 2,74 a 3,33; γ por debajo (escala con calibración).')
    for p in piezas:
        print('\n=== %s: líneas cualitativas ===' % p)
        for k, o in mapa.items():
            f = os.path.join(carpeta, 'resultados', 'lector_%d.txt' % k)
            if not os.path.exists(f) or p not in o:
                continue
            pos = o.index(p) + 1
            t = open(f, encoding='utf-8').read()
            print('--- lector %d' % k)
            for tag in ('ENGANCHA', 'FRIO', 'VIVO', 'REPAROS', 'SACA'):
                m = re.search(r'^T%d_%s:\s*(.*)$' % (pos, tag), t, re.M)
                print('  %s: %s' % (tag, m.group(1)[:300] if m else '—'))


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == 'preparar':
        preparar(a[1], a[2:])
    elif len(a) == 2 and a[0] == 'resumir':
        resumir(a[1])
    else:
        sys.exit(__doc__)
