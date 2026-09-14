---
title: '"copy" --- Shallow and deep copy operations'
source_url: https://docs.python.org/es/3
source_path: library/copy.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2140
---

# "copy" --- Shallow and deep copy operations

**Código fuente:** Lib/copy.py

======================================================================

Las declaraciones de asignación en Python no copian objetos, crean
enlaces entre un objetivo y un objeto. Para colecciones que son
mutables o que contienen elementos mutables, a veces se necesita una
copia para que uno pueda cambiar una copia sin cambiar la otra. Este
módulo proporciona operaciones genéricas de copia superficial y
profunda (explicadas a continuación).

Resumen de la interfaz:

copy.copy(obj)

   Return a shallow copy of *obj*.

copy.deepcopy(obj[, memo])

   Return a deep copy of *obj*.

copy.replace(obj, /, **changes)

   Creates a new object of the same type as *obj*, replacing fields
   with values from *changes*.

   Added in version 3.13.

exception copy.Error

   Levantado para errores específicos del módulo.

La diferencia entre copia superficial y profunda solo es relevante
para objetos compuestos (objetos que contienen otros objetos, como
listas o instancias de clase):

* Una copia superficial (*shallow copy*) construye un nuevo objeto
  compuesto y luego (en la medida de lo posible) inserta *references*
  en él a los objetos encontrados en el original.

* Una copia profunda (*deep copy*) construye un nuevo objeto compuesto
  y luego, recursivamente, inserta *copias* en él de los objetos
  encontrados en el original.

A menudo existen dos problemas con las operaciones de copia profunda
que no existen con las operaciones de copia superficial:

* Los objetos recursivos (objetos compuestos que, directa o
  indirectamente, contienen una referencia a sí mismos) pueden causar
  un bucle recursivo.

* Debido a que la copia profunda copia todo, puede copiar demasiado,
  como los datos que deben compartirse entre copias.

La función "deepcopy()" evita estos problemas al:

* mantener un diccionario "memo" de objetos ya copiados durante la
  aprobación de copia actual; y

* permitiendo que las clases definidas por el usuario anulen la
  operación de copia o el conjunto de componentes copiados.

Este módulo no copia tipos como módulo, método, seguimiento de pila,
marco de pila, archivo, socket, ventana,  o cualquier tipo similar.
Sí "copia" funciones y clases (superficiales y profundas), retornando
el objeto original sin cambios; Esto es compatible con la forma en que
son tratados por el módulo "pickle".

Shallow copies of many collections can be made using the corresponding
"copy()" method (such as "list.copy()", "dict.copy()" or
"set.copy()"), and of sequences (such as lists or bytearrays) by
making a slice of the entire sequence ("sequence[:]"). However, these
methods and slicing can create an instance of the base type when
copying an instance of a subclass, whereas "copy.copy()" normally
returns an instance of the same type.

Classes can use the same interfaces to control copying that they use
to control pickling.  See the description of module "pickle" for
information on these methods.  In fact, the "copy" module uses the
registered pickle functions from the "copyreg" module.

In order for a class to define its own copy implementation, it can
define special methods "__copy__()" and "__deepcopy__()".

object.__copy__(self)

   Called to implement the shallow copy operation; no additional
   arguments are passed.

object.__deepcopy__(self, memo)

   Called to implement the deep copy operation; it is passed one
   argument, the *memo* dictionary.  If the "__deepcopy__"
   implementation needs to make a deep copy of a component, it should
   call the "deepcopy()" function with the component as first argument
   and the *memo* dictionary as second argument. The *memo* dictionary
   should be treated as an opaque object.

Function "copy.replace()" is more limited than "copy()" and
"deepcopy()", and only supports named tuples created by
"namedtuple()", "dataclasses", and other classes which define method
"__replace__()".

object.__replace__(self, /, **changes)

   This method should create a new object of the same type, replacing
   fields with values from *changes*.

   Added in version 3.13.

Ver también:

  Módulo "pickle"
     Discusión de los métodos especiales utilizados para apoyar la
     recuperación y restauración del estado del objeto.
