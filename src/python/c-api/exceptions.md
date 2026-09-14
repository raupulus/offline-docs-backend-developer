---
title: Manejo de excepciones
source_url: https://docs.python.org/es/3
source_path: c-api/exceptions.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 250
---

# Manejo de excepciones

Las funciones descritas en este capítulo le permitirán manejar y
lanzar excepciones de Python.  Es importante comprender algunos de los
conceptos básicos del manejo de excepciones de Python.  Funciona de
manera similar a la variable POSIX "errno": hay un indicador global
(por hilo) del último error que ocurrió.  La mayoría de las funciones
de C API no borran esto en caso de éxito, pero lo configurarán para
indicar la causa del error en caso de falla. La mayoría de las
funciones de C API también retornan un indicador de error,
generalmente "NULL" si se supone que retornan un puntero, o "-1" si
retornan un número entero (excepción: las funciones "PyArg_*" retornan
"1" para el éxito y "0" para el fracaso).

Concretamente, el indicador de error consta de tres punteros de
objeto: el tipo de excepción, el valor de la excepción y el objeto de
rastreo. Cualquiera de esos punteros puede ser "NULL" si no está
configurado (aunque algunas combinaciones están prohibidas, por
ejemplo, no puede tener un rastreo no "NULL" si el tipo de excepción
es "NULL").

Cuando una función debe fallar porque alguna función que llamó falló,
generalmente no establece el indicador de error; la función que llamó
ya lo configuró. Es responsable de manejar el error y borrar la
excepción o regresar después de limpiar cualquier recurso que tenga
(como referencias de objetos o asignaciones de memoria); debería *no*
continuar normalmente si no está preparado para manejar el error. Si
regresa debido a un error, es importante indicarle a la persona que
llama que se ha establecido un error. Si el error no se maneja o se
propaga cuidadosamente, es posible que las llamadas adicionales a la
API de Python/C no se comporten como se espera y pueden fallar de
manera misteriosa.

Nota:

  The error indicator is **not** the result of "sys.exc_info()". The
  former corresponds to an exception that is not yet caught (and is
  therefore still propagating), while the latter returns an exception
  after it is caught (and has therefore stopped propagating).

## Impresión y limpieza

void PyErr_Clear()
    * Part of the Stable ABI.*

   Borra el indicador de error. Si el indicador de error no está
   configurado, no hay efecto.

void PyErr_PrintEx(int set_sys_last_vars)
    * Part of the Stable ABI.*

   Imprime un rastreo estándar en "sys.stderr" y borra el indicador de
   error. **A menos que** el error sea un "Salida del sistema", en ese
   caso no se imprime ningún rastreo y el proceso de Python se cerrará
   con el código de error especificado por la instancia de "Salida del
   sistema".

   Llame a esta función **solo** cuando el indicador de error está
   configurado. De lo contrario, provocará un error fatal!

   If *set_sys_last_vars* is nonzero, the variable "sys.last_exc" is
   set to the printed exception. For backwards compatibility, the
   deprecated variables "sys.last_type", "sys.last_value" and
   "sys.last_traceback" are also set to the type, value and traceback
   of this exception, respectively.

   Distinto en la versión 3.12: The setting of "sys.last_exc" was
   added.

void PyErr_Print()
    * Part of the Stable ABI.*

   Alias para "PyErr_PrintEx(1)".

void PyErr_WriteUnraisable(PyObject *obj)
    * Part of the Stable ABI.*

   Llama "sys.unraisablehook()" utilizando la excepción actual y el
   argumento *obj*.

   This utility function prints a warning message to "sys.stderr" when
   an exception has been set but it is impossible for the interpreter
   to actually raise the exception.  It is used, for example, when an
   exception occurs in an "__del__()" method.

   The function is called with a single argument *obj* that identifies
   the context in which the unraisable exception occurred. If
   possible, the repr of *obj* will be printed in the warning message.
   If *obj* is "NULL", only the traceback is printed.

   Se debe establecer una excepción al llamar a esta función.

   Distinto en la versión 3.4: Print a traceback. Print only traceback
   if *obj* is "NULL".

   Distinto en la versión 3.8: Use "sys.unraisablehook()".

void PyErr_FormatUnraisable(const char *format, ...)

   Similar to "PyErr_WriteUnraisable()", but the *format* and
   subsequent parameters help format the warning message; they have
   the same meaning and values as in "PyUnicode_FromFormat()".
   "PyErr_WriteUnraisable(obj)" is roughly equivalent to
   "PyErr_FormatUnraisable("Exception ignored in: %R", obj)". If
   *format* is "NULL", only the traceback is printed.

   Added in version 3.13.

void PyErr_DisplayException(PyObject *exc)
    * Part of the Stable ABI since version 3.12.*

   Print the standard traceback display of "exc" to "sys.stderr",
   including chained exceptions and notes.

   Added in version 3.12.

void PyErr_Display(PyObject *unused, PyObject *value, PyObject *tb)
    * Part of the Stable ABI.*

   Legacy variant of "PyErr_DisplayException()".

   Print the exception *value* with its traceback to "sys.stderr". If
   *value* has no traceback set, *tb* is used as its traceback. The
   first argument is ignored.

   If "sys.stderr" is "None", nothing is printed. If "sys.stderr" is
   not set, the exception is dumped to the C "stderr" stream instead.

   Obsoleto desde la versión 3.12: Use "PyErr_DisplayException()"
   instead.

## Lanzando excepciones

Estas funciones lo ayudan a configurar el indicador de error del hilo
actual. Por conveniencia, algunas de estas funciones siempre
retornarán un puntero "NULL" para usar en una declaración "return".

void PyErr_SetString(PyObject *type, const char *message)
    * Part of the Stable ABI.*

   This is the most common way to set the error indicator.  The first
   argument specifies the exception type; it is normally one of the
   standard exceptions, e.g. "PyExc_RuntimeError".  You need not
   create a new *strong reference* to it (e.g. with "Py_INCREF()").
   The second argument is an error message; it is decoded from
   "'utf-8'".

void PyErr_SetObject(PyObject *type, PyObject *value)
    * Part of the Stable ABI.*

   Esta función es similar a "PyErr_SetString()" pero le permite
   especificar un objeto Python arbitrario para el "valor" de la
   excepción.

PyObject *PyErr_Format(PyObject *exception, const char *format, ...)
    *Return value: Always NULL.** Part of the Stable ABI.*

   Esta función establece el indicador de error y retorna "NULL".
   *exception* debe ser una clase de excepción Python. El *format* y
   los parámetros posteriores ayudan a formatear el mensaje de error;
   tienen el mismo significado y valores que en
   "PyUnicode_FromFormat()". *format* es una cadena de caracteres
   codificada en ASCII.

