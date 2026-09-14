# Análisis y plan de reorganización — Documentación offline

**Fecha:** 31 de julio de 2026
**Autor del proyecto:** @raupulus
**Estado:** propuesta, pendiente de aprobación antes de implementar

---

## 1. Diagnóstico de lo que hay hoy

### 1.1 Estructura real encontrada

```
docs/
├── README.md
├── resources.json              ← JSON inválido, sin usar
├── md_site_generator.py        ← generador markdown → HTML
├── md_site_generator BACKUP.py ← copia manual, con espacio en el nombre
├── download_phpdoc.py          ← descarga el manual PHP
├── repos/                      ← clones de repositorios fuente
│   ├── laravel/                ← repo laravel/docs (markdown puro)
│   └── filament/               ← clon COMPLETO, incluye vendor/ y node_modules
└── public/                     ← sitio generado
    ├── laravel/
    ├── filament/
    └── php/                    ← 11.726 ficheros HTML del manual oficial
```

### 1.2 Cifras

| Métrica | Valor |
|---|---|
| Ficheros totales en la carpeta | ~74.200 |
| Ficheros HTML del manual PHP | 11.726 |
| Ficheros que son documentación útil | ~1.500 |
| Ficheros que son ruido (`vendor/`, `node_modules/`, código fuente) | **~60.000** |

**Más del 80% de la carpeta es basura.** El clon de Filament arrastra `vendor/`, `docs-assets/app/vendor/`, `node_modules` y todo el código fuente de los paquetes. La documentación real de Filament son **82 ficheros markdown, 1,5 MB**.

### 1.3 Lo que funciona bien y hay que conservar

- **La idea de fondo es correcta.** Markdown como origen y HTML navegable como salida es exactamente el enfoque adecuado.
- `md_site_generator.py` funciona: agrupa por directorio de primer nivel, genera nav lateral con grupos plegables, es responsive y no depende de CDN salvo la fuente Roboto.
- El manual de PHP descargado de php.net es la doc oficial íntegra y autocontenida.
- Está todo en texto plano y sin dependencias pesadas. Eso es una virtud, no un defecto.

### 1.4 Problemas concretos

| # | Problema | Impacto |
|---|---|---|
| 1 | `repos/filament` clonado entero con `vendor/` | ~60.000 ficheros inútiles; Google Drive sincroniza durante horas |
| 2 | `resources.json` es JSON inválido (comas sobrantes, coma ausente tras `"script": "?"`) y no lo lee nadie | El catálogo de fuentes no existe en la práctica |
| 3 | El README dice que los scripts van en `scripts/`, pero están en la raíz | Instrucciones que no se corresponden con la realidad |
| 4 | `md_site_generator BACKUP.py` | Versionado manual con espacio en el nombre; señal de que falta control de versiones |
| 5 | No hay `index.html` raíz en `public/` | No hay portada única; hay que entrar a mano en cada carpeta |
| 6 | Los pasos de actualización son comandos sueltos copiados del README | Cada reconstrucción es manual y propensa a fallos |
| 7 | No se registra qué versión ni qué fecha tiene cada documentación | Imposible saber si la doc de Laravel es de la 11 o de la 12 |
| 8 | La doc de PHP solo existe en HTML | No es consultable por modelos de IA locales |
| 9 | El HTML generado se guarda junto al markdown | Contenido duplicado, sin separación fuente/derivado |
| 10 | La fuente Roboto se carga desde Google Fonts | Ironía: la web offline hace una petición a internet |

---

## 2. Arquitectura propuesta

### 2.1 Principio rector

> **`src/` en markdown es la única fuente de verdad. Todo lo demás es derivado y desechable.**

Tres capas, tres directorios, tres estados:

| Capa | Directorio | ¿Se versiona? | ¿Se sincroniza a Drive? |
|---|---|---|---|
| Origen bruto (clones, tarballs) | `work/` | No | No |
| **Markdown canónico** | **`src/`** | **Sí** | **Sí** |
| Sitio HTML navegable | `public/` | No | Sí (o se comparte como ZIP) |

