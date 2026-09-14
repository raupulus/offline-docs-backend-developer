---
title: '"traceback" --- Print or retrieve a stack traceback'
source_url: https://docs.python.org/es/3
source_path: library/traceback.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4290
---

# "traceback" --- Print or retrieve a stack traceback

**Código fuente:** Lib/traceback.py

======================================================================

This module provides a standard interface to extract, format and print
stack traces of Python programs. It is more flexible than the
interpreter's default traceback display, and therefore makes it
possible to configure certain aspects of the output. Finally, it
contains a utility for capturing enough information about an exception
to print it later, without the need to save a reference to the actual
exception. Since exceptions can be the roots of large objects graph,
this utility can significantly improve memory management.

The module uses traceback objects --- these are objects of type
"types.TracebackType", which are assigned to the "__traceback__" field
of "BaseException" instances.

Ver también:

  Módulo "faulthandler"
     Usado para volcar explícitamente los rastreos Python, en un
     error, después de un tiempo de espera (*timeout*), o en una señal
     de usuario.

  Módulo "pdb"
     Depurador interactivo de código fuente para programas Python.

The module's API can be divided into two parts:

* Module-level functions offering basic functionality, which are
  useful for interactive inspection of exceptions and tracebacks.

* "TracebackException" class and its helper classes "StackSummary" and
  "FrameSummary". These offer both more flexibility in the output
  generated and the ability to store the information necessary for
  later formatting without holding references to actual exception and
  traceback objects.

Added in version 3.13: Output is colorized by default and can be
controlled using environment variables.

## Module-Level Functions

traceback.print_tb(tb, limit=None, file=None)

   Print up to *limit* stack trace entries from traceback object *tb*
   (starting from the caller's frame) if *limit* is positive.
   Otherwise, print the last "abs(limit)" entries.  If *limit* is
   omitted or "None", all entries are printed.  If *file* is omitted
   or "None", the output goes to "sys.stderr"; otherwise it should be
   an open *file* or *file-like object* to receive the output.

   Nota:

     The meaning of the *limit* parameter is different than the
     meaning of "sys.tracebacklimit". A negative *limit* value
     corresponds to a positive value of "sys.tracebacklimit", whereas
     the behaviour of a positive *limit* value cannot be achieved with
     "sys.tracebacklimit".

   Distinto en la versión 3.5: Soporte para *limit* negativo añadido.

traceback.print_exception(exc, /, [value, tb, ]limit=None, file=None, chain=True)

   Print exception information and stack trace entries from traceback
   object *tb* to *file*. This differs from "print_tb()" in the
   following ways:

   * si *tb* no es "None", muestra una cabecera "Traceback (most
     recent call last):"

   * imprime el tipo de excepción y *value* después del seguimiento de
     la pila

   * si *type(value)* es "SyntaxError" y *value* tiene el formato
     apropiado, muestra la línea donde el error sintáctico ha ocurrido
     con un cursor indicando la posición aproximada del error.

   Desde Python 3.10, en lugar de pasar *value* y *tb*, se puede pasar
   un objeto de excepción como primer argumento. Si se proporcionan
   *value* y *tb*, el primer argumento se ignora para proporcionar
   compatibilidad con versiones anteriores.

   The optional *limit* argument has the same meaning as for
   "print_tb()". If *chain* is true (the default), then chained
   exceptions (the "__cause__" or "__context__" attributes of the
   exception) will be printed as well, like the interpreter itself
   does when printing an unhandled exception.

   Distinto en la versión 3.5: El argumento *etype* es ignorado e
   infiere desde el tipo de *value*.

   Distinto en la versión 3.10: El parámetro *etype* ha cambiado de
   nombre a *exc* y ahora es solo posicional.

traceback.print_exc(limit=None, file=None, chain=True)

   This is a shorthand for "print_exception(sys.exception(),
   limit=limit, file=file, chain=chain)".

traceback.print_last(limit=None, file=None, chain=True)

   This is a shorthand for "print_exception(sys.last_exc, limit=limit,
   file=file, chain=chain)".  In general it will work only after an
   exception has reached an interactive prompt (see "sys.last_exc").

