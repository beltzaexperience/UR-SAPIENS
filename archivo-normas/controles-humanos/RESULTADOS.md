# RESULTADOS.md · qué umbrales saltan en textos humanos

Una fila por medida y por control. «Salta» = ALARMA o AVISO de `ultra-medidas.py --texto`. Banco actual: **1 texto (572 palabras), n insuficiente** (regla 4 de `LEEME.md`): los umbrales de VI.2 no cambian todavía.

## 2019-continente-ur-o-reyno-de-la-mancha.txt (29/10/26)
Medido: 562 palabras de cuerpo, 8 párrafos, 22 frases. De 30 filas medibles: **1 ALARMA y 3 AVISOS**, y ninguna de ellas es un hallazgo real (el texto es humano):

| Norma | Medida | Valor | Estado | Lectura |
|---|---|---|---|---|
| 3 | «aquí» / «aparece» | 1 («De aquí nuestras inmensas capacidades…») | ALARMA | **falso positivo**: «de aquí» consecutivo, no el tic de la Norma 3 |
| 26 | párrafos cortos (≤ 25 palabras) | 1 de 8 (12 %) | AVISO | línea final del texto, sin terminar |
| 10 | gerundio tras coma | 1 | AVISO | «siguiendo la estela de la verdad…», gerundio de modo legítimo |
| 4 | frases con tres o más «y» | 1 | AVISO | enumeración de pares, normal en prosa humana |

Lectura: con un solo texto no se calcula un porcentaje. Pista: las medidas léxicas simples (3, 10, 4) son las que más fácil saltan en humanos. Las medidas de forma con umbral de canon que sí se midieron no saltaron (artículo inicial 27 % frente a alarma 35 %; desviación de frase 13,1 frente a 9,8). **No medidas** en este control: esqueleto repetido (38.1 bis) y sujeto «artículo + sustantivo» (38.1 ter), que exigen la ventana de mil palabras y el analizador sintáctico (el texto tiene 562).
