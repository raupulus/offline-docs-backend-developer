---
title: Excepciones incorporadas
source_url: https://docs.python.org/es/3
source_path: library/exceptions.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2570
---

# Excepciones incorporadas

En Python, todas las excepciones deben ser instancias de una clase que
se derive de "BaseException". En una instrucción "try" con una
cláusula "except" que menciona una clase determinada, esa cláusula
también controla las clases de excepción derivadas de esa clase
(excepto las clases de excepción de las que esta se deriva). Dos
clases de excepción que no están relacionadas mediante subclases nunca
son equivalentes, incluso si tienen el mismo nombre.

Las excepciones incorporadas enumeradas en este apartado pueden ser
lanzadas por el intérprete o funciones integradas. Excepto donde se
mencione lo contrario, tienen un "valor asociado" que indica la causa
detallada del error. Esto podría una cadena de caracteres o una tupla
de varios elementos de información (por ejemplo, un código de error y
una cadena que explica el código). El valor asociado generalmente se
pasa como argumentos al constructor de la clase de excepción.

El código de usuario puede lanzar excepciones predefinidas. Esto puede
ser usado para probar un gestor de excepciones o para notificar una
condición de error "igual" a la situación en la cual el intérprete
lance la misma excepción; pero tenga en cuenta que no hay nada que
impida que el código del usuario produzca un error inapropiado.

Las clases de excepción predefinidas pueden ser usadas como subclases
para definir otras nuevas; se recomienda a los programadores que
deriven nuevas excepciones a partir de la clase "Exception" o de una
de sus subclases, y no de "BaseException". Hay disponible más
información sobre la definición de excepciones en el Tutorial de
Python en Excepciones definidas por el usuario.

## Contexto de una excepción

Tres atributos en los objetos de excepción ofrecen información sobre
el contexto en el cual la excepción fue lanzada:

BaseException.__context__
BaseException.__cause__
BaseException.__suppress_context__

   Al lanzar una nueva excepción mientras otra excepción está siendo
   manejada, el atributo "__context__" de la nueva excepción es
   automáticamente asignado a la excepción manejada.  Una excepción
   puede ser manejada cuando se utiliza la cláusula "except" o
   "finally", o con la sentencia "with".

   Este contexto de excepción implícita se puede complementar con una
   causa explícita usando "from" con "raise":

      raise new_exc from original_exc

   La expresión que sigue a "from" debe ser una excepción o "None". Se
   establecerá como "__cause__" en la excepción lanzada. La
   configuración de "__cause__" también establece implícitamente el
   atributo "__suppress_context__" a "True", de modo que el uso de
   "raise new_exc from None" reemplaza efectivamente la excepción
   anterior con la nueva para fines de visualización (por ejemplo,
   conversión de "KeyError" a "AttributeError"), dejando la excepción
   anterior disponible en "__context__" para introspección durante la
   depuración.

   La visualización por defecto de la traza de seguimiento muestra
   estas excepciones encadenadas además de la traza de la propia
   excepción. Siempre se muestra una excepción encadenada
   explícitamente en "__cause__" cuando está presente. Una excepción
   implícitamente encadenada en "__context__" solo se muestra si
   "__cause__" es "None" y "__suppress_context__" es falso.

   En cualquier caso, la excepción en sí siempre se muestra después de
   cualquier excepción encadenada para que la línea final del
   seguimiento siempre muestre la última excepción que se generó.

## Heredando de excepciones incorporadas

El código del usuario puede crear subclases que heredan de una
excepción. Se recomienda heredar solo de una clase de tipo excepción a
la vez para evitar cualquier conflicto posible en el manejo del
atributo "args" por parte de las clases base, como también por
posibles incompatibilidades en de la memoria.

La mayoría de las excepciones integradas están implementadas en C por
eficiencia, vea: Objects/exceptions.c.  Algunas tienen distribuciones
de memoria personalizadas, lo que hace imposible crear una subclase
que herede de múltiples tipos de excepciones. La distribución de
memoria de un tipo es un detalle de implementación y podría cambiar
entre versiones de Python, llevando a nuevos conflictos en el futuro.
Por lo tanto, se recomienda evitar la herencia de múltiples tipos de
excepción.

## Clases base

Las siguientes excepciones se utilizan principalmente como clases base
para otras excepciones.