traceback.print_stack(f=None, limit=None, file=None)

   Print up to *limit* stack trace entries (starting from the
   invocation point) if *limit* is positive.  Otherwise, print the
   last "abs(limit)" entries.  If *limit* is omitted or "None", all
   entries are printed. The optional *f* argument can be used to
   specify an alternate stack frame to start.  The optional *file*
   argument has the same meaning as for "print_tb()".

   Distinto en la versión 3.5: Soporte para *limit* negativo añadido.

traceback.extract_tb(tb, limit=None)

   Return a "StackSummary" object representing a list of "pre-
   processed" stack trace entries extracted from the traceback object
   *tb*.  It is useful for alternate formatting of stack traces.  The
   optional *limit* argument has the same meaning as for "print_tb()".
   A "pre-processed" stack trace entry is a "FrameSummary" object with
   attributes representing the information that is usually printed for
   a stack trace.

traceback.extract_stack(f=None, limit=None)

   Extract the raw traceback from the current stack frame.  The return
   value has the same format as for "extract_tb()".  The optional *f*
   and *limit* arguments have the same meaning as for "print_stack()".

traceback.print_list(extracted_list, file=None)

   Print the list of tuples as returned by "extract_tb()" or
   "extract_stack()" as a formatted stack trace to the given file. If
   *file* is "None", the output is written to "sys.stderr".

traceback.format_list(extracted_list)

   Dada una lista de tuplas u objetos "FrameSummary" según lo
   retornado por "extract_tb()" o "extract_stack()", retorna una lista
   de cadenas preparadas para ser mostradas. Cada cadena en la lista
   resultante corresponde con el elemento con el mismo índice en la
   lista de argumentos. Cada cadena finaliza en una nueva línea; las
   cadenas pueden contener nuevas líneas internas también, para
   aquellos elementos cuya línea de texto de origen no es "None".

traceback.format_exception_only(exc, /, [value, ]*, show_group=False)

   Format the exception part of a traceback using an exception value
   such as given by "sys.last_exc".  The return value is a list of
   strings, each ending in a newline.  The list contains the
   exception's message, which is normally a single string; however,
   for "SyntaxError" exceptions, it contains several lines that (when
   printed) display detailed information about where the syntax error
   occurred. Following the message, the list contains the exception's
   "notes".

   Desde Python 3,10, en lugar de pasar *value*, un objeto de
   excepción se puede pasar como primer argumento. Si se proporciona
   *value*, el primer argumento se ignora el fin de proporcionar
   compatibilidad hacia atrás.

   When *show_group* is "True", and the exception is an instance of
   "BaseExceptionGroup", the nested exceptions are included as well,
   recursively, with indentation relative to their nesting depth.

   Distinto en la versión 3.10: El parámetro *etype* ha cambiado de
   nombre a *exc* y ahora es solo posicional.

   Distinto en la versión 3.11: The returned list now includes any
   "notes" attached to the exception.

   Distinto en la versión 3.13: *show_group* parameter was added.

traceback.format_exception(exc, /, [value, tb, ]limit=None, chain=True)

   Formatea una traza de pila y la información de la excepción. Los
   argumentos tienen el mismo significado que los argumentos
   correspondientes a "print_exception()". El valor retornado es una
   lista de cadenas, acabando cada una en una nueva línea y algunas
   contienen nuevas líneas internas. Cuando estas líneas son
   concatenadas y mostradas, exactamente el mismo texto es mostrado
   como hace "print_exception()".

   Distinto en la versión 3.5: El argumento *etype* es ignorado e
   infiere desde el tipo de *value*.

   Distinto en la versión 3.10: El comportamiento y la firma de esta
   función se modificaron para coincidir con "print_exception()".

traceback.format_exc(limit=None, chain=True)

   Esto es como "print_exc(limit)" pero retorna una cadena en lugar de
   imprimirlo en un archivo.

traceback.format_tb(tb, limit=None)

   Un atajo para "format_list(extract_tb(tb, limit))".

traceback.format_stack(f=None, limit=None)

   Un atajo para "format_list(extract_stack(f, limit))".

traceback.clear_frames(tb)

   Clears the local variables of all the stack frames in a traceback
   *tb* by calling the "clear()" method of each frame object.

   Added in version 3.4.

