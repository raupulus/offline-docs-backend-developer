---
title: El objeto "None"
source_url: https://docs.python.org/es/3
source_path: c-api/none.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 520
---

# El objeto "None"

Ten en cuenta que el "PyTypeObject" para "None" no está expuesto
directamente en la API de Python/C.  Dado que "None" es un singleton,
basta con comprobar la identidad del objeto (usando "==" en C). No
existe una función "PyNone_Check()" por la misma razón.

PyObject *Py_None

   El objeto Python "None", que denota falta de valor.  Este objeto no
   tiene métodos y es *immortal*.

   Distinto en la versión 3.12: "Py_None" es *immortal*.

Py_RETURN_NONE

   Retorna "Py_None" desde una función.
