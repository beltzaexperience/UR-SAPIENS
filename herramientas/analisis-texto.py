#!/usr/bin/env python3
"""Marco de análisis textual de UR (MARCO-ANALISIS-TEXTUAL.md): los 18 análisis en cuatro dimensiones.

Mide, con un analizador sintáctico del español (spaCy), los rasgos automatizables de
cada una de las 18 familias de análisis y compara cada pieza de URS con el corredor del
canon (Baroja, Orwell) y con el pico licenciado (Martín Santos). Complementa a
`perfil-corpus.py` (que mide los indicadores de la Norma 36.8 y los de puntuación y ritmo).

Requisitos (instalación única):
    pip install spacy numpy
    pip install https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.7.0/es_core_news_md-3.7.0-py3-none-any.whl
Los textos de las obras (PDF o TXT) no se incluyen en el repositorio.

Uso:
    python3 herramientas/analisis-texto.py --html urtz.html \\
        --obra baroja_aurora=/ruta/aurora.pdf --hyph baroja_aurora ... \\
        --obra martin_santos=/ruta/tiempo.pdf --aparte martin_santos \\
        [--ventana 1000] [--cache datos.pkl] [--matriz] [--pieza TEXTO] [--delta] [--dospuntos]

  --ventana N   palabras por ventana de medida (por defecto 1000; canon y UR igual).
  --cache F     guarda/lee las medidas ya calculadas (no guarda texto), para repetir en segundos.
  --matriz      lista las piezas de URS por indicadores dentro del corredor.
  --pieza T     detalle de las piezas cuyo título contenga T.
  --delta       estilometría (Delta de Burrows): obra más cercana de cada pieza y piezas atípicas.
  --dospuntos   clasifica los dos puntos (cita, rótulo, enumeración, complemento, cláusula + cláusula) en el canon y en UR,
                separando las piezas teóricas del resto, con ejemplos de UR (apoya la norma de los dos puntos).

Cautelas: el analizador es estadístico y comete errores en prosa literaria y en los
neologismos de UR; sirve para comparar masas de texto con el mismo instrumento, no para
juzgar una frase. La perplejidad (qué predecible es la palabra siguiente) exige un modelo
de lenguaje y no se calcula; se mide en su lugar la ráfaga y la repetición de plantillas.
"""
import argparse
import collections
import importlib.util
import math
import os
import pickle
import re
import statistics as st
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def _carga(nombre, fichero):
    spec = importlib.util.spec_from_file_location(nombre, os.path.join(AQUI, fichero))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pc = _carga('pc', 'perfil-corpus.py')
wc = pc.wc
pct = pc.pct

VOC = 'aeiouáéíóúü'
FUERTES = 'aeoáéóíú'  # í y ú acentuadas rompen diptongo
DEBILES = 'iuü'
CONTENIDO = {'NOUN', 'VERB', 'ADJ', 'ADV', 'PROPN'}
# Indicadores de alarma de la matriz de piezas y dirección en que dan la alarma (el resto es descriptivo:
# tiempos y personas verbales, tipos de entidad y recursos dependen del registro, no de un defecto).
ALARMA = {'suj_art_sust': '↑', 'suj_abstracto_art': '↑', 'suj_pronombre': '↓', 'suj_omitido': '↓', 'm_sust': '↑', 'm_verbo': '↓',
          'm_pron': '↓', 's_sub_frase': '↓', 's_fin_frase': '↓', 'q_esqueleto': '↑', 'q_apertura2': '↑', 'e_anafora': '↑',
          'e_parent': '↑', 'r_cv': '↓', 'f_sil_sd': '↓', 'l_densidad': '↑', 'g_total': '↓'}
# Piezas teóricas según la Norma 36.8 (pendiente de confirmar por Luis).
TEORICAS = ('I ·', 'II ·', 'III ·', 'IV ·', 'DIGITALISMO', 'ANTROPOLOGÍA RACIAL')
ABS = re.compile(r'(ción|sión|dad|tud|miento|ncia|ismo|aje)$')


# ---------- fonética: sílabas, acento, asonancia ----------
def nucleos(palabra):
    """Lista de núcleos silábicos (cadenas de vocales) de una palabra, rompiendo hiatos."""
    w = re.sub(r'(?<=[qg])u(?=[eiéí])', '', palabra.lower())
    out = []
    for g in re.findall(r'[aeiouáéíóúü]+', w):
        cur = g[0]
        for c in g[1:]:
            prev = cur[-1]
            if (prev in FUERTES and c in FUERTES) or prev in 'íú' or c in 'íú':
                out.append(cur)
                cur = c
            else:
                cur += c
        out.append(cur)
    return out


