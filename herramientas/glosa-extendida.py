#!/usr/bin/env python3
"""Deposita la glosa íntegra de una pieza de URS en la pestaña GLOSAS EXTENDIDAS (Norma 55, punto 4).

Uso:  python3 herramientas/glosa-extendida.py "INICIO DEL TÍTULO DE LA PIEZA" ["Sección que se muestra"] [--prueba]

Lee la glosa actual de la pieza (antes de podarla), arma su pestaña interna con la etiqueta «⚑ PARA:» y el texto
completo, y la inserta en la pieza GLOSAS EXTENDIDAS de la categoría «CONTRAPORTADA Y GLOSAS EXTENDIDAS»
en el lugar que le corresponde por orden de URS. Con --prueba no escribe nada. No toca el Marcador ni la pieza.
"""
import html, re, sys, os

args = [a for a in sys.argv[1:] if not a.startswith('--')]
prueba = '--prueba' in sys.argv
if not args:
    sys.exit(__doc__)
clave = args[0]
seccion = args[1] if len(args) > 1 else ''
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta = os.path.join(raiz, 'urtz.html')
s = open(ruta, encoding='utf-8').read()
SP = '<span style="color:#b01a1a;">%s</span>'

def mark(t): return re.sub(r'(?i)ur', lambda m: SP % m.group(0), t)
def plain(x): return html.unescape(re.sub(r'<[^>]*>', '', x)).strip()

fin = s.find('FIN DEL LIBRO')
piezas = [(m.start(), plain(m.group(1))) for m in re.finditer(r'<details class="pieza"[^>]*>\s*<summary[^>]*>(.*?)</summary>', s, re.S)]
cand = [(p, t) for p, t in piezas if p < fin and t.startswith('▶' + clave) and 'GLOSAS EXTENDIDAS' not in t]
if len(cand) != 1:
    sys.exit('La clave «%s» encuentra %d piezas del libro; afínala.' % (clave, len(cand)))
pos, titulo_resumen = cand[0]
titulo = re.split(r'[αβγ☠]', titulo_resumen[1:])[0].strip()
fin_pieza = s.find('</details>', pos)
seg = s[pos:fin_pieza]
g = seg.find('GLOSA')
ls = re.findall(r'<li.*?</li>', seg[g:], re.S)
if not ls:
    sys.exit('La pieza no tiene glosa con entradas.')
top = s.find('data-s="glosas extendidas')
if top < 0:
    sys.exit('No existe la pieza GLOSAS EXTENDIDAS.')
top_fin = s.find('</details>\n', s.find('GLOSAS EXTENDIDAS &middot;', top))  # cierre de la pieza (tras el pie)
# pestañas ya depositadas, con la posición de su pieza de origen
pestanas = list(re.finditer(r'<details style="margin:1.2rem 0 0 0; border-top:1px solid rgba\(176,26,26,0.15\); padding-top:1rem;">\n<summary[^>]*>.*?</summary>.*?\n</details>\n', s[top:], re.S))
orden = []
for m in pestanas:
    t = plain(re.search(r'<summary[^>]*>(.*?)</summary>', m.group(0), re.S).group(1))
    t = t.lstrip('▶ ').split(' — ')[0].strip()
    orig = [p for p, tt in piezas if p < fin and tt.startswith('▶' + t)]
    orden.append((orig[0] if orig else 10 ** 9, top + m.start()))
if any(plain(re.search(r'<summary[^>]*>(.*?)</summary>', m.group(0), re.S).group(1)).lstrip('▶ ').split(' — ')[0].strip() == titulo for m in pestanas):
    sys.exit('Ya hay una pestaña para «%s».' % titulo)
# punto de inserción: antes de la primera pestaña cuya pieza de origen esté después; si no, antes del pie
ins = None
for p_orig, p_ins in sorted(orden):
    if p_orig > pos:
        ins = p_ins
        break
if ins is None:
    ins = s.rfind('      <div style="font-family:\'Bebas Neue\'', top, top_fin)
SUM = "font-family:'Bebas Neue',sans-serif; font-size:0.95rem; letter-spacing:0.12em; color:#b01a1a; cursor:pointer; list-style:none; padding:0.3rem 0; border-bottom:1px dotted rgba(176,26,26,0.25);"
PP = "font-family:'Courier Prime',monospace; font-size:1rem; line-height:1.8; color:#222; margin-bottom:0.8rem;"
parrafos = ''.join('<p style="%s">%s</p>\n' % (PP, re.sub(r'^<li[^>]*>|</li>$', '', l)) for l in ls)
para = ("<div style=\"font-family:'Bebas Neue',sans-serif; font-size:0.78rem; letter-spacing:0.15em; color:#c8922a; margin-bottom:0.9rem;\">"
        "&#9873; PARA: %s (URS) &mdash;las %d entradas de su glosa tal como estaban el %s, antes de pasarla a forma telegr&aacute;fica de dos niveles (Norma 55)&mdash;</div>"
        % (mark(titulo.replace('&', '&amp;').replace('·', '&middot;')), len(ls), '%s'))
import datetime
para = para % datetime.date.today().strftime('%d/%m/%y')
bloque = ('<details style="margin:1.2rem 0 0 0; border-top:1px solid rgba(176,26,26,0.15); padding-top:1rem;">\n'
          '<summary style="%s"><span style="font-size:0.7rem; margin-right:0.4rem;">&#9654;</span>%s <span style="color:#888; font-family:\'Courier Prime\',monospace; font-size:0.75rem; letter-spacing:0; font-style:italic;">&mdash; %s</span></summary>\n'
          '<div style="padding-top:0.5rem;">\n%s\n%s</div>\n</details>\n\n') % (SUM, mark(titulo.replace('&', '&amp;')), mark(seccion), para, parrafos)
if prueba:
    print('Pestaña que se insertaría (%d entradas, %d palabras) en la posición %d:' % (len(ls), len(plain(bloque).split()), ins))
    print(plain(bloque)[:600])
else:
    s = s[:ins] + bloque + s[ins:]
    assert s.count('<details') == s.count('</details>')
    open(ruta, 'w', encoding='utf-8').write(s)
    print('Pestaña insertada: «%s» (%d entradas).' % (titulo, len(ls)))