PyObject *PyErr_FormatV(PyObject *exception, const char *format, va_list vargs)
    *Return value: Always NULL.** Part of the Stable ABI since version
   3.5.*

   Igual que "PyErr_Format()", pero tomando un argumento "va_list" en
   lugar de un número variable de argumentos.

   Added in version 3.5.

void PyErr_SetNone(PyObject *type)
    * Part of the Stable ABI.*

   Esta es una abreviatura de "PyErr_SetObject(type, Py_None)".

int PyErr_BadArgument()
    * Part of the Stable ABI.*

   Esta es una abreviatura de "PyErr_SetString(PyExc_TypeError,
   message)", donde *message* indica que se invocó una operación
   incorporada con un argumento ilegal. Es principalmente para uso
   interno.

PyObject *PyErr_NoMemory()
    *Return value: Always NULL.** Part of the Stable ABI.*

   Esta es una abreviatura de "PyErr_SetNone(PyExc_MemoryError)";
   retorna "NULL" para que una función de asignación de objetos pueda
   escribir "return PyErr_NoMemory();" cuando se queda sin memoria.

PyObject *PyErr_SetFromErrno(PyObject *type)
    *Return value: Always NULL.** Part of the Stable ABI.*

   This is a convenience function to raise an exception when a C
   library function has returned an error and set the C variable
   "errno".  It constructs a tuple object whose first item is the
   integer "errno" value and whose second item is the corresponding
   error message (gotten from "strerror()"), and then calls
   "PyErr_SetObject(type, object)".  On Unix, when the "errno" value
   is "EINTR", indicating an interrupted system call, this calls
   "PyErr_CheckSignals()", and if that set the error indicator, leaves
   it set to that.  The function always returns "NULL", so a wrapper
   function around a system call can write "return
   PyErr_SetFromErrno(type);" when the system call returns an error.

PyObject *PyErr_SetFromErrnoWithFilenameObject(PyObject *type, PyObject *filenameObject)
    *Return value: Always NULL.** Part of the Stable ABI.*

   Similar to "PyErr_SetFromErrno()", with the additional behavior
   that if *filenameObject* is not "NULL", it is passed to the
   constructor of *type* as a third parameter.  In the case of
   "OSError" exception, this is used to define the "filename"
   attribute of the exception instance.

PyObject *PyErr_SetFromErrnoWithFilenameObjects(PyObject *type, PyObject *filenameObject, PyObject *filenameObject2)
    *Return value: Always NULL.** Part of the Stable ABI since version
   3.7.*

   Similar a "PyErr_SetFromErrnoWithFilenameObject()", pero toma un
   segundo objeto de nombre de archivo, para lanzar errores cuando
   falla una función que toma dos nombres de archivo.

   Added in version 3.4.

PyObject *PyErr_SetFromErrnoWithFilename(PyObject *type, const char *filename)
    *Return value: Always NULL.** Part of the Stable ABI.*

   Similar a "PyErr_SetFromErrnoWithFilenameObject()", pero el nombre
   del archivo se da como una cadena de caracteres de C. *filename* se
   decodifica a partir de la codificación de *filesystem encoding and
   error handler*.

PyObject *PyErr_SetFromWindowsErr(int ierr)
    *Return value: Always NULL.** Part of the Stable ABI on Windows
   since version 3.7.*

   This is a convenience function to raise "OSError". If called with
   *ierr* of "0", the error code returned by a call to
   "GetLastError()" is used instead.  It calls the Win32 function
   "FormatMessage()" to retrieve the Windows description of error code
   given by *ierr* or "GetLastError()", then it constructs a "OSError"
   object with the "winerror" attribute set to the error code, the
   "strerror" attribute set to the corresponding error message (gotten
   from "FormatMessage()"), and then calls
   "PyErr_SetObject(PyExc_OSError, object)". This function always
   returns "NULL".

   Availability: Windows.

PyObject *PyErr_SetExcFromWindowsErr(PyObject *type, int ierr)
    *Return value: Always NULL.** Part of the Stable ABI on Windows
   since version 3.7.*

   Similar a "PyErr_SetFromWindowsErr()", con un parámetro adicional
   que especifica el tipo de excepción que se lanzará.

   Availability: Windows.

PyObject *PyErr_SetFromWindowsErrWithFilename(int ierr, const char *filename)
    *Return value: Always NULL.** Part of the Stable ABI on Windows
   since version 3.7.*

   Similar to "PyErr_SetFromWindowsErr()", with the additional
   behavior that if *filename* is not "NULL", it is decoded from the
   filesystem encoding ("os.fsdecode()") and passed to the constructor
   of "OSError" as a third parameter to be used to define the
   "filename" attribute of the exception instance.

   Availability: Windows.

PyObject *PyErr_SetExcFromWindowsErrWithFilenameObject(PyObject *type, int ierr, PyObject *filename)
    *Return value: Always NULL.** Part of the Stable ABI on Windows
   since version 3.7.*

   Similar to "PyErr_SetExcFromWindowsErr()", with the additional
   behavior that if *filename* is not "NULL", it is passed to the
   constructor of "OSError" as a third parameter to be used to define
   the "filename" attribute of the exception instance.

   Availability: Windows.

PyObject *PyErr_SetExcFromWindowsErrWithFilenameObjects(PyObject *type, int ierr, PyObject *filename, PyObject *filename2)
    *Return value: Always NULL.** Part of the Stable ABI on Windows
   since version 3.7.*

   Similar a "PyErr_SetExcFromWindowsErrWithFilenameObject()", pero
   acepta un segundo objeto de nombre de archivo.

   Availability: Windows.

   Added in version 3.4.

PyObject *PyErr_SetExcFromWindowsErrWithFilename(PyObject *type, int ierr, const char *filename)
    *Return value: Always NULL.** Part of the Stable ABI on Windows
   since version 3.7.*

   Similar a "PyErr_SetFromWindowsErrWithFilename()", con un parámetro
   adicional que especifica el tipo de excepción que se lanzará.

   Availability: Windows.

PyObject *PyErr_SetImportError(PyObject *msg, PyObject *name, PyObject *path)
    *Return value: Always NULL.** Part of the Stable ABI since version
   3.7.*

   Esta es una función conveniente para subir "ImportError". *msg* se
   establecerá como la cadena de mensaje de la excepción. *name* y
   *path*, que pueden ser "NULL", se establecerán como atributos
   respectivos "name" y "path" de "ImportError".

   Added in version 3.3.

