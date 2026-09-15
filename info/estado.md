# Estado

Última actualización: 14 de septiembre de 2026

## Funcionando y probado

| Fase | Qué hace |
|---|---|
| 1 · Base | `sources.yaml`, `Makefile`, estructura, `.gitignore` |
| 2 · Markdown nativo | `fetch`, `normalize`, `check` para las fuentes en markdown |
| 3 · Visor | `build`, buscador offline, modo oscuro, código resaltado con Pygments |
| 4a · PHP | DocBook XML (`doc-es`) → markdown |
| 4b · Python y Bash | Python compilado limpio y Bash desde Texinfo oficial de GNU |
| 5 · Acabado | `make bundles` (12 archivos .md para IA/offline), RSS 2.0, Sitemap.xml, PWA vanilla, SEO |

**Cifras verificadas contra los repositorios reales:**

| Tecnología | Documentos |
|---|---:|
| Bash | 70 |
| Composer | 33 |
| Filament | 82 |
| JavaScript | 1.331 |
| Laravel | 101 |
| Node.js | 70 |
| npm | 87 |
| Nuxt | 261 |
| PHP | 11.000 |
| pnpm | 140 |
| Python | 536 |
| Vue 3 | 109 |
| **Total** | **13.820 documentos** |

Enlaces internos comprobados en el sitio generado: ninguno roto. `make test` pasa 16 comprobaciones sin red.

## Pendiente

- Las 15 ilustraciones de pnpm (`/img/*.svg`) salen rotas: están fuera de su carpeta de documentación en el sparse checkout

## Historial de decisiones

| Cuándo | Qué se decidió |
|---|---|
| Inicio | Markdown como fuente única, HTML pre-generado como salida |
| Fase 4 | PHP desde DocBook y no desde el tarball de HTML de php.net |
| Fase 4 | Descartado psysh como fuente: es un derivado y no cubre el lenguaje |
| Fase 4 | Eliminado el adaptador de HTML: Python pasa a texto plano y Bash a Texinfo |

## Trampas ya resueltas

No reintroducir:

| Trampa | Solución |
|---|---|
| Clon completo de Filament (60.000 ficheros de `vendor/`) | Sparse checkout siempre |
| Autoescape de Jinja sobre el cuerpo del documento | `Markup()` en `build.py` |
| Índice de búsqueda como `.json` | Debe ser `.js`: `fetch()` está bloqueado en `file://` |
| Enlaces de referencia `[1]: x.md` sin reescribir | `RE_MD_REF_LINK` en `normalize.py` |
| Rutas absolutas del sitio oficial muertas en local | `RE_HREF_ABS` en `build.py` |
| Prefijos numéricos en directorios | `target_path` los quita también de los segmentos |
| `source_url` construido a ojo | Se usa el `xml:id` real del documento |
