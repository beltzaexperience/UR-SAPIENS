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

## Pendientes de fecha (no cuentan en el recuento)
### pendientes-de-fecha/sin-fecha-talleres-heriotza.txt (29/10/26)
Texto breve (170 palabras, 3 párrafos, 6 frases), presentación de un taller; el original termina cortado en «gráfic». **0 ALARMAS y 1 AVISO:** años y cifras en el cuerpo (6 cifras: «1 hora y 1/4», «10 €», «3/4 de hora»). Son datos de precio y horario, no cifras de prosa: **falso positivo de la medida** en textos de anuncio. Sin fecha, no cuenta hasta confirmarla.

### pendientes-de-fecha/sin-fecha-no-future-peter-test-tube-babies.txt (29/10/26)
667 palabras de cuerpo, 12 párrafos, 31 frases. **2 ALARMAS y 3 AVISOS** (sin fecha: no cuenta):
| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 3 | «aquí» / «aparece» | 1 | ALARMA | **falso positivo**: «Aquí se acaba la crónica» es una frase humana, no el tic de la norma |
| adenda 17/10 | «alguien» | 1 («Si alguien puede confirmarlo o desmentirlo…») | ALARMA | **falso positivo**: «alguien» en pregunta directa al lector, no voz anónima |
| 26 | párrafos cortos | 2 de 12 (17 %) | AVISO | uno es el título del concierto (línea 2) |
| 10 | gerundio tras coma | 1 | AVISO | |
| 4 | frases con tres o más «y» | 3 | AVISO | |

### pendientes-de-fecha/sin-fecha-rich-kids-on-lsd-jimmy-jazz.txt (29/10/26)
674 palabras de cuerpo, 9 párrafos, 25 frases. **0 ALARMAS y 4 AVISOS:** gerundio tras coma (10), frase con tres o más «que» (41.1), frase con tres o más «y» (4) y años y cifras (3 años y 5 cifras: «1984», «1994», «41 años», nombres de discos: **falso positivo** en una crónica musical). Por su propia fecha (2025) no puede ser control anterior a la IA; ver `LEEME.md`.

Pista (no resultado): con las dos crónicas, las medidas de «aquí» (3) y «alguien» (adenda) vuelven a dar falsos positivos en prosa humana oral, y las de cifras y años (50/56) en textos de crónica y de anuncio.

## Medidas sobre textos de terceros (el texto no se guarda en el repositorio)
### «RAMM: ΣLL: ZΣΣ / Futurismo gótico / Destructor de iconos / Los nombres / Los caminos / Los edificios», de Carlos G. De Marcos (Beltza, 2024) (29/10/26)
Texto de un amigo de Luis, publicado en 2024: **posterior a la IA y de otro autor**, por tanto no es control del banco ni se guarda. Se midieron las primeras 3.597 palabras (hasta «…como un acto político»; el resto no se midió), 12 párrafos largos, 103 frases. **3 ALARMAS y 7 AVISOS** sobre texto humano:

| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 1 | no X, sino Y | 5 | ALARMA | 2 son la antítesis real («No es paranoia, es una construcción mágica»; «no es un nombre, es una fórmula»); las otras 3 son coincidencias del patrón |
| 3 | «aquí» / «aparece» | 4 | ALARMA | el verbo «aparece» en su uso normal y «He aquí» en una cita bíblica: **falsos positivos** |
| 5 | andamios de entrada | 4 | ALARMA | «se trata de», «hay que», «no deberíamos olvidar»: aparecen en prosa ensayística humana |
| 26 | media de palabras por párrafo | 300 | AVISO | párrafos muy largos de ensayo en web |
| 10, 32/32 bis, 41.1, 4, «a veces», 50/56 | gerundio tras coma (6), coberturas (11), frases con tres «que» (13) y tres «y» (10), «a veces» (2), años y cifras (3 y 7) | | AVISO | prosa ensayística larga con citas y paréntesis |

No saltaron: artículo inicial (16 % frente a 35 %), desviación de frase (31,0 frente a 9,8) ni punto y coma (4,4 por mil).

Pista (no resultado): las tres ALARMAS de tics (1, 3, 5) saltan en un ensayo humano de 2024; la norma 3 («aparece»: cero tolerancia) y la 5 (andamios) tienen falsos positivos reales en prosa de ensayo. Esto es lo que la calibración tiene que cuantificar con más textos.
