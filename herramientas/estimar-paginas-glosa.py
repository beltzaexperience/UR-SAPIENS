#!/usr/bin/env python3
"""Estimación de páginas del libro puro con la glosa telegráfica (Norma 55).

Lee urtz.html y herramientas/glosas-tratadas.json (palabras de glosa antes y después en cada
pieza ya tratada) y calcula: ahorro medio r de las piezas tratadas, glosa sin tratar del libro puro
y páginas estimadas = (palabras del libro puro - r * glosa sin tratar) / 250.
Cada pieza nueva que se trate se añade al JSON y se vuelve a ejecutar.
"""
import html, json, os, re, sys

aqui = os.path.dirname(os.path.abspath(__file__))
raiz = os.path.dirname(aqui)
s = open(os.path.join(raiz, 'urtz.html'), encoding='utf-8').read()
tratadas = json.load(open(os.path.join(aqui, 'glosas-tratadas.json'), encoding='utf-8'))

def txt(x):
    return html.unescape(re.sub(r'<[^>]*>', '', x))

m = re.search(r'LIBRO PURO.*?caracteres &middot; ([\d.]+) palabras', s, re.S)
palabras_libro = int(m.group(1).replace('.', ''))
fin = s.find('FIN DEL LIBRO')
glosa = 0
for p in re.finditer(r'<details class="pieza"[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>', s, re.S):
    if p.start() > fin:
        break
    for ul in re.findall(r"<ul style=\"font-family:'Courier Prime'.*?</ul>", p.group(2), re.S):
        glosa += len(txt(ul).split())
UMBRAL = 150  # solo las glosas de partida de al menos 150 palabras fijan r: las cortas, podadas hasta cero, no representan lo que queda
repr_ = {k: v for k, v in tratadas.items() if v[0] >= UMBRAL}
tratadas_despues = sum(d for _, d in tratadas.values())
sin_tratar = glosa - tratadas_despues

def paginas(r):
    return (palabras_libro - r * sin_tratar) / 250

antes = sum(a for a, _ in repr_.values())
despues = sum(d for _, d in repr_.values())
r_pond = (antes - despues) / antes                       # ponderado por palabras
ahorros = sorted((a - d) / a for a, d in repr_.values())  # ahorro de cada pieza
n = len(ahorros)
r_med = ahorros[n // 2] if n % 2 else (ahorros[n // 2 - 1] + ahorros[n // 2]) / 2   # mediana: robusta ante una pieza extrema
sin_extremos = {k: v for k, v in repr_.items() if (v[0] - v[1]) / v[0] < 0.9}
r_sin = (sum(a for a, _ in sin_extremos.values()) - sum(d for _, d in sin_extremos.values())) / sum(a for a, _ in sin_extremos.values())
est = [paginas(r_med), paginas(r_pond), paginas(r_sin)]
print('piezas tratadas: %d; con glosa de partida de %d palabras o más: %d' % (len(tratadas), UMBRAL, n))
print('glosa del libro puro: %d palabras (%.0f pág.); sin tratar: %d' % (glosa, glosa / 250, sin_tratar))
print('palabras del libro puro (Marcador): %d (%.1f pág.)' % (palabras_libro, palabras_libro / 250))
print('ahorro por pieza: ' + ', '.join('%.0f %%' % (x * 100) for x in ahorros))
print('r mediana %.1f %% -> ≈%d pág. (CENTRAL, la del cartel)' % (r_med * 100, round(est[0])))
print('r ponderada %.1f %% -> ≈%d pág.' % (r_pond * 100, round(est[1])))
print('r sin piezas de ahorro ≥ 90 %% (%.1f %%) -> ≈%d pág.' % (r_sin * 100, round(est[2])))
print('rango entre los tres estimadores: ≈%d a ≈%d pág.' % (round(min(est)), round(max(est))))
