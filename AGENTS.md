# AGENTS.md

Contexto para agentes de IA que trabajen en este repositorio. Léelo entero antes de tocar nada.

---

## 1. Qué es este proyecto

Un **espejo offline de documentación técnica oficial**, en markdown, con un visor web estático generado a partir de ese markdown.

Existe para poder trabajar sin conexión a internet: viajes, averías de red, caídas de servidor, o bloqueos DNS de operadoras que tumban dominios legítimos (en España ha pasado con rangos de Cloudflare por motivos de retransmisiones deportivas).

No es un proyecto alarmista. Es una red de seguridad que ha resultado útil, y se comparte públicamente para quien la quiera usar.

**Mantenedor:** @raupulus · contacto público: `public@raupulus.dev`

---

## 2. Objetivos permanentes

Se cumplen hoy y deben seguir cumpliéndose con **toda** tecnología que se añada en el futuro. Antes de dar por buena una fuente nueva, comprueba los nueve.

| # | Objetivo | Dónde se garantiza |
|---|---|---|
| 1 | Cada tecnología acaba en markdown en `src/<id>/` | `normalize*` |
| 2 | Cada tecnología acaba en HTML propio en `public/<id>/` | `build.py` |
| 3 | Se puede buscar en cada tecnología por separado | `search.py`, un `_search-index.js` por tecnología |
| 4 | Al terminar se borra todo lo intermedio | `make tidy`, encadenado en `make update` |
| 5 | Un solo comando lo hace todo: `make update` | `Makefile` |
| 6 | Toda la información técnica documentada en `info/` | `info/` |
| 7 | El markdown es legible y procesable por lotes | Front-matter + texto plano, sin HTML incrustado |
| 8 | Lo descargado se considera temporal y se borra | `work/` en `.gitignore` y borrado por `tidy` |
| 9 | En git van resultados y herramientas, no pasos intermedios | `.gitignore` |

Sobre el 9, para que no se vuelva a tocar por error: **`src/` y `public/` SÍ se versionan.** Son los resultados del proyecto. Lo único que no va a git es `work/`, que es lo que se descarga.

Sobre el 7: nada de envolver documentos enteros en un bloque de código. Se hizo con Python y salía un muro monoespaciado ilegible. Los encabezados tienen que ser encabezados de markdown.

---

## 3. Reglas que no se negocian

1. **Solo información pública.** Este directorio se comparte con terceros. Nunca añadas credenciales, tokens, rutas de máquinas privadas, IPs internas, datos personales ni nada que no pueda ser público.
2. **`src/` es la única fuente de verdad.** Todo lo demás se puede borrar y regenerar. Nunca edites `public/` a mano.
3. **Nada de dependencias en tiempo de ejecución.** El visor debe funcionar abriendo un HTML con doble clic, sin servidor, sin Node, sin internet. Cero CDN, cero fuentes remotas, cero analíticas.
4. **Respeta las licencias.** Cada documentación tiene la suya y casi todas exigen atribución. Ver sección 8.
5. **Nunca hagas clones completos de repositorios.** Siempre `--depth 1` y sparse checkout limitado a la carpeta de documentación. Un descuido aquí mete decenas de miles de ficheros basura (ya pasó con Filament: 40 MB frente a 1,5 MB reales).

---

## 3. Arquitectura

Tres capas, tres estados. El flujo va siempre en una dirección:

```
  make fetch          make normalize        make build
     │                     │                     │
     ▼                     ▼                     ▼
┌─────────┐          ┌─────────┐          ┌─────────┐
│  work/  │  ──────► │  src/   │  ──────► │ public/ │
│ clones  │          │markdown │          │  HTML   │
│tarballs │          │canónico │          │ estático│
└─────────┘          └─────────┘          └─────────┘
 desechable          versionado            generado
 gitignored          ★ lo que importa ★    gitignored
```

| Capa | Directorio | Versionado | Se puede borrar |
|---|---|---|---|
| Origen bruto | `work/` | No | Sí, siempre |
| **Markdown canónico** | **`src/`** | **Sí** | **No** |
| Sitio HTML | `public/` | No | Sí, se regenera |

**Por qué están separadas:** cambiar el diseño del visor solo requiere `make build` (segundos, sin red). Cambiar de dónde viene una fuente solo toca `fetch`. Y `git diff src/` muestra exactamente qué cambió en la documentación entre dos actualizaciones, que es información valiosa.

### Estructura de directorios

