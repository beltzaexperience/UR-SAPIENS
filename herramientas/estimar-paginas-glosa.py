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
antes = sum(a for a, _ in repr_.values())
despues = sum(d for _, d in repr_.values())
r = (antes - despues) / antes
todas_antes = sum(a for a, _ in tratadas.values())
todas_despues = sum(d for _, d in tratadas.values())
r_todas = (todas_antes - todas_despues) / todas_antes
tratadas_despues = sum(d for _, d in tratadas.values())
sin_tratar = glosa - tratadas_despues
paginas = (palabras_libro - r * sin_tratar) / 250
print('piezas tratadas: %d (todas: glosa %d -> %d, ahorro %.1f %%)' % (len(tratadas), todas_antes, todas_despues, r_todas * 100))
print('piezas con glosa de partida de %d palabras o más: %d (glosa %d -> %d; ahorro medio r = %.1f %%)' % (UMBRAL, len(repr_), antes, despues, r * 100))
print('glosa del libro puro: %d palabras (%.0f pág.); sin tratar: %d' % (glosa, glosa / 250, sin_tratar))
print('palabras del libro puro (Marcador): %d (%.1f pág.)' % (palabras_libro, palabras_libro / 250))
print('páginas estimadas con glosa telegráfica: %.1f -> ≈%d' % (paginas, round(paginas)))
print('(con r de todas las piezas, %.1f %%: ≈%d pág.)' % (r_todas * 100, round((palabras_libro - r_todas * sin_tratar) / 250)))
rs = [(a - d) / a for a, d in repr_.values()]
lo, hi = min(rs), max(rs)
print('rango con el mínimo y el máximo de esas piezas (%.0f %% y %.0f %%): ≈%d a ≈%d pág.' % (
    lo * 100, hi * 100, round((palabras_libro - hi * sin_tratar) / 250), round((palabras_libro - lo * sin_tratar) / 250)))
