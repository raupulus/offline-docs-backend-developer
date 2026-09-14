---
title: '"reprlib" --- Alternate "repr()" implementation'
source_url: https://docs.python.org/es/3
source_path: library/reprlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3670
---

# "reprlib" --- Alternate "repr()" implementation

**Código fuente:** Lib/reprlib.py

======================================================================

The "reprlib" module provides a means for producing object
representations with limits on the size of the resulting strings. This
is used in the Python debugger and may be useful in other contexts as
well.

Este módulo provee una clase, una instancia y una función:

class reprlib.Repr(*, maxlevel=6, maxtuple=6, maxlist=6, maxarray=5, maxdict=4, maxset=6, maxfrozenset=6, maxdeque=6, maxstring=30, maxlong=40, maxother=30, fillvalue='...', indent=None)

   Clase que provee de servicios de formateo útiles en la
   implementación de funciones similar a la integrada "repr()"; los
   límites de tamaño para diferentes tipos de objetos son añadidos
   para evitar la generación de representaciones que son excesivamente
   largas.

   The keyword arguments of the constructor can be used as a shortcut
   to set the attributes of the "Repr" instance. Which means that the
   following initialization:

      aRepr = reprlib.Repr(maxlevel=3)

   Is equivalent to:

      aRepr = reprlib.Repr()
      aRepr.maxlevel = 3

   See section Repr Objects for more information about "Repr"
   attributes.

   Distinto en la versión 3.12: Allow attributes to be set via keyword
   arguments.

reprlib.aRepr

   Esta es una instancia de "Repr" que es usada para proveer la
   función "repr()" descrita debajo. Cambiar los atributos de este
   objeto afectará los límites de tamaño usados por "repr()" y el
   depurador de Python.

reprlib.repr(obj)

   Este es el método "repr()" de "aRepr". Retorna una cadena similar a
   la retornada por la función integrada del mismo nombre, pero con
   límites en la mayoría de tamaños.

In addition to size-limiting tools, the module also provides a
decorator for detecting recursive calls to "__repr__()" and
substituting a placeholder string instead.

@reprlib.recursive_repr(fillvalue='...')

   Decorator for "__repr__()" methods to detect recursive calls within
   the same thread.  If a recursive call is made, the *fillvalue* is
   returned, otherwise, the usual "__repr__()" call is made.  For
   example:

      >>> from reprlib import recursive_repr
      >>> class MyList(list):
      ...     @recursive_repr()
      ...     def __repr__(self):
      ...         return '<' + '|'.join(map(repr, self)) + '>'
      ...
      >>> m = MyList('abc')
      >>> m.append(m)
      >>> m.append('x')
      >>> print(m)
      <'a'|'b'|'c'|...|'x'>

   Added in version 3.2.

## Objetos Repr

Las instancias "Repr" proveen varios atributos que pueden ser usados
para proporcionar límites de tamaño para las representaciones de
diferentes tipos de objetos, y métodos que formatean tipos de objetos
específicos.

Repr.fillvalue

   Esta cadena se muestra para referencias recursivas. El valor
   predeterminado es "...".

   Added in version 3.11.

Repr.maxlevel

   Límite de profundidad en la creación de representaciones
   recursivas. El valor por defecto es "6".

Repr.maxdict
Repr.maxlist
Repr.maxtuple
Repr.maxset
Repr.maxfrozenset
Repr.maxdeque
Repr.maxarray

   Límites en el número de entradas representadas por el tipo de
   objeto nombrado. El valor por defecto es "4" para "maxdict", "5"
   para  "maxarray", y "6" para los otros.

Repr.maxlong

   Máximo número de caracteres en la representación para un entero.
   Los dígitos son eliminados desde el medio. El valor por defecto es
   "40".

Repr.maxstring

   Límite en el número de caracteres en la representación de la
   cadena. Fíjese que la representación "normal" de la cadena  es la
   usada como la fuente de caracteres: si se necesitan secuencias de
   escape en la representación, estas pueden ser desordenadas cuando
   la representación se ha acortado. El valor por defecto es "30".

Repr.maxother

   Este límite es usado para controlar el tamaño de los tipos de
   objetos para los cuales no hay ningún método de formateo específico
   en el objeto "Repr". Se aplica de una manera similar a "maxstring".
   El valor por defecto es "20".

Repr.indent

   If this attribute is set to "None" (the default), the output is
   formatted with no line breaks or indentation, like the standard
   "repr()". For example:

      >>> example = [
      ...     1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']
      >>> import reprlib
      >>> aRepr = reprlib.Repr()
      >>> print(aRepr.repr(example))
      [1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']

   If "indent" is set to a string, each recursion level is placed on
   its own line, indented by that string:

      >>> aRepr.indent = '-->'
      >>> print(aRepr.repr(example))
      [
      -->1,
      -->'spam',
      -->{
      -->-->'a': 2,
      -->-->'b': 'spam eggs',
      -->-->'c': {
      -->-->-->3: 4.5,
      -->-->-->6: [],
      -->-->},
      -->},
      -->'ham',
      ]

   Setting "indent" to a positive integer value behaves as if it was
   set to a string with that number of spaces:

      >>> aRepr.indent = 4
      >>> print(aRepr.repr(example))
      [
          1,
          'spam',
          {
              'a': 2,
              'b': 'spam eggs',
              'c': {
                  3: 4.5,
                  6: [],
              },
          },
          'ham',
      ]

   Added in version 3.12.

Repr.repr(obj)

   El equivalente a la función integrada "repr()" que usa el formateo
   impuesto por la instancia.

Repr.repr1(obj, level)

   Implementación recursiva usada por "repr()". Este usa el tipo de
   *obj* para determinar qué método invocar, pasándole *obj* y
   *level*. Los métodos de tipo específico deben invocar "repr1()"
   para realizar formateo recursivo, con "level - 1" para el valor de
   *level* en la invocación recursiva.

Repr.repr_TYPE(obj, level)

   Métodos de formateo para tipos específicos son implementados como
   métodos con un nombre basado en el nombre del tipo. En el nombre
   del método, **TYPE** es reemplazado por
   "'_'.join(type(obj).__name__.split())". El envío a estos métodos es
   gestionado por "repr1()". Los métodos de tipo específico que
   necesitan formatear recursivamente un valor deben invocar
   "self.repr1(subobj, level - 1)".

## Subclasificando Objetos Repr

The use of dynamic dispatching by "Repr.repr1()" allows subclasses of
"Repr" to add support for additional built-in object types or to
modify the handling of types already supported. This example shows how
special support for file objects could be added:

   import reprlib
   import sys

   class MyRepr(reprlib.Repr):

       def repr_TextIOWrapper(self, obj, level):
           if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
               return obj.name
           return repr(obj)

   aRepr = MyRepr()
   print(aRepr.repr(sys.stdin))         # prints '<stdin>'

   <stdin>