exception BaseException

   La clase base para todas las excepciones predefinidas. No está
   pensada para ser heredada directamente por las clases definidas por
   el usuario (para eso, use "Exception"). Si se llama a "str()" en
   una instancia de esta clase, se retorna la representación de los
   argumentos de la instancia o la cadena vacía cuando no había
   argumentos.

   args

      La tupla de argumentos dada al constructor de excepción. Algunas
      excepciones predefinidas (como "OSError") esperan un cierto
      número de argumentos y asignan un significado especial a los
      elementos de esta tupla, mientras que otras normalmente se
      llaman solo con una sola cadena que da un mensaje de error.

   with_traceback(tb)

      Este método establece *tb* como el nuevo rastreo para la
      excepción y retorna el objeto de excepción. Se usaba con más
      frecuencia antes de que las características de encadenamiento de
      excepciones de **PEP 3134** estuvieran disponibles. El siguiente
      ejemplo muestra cómo podemos convertir una instancia de
      "SomeException" en una instancia de "OtherException" mientras se
      conserva el rastreo. Una vez lanzada, el marco actual se inserta
      en el rastreo del "OtherException", como habría sucedido con el
      rastreo del "SomeException" original si hubiéramos permitido que
      se propagara al llamador.

         try:
             ...
         except SomeException:
             tb = sys.exception().__traceback__
             raise OtherException(...).with_traceback(tb)

   __traceback__

      Un campo escribible que mantenga los objetos de seguimiento de
      pila (traceback) asociados con esta excepción. Consulte La
      declaración raise para más información.

   add_note(note)

      Agrega la cadena "note" a las notas de la excepción, las cuales
      aparecen en el rastreo después de la cadena de la excepción. Se
      lanza un "TypeError" si "note" no es una cadena de caracteres.

      Added in version 3.11.

   __notes__

      Una lista de las notas de esta excepción, las cuales fueron
      añadidas con el método "add_note()". Este atributo es creado
      cuando se llama a "add_note()".

      Added in version 3.11.

exception Exception

   Todas las excepciones predefinidas *non-system-exiting*, que no
   salen del sistema se derivan de esta clase. Todas las excepciones
   definidas por el usuario también deben derivarse de esta clase.

exception ArithmeticError

   La clase base para las excepciones predefinidas que se lanzan para
   varios errores aritméticos: "OverflowError", "ZeroDivisionError",
   "FloatingPointError".

exception BufferError

   Se lanza cuando buffer no se puede realizar una operación
   relacionada.

exception LookupError

   La clase base para las excepciones que se lanzan cuando una clave o
   índice utilizado en un mapa o secuencia que no es válido:
   "IndexError", "KeyError". Esto se puede lanzar directamente por
   "codecs.lookup()".

## Excepciones específicas

Las siguientes excepciones son las excepciones que normalmente se
lanzan.

exception AssertionError

   Se lanza cuando se produce un error en una instrucción "assert".

exception AttributeError

   Se lanza cuando se produce un error en una referencia de atributo
   (ver Referencias de atributos) o la asignación falla. (Cuando un
   objeto no admite referencias de atributos o asignaciones de
   atributos en absoluto, se lanza "TypeError".)

   The optional *name* and *obj* keyword-only arguments set the
   corresponding attributes:

   name

      The name of the attribute that was attempted to be accessed.

   obj

      The object that was accessed for the named attribute.

   Distinto en la versión 3.10: Se agregaron los atributos "name" y
   "obj".

exception EOFError

   Raised when the "input()" function hits an end-of-file condition
   (EOF) without reading any data. (Note: the "io.TextIOBase.read()"
   and "io.IOBase.readline()" methods return an empty string when they
   hit EOF.)

exception FloatingPointError

   No se usa actualmente.

exception GeneratorExit

   Se lanza cuando un *generator* o *coroutine* está cerrado; ver
   "generator.close()" y "coroutine.close()". Hereda directamente de
   "BaseException" en lugar de "Exception" ya que técnicamente no es
   un error.

exception ImportError

   Se lanza cuando la instrucción "import" tiene problemas al intentar
   cargar un módulo. También se produce cuando la *from list* en "from
   ... import" tiene un nombre que no se puede encontrar.

   Los argumentos opcionales *name* y *path* de solo palabras clave
   establecen los atributos correspondientes:

   name

      El nombre del módulo que se intentó importar.

   path

      La ruta a cualquier archivo que provocó la excepción.

   Distinto en la versión 3.3: Se han añadido los atributos "name" y
   "path".

exception ModuleNotFoundError

   Una subclase de "ImportError" que se lanza mediante "import" cuando
   no se pudo encontrar un módulo. También se lanza cuando "None" se
   encuentra en "sys.modules".

   Added in version 3.6.

exception IndexError

   Se lanza cuando un subíndice de secuencia está fuera del rango.
   (Los índices de la rebanada son truncados silenciosamente para caer
   en el intervalo permitido; si un índice no es un entero, se lanza
   "TypeError".)

exception KeyError

   Se lanza cuando no se encuentra una clave de asignación
   (diccionario) en el conjunto de claves existentes (mapa).

