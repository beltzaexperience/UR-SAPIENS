"""Ayudas para editar piezas de urtz.html tolerando etiquetas y entidades dentro del texto (pat), y aplicar lotes antes/después (aplicar)."""
import sys,re,shutil,json
from html.entities import codepoint2name
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib_poda import P,inl,medir,SP_
TAG=r'(?:<[^>]*>)*'
def alt(c):
    al=[re.escape(c)]
    if ord(c)>127:
        n=codepoint2name.get(ord(c))
        if n: al.append('&%s;'%n)
        al+=['&#%d;'%ord(c),'&#x%x;'%ord(c)]
    return '(?:'+'|'.join(al)+')'
def pat(old):
    out=[]
    for c in old:
        if c=='&': r='&amp;'
        elif c=="'": r="(?:'|&#39;|&apos;)"
        elif c==' ': r='(?:\\s|&nbsp;)+'
        elif ord(c)>127: r=alt(c)
        else: r=re.escape(c)
        out.append(r)
    return TAG.join(out)
def pieza_trabajo(s):
    i=s.find('<details class="pieza" data-s="borrador cultura continente ibérico versión de trabajo'); assert i>=0
    d=0
    for m in re.finditer(r'<details\b|</details>',s[i:]):
        d+=1 if m.group(0).startswith('<details') else -1
        if d==0: return i,i+m.end()
def aplicar(tag,E):
    shutil.copy(P,SP_+'/urtz_antes_%s.html'%tag); medir(SP_+'/medida_%s_0.json'%tag)
    s=open(P,encoding='utf-8').read()
    a,b=pieza_trabajo(s); seg=s[a:b]; bad=0
    for old,new in E:
        ms=list(re.finditer(pat(old),seg))
        if len(ms)!=1: print('✗',len(ms),old[:70]); bad+=1; continue
        seg=seg[:ms[0].start()]+inl(new)+seg[ms[0].end():]
        if seg.count('<span')!=seg.count('</span>'): print('✗ span desequilibrado tras',old[:50]); bad+=1
    if bad: print('FALLOS',bad); sys.exit(1)
    s=s[:a]+seg+s[b:]
    assert s.count('<details')==s.count('</details>')
    open(P,'w',encoding='utf-8').write(s)
    medir(SP_+'/medida_%s_1.json'%tag)
    A=json.load(open(SP_+'/medida_%s_0.json'%tag)); B=json.load(open(SP_+'/medida_%s_1.json'%tag)); assert len(A)==len(B)
    dw=sum(y['words']-x['words'] for x,y in zip(A,B)); dc=sum(y['chars']-x['chars'] for x,y in zip(A,B))
    # Marcador (URIM, URS+URIM, TOTAL, el total)
    s=open(P,encoding='utf-8').read()
    num=lambda x:format(x,',').replace(',','.'); par=lambda x:int(x.replace('.',''))
    pg=lambda w:round(w/250)
    def sub(p,fn):
        nonlocal s
        m=re.search(p,s); assert m,p
        s=s[:m.start()]+fn(m)+s[m.end():]
    sub(r'(<strong><span style="color:#b01a1a;">UR</span>IM</strong> &middot; )([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;\d+ p&aacute;g\. &middot; ([^<]*)',
        lambda m:'%s%s caracteres &middot; %s palabras &middot; &asymp;%d p&aacute;g. &middot; %s'%(m.group(1),num(par(m.group(2))+dc),num(par(m.group(3))+dw),pg(par(m.group(3))+dw),m.group(4)))
    sub(r'([\d.]+) caracteres &middot; ([\d.]+) palabras \(piezas reales\) &middot; &asymp;\d+ p&aacute;g\.',
        lambda m:'%s caracteres &middot; %s palabras (piezas reales) &middot; &asymp;%d p&aacute;g.'%(num(par(m.group(1))+dc),num(par(m.group(2))+dw),pg(par(m.group(2))+dw)))
    sub(r'TOTAL &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;\d+ p&aacute;g\.',
        lambda m:'TOTAL &middot; %s caracteres &middot; %s palabras &middot; &asymp;%d p&aacute;g.'%(num(par(m.group(1))+dc),num(par(m.group(2))+dw),pg(par(m.group(2))+dw)))
    sub(r'([\d.]+) palabras = el total',lambda m:num(par(m.group(1))+dw)+' palabras = el total')
    open(P,'w',encoding='utf-8').write(s)
    out={}
    for k,p in [('urim',r'IM</strong> &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+)'),('urs_urim',r'([\d.]+) caracteres &middot; ([\d.]+) palabras \(piezas reales\) &middot; &asymp;(\d+)'),('total',r'TOTAL &middot; ([\d.]+) caracteres &middot; ([\d.]+) palabras &middot; &asymp;(\d+)')]:
        m=re.search(p,s); out[k]=m.groups()
    print('delta',dw,dc,out)
    return dw,dc,out
