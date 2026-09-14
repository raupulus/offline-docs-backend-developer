---
title: '"builtins" --- Built-in objects'
source_url: https://docs.python.org/es/3
source_path: library/builtins.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1870
---

# "builtins" --- Built-in objects

======================================================================

This module provides direct access to all 'built-in' identifiers of
Python; for example, "builtins.open" is the full name for the built-in
function "open()".

Este módulo normalmente no es accedido explícitamente por la mayoría
de las aplicaciones, pero puede ser útil en módulos que provean
objetos con el mismo nombre que un valor incorporado, pero que sea
necesario también el incorporado con ese nombre. Por ejemplo, en un
módulo que quiera implementar una función "open()" que envuelva la
integrada "open()", este módulo puede se usado directamente:

   import builtins

   def open(path):
       f = builtins.open(path, 'r')
       return UpperCaser(f)

   class UpperCaser:
       '''Wrapper around a file that converts output to uppercase.'''

       def __init__(self, f):
           self._f = f

       def read(self, count=-1):
           return self._f.read(count).upper()

       # ...

Como un detalle de implementación, la mayoría de los módulos tienen el
nombre "__builtins__" disponible como parte de sus globales. El valor
de "__builtins__" es normalmente o este módulo o el valor del atributo
"__dict__" de este módulo. Como este es un detalle de implementación,
puede que no sea usado por implementaciones alternativas de Python.

Ver también:

  * Constantes incorporadas

  * Excepciones incorporadas

  * Funciones incorporadas

  * Tipos integrados
