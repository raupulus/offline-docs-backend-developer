# Fuentes de documentación

Todas se declaran en `sources.yaml`. Añadir una es añadir una entrada, no escribir código.

## Qué hay ahora

| Tecnología | Origen | Formato | Adaptador | Requiere |
|---|---|---|---|---|
| Laravel | `laravel/docs` | Markdown | `git_markdown` | git |
| Filament | `filamentphp/filament` | Markdown | `git_markdown` | git |
| Composer | `composer/composer` | Markdown | `git_markdown` | git |
| Node.js | `nodejs/node` | Markdown | `git_markdown` | git |
| npm | `npm/cli` | Markdown | `git_markdown` | git |
| pnpm | `pnpm/pnpm.io` | Markdown | `git_markdown` | git |
| PHP | `php/doc-es` + `php/doc-base` | DocBook XML | `docbook_xml` | git, pandoc |
| Python | docs.python.org | Texto plano | `plaintext` | — |
| Bash | ftp.gnu.org | Texinfo | `texinfo` | pandoc, texi2any |

## Idioma

Comprobado repo a repo el 1 de agosto de 2026:

| | Español | Cómo |
|---|---|---|
| PHP | Sí | `php/doc-es`. Para inglés, cambiar a `php/doc-en` |
| Python | Sí | Meter `/es/` en la URL del bundle |
| JavaScript (MDN) | Parcial (495 de 1331) | `mdn/translated-content`, ruta `files/es/web/javascript` |
| Vue, Nuxt, Laravel, Node.js, npm, pnpm, Composer, Filament, Bash | No | Sin traducción oficial mantenida |

De Vue existieron traducciones de la comunidad, pero el repositorio bajo `vuejs-translations` para español ya no está.

Sobre MDN: la traducción cubre el 37%. Se puede tomar el español y dejar el inglés para lo que falte, pero eso requiere superponer dos repositorios en la misma tecnología, que hoy el pipeline no hace. Mientras tanto, o todo en inglés o solo el 37% en español.

## Cómo elegir el formato de origen

Por orden de preferencia:

1. **Markdown en git.** Coste cero.
2. **Texto plano descargable.** Coste cero también. Se envuelve en un bloque literal y listo.
3. **Fuente estructurado en git** (DocBook, Texinfo). Barato y da mejor resultado que cualquier compilado.
4. **HTML compilado.** Último recurso.

**No hay adaptador de HTML, y es a propósito.** Se escribió uno y se tiró: obliga a recortar navegación, migas y pie de cada página, y a deshacer maquetación. Para las tres fuentes sin markdown resultó haber siempre algo mejor. Antes de escribir uno, agota las alternativas.

**Nunca conviertas `.rst` de Sphinx con pandoc.** Las directivas se cuelan como HTML crudo en la salida. Si un proyecto usa Sphinx, busca su bundle de texto plano — casi siempre lo publican.

## Decisiones tomadas y por qué

**PHP: el XML, no el tarball de HTML de php.net.** El HTML compilado mete los ejemplos de código en `div.phpcode` con spans de color y `<br />`, lo que obliga a rearmarlos a mano. El XML es estructura, no presentación. Además viene de git, así que hay commit registrado y `git diff` entre reconstrucciones. De regalo, cada fichero anota el estado de su traducción al español.

**PHP: psysh descartado como fuente.** Su manual es un artefacto derivado, una fila por símbolo con el contenido en HTML, y no incluye los capítulos del lenguaje. Como herramienta de terminal es otra cosa y complementa bien esto.

**Python: texto plano, no HTML.** Se pierde el formato de tablas y los enlaces quedan como texto, pero no hay nada que parsear. Si algún día hace falta más riqueza, se cambia la fuente sin tocar código.

**JavaScript: ruta e identificador `js-javascript` en lugar de `javascript`.** En servidores Linux basados en Debian o Ubuntu con Apache instalado, el paquete del sistema `javascript-common` habilita de forma predeterminada un alias global (`Alias /javascript /usr/share/javascript/`). Para prevenir colisiones en el servidor web que intercepten la ruta y causen errores 403/404 o muestren assets del sistema, la tecnología se identifica canónicamente como `js-javascript`.

## Fijar versiones

`laravel/docs` mantiene varias ramas activas a la vez. `sources.yaml` fija cuál se usa y `versions.lock.json` guarda el commit exacto de la última descarga. Las URLs de Python y Bash llevan el número de versión dentro: hay que subirlas a mano al cambiar de rama.

## Candidatas

Mismo coste que las actuales: Livewire, Alpine.js, Tailwind, Vue, Git, Docker, PostgreSQL, MariaDB, Redis, systemd, nginx. Y por perfil de IoT: Raspberry Pi, ESP-IDF, MicroPython, PlatformIO.
