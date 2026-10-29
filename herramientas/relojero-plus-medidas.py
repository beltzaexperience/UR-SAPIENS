#!/usr/bin/env python3
"""Relojero-Plus: batería de medidas (tipo M de la «Matriz del Relojero-Plus» de NORMA-METODO.md).

Uso:
    python3 herramientas/relojero-plus-medidas.py "cultura: continente ibérico umbral"
    python3 herramientas/relojero-plus-medidas.py "cultura: continente ibérico umbral" --frases

El argumento es un fragmento (sin importar mayúsculas) del atributo data-s de la
pieza en urtz.html. Imprime una tabla en markdown: una fila por norma medible, con
el valor, el umbral de la norma y el estado (OK / AVISO / ALARMA / INFO) y, cuando
hay hallazgos, las frases citadas. Con --frases imprime además todas las frases
numeradas, para la pasada de sentido (S) y la lectura línea por línea (L).

Límites (v1, 22/10/26): mide formas, no sentido. Un OK aquí no sustituye la lectura
de las normas de tipo L, S y O; solo evita que las medibles se omitan.
Los umbrales salen de las propias normas (se citan en cada fila).
"""
import re, sys, html, statistics as st, collections, os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HTML = os.path.join(RAIZ, 'urtz.html')


def pieza(s, frag):
    frag = frag.lower()
    for m in re.finditer(r'<details class="pieza"[^>]*data-s="([^"]*)"', s):
        ds = m.group(1)
        if frag in ds.lower() and not any(x in ds for x in ('glosas extendidas', 'estano recursos', 'fe de erratas')):
            i = m.start(); d = 0
            for mm in re.finditer(r'<details\b|</details>', s[i:]):
                d += 1 if mm.group(0).startswith('<details') else -1
                if d == 0:
                    return ds, s[i:i + mm.end()]
    sys.exit('No encuentro una pieza con ese fragmento de data-s')


def limpia(x):
    x = re.sub(r'<sup class="gr">\(\d+\)</sup>', '', x)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()


