#!/usr/bin/env bash
# Prepara el entorno del Relojero Ultra (recorrido 5, los 18 análisis): spaCy, el modelo es_core_news_md y el caché del canon.
# Los textos del canon (Baroja, Orwell, Martín Santos) NO están en el repositorio: se recuperan de la historia (commit 9f13cdc, 08/10/26)
# a un directorio fuera del repositorio y no se vuelven a subir. Idempotente. Uso: herramientas/preparar-entorno.sh
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
CANON="${UR_CANON:-/tmp/ur-canon}"
mkdir -p "$CANON"
python3 -c "import spacy" 2>/dev/null || pip install -q spacy numpy
python3 -c "import es_core_news_md" 2>/dev/null || pip install -q https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.8.0/es_core_news_md-3.8.0-py3-none-any.whl
if [ ! -s "$CANON/datos_canon.pkl" ]; then
  git cat-file -e 9f13cdc 2>/dev/null || git fetch -q origin 9f13cdc 2>/dev/null || git fetch -q --unshallow origin
  python3 - "$CANON" <<'PY'
import subprocess,sys
C=sys.argv[1]
pares={'BAROJA - AURORA ROJA':'aurora','BAROJA - EL ARBOL':'arbol','BAROJA - ZALACAIN':'zalacain','ORWELL - 1984':'1984','ORWELL - REBELION':'rebelion','HOMANJE':'homenaje','TIEMPO DE SILENCIO':'tiempo'}
nombres=subprocess.run(['git','ls-tree','--name-only','-z','9f13cdc'],capture_output=True,text=True).stdout.split('\0')
hechos=set()
for n in nombres:
    for clave,dest in pares.items():
        if clave in n and dest not in hechos:
            open('%s/%s.pdf'%(C,dest),'wb').write(subprocess.run(['git','show','9f13cdc:'+n],capture_output=True).stdout); hechos.add(dest)
assert len(hechos)==7,hechos
PY
  python3 herramientas/analisis-texto.py --html urtz.html --cache "$CANON/datos_canon.pkl" \
    --obra baroja_aurora=$CANON/aurora.pdf --hyph baroja_aurora --obra baroja_arbol=$CANON/arbol.pdf --obra baroja_zalacain=$CANON/zalacain.pdf \
    --obra orwell_1984=$CANON/1984.pdf --obra orwell_homenaje=$CANON/homenaje.pdf --hyph orwell_homenaje --obra orwell_rebelion=$CANON/rebelion.pdf \
    --obra martin_santos=$CANON/tiempo.pdf --aparte martin_santos > "$CANON/salida_cache.txt" 2>&1
fi
echo "Listo. Uso: python3 herramientas/ultra-18-analisis.py --cache $CANON/datos_canon.pkl --pieza \"TÍTULO\""
