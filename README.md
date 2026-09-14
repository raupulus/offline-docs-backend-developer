# Documentación técnica offline

Espejo de documentación oficial en markdown, con un visor web estático que funciona sin conexión.

Existe para poder seguir trabajando cuando no hay internet: viajes, averías de red, caídas de servidor, o bloqueos DNS de operadoras que tumban dominios legítimos (en España ha pasado con rangos de Cloudflare por motivos de retransmisiones deportivas).

No pretende ser una solución alarmista, pero me ha sacado de más de un apuro y la comparto por si a alguien le sirve.

---

## Uso rápido

```bash
make            # ayuda
make update     # reconstruye todo (lo que ejecuto cada pocos meses)
make status     # qué hay descargado y de qué versión
```

Después, abre `public/index.html` en el navegador. Sin servidor, sin Node, sin internet.

---

## Cómo está organizado

Tres capas y una única dirección de flujo:

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

| Directorio | Qué es | ¿Versionado? |
|---|---|---|
| `work/` | Clones y tarballs recién descargados | No, se borra tras cada build |
| **`src/`** | **Markdown canónico: la única fuente de verdad** | **Sí** |
| `public/` | Sitio HTML navegable | No, se regenera |
| `scripts/` | El pipeline y las plantillas | Sí |
| `sources.yaml` | Catálogo de fuentes | Sí |

Tener el markdown separado del HTML permite además consultarlo con `grep`, `rg` o modelos de IA locales sin pelearse con etiquetas.

---

## Documentación incluida

| Tecnología | Origen | Formato de origen |
|---|---|---|
| Laravel | `laravel/docs` | Markdown nativo |
| Filament | `filamentphp/filament` | Markdown nativo |
| Composer | `composer/composer` | Markdown nativo |
| Node.js | `nodejs/node` | Markdown nativo |
| npm | `npm/cli` | Markdown nativo |
| pnpm | `pnpm/pnpm.io` | Markdown nativo |
| PHP | `php/doc-es` (+ `php/doc-base`) | DocBook XML, convertido con pandoc |
| Python | docs.python.org | Texto plano, sin conversión |
| Bash | ftp.gnu.org (tarball) | Texinfo → DocBook con texi2any |

PHP se toma del **fuente en DocBook**, no del tarball de HTML de php.net. Sale más limpio, viene de git como el resto, y cada fichero trae el estado de su traducción al español (`translation_status`, `translation_reviewed`), que el pipeline vuelca al front-matter. Para la versión inglesa basta cambiar el `repo` a `php/doc-en` en `sources.yaml`.

---

## Añadir una tecnología

No hace falta escribir un script. Se añade una entrada en `sources.yaml`:

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

Y se ejecuta:

```bash
make fetch-one S=livewire
make normalize
make build
```

Antes de añadir nada, comprueba en qué formato publica su documentación el proyecto. Si usa Sphinx (`.rst`), **no** conviertas el `.rst` directamente: descarga su bundle HTML compilado. Los detalles están en `AGENTS.md`.

---

## Requisitos

```bash
# Debian / Ubuntu
sudo apt install git python3 pandoc

# macOS
brew install git python3 pandoc

# Dependencias de Python
pip3 install pyyaml markdown jinja2 pygments --break-system-packages
```

`make deps` comprueba que está todo.

---

## Estado del proyecto

En reorganización. La arquitectura descrita arriba es la de destino; el plan completo y el análisis de lo que había antes están en [`ANALISIS-Y-PLAN.md`](ANALISIS-Y-PLAN.md).

- [x] **Fase 1** — Base: `AGENTS.md`, `.gitignore`, `sources.yaml`, `Makefile`, estructura
- [x] **Fase 2** — Pipeline para las fuentes con markdown nativo (`fetch`, `normalize`, `check`)
- [x] **Fase 3** — Generador de sitio y buscador offline (`build`, `search`)
- [x] **Fase 4a** — PHP desde el fuente DocBook (`docbook`, `normalize_docbook`)
- [ ] **Fase 4b** — Python (texto plano) y Bash (Texinfo): escrito, sin probar con descarga real
- [ ] **Fase 5** — Acabado: licencias, bundles para IA, validaciones

