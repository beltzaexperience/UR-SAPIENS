#!/usr/bin/env python3
"""Relojero-Plus Ultra · recorrido 3, palabra por palabra (Norma 62, punto 3).

Uso:
    python3 herramientas/relojero-ultra-palabras.py "kurt shakur ultima frontera analogica"
    python3 herramientas/relojero-ultra-palabras.py "<fragmento de data-s>" --lexico ruta1.txt ruta2.txt

El primer argumento es un fragmento (sin importar mayúsculas) del atributo data-s de la
pieza en urtz.html, igual que en `relojero-plus-medidas.py`. Imprime markdown con cinco bloques:

  (i)   «ur» en rojo en todas sus variantes y la 'T' entre comillas rectas simples;
  (ii)  concordancia de palabras de contenido repetidas (Norma 27) y palabras vigiladas
        («cuerpo», Norma 54; «memoria», Norma 49; palabrería, Norma 46);
  (iii) términos propios contra `GLOSARIO-UR-SAPIENS.md` y variantes de escritura;
  (iv)  ortografía, concordancia y tipografía (reglas formales y léxico desconocido);
  (v)   cada nombre propio, cifra y fecha del cuerpo contra su glosa (Normas 50, 55 y 56).

Límites (v1, 29/10/26): mide formas, no sentido. El «léxico desconocido» compara cada
palabra con el resto de urtz.html (y con los textos de --lexico, si se pasan); no es un
corrector ortográfico: sirve para que ninguna palabra rara pase sin mirarla. Un OK aquí
no sustituye la lectura de Claude; solo evita que las comprobaciones mecánicas se omitan.
"""
import re, sys, html, os, collections, argparse, importlib.util

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HTML = os.path.join(RAIZ, 'urtz.html')
GLOSARIO = os.path.join(RAIZ, 'GLOSARIO-UR-SAPIENS.md')

spec = importlib.util.spec_from_file_location('plus', os.path.join(os.path.dirname(__file__), 'relojero-plus-medidas.py'))
plus = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plus)

ROJO = r'<span style="color:#b01a1a;">'
STOP = set('''a al algo algún alguna algunas alguno algunos ambos ante antes aquel aquella aquellas aquello aquellos aquí así aun aunque
cada como con contra cual cuales cuando de del desde donde dos e el ella ellas ello ellos en entre era eran es esa esas ese eso esos esta
están estar este esto estos fue fueron ha había han hasta hay la las le les lo los más me mi mis mientras mismo muy ni no nos nosotros o otra
otras otro otros para pero poco por porque que quien quienes se sea según ser si sí sin sobre solo son su sus también tan tanto te tiene
tienen todo todos tras tu un una unas uno unos va van y ya yo cuánto cuántos qué cómo dónde cuándo quién todavía menos mucho muchos cuyo cuya'''.split())
VIGILADAS = {
    'cuerpo': r'\bcuerp(?:o|os)\b',
    'memoria': r'\bmemoria(?:s)?\b',
}
EXC_CUERPO = r'tomar(?:\w*)? cuerpo|toma(?:ba|n|r)? cuerpo|tom[óo] cuerpo|cobr(?:ar|a|ó|ó) cuerpo|de cuerpo presente|cuerpo a cuerpo|cuerpo de agua|cuerpo celeste'
PALABRERIA = [
    r'\ba veces\b', r'\ben cierto modo\b', r'\bde alguna manera\b', r'\ben cierta medida\b', r'\bpor así decirlo\b',
    r'\bde algún modo\b', r'\bal fin y al cabo\b', r'\ben definitiva\b', r'\ben última instancia\b', r'\bcabe señalar\b',
    r'\bes importante\b', r'\bconstelaci[óo]n\b', r'\bmatriz\b', r'\bpalimpsesto\b', r'\btapiz\b', r'\bentramado\b',
    r'\bsin duda\b', r'\bevidentemente\b', r'\bobviamente\b', r'\bcomplej[oa]s?\b', r'\bde hecho\b', r'\bpor supuesto\b',
    r'\bde alguna forma\b', r'\bpodr[ií]a decirse\b', r'\bdigamos\b', r'\bun poco\b', r'\bsimplemente\b',
]


def partes(s, frag):
    ds, seg = plus.pieza(s, frag)
    corte = seg.find('GLOSA &middot;')
    cuerpo = seg[:corte] if corte > 0 else seg
    glosa = seg[corte:] if corte > 0 else ''
    return ds, seg, cuerpo, glosa


