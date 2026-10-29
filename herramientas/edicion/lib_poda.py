"""Utilidades de edición sobre urtz.html (poda de glosas, Marcador, ledger, medición por piezas).

Se importan desde los scripts de edición (ver herr.py). Rutas:
  R   raíz del repositorio (dos carpetas por encima de este archivo)
  P   urtz.html
  SP_ carpeta de trabajo para copias de seguridad y medidas (variable UR_TRABAJO; por defecto /tmp/ur-trabajo).
Necesita node con playwright para medir (medir-piezas.js). La autoría de los commits se pasa por la variable CIERRE.
"""
import re,html,json,subprocess,shutil,os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
R=os.path.dirname(os.path.dirname(HERE))
P=R+'/urtz.html'
SP_=os.environ.get('UR_TRABAJO','/tmp/ur-trabajo'); os.makedirs(SP_,exist_ok=True)
SPAN='<span style="color:#b01a1a;">%s</span>'
def mark(t): return re.sub(r'(?i)ur',lambda m:SPAN%m.group(0),t)
def inl(t):
    out=''
    for p in re.split(r'(\*[^*]+\*)',t):
        if p.startswith('*') and p.endswith('*') and len(p)>2: out+='<em>'+mark(p[1:-1].replace('&','&amp;'))+'</em>'
        else: out+=mark(p.replace('&','&amp;'))
    return out
G2='<span style="font-size:0.86em; color:#7d7d7d;">%s</span>'
NUM='<span style="color:#b01a1a; font-size:0.78em;">(%d)</span>'
def txt(x): return html.unescape(re.sub(r'<[^>]*>','',x)).strip()
def medir(destino):
    subprocess.run(['node',HERE+'/medir-piezas.js',P,destino],check=True,capture_output=True)
def antes(nombre,seccion,clave):
    """copia de seguridad, medida previa y pestaña de GLOSAS EXTENDIDAS"""
    shutil.copy(P,SP_+'/urtz_antes_%s.html'%nombre)
    medir(SP_+'/medida_%s_0.json'%nombre)
    r=subprocess.run(['python3',R+'/herramientas/glosa-extendida.py',clave,seccion],capture_output=True,text=True)
    print(r.stdout.strip(),r.stderr.strip())
    assert 'insertada' in r.stdout