```
.
├── AGENTS.md              ← este fichero
├── README.md              ← para humanos
├── LICENSES.md            ← licencias de cada documentación
├── ANALISIS-Y-PLAN.md     ← análisis y plan de migración
├── Makefile               ← única interfaz de uso
├── sources.yaml           ← catálogo declarativo de fuentes
├── versions.lock.json     ← generado: commits exactos del último build
│
├── scripts/
│   ├── docsync/
│   │   ├── fetch.py       ← fase 1: red → work/
│   │   ├── normalize.py   ← fase 2: work/ → src/
│   │   ├── build.py       ← fase 3: src/ → public/
│   │   ├── search.py      ← índice de búsqueda
│   │   └── adapters/
│   │       ├── git_markdown.py   ← repos que ya traen markdown
│   │       ├── html_tarball.py   ← PHP, Python, Bash
│   │       └── manpage.py        ← páginas man
│   ├── templates/         ← Jinja2, FUERA del código Python
│   └── assets/            ← CSS, JS y fuentes locales
│
├── bundles/               ← markdown consolidado por tecnología (versionado)
├── src/<tecnologia>/      ← markdown canónico
├── work/                  ← efímero
└── public/                ← generado
```

---

## 4. Cómo añadir una tecnología nueva

**No escribas un script.** Añade una entrada en `sources.yaml`:

```yaml
  livewire:
    name: Livewire
    adapter: git_markdown
    repo: https://github.com/livewire/livewire.git
    ref: "3.x"
    sparse: ["/docs"]
    license: MIT
    homepage: https://livewire.laravel.com/docs
```

Luego: `make fetch-one S=livewire && make normalize && make build`.

Si la fuente no encaja en ningún adaptador existente, escribe uno nuevo en `scripts/docsync/adapters/`. Los adaptadores reciben la entrada de `sources.yaml` y dejan markdown en `src/<id>/`. Esa es toda su responsabilidad.

### Antes de añadir nada, comprueba el formato de origen

| Formato de origen | Adaptador | Coste |
|---|---|---|
| Markdown en un repo git | `git_markdown` | Trivial |
| Texto plano descargable | `plaintext` | Trivial |
| DocBook XML en un repo git | `docbook_xml` + pandoc | Bajo |
| Texinfo | `texinfo` + texi2any + pandoc | Bajo |
| **HTML compilado** | **último recurso** | Ver abajo |
| **reStructuredText de Sphinx** | **evitar** | Ver aviso abajo |

**No hay ningún adaptador de HTML, y es deliberado.** Se llegó a escribir uno y se descartó: obliga a recortar navegación, migas de pan y pie de cada página, y a deshacer maquetación (el manual de PHP metía sus ejemplos en `div.phpcode` con spans de color). Para las tres fuentes que no publican markdown resultó haber siempre una vía mejor: DocBook para PHP, texto plano para Python, Texinfo para Bash. Antes de escribir un adaptador de HTML, agota las alternativas.

> **Aviso verificado (31/07/2026):** convertir `.rst` de Sphinx directamente con pandoc **da mal resultado**. Las directivas se cuelan como HTML crudo en la salida (`<div class="module">`, roles `:func:` sin resolver). Si un proyecto usa Sphinx, **descarga su bundle HTML ya compilado** y convierte desde ahí. Ese es el caso de Python.

### Busca el fuente antes de conformarte con el HTML

Antes de dar por bueno un tarball de HTML, comprueba si el proyecto publica el **fuente** de su documentación en git. Casi siempre existe, y siempre es mejor:

- No hay que recortar navegación, migas de pan ni pie de página.
- No hay maquetación que deshacer.
- Viene de git: clon superficial, commit exacto en `versions.lock.json`, y `git diff` enseña qué cambió.
- Suele traer metadatos que el HTML pierde (versiones, estado de traducción, identificadores canónicos).

Con PHP se empezó por el tarball de HTML y fue un error: el fuente en DocBook (`php/doc-es`) da un resultado mucho más limpio con menos código. El HTML compilado es el último recurso, no el primero.

---

## 5. Formato canónico del markdown en `src/`

Cada `.md` lleva front-matter YAML. Es lo que permite que el mismo fichero sirva a la web, a `grep` y a un modelo de IA local:

```yaml
---
title: Migraciones de base de datos
source_url: https://laravel.com/docs/12.x/migrations
source_repo: laravel/docs
source_ref: 12.x
source_commit: be9d43b
source_path: migrations.md
technology: laravel
version: "12.x"
license: MIT
retrieved_at: 2026-07-31
section: Base de datos
order: 30
---
```

**No inventes valores.** Si un dato no se puede obtener de la fuente, omite la clave; es preferible a rellenarla con algo falso. La trazabilidad es el punto entero de este front-matter.

Además, por cada tecnología:

- **`src/<tec>/_meta.json`** — nombre, versión, licencia, fecha de descarga, URL oficial, número de documentos.
- **`src/<tec>/_toc.json`** — árbol de navegación con el orden real.

### Convenciones de nombres

