#!/usr/bin/env python3
"""Verificador de cobertura de la matriz del Relojero Ultra (Norma 62, Parte II.2).

Comprueba que CADA encabezado de NORMA-METODO.md (secciones, normas, subnormas, subsecciones de las Partes I, II y IV)
figura en la columna «Cubre» de la matriz de la Parte VI (tabla VI.1), y avisa de las entradas de la matriz que ya no
corresponden a ningún encabezado. Una regla sin fila no existe para el procedimiento: se ejecuta con cada cambio del archivo.

Uso:
    python3 herramientas/verificar-matriz.py [ruta/a/NORMA-METODO.md]
Salida: 0 si todo está cubierto; 1 si falta alguna fila (la lista dice cuáles).
"""
import re, sys, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, 'NORMA-METODO.md')
txt = open(ruta, encoding='utf-8').read().split('\n')

TOK = re.compile(r'^(?:[IVX]+(?:\.\d+)?(?:[–-][IVX]+)?(?: y [IVX]+)?(?: bis| ter| quater)?|\d+(?:\.\d+)?(?: bis| ter)?)$')
enc = []
for l in txt:
    m = re.match(r'^### (.+?) · ', l)
    if m and TOK.match(m.group(1)):
        enc.append(m.group(1))
        continue
    m = re.match(r'^\*\*((?:\d+|[IVX]+)\.\d+(?: bis| ter)?) · ', l)
    if m:
        enc.append(m.group(1))
# la propia matriz (VI.x) no necesita fila
enc = [e for e in enc if not e.startswith('VI.')]

# tabla VI.1
filas, dentro = [], False
for l in txt:
    if l.startswith('### VI.1'):
        dentro = True
        continue
    if dentro and l.startswith('### '):
        break
    if dentro and l.startswith('|') and not l.startswith('|---') and not l.startswith('| Fila'):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) >= 7:
            filas.append(c)
cubre = set()
for c in filas:
    for t in c[1].split(';'):
        t = re.sub(r'\s*\(.*\)\s*$', '', t.strip())
        if t:
            cubre.add(t)

falta = [e for e in enc if e not in cubre]
sobra = [c for c in sorted(cubre) if c not in enc and c != 'XXVII' and not c.startswith('Regla ')]
print('encabezados con token: %d · filas en la matriz: %d · tokens cubiertos: %d' % (len(enc), len(filas), len(cubre)))
if falta:
    print('SIN FILA en la matriz (añadir en el mismo paso):')
    for e in falta:
        print('  -', e)
if sobra:
    print('Entradas de la matriz sin encabezado (revisar):')
    for e in sobra:
        print('  -', e)
if not falta and not sobra:
    print('OK: todo encabezado tiene fila y toda fila tiene encabezado.')
sys.exit(1 if falta else 0)
