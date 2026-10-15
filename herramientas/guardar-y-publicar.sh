#!/usr/bin/env bash
# Guardar y publicar (NOTAS-URTZ.md, Regla 38).
#
#   guardar-y-publicar.sh "mensaje"          guarda todo y publica todo menos los HTML
#   guardar-y-publicar.sh "mensaje" --html   guarda todo y publica también los HTML (solo con el OK de Luis)
#   guardar-y-publicar.sh traer              trae a la línea de trabajo los archivos nuevos que Luis ha subido desde la web
#
# Guardar: copia de seguridad de todo en la línea de trabajo (la rama en la que se está). No cambia nada público.
# Publicar: pasa a la versión pública (main) los archivos tal como están en la línea de trabajo.
#           Los .html solo se publican con --html; si no, la versión pública conserva el último HTML publicado.
# Variable opcional CIERRE: líneas finales del mensaje de guardado (autoría de la sesión).
# Los borrados no se publican solos: se hacen a mano y se avisa a Luis.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
RAMA="$(git rev-parse --abbrev-ref HEAD)"
PUBLICA="main"

reintentar() {
  local n=0
  until "$@"; do
    n=$((n + 1))
    [ "$n" -ge 4 ] && return 1
    sleep $((2 ** n))
  done
}

if [ "${1:-}" = "traer" ]; then
  git fetch -q origin "$PUBLICA"
  nuevos="$(comm -13 \
    <(git ls-tree -r -z --name-only HEAD | tr '\0' '\n' | sort) \
    <(git ls-tree -r -z --name-only "origin/$PUBLICA" | tr '\0' '\n' | sort))"
  if [ -z "$nuevos" ]; then
    echo "No hay archivos nuevos en la versión pública."
    exit 0
  fi
  echo "Archivos nuevos en la versión pública:"
  echo "$nuevos"
  while IFS= read -r f; do
    git checkout "origin/$PUBLICA" -- "$f"
  done <<< "$nuevos"
  git commit -q -m "Traídos de la versión pública los archivos subidos desde la web" ${CIERRE:+-m "$CIERRE"}
  reintentar git push -q -u origin "$RAMA"
  echo "Traídos y guardados."
  exit 0
fi

MENSAJE="${1:-Guardado}"
CON_HTML=0
[ "${2:-}" = "--html" ] && CON_HTML=1

# 1) Guardar
git add -A
if ! git diff --cached --quiet; then
  git commit -q -m "$MENSAJE" ${CIERRE:+-m "$CIERRE"}
fi
reintentar git push -q -u origin "$RAMA"
echo "Guardado en $RAMA."

# 2) Publicar
git fetch -q origin "$PUBLICA"
TMP="$(mktemp -d)"
git worktree add -q --detach "$TMP" "origin/$PUBLICA"
trap 'git worktree remove --force "$TMP" >/dev/null 2>&1 || true' EXIT
(
  cd "$TMP"
  if [ "$CON_HTML" -eq 1 ]; then
    git ls-tree -r -z --name-only "$RAMA" | xargs -0 git checkout "$RAMA" --
  else
    git ls-tree -r -z --name-only "$RAMA" | grep -z -v '\.html$' | xargs -0 git checkout "$RAMA" --
  fi
  if git diff --cached --quiet; then
    echo "Nada nuevo que publicar."
  else
    git commit -q -m "Publicado: $MENSAJE" ${CIERRE:+-m "$CIERRE"}
    reintentar git push -q origin "HEAD:$PUBLICA"
    if [ "$CON_HTML" -eq 1 ]; then
      echo "Publicado, HTML incluidos."
    else
      echo "Publicado, sin los HTML."
    fi
  fi
)
