"""Resumen de una ronda de lectura de ocho lectores independientes (ver lectura-rubrica.md).

Uso:  python3 lectura-resumen.py CARPETA PIEZA
  CARPETA  un .txt por lector; en cada uno, una línea por pieza leída:  pieza|aporte|prosa|evidencia|publico|editores|entrada|emocion|noespecialista|memorabilidad
           (la pieza evaluada y las dos de calibración: angostura e islandia1)
  PIEZA    nombre de la pieza evaluada tal como aparece en esas líneas (por ejemplo: cultura)

Calcula la nota (60 % calidad + 40 % impacto), la media por criterio, la nota ajustada por calibración y la dispersión entre lectores.
Notas oficiales de calibración (lectura del 09/10/26): Angostura 3,50, Islandia I 3,16. Umbrales: α >= 3,34; β de 2,74 a 3,33; γ por debajo.
"""
import glob,os,re,statistics as st,sys
COLS=['aporte','prosa','evidencia','publico','editores','entrada','emocion','noespecialista','memorabilidad']
OFF={'islandia1':3.16,'angostura':3.5}
def nota(v):
    q=sum(v[0:3])/3; i=(v[3]+v[4])/2
    return q,i,.6*q+.4*i
def leer(carpeta):
    L={}
    for f in sorted(glob.glob(os.path.join(carpeta,'*.txt'))):
        d={}
        for linea in open(f,encoding='utf-8'):
            m=re.match(r'\s*([a-z0-9_]+)\|([\d.|]+)\s*$',linea)
            if m:
                v=[float(x) for x in m.group(2).split('|')]
                if len(v)==9: d[m.group(1)]=v
        if d: L[os.path.basename(f)]=d
    return L
def main(carpeta,pieza):
    L=leer(carpeta)
    ev=[d[pieza] for d in L.values() if pieza in d]
    if not ev: sys.exit('Ningún lector tiene la pieza «%s».'%pieza)
    ns=[nota(v)[2] for v in ev]
    print('lectores con la pieza: %d'%len(ev))
    print('nota bruta %.2f (calidad %.2f, impacto %.2f); mín %.2f, máx %.2f, desviación %.2f'%(
        st.mean(nota(v)[2] for v in ev),st.mean(nota(v)[0] for v in ev),st.mean(nota(v)[1] for v in ev),min(ns),max(ns),st.stdev(ns) if len(ns)>1 else 0))
    for c,k in zip(COLS,range(9)): print('  %-15s %.2f'%(c,st.mean(v[k] for v in ev)))
    aj=[]
    for d in L.values():
        cal=[k for k in OFF if k in d]
        if pieza in d and cal: aj.append(nota(d[pieza])[2]+st.mean(OFF[k]-nota(d[k])[2] for k in cal))
    if aj: print('nota ajustada por calibración (n=%d): %.2f; mín %.2f, máx %.2f'%(len(aj),st.mean(aj),min(aj),max(aj)))
    for k in OFF:
        c=[nota(d[k])[2] for d in L.values() if k in d]
        if c: print('  calibración %s: %.2f (oficial %.2f)'%(k,st.mean(c),OFF[k]))
if __name__=='__main__':
    if len(sys.argv)!=3: sys.exit(__doc__)
    main(sys.argv[1],sys.argv[2])
