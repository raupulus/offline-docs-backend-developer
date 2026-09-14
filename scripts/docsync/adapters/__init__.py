"""
Adaptadores de fuentes.

Un adaptador recibe la entrada correspondiente de sources.yaml y deja
markdown en src/<id>/. Esa es toda su responsabilidad.

Adaptadores previstos:

    git_markdown   repos que ya publican markdown
                   -> laravel, filament, composer, nodejs, npm, pnpm

    html_tarball   HTML compilado descargable, convertido con pandoc
                   -> php, python, bash

    manpage        páginas man convertidas con `pandoc -f man -t gfm`

Reglas para cualquier adaptador nuevo:

  * Clones siempre con --depth 1 y sparse checkout limitado a la carpeta
    de documentación. Nunca un clon completo.
  * Nunca convertir .rst de Sphinx directamente con pandoc: las
    directivas se cuelan como HTML crudo. Usar el bundle HTML compilado
    que publique el proyecto.
  * No inventar valores de front-matter. Si un dato no se puede obtener
    de la fuente, omitir la clave.
"""