traceback.walk_stack(f)

   Walk a stack following "f.f_back" from the given frame, yielding
   the frame and line number for each frame. If *f* is "None", the
   current stack is used. This helper is used with
   "StackSummary.extract()".

   Added in version 3.5.

   Distinto en la versión 3.14: This function previously returned a
   generator that would walk the stack when first iterated over. The
   generator returned now is the state of the stack when "walk_stack"
   is called.

traceback.walk_tb(tb)

   Walk a traceback following "tb_next" yielding the frame and line
   number for each frame. This helper is used with
   "StackSummary.extract()".

   Added in version 3.5.

## "TracebackException" Objects

Added in version 3.5.

"TracebackException" objects are created from actual exceptions to
capture data for later printing.  They offer a more lightweight method
of storing this information by avoiding holding references to
traceback and frame objects. In addition, they expose more options to
configure the output compared to the module-level functions described
above.

class traceback.TracebackException(exc_type, exc_value, exc_traceback, *, limit=None, lookup_lines=True, capture_locals=False, compact=False, max_group_width=15, max_group_depth=10)

   Capture an exception for later rendering. The meaning of *limit*,
   *lookup_lines* and *capture_locals* are as for the "StackSummary"
   class.

   If *compact* is true, only data that is required by
   "TracebackException"'s "format()" method is saved in the class
   attributes. In particular, the "__context__" field is calculated
   only if "__cause__" is "None" and "__suppress_context__" is false.

   Tenga en cuenta que cuando se capturan locales, también se muestran
   en el rastreo.

   *max_group_width* (*anchura máxima del grupo*) y *max_group_depth*
   (*profundidad máxima del grupo*) controlan el formato del grupo de
   excepciones (ver "BaseExceptionGroup"). La profundidad (*depth*) se
   refiere al nivel de anidamiento del grupo, y la anchura (*width*)
   se refiere al tamaño de una excepción simple perteneciente al
   arreglo del grupo de excepciones. El formato de salida se trunca
   cuando se excede el límite.

   Distinto en la versión 3.10: Se agregó el parámetro *compact*.

   Distinto en la versión 3.11: Se agregaron los parámetros
   *max_group_width* y *max_group_depth*

   __cause__

      A "TracebackException" of the original "__cause__".

   __context__

      A "TracebackException" of the original "__context__".

   exceptions

      If "self" represents an "ExceptionGroup", this field holds a
      list of "TracebackException" instances representing the nested
      exceptions. Otherwise it is "None".

      Added in version 3.11.

   __suppress_context__

      The "__suppress_context__" value from the original exception.

   __notes__

      The "__notes__" value from the original exception, or "None" if
      the exception does not have any notes. If it is not "None" is it
      formatted in the traceback after the exception string.

      Added in version 3.11.

   stack

      Una clase "StackSummary" representando el seguimiento de pila.

   exc_type

      The class of the original exception.

      Obsoleto desde la versión 3.13.

   exc_type_str

      String display of the class of the original exception.

      Added in version 3.13.

   filename

      Para errores sintácticos - el nombre del archivo donde el error
      ha ocurrido.

   lineno

      Para errores sintácticos - el número de línea donde el error ha
      ocurrido.

   end_lineno

      Para errores sintácticos - el número de línea donde el error ha
      ocurrido. Puede ser "None" si no está presente.

      Added in version 3.10.

   text

      Para errores sintácticos - el texto donde el error ha ocurrido.

   offset

      Para errores sintácticos - el *offset* en el texto donde el
      error ha ocurrido.

   end_offset

      Para errores sintácticos - el *offset* en el texto donde el
      error ha ocurrido. Puede ser "None" si no está presente.

      Added in version 3.10.

   msg

      Para errores sintácticos - el mensaje de error del compilador.

   classmethod from_exception(exc, *, limit=None, lookup_lines=True, capture_locals=False, compact=False, max_group_width=15, max_group_depth=10)

      Captura una excepción para su posterior procesado. *limit*,
      *lookup_lines* y *capture_locals* son como para la clase
      "StackSummary".

      Tenga en cuenta que cuando se capturan locales, también se
      muestran en el rastreo.

   print(*, file=None, chain=True)

      Imprime en *file* ("sys.stderr" por defecto) la información de
      la excepción retornada por "format()".

      Added in version 3.11.

   format(*, chain=True)

      Formatea la excepción.

      If *chain* is not "True", "__cause__" and "__context__" will not
      be formatted.

      El valor retornado es un generador de cadenas, donde cada una
      acaba en una nueva línea y algunas contienen nuevas líneas
      internas. "print_exception()" es un contenedor alrededor de este
      método que simplemente muestra las líneas de un archivo.

   format_exception_only(*, show_group=False)

      Formatea la parte de la excepción de un seguimiento de pila.

      El valor retornado es un generador de cadenas, donde cada una
      acaba en una nueva línea.

      When *show_group* is "False", the generator emits the
      exception's message followed by its notes (if it has any). The
      exception message is normally a single string; however, for
      "SyntaxError" exceptions, it consists of several lines that
      (when printed) display detailed information about where the
      syntax error occurred.

      When *show_group* is "True", and the exception is an instance of
      "BaseExceptionGroup", the nested exceptions are included as
      well, recursively, with indentation relative to their nesting
      depth.

      Distinto en la versión 3.11: The exception's "notes" are now
      included in the output.

      Distinto en la versión 3.13: Added the *show_group* parameter.

