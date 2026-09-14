# Licencias y Atribución

Este repositorio y el sitio web en [docs.raupulus.dev](https://docs.raupulus.dev) constituyen un **espejo no oficial** de documentación técnica de referencia. 

Cada documentación incluida conserva íntegramente la autoría, el copyright y los términos de licencia de su respectivo proyecto de origen. La labor de este proyecto se limita estrictamente a la adaptación técnica de formato (conversión a Markdown unificado y compilación en visor web estático sin dependencias de red); el contenido no ha sido reescrito, ni resumido, ni alterado en su significado técnico.

La fuente canónica siempre es el sitio oficial de cada tecnología. Si existiese cualquier discrepancia o desactualización, prevalece siempre la documentación original.

---

## Catálogo de Documentación y Licencias

Todas las fuentes han sido verificadas contra sus repositorios oficiales y términos de licencia vigentes:

| Tecnología | Titular del Copyright / Autores | Origen canónico | Licencia aplicable |
|---|---|---|---|
| **Bash** | Free Software Foundation, Inc. (Chet Ramey, Brian Fox) | [GNU Bash Manual](https://www.gnu.org/software/bash/manual/) | [GFDL-1.3](https://www.gnu.org/licenses/fdl-1.3.html) |
| **Composer** | Nils Adermann, Jordi Boggiano y colaboradores de Composer | [composer/composer](https://github.com/composer/composer) | [MIT](https://opensource.org/licenses/MIT) |
| **Filament** | Dan Harrin y colaboradores de Filament | [filamentphp/filament](https://github.com/filamentphp/filament) | [MIT](https://opensource.org/licenses/MIT) |
| **JavaScript** | Individual Mozilla Contributors (MDN Web Docs) | [mdn/content](https://github.com/mdn/content) | [CC-BY-SA-2.5](https://creativecommons.org/licenses/by-sa/2.5/) |
| **Laravel** | Taylor Otwell | [laravel/docs](https://github.com/laravel/docs) | [MIT](https://opensource.org/licenses/MIT) |
| **Node.js** | Joyent, Inc., OpenJS Foundation y colaboradores de Node.js | [nodejs/node](https://github.com/nodejs/node) | [MIT](https://opensource.org/licenses/MIT) |
| **npm** | npm, Inc. y colaboradores de npm / GitHub | [npm/cli](https://github.com/npm/cli) | [Artistic-2.0](https://opensource.org/licenses/Artistic-2.0) |
| **Nuxt** | Nuxt Team (Alexandre Chopin, Sébastien Chopin y colaboradores) | [nuxt/nuxt](https://github.com/nuxt/nuxt) | [MIT](https://opensource.org/licenses/MIT) |
| **PHP** | 1997-2026 The PHP Documentation Group | [php.net/manual](https://www.php.net/manual/es/) / [php/doc-es](https://github.com/php/doc-es) | [CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/) |
| **pnpm** | Zoltan Kochan y colaboradores de pnpm | [pnpm/pnpm.io](https://github.com/pnpm/pnpm.io) | [MIT](https://opensource.org/licenses/MIT) |
| **Python** | Python Software Foundation | [docs.python.org](https://docs.python.org/3/) | [PSF License v2](https://docs.python.org/3/license.html) (ejemplos bajo [0BSD](https://opensource.org/licenses/0BSD)) |
| **Vue 3** | Evan You y colaboradores de Vue | [vuejs/docs](https://github.com/vuejs/docs) | [MIT](https://opensource.org/licenses/MIT) |

---

## Términos de las Licencias Principales

### Licencia MIT
Aplica a: Laravel, Filament, Composer, Node.js, Nuxt, pnpm y Vue 3.

```text
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Creative Commons (CC-BY-SA 2.5 y CC-BY 3.0)
- **JavaScript (MDN Content):** El contenido de MDN Web Docs se distribuye bajo [Creative Commons Attribution-ShareAlike 2.5 Generic (CC-BY-SA-2.5)](https://creativecommons.org/licenses/by-sa/2.5/). Cualquier redistribución de esta sección preserva la atribución a los colaboradores de Mozilla y la obligación de compartir bajo los mismos términos.
- **Manual de PHP:** El manual de PHP es propiedad de *The PHP Documentation Group* y está bajo [Creative Commons Attribution 3.0 Unported (CC-BY-3.0)](https://creativecommons.org/licenses/by/3.0/) o superior.

### Python Software Foundation License (PSF v2)
La documentación oficial de Python es copyright © 2001-2026 de la *Python Software Foundation*, distribuida bajo los términos de la PSF License Agreement. Ejemplos de código incorporados se encuentran adicionalmente bajo licencia [Zero Clause BSD (0BSD)](https://opensource.org/licenses/0BSD).

### GNU Free Documentation License v1.3 (GFDL)
El manual de referencia de GNU Bash es copyright © Free Software Foundation, Inc. y se distribuye bajo los términos de la [GNU Free Documentation License Version 1.3](https://www.gnu.org/licenses/fdl-1.3.html). El texto íntegro de la licencia se encuentra incluido y accesible en este visor.

### The Artistic License 2.0
La documentación de la herramienta CLI de npm es copyright © npm, Inc. y colaboradores, distribuida bajo los términos de [The Artistic License 2.0](https://opensource.org/licenses/Artistic-2.0).

---

## Código y Herramientas del Proyecto

Todo el software propio desarrollado para este repositorio (el pipeline en `scripts/`, las plantillas HTML, los estilos CSS, el código JavaScript del visor y el archivo `Makefile`) es obra de **[@raupulus](https://github.com/raupulus)** (`public@raupulus.dev`) y se distribuye bajo licencia **MIT**.