Esto resuelve de golpe los problemas 1, 9 y 10: `work/` es efímero y se borra tras cada build, `src/` es ligero y es lo que de verdad importa, y `public/` se regenera cuando haga falta.

### 2.2 Estructura de directorios

```
docs/
├── AGENTS.md                   ← contexto para agentes de IA
├── README.md                   ← para humanos
├── LICENSES.md                 ← licencias de cada documentación incluida
├── Makefile                    ← única interfaz de uso
├── sources.yaml                ← catálogo declarativo de fuentes
├── versions.lock.json          ← generado: qué commit/versión se usó en el último build
│
├── scripts/
│   ├── docsync/
│   │   ├── __init__.py
│   │   ├── fetch.py            ← fase 1: descarga a work/
│   │   ├── normalize.py        ← fase 2: work/ → src/ en markdown
│   │   ├── build.py            ← fase 3: src/ → public/ en HTML
│   │   ├── search.py           ← genera el índice de búsqueda
│   │   └── adapters/           ← un adaptador por tipo de fuente
│   │       ├── git_markdown.py ← repos que ya traen markdown
│   │       ├── html_tarball.py ← PHP, Python, Bash
│   │       └── manpage.py      ← páginas man
│   ├── templates/              ← plantillas Jinja2 fuera del código Python
│   │   ├── base.html
│   │   ├── page.html
│   │   └── index.html
│   └── assets/                 ← CSS y JS propios, fuentes locales
│
├── src/                        ← ★ MARKDOWN CANÓNICO ★
│   ├── php/
│   │   ├── _meta.json
│   │   ├── _toc.json
│   │   └── **/*.md
│   ├── laravel/
│   ├── filament/
│   ├── python/
│   ├── nodejs/
│   ├── npm/
│   ├── pnpm/
│   ├── composer/
│   └── bash/
│
├── work/                       ← efímero, en .gitignore
└── public/                     ← generado, en .gitignore
```

### 2.3 Catálogo declarativo (`sources.yaml`)

Sustituye al `resources.json` roto. Todo lo específico de cada fuente vive aquí, no repartido por scripts:

```yaml
version: 1

sources:
  laravel:
    name: Laravel
    adapter: git_markdown
    repo: https://github.com/laravel/docs.git
    ref: "12.x"                 # fijado a la versión que uso
    include: ["*.md"]
    exclude: ["readme.md", "license.md", "contributions.md"]
    license: MIT
    homepage: https://laravel.com/docs

  filament:
    name: Filament
    adapter: git_markdown
    repo: https://github.com/filamentphp/filament.git
    ref: "4.x"
    sparse: ["/packages/*/docs"]
    strip_prefix: "packages"
    license: MIT
    homepage: https://filamentphp.com/docs

  php:
    name: PHP
    adapter: html_tarball
    url: https://www.php.net/distributions/manual/php_manual_es.tar.gz
    content_selector: "#layout-content"
    drop_selectors: [".navbar", "#breadcrumbs", ".foot", ".usernotes"]
    license: CC-BY-3.0
    homepage: https://www.php.net/manual/es/
```

Añadir una tecnología nueva pasa a ser **una entrada en un YAML**, no escribir un script.

### 2.4 Pipeline de tres fases

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
```

Separar las fases importa porque:

- Si cambias el diseño del visor, solo re-ejecutas `build` (segundos, sin red).
- Si una fuente cambia de sitio, solo tocas `fetch` de esa fuente.
- `src/` se puede revisar con `git diff` antes de regenerar nada: ves exactamente qué cambió en la documentación entre actualizaciones.

### 2.5 Makefile como única interfaz

```makefile
.PHONY: all update fetch normalize build serve clean

all: build

update: fetch normalize build clean-work   ## reconstrucción completa

fetch:          ## descarga fuentes a work/
	python3 -m scripts.docsync.fetch

