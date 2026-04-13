# UR-SAPIENS — Notas de Diseño y Estructura
**Título completo:** UR: TECHNOVISION Y COSMOGONÍA DE UN HALLAZGO DE PALEOLINGÜÍSTICA Y SU POSTERIOR US-UR-PACIÓN SISTÉMICA  
**Subtítulo:** El Último Apóstol  
**URL prevista:** https://beltzaexperience.github.io/UR-SAPIENS/  
**Repo:** https://github.com/beltzaexperience/UR-SAPIENS (pendiente de crear)  
**Autor:** Luis Beltza · Doneztebe, Nafarroa  
**Estado:** archivo local recuperado, algunas fotos perdidas  

---

## Archivos necesarios
- `index.html` — estructura completa (recuperada)
- `style.css` — CSS externo (pendiente de recuperar/recrear)
- Fotos propias alojadas en Flickr (cuenta beltzascene2)
- Símbolo UR-SAPIENS: https://live.staticflickr.com/65535/55173125591_3066404ecb_o.png
- Puño Beltza: https://beltzaexperience.github.io/Manifiesto-Beltza/beltza-puno.png

---

## Colores
```
--black:  #0a0a0a
--white:  #f2ede6
--red:    #b01a1a  (color principal UR — mismo que Manifiesto)
--amber:  #c8922a
--muted:  #666
Fondo artículos: crema/blanco #f5f0e8 o similar
Texto artículos: #1a1a1a o #333 (casi negro sobre fondo claro)
```

---

## Tipografías
Mismas que Manifiesto y Magic Bus:
- **Bebas Neue** — topband, brand-slash, títulos secciones, marquees, índice
- **Playfair Display** — citas destacadas en itálica
- **Courier Prime** — cuerpo de texto de todos los artículos

---

## Fonema UR
**Regla fundamental del proyecto:** toda aparición del fonema "ur" va en rojo `#b01a1a`.  
Ejemplos: NAT-**UR**-ALEZA, **UR**-UMEA, US-**UR**-PACIÓN, B-**UR**-OCRACIA, escri-T-**UR**-A, Ag-**UR**, etc.

---

## Estructura general (de arriba a abajo)

1. **Topband** — BELTZA RECORDS · DONOSTIA _ DONEZTEBE | links a los 3 proyectos
2. **Brand-slash** — UR (negro sobre rojo) + SAPIENS (rojo sobre negro) + símbolo UR + puño
3. **Línea negra separadora** — `clamp(0.5rem,2vw,1.75rem)`
4. **Foto apertura** — Nervión Two Tone[ismo] · Koldo Roteta (ancho completo)
5. **Línea negra separadora**
6. **Marquee UR** — fondo rojo, texto crema, 80s, palabras con fonema UR
7. **Línea negra separadora**
8. **PC₁ — Portada principal** — símbolo + título fit-to-width + texto introducción
9. **Marquee fotos** — ~20 fotos Flickr, borde rojo 10px, pausable con click
10. **Artículos** — layout flex: sidebar izquierda (índice) + contenido principal
11. **Marquee UR inferior** — igual que el superior, 40s
12. **Línea negra separadora**
13. **Foto Oteiza Arantzazu** — "El Último Apóstol", ancho completo
14. **Brand-slash inferior** — BELTZA/RECORDS + puño + símbolo UR
15. **Footer** — links a los 3 proyectos

---

## PC₁ — Portada principal
- Fondo: crema/blanco
- Símbolo UR a la izquierda: `clamp(260px,35vw,500px)`
- Título a la derecha: fit-to-width con JS (el texto llena exactamente el ancho)
  - Línea 1: **UR**: COSMOGONÍA
  - Línea 2: PALEOLINGÜÍSTICA
  - Línea 3: US-**UR**-PACIÓN SISTÉMICA
  - Bordes laterales rojos 3px
- Texto introductorio debajo: Courier Prime, fondo crema
- Firma: **· Luis Gonzaga Roteta ·** en ámbar, Bebas Neue, alineado a la derecha

---

