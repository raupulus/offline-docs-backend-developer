# Arquitectura

## Tres capas, una dirección

```
  make fetch          make normalize        make build
     │                     │                     │
     ▼                     ▼                     ▼
┌─────────┐          ┌─────────┐          ┌─────────┐
│  work/  │  ──────► │  src/   │  ──────► │ public/ │
│ clones  │          │markdown │          │  HTML   │
│tarballs │          │canónico │          │ estático│
└─────────┘          └─────────┘          └─────────┘
 desechable          ★ lo que importa ★    generado
```

| Directorio | Versionado | Se puede borrar |
|---|---|---|
| `work/` | No | Siempre |
| **`src/`** | **Sí** | **No** |
| `bundles/` | **Sí** | No (generado canónico) |
| `public/` | No | Sí, se regenera |

Separarlas importa: cambiar el diseño del visor solo requiere `make build`, sin red. Y `git diff src/` enseña exactamente qué cambió en la documentación entre dos actualizaciones.

## Ficheros

```
sources.yaml            catálogo de fuentes
versions.lock.json      commits exactos de la última descarga
requirements.txt        dependencias Python
Makefile                única interfaz de uso

scripts/docsync/
  common.py             configuración, log, utilidades compartidas
  fetch.py              red → work/
  normalize.py          work/ → src/ (markdown nativo) y despacho por adaptador
  normalize_docbook.py  PHP
  normalize_text.py     Python y Bash
  docbook.py            DocBook → markdown
  mdsplit.py            trocear documentos largos por secciones
  build.py              src/ → public/
  search.py             índices de búsqueda
  bundle.py             src/ → bundles/ (markdown consolidado para LLMs)
  check.py              validación
  selftest.py           16 comprobaciones sin red
  adapters/archive.py   descarga y descompresión

scripts/templates/      Jinja2, fuera del código Python
scripts/assets/         CSS y JS locales, sin CDN
```

## Formato canónico

Cada `.md` de `src/` lleva front-matter YAML con título, origen, versión, licencia y fecha. Es lo que permite que el mismo fichero sirva a la web, a `grep` y a un modelo de IA local.

Además, por tecnología: `_meta.json` (versión, licencia, número de documentos) y `_toc.json` (árbol de navegación con secciones y orden ya resueltos).

**No se inventan valores.** Si un dato no se puede sacar de la fuente, se omite la clave. Un `source_url` construido a ojo que devuelve 404 es peor que no poner ninguno.

## Restricciones del visor

Se abre desde `file://` con doble clic. Eso impone:

- Todas las rutas relativas. Nada que empiece por `/`.
- Ningún recurso externo: ni CDN, ni tipografías remotas.
- **El índice de búsqueda es un `.js`, no un `.json`.** Sobre `file://` el navegador bloquea `fetch()` pero permite `<script src>`. Pasarlo a JSON rompería el buscador sin servidor.
- Resaltado de sintaxis con Pygments en tiempo de compilación, cero JavaScript para colorear.

## Comandos

```bash
make            ayuda
make update     reconstrucción completa
make test       16 comprobaciones, sin red, un segundo
make check      valida front-matter y enlaces
make status     qué hay descargado y de qué versión
make diff       qué cambió desde la última actualización
make serve      servidor local en :8080 (opcional)
make clean-all  borra lo generado y la carpeta repos/ antigua
```

Sobre Google Drive o Dropbox, saca `work/` fuera: `make update WORK_DIR=/tmp/docs-work`.