def acento(palabra, nu):
    """Índice del núcleo tónico."""
    if len(nu) <= 1:
        return 0
    for i, n in enumerate(nu):
        if re.search(r'[áéíóú]', n):
            return i
    w = palabra.lower()
    if re.search(r'[aeiouns]$', w):
        return max(0, len(nu) - 2)
    return len(nu) - 1


def clave_asonante(palabra):
    nu = nucleos(palabra)
    if len(nu) < 2:
        return None
    t = acento(palabra, nu)
    quita = str.maketrans('áéíóúü', 'aeiouu')

    def vocal(n):
        n = n.translate(quita)
        f = [c for c in n if c in 'aeo']
        return f[0] if f else n[-1]
    return ''.join(vocal(n) for n in nu[t:])


# ---------- medida de una ventana (lista de documentos spaCy, uno por párrafo) ----------
def morf(tok, k):
    v = tok.morph.get(k)
    return v[0] if v else None


def medir_ventana(docs):
    toks = [t for d in docs for t in d if not t.is_space]
    pal = [t for t in toks if not t.is_punct]
    W = len(pal)
    if W < 300:
        return None
    sents = [s for d in docs for s in d.sents]
    sents = [s for s in sents if sum(1 for t in s if not t.is_punct) >= 2]
    NS = len(sents)
    r = {}
    per100 = lambda n: 100.0 * n / W
    per1000 = lambda n: 1000.0 * n / W
    per10k = lambda n: 10000.0 * n / W

    # 2 · morfología
    cnt = collections.Counter(t.pos_ for t in pal)
    for k, nombre in [('NOUN', 'm_sust'), ('VERB', 'm_verbo'), ('ADJ', 'm_adj'), ('ADV', 'm_adv'), ('ADP', 'm_prep'),
                      ('DET', 'm_det'), ('PRON', 'm_pron'), ('CCONJ', 'm_ccon'), ('SCONJ', 'm_scon'), ('PROPN', 'm_propn'), ('NUM', 'm_num')]:
        r[nombre] = per100(cnt[k])
    r['m_verbo'] += per100(cnt['AUX'])
    r['m_adj_x_sust'] = cnt['ADJ'] / max(1, cnt['NOUN'])
    fin = [t for t in pal if t.pos_ in ('VERB', 'AUX') and 'Fin' in t.morph.get('VerbForm')]
    nf = max(1, len(fin))
    tiempos = collections.Counter(morf(t, 'Tense') for t in fin)
    modos = collections.Counter(morf(t, 'Mood') for t in fin)
    pers = collections.Counter(morf(t, 'Person') for t in fin)
    r['t_pres'] = 100.0 * tiempos['Pres'] / nf
    r['t_pasado'] = 100.0 * (tiempos['Past'] + tiempos['Imp']) / nf
    r['t_pret'] = 100.0 * tiempos['Past'] / nf
    r['t_imp'] = 100.0 * tiempos['Imp'] / nf
    r['t_fut'] = 100.0 * tiempos['Fut'] / nf
    r['t_cond'] = 100.0 * modos['Cnd'] / nf
    r['t_subj'] = 100.0 * modos['Sub'] / nf
    r['p_1'] = 100.0 * pers['1'] / nf
    r['p_2'] = 100.0 * pers['2'] / nf
    r['p_3'] = 100.0 * pers['3'] / nf
    r['v_fin_100'] = per100(len(fin))
    r['v_inf'] = per100(sum(1 for t in pal if 'Inf' in t.morph.get('VerbForm')))
    r['v_part'] = per100(sum(1 for t in pal if 'Part' in t.morph.get('VerbForm') and t.pos_ == 'VERB'))
    r['v_imper'] = per10k(sum(1 for t in pal if 'Imp' in t.morph.get('Mood')))

    # 3 · sintaxis
    prof, dd, subs, sinfin, finpf = [], [], 0, 0, 0
    sujetos = collections.Counter()
    ger = collections.Counter()
    pasivas = 0
    for s in sents:
        tk = [t for t in s if not t.is_punct]
        if not tk:
            continue
        mx = 0
        for t in tk:
            d, x = 0, t
            while x.head.i != x.i and d < 60:
                x = x.head
                d += 1
            mx = max(mx, d)
            dd.append(abs(t.i - t.head.i))
        prof.append(mx)
        finv = [t for t in tk if t.pos_ in ('VERB', 'AUX') and 'Fin' in t.morph.get('VerbForm')]
        finpf += len(finv)
        if not finv:
            sinfin += 1
        subs += sum(1 for t in tk if t.dep_ in ('advcl', 'ccomp', 'csubj', 'acl', 'acl:relcl', 'xcomp'))
        pasivas += sum(1 for t in tk if t.dep_ in ('nsubj:pass', 'expl:pass'))
        root = [t for t in s if t.dep_ == 'ROOT']
        if root:
            ro = root[0]
            sj = [c for c in ro.children if c.dep_ in ('nsubj', 'nsubj:pass')]
            if not sj:
                sujetos['omitido' if ro.pos_ in ('VERB', 'AUX') and 'Fin' in ro.morph.get('VerbForm') else 'sin_verbo'] += 1
            else:
                h = sj[0]
                if h.pos_ == 'PRON':
                    sujetos['pronombre'] += 1
                elif h.pos_ == 'PROPN':
                    sujetos['propio'] += 1
                else:
                    art = any(c.dep_ == 'det' and c.pos_ == 'DET' and c.i < h.i and c.lower_ in ('el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas') for c in h.children)
                    sujetos['abstracto_art' if (art and ABS.search(h.lower_)) else ('art_sust' if art else 'sust_sin_art')] += 1
        for t in tk:
            if 'Ger' in t.morph.get('VerbForm') and t.pos_ in ('VERB', 'AUX'):
                coma = t.i > 0 and t.doc[t.i - 1].text == ','
                if t.dep_ == 'advcl' or t.dep_ == 'xcomp' and t.head.pos_ == 'VERB' and t.head.lemma_ not in ('estar', 'ir', 'seguir', 'llevar', 'andar', 'venir', 'quedar'):
                    if t.i > t.head.i:
                        ger['posterior_coma' if coma else 'posterior_sin_coma'] += 1
                    else:
                        ger['anteposicion'] += 1
                elif t.dep_ in ('aux', 'xcomp') or t.head.lemma_ in ('estar', 'ir', 'seguir', 'llevar', 'andar', 'venir', 'quedar'):
                    ger['perifrasis'] += 1
                else:
                    ger['otro'] += 1
    nm = max(1, sum(sujetos.values()))
    r['s_prof'] = st.mean(prof) if prof else 0
    r['s_dist'] = st.mean(dd) if dd else 0
    r['s_fin_frase'] = finpf / max(1, NS)
    r['s_sub_frase'] = subs / max(1, NS)
    r['s_sin_verbo'] = 100.0 * sinfin / max(1, NS)
    r['s_pasiva'] = per1000(pasivas)
    for k in ('pronombre', 'propio', 'art_sust', 'sust_sin_art', 'abstracto_art', 'omitido', 'sin_verbo'):
        r['suj_' + k] = 100.0 * sujetos[k] / nm
    r['g_total'] = per10k(sum(ger.values()))
    for k in ('posterior_coma', 'posterior_sin_coma', 'anteposicion', 'perifrasis', 'otro'):
        r['g_' + k] = per10k(ger[k])

    # 4 · lexicometría
    low = [t.lower_ for t in pal if t.is_alpha]
    cont = [t for t in pal if t.pos_ in CONTENIDO]
    r['l_densidad'] = per100(len(cont))
    wv = 500
    if len(low) >= wv:
        v = [len(set(low[i:i + wv])) / wv for i in range(0, len(low) - wv + 1, 100)]
        r['l_mattr'] = st.mean(v)
    cl = collections.Counter(low)
    r['l_hapax'] = 100.0 * sum(1 for w, n in cl.items() if n == 1) / max(1, len(cl))
    lem = [t.lemma_.lower() for t in cont]
    rep = 0
    for i, lm in enumerate(lem):
        if lm in lem[max(0, i - 50):i]:
            rep += 1
    r['l_repite50'] = 100.0 * rep / max(1, len(lem))
    top = collections.Counter(lem).most_common(10)
    r['l_top10'] = 100.0 * sum(n for _, n in top) / max(1, len(lem))
    r['l_abstractos'] = per100(sum(1 for t in pal if t.pos_ == 'NOUN' and ABS.search(t.lower_)))

    # 5 · cohesión
    conj = [set(t.lemma_.lower() for t in s if t.pos_ in ('NOUN', 'PROPN', 'VERB', 'ADJ') and not t.is_stop) for s in sents]
    ov, sin = [], 0
    for a, b in zip(conj, conj[1:]):
        if a and b:
            j = len(a & b) / len(a | b)
            ov.append(j)
            if not (a & b):
                sin += 1
    r['c_solape'] = 100.0 * st.mean(ov) if ov else 0
    r['c_sin_enlace'] = 100.0 * sin / max(1, len(ov))
    texto = ' '.join(d.text for d in docs)
    cn = lambda rx: len(re.findall(rx, texto, flags=re.I))
    r['c_demostr'] = per1000(cn(r'\b(este|esta|estos|estas|esto|ese|esa|esos|esas|eso|aquel|aquella|aquellos|aquellas)\b'))
    r['c_aditivo'] = per1000(cn(r'\b(además|también|asimismo|incluso|tampoco|igualmente)\b'))
    r['c_consec'] = per1000(cn(r'\b(así|entonces|por eso|por tanto|por lo tanto|de ahí|de modo que|de manera que)\b'))
    r['c_temporal'] = per1000(cn(r'\b(luego|después|antes|mientras|cuando|ya|todavía|aún|hoy|ahora)\b'))
    r['c_sujeto_igual'] = 0.0
    sj_prev, igual, tot = None, 0, 0
    for s in sents:
        ro = [t for t in s if t.dep_ == 'ROOT']
        h = None
        if ro:
            for c in ro[0].children:
                if c.dep_ in ('nsubj', 'nsubj:pass'):
                    h = c.lemma_.lower()
        if h and sj_prev:
            tot += 1
            if h == sj_prev:
                igual += 1
        sj_prev = h or sj_prev
    r['c_sujeto_igual'] = 100.0 * igual / max(1, tot)

    # 9 · legibilidad (Fernández Huerta, Szigriszt-Pazos)
    sil = sum(len(nucleos(t.text)) for t in pal if t.is_alpha)
    wa = max(1, sum(1 for t in pal if t.is_alpha))
    P = 100.0 * sil / wa
    F = 100.0 * NS / wa
    r['x_huerta'] = 206.84 - 0.60 * P - 1.02 * F
    r['x_szigriszt'] = 206.835 - 62.3 * (sil / wa) - (wa / max(1, NS))
    r['x_sil_pal'] = sil / wa
    r['x_poli'] = 100.0 * sum(1 for t in pal if t.is_alpha and len(nucleos(t.text)) >= 4) / wa

    # 1 · fonética
    ls = []
    for s in sents:
        ls.append(sum(len(nucleos(t.text)) for t in s if t.is_alpha))
    r['f_sil_frase'] = st.mean(ls) if ls else 0
    r['f_sil_sd'] = st.pstdev(ls) if len(ls) > 1 else 0
    fin_ac = collections.Counter()
    claves = []
    for s in sents:
        ws = [t for t in s if t.is_alpha]
        if ws:
            w = ws[-1].text
            nu = nucleos(w)
            if len(nu) >= 2:
                a = acento(w, nu)
                fin_ac['aguda' if a == len(nu) - 1 else ('llana' if a == len(nu) - 2 else 'esdrujula')] += 1
            claves.append(clave_asonante(w))
    nfa = max(1, sum(fin_ac.values()))
    r['f_fin_aguda'] = 100.0 * fin_ac['aguda'] / nfa
    r['f_fin_esdr'] = 100.0 * fin_ac['esdrujula'] / nfa
    pares = [(a, b) for a, b in zip(claves, claves[1:]) if a and b]
    r['f_asonancia'] = 100.0 * sum(1 for a, b in pares if a == b) / max(1, len(pares))
    # aliteración: palabras de contenido consecutivas (hasta dos de distancia) con la misma consonante inicial
    cw = [t.lower_ for t in pal if t.pos_ in CONTENIDO and t.is_alpha]
    al = sum(1 for i in range(len(cw) - 2) for j in (1, 2) if cw[i][0] == cw[i + j][0] and cw[i][0] not in VOC)
    r['f_aliteracion'] = per100(al)

    # 8 · retórica
    r['e_preg'] = per10k(texto.count('¿'))
    r['e_excl'] = per10k(texto.count('¡'))
    r['e_parent'] = per10k(texto.count('('))
    r['e_raya'] = per10k(len(re.findall(r'[—–]', texto)))
    ap1 = []
    for s in sents:
        tk = [t for t in s if not t.is_punct]
        if tk:
            ap1.append(tk[0].lower_)
    r['e_anafora'] = 100.0 * sum(1 for a, b in zip(ap1, ap1[1:]) if a == b) / max(1, len(ap1) - 1)

    # 16 · entidades
    ents = [e for d in docs for e in d.ents]
    r['n_ent'] = per100(len(ents))
    for lab, nom in (('PER', 'n_per'), ('LOC', 'n_loc'), ('ORG', 'n_org'), ('MISC', 'n_misc')):
        r[nom] = per100(sum(1 for e in ents if e.label_ == lab))
    r['n_frases_ent'] = 100.0 * sum(1 for s in sents if s.ents or re.search(r'\b\d{2,}\b', s.text)) / max(1, NS)
    r['n_cifras'] = per100(len(re.findall(r'\b\d[\d.,]*\b', texto)))

    # 17 · ráfaga ; 18 · plantillas
    L = [sum(1 for t in s if not t.is_punct) for s in sents]
    r['r_cv'] = (st.pstdev(L) / st.mean(L)) if L and st.mean(L) else 0
    r['r_saltos'] = (st.mean(abs(a - b) for a, b in zip(L, L[1:])) / st.mean(L)) if len(L) > 1 and st.mean(L) else 0
    g4 = [tuple(low[i:i + 4]) for i in range(len(low) - 3)]
    c4 = collections.Counter(g4)
    r['q_4gram'] = 100.0 * sum(n for n in c4.values() if n >= 2) / max(1, len(g4))
    esq = collections.Counter()
    for s in sents:
        tk = [t for t in s if not t.is_punct][:4]
        if len(tk) == 4:
            esq[tuple(t.pos_ for t in tk)] += 1
    ne = max(1, sum(esq.values()))
    r['q_esqueleto'] = 100.0 * sum(n for n in esq.values() if n >= 4) / ne
    ap2 = collections.Counter(tuple(t.lower_ for t in [x for x in s if not x.is_punct][:2]) for s in sents)
    r['q_apertura2'] = 100.0 * sum(n for k, n in ap2.items() if n >= 3 and len(k) == 2) / max(1, NS)
    r['q_dospuntos_sub'] = per1000(texto.count(':'))
    return r, low


