# controles-humanos/

Banco de textos humanos conocidos para calibrar las medidas de tipo M del Relojero Ultra (`NORMA-METODO.md`, VI.2, «Calibración con controles humanos»). Un control sirve para saber **cuánto se equivoca cada medida con un texto que sabemos escrito por una persona**; no es parte del libro ni se corrige.

## Reglas del banco
1. **Solo texto humano anterior a la IA:** textos de Luis fechados antes de 2023 y trozos del canon (Baroja, Orwell, Martín Santos, cuyos textos no se guardan en el repositorio: solo se anotan sus resultados). Cada texto lleva autor, fecha y origen.
2. **Se guardan tal como se escribieron**, con sus erratas y sus defectos. Si el original no tiene título, la primera línea es `[sin título]`. No se corrigen, no se retocan y no se mejoran: un control corregido deja de ser un control.
3. **Parte reservada:** una parte del banco queda reservada y solo sirve para comprobar umbrales ya fijados, nunca para fijarlos.
4. **Tamaño:** con menos de 100 trozos el porcentaje de falsos positivos se anota con «n insuficiente» y los umbrales vigentes no cambian.
5. **Cómo se mide:** `python3 herramientas/ultra-medidas.py archivo-normas/controles-humanos/TEXTO.txt --texto` (primera línea del archivo = título, no se mide). Los resultados se anotan en `RESULTADOS.md`.

## Textos
| Archivo | Autor | Fecha | Palabras | Uso |
|---|---|---|---|---|
| `2019-continente-ur-o-reyno-de-la-mancha.txt` | Luis Beltza | 2019 (antes del 28/04/2019, según el propio texto) | 572 | reservado (comprobación) |
| `sin-fecha-el-reyno-de-la-mancha-quinta-temporada.txt` | Luis Beltza | sin fecha de Luis; por el contenido (Rajoy en activo, el «proceso» en curso) hacia 2017-2019, **por confirmar** | 696 | fijación |
| `2019-reyno-de-la-mancha-va-bien.txt` | Luis Beltza | marzo de 2019 (comenta el manifiesto de los 41 senadores, del 24-25/03/2019 según la prensa) | 83 | fijación (solo medidas léxicas: texto breve) |
| `2019-manifiesto-41-senadores-franceses.txt` | 41 senadores franceses, traducción al castellano (traductor sin identificar) | 24-25/03/2019, según la prensa | 211 | fijación (registro institucional y traducido; solo medidas léxicas: texto breve) |

Los dos últimos llegaron en un mismo mensaje de Luis: el comentario es suyo y el manifiesto es el texto que cita. Se guardan por separado para no mezclar autores.

## Pendientes de fecha (no cuentan en el banco)
Un texto sin fecha no puede ser control (regla 1). Mientras Luis no confirme que es anterior a 2023, se guarda en `pendientes-de-fecha/`, se mide y sus resultados se anotan aparte; no entra en los recuentos.

| Archivo | Autor | Fecha | Palabras | Nota |
|---|---|---|---|---|
| `pendientes-de-fecha/sin-fecha-talleres-heriotza.txt` | Luis Beltza | sin fecha | 171 | presentación de los Talleres Heriötza; el original termina cortado en «su importancia gráfic» |
| `pendientes-de-fecha/sin-fecha-no-future-peter-test-tube-babies.txt` | Luis Beltza | sin fecha | 669 | crónica «NO FUTURE · Peter & the Test Tube Babies»; la segunda línea (título del concierto) se mide como párrafo corto |
| `pendientes-de-fecha/sin-fecha-rich-kids-on-lsd-jimmy-jazz.txt` | Luis Beltza | **2025 según el propio texto** («41 años después del lanzamiento de su primer single (1984)»): posterior a 2023, por tanto **no puede ser control** de texto anterior a la IA | 676 | crónica del concierto de Rich Kids on LSD en la Jimmy Jazz |

Los tres textos de ese mensaje de Luis eran dos crónicas y un ensayo («Costra en mi cerebro: Brad Delp»). El ensayo no se guarda: es de procedencia mixta (narra hechos y cita a Cirlot, Smail y Wilson, de fuentes que no se identifican) y no sirve como control de la voz de Luis.
