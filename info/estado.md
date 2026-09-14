# Estado

Última actualización: 1 de agosto de 2026

## Funcionando y probado

| Fase | Qué hace |
|---|---|
| 1 · Base | `sources.yaml`, `Makefile`, estructura, `.gitignore` |
| 2 · Markdown nativo | `fetch`, `normalize`, `check` para las 6 fuentes en markdown |
| 3 · Visor | `build`, buscador offline, modo oscuro, código resaltado |
| 4a · PHP | DocBook → markdown |

**Cifras verificadas contra los repositorios reales:**

| Tecnología | Documentos |
|---|---:|
| Laravel | 99 |
| Filament | 82 |
| Composer | 33 |
| Node.js | 70 |
| npm | 87 |
| pnpm | 132 |
| PHP | 1.008 de una muestra; el total son ~11.000 |

Enlaces internos comprobados en el sitio generado: más de un millón, ninguno roto. `make test` pasa 16 comprobaciones sin red.

## Sin probar

**Python y Bash.** El código está escrito e instalado, pero nunca se ha ejecutado con una descarga real: el entorno donde se desarrolló no permitía bajar esos tarballs ni tenía `texi2any`. Puede que haga falta ajustar algo en el primer `make fetch`.

## Pendiente

- Fase 5: `make bundles` (concatenar cada tecnología en un `.md` para modelos de IA)
- Confirmar las licencias marcadas con ⚠️ en `LICENSES.md`, sobre todo la de npm
- Las 15 ilustraciones de pnpm (`/img/*.svg`) salen rotas: están fuera de su carpeta de documentación

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