def frases(t):
    return re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡«"\'—])', t)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    frag = sys.argv[1]
    s = open(HTML, encoding='utf-8').read()
    ds, seg = pieza(s, frag)
    corte = seg.find('GLOSA &middot;')
    cuerpo_html = seg[:corte] if corte > 0 else seg
    glosa_html = seg[corte:] if corte > 0 else ''
    ps = re.findall(r'<p style="[^"]*">(.*?)</p>', cuerpo_html, re.S)
    P = [limpia(p) for p in ps]
    heads = re.findall(r'<h4[^>]*>(.*?)</h4>', cuerpo_html, re.S)
    heads_div = re.findall(r"<div style=\"font-family:'Bebas Neue',sans-serif; font-size:1\.1rem[^>]*>(.*?)</div>", cuerpo_html, re.S)
    li = re.findall(r'<li(?: [^>]*)?>(.*?)</li>', glosa_html, re.S)
    txt = ' '.join(P)
    W = len(txt.split())
    SF = []
    for t in P:
        SF += frases(t)
    L = [len(x.split()) for x in SF]
    filas = []

    def fila(norma, que, valor, umbral, estado, citas=None):
        filas.append((norma, que, valor, umbral, estado, citas or []))

    def cita(pat, flags=re.I):
        return [x[:150] for x in SF if re.search(pat, x, flags)]

    # --- estructura (24, 25, 26, 39, 43, 23) ---
    nh = len(heads) + len(heads_div)
    fila('24', 'palabras del cuerpo (sin glosa)', W, 'zona habitual 1.100-2.000', 'INFO')
    gw = sum(len(limpia(x).split()) for x in li)
    tot = W + gw
    pct = round(gw / tot * 100) if tot else 0
    fila('24', 'glosa sobre el total', '%d palabras, %d %%' % (gw, pct), 'zona habitual 24-43 %', 'OK' if 24 <= pct <= 43 else 'AVISO')
    fila('23', 'entradas de glosa', len(li), 'referencia 10-15 (no condena)', 'OK' if len(li) <= 15 else 'INFO')
    # tramos
    partes = re.split(r'<h4[^>]*>.*?</h4>|<div style="font-family:\'Bebas Neue\',sans-serif; font-size:1\.1rem[^>]*>.*?</div>', cuerpo_html, flags=re.S)
    tramos = [sum(len(limpia(p).split()) for p in re.findall(r'<p style="[^"]*">(.*?)</p>', x, re.S)) for x in partes]
    tramos = [t for t in tramos if t]
    fila('25', 'subtítulos internos', '%d en %d palabras' % (nh, W), 'referencia: 2-3 tramos por cada 1.000 palabras', 'OK' if nh <= max(3, round(W / 400)) else 'ALARMA')
    fila('43', 'subtítulos en la forma <h4> negra', '%d h4, %d div rojos' % (len(heads), len(heads_div)), 'solo h4 (Norma 43)', 'OK' if not heads_div else 'ALARMA')
    corto = [p for p in P if len(p.split()) <= 25]
    fila('26', 'párrafos cortos (≤ 25 palabras)', '%d de %d (%d %%)' % (len(corto), len(P), round(len(corto) / max(1, len(P)) * 100)), 'techo 10 % (20 % no pasa)', 'OK' if len(corto) / max(1, len(P)) <= .10 else ('AVISO' if len(corto) / len(P) < .20 else 'ALARMA'), [c[:100] for c in corto])
    fila('26', 'media de palabras por párrafo', round(W / max(1, len(P))), '4-8 líneas ≈ 60-120', 'OK' if 55 <= W / max(1, len(P)) <= 125 else 'AVISO')
    if len(tramos) > 1:
        r = max(tramos) / min(tramos)
        fila('39', 'razón entre tramos', '%s (%s)' % (round(r, 2), ', '.join(map(str, tramos))), 'referencia 3,1; alarma < 2,5 (informativa)', 'OK' if r >= 2.5 else 'AVISO')
    # --- frases y ritmo (33, 36.8, 38) ---
    dt = st.pstdev(L)
    fila('36.8', 'desviación típica de la longitud de frase', round(dt, 1), 'alarma < 9,8 (no objetivo)', 'OK' if dt >= 9.8 else 'AVISO')
    fila('33', 'frases de ≤ 8 palabras', '%d de %d' % (sum(1 for x in L if x <= 8), len(SF)), 'informativo', 'INFO')
    art = [x for x in SF if re.match(r'(El|La|Los|Las|Un|Una|Unos|Unas)\b', x)]
    en = [x for x in SF if x.startswith('En ')]
    fila('38', 'frases que abren con artículo', '%d de %d (%d %%)' % (len(art), len(SF), round(len(art) / len(SF) * 100)), 'alarma 35 %', 'OK' if len(art) / len(SF) <= .35 else 'ALARMA')
    fila('38', 'frases que abren con «En»', '%d (%d %%)' % (len(en), round(len(en) / len(SF) * 100)), 'molde «En + lugar» (informativo)', 'INFO')
    # --- tics léxicos y de forma ---
    c = cita(r'\bno (?:es|son|fue|fueron|solo|solamente)\b[^.;]*\b(?:sino|es|son)\b|\bsino\b')
    fila('1', 'no X, sino Y', len(c), '0', 'OK' if not c else 'ALARMA', c)
    c = cita(r'\baquí\b|\bapare[cz]\w+')
    fila('3', 'aquí / aparece', len(c), '0', 'OK' if not c else 'ALARMA', c)
    c = cita(r'\b(?:es importante|cabe señalar|conviene|hay que|se trata de|no hay que olvidar)\b')
    fila('5', 'andamios de entrada', len(c), '0', 'OK' if not c else 'ALARMA', c)
    c = cita(r'(?:ando|iendo|yendo)[.;]\s*$|,\s*\w*(?:ando|iendo|yendo)\b')
    fila('10', 'gerundio tras coma o final de frase', len(c), 'revisar cada uno (posterioridad)', 'OK' if not c else 'AVISO', c)
    c = cita(r'\b(?:puede\w*|podr\w+|parece\w*|quizá|al parecer|sugiere\w*|tal vez|probablemente|pertenece al terreno)\b')
    fila('32/32 bis', 'coberturas (puede, podría, parece, quizá, al parecer, sugiere…)', '%d en %d frases' % (len(c), len(SF)), 'cada una con argumento; repetidas = tic', 'OK' if len(c) <= 2 else 'AVISO', c)
    c = cita(r'\bmientras\b')
    fila('41.5', '«mientras A, B»', len(c), 'informativo (preferir a «A y B» si hay tensión)', 'INFO', c)
    c = cita(r'(?:\bque\b[^.;]*){3}')
    fila('41.1', 'frases con 3 o más «que»', len(c), 'preferir cláusula directa', 'OK' if not c else 'AVISO', c)
    c = cita(r'\bno\b[^.;]{0,60}[,;]\s*(?:sino|pero)\b')
    fila('42', 'antítesis «no…, sino/pero»', len(c), '3 o más en una pieza = patrón', 'OK' if len(c) < 3 else 'ALARMA', c)
    dp = txt.count(':'); pc = txt.count(';')
    fila('42 bis', 'dos puntos por mil palabras', '%d (%.1f)' % (dp, dp / W * 1000), 'mediana del libro 10,5; p90 20,7', 'OK' if dp / W * 1000 <= 20.7 else 'ALARMA')
    fila('36.8', 'punto y coma por mil palabras', '%d (%.1f)' % (pc, pc / W * 1000), 'aviso > 11', 'OK' if pc / W * 1000 <= 11 else 'AVISO')
    c = [x for x in SF if len(re.findall(r'\by\b', x)) >= 3]
    fila('4', 'frases con 3 o más «y»', len(c), 'saturación', 'OK' if not c else 'AVISO', [x[:150] for x in c])
    c = cita(r'\b[\wáéíóúñ]+,\s+[\wáéíóúñ ]{1,30},\s+[\wáéíóúñ ]{1,30}\s+y\s+[\wáéíóúñ ]+')
    fila('36.7', 'enumeraciones de 4 o más elementos (revisar si son cadena)', len(c), 'cada elemento un dato o un verbo propio', 'INFO', c)
    # Norma 54 (alarma y excepciones naturales, Luis 28/10/26): «cuerpo» no vale para todo
    EXC_CUERPO = (r'cuerpos? del delito|cuerpos? de agua|cuerpos? celestes?|tom\w+ cuerpo|(?:dar|da|dan|dio) cuerpo|cuerpo a cuerpo|de cuerpo presente|cuerpo humano'
                  r'|cuerpos? (?:legal\w*|normativ\w+|de seguridad|de bomberos|diplom\w+|docente|de (?:Cristo|ejército|policía))'
                  r'|(?:bell\w+|hermos\w+|desnud\w+|muert\w+|inerte\w*|animal\w*|devorad\w+)\W+(?:\w+\W+){0,3}cuerpos?'
                  r'|cuerpos?\W+(?:\w+\W+){0,3}(?:bell\w+|hermos\w+|desnud\w+|muert\w+|inerte\w*|animal\w*|devorad\w+)')
    c = cita(r'\bcuerpos?\b')
    sus = [x for x in c if not re.search(EXC_CUERPO, x, re.I)]
    dens = len(c) / W * 1e4
    est = 'ALARMA' if (dens > 30 or len(sus) >= 3) else ('AVISO' if sus else 'OK')
    fila('54', '«cuerpo»: usos, por 10.000 y sin excepción natural', '%d (%.0f por 10.000); %d sin excepción natural' % (len(c), dens, len(sus)),
         'control 30 por 10.000 (media del libro 15); sujeto concreto por defecto', est,
         [('[REVISAR] ' if x in sus else '[excepción natural] ') + x for x in c])
    mem = len(re.findall(r'\bmemoria\b', txt, re.I))
    fila('49', '«memoria» por 10.000 palabras', '%d (%.0f)' % (mem, mem / W * 1e4), 'control: 40 (media del libro 20,7)', 'OK' if mem / W * 1e4 <= 40 else 'ALARMA')
    c = cita(r'^(?:La|El)\s+(?:civilización|cultura|escritura|agricultura|función|transición|sequía|lectura|crítica|palabra|lengua|genética|hipótesis|pregunta|ascendencia|dependencia|irrigación|coordinación|burocracia|técnica|relación|infraestructura|proceso)\b')
    fila('47', 'frases con sujeto abstracto (heurística)', '%d de %d' % (len(c), len(SF)), 'actor concreto si existe; recuento formal por lectura', 'INFO', c)
    # --- moldes 59 y 60 ---
    c = cita(r'\bantes de (?:ser|que)\b|\bya (?:estaba|era|había|existía)\b|\bhasta que\b|\bsin nombre\b|\bmucho antes\b|\bdesde antes\b')
    fila('59', 'molde de la anterioridad', len(c), 'como máximo 1 por pieza (la tesis); 0 en apertura/cierre/título', 'OK' if len(c) <= 1 else 'ALARMA', c)
    c = cita(r'\bQuien(?:es)?\b[^.;:]{0,90}\b(?:decid\w+|mand\w+|orden\w+|control\w+|defin\w+|fij\w+|eleg\w+|dict\w+)\b|\b(?:decid\w+|determin\w+)\s+(?:qui[eé]n(?:es)?|qu[eé]|c[oó]mo|cu[aá]ndo|d[oó]nde)\b|qui[eé]n[^.;]{1,40},\s*qui[eé]n[^.;]{1,40}\s+y\s+qui[eé]n')
    fila('60', 'molde «Quien X decide Y»', len(c), 'como máximo 1 por pieza; nunca en serie ni triple', 'OK' if len(c) <= 1 else 'ALARMA', c)
    c = cita(r'\balguien\b')
    fila('adenda 17/10', '«alguien»', len(c), '0 (tic de voz anónima)', 'OK' if not c else 'ALARMA', c)
    c = cita(r'\ba veces\b')
    fila('Luis 22/10', '«a veces»', len(c), 'tibieza: «cuando» cumple mejor', 'OK' if not c else 'AVISO', c)
    # --- marcado, notas, glosa (15, 16, 55) ---
    rojo = re.sub(r'<span style="color:#b01a1a;">[^<]*</span>', '§', seg)
    suelto = [limpia(rojo)[max(0, m.start() - 20):m.end() + 20] for m in re.finditer(r'[uúùüû]r', limpia(rojo), re.I)]
    fila('15', 'UR sin marcar en rojo', len(suelto), '0', 'OK' if not suelto else 'ALARMA', suelto[:8])
    bad = 0
    for m in re.finditer(r'<(p|li|h3|h4)\b[^>]*>(.*?)</\1>', seg, re.S):
        if len(re.findall(r'<span\b', m.group(2))) != m.group(2).count('</span>'):
            bad += 1
    fila('HTML', '<span> sin cerrar o de más', bad, '0', 'OK' if not bad else 'ALARMA')
    sup = re.findall(r'<sup class="gr">\((\d+)\)</sup>', seg)
    ok = sup == [str(k) for k in range(1, len(sup) + 1)]
    gl = re.findall(r'font-size:0\.78em;">\((\d+)\)</span>', glosa_html)
    fila('18/55', 'llamadas en orden y una entrada por llamada', '%d llamadas, %d entradas, orden %s' % (len(sup), len(gl), 'correcto' if ok else 'ROTO'), 'iguales y consecutivas', 'OK' if ok and len(sup) == len(gl) else 'ALARMA')
    # --- años, cifras, nombres (50/56) ---
    anos = re.findall(r'\b(?:1[0-9]{3}|20[0-9]{2}|[2-9][0-9]{3}|[1-9]\.?[0-9]{3}\s?a\. ?C\.)\b', txt)
    cif = re.findall(r'\b\d[\d.,]*\b', txt)
    fila('50/56', 'años y cifras en el cuerpo', '%d años, %d cifras' % (len(anos), len(cif)), 'generalizar; exacto en la glosa', 'OK' if len(cif) <= 3 else 'AVISO', [a for a in cif][:8])
    nombres = re.findall(r'(?<![.¿¡:] )(?<!^)\b[A-ZÁÉÍÓÚÑ][a-záéíóúñü]{3,}\b', txt)
    top = collections.Counter(nombres)
    fila('56', 'nombres propios por mil palabras', '%d (%.0f)' % (len(nombres), len(nombres) / W * 1000), 'informativo (inventario en la redacción final)', 'INFO')
    # --- léxico repetido (27) ---
    stop = set('de la el en y a que los las un una por con para se del al es lo su sus como más no o también hasta sin entre sobre desde cuando quien donde pero esa ese esto este esta otros otras otra otro ya muy le les nos si fue son ser han ha era eran'.split())
    pal = [w for w in re.findall(r'[a-záéíóúñü]+', txt.lower()) if w not in stop and len(w) > 3]
    rep = [(w, n) for w, n in collections.Counter(pal).most_common(12) if n >= 4]
    fila('27', 'palabras de contenido repetidas (≥ 4)', ', '.join('%s %d' % x for x in rep) or 'ninguna', 'revisar si es eco o concepto', 'INFO')
    # --- cierres (31) ---
    ult = SF[-1]
    fila('31', 'última frase de la pieza (leer: ¿aporta información?)', len(ult.split()), 'prohibido el cierre que resume', 'INFO', [ult[:160]])
    cierres = [frases(p)[-1] for p in P]
    fila('31', 'última frase de cada párrafo (leer)', len(cierres), 'sin consigna que recapitule', 'INFO', [c[:110] for c in cierres])

    print('# Relojero-Plus · batería de medidas · %s' % ds[:70])
    print()
    print('Cuerpo: %d palabras, %d frases, %d párrafos, %d subtítulos. Glosa: %d entradas, %d palabras.' % (W, len(SF), len(P), nh, len(li), gw))
    print()
    print('| Norma | Qué se mide | Valor | Umbral de la norma | Estado |')
    print('|---|---|---|---|---|')
    for n, q, v, u, e, cs in filas:
        print('| %s | %s | %s | %s | **%s** |' % (n, q, v, u, e))
    print()
    hall = [f for f in filas if f[5] and f[4] in ('ALARMA', 'AVISO', 'INFO')]
    print('## Citas')
    for n, q, v, u, e, cs in hall:
        print('\n**%s · %s · %s**' % (n, q, e))
        for c in cs[:12]:
            print('- ' + c)
    if '--frases' in sys.argv:
        print('\n## Frases (para la pasada de sentido S y la lectura L)\n')
        for k, x in enumerate(SF, 1):
            print('%d. %s' % (k, x))
    al = sum(1 for f in filas if f[4] == 'ALARMA'); av = sum(1 for f in filas if f[4] == 'AVISO')
    print('\nResumen: %d alarmas, %d avisos, %d filas.' % (al, av, len(filas)))


if __name__ == '__main__':
    main()