PyObject *PyErr_SetImportErrorSubclass(PyObject *exception, PyObject *msg, PyObject *name, PyObject *path)
    *Return value: Always NULL.** Part of the Stable ABI since version
   3.6.*

   Al igual que "PyErr_SetImportError()" pero esta función permite
   especificar una subclase de "ImportError" para aumentar.

   Added in version 3.6.

void PyErr_SyntaxLocationObject(PyObject *filename, int lineno, int col_offset)

   Establece información de archivo, línea y desplazamiento para la
   excepción actual. Si la excepción actual no es un "SyntaxError",
   establece atributos adicionales, lo que hace que el sub sistema de
   impresión de excepciones piense que la excepción es "SyntaxError".

   Added in version 3.4.

void PyErr_RangedSyntaxLocationObject(PyObject *filename, int lineno, int col_offset, int end_lineno, int end_col_offset)

   Similar to "PyErr_SyntaxLocationObject()", but also sets the
   *end_lineno* and *end_col_offset* information for the current
   exception.

   Added in version 3.10.

void PyErr_SyntaxLocationEx(const char *filename, int lineno, int col_offset)
    * Part of the Stable ABI since version 3.7.*

   Como "PyErr_SyntaxLocationObject()", pero *filename* es una cadena
   de bytes decodificada a partir de *filesystem encoding and error
   handler*.

   Added in version 3.2.

void PyErr_SyntaxLocation(const char *filename, int lineno)
    * Part of the Stable ABI.*

   Como "PyErr_SyntaxLocationEx()", pero se omite el parámetro
   *col_offset*.

void PyErr_BadInternalCall()
    * Part of the Stable ABI.*

   Esta es una abreviatura de "PyErr_SetString(PyExc_SystemError,
   message)", donde *message* indica que se invocó una operación
   interna (por ejemplo, una función de Python/C API) con un argumento
   ilegal. Es principalmente para uso interno.

PyObject *PyErr_ProgramTextObject(PyObject *filename, int lineno)

   Get the source line in *filename* at line *lineno*. *filename*
   should be a Python "str" object.

   On success, this function returns a Python string object with the
   found line. On failure, this function returns "NULL" without an
   exception set.

PyObject *PyErr_ProgramText(const char *filename, int lineno)
    * Part of the Stable ABI.*

   Similar to "PyErr_ProgramTextObject()", but *filename* is a const
   char*, which is decoded with the *filesystem encoding and error
   handler*, instead of a Python object reference.

## Emitir advertencias

Use estas funciones para emitir advertencias desde el código C.
Reflejan funciones similares exportadas por el módulo Python
"warnings". Normalmente imprimen un mensaje de advertencia a
*sys.stderr*; sin embargo, también es posible que el usuario haya
especificado que las advertencias se conviertan en errores, y en ese
caso lanzarán una excepción. También es posible que las funciones
generen una excepción debido a un problema con la maquinaria de
advertencia. El valor de retorno es "0" si no se lanza una excepción,
o "-1" si se lanza una excepción. (No es posible determinar si
realmente se imprime un mensaje de advertencia, ni cuál es el motivo
de la excepción; esto es intencional). Si se produce una excepción, la
persona que llama debe hacer su manejo normal de excepciones (por
ejemplo, referencias propiedad de "Py_DECREF()" y retornan un valor de
error).

int PyErr_WarnEx(PyObject *category, const char *message, Py_ssize_t stack_level)
    * Part of the Stable ABI.*

   Emite un mensaje de advertencia. El argumento *category* es una
   categoría de advertencia (ver más abajo) o "NULL"; el argumento
   *message* es una cadena de caracteres codificada en UTF-8.
   *stack_level* es un número positivo que proporciona una cantidad de
   marcos de pila; la advertencia se emitirá desde la línea de código
   que se está ejecutando actualmente en ese marco de pila. Un
   *stack_level* de 1 es la función que llama "PyErr_WarnEx()", 2 es
   la función por encima de eso, y así sucesivamente.

   Las categorías de advertencia deben ser subclases de
   "PyExc_Warning"; "PyExc_Warning" es una subclase de
   "PyExc_Exception"; la categoría de advertencia predeterminada es
   "PyExc_RuntimeWarning". Las categorías de advertencia estándar de
   Python están disponibles como variables globales cuyos nombres se
   enumeran en Warning types.

   Para obtener información sobre el control de advertencia, consulte
   la documentación del módulo "warnings" y la opción "-W" en la
   documentación de la línea de comandos. No hay API de C para el
   control de advertencia.

int PyErr_WarnExplicitObject(PyObject *category, PyObject *message, PyObject *filename, int lineno, PyObject *module, PyObject *registry)

   Emite un mensaje de advertencia con control explícito sobre todos
   los atributos de advertencia.  Este es un contenedor sencillo
   alrededor de la función Python "warnings.warn_explicit()"; consulte
   allí para obtener más información.  Los argumentos *module* y
   *registry* pueden establecerse en "NULL" para obtener el efecto
   predeterminado que se describe allí.

   Added in version 3.4.

int PyErr_WarnExplicit(PyObject *category, const char *message, const char *filename, int lineno, const char *module, PyObject *registry)
    * Part of the Stable ABI.*

   Similar a "PyErr_WarnExplicitObject()" excepto que *message* y
   *module* son cadenas codificadas UTF-8, y *filename* se decodifica
   de *filesystem encoding and error handler*.

int PyErr_WarnFormat(PyObject *category, Py_ssize_t stack_level, const char *format, ...)
    * Part of the Stable ABI.*

   Function similar to "PyErr_WarnEx()", but uses
   "PyUnicode_FromFormat()" to format the warning message.  *format*
   is an ASCII-encoded string.

   Added in version 3.2.

int PyErr_WarnExplicitFormat(PyObject *category, const char *filename, int lineno, const char *module, PyObject *registry, const char *format, ...)

   Similar to "PyErr_WarnExplicit()", but uses
   "PyUnicode_FromFormat()" to format the warning message. *format* is
   an ASCII-encoded string.

   Added in version 3.2.

int PyErr_ResourceWarning(PyObject *source, Py_ssize_t stack_level, const char *format, ...)
    * Part of the Stable ABI since version 3.6.*

   Function similar to "PyErr_WarnFormat()", but *category* is
   "ResourceWarning" and it passes *source* to
   "warnings.WarningMessage".

   Added in version 3.6.

## Consultando el indicador de error