exception KeyboardInterrupt

   Se lanza cuando el usuario pulsa la tecla de interrupción
   (normalmente "Control"-"C" o "Delete"). Durante la ejecución, se
   realiza una comprobación de interrupciones con regularidad. La
   excepción hereda de "BaseException" para no ser detectada de forma
   accidental por "Exception" y, por lo tanto, prevenir que el
   intérprete salga.

   Nota:

     Capturar una "KeyboardInterrupt" requiere especial consideración.
     Debido a que puede ser lanzada en puntos impredecibles, puede, en
     algunas circunstancias, dejar al programa en ejecución en un
     estado inconsistente. Por lo general, es mejor permitir que
     "KeyboardInterrupt" termine el programa tan pronto como sea o
     evitar lanzarla por completo. (Vea Nota sobre Manejadores de
     Señales y Excepciones.)

exception MemoryError

   Se lanza cuando una operación se queda sin memoria pero la
   situación aún puede ser recuperada (eliminando algunos objetos). El
   valor asociado es una cadena que indica que tipo de operación
   (interna) se quedó sin memoria. Tenga en cuenta que debido a la
   arquitectura de administración de memoria (función "malloc()" de
   C), el intérprete no siempre puede recuperarse completamente de
   esta situación; sin embargo, plantea una excepción para que se
   pueda imprimir un seguimiento de la pila, en caso de que un
   programa fuera de servicio fuera lo causa.

exception NameError

   Se lanza cuando no se encuentra un nombre local o global. Esto se
   aplica solo a nombres no calificados. El valor asociado es un
   mensaje de error que incluye el nombre que no se pudo encontrar.

   The optional *name* keyword-only argument sets the attribute:

   name

      The name of the variable that was attempted to be accessed.

   Distinto en la versión 3.10: Se agregó el atributo "name".

exception NotImplementedError

   Esta excepción se deriva de "RuntimeError". En las clases base
   definidas por el usuario, los métodos abstractos deberían lanzar
   esta excepción cuando requieren clases derivadas para anular el
   método, o mientras se desarrolla la clase para indicar que la
   implementación real aún necesita ser agregada.

   Nota:

     No debe usarse para indicar que un operador o método no debe ser
     admitido en absoluto -- en ese caso, deje el operador / método
     sin definir o, si es una subclase, se establece en "None".

   Prudencia:

     "NotImplementedError" and "NotImplemented" are not
     interchangeable. This exception should only be used as described
     above; see "NotImplemented" for details on correct usage of the
     built-in constant.

exception OSError([arg])
exception OSError(errno, strerror[, filename[, winerror[, filename2]]])

   Esta excepción se produce cuando una función del sistema retorna un
   error relacionado con el sistema, que incluye fallas de E/S como
   "file not found" o "disk full" (no para tipos de argumentos
   ilegales u otros errores incidentales).

   La segunda forma del constructor establece los atributos
   correspondientes, que se describen a continuación. Los atributos
   predeterminados son "None" si no se especifican. Para
   compatibilidad con versiones anteriores, si se pasan tres
   argumentos, el atributo "args" contiene solo una tupla de 2 de los
   dos primeros argumentos del constructor.

   El constructor a menudo retorna una subclase de "OSError", como se
   describe en OS exceptions a continuación. La subclase particular
   depende del valor final "errno". Este comportamiento solo ocurre
   cuando se construye "OSError" directamente o mediante un alias, y
   no se hereda al derivar.

   errno

      Un código de error numérico de la variable C, "errno".

   winerror

      En Windows, esto le proporciona el código de error nativo de
      Windows. El atributo "errno" es entonces una traducción
      aproximada, en términos POSIX, de ese código de error nativo.

      En Windows, si el argumento del constructor "winerror" es un
      entero, el atributo "errno" se determina a partir del código de
      error de Windows y el argumento "errno" se ignora. En otras
      plataformas, el argumento "winerror" se ignora y el atributo
      "winerror" no existe.

   strerror

      The corresponding error message, as provided by the operating
      system.  It is formatted by the C functions "perror()" under
      POSIX, and "FormatMessage()" under Windows.

   filename
   filename2

      Para las excepciones que involucran una ruta del sistema de
      archivos (como "open()" o "os.unlink()"), "filename" es el
      nombre del archivo pasado a la función. Para las funciones que
      involucran dos rutas del sistema de archivos (como
      "os.rename()"), "filename2" corresponde al segundo nombre de
      archivo pasado a la función.

   Distinto en la versión 3.3: "EnvironmentError", "IOError",
   "WindowsError", "socket.error", "select.error" and "mmap.error"
   have been merged into "OSError", and the constructor may return a
   subclass.

   Distinto en la versión 3.4: El atributo "filename" es ahora el
   nombre de archivo original pasado a la función, en lugar del nombre
   codificado o decodificado desde *filesystem encoding and error
   handler*. Además, se agregaron el argumento y atributo del
   constructor *filename2*.

