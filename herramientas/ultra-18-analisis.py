#!/usr/bin/env python3
"""Relojero Ultra · recorrido 5: los 18 análisis medidos de una pieza (Norma 62, punto 3.5).

Uso (con el entorno de spaCy y el modelo es_core_news_md; ver la cabecera de analisis-texto.py):
    python3 herramientas/ultra-18-analisis.py --cache /ruta/datos_canon.pkl --pieza KURT

Mide la pieza de URS cuyo título contenga --pieza en ventanas de 1.000 palabras con el mismo código de
`analisis-texto.py` y la compara con el corredor del canon (todas las obras del caché menos Martín Santos)
y con las piezas de URS ya medidas en el caché. Imprime una tabla markdown por indicador (valor de la pieza,
corredor p10·p50·p90, UR p10·p50·p90 y la dirección en que sale del corredor), las alarmas del marco y el
Delta de Burrows de la pieza frente al perfil medio de UR.

El caché (`--cache`) lo genera `analisis-texto.py` con las obras de referencia, que no están en el repositorio.
Cautelas: estadístico, se equivoca en prosa literaria y en los neologismos de UR; la perplejidad no se calcula.
"""
import sys, importlib.util, pickle, statistics as st, collections, argparse, os

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache', required=True)
    ap.add_argument('--pieza', required=True)
    ap.add_argument('--html', default=os.path.join(RAIZ, 'urtz.html'))
    ap.add_argument('--ventana', type=int, default=1000)
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location('at', os.path.join(AQUI, 'analisis-texto.py'))
    at = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(at)
    datos = pickle.load(open(a.cache, 'rb'))
    obras, ur = datos['obras'], datos['ur']
    aparte = [k for k in obras if 'martin' in k.lower() or 'santos' in k.lower()]
    canon = [k for k in obras if k not in aparte]
    nlp = at.cargar_nlp()
    cand = [p for p in at.pc.piezas_urs(a.html) if a.pieza.upper() in p[0].upper()]
    if len(cand) != 1:
        sys.exit('«%s» encuentra %d piezas de URS' % (a.pieza, len(cand)))
    tit, paras = cand[0]
    res, lows = at.medir_texto(paras, nlp, a.ventana)
    pct = at.pc.pct
    pool = {k: [w[k] for c in canon for w in obras[c] if k in w] for k in at.CLAVES}
    urv = {k: [w[k] for t in ur for w in ur[t] if k in w] for k in at.CLAVES}
    print('<!-- %s · ventanas %d · palabras %d -->' % (tit, len(res), sum(at.wc(p) for p in paras)))
    print('| análisis | indicador | pieza | corredor p10 · p50 · p90 | UR p10 · p50 · p90 | fuera (↑ sobre p90, ↓ bajo p10) |')
    print('|---|---|---|---|---|---|')
    for titulo, grupo in at.GRUPOS:
        for k, n in grupo:
            if not pool[k]:
                continue
            v = [w[k] for w in res if k in w]
            if not v:
                continue
            m = st.mean(v)
            lo, md, hi = pct(pool[k], 10), pct(pool[k], 50), pct(pool[k], 90)
            u = urv[k]
            flag = '↑' if m > hi else ('↓' if m < lo else '—')
            print('| %s | %s | %.1f | %.1f · %.1f · %.1f | %.1f · %.1f · %.1f | %s |' % (titulo.split(' · ')[0], n, m, lo, md, hi, pct(u, 10), pct(u, 50), pct(u, 90), flag))
    fuera = []
    for k, d in at.ALARMA.items():
        v = [w[k] for w in res if k in w]
        if not v:
            continue
        m = st.mean(v)
        lo, hi = pct(pool[k], 10), pct(pool[k], 90)
        if (d == '↑' and m > hi) or (d == '↓' and m < lo):
            fuera.append(k + d)
    print('\nAlarmas del marco fuera del corredor (%d de %d): %s' % (len(fuera), len(at.ALARMA), ' '.join(fuera) or 'ninguna'))
    import numpy as np
    low = dict(datos['mfw_low'])
    todo = collections.Counter(w for k in low for ven in low[k] for w in ven)
    mfw = [w for w, _ in todo.most_common(150)]

    def vec(ven):
        c = collections.Counter(ven)
        n = max(1, len(ven))
        return np.array([c[w] / n for w in mfw])
    V = {k: np.array([vec(v) for v in low[k]]) for k in low}
    allv = np.vstack([V[k] for k in V])
    mu, sd = allv.mean(0), allv.std(0) + 1e-9
    Z = {k: (V[k] - mu) / sd for k in V}
    perfil = {o: Z[o].mean(0) for o in obras}
    dist = lambda x, y: float(np.mean(np.abs(x - y)))
    centro = np.vstack([Z[t] for t in ur]).mean(0)
    za = ((np.array([vec(v) for v in lows]) - mu) / sd).mean(0)
    print('\nDelta de Burrows de la pieza: al perfil medio de UR %.2f; obras más cercanas: %s' % (
        dist(za, centro), ', '.join('%s %.2f' % (o[:14], dist(za, perfil[o])) for o in sorted(obras, key=lambda o: dist(za, perfil[o]))[:3])))
    dd = sorted(dist(Z[t].mean(0), centro) for t in ur)
    print('Distancias de las piezas de URS al perfil medio: mediana %.2f, p90 %.2f, máxima %.2f (aviso en 0,7)' % (st.median(dd), pct(dd, 90), dd[-1]))


if __name__ == '__main__':
    main()
