# Herramientas

Todo lo que no es texto del libro pero hace falta para trabajarlo. Los textos de las obras de referencia (Baroja, Orwell, Martín Santos) no se guardan en el repositorio.

| Archivo | Para qué sirve |
|---|---|
| `guardar-y-publicar.sh` | Guarda el trabajo en la rama y publica en `main` todo menos los HTML (los HTML, solo con el OK de Luis y la opción `--html`). Con `traer`, recoge lo que Luis sube desde la web. Los borrados no se publican solos. |
| `ultra-medidas.py` | Recorrido 4 del Relojero Ultra (antes `relojero-plus-medidas.py`): mide una pieza con la batería de las filas de tipo M de la matriz (Normas 38, 55 y otras): tabla con valor, umbral y estado. |
| `verificar-matriz.py` | Comprueba que cada encabezado de `NORMA-METODO.md` tiene fila en la matriz del Ultra y que ninguna fila queda huérfana. Se ejecuta con cada cambio del archivo de normas. |
| `relojero-ultra-palabras.py` | Recorrido 3 del Relojero Ultra (Norma 62): «ur» en rojo y la 'T', concordancia de palabras, términos propios, tipografía y léxico desconocido, y nombres, cifras y fechas contra la glosa. |
| `ultra-18-analisis.py` | Recorrido 5 del Ultra: los 18 análisis medidos de una pieza frente al corredor del canon y a las piezas de URS (necesita spaCy y el caché de `analisis-texto.py`). |
| `perfil-frase.py` | Perfil de frase de cada pieza (Norma 36.8): longitud, comienzos, subordinación. |
| `perfil-corpus.py` | Compara las piezas con el corredor del canon (rango de los trozos de 2.000 palabras de las obras de referencia). |
| `analisis-texto.py` | Los 18 análisis del marco textual con analizador sintáctico (necesita spaCy). |
| `estimar-paginas-glosa.py` y `glosas-tratadas.json` | Estimación de páginas del libro puro con la glosa telegráfica; el JSON guarda las palabras de glosa antes y después de cada pieza tratada. |
| `glosa-extendida.py` | Deposita la glosa íntegra de una pieza en la pestaña GLOSAS EXTENDIDAS antes de podarla. |
| `edicion/lib_poda.py` | Utilidades de edición: poda de glosas, Marcador, ledger, medición por piezas. |
| `edicion/herr.py` | Búsqueda tolerante a etiquetas y entidades dentro del texto y aplicación de lotes antes/después. |
| `edicion/medir-piezas.js` | Palabras y caracteres de cada pieza de `urtz.html` (node y playwright). |
| `edicion/lectura-rubrica.md` | Protocolo de la lectura de ocho lectores independientes (nueve criterios, calibración). |
| `edicion/lectura-resumen.py` | Nota, medias por criterio, ajuste de calibración y dispersión de una ronda de lectura. |
| `edicion/calibracion/` | Las dos piezas de calibración (Angostura e Islandia I) en la versión usada en las lecturas. |

Los scripts de `edicion/` guardan sus copias de seguridad y medidas en `/tmp/ur-trabajo` (o en la carpeta de la variable `UR_TRABAJO`) y la autoría de los commits se pasa por la variable `CIERRE`.