PyObject *PyErr_Occurred()
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Prueba si el indicador de error está configurado.  Si se establece,
   retorna la excepción *type* (el primer argumento de la última
   llamada a una de las funciones "PyErr_Set*" o "PyErr_Restore()").
   Si no está configurado, retorna "NULL".  No posee una referencia al
   valor de retorno, por lo que no necesita usar "Py_DECREF()".

   The caller must have an *attached thread state*.

   Nota:

     No compare el valor de retorno con una excepción específica; use
     "PyErr_ExceptionMatches()" en su lugar, como se muestra a
     continuación. (La comparación podría fallar fácilmente ya que la
     excepción puede ser una instancia en lugar de una clase, en el
     caso de una excepción de clase, o puede ser una subclase de la
     excepción esperada).

int PyErr_ExceptionMatches(PyObject *exc)
    * Part of the Stable ABI.*

   Equivalente a "PyErr_GivenExceptionMatches(PyErr_Occurred(), exc)".
   Esto solo debería llamarse cuando se establece una excepción; se
   producirá una infracción de acceso a la memoria si no se ha
   producido ninguna excepción.

int PyErr_GivenExceptionMatches(PyObject *given, PyObject *exc)
    * Part of the Stable ABI.*

   Retorna verdadero si la excepción *dada* coincide con el tipo de
   excepción en *exc*. Si *exc* es un objeto de clase, esto también
   retorna verdadero cuando *dado* es una instancia de una subclase.
   Si *exc* es una tupla, se busca una coincidencia en todos los tipos
   de excepción en la tupla (y recursivamente en sub tuplas).

PyObject *PyErr_GetRaisedException(void)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.12.*

   Return the exception currently being raised, clearing the error
   indicator at the same time. Return "NULL" if the error indicator is
   not set.

   This function is used by code that needs to catch exceptions, or
   code that needs to save and restore the error indicator
   temporarily.

   For example:

      {
         PyObject *exc = PyErr_GetRaisedException();

         /* ... code that might produce other errors ... */

         PyErr_SetRaisedException(exc);
      }

   Ver también:

     "PyErr_GetHandledException()", to save the exception currently
     being handled.

   Added in version 3.12.

void PyErr_SetRaisedException(PyObject *exc)
    * Part of the Stable ABI since version 3.12.*

   Set *exc* as the exception currently being raised, clearing the
   existing exception if one is set.  If *exc* is "NULL", just clear
   the existing exception.

   *exc* must be a valid exception or "NULL".

   This call "*steals*" a reference to *exc*.

   Added in version 3.12.

void PyErr_Fetch(PyObject **ptype, PyObject **pvalue, PyObject **ptraceback)
    * Part of the Stable ABI.*

   Obsoleto desde la versión 3.12: Use "PyErr_GetRaisedException()"
   instead.

   Recupera el indicador de error en tres variables cuyas direcciones
   se pasan. Si el indicador de error no está configurado, configure
   las tres variables en "NULL".  Si está configurado, se borrará y
   usted tendrá una referencia a cada objeto recuperado. El objeto de
   valor y rastreo puede ser "NULL" incluso cuando el objeto de tipo
   no lo es.

   Nota:

     This function is normally only used by legacy code that needs to
     catch exceptions or save and restore the error indicator
     temporarily.For example:

        {
           PyObject *type, *value, *traceback;
           PyErr_Fetch(&type, &value, &traceback);

           /* ... code that might produce other errors ... */

           PyErr_Restore(type, value, traceback);
        }

