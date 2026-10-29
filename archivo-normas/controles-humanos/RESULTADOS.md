# RESULTADOS.md · qué umbrales saltan en textos humanos

Una fila por medida y por control (los textos están descritos en `LEEME.md`, sin su contenido). «Salta» = ALARMA o AVISO de `ultra-medidas.py --texto`. Banco del grupo A: **4 textos (1.562 palabras), n insuficiente** (regla 4 de `LEEME.md`): los umbrales de VI.2 no cambian todavía.

## Resultados por texto (29/10/26)
| Id | Palabras de cuerpo | Alarmas | Avisos | Qué saltó |
|---|---|---|---|---|
| T1 | 562 | 1 | 3 | norma 3 (falso positivo: «aquí» en la locución «de aquí»); 26 párrafos cortos (línea final sin terminar); 10 gerundio tras coma; 4 frases con tres «y» |
| T2 | 689 | 2 | 6 | 26 párrafos cortos (línea de despedida); 1 «no X, sino Y» (**falso positivo del patrón**: casó «no es …, que es …»); 26 media por párrafo (138); 10 gerundio; 32/32 bis coberturas (3); 4 frases con tres «y» (3); 50/56 cifras (**falso positivo**: un número que forma parte de un nombre) |
| T3 | 81 | 0 | 2 | 26 media por párrafo (2 párrafos); 4 frase con tres «y» |
| T4 | 209 | 1 | 2 | 26 párrafos cortos (2 de 7); 26 media por párrafo; 36.8 punto y coma (19,1 por mil: viñetas terminadas en «;»); todo por la estructura de lista |
| T5 | 170 | 0 | 1 | 50/56 cifras (**falso positivo**: precio y horario en un anuncio) |
| T6 | 667 | 2 | 3 | 3 «aquí» (**falso positivo**: «Aquí se acaba…»); adenda 17/10 «alguien» (**falso positivo**: pregunta directa al lector); 26 párrafos cortos (17 %, uno es el título); 10 gerundio; 4 frases con tres «y» |
| T7 | 674 | 0 | 4 | 10 gerundio; 41.1 frase con tres «que»; 4 frase con tres «y»; 50/56 cifras (**falso positivo**: años y nombres de discos en una crónica musical) |
| T8 | 3.597 | 3 | 7 | ver abajo |

## T8 (ensayo de Carlos G. De Marcos, 2024; primeras 3.597 palabras; no se copia)
| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 1 | no X, sino Y | 5 | ALARMA | 2 son la antítesis real; las otras 3, coincidencias del patrón |
| 3 | «aquí» / «aparece» | 4 | ALARMA | el verbo «aparece» en su uso normal y «He aquí» en una cita bíblica: **falsos positivos** |
| 5 | andamios de entrada | 4 | ALARMA | «se trata de», «hay que», «no deberíamos olvidar»: aparecen en prosa ensayística humana |
| 26 | media de palabras por párrafo | 300 | AVISO | párrafos muy largos de ensayo en web |
| 10, 32/32 bis, 41.1, 4, «a veces», 50/56 | gerundio (6), coberturas (11), tres «que» (13), tres «y» (10), «a veces» (2), años y cifras (3 y 7) | | AVISO | prosa ensayística larga con citas y paréntesis |

No saltaron: artículo inicial (16 % frente a 35 %), desviación de frase (31,0 frente a 9,8) ni punto y coma (4,4 por mil).

## Cuántos controles disparan cada medida (grupo A, n = 4, insuficiente)
| Norma | Medida | Salta en | Estado |
|---|---|---|---|
| 26 | párrafos cortos (≤ 25 palabras) | 3 de 4 | efecto de líneas finales, frases sueltas y viñetas |
| 26 | media de palabras por párrafo | 3 de 4 | AVISO: párrafos largos o textos de pocos párrafos |
| 4 | frases con tres o más «y» | 3 de 4 | AVISO |
| 10 | gerundio tras coma | 2 de 4 | AVISO |
| 3 | «aquí» / «aparece» | 1 de 4 | falso positivo |
| 1 | no X, sino Y | 1 de 4 | falso positivo del patrón |
| 32/32 bis | coberturas | 1 de 4 | AVISO |
| 50/56 | años y cifras | 1 de 4 | falso positivo |
| 36.8 | punto y coma por mil palabras | 1 de 4 | AVISO: viñetas con «;» |

## Pista (no resultado)
- Las medidas de **párrafo** (26) y de **«y»** (4) saltan en tres de cuatro textos del grupo A y las de **gerundio** (10) en dos: son las más sensibles al género (blog, lista, texto breve).
- Las medidas de **tics** 1, 3 y 5 saltan en el ensayo de 2024 (T8) y las 3 y «alguien» en una crónica (T6): tienen falsos positivos reales en prosa humana de ensayo y de crónica.
- Cuatro de los falsos positivos son defectos de la propia medida (patrón «no X, sino Y»; un número dentro de un nombre contado como cifra; cifras de precio, horario, años y discos). Convendrá afinarla cuando haya más textos.
- Los textos de menos de unas 300 palabras solo sirven para medidas léxicas.