# ---------- estructura de datos y comparación ----------
GRUPOS = [
    ('1 · Fonético y fonológico', [
        ('f_sil_frase', 'sílabas por frase (media)'), ('f_sil_sd', 'sílabas por frase (desviación)'),
        ('f_fin_aguda', '% de frases que acaban en palabra aguda'), ('f_fin_esdr', '% de frases que acaban en esdrújula'),
        ('f_asonancia', '% de frases que riman en asonante con la anterior'), ('f_aliteracion', 'aliteración (pares por 100 palabras)')]),
    ('2 · Morfológico', [
        ('m_sust', 'sustantivos por 100 palabras'), ('m_verbo', 'verbos por 100 palabras'), ('m_adj', 'adjetivos por 100'),
        ('m_adv', 'adverbios por 100'), ('m_prep', 'preposiciones por 100'), ('m_det', 'determinantes por 100'),
        ('m_pron', 'pronombres por 100'), ('m_ccon', 'conjunciones coordinantes por 100'), ('m_scon', 'conjunciones subordinantes por 100'),
        ('m_propn', 'nombres propios por 100'), ('m_adj_x_sust', 'adjetivos por sustantivo'),
        ('t_pres', '% de verbos finitos en presente'), ('t_pasado', '% en pasado (pretérito + imperfecto)'), ('t_fut', '% en futuro'),
        ('t_cond', '% en condicional'), ('t_subj', '% en subjuntivo'), ('p_1', '% en primera persona'), ('p_3', '% en tercera persona'),
        ('v_inf', 'infinitivos por 100'), ('v_part', 'participios por 100')]),
    ('3 · Sintáctico', [
        ('s_prof', 'profundidad máxima del árbol (media por frase)'), ('s_dist', 'distancia media de dependencia'),
        ('s_fin_frase', 'verbos finitos por frase'), ('s_sub_frase', 'subordinadas por frase'), ('s_sin_verbo', '% de frases sin verbo finito'),
        ('s_pasiva', 'pasivas por 1.000 palabras'),
        ('suj_propio', 'sujeto principal: % nombre propio'), ('suj_pronombre', 'sujeto principal: % pronombre'),
        ('suj_art_sust', 'sujeto principal: % artículo + sustantivo'), ('suj_abstracto_art', 'sujeto principal: % artículo + abstracto'),
        ('suj_sust_sin_art', 'sujeto principal: % sustantivo sin artículo'), ('suj_omitido', 'sujeto principal: % omitido'),
        ('g_total', 'gerundios por 10.000'), ('g_posterior_coma', 'gerundio tras coma y tras su verbo (candidato Norma 10) por 10.000'),
        ('g_posterior_sin_coma', 'gerundio posterior sin coma por 10.000'), ('g_anteposicion', 'gerundio antepuesto por 10.000'),
        ('g_perifrasis', 'gerundio en perífrasis (estar, ir, seguir…) por 10.000'), ('g_otro', 'otros gerundios por 10.000')]),
    ('4 · Léxico', [
        ('l_densidad', 'densidad léxica (% de palabras de contenido)'), ('l_mattr', 'diversidad léxica (MATTR 500)'),
        ('l_hapax', '% de palabras distintas que aparecen una vez'), ('l_repite50', '% de palabras de contenido que repiten otra de las 50 anteriores'),
        ('l_top10', '% de las palabras de contenido que son las 10 más usadas'), ('l_abstractos', 'abstractos (-ción, -dad…) por 100')]),
    ('5 · Textualidad', [
        ('c_solape', 'solape léxico con la frase anterior (%)'), ('c_sin_enlace', '% de frases sin ninguna palabra en común con la anterior'),
        ('c_sujeto_igual', '% de frases con el mismo sujeto que la anterior'), ('c_demostr', 'demostrativos por 1.000'),
        ('c_aditivo', 'conectores aditivos por 1.000'), ('c_consec', 'conectores consecutivos por 1.000'), ('c_temporal', 'marcadores temporales por 1.000')]),
    ('8 · Estilístico (recursos)', [
        ('e_preg', 'preguntas retóricas (¿) por 10.000'), ('e_excl', 'exclamaciones (¡) por 10.000'), ('e_parent', 'paréntesis por 10.000'),
        ('e_raya', 'rayas por 10.000'), ('e_anafora', '% de frases que abren con la misma palabra que la anterior')]),
    ('9 · Legibilidad', [
        ('x_huerta', 'Fernández Huerta'), ('x_szigriszt', 'Szigriszt-Pazos (INFLESZ)'), ('x_sil_pal', 'sílabas por palabra'), ('x_poli', '% de palabras de 4+ sílabas')]),
    ('10 · Pragmática y 13 · Narratología (marcadores)', [
        ('v_imper', 'imperativos por 10.000'), ('p_2', '% de verbos en segunda persona')]),
    ('16 · Entidades', [
        ('n_ent', 'entidades por 100 palabras'), ('n_per', 'personas por 100'), ('n_loc', 'lugares por 100'), ('n_org', 'organizaciones por 100'),
        ('n_misc', 'otras entidades por 100'), ('n_frases_ent', '% de frases con entidad o cifra'), ('n_cifras', 'cifras por 100 palabras')]),
    ('17 · Ráfaga y 18 · Plantillas', [
        ('r_cv', 'ráfaga: coeficiente de variación de la longitud de frase'), ('r_saltos', 'ráfaga: salto medio entre frases consecutivas / longitud media'),
        ('q_4gram', '% de secuencias de 4 palabras que se repiten'), ('q_esqueleto', '% de frases con esqueleto gramatical repetido (≥4 veces)'),
        ('q_apertura2', '% de frases cuyas dos primeras palabras se repiten (≥3 veces)')]),
]
CLAVES = [k for _, g in GRUPOS for k, _ in g]
NOMBRES = {k: n for _, g in GRUPOS for k, n in g}


