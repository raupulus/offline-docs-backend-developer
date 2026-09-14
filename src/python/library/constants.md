---
title: Constantes incorporadas
source_url: https://docs.python.org/es/3
source_path: library/constants.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2110
---

# Constantes incorporadas

Un pequeño número de constantes viven en el espacio de nombres
incorporado. Ellas son:

False

   El valor falso del tipo "bool". Las asignaciones a "False" son
   ilegales y generan un "SyntaxError".

True

   El valor verdadero del tipo "bool". Las asignaciones a "True" son
   ilegales y generan un "SyntaxError".

None

   An object frequently used to represent the absence of a value, as
   when default arguments are not passed to a function. Assignments to
   "None" are illegal and raise a "SyntaxError". "None" is the sole
   instance of the "NoneType" type.

NotImplemented

   A special value which should be returned by the binary special
   methods (e.g. "__eq__()", "__lt__()", "__add__()", "__rsub__()",
   etc.) to indicate that the operation is not implemented with
   respect to the other type; may be returned by the in-place binary
   special methods (e.g. "__imul__()", "__iand__()", etc.) for the
   same purpose. It should not be evaluated in a boolean context.
   "NotImplemented" is the sole instance of the
   "types.NotImplementedType" type.

   Nota:

     When a binary (or in-place) method returns "NotImplemented" the
     interpreter will try the reflected operation on the other type
     (or some other fallback, depending on the operator).  If all
     attempts return "NotImplemented", the interpreter will raise an
     appropriate exception. Incorrectly returning "NotImplemented"
     will result in a misleading error message or the "NotImplemented"
     value being returned to Python code.Consulte Implementar
     operaciones aritméticas para ver ejemplos.

   Prudencia:

     "NotImplemented" and "NotImplementedError" are not
     interchangeable. This constant should only be used as described
     above; see "NotImplementedError" for details on correct usage of
     the exception.

   Distinto en la versión 3.9: Evaluating "NotImplemented" in a
   boolean context was deprecated.

   Distinto en la versión 3.14: Evaluating "NotImplemented" in a
   boolean context now raises a "TypeError". It previously evaluated
   to "True" and emitted a "DeprecationWarning" since Python 3.9.

Ellipsis

   The same as the ellipsis literal ""..."", an object frequently used
   to indicate that something is omitted. Assignment to "Ellipsis" is
   possible, but assignment to  "..." raises a "SyntaxError".
   "Ellipsis" is the sole instance of the "types.EllipsisType" type.

__debug__

   Esta constante es verdadera si Python no se inició con una opción
   "-O". Vea también la instrucción "assert".

Nota:

  Los nombres: "None", "False", "True" y "__debug__" no se pueden
  reasignar (asignaciones a ellos, incluso como un nombre de atributo,
  lanza "SyntaxError" ), por lo que pueden considerarse constantes
  "verdaderas".

## Constantes agregadas por el módulo "site"

El módulo "site" (que se importa automáticamente durante el inicio,
excepto si se proporciona la opción "-S" en la línea de comandos)
agrega varias constantes al espacio de nombres integrado. Son útiles
para el intérprete interactivo y no deben usarse en programas.

quit(code=None)
exit(code=None)

   Objects that when printed, print a message like "Use quit() or
   Ctrl-D (i.e. EOF) to exit", and when accessed directly in the
   interactive interpreter or called as functions, raise "SystemExit"
   with the specified exit code.

help

   Object that when printed, prints the message "Type help() for
   interactive help, or help(object) for help about object.", and when
   accessed directly in the interactive interpreter, invokes the
   built-in help system (see "help()").

copyright
credits

   Objetos que al ser impresos o llamados imprimen el texto de
   derechos de autor o créditos, respectivamente.

license

   Objeto que cuando se imprime, muestra el mensaje "Escriba licencia
   () para ver el texto completo de la licencia", y cuando se le
   llama, muestra el texto completo de la licencia en forma de
   buscapersonas (una pantalla a la vez).