## "StackSummary" Objects

Added in version 3.5.

"StackSummary" objects represent a call stack ready for formatting.

class traceback.StackSummary

   classmethod extract(frame_gen, *, limit=None, lookup_lines=True, capture_locals=False)

      Construct a "StackSummary" object from a frame generator (such
      as is returned by "walk_stack()" or "walk_tb()").

      If *limit* is supplied, only this many frames are taken from
      *frame_gen*. If *lookup_lines* is "False", the returned
      "FrameSummary" objects will not have read their lines in yet,
      making the cost of creating the "StackSummary" cheaper (which
      may be valuable if it may not actually get formatted). If
      *capture_locals* is "True" the local variables in each
      "FrameSummary" are captured as object representations.

      Distinto en la versión 3.12: Las excepciones lanzadas desde
      "repr()" en una variable local (cuando *capture_locals* es
      "True") no son propagadas al invocador.

   classmethod from_list(a_list)

      Construct a "StackSummary" object from a supplied list of
      "FrameSummary" objects or old-style list of tuples.  Each tuple
      should be a 4-tuple with *filename*, *lineno*, *name*, *line* as
      the elements.

   format()

      Returns a list of strings ready for printing.  Each string in
      the resulting list corresponds to a single frame from the stack.
      Each string ends in a newline; the strings may contain internal
      newlines as well, for those items with source text lines.

      Para secuencias largas del mismo marco y línea, se muestran las
      primeras repeticiones, seguidas de una línea de resumen que
      indica el número exacto de repeticiones adicionales.

      Distinto en la versión 3.6: Las secuencias largas de cuadros
      repetidos ahora se abrevian.

   format_frame_summary(frame_summary)

      Returns a string for printing one of the frames involved in the
      stack. This method is called for each "FrameSummary" object to
      be printed by "StackSummary.format()". If it returns "None", the
      frame is omitted from the output.

      Added in version 3.11.

## "FrameSummary" Objects

Added in version 3.5.

A "FrameSummary" object represents a single frame in a traceback.

class traceback.FrameSummary(filename, lineno, name, *, lookup_line=True, locals=None, line=None, end_lineno=None, colno=None, end_colno=None)

   Represents a single frame in the traceback or stack that is being
   formatted or printed. It may optionally have a stringified version
   of the frame's locals included in it. If *lookup_line* is "False",
   the source code is not looked up until the "FrameSummary" has the
   "line" attribute accessed (which also happens when casting it to a
   "tuple"). "line" may be directly provided, and will prevent line
   lookups happening at all. *locals* is an optional local variable
   mapping, and if supplied the variable representations are stored in
   the summary for later display.

   "FrameSummary" instances have the following attributes:

   filename

      The filename of the source code for this frame. Equivalent to
      accessing "f.f_code.co_filename" on a frame object *f*.

   lineno

      The line number of the source code for this frame.

   name

      Equivalent to accessing "f.f_code.co_name" on a frame object
      *f*.

   line

      A string representing the source code for this frame, with
      leading and trailing whitespace stripped. If the source is not
      available, it is "None".

   end_lineno

      The last line number of the source code for this frame. By
      default, it is set to "lineno" and indexation starts from 1.

      Distinto en la versión 3.13: The default value changed from
      "None" to "lineno".

   colno

      The column number of the source code for this frame. By default,
      it is "None" and indexation starts from 0.

   end_colno

      The last column number of the source code for this frame. By
      default, it is "None" and indexation starts from 0.