- Los prefijos numéricos del origen (`01-installation.md`, típico de Filament) **se quitan del nombre** del fichero. El orden se conserva en `_toc.json` y en la clave `order` del front-matter.
- Nombres en minúsculas con guiones. Sin espacios, sin acentos, sin mayúsculas.
- Nunca ficheros con espacios en el nombre. Ya hubo un `md_site_generator BACKUP.py`; no repetir.

---

## 6. El visor web: restricciones técnicas

El visor se abre desde `file://`. Esto impone límites reales que hay que respetar:

1. **`fetch()` y `XMLHttpRequest` están bloqueados sobre `file://`.** El navegador trata cada fichero local como origen opaco.
2. **`<script src="...">` sí funciona.** Por eso el **índice de búsqueda debe emitirse como JavaScript, nunca como JSON**:

   ```javascript
   // public/laravel/_search-index.js
   window.DOCS_INDEX = window.DOCS_INDEX || {};
   window.DOCS_INDEX.laravel = [ /* … */ ];
   ```

   Se carga inyectando un `<script>` al vuelo cuando el usuario busca en esa tecnología. Un índice por tecnología, bajo demanda: no cargues el índice entero de PHP para buscar en Composer.

3. **Todas las rutas deben ser relativas.** Nada de rutas absolutas que empiecen por `/`.
4. **Resaltado de sintaxis en tiempo de build** con Pygments, que genera HTML ya coloreado. Cero JavaScript en el cliente para esto.
5. **Enlaces internos:** el markdown de origen enlaza con `[queues](queues.md)`. El build debe reescribir `.md` → `.html`, o los enlaces quedan rotos.
6. **Título desde el front-matter**, nunca de `basename().capitalize()`. El generador antiguo hacía eso y por eso `http-client.md` aparecía como "Http client".

---

## 7. Comandos

```bash
make update            # reconstrucción completa: fetch + normalize + build + limpieza
make fetch             # descarga todas las fuentes a work/
make fetch-one S=php   # descarga solo una fuente
make normalize         # work/ -> src/
make build             # src/ -> public/
make serve             # servidor local en http://localhost:8080 (opcional)
make check             # valida front-matter, _meta.json y enlaces rotos
make diff              # qué cambió en la documentación desde la última actualización
make clean-work        # borra work/
make bundles           # concatena cada tecnología en un .md para modelos de IA
```

**Cadencia prevista:** una reconstrucción completa cada pocos meses. `make update` tiene que ser suficiente. Si un agente añade un paso manual al proceso, ha fallado en el objetivo.

---

## 8. Licencias

Este repositorio se comparte públicamente. Redistribuir documentación oficial es legítimo, pero **casi todas las licencias exigen mantener la atribución**.

Obligaciones al añadir o modificar una fuente:

1. Registrar la licencia en la clave `license` del front-matter de cada fichero.
2. Añadir una entrada en `LICENSES.md`: licencia, titular del copyright y URL oficial.
3. La portada del sitio debe indicar que es un **espejo no oficial** y enlazar a la documentación original.
4. **No modifiques el contenido de la documentación.** Conversión de formato sí; reescribir, resumir o traducir, no. Debe seguir siendo la doc oficial.

Si no tienes certeza de la licencia de una fuente, **léela en el repositorio de origen antes de añadirla**. No la deduzcas ni la des por supuesta.

---

## 9. Contexto de trabajo del mantenedor

- Desarrollador web senior. PHP, JavaScript y Python. Buen nivel de sistemas, IoT y electrónica.
- Prefiere respuestas claras, directas y sin ambigüedad.
- Crédito: nick **@raupulus**, y `public@raupulus.dev` como único correo público utilizable.

---

## 10. Errores conocidos que no hay que repetir

Historial de este proyecto, para que un agente no vuelva a caer en lo mismo:

| Error | Consecuencia | Prevención |
|---|---|---|
| `git clone` completo de Filament | ~60.000 ficheros de `vendor/` y `node_modules` | Sparse checkout siempre |
| `resources.json` con comas sobrantes | JSON inválido, nunca llegó a usarse | Validar el YAML/JSON en `make check` |
| Plantilla HTML dentro de un string de Python (330 líneas) | Tocar el diseño obligaba a editar código | Plantillas en `scripts/templates/` |
| `md_site_generator BACKUP.py` | Versionado manual con espacio en el nombre | Usar git, no copias |
| Fuente Roboto desde Google Fonts | Una web offline pidiendo a internet | Fuentes locales en `scripts/assets/` |
| README describiendo `scripts/` mientras los scripts estaban en la raíz | Instrucciones que no correspondían con la realidad | Actualizar el README en el mismo commit |
| Guardar HTML generado junto al markdown | Contenido duplicado, sin separar fuente y derivado | `src/` frente a `public/` |

---

## 11. Nota sobre Google Drive