normalize:      ## work/ -> src/ (markdown)
	python3 -m scripts.docsync.normalize

build:          ## src/ -> public/ (HTML)
	python3 -m scripts.docsync.build

fetch-one:      ## make fetch-one S=laravel
	python3 -m scripts.docsync.fetch --source=$(S)

serve:
	python3 -m http.server -d public 8080

clean-work:
	rm -rf work/

diff:           ## qué cambió en la doc desde la última actualización
	git diff --stat src/
```

Reconstruir todo cada pocos meses pasa a ser: `make update`.

---

## 3. Viabilidad por tecnología

Datos **verificados** clonando cada repositorio el 31/07/2026.

### 3.1 Markdown nativo — coste cero de conversión

| Tecnología | Repositorio | Ruta | Ficheros | Peso | Método |
|---|---|---|---|---|---|
| **Laravel** | `laravel/docs` (`12.x`) | raíz | 103 `.md` | 3,3 MB | `clone --depth 1` |
| **Filament** | `filamentphp/filament` (`4.x`) | `packages/*/docs` | 82 `.md` | 1,5 MB | sparse `--no-cone` |
| **Node.js** | `nodejs/node` (`main`) | `doc/api` | 70 `.md` | 4,4 MB | sparse |
| **npm** | `npm/cli` (`latest`) | `docs/lib/content` | 87 `.md` | 568 KB | sparse |
| **pnpm** | `pnpm/pnpm.io` (`main`) | `docs` | 123 `.md` + 9 `.mdx` | 748 KB | sparse |
| **Composer** | `composer/composer` (`main`) | `doc` | 33 `.md` | 504 KB | sparse |

**Total: 498 ficheros markdown, ~11 MB.** Seis de las nueve tecnologías salen prácticamente gratis.

Detalle importante que cambia todo: el clon sparse de Filament restringido a `/packages/*/docs` baja de **40 MB a 1,5 MB**. Ahí está el 95% del problema actual resuelto con una línea de configuración.

### 3.2 Requieren conversión

#### PHP — viable, es el trabajo más pesado

- Origen: `php_manual_es.tar.gz` de php.net (13,5 MB comprimido, versión de 9 de mayo de 2026).
- El fuente real de la doc PHP es DocBook XML, no markdown. Convertir desde DocBook es frágil por las entidades y los includes.
- **Ruta recomendada: HTML → markdown con pandoc.** He inspeccionado el HTML que ya tienes y es limpio y semántico: `<div id="layout-content">` contiene el cuerpo, con clases `refentry`, `refsect1`, `methodsynopsis`. Se extrae ese div, se descartan navbar y breadcrumbs, y se pasa por `pandoc -f html -t gfm`.
- Volumen: 11.726 ficheros. Con `xargs -P$(nproc)` es cuestión de minutos, no de horas.
- La traducción al español está incompleta en partes; php.net advierte que la versión inglesa es la más precisa. Merece la pena plantearse bajar la inglesa o ambas.

#### Python — viable, pero **no** desde el repositorio

Esto lo he probado y conviene documentarlo para no repetir el error:

Convertir el `.rst` de CPython directamente con pandoc **da mal resultado**. Las directivas de Sphinx no se entienden y se cuelan como HTML crudo en la salida:

```markdown
# `!os.path` --- Common pathname manipulations
<div class="module" data-synopsis="Operations on pathnames.">
os.path
</div>
```

**Ruta recomendada:** descargar el bundle HTML ya compilado de `docs.python.org` (ofrece HTML, texto plano, Texinfo y EPUB) y convertir HTML → markdown. El HTML de Sphinx sí es limpio.

Alternativa aún más simple: el bundle de **texto plano** ya viene legible y es perfectamente utilizable por un modelo local, aunque pierde tablas y enlaces.

#### Bash — viable, la más pequeña

- El manual GNU de Bash está en Texinfo. Pandoc no lee Texinfo, pero sí lee `html` y `man`.
- Dos rutas: convertir el manual HTML de gnu.org, o convertir la página man local con `pandoc -f man -t gfm`.
- Recomiendo el HTML de gnu.org: está estructurado en secciones y sale un markdown navegable.
- Nota: el lector `man` de pandoc existe desde la versión 2.9, que es la que hay disponible. Conviene comprobar la versión instalada en tu máquina.

### 3.3 Resumen de viabilidad

| Tecnología | ¿Web? | ¿Markdown? | Esfuerzo | Riesgo |
|---|---|---|---|---|
| Laravel | ✅ | ✅ nativo | Trivial | Ninguno |
| Filament | ✅ | ✅ nativo | Trivial | Sintaxis propia a limpiar |
| Composer | ✅ | ✅ nativo | Trivial | Ninguno |
| Node.js | ✅ | ✅ nativo | Trivial | Ninguno |
| npm | ✅ | ✅ nativo | Trivial | Ninguno |
| pnpm | ✅ | ✅ nativo | Bajo | 9 ficheros `.mdx` con JSX a limpiar |
| PHP | ✅ | ⚙️ conversión | Alto (volumen) | Traducción ES incompleta |
| Python | ✅ | ⚙️ conversión | Medio | **No usar el `.rst` del repo** |
| Bash | ✅ | ⚙️ conversión | Bajo | Ninguno |

**Las nueve son viables.** Ninguna se queda en "solo estructura vacía".

---

## 4. Formato canónico del markdown en `src/`

Para que sirva igual a la web, a `grep` y a un modelo local, cada `.md` lleva front-matter YAML:

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

Ventajas concretas:

- Un modelo local que lea el fichero sabe de qué versión habla y puede citar la URL oficial.
- El generador de HTML saca de ahí el título y el orden del menú, en vez de adivinarlos a partir del nombre de fichero (que es lo que hace hoy, y por eso `http-client.html` aparece como "Http client").
- `grep -l "version: \"12.x\"" src/**/*.md` te dice al instante qué está desactualizado.

Además, por cada tecnología:

- **`_meta.json`** — nombre, versión, licencia, fecha de descarga, URL oficial, número de documentos.
- **`_toc.json`** — árbol de navegación con el orden real. Resuelve el problema de los prefijos numéricos de Filament (`01-installation.md`): el prefijo se quita del nombre pero el orden se conserva aquí.

---

## 5. El visor web

Has elegido **HTML pre-generado**, que es la decisión correcta para este caso: abre con doble clic, sin servidor, sin Node, sin dependencias. Mejoras sobre el generador actual:

### 5.1 Portada única

`public/index.html` con tarjetas por tecnología mostrando versión y fecha de descarga. Es lo que falta hoy.

### 5.2 Búsqueda que funciona sobre `file://`