## Examples of Using the Module-Level Functions

Este ejemplo sencillo implementa un bucle de lectura, evaluación e
impresión básico, similar a (pero menos útil) el bucle del intérprete
interactivo estándar de Python. Para una implementación más completa
del bucle del intérprete, ir al módulo "code"

   import sys, traceback

   def run_user_code(envdir):
       source = input(">>> ")
       try:
           exec(source, envdir)
       except Exception:
           print("Exception in user code:")
           print("-"*60)
           traceback.print_exc(file=sys.stdout)
           print("-"*60)

   envdir = {}
   while True:
       run_user_code(envdir)

El siguiente ejemplo demuestra las diferentes manera para mostrar y
formatear la excepción y el seguimiento de pila:

   import sys, traceback

   def lumberjack():
       bright_side_of_life()

   def bright_side_of_life():
       return tuple()[0]

   try:
       lumberjack()
   except IndexError as exc:
       print("*** print_tb:")
       traceback.print_tb(exc.__traceback__, limit=1, file=sys.stdout)
       print("*** print_exception:")
       traceback.print_exception(exc, limit=2, file=sys.stdout)
       print("*** print_exc:")
       traceback.print_exc(limit=2, file=sys.stdout)
       print("*** format_exc, first and last line:")
       formatted_lines = traceback.format_exc().splitlines()
       print(formatted_lines[0])
       print(formatted_lines[-1])
       print("*** format_exception:")
       print(repr(traceback.format_exception(exc)))
       print("*** extract_tb:")
       print(repr(traceback.extract_tb(exc.__traceback__)))
       print("*** format_tb:")
       print(repr(traceback.format_tb(exc.__traceback__)))
       print("*** tb_lineno:", exc.__traceback__.tb_lineno)

La salida para el ejemplo podría ser similar a esto:

   *** print_tb:
     File "<doctest...>", line 10, in <module>
       lumberjack()
       ~~~~~~~~~~^^
   *** print_exception:
   Traceback (most recent call last):
     File "<doctest...>", line 10, in <module>
       lumberjack()
       ~~~~~~~~~~^^
     File "<doctest...>", line 4, in lumberjack
       bright_side_of_life()
       ~~~~~~~~~~~~~~~~~~~^^
   IndexError: tuple index out of range
   *** print_exc:
   Traceback (most recent call last):
     File "<doctest...>", line 10, in <module>
       lumberjack()
       ~~~~~~~~~~^^
     File "<doctest...>", line 4, in lumberjack
       bright_side_of_life()
       ~~~~~~~~~~~~~~~~~~~^^
   IndexError: tuple index out of range
   *** format_exc, first and last line:
   Traceback (most recent call last):
   IndexError: tuple index out of range
   *** format_exception:
   ['Traceback (most recent call last):\n',
    '  File "<doctest default[0]>", line 10, in <module>\n    lumberjack()\n    ~~~~~~~~~~^^\n',
    '  File "<doctest default[0]>", line 4, in lumberjack\n    bright_side_of_life()\n    ~~~~~~~~~~~~~~~~~~~^^\n',
    '  File "<doctest default[0]>", line 7, in bright_side_of_life\n    return tuple()[0]\n           ~~~~~~~^^^\n',
    'IndexError: tuple index out of range\n']
   *** extract_tb:
   [<FrameSummary file <doctest...>, line 10 in <module>>,
    <FrameSummary file <doctest...>, line 4 in lumberjack>,
    <FrameSummary file <doctest...>, line 7 in bright_side_of_life>]
   *** format_tb:
   ['  File "<doctest default[0]>", line 10, in <module>\n    lumberjack()\n    ~~~~~~~~~~^^\n',
    '  File "<doctest default[0]>", line 4, in lumberjack\n    bright_side_of_life()\n    ~~~~~~~~~~~~~~~~~~~^^\n',
    '  File "<doctest default[0]>", line 7, in bright_side_of_life\n    return tuple()[0]\n           ~~~~~~~^^^\n']
   *** tb_lineno: 10