void PyErr_Restore(PyObject *type, PyObject *value, PyObject *traceback)
    * Part of the Stable ABI.*

   Obsoleto desde la versión 3.12: Use "PyErr_SetRaisedException()"
   instead.

   Set the error indicator from the three objects, *type*, *value*,
   and *traceback*, clearing the existing exception if one is set. If
   the objects are "NULL", the error indicator is cleared.  Do not
   pass a "NULL" type and non-"NULL" value or traceback.  The
   exception type should be a class.  Do not pass an invalid exception
   type or value. (Violating these rules will cause subtle problems
   later.)  This call takes away a reference to each object: you must
   own a reference to each object before the call and after the call
   you no longer own these references.  (If you don't understand this,
   don't use this function.  I warned you.)

   Nota:

     This function is normally only used by legacy code that needs to
     save and restore the error indicator temporarily. Use
     "PyErr_Fetch()" to save the current error indicator.

void PyErr_NormalizeException(PyObject **exc, PyObject **val, PyObject **tb)
    * Part of the Stable ABI.*

   Obsoleto desde la versión 3.12: Use "PyErr_GetRaisedException()"
   instead, to avoid any possible de-normalization.

   Bajo ciertas circunstancias, los valores retornados por
   "PyErr_Fetch()" a continuación pueden ser "no normalizados", lo que
   significa que "*exc" es un objeto de clase pero "*val" no es una
   instancia de la misma clase . Esta función se puede utilizar para
   crear instancias de la clase en ese caso. Si los valores ya están
   normalizados, no pasa nada. La normalización retrasada se
   implementa para mejorar el rendimiento.

   Nota:

     This function *does not* implicitly set the "__traceback__"
     attribute on the exception value. If setting the traceback
     appropriately is desired, the following additional snippet is
     needed:

        if (tb != NULL) {
          PyException_SetTraceback(val, tb);
        }

PyObject *PyErr_GetHandledException(void)
    * Part of the Stable ABI since version 3.11.*

   Recupera la instancia de excepción activa, como la que devolvería
   "sys.exception()". Esto se refiere a una excepción que *ya fue
   capturada*, no a una excepción recién lanzada. Retorna una nueva
   referencia a la excepción o "NULL". No modifica el estado de
   excepción del intérprete.

   Nota:

     Esta función normalmente no es utilizada por el código que quiere
     manejar excepciones. En cambio, se puede usar cuando el código
     necesita guardar y restaurar el estado de excepción
     temporalmente.   Use "PyErr_SetHandledException()" para restaurar
     o borrar el estado de excepción.

   Added in version 3.11.

void PyErr_SetHandledException(PyObject *exc)
    * Part of the Stable ABI since version 3.11.*

   Establece la excepción activa, como se conoce de "sys.exception()".
   Esto se refiere a la excepción que **ya fue capturada**, no a una
   excepción que fue lanzada recientemente. Para borrar el estado de
   la excepción, pasa "NULL".

   Nota:

     Esta función normalmente no es utilizada por el código que quiere
     manejar excepciones. En cambio, se puede usar cuando el código
     necesita guardar y restaurar el estado de excepción
     temporalmente. Use "PyErr_GetHandledException()" para leer el
     estado de excepción.

   Added in version 3.11.

void PyErr_GetExcInfo(PyObject **ptype, PyObject **pvalue, PyObject **ptraceback)
    * Part of the Stable ABI since version 3.7.*

   Recupera la información de excepción, como se conoce de
   "sys.exc_info()".  Esto se refiere a una excepción que *ya fue
   capturada*, no a una excepción que fue lanzada recientemente.
   Retorna nuevas referencias para los tres objetos, cualquiera de los
   cuales puede ser "NULL".  No modifica el estado de información de
   excepción.  Esta función se mantiene por retro-compatibilidad. Es
   preferible usar "PyErr_GetHandledException()".

   Nota:

     Esta función normalmente no es utilizada por el código que quiere
     manejar excepciones. En cambio, se puede usar cuando el código
     necesita guardar y restaurar el estado de excepción
     temporalmente. Use "PyErr_SetExcInfo()" para restaurar o borrar
     el estado de excepción.

   Added in version 3.3.

void PyErr_SetExcInfo(PyObject *type, PyObject *value, PyObject *traceback)
    * Part of the Stable ABI since version 3.7.*

   Set the exception info, as known from "sys.exc_info()".  This
   refers to an exception that was *already caught*, not to an
   exception that was freshly raised.  This function "*steals*" the
   references of the arguments. To clear the exception state, pass
   "NULL" for all three arguments. This function is kept for backwards
   compatibility. Prefer using "PyErr_SetHandledException()".

   Nota:

     Esta función normalmente no es utilizada por el código que quiere
     manejar excepciones. En cambio, se puede usar cuando el código
     necesita guardar y restaurar el estado de excepción
     temporalmente. Use "PyErr_GetExcInfo()" para leer el estado de
     excepción.

   Added in version 3.3.

   Distinto en la versión 3.11: The "type" and "traceback" arguments
   are no longer used and can be NULL. The interpreter now derives
   them from the exception instance (the "value" argument). The
   function still "*steals*" references of all three arguments.

## Manejo de señal

int PyErr_CheckSignals()
    * Part of the Stable ABI.*

   Handle external interruptions, such as signals or activating a
   debugger, whose processing has been delayed until it is safe to run
   Python code and/or raise exceptions.

   For example, pressing "Ctrl"-"C" causes a terminal to send the
   "signal.SIGINT" signal. This function executes the corresponding
   Python signal handler, which, by default, raises the
   "KeyboardInterrupt" exception.

   "PyErr_CheckSignals()" should be called by long-running C code
   frequently enough so that the response appears immediate to humans.

   Handlers invoked by this function currently include:

   * Signal handlers, including Python functions registered using the
     "signal" module.

     Signal handlers are only run in the main thread of the main
     interpreter.

     (This is where the function got the name: originally, signals
     were the only way to interrupt the interpreter.)

   * Running the garbage collector, if necessary.

   * Executing a pending remote debugger script.

   If any handler raises an exception, immediately return "-1" with
   that exception set. Any remaining interruptions are left to be
   processed on the next "PyErr_CheckSignals()" invocation, if
   appropriate.

   If all handlers finish successfully, or there are no handlers to
   run, return "0".

   Distinto en la versión 3.12: This function may now invoke the
   garbage collector.

   Distinto en la versión 3.14: This function may now execute a remote
   debugger script, if remote debugging is enabled.

void PyErr_SetInterrupt()
    * Part of the Stable ABI.*

   Simulate the effect of a "SIGINT" signal arriving. This is
   equivalent to "PyErr_SetInterruptEx(SIGINT)".

   Nota:

     This function is async-signal-safe.  It can be called without an
     *attached thread state* and from a C signal handler.

int PyErr_SetInterruptEx(int signum)
    * Part of the Stable ABI since version 3.10.*

   Simula el efecto de la llegada de una señal. La próxima vez que sea
   llamado "PyErr_CheckSignals()", se llamará al manejador de señal de
   Python para el número de señal dado.

   Esta función puede ser llamada por código C que configura su propio
   manejo de señales y quiere que los manejadores de señales de Python
   sean invocados como se espera cuando se solicita una interrupción
   (por ejemplo, cuando el usuario presiona Ctrl-C para interrumpir
   una operación).

   If the given signal isn't handled by Python (it was set to
   "signal.SIG_DFL" or "signal.SIG_IGN"), it will be ignored.

   Si *signum* está fuera del rango permitido de números de señal, se
   devuelve "-1". De lo contrario, se devuelve "0". Esta función nunca
   cambia el indicador de error.

   Nota:

     This function is async-signal-safe.  It can be called without an
     *attached thread state* and from a C signal handler.

   Added in version 3.10.

int PySignal_SetWakeupFd(int fd)

   Esta función de utilidad especifica un descriptor de archivo en el
   que el número de señal se escribe como un solo byte cada vez que se
   recibe una señal. *fd* debe ser sin bloqueo. retorna el descriptor
   de archivo anterior.

   El valor "-1" desactiva la función; Este es el estado inicial. Esto
   es equivalente a "signal.set_wakeup_fd()" en Python, pero sin
   verificación de errores. *fd* debe ser un descriptor de archivo
   válido. La función solo debe llamarse desde el hilo principal.

   Distinto en la versión 3.5: En Windows, la función ahora también
   admite controladores de socket.

## Clases de excepción

PyObject *PyErr_NewException(const char *name, PyObject *base, PyObject *dict)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta función de utilidad crea y retorna una nueva clase de
   excepción. El argumento *name* debe ser el nombre de la nueva
   excepción, una cadena de caracteres en C de la forma
   "module.classname". Los argumentos *base* y *dict* son normalmente
   "NULL". Esto crea un objeto de clase derivado de "Exception"
   (accesible en C como "PyExc_Exception").

   The "__module__" attribute of the new class is set to the first
   part (up to the last dot) of the *name* argument, and the class
   name is set to the last part (after the last dot).  The *base*
   argument can be used to specify alternate base classes; it can
   either be only one class or a tuple of classes. The *dict* argument
   can be used to specify a dictionary of class variables and methods.

PyObject *PyErr_NewExceptionWithDoc(const char *name, const char *doc, PyObject *base, PyObject *dict)
    *Return value: New reference.** Part of the Stable ABI.*

   Igual que "PyErr_NewException()", excepto que la nueva clase de
   excepción puede recibir fácilmente una cadena de documentación: si
   *doc* no es "NULL", se utilizará como la cadena de documentación
   para la clase de excepción.

   Added in version 3.2.

int PyExceptionClass_Check(PyObject *ob)

   Return non-zero if *ob* is an exception class, zero otherwise. This
   function always succeeds.

const char *PyExceptionClass_Name(PyObject *ob)
    * Part of the Stable ABI since version 3.8.*

   Return "tp_name" of the exception class *ob*.