Detalle técnico que hay que tener claro desde el principio: sobre `file://` el navegador **bloquea `fetch()` y `XMLHttpRequest`** por política de origen. Pero **sí permite cargar `<script src="...">`**.

Por tanto el índice de búsqueda **no puede ser un `.json` que se descargue con `fetch`**. Tiene que emitirse como JavaScript:

```javascript
// public/laravel/_search-index.js
window.DOCS_INDEX = window.DOCS_INDEX || {};
window.DOCS_INDEX.laravel = [ /* … */ ];
```

y cargarse inyectando un `<script>` al vuelo cuando el usuario busca en esa tecnología. Un índice de títulos + encabezados H2/H3 + primeras palabras de cada sección basta y pesa poco. Índice por tecnología, cargado bajo demanda: no tiene sentido cargar el índice de PHP entero para buscar en Composer.

### 5.3 Otras mejoras del generador actual

- **Plantillas fuera del Python.** Hoy hay 330 líneas de HTML y CSS dentro de un string en `md_site_generator.py`. Sacarlas a `scripts/templates/` permite tocar el diseño sin miedo a romper el código.
- **Fuentes locales.** Quitar la petición a Google Fonts. Una web offline no debería salir a internet ni para una tipografía.
- **Resaltado de sintaxis offline.** Pygments genera el HTML ya coloreado en tiempo de build. Cero JavaScript, cero CDN.
- **Título desde el front-matter**, no desde `basename().capitalize()`.
- **Modo oscuro** con `prefers-color-scheme` y un toggle. Consultar doc a las tantas se agradece.
- **Enlaces internos reescritos.** Hoy un enlace `[queues](queues.md)` dentro del markdown queda roto en el HTML. Hay que reescribir `.md` → `.html` en el build.

