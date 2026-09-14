---
title: '"keyword" --- Testing for Python keywords'
source_url: https://docs.python.org/es/3
source_path: library/keyword.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3080
---

# "keyword" --- Testing for Python keywords

**Código fuente:** Lib/keyword.py

======================================================================

Este módulo permite a un programa Python determinar si una cadena de
caracteres es una palabra clave o palabra clave suave.

keyword.iskeyword(s)

   Retorna "True" si *s* es una palabra clave Python.

keyword.kwlist

   Secuencia que contiene todos las palabras clave definidos para el
   intérprete. Si cualquier palabra clave es definida para estar
   activa sólo cuando las declaraciones particulares "__future__"
   están vigentes, estas se incluirán también.

keyword.issoftkeyword(s)

   Retorna "True" si *s* es una palabra clave suave de Python.

   Added in version 3.9.

keyword.softkwlist

   Secuencia que contiene todos las palabras clave suaves definidas
   para el intérprete. Si cualquier palabra clave suave es definida
   para estar activa sólo cuando las declaraciones particulares
   "__future__" están vigentes, estas se incluirán también.

   Added in version 3.9.