def ventanas(paras, n):
    out, cur, w = [], [], 0
    for p in paras:
        cur.append(p)
        w += wc(p)
        if w >= n:
            out.append(cur)
            cur, w = [], 0
    if cur and w >= min(0.7 * n, 450):  # la última ventana corta se conserva si llega a 450 palabras (la pieza más breve de URS)
        out.append(cur)
    return out


def cargar_nlp():
    try:
        import spacy
    except ImportError:
        sys.exit('Falta spaCy: pip install spacy numpy  y el modelo es_core_news_md (ver cabecera).')
    try:
        return spacy.load('es_core_news_md')
    except OSError:
        sys.exit('Falta el modelo: pip install https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.7.0/es_core_news_md-3.7.0-py3-none-any.whl')


def medir_texto(paras, nlp, n):
    """Mide cada ventana de n palabras; devuelve (lista de dicts, lista de listas de palabras minúsculas)."""
    res, lows = [], []
    for v in ventanas(paras, n):
        docs = list(nlp.pipe(v, batch_size=64))
        m = medir_ventana(docs)
        if m:
            res.append(m[0])
            lows.append(m[1])
    return res, lows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--obra', action='append', required=True)
    ap.add_argument('--hyph', action='append', default=[])
    ap.add_argument('--aparte', action='append', default=[])
    ap.add_argument('--html', default='urtz.html')
    ap.add_argument('--ventana', type=int, default=1000)
    ap.add_argument('--cache')
    ap.add_argument('--matriz', action='store_true')
    ap.add_argument('--pieza')
    ap.add_argument('--delta', action='store_true')
    ap.add_argument('--dospuntos', action='store_true')
    a = ap.parse_args()

    if a.dospuntos:
        dospuntos(a)
        return
    if a.cache and os.path.exists(a.cache):
        datos = pickle.load(open(a.cache, 'rb'))
    else:
        nlp = cargar_nlp()
        datos = {'obras': {}, 'ur': {}, 'mfw_low': {}}
        for kv in a.obra:
            k, ruta = kv.split('=', 1)
            P = pc.parrafos(pc.leer(ruta), k in a.hyph)
            narr = [p for p in P if not pc.es_dialogo(p, k in a.hyph)]
            datos['obras'][k], datos['mfw_low'][k] = medir_texto(narr, nlp, a.ventana)
            print('%-18s %d ventanas' % (k, len(datos['obras'][k])), file=sys.stderr)
        for t, paras in pc.piezas_urs(a.html):
            if sum(wc(p) for p in paras) < 450:
                continue
            r, lows = medir_texto(paras, nlp, a.ventana)
            if r:
                datos['ur'][t], datos['mfw_low'][t] = r, lows
        if a.cache:
            pickle.dump(datos, open(a.cache, 'wb'))
    obras, ur = datos['obras'], datos['ur']
    canon = [k for k in obras if k not in a.aparte]
    cols = list(obras)
    pool = {k: [w[k] for c in canon for w in obras[c] if k in w] for k in CLAVES}
    urv = {k: [w[k] for t in ur for w in ur[t] if k in w] for k in CLAVES}
    print('Ventanas de %d palabras: canon %d, UR %d (66 piezas)' % (a.ventana, sum(len(obras[c]) for c in canon), sum(len(v) for v in ur.values())))
    corr = {}
    for titulo, grupo in GRUPOS:
        print('\n## ' + titulo)
        print('%-62s' % 'indicador (mediana de ventanas)', *['%9s' % c[:9] for c in cols], '| corredor p10 p50 p90 | UR p10 p50 p90 | UR fuera: <p10 >p90 (% ventanas)')
        for k, n in grupo:
            if not pool[k]:
                continue
            lo, md, hi = pct(pool[k], 10), pct(pool[k], 50), pct(pool[k], 90)
            corr[k] = (lo, hi)
            u = urv[k]
            fila = [st.median([w[k] for w in obras[c] if k in w]) for c in cols]
            print('%-62s' % n[:62], *['%9.1f' % x for x in fila], '| %7.1f %7.1f %7.1f | %7.1f %7.1f %7.1f | %3.0f %3.0f' % (
                lo, md, hi, pct(u, 10), pct(u, 50), pct(u, 90), 100.0 * sum(1 for x in u if x < lo) / len(u), 100.0 * sum(1 for x in u if x > hi) / len(u)))

    if a.matriz or a.pieza:
        print('\nPIEZAS: indicadores de alarma (%d) fuera del corredor, en la dirección de la alarma (media de las ventanas de la pieza)' % len(ALARMA))
        filas = []
        for t, ws in ur.items():
            fuera = []
            for k, d in ALARMA.items():
                if k not in corr:
                    continue
                v = st.mean(w[k] for w in ws if k in w)
                if (d == '↑' and v > corr[k][1]) or (d == '↓' and v < corr[k][0]):
                    fuera.append(k + d)
            filas.append((len(fuera), t, fuera))
        filas.sort(key=lambda x: (x[0], x[1]))
        for n, t, fuera in filas:
            if a.matriz or (a.pieza and a.pieza.lower() in t.lower()):
                print('%2d de %d  %-60s %s' % (n, len(ALARMA), t[:60], ' '.join(fuera)))

    if a.delta:
        delta(datos, canon, a)


