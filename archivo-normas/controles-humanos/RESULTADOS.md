# RESULTADOS.md · qué umbrales saltan en textos humanos

Una fila por medida y por control. «Salta» = ALARMA o AVISO de `ultra-medidas.py --texto`. Banco actual: **4 textos (1.562 palabras), n insuficiente** (regla 4 de `LEEME.md`): los umbrales de VI.2 no cambian todavía.

## 2019-continente-ur-o-reyno-de-la-mancha.txt (29/10/26)
Medido: 562 palabras de cuerpo, 8 párrafos, 22 frases. De 30 filas medibles: **1 ALARMA y 3 AVISOS**, y ninguna de ellas es un hallazgo real (el texto es humano):

| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 3 | «aquí» / «aparece» | 1 («De aquí nuestras inmensas capacidades…») | ALARMA | **falso positivo**: «de aquí» consecutivo, no el tic de la Norma 3 |
| 26 | párrafos cortos (≤ 25 palabras) | 1 de 8 (12 %) | AVISO | línea final del texto, sin terminar |
| 10 | gerundio tras coma | 1 | AVISO | «siguiendo la estela de la verdad…», gerundio de modo legítimo |
| 4 | frases con tres o más «y» | 1 | AVISO | enumeración de pares, normal en prosa humana |

Lectura: con un solo texto no se calcula un porcentaje. Pista: las medidas léxicas simples (3, 10, 4) son las que más fácil saltan en humanos. Las medidas de forma con umbral de canon que sí se midieron no saltaron (artículo inicial 27 % frente a alarma 35 %; desviación de frase 13,1 frente a 9,8). **No medidas** en este control: esqueleto repetido (38.1 bis) y sujeto «artículo + sustantivo» (38.1 ter), que exigen la ventana de mil palabras y el analizador sintáctico (el texto tiene 562).

## sin-fecha-el-reyno-de-la-mancha-quinta-temporada.txt (29/10/26)
Medido: 689 palabras de cuerpo, 5 párrafos, 43 frases. De 30 filas medibles: **2 ALARMAS y 6 AVISOS** sobre texto humano:

| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 26 | párrafos cortos (≤ 25 palabras) | 1 de 5 (20 %) | ALARMA | línea final de despedida («Tal vez siga…o no, soy de Ourense hermanos. Un placer.») |
| 26 | media de palabras por párrafo | 138 | AVISO | cuatro párrafos largos de blog |
| 1 | no X, sino Y | 1 («…su vieja, que no es tonta, que es griega…») | ALARMA | **falso positivo de la medida**: el patrón casa «no es … es», no «no X, sino Y» |
| 10 | gerundio tras coma | 1 («haciendo de Mariano, nos tiene…») | AVISO | gerundio de modo legítimo |
| 32/32 bis | coberturas | 3 en 43 frases («parece», «tal vez») | AVISO | pocas y con sentido |
| 4 | frases con tres o más «y» | 3 | AVISO | enumeraciones |
| 50/56 | años y cifras en el cuerpo | 5 cifras («500», «19», «Felipe 6» tres veces) | AVISO | «Felipe 6» es un nombre, no una cifra: **falso positivo de la medida** |

## 2019-reyno-de-la-mancha-va-bien.txt (29/10/26)
Texto breve (81 palabras, 2 párrafos, 4 frases): solo valen las medidas léxicas. **0 ALARMAS y 2 AVISOS:** media de palabras por párrafo (40; el texto son dos párrafos) y una frase con tres o más «y» («…ganarlo por goleada con absoluta limpieza y aprobar…»).

## 2019-manifiesto-41-senadores-franceses.txt (29/10/26)
Texto breve, traducido, de registro institucional (209 palabras, 7 párrafos, 8 frases): **1 ALARMA y 2 AVISOS** sobre texto humano. Los tres son efecto de la estructura de lista con viñetas «.-»: párrafos cortos (2 de 7, 29 %), media de palabras por párrafo (30) y punto y coma por mil palabras (19,1, por las viñetas que terminan en «;»).

## Cuántos controles disparan cada medida (n = 4, insuficiente)
| Norma | Medida | Salta en | Estado |
|---|---|---|---|
| 26 | párrafos cortos (≤ 25 palabras) | 3 de 4 | efecto de líneas finales, frases sueltas y viñetas |
| 26 | media de palabras por párrafo | 3 de 4 | AVISO: párrafos largos de blog o textos de pocos párrafos |
| 4 | frases con tres o más «y» | 3 de 4 | AVISO |
| 10 | gerundio tras coma | 2 de 4 | AVISO |
| 3 | «aquí» / «aparece» | 1 de 4 | falso positivo («de aquí») |
| 1 | no X, sino Y | 1 de 4 | falso positivo del patrón |
| 32/32 bis | coberturas | 1 de 4 | AVISO |
| 50/56 | años y cifras | 1 de 4 | falso positivo («Felipe 6») |
| 36.8 | punto y coma por mil palabras | 1 de 4 | AVISO: viñetas con «;» |

Pista (no resultado): las medidas de **párrafo** (26) y de **«y»** (4) saltan en tres de cuatro textos humanos y las de **gerundio** (10) en dos; son las más sensibles al género (blog, lista, texto breve). Dos de los falsos positivos son defectos de la propia medida (patrón «no X, sino Y»; «Felipe 6» como cifra). Los textos de menos de unas 300 palabras solo sirven para medidas léxicas; para fijar umbrales de forma hacen falta trozos de unas 1.000 palabras.