def poda(clave,E_,body_edits=(),tratada_key=None):
    s=open(P,encoding='utf-8').read()
    a0=None
    for m in re.finditer(r'<details class="pieza"([^>]*)>\s*<summary[^>]*>(.*?)</summary>',s,re.S):
        t=txt(m.group(2))
        if t.startswith('▶'+clave) and 'GLOSAS EXTENDIDAS' not in t and m.start()<s.find('FIN DEL LIBRO'): a0=m.start(); titulo=re.split(r'[αβγ☠]',t[1:])[0].strip(); break
    assert a0
    j=s.find('</details>',a0); seg=s[a0:j]
    g=seg.find('GLOSA &middot;'); assert g>0
    body,glo=seg[:g],seg[g:]
    for old,new in body_edits:
        assert body.count(old)==1,(old[:60],body.count(old))
        body=body.replace(old,new)
    num=[e for e in E_ if e[3]]
    mp={e[3]:k for k,e in enumerate(num,1)}
    presentes={int(x) for x in re.findall(r'<sup class="gr">\((\d+)\)</sup>',body)}
    body=re.sub(r'<sup class="gr">\((\d+)\)</sup>',lambda m:'<sup class="gr">(%d)</sup>'%mp[int(m.group(1))] if int(m.group(1)) in mp else '',body)
    assert body.count(' (*-glo)')==1
    body=body.replace(' (*-glo)','',1)
    mlist=re.search(r'<(ul|ol)\b[^>]*>',glo); assert mlist,'sin lista de glosa'
    ltag=mlist.group(1); u0=mlist.start(); u1=glo.find('</%s>'%ltag,u0)
    STD_UL="<ul style=\"font-family:'Courier Prime',monospace; font-size:0.92rem; line-height:1.7; color:#444; padding-left:1.1rem; margin:0;\">"
    ul_open=glo[u0:mlist.end()] if ltag=='ul' else STD_UL
    old_lis=re.findall(r'<li\b[^>]*>.*?</li>',glo[u0:u1],re.S)
    AP=re.search(r'<div style="border-top:1px solid rgba\(176,26,26,0\.25\); margin-top:2rem; padding-top:1rem;"><div[^>]*>APARATO CR.*?</ul></div>\s*',glo,re.S)
    if AP: old_lis+=re.findall(r'<li\b[^>]*>.*?</li>',AP.group(0),re.S)
    lis=[]
    k=0
    for (t,a,b,o) in E_:
        if o:
            k+=1
            li='<li>'+NUM%k+' <strong>'+mark(t.replace('&','&amp;'))+'</strong>:'
        else:
            li='<li>'
        if a: li+=(' ' if o else '')+inl(a)
        if b: li+=' '+G2%inl(b)
        lis.append(li+'</li>')
    nsup=len(re.findall(r'<sup class="gr">',body))
    glo2=glo[:u0]+ul_open+'\n'+'\n'.join(lis)+'\n</ul>'+glo[u1+len('</%s>'%ltag):]
    if AP: glo2=glo2.replace(AP.group(0),'',1)
    s=s[:a0]+body+glo2+s[j:]
    open(P,'w',encoding='utf-8').write(s)
    w=lambda L:sum(len(txt(x).split()) for x in L)
    wa,wd=w(old_lis),w(lis)
    print('«%s»: glosa %d entradas %d palabras -> %d entradas %d palabras (%.0f %%); llamadas en el cuerpo: %d'%(titulo,len(old_lis),wa,len(lis),wd,(wd-wa)/wa*100,nsup))
    assert nsup==len(num),('llamadas y entradas no cuadran',nsup,len(num))
    jp=R+'/herramientas/glosas-tratadas.json'
    d=json.load(open(jp,encoding='utf-8')); d[tratada_key or titulo]=[wa,wd]
    json.dump(d,open(jp,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    return titulo,wa,wd
def marcador(nombre,filas):
    """filas: nombres de las filas del Marcador (categoría y subcategoría) que reciben el cambio de la pieza"""
    medir(SP_+'/medida_%s_1.json'%nombre)
    A=json.load(open(SP_+'/medida_%s_0.json'%nombre)); B=json.load(open(SP_+'/medida_%s_1.json'%nombre))
    assert len(A)==len(B)
    anex=('CONTRAPORTADA Y OTROS ASUNTOS RELEVANTES','PRECEDENTES, BIBLIOGRAFÍA Y RESISTENCIAS HÍDRICAS','¿PUEDE NEXUS-7 SOÑAR CON UR?','EL NOTurIKON: DICCIONARIO ANAGRAMÁTICO','MARCADOR FONOMÁTICO')
    d={'urs':[0,0],'pure':[0,0],'urim':[0,0],'ge':[0,0],'pieza':[0,0]}
    for a,b in zip(A,B):
        dc,dw=b['chars']-a['chars'],b['words']-a['words']
        if dc==0 and dw==0: continue
        if 'ESTAÑO Y RECURSOS' in a['title'] or 'FE DE ERRATAS' in a['title']: continue  # dossier de estaño: material de trabajo, no cuenta
        k='urs' if a['zone']=='URS' else 'urim'
        d[k][0]+=dc; d[k][1]+=dw
        if k=='urs' and a['cat'] not in anex: d['pure'][0]+=dc; d['pure'][1]+=dw; d['pieza'][1]+=dw
        if a['cat']=='CONTRAPORTADA Y OTROS ASUNTOS RELEVANTES': d['ge'][0]+=dc; d['ge'][1]+=dw
    print('deltas (caracteres, palabras):',d)
    s=open(P,encoding='utf-8').read()
    def num(x): return format(x,',').replace(',','.')
    def parse(x): return int(x.replace('.',''))
    def linea(patron,dc,dw,pag=True):
        nonlocal s
        m=re.search(patron,s); assert m,patron
        c,w=parse(m.group(2)),parse(m.group(3))
        nc,nw=c+dc,w+dw
        nuevo=m.group(1)+num(nc)+' caracteres &middot; '+num(nw)+' palabras'+m.group(4)+('%d'%round(nw/250))+m.group(5)
        s=s[:m.start()]+nuevo+s[m.end():]
        return nw
    # URS
    linea(r'(&middot; )([\d.]+) caracteres &middot; ([\d.]+) palabras(( &middot; &asymp;))(\d+)?',0,0) if False else None
    def ln(patron,dc,dw):
        nonlocal s
        m=re.search(patron,s); assert m,patron
        c,w,pg=parse(m.group(1)),parse(m.group(2)),m.group(3)
        nw=w+dw
        s=s[:m.start(1)]+num(c+dc)+s[m.end(1):m.start(2)]+num(nw)+s[m.end(2):m.start(3)]+str(round(nw/250))+s[m.end(3):]
        return nw
    ln(r'([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+) p&aacute;g\. &middot; 78 piezas',*d['urs'])
    nw_pure=ln(r'([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+) p&aacute;g\. &middot; 69 piezas',*d['pure'])
    ln(r'([\d.]+) caracteres &middot; ([\d.]+) palabras \(piezas reales\) &middot; &asymp;(\d+) p&aacute;g\.',d['urs'][0]+d['urim'][0],d['urs'][1]+d['urim'][1])
    ln(r'TOTAL &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+) p&aacute;g\.',d['urs'][0]+d['urim'][0],d['urs'][1]+d['urim'][1])
    m=re.search(r'([\d.]+) palabras = el total',s); s=s[:m.start(1)]+num(parse(m.group(1))+d['urs'][1]+d['urim'][1])+s[m.end(1):]
    def fila_delta(nombre,dw):
        nonlocal s
        objetivo=html.unescape(nombre)
        ms=[m for m in re.finditer(r'<tr[^>]*>\s*<td[^>]*>(.*?)</td>.*?</tr>',s,flags=re.S) if html.unescape(re.sub(r'<[^>]*>','',m.group(1))).strip()==objetivo]
        assert len(ms)==1,(nombre,len(ms))
        row=ms[0].group(0)
        cells=re.findall(r'<td[^>]*>(.*?)</td>',row,flags=re.S)
        words=parse(cells[9]); nw=words+dw; pages=round(nw/250)
        newrow=row.replace('>%s<'%cells[9],'>%s<'%num(nw),1)
        if cells[10].isdigit(): newrow=newrow.replace('>%s<'%cells[10],'>%d<'%pages,1)
        s=s.replace(row,newrow,1); print('  fila',nombre,words,'->',nw)
    fila_delta('TOTAL DEL LIBRO',d['urs'][1]+d['urim'][1])
    if d['ge'][1]: fila_delta('Contraportada y otros asuntos relevantes',d['ge'][1])
    for f in filas: fila_delta(f,d['pieza'][1])
    open(P,'w',encoding='utf-8').write(s)
    r=subprocess.run(['python3',R+'/herramientas/estimar-paginas-glosa.py'],capture_output=True,text=True,cwd=R).stdout
    print(r)
    est=int(re.search(r'r mediana [\d.]+ % -> ≈(\d+) pág\.',r).group(1))
    s=open(P,encoding='utf-8').read()
    ms=list(re.finditer(r'&asymp;(\d+) p&aacute;g\. &middot; ([\d.]+) palabras &middot; (\d+) piezas</div>',s)); assert len(ms)==1,len(ms)
    m=ms[0]
    s=s[:m.start()]+'&asymp;%d p&aacute;g. &middot; %s palabras &middot; %s piezas</div>'%(round(nw_pure/250),num(nw_pure),m.group(3))+s[m.end():]
    open(P,'w',encoding='utf-8').write(s)
    rng=re.search(r'rango.*',r).group(0)
    print('MARCADOR OK; libro puro',num(nw_pure),'palabras ≈%d pág.; estimación ≈%d'%(round(nw_pure/250),est)); print(rng)
    return d,est,rng

def registrar(norma_txt,ledger_txt,est_out):
    """norma_txt: párrafo de aplicación (Norma 55); ledger_txt: entrada de analisis-editorial.md; est_out: salida del estimador.
    Desde el 29/10/26 el registro vive en archivo-normas/REGISTRO-DE-APLICACIONES.md (NORMA-METODO.md ya no lo lleva)."""
    RG=R+'/archivo-normas/REGISTRO-DE-APLICACIONES.md'
    n=open(RG,encoding='utf-8').read()
    n=n.rstrip('\n')+'\n\n'+norma_txt.strip()+'\n'
    open(RG,'w',encoding='utf-8').write(n)
    l=open(R+'/analisis-editorial.md',encoding='utf-8').read()
    open(R+'/analisis-editorial.md','w',encoding='utf-8').write(l.rstrip('\n')+'\n\n'+ledger_txt.strip()+'\n')
    print('registrado en el registro de aplicaciones')

def est_out():
    return subprocess.run(['python3',R+'/herramientas/estimar-paginas-glosa.py'],capture_output=True,text=True,cwd=R).stdout
def marcador_resumen():
    s=open(P,encoding='utf-8').read()
    f=lambda p:re.search(p,s).groups()
    u=f(r'UR</span>S</strong> &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+) p&aacute;g\.')
    l=f(r'LIBRO PURO</strong> &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+) p&aacute;g\.')
    t=f(r'([\d.]+) caracteres &middot; ([\d.]+) palabras \(piezas reales\) &middot; &asymp;(\d+) p&aacute;g\.')
    T=f(r'TOTAL &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+) p&aacute;g\.')
    return ('**Marcador (Regla 14):** URS %s caracteres / %s palabras / ≈%s págs.; libro puro %s / %s / ≈%s; URS+URIM %s / %s / ≈%s; TOTAL DEL PROYECTO %s / %s / ≈%s.'%(u+l+t+T))

def notas_mapa(nombre,ahorro,est_o):
    """nombre: título corto para NOTAS y MAPA; ahorro: '−48 %'"""
    s=open(P,encoding='utf-8').read(); fin=s.find('FIN DEL LIBRO')
    n_glo=sum(1 for m in re.finditer(r'<details class="pieza"[^>]*>\s*<summary[^>]*>(.*?)</summary>',s,re.S) if m.start()<fin and '(*-glo)' in txt(m.group(1)))
    nt=open(R+'/NOTAS-URTZ.md',encoding='utf-8').read()
    a=nt.index(' Hoy la llevan '); b=nt.index(' piezas (recuento en `urtz.html`).',a)
    nt=nt[:a]+' Tampoco la lleva «%s».'%nombre+' Hoy la llevan %d'%n_glo+nt[b:]
    open(R+'/NOTAS-URTZ.md','w',encoding='utf-8').write(nt)
    mp=open(R+'/MAPA-DEL-METODO.md',encoding='utf-8').read()
    mp=mp.replace('Curaca (−63 %) y Endorois (−66 %)','Curaca (−63 %), Endorois (−66 %)',1)
    clave='; el cartel de FIN DEL LIBRO lleva una estimación'
    assert clave in mp
    mp=mp.replace(clave,', '+nombre+' ('+ahorro+')'+clave,1)
    # estimación
    est=re.search(r'r mediana [\d.]+ % -> ≈(\d+)',est_o).group(1); rg=re.search(r'rango entre los tres estimadores: ≈(\d+) a ≈(\d+)',est_o)
    mp=re.sub(r'\(≈\d+, mediana del ahorro por pieza, rango ≈\d+-\d+;','(≈%s, mediana del ahorro por pieza, rango ≈%s-%s;'%(est,rg.group(1),rg.group(2)),mp,count=1)
    open(R+'/MAPA-DEL-METODO.md','w',encoding='utf-8').write(mp)
    print('NOTAS: quedan',n_glo,'con (*-glo)')

CARAS={'Cara 1 · Ibérico':['Ibero Intros','Euskal Herria','Cantábrico','Atlántico','Mediterráneo Andaluz','Mediterráneo Levantino','Central','Portugal','Panibérico'],
'Cara 2 · Europa':['Escandinavia · Norte','Islas Británicas · Atlántico Norte','Europa Central · Rin-Danubio','Europa Latina · Francia-Italia-Grecia','Europa del Este · Balcanes-Cárpatos','Finlandia · Báltico'],
'Cara 3 · Asia':['Anatolia · Cáucaso','Mesopotamia · Levante','Asia Central · Turán-Irán','Asia del Sur · Indo-Ganges','Asia del Este · Amur-Japón','Asia del Sureste · Mekong'],
'Cara 4 · América':['América Intros','Ártico americano · Inuit','América del Norte · Grandes Lagos-Misisipí','Mesoamérica · Caribe · Urabá','Orinoco · Amazonia','Brasil · Nordeste y cuencas atlánticas','Andes · Pacífico','Cono Sur · Patagonia-Tierra del Fuego'],
'Cara 5 · África':['Norte de África · Nilo-Sahara','África Occidental · Níger-Senegal','Cuenca del Congo','África Oriental · Rift Valley-Grandes Lagos','Cuerno de África · Yemen','África del Sur · Kalahari-Cabo'],
'Cara 6 · Oceanía':['Australia · interior árido y costas','Nueva Guinea · Melanesia','Polinesia · el Pacífico','Micronesia · Microcontinentes','Nueva Zelanda · Maorí','Antártida · el hielo primordial']}
CATS={'PREFACIO':'Prefacio','INTRODUCCIÓN':'Introducción','ENSAYOS ANTI-DOGMÁTICOS':'Ensayos Anti-Dogmáticos','BIOPSIA DEL SISTEMA MUNDO':'Biopsia del Sistema Mundo','INTERLUDIOS · DEFENSA RADICAL Y DEMOCRÁTICA DE UR':'Interludios','IMPUGNACIÓN A UR':'Impugnación a UR','ETIMOLOGÍA INSURGENTE':'Etimología Insurgente','BONUS TRACKS':'Bonus Tracks','EPÍLOGO':'Epílogo'}
def ubicar(clave):
    medir(SP_+'/medida_tmp.json'); d=json.load(open(SP_+'/medida_tmp.json'))
    for r in d:
        if r['title'].startswith('▶'+clave) and r['zone']=='URS': break
    else: raise Exception('no hallada '+clave)
    cat,sub=r['cat'],re.sub(r'^[●◑○◦]\s*','',r['sub'])
    if sub:
        cara=[c for c,l in CARAS.items() if sub in l][0]
        return cara+' · '+sub, [cara,'&ndash; '+sub]
    return CATS[cat].replace('Prefacio','Prefacio'), [CATS[cat]]
_n=[20]
def hacer(clave,E_,informe,corto,body_edits=(),tratada_key=None,tag=None,reanudar=False):
    """informe: texto (markdown) que va a la Norma 55 y sirve de informe a Luis; corto: título para NOTAS/MAPA"""
    _nt=open(R+'/archivo-normas/REGISTRO-DE-APLICACIONES.md',encoding='utf-8').read()
    _n[0]=20+len(re.findall(r'\*\*Aplicación n\.º \d+:',_nt))+1
    verificar_edits(clave,body_edits)
    seccion,filas=ubicar(clave)
    nombre=tag or ('p%d'%_n[0])
    if not reanudar: antes(nombre,seccion,clave)
    tit,wa,wd=poda(clave,E_,body_edits,tratada_key)
    d,est,rng=marcador(nombre,[f for f in filas])
    eo=est_out(); rm=marcador_resumen()
    ah='−%.0f %%'%((wa-wd)/wa*100)
    norma='**Aplicación n.º %d: «%s» (17/10/26, poda general de URS, a petición de Luis).** Sección: %s. Glosa de %d palabras a %d (%s); pieza %s palabras (cuerpo y glosa; Marcador). '%(_n[0],tit,seccion,wa,wd,ah,('%+d'%d['pieza'][1]).replace('-','−'))+informe.strip()
    ledger='**Poda de glosa n.º %d: «%s» (17/10/2026).** Glosa %d → %d palabras (%s). Detalle en la Norma 55, aplicación n.º %d. %s Estimación del cartel: ≈%d págs. (%s). HTML sin publicar.'%(_n[0],tit,wa,wd,ah,_n[0],rm,est,rng.replace('rango entre los tres estimadores: ',''))
    registrar(norma,ledger,eo)
    notas_mapa(corto,ah,eo)
    r=subprocess.run(['bash',R+'/herramientas/guardar-y-publicar.sh','Poda de la glosa de «%s» (%s); Marcador y estimación al día'%(tit,ah)],capture_output=True,text=True,cwd=R,env=os.environ)
    print(r.stdout[-200:],r.stderr[-200:])
    # informe breve a la bitácora para el final
    open(SP_+'/informes.txt','a',encoding='utf-8').write('\n\n=== %d · %s ===\nsección: %s | glosa %d -> %d (%s) | estimación ≈%d\n%s\n'%(_n[0],tit,seccion,wa,wd,ah,est,informe.strip()))
    print('HECHO',tit,wa,'->',wd,ah,'| estim ≈',est)

def terminar(clave,tit,wa,wd,informe,corto,nombre):
    """Reanuda hacer() cuando la poda ya se aplicó (Marcador, registro, NOTAS, MAPA, guardado)."""
    _nt=open(R+'/archivo-normas/REGISTRO-DE-APLICACIONES.md',encoding='utf-8').read()
    _n[0]=20+len(re.findall(r'\*\*Aplicación n\.º \d+:',_nt))+1
    seccion,filas=ubicar(clave)
    d,est,rng=marcador(nombre,list(filas))
    eo=est_out(); rm=marcador_resumen()
    ah='−%.0f %%'%((wa-wd)/wa*100)
    norma='**Aplicación n.º %d: «%s» (17/10/26, poda general de URS, a petición de Luis).** Sección: %s. Glosa de %d palabras a %d (%s); pieza %s palabras (cuerpo y glosa; Marcador). '%(_n[0],tit,seccion,wa,wd,ah,('%+d'%d['pieza'][1]).replace('-','−'))+informe.strip()
    ledger='**Poda de glosa n.º %d: «%s» (17/10/2026).** Glosa %d → %d palabras (%s). Detalle en la Norma 55, aplicación n.º %d. %s Estimación del cartel: ≈%d págs. (%s). HTML sin publicar.'%(_n[0],tit,wa,wd,ah,_n[0],rm,est,rng.replace('rango entre los tres estimadores: ',''))
    registrar(norma,ledger,eo)
    notas_mapa(corto,ah,eo)
    r=subprocess.run(['bash',R+'/herramientas/guardar-y-publicar.sh','Poda de la glosa de «%s» (%s); Marcador y estimación al día'%(tit,ah)],capture_output=True,text=True,cwd=R,env=os.environ)
    print(r.stdout[-200:],r.stderr[-200:])
    open(SP_+'/informes.txt','a',encoding='utf-8').write('\n\n=== %d · %s ===\nsección: %s | glosa %d -> %d (%s) | estimación ≈%d\n%s\n'%(_n[0],tit,seccion,wa,wd,ah,est,informe.strip()))
    print('HECHO',tit,wa,'->',wd,ah,'| estim ≈',est)


def verificar_edits(clave,body_edits):
    s=open(P,encoding='utf-8').read()
    for m in re.finditer(r'<details class="pieza"([^>]*)>\s*<summary[^>]*>(.*?)</summary>',s,re.S):
        if txt(m.group(2)).startswith('▶'+clave) and m.start()<s.find('FIN DEL LIBRO'): a=m.start();break
    else: raise Exception('no hallada '+clave)
    j=s.find('</details>',a); seg=s[a:j]; g=seg.find('GLOSA &middot;'); body=seg[:g]
    for old,new in body_edits:
        assert body.count(old)==1,('EDICIÓN NO VÁLIDA',old[:70],body.count(old))


def hacer_manual(clave,edits,informe,corto,tratada_key=None):
    """Piezas cuya glosa es una lista de referencias en <p> (sin <li>): edita cadenas crudas en la pieza, retira (*-glo) y cierra como hacer()."""
    _nt=open(R+'/archivo-normas/REGISTRO-DE-APLICACIONES.md',encoding='utf-8').read()
    _n[0]=20+len(re.findall(r'\*\*Aplicación n\.º \d+:',_nt))+1
    seccion,filas=ubicar(clave)
    nombre='p%d'%_n[0]
    shutil.copy(P,SP_+'/urtz_antes_%s.html'%nombre); medir(SP_+'/medida_%s_0.json'%nombre)
    s=open(P,encoding='utf-8').read()
    for m in re.finditer(r'<details class="pieza"([^>]*)>\s*<summary[^>]*>(.*?)</summary>',s,re.S):
        t=txt(m.group(2))
        if t.startswith('▶'+clave) and m.start()<s.find('FIN DEL LIBRO'):
            a0=m.start(); titulo=re.split(r'[αβγ☠]',t[1:])[0].strip(); break
    else: raise Exception('no hallada '+clave)
    j=s.find('</details>',a0); seg=s[a0:j]
    def glosa_words(sg):
        h=re.search(r'<h4[^>]*>GLOSA[^<]*</h4>',sg)
        g=sg[h.start():]
        r=g.find('&rarr; RAYUELAS')
        if r>0: g=g[:r]
        return len(txt(g).split())
    wa=glosa_words(seg)
    for old,new in edits:
        assert seg.count(old)==1,('EDICIÓN NO VÁLIDA',old[:70],seg.count(old))
        seg=seg.replace(old,new)
    assert seg.count(' (*-glo)')==1
    seg=seg.replace(' (*-glo)','',1)
    wd=glosa_words(seg)
    s=s[:a0]+seg+s[j:]
    open(P,'w',encoding='utf-8').write(s)
    jp=R+'/herramientas/glosas-tratadas.json'
    print('«%s»: glosa %d -> %d palabras'%(titulo,wa,wd))
    dd,est,rng=marcador(nombre,list(filas))
    eo=est_out(); rm=marcador_resumen()
    ah=('−%.0f %%'%((wa-wd)/wa*100) if wd<=wa else '+%.0f %%'%((wd-wa)/wa*100)) if wa else '0 %'
    norma='**Aplicación n.º %d: «%s» (17/10/26, poda general de URS, a petición de Luis).** Sección: %s. Glosa de %d palabras a %d (%s); pieza %s palabras (cuerpo y glosa; Marcador). '%(_n[0],titulo,seccion,wa,wd,ah,('%+d'%dd['pieza'][1]).replace('-','−'))+informe.strip()
    ledger='**Poda de glosa n.º %d: «%s» (17/10/2026).** Glosa %d → %d palabras (%s). Detalle en la Norma 55, aplicación n.º %d. %s Estimación del cartel: ≈%d págs. (%s). HTML sin publicar.'%(_n[0],titulo,wa,wd,ah,_n[0],rm,est,rng.replace('rango entre los tres estimadores: ',''))
    registrar(norma,ledger,eo)
    notas_mapa(corto,ah,eo)
    r=subprocess.run(['bash',R+'/herramientas/guardar-y-publicar.sh','Poda de la glosa de «%s» (%s); Marcador y estimación al día'%(titulo,ah)],capture_output=True,text=True,cwd=R,env=os.environ)
    print(r.stdout[-200:],r.stderr[-200:])
    open(SP_+'/informes.txt','a',encoding='utf-8').write('\n\n=== %d · %s ===\nsección: %s | glosa %d -> %d (%s) | estimación ≈%d\n%s\n'%(_n[0],titulo,seccion,wa,wd,ah,est,informe.strip()))
    print('HECHO',titulo,wa,'->',wd,ah,'| estim ≈',est)
