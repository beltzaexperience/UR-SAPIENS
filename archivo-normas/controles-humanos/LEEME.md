# controles-humanos/

Banco de textos humanos conocidos para calibrar las medidas de tipo M del Relojero Ultra (`NORMA-METODO.md`, VI.2, «Calibración con controles humanos»). Un control sirve para saber **cuánto se equivoca cada medida con un texto que sabemos escrito por una persona**; no es parte del libro ni se corrige.

## Reglas del banco
1. **Solo texto humano anterior a la IA:** textos de Luis fechados antes de 2023 y trozos del canon (Baroja, Orwell, Martín Santos, cuyos textos no se guardan en el repositorio: solo se anotan sus resultados). Cada texto lleva autor, fecha y origen.
2. **Se guardan tal como se escribieron**, con sus erratas y sus defectos. No se corrigen, no se retocan y no se mejoran: un control corregido deja de ser un control.
3. **Parte reservada:** una parte del banco queda reservada y solo sirve para comprobar umbrales ya fijados, nunca para fijarlos.
4. **Tamaño:** con menos de 100 trozos el porcentaje de falsos positivos se anota con «n insuficiente» y los umbrales vigentes no cambian.
5. **Cómo se mide:** `python3 herramientas/ultra-medidas.py archivo-normas/controles-humanos/TEXTO.txt --texto` (primera línea del archivo = título, no se mide). Los resultados se anotan en `RESULTADOS.md`.

## Textos
| Archivo | Autor | Fecha | Palabras | Uso |
|---|---|---|---|---|
| `2019-continente-ur-o-reyno-de-la-mancha.txt` | Luis Beltza | 2019 (antes del 28/04/2019, según el propio texto) | 572 | reservado (comprobación) |
| `sin-fecha-el-reyno-de-la-mancha-quinta-temporada.txt` | Luis Beltza | sin fecha de Luis; por el contenido (Rajoy en activo, el «proceso» en curso) hacia 2017-2018, **por confirmar** | 696 | fijación |
