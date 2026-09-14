---
title: '"html" --- HyperText Markup Language support'
source_url: https://docs.python.org/es/3
source_path: library/html.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2840
---

# "html" --- HyperText Markup Language support

**Código fuente:** Lib/html/__init__.py

======================================================================

Este módulo define utilidades para manipular HTML.

html.escape(s, quote=True)

   Convert the characters "&", "<" and ">" in string *s* to HTML-safe
   sequences.  Use this if you need to display text that might contain
   such characters in HTML.  If the optional flag *quote* is true (the
   default), the characters (""") and ("'") are also translated; this
   helps for inclusion in an HTML attribute value delimited by quotes,
   as in "<a href="...">". If *quote* is set to false, the characters
   (""") and ("'") are not translated.

   Added in version 3.2.

html.unescape(s)

   Convierte todas las referencias de caracteres numéricos y con
   nombre (por ejemplo "&gt;", "&#62;", "&#x3e;") de la cadena de
   caracteres *s* a los caracteres Unicode correspondientes.  Esta
   función utiliza las reglas definidas por el estándar HTML 5 para
   las referencias de caracteres válidas e inválidas, y la "lista de
   referencia de caracteres con nombre de HTML 5".

   Added in version 3.4.

======================================================================

Los submódulos del paquete "html" son:

* "html.parser" -- Analizador sintáctico simple de HTML y XHTML

* "html.entities" -- Definición general de entidades HTML