PHP se probó sobre 1.008 documentos reales de `doc-es` (lenguaje, 8 extensiones, apéndices, seguridad): 0 errores, 0 entidades sin resolver, y 1.023.121 enlaces internos comprobados en el sitio generado sin ninguno roto. La conversión completa de los 11.339 ficheros tarda unos 6 minutos en un proceso y menos de 1 en ocho.

### Estado real del pipeline

Probado el 01/08/2026 contra los repositorios reales: **503 documentos** normalizados, validados y publicados. 53.147 enlaces internos comprobados, ninguno roto.

| Tecnología | Documentos | Secciones |
|---|---:|---:|
| Laravel | 99 | 1 |
| Filament | 82 | 7 |
| Composer | 33 | 5 |
| Node.js | 70 | 1 |
| npm | 87 | 3 |
| pnpm | 132 | 3 |

El sitio generado ocupa unos 25 MB. Se abre con doble clic en `public/index.html`: sin servidor, sin conexión y sin cargar ni un solo recurso externo.

### El visor

- Portada con una tarjeta por tecnología, indicando versión y fecha de descarga.
- Menú lateral por secciones, plegable, con la página actual resaltada.
- Buscador con atajo `/`, navegable con flechas. Índice por tecnología cargado bajo demanda, más un índice global en la portada.
- Modo claro y oscuro, siguiendo el sistema o forzado con el conmutador.
- Código resaltado en tiempo de compilación con Pygments: cero JavaScript para colorear.
- Índice de contenidos por página y navegación anterior/siguiente.

Detalle técnico que conviene no tocar: sobre `file://` el navegador bloquea `fetch()`, así que **el índice de búsqueda es un `.js` que declara una variable global, no un `.json`**. Convertirlo a JSON rompería el buscador al abrir el sitio sin servidor.

### Limitación conocida

Las ilustraciones de pnpm (`/img/*.svg`) no se descargan, porque están fuera de su carpeta de documentación. Son 15 imágenes que se verán rotas; el texto está completo. Se resuelve en una iteración posterior ampliando su `sparse` en `sources.yaml`.

### Aviso sobre carpetas sincronizadas

Git necesita cambiar permisos, y sobre sistemas de ficheros sincronizados (Google Drive, Dropbox) esas operaciones pueden fallar. Si `make fetch` da errores de permisos, saca `work/` a un disco normal:

```bash
make update WORK_DIR=/tmp/docs-work
```

`src/` y `public/` no tienen ese problema: son ficheros normales.

### Migración desde la estructura antigua

La carpeta `repos/` de la versión anterior contenía clones completos (más de 60.000 ficheros de `vendor/` y `node_modules`). Ya no se usa: la sustituye `work/` con clones sparse. Para eliminarla:

```bash
make clean-all
```

---

## Licencias

Cada documentación mantiene la licencia de su proyecto original, y casi todas exigen conservar la atribución. Ver [`LICENSES.md`](LICENSES.md).

Este repositorio es un **espejo no oficial**. La documentación de referencia siempre es la del sitio oficial de cada proyecto; aquí solo se cambia el formato, nunca el contenido.

El código del proyecto (scripts, plantillas y estilos) es de @raupulus.

---

## Contribuir

Las documentaciones incluidas son las que uso a diario. Si echas en falta alguna, adelante: una entrada en `sources.yaml` y listo.

Requisito estricto: **todo lo que se guarde aquí tiene que ser público**. Nada de credenciales, tokens, rutas de máquinas privadas ni datos personales, porque la carpeta se comparte.

---

*Mantenido por [@raupulus](https://github.com/raupulus) · public@raupulus.dev*
