"""
docsync — pipeline de documentación offline.

Tres fases, en este orden y solo en esta dirección:

    fetch      red        -> work/    descarga clones sparse y tarballs
    normalize  work/      -> src/     convierte todo a markdown canónico
    build      src/       -> public/  genera el sitio HTML estático

`src/` es la única fuente de verdad. `work/` y `public/` son desechables.

Cada fuente se declara en sources.yaml y la maneja un adaptador de
docsync.adapters. Añadir una tecnología nueva es añadir una entrada al
YAML, no escribir código. Ver AGENTS.md.
"""

__version__ = "0.1.0"
__author__ = "@raupulus"