def visible(x):
    x = re.sub(r'<sup class="gr">\(\d+\)</sup>', '', x)
    return html.unescape(re.sub(r'<[^>]+>', '', x))


def parrafos_cuerpo(cuerpo):
    return re.findall(r'<p style="[^"]*">(.*?)</p>', cuerpo, re.S)


def solo_texto(cuerpo):
    """Párrafos y subtítulos h4 del cuerpo, sin título de pieza, marcas ni línea de RAYUELAS."""
    return '\n'.join(re.findall(r'(?:<h4[^>]*>.*?</h4>|<p style="[^"]*">.*?</p>)', cuerpo, re.S))


def entradas_glosa(glosa):
    lis = re.findall(r'<li(?: [^>]*)?>(.*?)</li>', glosa, re.S)
    return lis


def md_tabla(cab, filas):
    out = ['| ' + ' | '.join(cab) + ' |', '|' + '---|' * len(cab)]
    for f in filas:
        out.append('| ' + ' | '.join(str(c).replace('|', '/') for c in f) + ' |')
    return '\n'.join(out)


# ---------------------------------------------------------------- (i) ur y 'T'
def bloque_ur(cuerpo, glosa):
    print('## (i) «ur» en rojo y la \'T\'\n')
    filas = []
    for nombre, h in (('cuerpo', cuerpo), ('glosa', glosa)):
        h2 = re.sub(r'<span style="color:#b01a1a; font-size:0\.78em;">\(\d+\)</span>', '', h)  # número de glosa
        rojos = re.findall(ROJO + r'(.*?)</span>', h2, re.S)
        var = collections.Counter(re.sub(r'<[^>]+>', '', r) for r in rojos)
        raros = [r for r in var if not re.fullmatch(r'(?i)ur', r)]
        resto = re.sub(ROJO + r'.*?</span>', '\x00', h2, flags=re.S)
        t = visible(resto)
        sin = [m for m in re.finditer(r'(?i)ur', t)]
        ctx = [t[max(0, m.start() - 25):m.end() + 25].replace('\n', ' ') for m in sin]
        filas.append((nombre, sum(var.values()), dict(var), raros or '—', len(sin), '; '.join('…%s…' % c for c in ctx[:6]) or '—'))
    print(md_tabla(['zona', 'ur en rojo', 'variantes', 'rojos que no son «ur»', 'ur sin rojo', 'contexto'], filas))
    print()
    vis = visible(cuerpo) + ' ' + visible(glosa)
    rectas = len(re.findall(r"(?<![\w])'T'(?![\w])", vis))
    otras = {
        "‘T’ (tipográficas)": len(re.findall(r'‘T’', vis)),
        '"T" (dobles rectas)': len(re.findall(r'"T"', vis)),
        '“T” (dobles tipográficas)': len(re.findall(r'“T”', vis)),
        '«T»': len(re.findall(r'«T»', vis)),
    }
    sueltas = [vis[max(0, m.start() - 20):m.end() + 20].replace('\n', ' ') for m in re.finditer(r"(?<!['‘“\"«\w.-])T(?![\w'’”\"».-])", vis)]
    print('Comillas de la T: %d con comillas rectas simples (correcto, Norma 15); otras formas: %s; T sin comillas: %s.\n' % (
        rectas, {k: v for k, v in otras.items() if v} or 'ninguna', ('; '.join('…%s…' % c for c in sueltas[:6]) or 'ninguna')))
    if re.search(r'&#39;|&apos;', cuerpo + glosa):
        print('Nota: las comillas rectas aparecen como entidad HTML en el fuente; se leen igual.\n')


# ---------------------------------------------------------------- (ii) concordancia
def stem(w):
    w = w.lower()
    for suf in ('mente', 'ciones', 'ción', 'idades', 'idad', 'ando', 'iendo', 'aron', 'ieron', 'ados', 'adas', 'ado', 'ada', 'ían', 'ían', 'es', 's', 'a', 'o', 'e'):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[:-len(suf)]
    return w