exception OverflowError

   Se lanza cuando el resultado de una operación aritmética es
   demasiado grande para ser representado. Esto no puede ocurrir para
   los enteros (para lo cual lanza un "MemoryError" en vez de darse
   por vencido). Sin embargo, por razones históricas, "OverflowError"
   a veces se lanza para enteros que están fuera del rango requerido.
   Debido a la falta de estandarización del manejo de excepciones de
   coma flotante en C, la mayoría de las operaciones de coma flotante
   no se verifican.

exception PythonFinalizationError

   Esta excepción es derivada de "RuntimeError". Se lanza cuando una
   operación es bloqueada durante el apagado del intérprete, también
   conocido como *finalización de Python*.

   Ejemplos de operaciones que pueden ser bloqueadas con un
   "PythonFinalizationError" durante la finalización de Python:

   * Creación de nuevos hilos de Python.

   * "Joining" a running daemon thread.

   * "os.fork()".

   Revise también la función "sys.is_finalizing()".

   Added in version 3.13: Anteriormente, se planteó un simple
   "RuntimeError".

   Distinto en la versión 3.14: "threading.Thread.join()" can now
   raise this exception.

exception RecursionError

   Esta excepción se deriva de "RuntimeError". Se lanza cuando el
   intérprete detecta que se excede la profundidad máxima de recursión
   (ver "sys.getrecursionlimit()").

   Added in version 3.5: Anteriormente, se planteó un simple
   "RuntimeError".

exception ReferenceError

   Esta excepción se produce cuando un proxy de referencia débil,
   creado por la función "weakref.proxy()", se utiliza para acceder a
   un atributo del referente después de que se ha recolectado basura.
   Para obtener más información sobre referencias débiles, consulte el
   módulo "weakref" .

exception RuntimeError

   Se lanza cuando se detecta un error que no corresponde a ninguna de
   las otras categorías. El valor asociado es una cadena que indica
   exactamente qué salió mal.

exception StopIteration

   Lanzado por la función incorporada "next()" y un *iterator*'s
   "__next__()" para indicar que no hay más elementos producidos por
   el iterador.

   value

      El objeto de excepción tiene un solo atributo "value", que se
      proporciona como argumento al construir la excepción, y por
      defecto es "None".

   Cuando se retorna una función *generator* o *coroutine*, se lanza
   una nueva instancia "StopIteration", y el valor retornado por la
   función se utiliza como parámetro "value" para constructor de la
   excepción.

   Si un generador lanza directa o indirectamente "StopIteration", se
   convierte en "RuntimeError" (conservando "StopIteration" como la
   causa de la nueva excepción).

   Distinto en la versión 3.3: Se agregó el atributo **value** y la
   capacidad de las funciones del generador de usarlo para retornar un
   valor.

   Distinto en la versión 3.5: Introdujo la transformación
   *RuntimeError* a través de "from __future__ import generator_stop",
   ver **PEP 479**.

   Distinto en la versión 3.7: Habilitar **PEP 479** para todo el
   código por defecto: a "StopIteration" lanzado en un generador se
   transforma en "RuntimeError".

exception StopAsyncIteration

   Se debe lanzar mediante el método "__anext__()" de un objeto
   *asynchronous iterator* para detener la iteración.

   Added in version 3.5.