## Objetos excepción

int PyExceptionInstance_Check(PyObject *op)

   Return true if *op* is an instance of "BaseException", false
   otherwise. This function always succeeds.

PyExceptionInstance_Class(op)

   Equivalent to "Py_TYPE(op)".

PyObject *PyException_GetTraceback(PyObject *ex)
    *Return value: New reference.** Part of the Stable ABI.*

   Return the traceback associated with the exception as a new
   reference, as accessible from Python through the "__traceback__"
   attribute. If there is no traceback associated, this returns
   "NULL".

int PyException_SetTraceback(PyObject *ex, PyObject *tb)
    * Part of the Stable ABI.*

   Establezca el rastreo asociado con la excepción a *tb*. Use
   "Py_None" para borrarlo.

PyObject *PyException_GetContext(PyObject *ex)
    *Return value: New reference.** Part of the Stable ABI.*

   Return the context (another exception instance during whose
   handling *ex* was raised) associated with the exception as a new
   reference, as accessible from Python through the "__context__"
   attribute. If there is no context associated, this returns "NULL".

void PyException_SetContext(PyObject *ex, PyObject *ctx)
    * Part of the Stable ABI.*

   Set the context associated with the exception to *ctx*.  Use "NULL"
   to clear it.  There is no type check to make sure that *ctx* is an
   exception instance. This "*steals*" a reference to *ctx*.

PyObject *PyException_GetCause(PyObject *ex)
    *Return value: New reference.** Part of the Stable ABI.*

   Return the cause (either an exception instance, or "None", set by
   "raise ... from ...") associated with the exception as a new
   reference, as accessible from Python through the "__cause__"
   attribute.

void PyException_SetCause(PyObject *ex, PyObject *cause)
    * Part of the Stable ABI.*

   Set the cause associated with the exception to *cause*.  Use "NULL"
   to clear it.  There is no type check to make sure that *cause* is
   either an exception instance or "None". This "*steals*" a reference
   to *cause*.

   The "__suppress_context__" attribute is implicitly set to "True" by
   this function.

PyObject *PyException_GetArgs(PyObject *ex)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.12.*

   Return "args" of exception *ex*.

void PyException_SetArgs(PyObject *ex, PyObject *args)
    * Part of the Stable ABI since version 3.12.*

   Set "args" of exception *ex* to *args*.

PyObject *PyUnstable_Exc_PrepReraiseStar(PyObject *orig, PyObject *excs)

   *This is Unstable API. It may change without warning in minor
   releases.*

   Implement part of the interpreter's implementation of "except*".
   *orig* is the original exception that was caught, and *excs* is the
   list of the exceptions that need to be raised. This list contains
   the unhandled part of *orig*, if any, as well as the exceptions
   that were raised from the "except*" clauses (so they have a
   different traceback from *orig*) and those that were reraised (and
   have the same traceback as *orig*). Return the "ExceptionGroup"
   that needs to be reraised in the end, or "None" if there is nothing
   to reraise.

   Added in version 3.12.

## Objetos unicode de excepción

Las siguientes funciones se utilizan para crear y modificar
excepciones Unicode de C.

PyObject *PyUnicodeDecodeError_Create(const char *encoding, const char *object, Py_ssize_t length, Py_ssize_t start, Py_ssize_t end, const char *reason)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto "UnicodeDecodeError" con los atributos *encoding*,
   *object*, *length*, *start*, *end* y *reason*. *encoding* y
   *reason* son cadenas codificadas UTF-8.

