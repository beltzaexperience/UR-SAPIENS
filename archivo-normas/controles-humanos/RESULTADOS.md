# RESULTADOS.md · qué umbrales saltan en textos humanos

Una fila por medida y por control. «Salta» = ALARMA o AVISO de `ultra-medidas.py --texto`. Banco actual: **2 textos (1.268 palabras), n insuficiente** (regla 4 de `LEEME.md`): los umbrales de VI.2 no cambian todavía.

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

## Cuántos controles disparan cada medida (n = 2, insuficiente)
| Norma | Medida | Salta en | Estado |
|---|---|---|---|
| 26 | párrafos cortos (≤ 25 palabras) | 2 de 2 | efecto de la línea final de despedida o de la frase suelta |
| 10 | gerundio tras coma | 2 de 2 | AVISO en ambos |
| 4 | frases con tres o más «y» | 2 de 2 | AVISO en ambos |
| 3 | «aquí» / «aparece» | 1 de 2 | falso positivo («de aquí») |
| 1 | no X, sino Y | 1 de 2 | falso positivo del patrón |
| 26 | media de palabras por párrafo | 1 de 2 | AVISO |
| 32/32 bis | coberturas | 1 de 2 | AVISO |
| 50/56 | años y cifras | 1 de 2 | falso positivo («Felipe 6») |

Pista (no resultado): tres medidas saltan en los dos textos humanos (26, 10 y 4), lo que sugiere umbrales demasiado estrictos para prosa de blog, y dos de los falsos positivos son defectos de la propia medida (patrón «no X, sino Y»; «Felipe 6» como cifra), que conviene afinar cuando haya más textos.
