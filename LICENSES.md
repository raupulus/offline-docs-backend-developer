# Licencias

Este repositorio es un **espejo no oficial** de documentación técnica. Cada documentación conserva la licencia y el copyright de su proyecto de origen. Solo se cambia el formato: el contenido no se reescribe, ni se resume, ni se traduce.

La referencia siempre es el sitio oficial de cada proyecto. Si algo aquí contradice al original, manda el original.

---

## Documentación incluida

> **Estado:** verificación pendiente. Las licencias marcadas con ⚠️ deben confirmarse leyendo el fichero de licencia del repositorio de origen antes de publicar. No deducirlas ni darlas por supuestas.

| Tecnología | Origen | Licencia | Estado |
|---|---|---|---|
| Laravel | [laravel/docs](https://github.com/laravel/docs) | MIT | ⚠️ confirmar |
| Filament | [filamentphp/filament](https://github.com/filamentphp/filament) | MIT | ⚠️ confirmar |
| Composer | [composer/composer](https://github.com/composer/composer) | MIT | ⚠️ confirmar |
| Node.js | [nodejs/node](https://github.com/nodejs/node) | MIT | ⚠️ confirmar |
| npm | [npm/cli](https://github.com/npm/cli) | — | ⚠️ **sin verificar** |
| pnpm | [pnpm/pnpm.io](https://github.com/pnpm/pnpm.io) | MIT | ⚠️ confirmar |
| PHP | [php.net](https://www.php.net/manual/es/) | Creative Commons Attribution | ⚠️ confirmar versión |
| Python | [docs.python.org](https://docs.python.org/3/) | PSF License v2 | ✅ indicado en su página de copyright |
| Bash | [gnu.org](https://www.gnu.org/software/bash/manual/) | GFDL | ⚠️ confirmar versión |

La documentación de Python indica además que los ejemplos y recetas de código están adicionalmente bajo licencia Zero Clause BSD.

---

## Obligaciones al añadir una fuente

Antes de incorporar una documentación nueva:

1. **Leer su licencia** en el repositorio o sitio de origen. No deducirla del lenguaje ni del proyecto.
2. Registrarla en la clave `license` de su entrada en `sources.yaml`.
3. Añadir una fila a la tabla de arriba con el titular del copyright y la URL oficial.
4. Comprobar que la licencia permite la redistribución. Casi todas lo permiten manteniendo la atribución, pero conviene mirarlo.

El pipeline propaga la licencia al front-matter de cada fichero markdown generado, de modo que cualquier documento extraído de aquí lleva consigo su procedencia.

---

## Código del proyecto

Los scripts, plantillas y estilos de este repositorio (todo lo que hay en `scripts/`, más `Makefile` y `sources.yaml`) son obra de [@raupulus](https://github.com/raupulus).

El contenido de `src/` y `public/` **no** es obra del proyecto: es documentación de terceros con las licencias indicadas arriba.