---

## 6. Uso con modelos de IA locales

Ésta era una de tus motivaciones y la arquitectura la cubre sin trabajo extra:

- **Búsqueda directa:** `rg "Eloquent" src/laravel/` sobre texto plano, instantáneo.
- **Contexto para el modelo:** cada `.md` es una unidad autocontenida con front-matter que indica versión y fuente. Se pasan ficheros enteros al contexto sin preprocesado.
- **RAG local:** `src/` troceado por encabezados es un corpus listo para vectorizar. El front-matter aporta los metadatos de filtrado (tecnología, versión).
- **Bundles concatenados opcionales:** un `make bundles` que genere `dist/laravel-12.x.md` (los 103 ficheros en uno) es útil para modelos con ventana grande. Barato de añadir.

Con `src/` en ~15-25 MB de texto plano una vez incluidos PHP y Python, todo el corpus cabe holgadamente en cualquier portátil.

---

## 7. Licencias — importante porque lo compartes

El README dice que la carpeta se comparte con más gente. Redistribuir documentación oficial es legítimo, pero **cada una tiene su licencia y casi todas exigen mantener la atribución**. Conviene:

1. Registrar la licencia en el front-matter de cada fichero (ya está en el diseño).
2. Mantener un `LICENSES.md` en la raíz con una entrada por fuente: licencia, titular del copyright y URL oficial.
3. Poner en la portada del sitio un aviso de que es un espejo no oficial, con enlace a la documentación original.

Licencias a verificar y registrar durante la implementación (Laravel, Filament y Composer son MIT; el manual de PHP es Creative Commons; la doc de Python es PSF License v2 según su propia página de copyright; el manual de Bash es GFDL; Node.js y npm hay que confirmarlos leyendo su fichero de licencia). No cuesta nada hacerlo bien y evita problemas al compartir.

---

## 8. Plan de migración por fases

### Fase 1 — Base y limpieza *(la que más aporta por lo poco que cuesta)*

- [ ] `AGENTS.md` con todo el contexto del proyecto
- [ ] `.gitignore` con `work/`, `public/`, `repos/`, `.DS_Store`
- [ ] Convertir la carpeta en repositorio git si no lo es
- [ ] Borrar `repos/` (60.000 ficheros) y `md_site_generator BACKUP.py`
- [ ] `sources.yaml` con las 9 tecnologías
- [ ] `Makefile` con los objetivos principales

**Resultado: de ~74.000 ficheros a unos pocos miles.**

### Fase 2 — Pipeline de markdown nativo

- [ ] `fetch.py` con el adaptador `git_markdown` (sparse + shallow)
- [ ] `normalize.py`: front-matter, `_meta.json`, `_toc.json`
- [ ] Poblar `src/` con Laravel, Filament, Composer, Node.js, npm, pnpm
- [ ] `versions.lock.json`

**Resultado: 6 de 9 tecnologías en markdown canónico.**

### Fase 3 — Generador de sitio

- [ ] Plantillas fuera del código, assets locales
- [ ] Portada única con tarjetas
- [ ] Reescritura de enlaces internos, Pygments, modo oscuro
- [ ] Buscador con índice `.js` compatible con `file://`

**Resultado: web navegable y buscable sin conexión.**

### Fase 4 — Fuentes que requieren conversión

- [ ] Adaptador `html_tarball` con extracción de selector + pandoc
- [ ] PHP (con paralelización)
- [ ] Python (desde el bundle HTML oficial, **no** desde el `.rst`)
- [ ] Bash