def bloque_concordancia(frases, cuerpo_txt, W):
    print('## (ii) Concordancia de palabras\n')
    toks = []
    for i, f in enumerate(frases, 1):
        for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", f):
            if len(w) >= 4 and w.lower() not in STOP:
                toks.append((i, w))
    cnt = collections.defaultdict(list)
    forma = collections.defaultdict(collections.Counter)
    for i, w in toks:
        s = stem(w)
        cnt[s].append(i)
        forma[s][w.lower()] += 1
    filas = []
    for s, idx in sorted(cnt.items(), key=lambda x: -len(x[1])):
        if len(idx) >= 4:
            filas.append((' / '.join(sorted(forma[s], key=lambda k: -forma[s][k])[:3]), len(idx), ', '.join(map(str, idx[:14])) + ('…' if len(idx) > 14 else '')))
    print('Palabras de contenido con 4 o más casos (agrupadas por raíz aproximada), con los números de frase:\n')
    print(md_tabla(['palabra(s)', 'casos', 'frases'], filas))
    print()
    # vigiladas
    filas = []
    for nombre, pat in VIGILADAS.items():
        casos = [(i, f) for i, f in enumerate(frases, 1) if re.search(pat, f, re.I)]
        n = sum(len(re.findall(pat, f, re.I)) for _, f in casos)
        exc = [i for i, f in casos if nombre == 'cuerpo' and re.search(EXC_CUERPO, f, re.I)]
        filas.append((nombre, n, '%.0f por 10.000' % (n / W * 1e4), ', '.join(str(i) for i, _ in casos) or '—',
                      ('con excepción natural (modismo): %s' % ', '.join(map(str, exc))) if exc else '—'))
    print(md_tabla(['palabra vigilada', 'casos', 'tasa', 'frases', 'nota'], filas))
    print('\n(Norma 54: control 30 por 10.000 en «cuerpo»; Norma 49: control 40 por 10.000 en «memoria». Las excepciones físicas, anatómicas y jurídicas las juzga la lectura.)\n')
    filas = []
    for pat in PALABRERIA:
        casos = [i for i, f in enumerate(frases, 1) if re.search(pat, f, re.I)]
        if casos:
            filas.append((pat.replace('\\b', ''), len(casos), ', '.join(map(str, casos))))
    print('Palabrería vigilada (Norma 46 y Norma 36): ' + ('ninguna.' if not filas else ''))
    if filas:
        print(md_tabla(['expresión', 'casos', 'frases'], filas))
    print()


# ---------------------------------------------------------------- (iii) términos propios
def bloque_glosario(cuerpo_txt, glosa_txt):
    print('## (iii) Términos propios contra el glosario y la Norma 49\n')
    g = open(GLOSARIO, encoding='utf-8').read()
    terminos = []
    for m in re.finditer(r'^\*\*(.+?)\*\*', g, re.M):
        t = re.sub(r'\s*\(.*', '', m.group(1)).strip()
        if t and len(t) <= 40:
            terminos.append(t)
    vis = cuerpo_txt + ' ' + glosa_txt
    filas = []
    for t in dict.fromkeys(terminos):
        cs = [x for x in re.split(r'\s*[→/]\s*', t) if x]
        for c in cs:
            if len(c) < 2:
                continue
            if len(c) <= 4:
                n_exacto = len(re.findall(r"(?<![\w'-])" + re.escape(c) + r"(?![\w'-])", vis))
                n_var = 0
            else:
                n_exacto = len(re.findall(re.escape(c), vis))
                n_var = len(re.findall(re.escape(c), vis, re.I)) - n_exacto
            if n_exacto or n_var:
                filas.append((c, n_exacto, n_var if n_var else '—'))
    print(md_tabla(['término del glosario', 'casos con la grafía del glosario', 'casos con otra grafía (mayúsculas)'], filas) if filas else 'Ningún término del glosario aparece con su grafía.')
    print()
    # variantes críticas del libro
    var = []
    for pat, bien, nota in (
        (r'\burbe\b', 'URbe', 'URbe se escribe con UR en mayúsculas y «be» en minúscula (glosario)'),
        (r'\bur-?sapiens\b', 'UR-Sapiens', 'UR-Sapiens siempre con guion (18/10/26)'),
        (r'\bur-?book\b', 'UR-book', 'UR-book no pertenece a este libro (es la web): en URS se sustituye'),
        (r'\bhammurabeltz\b', 'Hammurabeltz', ''),
    ):
        for m in re.finditer(pat, vis, re.I):
            if m.group(0) != bien:
                var.append((m.group(0), bien, nota, vis[max(0, m.start() - 20):m.end() + 20].replace('\n', ' ')))
    print('Variantes de escritura de términos propios: ' + ('ninguna.' if not var else ''))
    if var:
        print(md_tabla(['aparece', 'debería', 'nota', 'contexto'], var))
    print()