exception SyntaxError(message, details)

   Se lanza cuando el analizador encuentra un error de sintaxis. Esto
   puede ocurrir en una instrucción "import", en una llamada a las
   funciones integradas "compile()", "exec()" o "eval()", o al leer el
   script inicial o la entrada estándar (también de forma
   interactiva).

   El "str()" de la instancia de excepción retorna solo el mensaje de
   error. Detalles es una tupla cuyos miembros también están
   disponibles como atributos separados.

   filename

      El nombre del archivo en el que se produjo el error de sintaxis.

   lineno

      En qué número de línea del archivo se produjo el error. Tiene un
      índice 1: la primera línea del archivo tiene un "lineno" de 1.

   offset

      La columna de la línea donde ocurrió el error. Está indexado a
      1: el primer carácter de la línea tiene un "offset" de 1.

   text

      El texto del código fuente involucrado en el error.

   end_lineno

      En qué número de línea del archivo termina el error. Está
      indexado a 1: la primera línea del archivo tiene un "lineno" de
      1.

   end_offset

      Finaliza la columna de la línea final donde ocurrió el error.
      Está indexado a 1: el primer carácter de la línea tiene un
      "offset" de 1.

   Para errores en los campos de cadena f, el mensaje tiene el prefijo
   "cadena f:" y las compensaciones son compensaciones en un texto
   construido a partir de la expresión de reemplazo. Por ejemplo,
   compilar f'Bad {ab} field 'da como resultado este atributo args: ('
   f-string: ... ', (' ', 1, 2,' (ab) n ', 1, 5)) .

   Distinto en la versión 3.10: Se agregaron los atributos
   "end_lineno" y "end_offset".

exception IndentationError

   Clase base para errores de sintaxis relacionados con sangría
   incorrecta. Esta es una subclase de "SyntaxError".

exception TabError

   Se lanza cuando la sangría contiene un uso inconsistente de
   pestañas y espacios. Esta es una subclase de "IndentationError".

exception SystemError

   Raised when the interpreter finds an internal error, but the
   situation does not look so serious to cause it to abandon all hope.
   The associated value is a string indicating what went wrong (in
   low-level terms). In *CPython*, this could be raised by incorrectly
   using Python's C API, such as returning a "NULL" value without an
   exception set.

   If you're confident that this exception wasn't your fault, or the
   fault of a package you're using, you should report this to the
   author or maintainer of your Python interpreter. Be sure to report
   the version of the Python interpreter ("sys.version"; it is also
   printed at the start of an interactive Python session), the exact
   error message (the exception's associated value) and if possible
   the source of the program that triggered the error.

exception SystemExit

   This exception is raised by the "sys.exit()" function.  It inherits
   from "BaseException" instead of "Exception" so that it is not
   accidentally caught by code that catches "Exception".  This allows
   the exception to properly propagate up and cause the interpreter to
   exit.  When it is not handled, the Python interpreter exits; no
   stack traceback is printed.  The constructor accepts the same
   optional argument passed to "sys.exit()". If the value is an
   integer, it specifies the system exit status (passed to C's
   "exit()" function); if it is "None", the exit status is zero; if it
   has another type (such as a string), the object's value is printed
   and the exit status is one.

   Una llamada "sys.exit()" se traduce en una excepción para que los
   gestores de limpieza ("finally" cláusulas de "try") puedan
   ejecutarse, y para que un depurador pueda ejecutar un *script* sin
   correr el riesgo de perder el control. La función "os._exit()" se
   puede usar si es absolutamente necesario salir (por ejemplo, en el
   proceso secundario después de una llamada a "os.fork()").

   code

      El estado de salida o mensaje de error que se pasa al
      constructor. (El valor predeterminado es "None".)

exception TypeError

   Se lanza cuando una operación o función se aplica a un objeto de
   tipo inapropiado. El valor asociado es una cadena que proporciona
   detalles sobre la falta de coincidencia de tipos.

   El código de usuario puede lanzar esta excepción para indicar que
   un intento de operación en un objeto no es compatible y no debe
   serlo. Si un objeto está destinado a soportar una operación dada
   pero aún no ha proporcionado una implementación,
   "NotImplementedError" es la excepción adecuada para lanzar.

   Pasar argumentos del tipo incorrecto (por ejemplo, pasar a "list"
   cuando se espera un "int") debería dar como resultado "TypeError",
   pero pasar argumentos con el valor incorrecto (por ejemplo, un
   número fuera límites esperados) debería dar como resultado
   "ValueError".

exception UnboundLocalError

   Se lanza cuando se hace referencia a una variable local en una
   función o método, pero no se ha vinculado ningún valor a esa
   variable. Esta es una subclase de "NameError".

exception UnicodeError

   Se lanza cuando se produce un error de codificación o
   decodificación relacionado con Unicode. Es una subclase de
   "ValueError".

   "UnicodeError" tiene atributos que describen el error de
   codificación o decodificación. Por ejemplo,
   "err.object[err.start:err.end]" proporciona la entrada inválida
   particular en la que falló el códec.

   encoding

      El nombre de la codificación que provocó el error.

   reason

      Una cadena que describe el error de códec específico.

   object

      El objeto que el códec intentaba codificar o decodificar.

   start

      El primer índice de datos no válidos en "object".

      This value should not be negative as it is interpreted as an
      absolute offset but this constraint is not enforced at runtime.

   end

      El índice después de los últimos datos no válidos en "object".

      This value should not be negative as it is interpreted as an
      absolute offset but this constraint is not enforced at runtime.

exception UnicodeEncodeError

   Se lanza cuando se produce un error relacionado con Unicode durante
   la codificación. Es una subclase de "UnicodeError".

exception UnicodeDecodeError

   Se lanza cuando se produce un error relacionado con Unicode durante
   la codificación. Es una subclase de "UnicodeError".

exception UnicodeTranslateError

   Se lanza cuando se produce un error relacionado con Unicode durante
   la codificación. Es una subclase de "UnicodeError".

exception ValueError

   Se lanza cuando una operación o función recibe un argumento que
   tiene el tipo correcto pero un valor inapropiado, y la situación no
   se describe con una excepción más precisa como "IndexError".

exception ZeroDivisionError

   Se lanza cuando el segundo argumento de una operación de división o
   módulo es cero. El valor asociado es una cadena que indica el tipo
   de operandos y la operación.

Las siguientes excepciones se mantienen por compatibilidad con
versiones anteriores; a partir de Python 3.3, son alias de "OSError".

exception EnvironmentError

exception IOError

exception WindowsError

   Solo disponible en Windows.

### Excepciones del sistema operativo

Las siguientes excepciones son subclases de "OSError", se lanzan según
el código de error del sistema.

exception BlockingIOError

   Se lanza cuando una operación se bloquearía en un objeto (ejemplo:
   *socket*) configurado para una operación no bloqueante. Corresponde
   a "errno" "EAGAIN", "EALREADY", "EWOULDBLOCK" y "EINPROGRESS".

   Además de los de "OSError", "BlockingIOError" puede tener un
   atributo más:

   characters_written

      An integer containing the number of **bytes** written to the
      stream before it blocked. This attribute is available when using
      the buffered I/O classes from the "io" module.

exception ChildProcessError

   Se lanza cuando falla una operación en un proceso secundario.
   Corresponde a "errno" "ECHILD".

exception ConnectionError

   Una clase base para problemas relacionados con la conexión.

   Las subclases son "BrokenPipeError", "ConnectionAbortedError",
   "ConnectionRefusedError" y "ConnectionResetError".

exception BrokenPipeError

   Una subclase de "ConnectionError", que se lanza cuando se intenta
   escribir en una tubería mientras el otro extremo se ha cerrado, o
   cuando se intenta escribir en un *socket* que se ha cerrado para
   escritura. Corresponde a "errno" "EPIPE" y "ESHUTDOWN".

exception ConnectionAbortedError

   Una subclase de "ConnectionError", que se lanza cuando el par
   aborta un intento de conexión. Corresponde a "errno"
   "ECONNABORTED".

exception ConnectionRefusedError

   Una subclase de "ConnectionError", que se lanza cuando el par
   rechaza un intento de conexión. Corresponde a "errno"
   "ECONNREFUSED".

exception ConnectionResetError

   Una subclase de "ConnectionError", que se lanza cuando el par
   restablece una conexión. Corresponde a "errno" "ECONNRESET".

exception FileExistsError

   Se lanza al intentar crear un archivo o directorio que ya existe.
   Corresponde a "errno" "EEXIST".

exception FileNotFoundError

   Se lanza cuando se solicita un archivo o directorio pero no existe.
   Corresponde a "errno" "ENOENT".

exception InterruptedError

   Se lanza cuando una señal entrante interrumpe una llamada del
   sistema. Corresponde a "errno" "EINTR".

   Distinto en la versión 3.5: Python ahora vuelve a intentar las
   llamadas del sistema cuando una señal interrumpe un *syscall*,
   excepto si el gestor de señales lanza una excepción (ver **PEP
   475** para la justificación), en lugar de lanzar
   "InterruptedError".

exception IsADirectoryError

   Se lanza cuando se solicita una operación de archivo (como
   "os.remove()") en un directorio. Corresponde a "errno" "EISDIR".

exception NotADirectoryError

   Se lanza cuando se solicita una operación de directorio (como
   "os.listdir()") en algo que no es un directorio.  En la mayoría de
   las plataformas POSIX, también se puede lanzar si una operación
   intenta abrir o recorrer un archivo que no es de directorio como si
   fuera un directorio. Corresponde a "errno" "ENOTDIR".

exception PermissionError

   Se lanza cuando se intenta ejecutar una operación sin los permisos
   de acceso adecuados, por ejemplo permisos del sistema de archivos.
   Corresponde a "errno" "EACCES", "EPERM" y "ENOTCAPABLE".

   Distinto en la versión 3.11.1: El error "ENOTCAPABLE" de WASI ahora
   se mapea a "PermissionError".

exception ProcessLookupError

   Se lanza cuando un proceso dado no existe. Corresponde a "errno"
   "ESRCH".

exception TimeoutError

   Se lanza cuando se agota el tiempo de espera de una función del
   sistema a nivel del sistema. Corresponde a "errno" "ETIMEDOUT".

Added in version 3.3: Por lo anterior se agregaron las subclases
"OSError".

Ver también:

  **PEP 3151** - Reelaborando el sistema operativo y la jerarquía de
  excepciones E/S

## Advertencias

Las siguientes excepciones se utilizan como categorías de advertencia;
consulte la documentación de Categorías de advertencia para obtener
más detalles.

exception Warning

   Clase base para categorías de advertencia.

exception UserWarning

   Clase base para advertencias generadas por código de usuario.

exception DeprecationWarning

   Clase base para advertencias sobre características obsoletas cuando
   esas advertencias están destinadas a otros desarrolladores de
   Python.

   Ignorado por los filtros de advertencia predeterminados, excepto en
   el módulo "__main__" (**PEP 565**). Habilitando Modo Desarrollo de
   Python muestra esta advertencia.

   La política de obsolescencia se describe en **PEP 387**.

exception PendingDeprecationWarning

   Clase base para advertencias sobre características que están
   obsoletas y que se espera que sean obsoletas en el futuro, pero que
   no lo son en este momento.

   Esta clase rara vez se usa para emitir una advertencia sobre una
   posible desaprobación próxima es inusual, y "DeprecationWarning" se
   prefiere para las desaprobaciones ya activas.

   Ignorado por los filtros de advertencia predeterminados.
   Habilitando Modo Desarrollo de Python muestra esta advertencia.

   La política de obsolescencia se describe en **PEP 387**.

exception SyntaxWarning

   Clase base para advertencias sobre sintaxis dudosa.

   This warning is typically emitted when compiling Python source
   code, and usually won't be reported when running already compiled
   code.

exception RuntimeWarning

   Clase base para advertencias sobre comportamiento dudoso en tiempo
   de ejecución.

exception FutureWarning

   Clase base para advertencias sobre características en desuso cuando
   esas advertencias están destinadas a usuarios finales de
   aplicaciones escritas en Python.

exception ImportWarning

   Clase base para advertencias sobre posibles errores en la
   importación de módulos.

   Ignorado por los filtros de advertencia predeterminados.
   Habilitando Modo Desarrollo de Python muestra esta advertencia.

exception UnicodeWarning

   Clase base para advertencias relacionadas con Unicode.

exception EncodingWarning

   Clase base para advertencias relacionadas con codificaciones.

   Consulte EncodingWarning opcional para obtener más detalles.

   Added in version 3.10.

exception BytesWarning

   Clase base para advertencias relacionadas con "bytes" y
   "bytearray".

exception ResourceWarning

   Clase base para advertencias relacionadas con el uso de recursos.

   Ignorado por los filtros de advertencia predeterminados.
   Habilitando Modo Desarrollo de Python muestra esta advertencia.

   Added in version 3.2.

## Grupos de excepciones

Las siguientes se utilizan cuando es necesario lanzar múltiples
excepciones no relacionadas. Forman parte de la jerarquía de
excepciones, por lo que pueden ser manejadas con "except" como todas
las demás excepciones. Además, son reconocidas por "except*", lo que
hace coincidir sus subgrupos basándose en los tipos de las excepciones
contenidas.

exception ExceptionGroup(msg, excs)

exception BaseExceptionGroup(msg, excs)

   Ambos tipos de excepción envuelven las excepciones en la secuencia
   "excs". El parámetro "msg" debe ser una cadena de caracteres. La
   diferencia entre las dos clases es que "BaseExceptionGroup"
   extiende a "BaseException" y puede envolver cualquier excepción,
   mientras que "ExceptionGroup" extiende a "Exception" y solo puede
   envolver subclases de "Exception". Este diseño está pensado para
   que "except Exception" capture un "ExceptionGroup" pero no
   "BaseExceptionGroup".

   El constructor "BaseExceptionGroup" retorna una "ExceptionGroup" en
   lugar de una "BaseExceptionGroup" si todas las excepciones
   contenidas son instancias de "Exception" , por lo que puede
   utilizarse para hacer la selección automática. El constructor
   "ExceptionGroup", por su parte, lanza un "TypeError" si alguna de
   las excepciones contenidas no es una subclase de "Exception".

   Exception groups are generic over the type of their contained
   exceptions.

   **Detalles de implementación de CPython:** The "excs" parameter may
   be any sequence, but lists and tuples are specifically processed
   more efficiently here. For optimal performance, pass a tuple as
   "excs".

   message

      El argumento "msg" para el constructor. Este atributo es de sólo
      lectura.

   exceptions

      Una tupla de la excepciones en la secuencia "excs" pasada al
      constructor. Este atributo es de sólo lectura.

   subgroup(condition)

      Retorna un grupo de excepciones que contiene sólo las
      excepciones del grupo actual que cumplen con *condition*, o
      "None" si el resultado está vacío.

      La condición puede ser un tipo de excepción o una tupla de tipos
      de excepción, en cuyo caso cada excepción se verifica para
      comprobar si coincide utilizando la misma verificación que es
      usada en una cláusula *except*. La condición también puede ser
      un invocable (distinto de un tipo objeto) que acepte una
      excepción como su único argumento, y retorne *true* para las
      excepciones que deban estar en el subgrupo.

      La estructura de anidamiento de la excepción actual se conserva
      en el resultado, así como también los valores de sus campos
      "message", "__traceback__", "__cause__", "__context__" y
      "__notes__" . Los grupos anidados vacíos son omitidos del
      resultado.

      La condición se comprueba para todas las excepciones del grupo
      de excepción anidado, incluyendo el nivel superior y cualquier
      grupo de excepción anidado. Si la condición es verdadera para
      dicho grupo de excepción, se incluye en el resultado en su
      totalidad.

      Added in version 3.13: "condition" puede ser cualquier invocable
      que no sea un objeto tipo.

   split(condition)

      Al igual que "subgroup()", pero retorna el par "(match, rest)"
      donde "match" es "subgroup(condition)" y "rest" es la parte
      restante que no coincide.

   derive(excs)

      Retorna un grupo de excepción con los mismos "message", pero que
      envuelve las excepciones en "excs".

      Este método es usado por "subgroup()" y "split()", los cuales se
      usan en varios contextos para romper un grupo de excepción. Se
      necesita una subclase que lo sobrescriba para que "subgroup()" y
      "split()" retornen instancias de la subclase en lugar de
      "ExceptionGroup".

      "subgroup()" y "split()" copian los campos "__traceback__",
      "__cause__", "__context__" y "__notes__" del grupo de excepción
      original al retornado por "derive()", por lo que estos campos no
      necesitan ser actualizados por "derive()".

         >>> class MyGroup(ExceptionGroup):
         ...     def derive(self, excs):
         ...         return MyGroup(self.message, excs)
         ...
         >>> e = MyGroup("eg", [ValueError(1), TypeError(2)])
         >>> e.add_note("a note")
         >>> e.__context__ = Exception("context")
         >>> e.__cause__ = Exception("cause")
         >>> try:
         ...    raise e
         ... except Exception as e:
         ...    exc = e
         ...
         >>> match, rest = exc.split(ValueError)
         >>> exc, exc.__context__, exc.__cause__, exc.__notes__
         (MyGroup('eg', [ValueError(1), TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
         >>> match, match.__context__, match.__cause__, match.__notes__
         (MyGroup('eg', [ValueError(1)]), Exception('context'), Exception('cause'), ['a note'])
         >>> rest, rest.__context__, rest.__cause__, rest.__notes__
         (MyGroup('eg', [TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
         >>> exc.__traceback__ is match.__traceback__ is rest.__traceback__
         True

   Note that "BaseExceptionGroup" defines "__new__()", so subclasses
   that need a different constructor signature need to override that
   rather than "__init__()". For example, the following defines an
   exception group subclass which accepts an exit_code and constructs
   the group's message from it.

      class Errors(ExceptionGroup):
         def __new__(cls, errors, exit_code):
            self = super().__new__(Errors, f"exit code: {exit_code}", errors)
            self.exit_code = exit_code
            return self

         def derive(self, excs):
            return Errors(excs, self.exit_code)

   Al igual que "ExceptionGroup", cualquier subclase de
   "BaseExceptionGroup" que también es una subclase de "Exception"
   sólo puede envolver instancias de "Exception".

   Added in version 3.11.

## Jerarquía de excepción

La jerarquía de clases para las excepciones incorporadas es:

   BaseException
    ├── BaseExceptionGroup
    ├── GeneratorExit
    ├── KeyboardInterrupt
    ├── SystemExit
    └── Exception
         ├── ArithmeticError
         │    ├── FloatingPointError
         │    ├── OverflowError
         │    └── ZeroDivisionError
         ├── AssertionError
         ├── AttributeError
         ├── BufferError
         ├── EOFError
         ├── ExceptionGroup [BaseExceptionGroup]
         ├── ImportError
         │    └── ModuleNotFoundError
         ├── LookupError
         │    ├── IndexError
         │    └── KeyError
         ├── MemoryError
         ├── NameError
         │    └── UnboundLocalError
         ├── OSError
         │    ├── BlockingIOError
         │    ├── ChildProcessError
         │    ├── ConnectionError
         │    │    ├── BrokenPipeError
         │    │    ├── ConnectionAbortedError
         │    │    ├── ConnectionRefusedError
         │    │    └── ConnectionResetError
         │    ├── FileExistsError
         │    ├── FileNotFoundError
         │    ├── InterruptedError
         │    ├── IsADirectoryError
         │    ├── NotADirectoryError
         │    ├── PermissionError
         │    ├── ProcessLookupError
         │    └── TimeoutError
         ├── ReferenceError
         ├── RuntimeError
         │    ├── NotImplementedError
         │    ├── PythonFinalizationError
         │    └── RecursionError
         ├── StopAsyncIteration
         ├── StopIteration
         ├── SyntaxError
         │    └── IndentationError
         │         └── TabError
         ├── SystemError
         ├── TypeError
         ├── ValueError
         │    └── UnicodeError
         │         ├── UnicodeDecodeError
         │         ├── UnicodeEncodeError
         │         └── UnicodeTranslateError
         └── Warning
              ├── BytesWarning
              ├── DeprecationWarning
              ├── EncodingWarning
              ├── FutureWarning
              ├── ImportWarning
              ├── PendingDeprecationWarning
              ├── ResourceWarning
              ├── RuntimeWarning
              ├── SyntaxWarning
              ├── UnicodeWarning
              └── UserWarning
