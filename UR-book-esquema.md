# NOTAS-UR-SAPIENS-HTML.md

## Documento maestro técnico
Fuente de verdad única para HTML, CSS, JS, maquetación, orden del sitio y control visual del UR-book.

---

## 1. Finalidad de este archivo

Este documento reúne la parte técnica del proyecto UR-SAPIENS: estructura del sitio, orden del DOM, CSS, márgenes, marquees, sidebars, artículos, imágenes, vídeos, comportamiento móvil y reglas de mantenimiento.

No trata el método editorial general ni la lectura conceptual profunda del libro. Esa parte pertenece a `NOTAS-UR-SAPIENS.md`.  
Aquí vive lo que hace funcionar el sitio.

---

## 2. Regla de separación

Hay dos niveles distintos de trabajo:

- **Archivo editorial**: contexto, método, criterios de corrección, voz y lectura.
- **Archivo técnico**: HTML, CSS, JS, estructura, comportamiento, compatibilidad y publicación.

No se mezclan.  
Si se cambia una parte técnica, debe mantenerse la coherencia visual y funcional del conjunto.

---

## 3. Estructura fija del sitio

El sitio sigue siempre este orden:

1. Topband.
2. Brand-slash rojo.
3. Separador negro.
4. Foto Nervión a ancho completo.
5. Separador negro.
6. Marquee de texto fijo superior.
7. Separador negro.
8. PC₁: símbolo + título fit-to-width.
9. Marquee de fotos, clic pausa/reanuda.
10. Separador negro.
11. UR-BOOK wrapper.
12. Feed principal con artículos.
13. Sidebar con índice y buscador.
14. Separador negro.
15. Marquee rojo fijo inferior.
16. Separador negro.
17. Foto Oteiza Arantzazu.
18. Brand-slash footer.
19. Footer final.

Esta secuencia no debe alterarse salvo decisión expresa.

---

## 4. Dos archivos de publicación

### 4.1 `index.html`
Versión limpia para GitHub Pages.  
Debe enlazar su CSS externo y mantenerse estable como versión pública.

### 4.2 `index-local.html`
Versión de trabajo local con CSS inlineado.  
Sirve para revisar el resultado sin depender de servidor.

La regla es clara: el contenido debe ser el mismo; cambia solo de dónde sale el CSS.

---

## 5. CSS y paleta

La paleta del proyecto es la misma de Magic Bus y Beltza Experience:

- `--black: #0a0a0a`
- `--white: #f2ede6`
- `--red: #b01a1a`
- `--amber: #c8922a`
- `--muted: #666`
- `--cream: #f0e8d8`

Tipografías:
- **Bebas Neue**: titulares, etiquetas, marquees.
- **Courier Prime**: cuerpo, captions, índice.
- **Playfair**: pullquotes y paginaciones.

El fondo de papel debe mantenerse como textura continua donde toque:
- en cada `<article>`,
- en el interior del sidebar,
- y en `.ur-main`.

No debe sustituirse por un `<main>` global que borre instancias.

---

## 6. Marquees

