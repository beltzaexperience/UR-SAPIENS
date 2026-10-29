# controles-humanos/

Banco de textos humanos conocidos para calibrar las medidas de tipo M del Relojero Ultra (`NORMA-METODO.md`, VI.2, «Calibración con controles humanos»). Un control sirve para saber **cuánto se equivoca cada medida con un texto que sabemos escrito por una persona**; no es parte del libro ni se corrige.

## Los textos no están en el repositorio
Los textos de Luis son privados (los escribe para sus amigos, sin presión, y no quiere que sean públicos) y los de terceros son de sus autores. **Ningún texto del banco se guarda en el repositorio**, que es público. Se miden desde fuera del repositorio (`python3 herramientas/ultra-medidas.py ruta/al/texto.txt --texto`; primera línea del archivo = título, no se mide) y aquí solo se anotan los **resultados** (`RESULTADOS.md`), sin citas del texto.

## Reglas del banco
1. **Dos grupos.** **A:** texto humano anterior a la IA (de Luis, fechado antes de 2023, o del canon): fija y comprueba umbrales. **B:** texto humano posterior, **declarado sin IA por su autor**: solo comprueba, nunca fija; su declaración no es un hecho fechable.
2. **Se miden tal como se escribieron**, con sus erratas y sus defectos; un control corregido deja de ser un control.
3. **Parte reservada:** una parte del banco queda reservada y solo sirve para comprobar umbrales ya fijados, nunca para fijarlos.
4. **Tamaño:** con menos de 100 trozos el porcentaje de falsos positivos se anota con «n insuficiente» y los umbrales vigentes no cambian. Los textos de menos de unas 300 palabras solo valen para medidas léxicas.
5. **Textos de terceros:** se miden y se anotan los resultados con autor y año; no se copian al repositorio.

## Textos medidos (sin contenido)
| Id | Autor | Año | Palabras | Grupo | Uso |
|---|---|---|---|---|---|
| T1 | Luis Beltza | 2019 | 572 | A | reservado (comprobación) |
| T2 | Luis Beltza | sin fecha; hacia 2017-2019, **por confirmar** | 696 | A (provisional) | fijación |
| T3 | Luis Beltza | marzo de 2019 | 83 | A | fijación (texto breve: solo medidas léxicas) |
| T4 | 41 senadores franceses (manifiesto, traducido) | 24-25/03/2019, según la prensa | 211 | A | fijación (registro institucional; texto breve) |
| T5 | Luis Beltza | sin fecha | 171 | B | comprobación (texto breve) |
| T6 | Luis Beltza | sin fecha | 669 | B | comprobación |
| T7 | Luis Beltza | 2025 (lo dice el propio texto) | 676 | B | comprobación |
| T9 | Carlos G. De Marcos, artículo publicado en Beltza (18/06/2010) | 2010 (fecha pública, comprobable) | 1.648 | A | reservado (comprobación) |
| T10 | Luis Beltza, sus comentarios públicos en esa página (18/06 a 05/07/2010) | 2010 (fecha pública, comprobable) | 819 | A | fijación (formato de comentarios: solo medidas léxicas) |
| T8 | Carlos G. De Marcos (publicado en Beltza) | 2024 | 3.597 medidas | B | comprobación |

Banco del grupo A: T1 a T4, T9 y T10 (4.029 palabras). T9 y T10 son los primeros con fecha **pública y comprobable** (Beltza, 2010). T2 pasa al grupo B si Luis no confirma una fecha anterior a 2023. T8 es de un tercero y se midió sin copiarlo.