Este directorio puede estar sincronizado con Google Drive, que sincroniza fichero a fichero. Decenas de miles de ficheros pequeños es su peor caso.

Consecuencia práctica: mantén el número de ficheros bajo. `work/` y `public/` están en `.gitignore` precisamente por esto. Si hace falta compartir el sitio generado, comprímelo en un único ZIP en lugar de sincronizar miles de HTML sueltos.

**Además, git puede fallar directamente sobre estas carpetas.** Google Drive y Dropbox montan sistemas de ficheros tipo FUSE que no permiten todas las operaciones de permisos que git necesita; el error típico es `Operation not permitted` al clonar. Si ocurre, saca `work/` fuera de la carpeta sincronizada:

```bash
make update WORK_DIR=/tmp/docs-work
```

`src/` y `public/` no se ven afectados: son ficheros normales que solo se escriben y se leen.


---

## 12. Estado del pipeline

| Fase | Estado | Scripts |
|---|---|---|
| 1 · Base y estructura | Hecha | — |
| 2 · Markdown nativo | Hecha | `fetch.py`, `normalize.py`, `check.py` |
| 3 · Generador de sitio | Hecha | `build.py`, `search.py` |
| 4a · PHP desde DocBook | Hecha | `docbook.py`, `normalize_docbook.py` |
| 4b · Python y Bash | Hecha | `normalize_text.py`, `adapters/archive.py` |
| 5 · Acabado | Hecha | `bundle.py` (bundles IA, RSS 2.0, PWA vanilla, SEO) |

Verificado: 16.577 documentos en 20 tecnologías (Bash, Composer, Debian Reference, Docker, Filament, Git, JavaScript, Laravel, llama.cpp, MicroPython (Pico), Node.js, npm, Nuxt, PHP, pnpm, PostgreSQL, Python, SQLite, Tailwind CSS, Vue 3).

`make test` ejecuta 16 comprobaciones del normalizador sin red ni descargas. Ejecútalo siempre antes de dar por buena una modificación de `normalize.py`.

### Trampas ya resueltas, no reintroducir

| Trampa | Síntoma | Solución aplicada |
|---|---|---|
| Autoescape de Jinja sobre el cuerpo | El documento aparece como HTML literal en pantalla | El cuerpo se envuelve en `Markup()` en `build.py`; el resto sigue escapado |
| Enlaces de referencia `[1]: x.md` | Enlaces rotos en Composer | `RE_MD_REF_LINK` en `normalize.py`, además de la forma en línea |
| Rutas absolutas del sitio oficial | `/docs/{{version}}/container` muerto en local | `RE_HREF_ABS` en `build.py` las traduce a páginas locales |
| Prefijos numéricos en directorios | Carpetas `02-columns/` en Filament | `target_path` los quita también de los segmentos de directorio |
| Enlaces resueltos por slug | Enlaces rotos en pnpm (Docusaurus) | Respaldo por nombre de fichero, solo si es inequívoco |
| Colisión de ruta Apache en Debian (`/javascript`) | Error 404/403 o redirección a `/usr/share/javascript` por el paquete `javascript-common` | La tecnología se nombra canónicamente `js-javascript` en `sources.yaml`, `src/` y `public/` |
| Bloqueo infinito de Pandoc con AsciiDoc (Git) | Pandoc entra en backtracking infinito en `git-config.adoc` con líneas `#` dentro de bloques abiertos `--` | `_sanitize_source` en `normalize_asciidoc.py` sustituye `\n#` por comentarios `\n //` y colapsa `--` antes de invocar pandoc |
| Colisión de notas de versión en Docker (`17.03.md`, `2.x-mac.md`) | Prefijos numéricos con punto se recortaban como ordenación eliminando la versión | `RE_NUMERIC_PREFIX` solo casa con `[-_]`, nunca con `.`; y se gestiona colisión de `_index.md` en segmentos descartados |
| Entidades XML no estándar en PostgreSQL SGML | Pandoc falla con `UnresolvedEntityException` por `&zwsp;` o ficheros obsoletos | Sanitización de entidades no-XML en `docbook.py` antes del parseo |
| Tablas `<ApiTable>` en MDX de Tailwind v4 | La documentación de utilidades quedaba sin tablas de CSS / valores | Parser `convert_api_tables` en `normalize.py` convierte estructuras JS a tablas Markdown estándar |

Al tocar la fase 4, ten en cuenta que `_toc.json` ya trae el árbol de navegación con secciones, títulos y orden resueltos. No hay que deducirlo del sistema de ficheros.

### Limitación conocida

Las ilustraciones de pnpm (`/img/*.svg`) quedan fuera del sparse checkout de su documentación: 15 imágenes rotas, texto completo. Para resolverlo hay que ampliar su `sparse` en `sources.yaml` y copiar los recursos en `build.py`.