def _fin(toks):
    return any(t.pos_ in ('VERB', 'AUX') and 'Fin' in t.morph.get('VerbForm') for t in toks)


def clase_dospuntos(t):
    """Clase de un signo ':' (token spaCy)."""
    doc, i = t.doc, t.i
    s = t.sent
    if 0 < i < len(doc) - 1 and doc[i - 1].like_num and doc[i + 1].like_num:
        return None
    antes = [x for x in doc[s.start:i] if not x.is_punct]
    despues = list(doc[i + 1:s.end])
    sig = doc[i + 1].text if i + 1 < len(doc) else ''
    if sig in ('«', '"', '“', '—', '–'):
        return 'cita'
    if len(antes) <= 3 and not _fin(antes):
        return 'rótulo'
    fa, fd = _fin(antes), _fin(despues)
    comas = sum(1 for x in despues if x.text == ',')
    if not fd:
        return 'enumeración' if comas >= 2 else 'complemento (aposición o lista corta)'
    if fa:
        return 'cláusula + cláusula'
    return 'rótulo largo + cláusula'


def dospuntos(a):
    nlp = cargar_nlp()
    conteo = collections.defaultdict(collections.Counter)
    ejemplos = collections.defaultdict(list)
    palabras = collections.Counter()
    for kv in a.obra:
        k, ruta = kv.split('=', 1)
        P = pc.parrafos(pc.leer(ruta), k in a.hyph)
        narr = [p for p in P if not pc.es_dialogo(p, k in a.hyph)]
        palabras[k] = sum(wc(p) for p in narr)
        for d in nlp.pipe([p for p in narr if ':' in p], batch_size=64):
            for t in d:
                if t.text == ':':
                    c = clase_dospuntos(t)
                    if c:
                        conteo[k][c] += 1
    for t, paras in pc.piezas_urs(a.html):
        if sum(wc(p) for p in paras) < 450:
            continue
        grupo = 'UR teóricas' if t.upper().startswith(TEORICAS) else 'UR resto'
        palabras[grupo] += sum(wc(p) for p in paras)
        for d in nlp.pipe([p for p in paras if ':' in p], batch_size=64):
            for tk in d:
                if tk.text == ':':
                    c = clase_dospuntos(tk)
                    if c:
                        conteo[grupo][c] += 1
                        if len(ejemplos[(grupo, c)]) < 40:
                            ejemplos[(grupo, c)].append(d.text[max(0, tk.idx - 90):tk.idx + 90].replace('\n', ' '))
    clases = ['cláusula + cláusula', 'complemento (aposición o lista corta)', 'enumeración', 'cita', 'rótulo', 'rótulo largo + cláusula']
    cols = [k for k in palabras]
    print('Dos puntos por clase, por 1.000 palabras de narración (entre paréntesis, nº de casos)')
    print('%-40s' % '', *['%16s' % c[:16] for c in cols])
    for c in clases:
        print('%-40s' % c, *['%9.2f (%4d)' % (1000.0 * conteo[k][c] / max(1, palabras[k]), conteo[k][c]) for k in cols])
    print('%-40s' % 'TOTAL', *['%9.2f (%4d)' % (1000.0 * sum(conteo[k].values()) / max(1, palabras[k]), sum(conteo[k].values())) for k in cols])
    import random
    random.seed(7)
    for grupo in ('UR resto', 'UR teóricas'):
        for c in clases:
            ex = ejemplos[(grupo, c)]
            for e in random.sample(ex, min(3, len(ex))):
                print('  [%s · %s] …%s…' % (grupo, c, e))