**Resultado: las 9 tecnologías completas.**

### Fase 5 — Acabado

- [ ] `LICENSES.md` y avisos de espejo no oficial
- [ ] `make bundles` para modelos de IA
- [ ] `make check` que valide enlaces rotos y front-matter ausente
- [ ] Documentar el proceso de "añadir una tecnología nueva" en el README

---

## 9. Sugerencias adicionales

### 9.1 Google Drive no es el sitio para 74.000 ficheros

Drive sincroniza fichero a fichero. Decenas de miles de ficheros pequeños es el peor caso posible para él, y explica cualquier lentitud que hayas notado. Recomendación:

- El **repositorio git** (con `src/`, scripts y plantillas) vive en GitHub o en tu servidor. Ligero, con historial, y el `git diff` de `src/` te muestra qué cambió en la documentación entre actualizaciones.
- En Drive dejas un único **`docs-offline-2026-07.zip`** con `public/` ya generado. Un fichero grande sincroniza rápido y es lo que de verdad quieres tener a mano en el portátil cuando te quedas sin red.

### 9.2 Fija las versiones, no sigas ramas

`laravel/docs` tiene ramas activas de la 10.x a la 13.x. Si el script clona `master` un día tendrás doc de una versión que no usas. `sources.yaml` fija la rama, y `versions.lock.json` guarda el commit exacto: si un build sale mal, sabes con qué reconstruir el anterior.

### 9.3 Que el build sea idempotente y verificable

Un `make check` que valide que cada tecnología tiene `_meta.json`, que no hay markdown sin front-matter y que no hay enlaces internos rotos. Cuesta poco y evita descubrir el fallo justo el día que no tienes internet, que es precisamente cuando este proyecto tiene que funcionar.

### 9.4 Espacio para documentación propia

Un `src/_notas/` con tus propios apuntes (comandos que siempre olvidas, configuraciones de nginx, snippets) entra en el mismo pipeline y aparece en la misma web. Muchas veces esto acaba siendo la parte más consultada.

### 9.5 Candidatas a añadir más adelante

Mismo coste que las actuales, todas con markdown nativo o conversión sencilla: Livewire, Alpine.js, Tailwind, Vue, Git, Docker, PostgreSQL, MariaDB, Redis, systemd. Y por tu perfil de IoT y electrónica: Raspberry Pi, ESP-IDF, MicroPython, Arduino, PlatformIO. Con `sources.yaml` cada una es una entrada de diez líneas.

### 9.6 Automatización opcional

Si el repositorio acaba en GitHub, una GitHub Action mensual que ejecute `make update` y abra un PR con el diff de `src/` te avisa de qué documentación ha cambiado sin que tengas que acordarte. Y si prefieres no depender de terceros, un `cron` trimestral en tu servidor hace lo mismo.

---

## 10. Resumen ejecutivo

| Aspecto | Hoy | Propuesta |
|---|---|---|
| Ficheros | ~74.200 | ~3.000 en `src/` |
| Fuente de verdad | HTML generado | Markdown en `src/` |
| Tecnologías | 3 | 9 |
| Actualizar | Comandos manuales del README | `make update` |
| Añadir tecnología | Escribir un script Python | Una entrada en `sources.yaml` |
| Buscar | No hay buscador | Índice offline por tecnología |
| Uso con IA local | Imposible (HTML) | Directo (markdown con front-matter) |
| Trazabilidad | Ninguna | Front-matter + `versions.lock.json` |

**Las tres decisiones que más impacto tienen, por orden:**

1. **Sparse checkout en los clones.** Elimina 60.000 ficheros con una línea de configuración por fuente.
2. **`src/` en markdown como fuente única.** Habilita a la vez la web, el `grep` y los modelos locales, sin duplicar nada.
3. **`sources.yaml` + `Makefile`.** Convierte el mantenimiento trimestral en un comando y añadir una tecnología en una entrada de configuración.

---

*Documento generado como paso previo a la implementación. Proyecto de @raupulus.*