PyObject *PyUnicodeDecodeError_GetEncoding(PyObject *exc)
PyObject *PyUnicodeEncodeError_GetEncoding(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el atributo *encoding* del objeto de excepción dado.

PyObject *PyUnicodeDecodeError_GetObject(PyObject *exc)
PyObject *PyUnicodeEncodeError_GetObject(PyObject *exc)
PyObject *PyUnicodeTranslateError_GetObject(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el atributo *object* del objeto de excepción dado.

int PyUnicodeDecodeError_GetStart(PyObject *exc, Py_ssize_t *start)
int PyUnicodeEncodeError_GetStart(PyObject *exc, Py_ssize_t *start)
int PyUnicodeTranslateError_GetStart(PyObject *exc, Py_ssize_t *start)
    * Part of the Stable ABI.*

   Obtiene el atributo *start* del objeto de excepción dado y lo
   coloca en **start*. *start* no debe ser "NULL". retorna "0" en caso
   de éxito, "-1" en caso de error.

   If the "UnicodeError.object" is an empty sequence, the resulting
   *start* is "0". Otherwise, it is clipped to "[0, len(object) - 1]".

   Ver también: "UnicodeError.start"

int PyUnicodeDecodeError_SetStart(PyObject *exc, Py_ssize_t start)
int PyUnicodeEncodeError_SetStart(PyObject *exc, Py_ssize_t start)
int PyUnicodeTranslateError_SetStart(PyObject *exc, Py_ssize_t start)
    * Part of the Stable ABI.*

   Set the *start* attribute of the given exception object to *start*.
   Return "0" on success, "-1" on failure.

   Nota:

     While passing a negative *start* does not raise an exception, the
     corresponding getters will not consider it as a relative offset.

int PyUnicodeDecodeError_GetEnd(PyObject *exc, Py_ssize_t *end)
int PyUnicodeEncodeError_GetEnd(PyObject *exc, Py_ssize_t *end)
int PyUnicodeTranslateError_GetEnd(PyObject *exc, Py_ssize_t *end)
    * Part of the Stable ABI.*

   Obtiene el atributo *end* del objeto de excepción dado y lo coloca
   en **end*. *end* no debe ser "NULL". retorna "0" en caso de éxito,
   "-1" en caso de error.

   If the "UnicodeError.object" is an empty sequence, the resulting
   *end* is "0". Otherwise, it is clipped to "[1, len(object)]".

int PyUnicodeDecodeError_SetEnd(PyObject *exc, Py_ssize_t end)
int PyUnicodeEncodeError_SetEnd(PyObject *exc, Py_ssize_t end)
int PyUnicodeTranslateError_SetEnd(PyObject *exc, Py_ssize_t end)
    * Part of the Stable ABI.*

   Establece el atributo *end* del objeto de excepción dado en *end*.
   Retorna "0" en caso de éxito, "-1" en caso de error.

   Ver también: "UnicodeError.end"

PyObject *PyUnicodeDecodeError_GetReason(PyObject *exc)
PyObject *PyUnicodeEncodeError_GetReason(PyObject *exc)
PyObject *PyUnicodeTranslateError_GetReason(PyObject *exc)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna el atributo *reason* del objeto de excepción dado.

int PyUnicodeDecodeError_SetReason(PyObject *exc, const char *reason)
int PyUnicodeEncodeError_SetReason(PyObject *exc, const char *reason)
int PyUnicodeTranslateError_SetReason(PyObject *exc, const char *reason)
    * Part of the Stable ABI.*

   Establece el atributo *reason* del objeto de excepción dado en
   *reason*. Retorna "0" en caso de éxito, "-1" en caso de error.

## Control de recursión

Estas dos funciones proporcionan una forma de realizar llamadas
recursivas seguras en el nivel C, tanto en el núcleo como en los
módulos de extensión. Son necesarios si el código recursivo no invoca
necesariamente el código Python (que rastrea su profundidad de
recursión automáticamente). Tampoco son necesarios para las
implementaciones de *tp_call* porque call protocol se encarga del
manejo de la recursividad.

int Py_EnterRecursiveCall(const char *where)
    * Part of the Stable ABI since version 3.9.*

   Marca un punto donde una llamada recursiva de nivel C está a punto
   de realizarse.

   The function then checks if the stack limit is reached.  If this is
   the case, a "RecursionError" is set and a nonzero value is
   returned. Otherwise, zero is returned.

   *where* debería ser una cadena de caracteres codificada en UTF-8
   como ""en la comprobación de instancia"" para concatenarse con el
   mensaje "RecursionError" causado por el límite de profundidad de
   recursión.

   Ver también:

     The "PyUnstable_ThreadState_SetStackProtection()" function.

   Distinto en la versión 3.9: This function is now also available in
   the limited API.

void Py_LeaveRecursiveCall(void)
    * Part of the Stable ABI since version 3.9.*

   Termina una "Py_EnterRecursiveCall()". Se debe llamar una vez por
   cada invocación *exitosa* de "Py_EnterRecursiveCall()".

   Distinto en la versión 3.9: This function is now also available in
   the limited API.

Properly implementing "tp_repr" for container types requires special
recursion handling.  In addition to protecting the stack, "tp_repr"
also needs to track objects to prevent cycles.  The following two
functions facilitate this functionality.  Effectively, these are the C
equivalent to "@reprlib.recursive_repr".

int Py_ReprEnter(PyObject *object)
    * Part of the Stable ABI.*

   Llamado al comienzo de la implementación "tp_repr" para detectar
   ciclos.

   Si el objeto ya ha sido procesado, la función retorna un entero
   positivo. En ese caso, la implementación "tp_repr" debería retornar
   un objeto de cadena que indique un ciclo. Como ejemplos, los
   objetos "dict" retornan "{...}" y los objetos "list" retornan
   "[...]".

   La función retornará un entero negativo si se alcanza el límite de
   recursión. En ese caso, la implementación "tp_repr" normalmente
   debería retornar "NULL".

   De lo contrario, la función retorna cero y la implementación
   "tp_repr" puede continuar normalmente.

void Py_ReprLeave(PyObject *object)
    * Part of the Stable ABI.*

   Termina a "Py_ReprEnter()". Se debe llamar una vez por cada
   invocación de "Py_ReprEnter()" que retorna cero.

int Py_GetRecursionLimit(void)
    * Part of the Stable ABI.*

   Get the recursion limit for the current interpreter. It can be set
   with "Py_SetRecursionLimit()". The recursion limit prevents the
   Python interpreter stack from growing infinitely.

   This function cannot fail, and the caller must hold an *attached
   thread state*.

   Ver también: "sys.getrecursionlimit()"

void Py_SetRecursionLimit(int new_limit)
    * Part of the Stable ABI.*

   Set the recursion limit for the current interpreter.

   This function cannot fail, and the caller must hold an *attached
   thread state*.

   Ver también: "sys.setrecursionlimit()"

## Exception and warning types

All standard Python exceptions and warning categories are available as
global variables whose names are "PyExc_" followed by the Python
exception name. These have the type PyObject*; they are all class
objects.

For completeness, here are all the variables:

### Exception types

+----------------------------------------------------+----------------------------------------------------+
| C name                                             | Python name                                        |
|====================================================|====================================================|
| PyObject *PyExc_BaseException  * Part of the       | "BaseException"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_BaseExceptionGroup  * Part of the  | "BaseExceptionGroup"                               |
## | Stable ABI since version 3.11.*                    |                                                    |

| PyObject *PyExc_Exception  * Part of the Stable    | "Exception"                                        |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_ArithmeticError  * Part of the     | "ArithmeticError"                                  |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_AssertionError  * Part of the      | "AssertionError"                                   |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_AttributeError  * Part of the      | "AttributeError"                                   |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_BlockingIOError  * Part of the     | "BlockingIOError"                                  |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_BrokenPipeError  * Part of the     | "BrokenPipeError"                                  |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_BufferError  * Part of the Stable  | "BufferError"                                      |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_ChildProcessError  * Part of the   | "ChildProcessError"                                |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_ConnectionAbortedError  * Part of  | "ConnectionAbortedError"                           |
## | the Stable ABI since version 3.7.*                 |                                                    |

| PyObject *PyExc_ConnectionError  * Part of the     | "ConnectionError"                                  |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_ConnectionRefusedError  * Part of  | "ConnectionRefusedError"                           |
## | the Stable ABI since version 3.7.*                 |                                                    |

| PyObject *PyExc_ConnectionResetError  * Part of    | "ConnectionResetError"                             |
## | the Stable ABI since version 3.7.*                 |                                                    |

| PyObject *PyExc_EOFError  * Part of the Stable     | "EOFError"                                         |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_FileExistsError  * Part of the     | "FileExistsError"                                  |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_FileNotFoundError  * Part of the   | "FileNotFoundError"                                |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_FloatingPointError  * Part of the  | "FloatingPointError"                               |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_GeneratorExit  * Part of the       | "GeneratorExit"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_ImportError  * Part of the Stable  | "ImportError"                                      |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_IndentationError  * Part of the    | "IndentationError"                                 |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_IndexError  * Part of the Stable   | "IndexError"                                       |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_InterruptedError  * Part of the    | "InterruptedError"                                 |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_IsADirectoryError  * Part of the   | "IsADirectoryError"                                |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_KeyError  * Part of the Stable     | "KeyError"                                         |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_KeyboardInterrupt  * Part of the   | "KeyboardInterrupt"                                |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_LookupError  * Part of the Stable  | "LookupError"                                      |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_MemoryError  * Part of the Stable  | "MemoryError"                                      |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_ModuleNotFoundError  * Part of the | "ModuleNotFoundError"                              |
## | Stable ABI since version 3.6.*                     |                                                    |

| PyObject *PyExc_NameError  * Part of the Stable    | "NameError"                                        |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_NotADirectoryError  * Part of the  | "NotADirectoryError"                               |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_NotImplementedError  * Part of the | "NotImplementedError"                              |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_OSError  * Part of the Stable      | "OSError"                                          |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_OverflowError  * Part of the       | "OverflowError"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_PermissionError  * Part of the     | "PermissionError"                                  |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_ProcessLookupError  * Part of the  | "ProcessLookupError"                               |
## | Stable ABI since version 3.7.*                     |                                                    |

## | PyObject *PyExc_PythonFinalizationError            | "PythonFinalizationError"                          |

| PyObject *PyExc_RecursionError  * Part of the      | "RecursionError"                                   |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_ReferenceError  * Part of the      | "ReferenceError"                                   |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_RuntimeError  * Part of the Stable | "RuntimeError"                                     |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_StopAsyncIteration  * Part of the  | "StopAsyncIteration"                               |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_StopIteration  * Part of the       | "StopIteration"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_SyntaxError  * Part of the Stable  | "SyntaxError"                                      |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_SystemError  * Part of the Stable  | "SystemError"                                      |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_SystemExit  * Part of the Stable   | "SystemExit"                                       |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_TabError  * Part of the Stable     | "TabError"                                         |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_TimeoutError  * Part of the Stable | "TimeoutError"                                     |
## | ABI since version 3.7.*                            |                                                    |

| PyObject *PyExc_TypeError  * Part of the Stable    | "TypeError"                                        |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_UnboundLocalError  * Part of the   | "UnboundLocalError"                                |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_UnicodeDecodeError  * Part of the  | "UnicodeDecodeError"                               |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_UnicodeEncodeError  * Part of the  | "UnicodeEncodeError"                               |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_UnicodeError  * Part of the Stable | "UnicodeError"                                     |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_UnicodeTranslateError  * Part of   | "UnicodeTranslateError"                            |
## | the Stable ABI.*                                   |                                                    |

| PyObject *PyExc_ValueError  * Part of the Stable   | "ValueError"                                       |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_ZeroDivisionError  * Part of the   | "ZeroDivisionError"                                |
## | Stable ABI.*                                       |                                                    |

Added in version 3.3: "PyExc_BlockingIOError",
"PyExc_BrokenPipeError", "PyExc_ChildProcessError",
"PyExc_ConnectionError", "PyExc_ConnectionAbortedError",
"PyExc_ConnectionRefusedError", "PyExc_ConnectionResetError",
"PyExc_FileExistsError", "PyExc_FileNotFoundError",
"PyExc_InterruptedError", "PyExc_IsADirectoryError",
"PyExc_NotADirectoryError", "PyExc_PermissionError",
"PyExc_ProcessLookupError" y "PyExc_TimeoutError" fueron introducidos
luego de **PEP 3151**.

Added in version 3.5: "PyExc_StopAsyncIteration" y
"PyExc_RecursionError".

Added in version 3.6: "PyExc_ModuleNotFoundError".

Added in version 3.11: "PyExc_BaseExceptionGroup".

### OSError aliases

The following are a compatibility aliases to "PyExc_OSError".

Distinto en la versión 3.3: Estos alias solían ser tipos de excepción
separados.

+-----------------------------------+-----------------------------------+-----------------------------------+
| C name                            | Python name                       | Notas                             |
|===================================|===================================|===================================|
| PyObject *PyExc_EnvironmentError  | "OSError"                         |                                   |
## | * Part of the Stable ABI.*        |                                   |                                   |

| PyObject *PyExc_IOError  * Part   | "OSError"                         |                                   |
## | of the Stable ABI.*               |                                   |                                   |

| PyObject *PyExc_WindowsError  *   | "OSError"                         | [win]                             |
| Part of the Stable ABI on Windows |                                   |                                   |
## | since version 3.7.*               |                                   |                                   |

Notas:

[win] "PyExc_WindowsError" is only defined on Windows; protect code
      that uses this by testing that the preprocessor macro
      "MS_WINDOWS" is defined.

### Warning types

+----------------------------------------------------+----------------------------------------------------+
| C name                                             | Python name                                        |
|====================================================|====================================================|
| PyObject *PyExc_Warning  * Part of the Stable      | "Warning"                                          |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_BytesWarning  * Part of the Stable | "BytesWarning"                                     |
## | ABI.*                                              |                                                    |

| PyObject *PyExc_DeprecationWarning  * Part of the  | "DeprecationWarning"                               |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_EncodingWarning  * Part of the     | "EncodingWarning"                                  |
## | Stable ABI since version 3.10.*                    |                                                    |

| PyObject *PyExc_FutureWarning  * Part of the       | "FutureWarning"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_ImportWarning  * Part of the       | "ImportWarning"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_PendingDeprecationWarning  * Part  | "PendingDeprecationWarning"                        |
## | of the Stable ABI.*                                |                                                    |

| PyObject *PyExc_ResourceWarning  * Part of the     | "ResourceWarning"                                  |
## | Stable ABI since version 3.7.*                     |                                                    |

| PyObject *PyExc_RuntimeWarning  * Part of the      | "RuntimeWarning"                                   |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_SyntaxWarning  * Part of the       | "SyntaxWarning"                                    |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_UnicodeWarning  * Part of the      | "UnicodeWarning"                                   |
## | Stable ABI.*                                       |                                                    |

| PyObject *PyExc_UserWarning  * Part of the Stable  | "UserWarning"                                      |
## | ABI.*                                              |                                                    |

Added in version 3.2: "PyExc_ResourceWarning".

Added in version 3.10: "PyExc_EncodingWarning".

## Tracebacks

PyTypeObject PyTraceBack_Type
    * Part of the Stable ABI.*

   Type object for traceback objects. This is available as
   "types.TracebackType" in the Python layer.

int PyTraceBack_Check(PyObject *op)

   Return true if *op* is a traceback object, false otherwise. This
   function does not account for subtypes.

int PyTraceBack_Here(PyFrameObject *f)
    * Part of the Stable ABI.*

   Replace the "__traceback__" attribute on the current exception with
   a new traceback prepending *f* to the existing chain.

   Calling this function without an exception set is undefined
   behavior.

   This function returns "0" on success, and returns "-1" with an
   exception set on failure.

int PyTraceBack_Print(PyObject *tb, PyObject *f)
    * Part of the Stable ABI.*

   Write the traceback *tb* into the file *f*.

   This function returns "0" on success, and returns "-1" with an
   exception set on failure.