# ---------------------------------------------------------------- (iv) ortografía y tipografía
def lexico_resto(s, ds, extra):
    resto = s
    i = s.find('data-s="%s"' % ds)
    if i > 0:
        a = s.rfind('<details class="pieza"', 0, i)
        d = 0
        for m in re.finditer(r'<details\b|</details>', s[a:]):
            d += 1 if m.group(0).startswith('<details') else -1
            if d == 0:
                resto = s[:a] + s[a + m.end():]
                break
    t = visible(re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', resto, flags=re.S))
    for f in extra:
        t += ' ' + open(f, encoding='utf-8', errors='ignore').read()
    c = collections.Counter(w.lower() for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", t))
    return c


def bloque_tipografia(cuerpo_txt, glosa_txt, frases, lex, minimo):
    print('## (iv) Ortografía, concordancia y tipografía\n')
    vis = cuerpo_txt + '\n' + glosa_txt
    reglas = [
        ('espacios dobles', r'(?<=\S)  +(?=\S)'),
        ('espacio antes de , . ; : ! ? ) »', r'\s[,.;:!?)»]'),
        ('falta espacio tras , ; : ! ? (sin ser cifra o hora)', r'[,;:!?](?=[A-Za-zÁÉÍÓÚÑ¿¡«])'),
        ('falta espacio tras punto entre letras (salvo siglas y URL)', r'(?<![A-Z.])[a-záéíóúñ]\.[A-ZÁÉÍÓÚÑ][a-záéíóúñ]'),
        ('comillas dobles rectas "…"', r'"'),
        ('comillas tipográficas “ ” ‘ ’', r'[“”‘’]'),
        ('tres puntos ASCII (…)', r'\.\.\.'),
        ('guion medio como raya " - "', r' - '),
        ('porcentaje sin espacio (55%)', r'\d%'),
        ('cifra de cinco o más dígitos sin punto de millar', r'(?<![\d.,])\d{5,}(?![\d.,])'),
        ('decimal con punto (3.5)', r'(?<![\d.])\d\.\d(?!\d)'),
        ('palabra repetida seguida (de de)', r'\b(\w{2,})\s+\1\b'),
        ('acentos en desuso (sólo, éste, ése, aquél)', r'\b(sólo|éste|ése|aquél|ésta|ésa|aquélla|éstos|ésos)\b'),
        ('monosílabos con tilde (fué, dió, vió, fuí)', r'\b(fué|dió|vió|fuí|guión|truhán)\b'),
        ('mayúscula tras coma o minúscula tras punto', r'(?:[a-záéíóúñ]\.\s+[a-záéíóúñ])'),
    ]
    filas = []
    for nombre, pat in reglas:
        hits = [vis[max(0, m.start() - 22):m.end() + 22].replace('\n', ' ') for m in re.finditer(pat, vis)]
        filas.append((nombre, len(hits), '; '.join('…%s…' % h for h in hits[:4]) or '—'))
    for a, b in (('«', '»'), ('(', ')'), ('¿', '?'), ('¡', '!')):
        filas.append(('signos sin cerrar %s%s' % (a, b), abs(vis.count(a) - vis.count(b)), 'abre %d, cierra %d' % (vis.count(a), vis.count(b))))
    print(md_tabla(['regla formal', 'casos', 'contexto'], filas))
    print()
    toks = collections.OrderedDict()
    for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{4,}", vis):
        if lex.get(w.lower(), 0) < minimo and w.lower() not in toks:
            toks[w.lower()] = w
    print('Léxico desconocido (palabras de 4 o más letras que no aparecen %d veces en el resto del libro): %d.\n' % (minimo, len(toks)))
    if toks:
        print(', '.join(sorted(toks.values(), key=str.lower)) + '\n')
    # concordancia de género/número elemental
    print('Concordancia elemental (determinante + sustantivo frecuente en el libro, ver lectura de Claude): sin comprobación automática más allá de las reglas de arriba.\n')


# ---------------------------------------------------------------- (v) nombres, cifras y fechas contra la glosa
def bloque_glosa(cuerpo, glosa, frases):
    print('## (v) Nombres propios, cifras y fechas del cuerpo contra la glosa\n')
    ps = parrafos_cuerpo(cuerpo)
    lis = entradas_glosa(glosa)
    glo_txt = visible(glosa)
    glo_por_n = {}
    for l in lis:
        m = re.search(r'\((\d+)\)', visible(l))
        if m:
            glo_por_n[int(m.group(1))] = visible(l)
    filas = []
    for k, p in enumerate(ps, 1):
        llamadas = [int(x) for x in re.findall(r'<sup class="gr">\((\d+)\)</sup>', p)]
        t = visible(p)
        # nombres: secuencias capitalizadas que no abren frase
        nombres = []
        for f in re.split(r'(?<=[.!?:;])\s+', t):
            f = f.strip()
            if not f:
                continue
            ws = list(re.finditer(r"[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑáéíóúñ.'-]*(?:\s+(?:de|del|la|las|los|y|of|the|and|from)\s+[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑáéíóúñ.'-]*|\s+[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑáéíóúñ.'-]*)*", f))
            for m in ws:
                w = m.group(0).strip('.,;:')
                if m.start() == 0 or f[:m.start()].strip('«¿¡ ') == '':
                    w = ' '.join(w.split()[1:])  # la primera palabra de frase no cuenta como nombre
                    w = re.sub(r'^(?:de|del|la|las|los|y|of|the|and|from)\s+', '', w)
                if not w or w.upper() in ('UR', 'T') or len(w) < 3:
                    continue
                nombres.append(w)
        cifras = [c.strip('.,') for c in re.findall(r'(?<![\w.])\d[\d.,]*(?: %)?', t)]
        for tok in dict.fromkeys(nombres + cifras):
            enGlosa = tok.lower() in glo_txt.lower()
            enSuya = any(tok.lower() in glo_por_n.get(n, '').lower() for n in llamadas)
            estado = 'en su entrada' if enSuya else ('en otra entrada' if enGlosa else 'SIN GLOSA')
            filas.append((k, tok, ','.join(map(str, llamadas)) or '—', estado))
    sin = [f for f in filas if f[3] == 'SIN GLOSA']
    print('Párrafos del cuerpo: %d. Nombres propios y cifras detectados: %d. Con respaldo en su entrada: %d; en otra entrada: %d; sin glosa: %d.\n' % (
        len(ps), len(filas), sum(1 for f in filas if f[3] == 'en su entrada'), sum(1 for f in filas if f[3] == 'en otra entrada'), len(sin)))
    if sin:
        print(md_tabla(['párrafo', 'nombre o cifra', 'llamadas del párrafo', 'estado'], sin))
        print()
    fuera = [f for f in filas if f[3] == 'en otra entrada']
    if fuera:
        print('En otra entrada (revisar si la llamada debería ir ahí):\n')
        print(md_tabla(['párrafo', 'nombre o cifra', 'llamadas del párrafo', 'estado'], fuera))
        print()
    # cabeceras de la glosa contra el cuerpo
    cu = visible(cuerpo).lower()
    filas = []
    for l in lis:
        h = re.search(r'<strong>(.*?)</strong>', l, re.S)
        if h:
            cab = visible(h.group(1)).strip()
            base = re.sub(r'\s*\(.*', '', cab)
            ok = any(x.lower() in cu for x in re.split(r'\s+y\s+|/', base) if len(x) > 3) or base.lower() in cu
            if not ok:
                filas.append((cab,))
    print('Cabeceras de la glosa que no aparecen en el cuerpo (Norma 18): ' + ('ninguna.' if not filas else ''))
    if filas:
        print(md_tabla(['cabecera'], filas))
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pieza')
    ap.add_argument('--lexico', nargs='*', default=[])
    ap.add_argument('--minimo', type=int, default=2)
    a = ap.parse_args()
    s = open(HTML, encoding='utf-8').read()
    ds, seg, cuerpo, glosa = partes(s, a.pieza)
    ps = [plus.limpia(p) for p in parrafos_cuerpo(cuerpo)]
    frases = []
    for p in ps:
        frases += plus.frases(p)
    W = sum(len(p.split()) for p in ps)
    print('# Relojero-Plus Ultra · palabra por palabra · %s\n' % ds[:70])
    print('Cuerpo: %d palabras, %d frases, %d párrafos. Glosa: %d entradas.\n' % (W, len(frases), len(ps), len(entradas_glosa(glosa))))
    cuerpo_solo = solo_texto(cuerpo)
    bloque_ur(cuerpo_solo, glosa)
    bloque_concordancia(frases, ' '.join(ps), W)
    cuerpo_txt, glosa_txt = visible(cuerpo_solo), visible(glosa)
    bloque_glosario(cuerpo_txt, glosa_txt)
    lex = lexico_resto(s, ds, a.lexico)
    bloque_tipografia(cuerpo_txt, glosa_txt, frases, lex, a.minimo)
    bloque_glosa(cuerpo, glosa, frases)


if __name__ == '__main__':
    main()