## Layout artículos
```
display: flex
├── aside (sidebar izquierda) — índice navegable con buscador
└── main (contenido) — artículos con id para anclar desde índice
```

### Sidebar / Índice
- Buscador de entradas
- Letras A-Z como separadores (`.il`)
- Entradas normales (`.ie`) — links a artículos
- Entradas Dadá-UR (`.ie-dada`) — estilo especial
- Función `burFiltrar()` — filtra entradas al escribir
- ~371 entradas documentadas

### Artículos — estructura tipo
- Label categoría: ATLAS UR GLOBAL / DOCUMENTADO / ESPECULACIÓN RAZONADA
- Título H2: Bebas Neue, `clamp(2rem,5vw,5rem)`, color #1a1a1a
- Subtítulos H3: Bebas Neue, rojo
- Cuerpo: Courier Prime, 1.15rem, line-height 2.05, color #333
- Citas destacadas: border-left rojo, fondo rgba(176,26,26,0.04), itálica
- Artefactos Dadá-UR: borde izquierdo rojo tenue, fondo rgba(176,26,26,0.02)
- Glosario al final: `.glosario` con lista numerada
- Pie de página artículo: · Pág. N · UR + E=mc² = SAPIENS

---

## Artículos identificados en el archivo
- **pub-intro** — Introducción general
- **pub-asia** — Eusko-Finés Asiático Oriental · Japonés · Altaico · Ainu · K-UR-osawa
- **pub-cosmos** — (pendiente ver contenido)
- Y muchos más accesibles desde el índice

### Artículos con fotos perdidas (pendiente restaurar)
- Algunos artículos tienen imágenes de fuentes externas que pueden haberse roto
- Las fotos propias en Flickr (cuenta beltzascene2) siguen activas

---

## Marquee UR — contenido
```
NAT-UR-ALEZA · UR · B-UR-OCRACIA · US-UR-PACIÓN · K-UR-DISTÁN · UR-UMEA · 
SISTEMA MUNDO · HÍDRICA · COSMOGONÍA · PALEOLINGÜÍSTICA · SANSINENEA · 
BRIGADAS INTERESTELARES · EL-UR · UR-LAÑO · E-UR-I · IT-UR-I · UR-A · 
URARTU · URUGUAY · URUBAMBA · URANO · MERCURIO · ADN · SAPIENS · 
EXTRATERRESTRE · INTUICIÓN · ETIMOLOGÍA · TOPONIMIA · HUMOR · O-UR-RENSE · 
NATURA · NATURE · NATURALEZA · COSMOS · TIERRA · AGUA · LUR · SATURNO · 
NABU · NABIA · TARTESSOS · SUMERIA · METALURGIA · AURORA · ABISMO · 
T-UR-ISMO · COLUMNA DURRUTI · SHARP · G-UR-Ú · F-UR-OR · UR-DIMBRE · 
ROTETA · MALERREKA · BAS-UR-A-PIENS · MICROPLÁSTICOS · FREE COSMIC UR · 
SUN RA · HAWKWIND · DERRIBOS ARIAS · TSUNAMI DE UR
```

---

## Fotos marquee principal (Flickr)
- Doneztebe
- NATURAL · Os Garabatos
- UR-SAPIENS (símbolo)
- La Naranja Mecánica · Jardines de Júpiter
- Miño · O-UR-ense (serie: ~12 fotos del río)
- UR-UMEA
- UR-Sapiens Acupuntado (foto Luis Beltza)
- Foto Oteiza Arantzazu (al final, ancho completo)

---

## Proyectos relacionados
- **Manifiesto:** https://github.com/beltzaexperience/Manifiesto-Beltza
- **Magic Bus:** https://github.com/beltzaexperience/magic-bus
- **Beltza Records:** https://www.beltzarecords.com

---

## Pendientes
- Crear repo `beltzaexperience/UR-SAPIENS` en GitHub
- Recuperar/recrear `style.css`
- Identificar y restaurar fotos perdidas en artículos
- Revisar todos los links del índice (algunos apuntan a `#pub-intro` como placeholder)
- Subir a GitHub Pages