El siguiente ejemplo muestra las diferentes maneras de imprimir y
formatear la pila:

   >>> import traceback
   >>> def another_function():
   ...     lumberstack()
   ...
   >>> def lumberstack():
   ...     traceback.print_stack()
   ...     print(repr(traceback.extract_stack()))
   ...     print(repr(traceback.format_stack()))
   ...
   >>> another_function()
     File "<doctest>", line 10, in <module>
       another_function()
     File "<doctest>", line 3, in another_function
       lumberstack()
     File "<doctest>", line 6, in lumberstack
       traceback.print_stack()
   [('<doctest>', 10, '<module>', 'another_function()'),
    ('<doctest>', 3, 'another_function', 'lumberstack()'),
    ('<doctest>', 7, 'lumberstack', 'print(repr(traceback.extract_stack()))')]
   ['  File "<doctest>", line 10, in <module>\n    another_function()\n',
    '  File "<doctest>", line 3, in another_function\n    lumberstack()\n',
    '  File "<doctest>", line 8, in lumberstack\n    print(repr(traceback.format_stack()))\n']

Este último ejemplo demuestra las últimas funciones de formateo:

   >>> import traceback
   >>> traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'),
   ...                        ('eggs.py', 42, 'eggs', 'return "bacon"')])
   ['  File "spam.py", line 3, in <module>\n    spam.eggs()\n',
    '  File "eggs.py", line 42, in eggs\n    return "bacon"\n']
   >>> an_error = IndexError('tuple index out of range')
   >>> traceback.format_exception_only(an_error)
   ['IndexError: tuple index out of range\n']

## Examples of Using "TracebackException"

With the helper class, we have more options:

   >>> import sys
   >>> from traceback import TracebackException
   >>>
   >>> def lumberjack():
   ...     bright_side_of_life()
   ...
   >>> def bright_side_of_life():
   ...     t = "bright", "side", "of", "life"
   ...     return t[5]
   ...
   >>> try:
   ...     lumberjack()
   ... except IndexError as e:
   ...     exc = e
   ...
   >>> try:
   ...     try:
   ...         lumberjack()
   ...     except:
   ...         1/0
   ... except Exception as e:
   ...     chained_exc = e
   ...
   >>> # limit works as with the module-level functions
   >>> TracebackException.from_exception(exc, limit=-2).print()
   Traceback (most recent call last):
     File "<python-input-1>", line 6, in lumberjack
       bright_side_of_life()
       ~~~~~~~~~~~~~~~~~~~^^
     File "<python-input-1>", line 10, in bright_side_of_life
       return t[5]
              ~^^^
   IndexError: tuple index out of range

   >>> # capture_locals adds local variables in frames
   >>> TracebackException.from_exception(exc, limit=-2, capture_locals=True).print()
   Traceback (most recent call last):
     File "<python-input-1>", line 6, in lumberjack
       bright_side_of_life()
       ~~~~~~~~~~~~~~~~~~~^^
     File "<python-input-1>", line 10, in bright_side_of_life
       return t[5]
              ~^^^
       t = ("bright", "side", "of", "life")
   IndexError: tuple index out of range

   >>> # The *chain* kwarg to print() controls whether chained
   >>> # exceptions are displayed
   >>> TracebackException.from_exception(chained_exc).print()
   Traceback (most recent call last):
     File "<python-input-19>", line 4, in <module>
       lumberjack()
       ~~~~~~~~~~^^
     File "<python-input-8>", line 7, in lumberjack
       bright_side_of_life()
       ~~~~~~~~~~~~~~~~~~~^^
     File "<python-input-8>", line 11, in bright_side_of_life
       return t[5]
              ~^^^
   IndexError: tuple index out of range

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<python-input-19>", line 6, in <module>
       1/0
       ~^~
   ZeroDivisionError: division by zero

   >>> TracebackException.from_exception(chained_exc).print(chain=False)
   Traceback (most recent call last):
     File "<python-input-19>", line 6, in <module>
       1/0
       ~^~
   ZeroDivisionError: division by zero
