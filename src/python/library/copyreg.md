---
title: '"copyreg" --- Register "pickle" support functions'
source_url: https://docs.python.org/es/3
source_path: library/copyreg.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2150
---

# "copyreg" --- Register "pickle" support functions

**Código fuente:** Lib/copyreg.py

======================================================================

The "copyreg" module offers a way to define functions used while
pickling specific objects.  The "pickle" and "copy" modules use those
functions when pickling/copying those objects.  The module provides
configuration information about object constructors which are not
classes. Such constructors may be factory functions or class
instances.

copyreg.constructor(object)

   Declara que el *object* es un constructor válido. Si el *object* no
   es invocable (y por lo tanto, no es válido como constructor), lanza
   una excepción "TypeError".

copyreg.pickle(type, function, constructor_ob=None)

   Declares that *function* should be used as a "reduction" function
   for objects of type *type*.  *function* must return either a string
   or a tuple containing between two and six elements. See the
   "dispatch_table" for more details on the interface of *function*.

   El parámetro *constructor_ob* es una característica heredada y
   ahora se ignora, pero si se pasa debe ser invocable.

   Note que el atributo "dispatch_table" de un objeto pickler o
   subclase de "pickle.Pickler" también puede ser utilizado para
   declarar funciones de reducción.

## Ejemplo

El siguiente ejemplo pretende mostrar cómo registrar una función
pickle y cómo se utilizará:

>>> import copyreg, copy, pickle
>>> class C:
...     def __init__(self, a):
...         self.a = a
...
>>> def pickle_c(c):
...     print("pickling a C instance...")
...     return C, (c.a,)
...
>>> copyreg.pickle(C, pickle_c)
>>> c = C(1)
>>> d = copy.copy(c)
pickling a C instance...
>>> p = pickle.dumps(c)
pickling a C instance...