def delta(datos, canon, a, n_mfw=150):
    import numpy as np
    low = datos['mfw_low']
    todo = collections.Counter(w for k in low for ven in low[k] for w in ven)
    mfw = [w for w, _ in todo.most_common(n_mfw)]
    idx = {w: i for i, w in enumerate(mfw)}

    def vec(ven):
        c = collections.Counter(ven)
        n = max(1, len(ven))
        return np.array([c[w] / n for w in mfw])
    V = {k: np.array([vec(v) for v in low[k]]) for k in low}
    allv = np.vstack([V[k] for k in V])
    mu, sd = allv.mean(0), allv.std(0) + 1e-9
    Z = {k: (V[k] - mu) / sd for k in V}
    perfil = {k: Z[k].mean(0) for k in canon + [o for o in datos['obras'] if o not in canon]}
    dist = lambda x, y: float(np.mean(np.abs(x - y)))
    print('\n## 14 · Estilometría (Delta de Burrows, %d palabras más frecuentes)' % n_mfw)
    print('Delta entre obras (menor = más parecidas):')
    ob = list(datos['obras'])
    print('%-16s' % '', *['%9s' % o[:9] for o in ob])
    for x in ob:
        print('%-16s' % x[:16], *['%9.2f' % dist(perfil[x], perfil[y]) for y in ob])
    centro_ur = np.vstack([Z[t] for t in datos['ur']]).mean(0)
    print('\nDelta del perfil medio de UR a cada obra:', ', '.join('%s %.2f' % (o[:12], dist(centro_ur, perfil[o])) for o in ob))
    print('\nObra más cercana de cada pieza de URS (Delta del perfil de la pieza) y distancia al perfil medio de UR:')
    rows = []
    for t in datos['ur']:
        pz = Z[t].mean(0)
        d_ob = sorted((dist(pz, perfil[o]), o) for o in ob)
        rows.append((dist(pz, centro_ur), t, d_ob[0][1], d_ob[0][0]))
    rows.sort(reverse=True)
    cont = collections.Counter(r[2] for r in rows)
    print('Reparto de la obra más cercana:', dict(cont))
    print('Las 12 piezas más alejadas del perfil medio de UR (voz atípica):')
    for d, t, o, do in rows[:12]:
        print('  %.2f  %-60s  más cercana: %s (%.2f)' % (d, t[:60], o, do))
    print('Las 6 más cercanas al perfil medio:')
    for d, t, o, do in rows[-6:]:
        print('  %.2f  %-60s  más cercana: %s (%.2f)' % (d, t[:60], o, do))


if __name__ == '__main__':
    main()
