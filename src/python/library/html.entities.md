---
title: '"html.entities" --- Definitions of HTML general entities'
source_url: https://docs.python.org/es/3
source_path: library/html.entities.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2820
---

# "html.entities" --- Definitions of HTML general entities

**Código fuente:** Lib/html/entities.py

======================================================================

Este módulo define cuatro diccionarios "html5", "name2codepoint",
"codepoint2name", y "entitydefs".

html.entities.html5

   Un diccionario que asigna referencias de caracteres con nombre
   HTML5 [1] a los caracteres Unicode equivalentes, p. Ej.
   "html5['gt;'] == '>'". Tenga en cuenta que el punto y coma al final
   está incluido en el nombre (por ejemplo, "'gt;'"), sin embargo,
   algunos de los nombres son aceptados por el estándar incluso sin el
   punto y coma: en este caso, el nombre está presente con y sin el
   "';'". Consulte también "html.unescape()".

   Added in version 3.3.

html.entities.entitydefs

   Un diccionario que asigna definiciones de entidad XHTML 1.0 a su
   texto de reemplazo en ISO Latin-1.

html.entities.name2codepoint

   Un diccionario que asigna nombres de entidades HTML4 a los puntos
   de código Unicode.

html.entities.codepoint2name

   Un diccionario que asigna puntos de código Unicode a nombres de
   entidades HTML4.

-[ Notas al pie ]-

[1] Vea https://html.spec.whatwg.org/multipage/named-characters.html
    #named-character-references
