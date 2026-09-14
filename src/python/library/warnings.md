---
title: '"warnings" --- Warning control'
source_url: https://docs.python.org/es/3
source_path: library/warnings.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4480
---

# "warnings" --- Warning control

**Código fuente:** Lib/warnings.py

======================================================================

Los mensajes de advertencia suelen emitirse en situaciones en las que
es útil alertar al usuario de alguna condición en un programa, cuando
esa condición (normalmente) no justifica que se haga una excepción y
se termine el programa.  Por ejemplo, se puede emitir una advertencia
cuando un programa utiliza un módulo obsoleto.

Los programadores de Python emiten advertencias llamando a la función
"warn()" definida en este módulo.  (Los programadores de C usan
"PyErr_WarnEx()"; ver Manejo de excepciones para más detalles)

Los mensajes de advertencia se escriben normalmente en "sys.stderr",
pero su disposición puede cambiarse de manera flexible, desde ignorar
todas las advertencias hasta convertirlas en excepciones.  La
disposición de las advertencias puede variar en función de la warning
category, el texto del mensaje de advertencia y la ubicación de la
fuente donde se emite.  Las repeticiones de una advertencia particular
para la misma ubicación de la fuente son típicamente suprimidas.

El control de las advertencias consta de dos etapas: en primer lugar,
cada vez que se emite una advertencia, se determina si se debe emitir
un mensaje o no; en segundo lugar, si se debe emitir un mensaje, se le
da formato y se imprime utilizando un gancho establecido por el
usuario.

La determinación de si se debe emitir un mensaje de advertencia está
controlada por el warning filter, que es una secuencia de reglas y
acciones que coinciden. Se pueden añadir reglas al filtro llamando a
"filterwarnings()" y restablecer su estado por defecto llamando a
"resetwarnings()".

La impresión de los mensajes de advertencia se realiza llamando a
"showwarning()", que puede ser anulado; la implementación por defecto
de esta función da formato al mensaje llamando a "formatwarning()",
que también está disponible para su uso en implementaciones
personalizadas.

Ver también:

  "logging.captureWarnings()" permite manejar todas las advertencias
  con la infraestructura de registro estándar.

## Categorías de advertencia

Hay una serie de excepciones incorporadas que representan categorías
de advertencia. Esta categorización es útil para poder filtrar grupos
de advertencias.

Aunque técnicamente se trata de built-in exceptions, están
documentadas aquí, porque  pertenecen al mecanismo de advertencias.

El código de usuario puede definir categorías de advertencia
adicionales mediante la subclasificación de una de las categorías de
advertencia estándar.  Una categoría de advertencia siempre debe ser
una subclase de la clase "Warning" class.

Actualmente están definidas las siguientes clases de categorías de
advertencias:

+------------------------------------+-------------------------------------------------+
| Clase                              | Descripción                                     |
|====================================|=================================================|
| "Warning"                          | Esta es la clase principal para todas las       |
|                                    | clases que pertenecen a la categoría de         |
## |                                    | advertencia.  Es una subclase de "Exception".   |

## | "UserWarning"                      | La categoría por defecto para "warn()".         |

| "DeprecationWarning"               | Categoría principal para advertencias sobre     |
|                                    | características obsoletas cuando esas           |
|                                    | advertencias están destinadas a otros           |
|                                    | desarrolladores de Python (ignoradas por        |
|                                    | defecto, a menos que sean activadas por el      |
## |                                    | código en "__main__").                          |

| "SyntaxWarning"                    | Base category for warnings about dubious        |
|                                    | syntactic features (typically emitted when      |
|                                    | compiling Python source code, and hence may not |
## |                                    | be suppressed by runtime filters)               |

| "RuntimeWarning"                   | Categoría principal para las advertencias sobre |
## |                                    | características dudosas de tiempo de ejecución. |

| "FutureWarning"                    | Categoría principal para las advertencias sobre |
|                                    | características obsoletas cuando esas           |
|                                    | advertencias están destinadas a los usuarios    |
## |                                    | finales de aplicaciones escritas en Python.     |

| "PendingDeprecationWarning"        | Categoría principal para las advertencias sobre |
|                                    | las características que serán desaprobadas en   |
## |                                    | el futuro (ignoradas por defecto).              |

| "ImportWarning"                    | Categoría principal para las advertencias que   |
|                                    | se activan durante el proceso de importación de |
## |                                    | un módulo (se ignoran por defecto).             |

| "UnicodeWarning"                   | Categoría principal para las advertencias       |
## |                                    | relacionadas con Unicode.                       |

| "BytesWarning"                     | Categoría principal para las advertencias       |
## |                                    | relacionadas con "bytes" y "bytearray".         |

| "ResourceWarning"                  | Categoría base para las advertencias            |
|                                    | relacionadas con el uso de los recursos         |
## |                                    | (ignorada por defecto).                         |

Distinto en la versión 3.7: Anteriormente "DeprecationWarning" y
"FutureWarning" se distinguían en función de si una característica se
eliminaba por completo o se cambiaba su comportamiento. Ahora se
distinguen en función de su público objetivo y de la forma en que son
manejados por los filtros de advertencia predeterminados.

## El filtro de advertencias

El filtro de advertencias controla si las advertencias se ignoran, se
muestran o se convierten en errores (planteando una excepción).

Conceptualmente, el filtro de advertencias mantiene una lista ordenada
de especificaciones de filtros; cualquier advertencia específica se
compara con cada especificación de filtro de la lista por turno hasta
que se encuentra una coincidencia; el filtro determina la disposición
de la coincidencia.  Cada entrada es una tupla de la forma (*action*,
*message*, *category*, *module*, *lineno*), donde:

* *action* es una de las siguientes cadenas:

  +-----------------+------------------------------------------------+
  | Valor           | Disposición                                    |
  |=================|================================================|
  | ""default""     | imprime la primera ocurrencia de advertencias  |
  |                 | coincidentes para cada lugar (módulo + número  |
  |                 | de línea) donde se emite la advertencia        |
  +-----------------+------------------------------------------------+
  | ""error""       | convertir las advertencias de coincidencia en  |
  |                 | excepciones                                    |
  +-----------------+------------------------------------------------+
  | ""ignore""      | nunca imprime advertencias que coincidan       |
  +-----------------+------------------------------------------------+
  | ""always""      | siempre imprime advertencias que coinciden     |
  +-----------------+------------------------------------------------+
  | ""all""         | alias to "always"                              |
  +-----------------+------------------------------------------------+
  | ""module""      | imprime la primera ocurrencia de advertencias  |
  |                 | coincidentes para cada módulo en el que se     |
  |                 | emite la advertencia (independientemente del   |
  |                 | número de línea)                               |
  +-----------------+------------------------------------------------+
  | ""once""        | imprime sólo la primera aparición de           |
  |                 | advertencias coincidentes, independientemente  |
  |                 | de la ubicación                                |
  +-----------------+------------------------------------------------+

* *message* esa cadena de caracteres que contiene una expresión
  regular que debería coincidir con el inicio del mensaje de
  advertencia, sin discriminar mayúsculas ni minúsculas. En "-W" y
  "PYTHONWARNINGS", *message* es una cadena de caracteres literal que
  debería coincidir con el inicio del mensaje de advertencia
  discriminando mayúsculas y/o minúsculas, pero ignorando cualquier
  espacio en blanco al inicio de *message*.

* *category* es una clase (una subclase de "Warning") de la cual la
  categoría de advertencia debe ser una subclase para poder coincidir.

* *module* es un cadena de caracteres que contiene una expresión
  regular, la cual debe coincidir exactamente (con mayúsculas y
  minúsculas) al nombre completo del módulo. En "-W" y
  "PYTHONWARNINGS", *module* es string literal que debe ser igual (con
  mayúsculas y minúsculas) al nombre completo del módulo, ignorando
  cualquier espacio en blanco al inicio o final de *module*.

* *lineno* es un número entero que el número de línea donde ocurrió la
  advertencia debe coincidir, o "0" para coincidir con todos los
  números de línea.

Como la clase "Warning" se deriva de la clase "Excepción" incorporada,
para convertir una advertencia en un error simplemente lanzamos
"category(message)".

Si se informa de una advertencia y no coincide con ningún filtro
registrado, se aplica la acción "por defecto" (de ahí su nombre).

### Repeated Warning Suppression Criteria

The filters that suppress repeated warnings apply the following
criteria to determine if a warning is considered a repeat:

* ""default"": A warning is considered a repeat only if the
  (*message*, *category*, *module*, *lineno*) are all the same.

* ""module"": A warning is considered a repeat if the (*message*,
  *category*, *module*) are the same, ignoring the line number.

* ""once"": A warning is considered a repeat if the (*message*,
  *category*) are the same, ignoring the module and line number.

### Descripción de los filtros de advertencia

The warnings filter is initialized by "-W" options passed to the
Python interpreter command line and the "PYTHONWARNINGS" environment
variable. The interpreter saves the arguments for all supplied entries
without interpretation in "sys.warnoptions"; the "warnings" module
parses these when it is first imported (invalid options are ignored,
after printing a message to "sys.stderr").

Los filtros de advertencia individuales se especifican como una
secuencia de campos separados por dos puntos:

   action:message:category:module:line

El significado de cada uno de estos campos es como se describe en El
filtro de advertencias. Cuando se enumeran varios filtros en una sola
línea (como en "PYTHONWARNINGS"), los filtros individuales se separan
por comas y los filtros que se enumeran más tarde tienen prioridad
sobre los que se enumeran antes de ellos (ya que se aplican de
izquierda a derecha, y los filtros aplicados más recientemente tienen
prioridad sobre los anteriores).

Los filtros de advertencia comúnmente utilizados se aplican a todas
las advertencias, a las advertencias de una categoría particular o a
las advertencias planteadas por módulos o paquetes particulares.
Algunos ejemplos:

   default                      # Show all warnings (even those ignored by default)
   ignore                       # Ignore all warnings
   error                        # Convert all warnings to errors
   error::ResourceWarning       # Treat ResourceWarning messages as errors
   default::DeprecationWarning  # Show DeprecationWarning messages
   ignore,default:::mymodule    # Only report warnings triggered by "mymodule"
   error:::mymodule             # Convert warnings to errors in "mymodule"

### Filtro de advertencia predeterminado

Por defecto, Python instala varios filtros de advertencia, que pueden
ser anulados por la opción de línea de comandos "-W", la variable de
entorno "PYTHONWARNINGS" y llamadas a "filterwarnings()".

En versiones regulares, el filtro de advertencia por defecto tiene las
siguientes entradas (en orden de precedencia):

   default::DeprecationWarning:__main__
   ignore::DeprecationWarning
   ignore::PendingDeprecationWarning
   ignore::ImportWarning
   ignore::ResourceWarning

En una compilación de depuración, la lista de filtros de advertencia
predeterminados está vacía.

Distinto en la versión 3.2: "DeprecationWarning" es ahora ignorado por
defecto además de "PendingDeprecationWarning".

Distinto en la versión 3.7: "DeprecationWarning" se muestra de nuevo
por defecto cuando se activa directamente por código en "__main__".

Distinto en la versión 3.7: "BytesWarning" ya no aparece en la lista
de filtros por defecto y en su lugar se configura a través de
"sys.warnoptions" cuando "-b" se especifica dos veces.

### Anulando el filtro por defecto

Los desarrolladores de aplicaciones escritas en Python pueden desear
ocultar *todas* las advertencias de nivel de Python a sus usuarios por
defecto, y sólo mostrarlas cuando se realizan pruebas o se trabaja de
otra manera en la aplicación. El atributo "sys.warnoptions" utilizado
para pasar las configuraciones de los filtros al intérprete puede
utilizarse como marcador para indicar si las advertencias deben ser
desactivadas o no:

   import sys

   if not sys.warnoptions:
       import warnings
       warnings.simplefilter("ignore")

Se aconseja a los desarrolladores de pruebas de código Python que se
aseguren de que *todas* las advertencias se muestren por defecto para
el código que se está probando, usando un código como:

   import sys

   if not sys.warnoptions:
       import os, warnings
       warnings.simplefilter("default") # Change the filter in this process
       os.environ["PYTHONWARNINGS"] = "default" # Also affect subprocesses

Por último, se aconseja a los desarrolladores de shells interactivos
que ejecuten el código de usuario en un espacio de nombres distinto de
"__main__" que se aseguren de que los mensajes "DeprecationWarning" se
hagan visibles por defecto, utilizando un código como el siguiente
(donde "user_ns" es el módulo utilizado para ejecutar el código
introducido interactivamente):

   import warnings
   warnings.filterwarnings("default", category=DeprecationWarning,
                                      module=user_ns.get("__name__"))

## Eliminación temporal de las advertencias

Si está utilizando un código que sabe que va a provocar una
advertencia, como una función obsoleta, pero no quiere ver la
advertencia (incluso cuando las advertencias se han configurado
explícitamente a través de la línea de comandos), entonces es posible
suprimir la advertencia utilizando el gestor de contexto
"catch_warnings":

   import warnings

   def fxn():
       warnings.warn("deprecated", DeprecationWarning)

   with warnings.catch_warnings():
       warnings.simplefilter("ignore")
       fxn()

While within the context manager all warnings will simply be ignored.
This allows you to use known-deprecated code without having to see the
warning while not suppressing the warning for other code that might
not be aware of its use of deprecated code.

   Nota:

     See Concurrent safety of Context Managers for details on the
     concurrency-safety of the "catch_warnings" context manager when
     used in programs using multiple threads or async functions.

## Advertencias de prueba

Para probar las advertencias planteadas por el código, use el
administrador de contexto "catch_warnings". Con él puedes mutar
temporalmente el filtro de advertencias para facilitar tus pruebas.
Por ejemplo, haz lo siguiente para capturar todas las advertencias
levantadas para comprobar:

   import warnings

   def fxn():
       warnings.warn("deprecated", DeprecationWarning)

   with warnings.catch_warnings(record=True) as w:
       # Cause all warnings to always be triggered.
       warnings.simplefilter("always")
       # Trigger a warning.
       fxn()
       # Verify some things
       assert len(w) == 1
       assert issubclass(w[-1].category, DeprecationWarning)
       assert "deprecated" in str(w[-1].message)

También se puede hacer que todas las advertencias sean excepciones
usando "error" en lugar de "always". Una cosa que hay que tener en
cuenta es que si una advertencia ya se ha planteado debido a una regla
de "once" o "default", entonces no importa qué filtros estén
establecidos, la advertencia no se verá de nuevo a menos que el
registro de advertencias relacionadas con la advertencia se haya
borrado.

Once the context manager exits, the warnings filter is restored to its
state when the context was entered. This prevents tests from changing
the warnings filter in unexpected ways between tests and leading to
indeterminate test results.

   Nota:

     See Concurrent safety of Context Managers for details on the
     concurrency-safety of the "catch_warnings" context manager when
     used in programs using multiple threads or async functions.

Cuando se prueban múltiples operaciones que plantean el mismo tipo de
advertencia, es importante probarlas de manera que se confirme que
cada operación plantea una nueva advertencia (por ejemplo, establecer
advertencias que se planteen como excepciones y comprobar que las
operaciones plantean excepciones, comprobar que la longitud de la
lista de advertencias siga aumentando después de cada operación, o
bien suprimir las entradas anteriores de la lista de advertencias
antes de cada nueva operación).

## Actualización del código para las nuevas versiones de las dependencias

Las categorías de advertencia que interesan principalmente a los
desarrolladores de Python (más que a los usuarios finales de
aplicaciones escritas en Python) se ignoran por defecto.

En particular, esta lista de "ignorados por defecto" incluye
"DeprecationWarning" (para cada módulo excepto "__main__"), lo que
significa que los desarrolladores deben asegurarse de probar su código
con advertencias típicamente ignoradas hechas visibles para recibir
notificaciones oportunas de futuros cambios del API a última hora(ya
sea en la biblioteca estándar o en paquetes de terceros).

En el caso ideal, el código tendrá un conjunto de pruebas adecuado, y
el corredor de pruebas se encargará de habilitar implícitamente todas
las advertencias cuando se ejecuten las pruebas (el corredor de
pruebas proporcionado por el módulo "unittest" hace esto).

En casos menos ideales, las aplicaciones pueden ser revisadas por el
uso de interfaces desaprobadas pasando "-Wd" al intérprete de Python
(esto es la abreviatura de "-W default") o ajustando
"PYTHONWARNINGS=default" en el entorno. Esto permite el manejo por
defecto de todas las advertencias, incluyendo aquellas que son
ignoradas por defecto. Para cambiar la acción que se lleva a cabo para
las advertencias encontradas puede cambiar el argumento que se pasa a
"-W" (por ejemplo "-W error"). Consulte el indicador "-W" para obtener
más detalles sobre lo que es posible.

## Funciones disponibles

warnings.warn(message, category=None, stacklevel=1, source=None, *, skip_file_prefixes=())

   Emite una advertencia, o tal vez la ignorar o lanza una excepción.
   El argumento *category*, si se da, debe ser un warning category
   class; por defecto es "UserWarning".  Alternativamente, *message*
   puede ser una instancia "Warning", en cuyo caso *category* será
   ignorada y se usará "message.__class__". En este caso, el texto del
   mensaje será "str(message)". Esta función hace una excepción si la
   advertencia particular emitida es convertida en un error por el
   warnings filter.   El argumento *stacklevel* puede ser usado por
   funciones de envoltura escritas en Python, como esta:

      def deprecated_api(message):
          warnings.warn(message, DeprecationWarning, stacklevel=2)

   Esto hace que la advertencia se refiera al invocador de
   "deprecated_api", en lugar de a la fuente de "deprecated_api" en sí
   (ya que esta última perdería el propósito del mensaje de
   advertencia).

   El parámetro de palabra clave *skip_file_prefixes* se puede
   utilizar para indicar qué *frames* de pila se ignoran al contar los
   niveles de pila. Esto puede ser útil cuando desea que la
   advertencia aparezca siempre en los sitios de llamadas fuera de un
   paquete cuando una constante *stacklevel* no se ajusta a todas las
   rutas de llamadas o en otro caso es difícil de mantener. Si se
   proporciona, debe ser una tupla de cadenas de caracteres. Cuando se
   proporcionan prefijos, el *stacklevel* se sobreescribe
   implícitamente con "max(2, stacklevel)". Para hacer que se atribuya
   una advertencia al invocador desde afuera del paquete actual, puede
   escribir:

      # example/lower.py
      _warn_skips = (os.path.dirname(__file__),)

      def one_way(r_luxury_yacht=None, t_wobbler_mangrove=None):
          if r_luxury_yacht:
              warnings.warn("Please migrate to t_wobbler_mangrove=.",
                            skip_file_prefixes=_warn_skips)

      # example/higher.py
      from . import lower

      def another_way(**kw):
          lower.one_way(**kw)

   This makes the warning refer to both the "example.lower.one_way()"
   and "example.higher.another_way()" call sites only from calling
   code living outside of "example" package.

   *source*, si se suministra, es el objeto destruido que emitió un
   "ResourceWarning".

   Distinto en la versión 3.6: Añadido parámetro *source*.

   Distinto en la versión 3.12: Añadido *skip_file_prefixes*.

warnings.warn_explicit(message, category, filename, lineno, module=None, registry=None, module_globals=None, source=None)

   This is a low-level interface to the functionality of "warn()",
   passing in explicitly the message, category, filename and line
   number, and optionally other arguments. *message* must be a string
   and *category* a subclass of "Warning" or *message* may be a
   "Warning" instance, in which case *category* will be ignored.

   *module*, if supplied, should be the module name. If no module is
   passed, the filename with ".py" stripped is used.

   *registry*, if supplied, should be the "__warningregistry__"
   dictionary of the module. If no registry is passed, each warning is
   treated as the first occurrence, that is, filter actions
   ""default"", ""module"" and ""once"" are handled as ""always"".

   *module_globals*, si se suministra, debe ser el espacio de nombres
   global en uso por el código para el que se emite la advertencia.
   (Este argumento se utiliza para apoyar la visualización de la
   fuente de los módulos que se encuentran en los archivos zip o en
   otras fuentes de importación que no son del sistema de archivos).

   *source*, si se suministra, es el objeto destruido que emitió un
   "ResourceWarning".

   Distinto en la versión 3.6: Añade el parámetro *source*.

warnings.showwarning(message, category, filename, lineno, file=None, line=None)

   Escriba una advertencia en un archivo.  La implementación por
   defecto llama "formatwarning(message, category, filename, lineno,
   line)" y escribe la cadena resultante a *file*, que por defecto es
   "sys.stderr".  Puede reemplazar esta función con cualquier
   interlocutor asignando a "warnings.showwarning". *line* es una
   línea de código fuente que se incluirá en el mensaje de
   advertencia; si no se proporciona *line*, "showwarning()" intentará
   leer la línea especificada por *nombre de archivo* y *lineno*.

warnings.formatwarning(message, category, filename, lineno, line=None)

   Formatea una advertencia de la manera estándar.  Esto retorna una
   cadena que puede contener nuevas líneas incrustadas y termina en
   una nueva línea.  *line* es una línea de código fuente a incluir en
   el mensaje de advertencia; si *line* no se suministra,
   "formatwarning()" intentará leer la línea especificada por el
   nombre de fichero *filename* y *lineno*.

warnings.filterwarnings(action, message='', category=Warning, module='', lineno=0, append=False)

   Inserta una entrada en la lista de warnings filter specifications.
   La entrada se inserta por defecto en el frente; si *append* es
   verdadero, se inserta al final.  Esto comprueba los tipos de los
   argumentos, compila las expresiones regulares *message* y *module*,
   y las inserta como una tupla en la lista de filtros de aviso.  Las
   entradas más cercanas al principio de la lista anulan las entradas
   posteriores de la lista, si ambas coinciden con una advertencia en
   particular.  Los argumentos omitidos predeterminan un valor que
   coincide con todo.

warnings.simplefilter(action, category=Warning, lineno=0, append=False)

   Inserte una simple entrada en la lista de warnings filter
   specifications.  El significado de los parámetros de la función es
   el mismo que el de "filterwarnings()", pero no se necesitan
   expresiones regulares ya que el filtro insertado siempre coincide
   con cualquier mensaje de cualquier módulo siempre que la categoría
   y el número de línea coincidan.

warnings.resetwarnings()

   Reajusta el filtro de advertencias.  Esto descarta el efecto de
   todas las llamadas previas a "filterwarnings()", incluyendo la de
   las opciones de línea de comandos de "-W" y las llamadas a
   "simplefilter()".

@warnings.deprecated(message, /, *, category=DeprecationWarning, stacklevel=1)

   Decorator to indicate that a class, function or overload is
   deprecated.

   When this decorator is applied to an object, deprecation warnings
   may be emitted at runtime when the object is used. *static type
   checkers* will also generate a diagnostic on usage of the
   deprecated object.

   Usage:

      from warnings import deprecated
      from typing import overload

      @deprecated("Use B instead")
      class A:
          pass

      @deprecated("Use g instead")
      def f():
          pass

      @overload
      @deprecated("int support is deprecated")
      def g(x: int) -> int: ...
      @overload
      def g(x: str) -> int: ...

   The warning specified by *category* will be emitted at runtime on
   use of deprecated objects. For functions, that happens on calls;
   for classes, on instantiation and on creation of subclasses. If the
   *category* is "None", no warning is emitted at runtime. The
   *stacklevel* determines where the warning is emitted. If it is "1"
   (the default), the warning is emitted at the direct caller of the
   deprecated object; if it is higher, it is emitted further up the
   stack. Static type checker behavior is not affected by the
   *category* and *stacklevel* arguments.

   The deprecation message passed to the decorator is saved in the
   "__deprecated__" attribute on the decorated object. If applied to
   an overload, the decorator must be after the "@~typing.overload"
   decorator for the attribute to exist on the overload as returned by
   "typing.get_overloads()".

   Added in version 3.13: See **PEP 702**.

## Gestores de contexto disponibles

class warnings.catch_warnings(*, record=False, module=None, action=None, category=Warning, lineno=0, append=False)

   A context manager that copies and, upon exit, restores the warnings
   filter and the "showwarning()" function. If the *record* argument
   is "False" (the default) the context manager returns "None" on
   entry. If *record* is "True", a list is returned that is
   progressively populated with objects as seen by a custom
   "showwarning()" function (which also suppresses output to
   "sys.stderr"). Each object in the list is guaranteed to have the
   following attributes:

      * "message": the warning message (an instance of "Warning")

      * "category": the warning category (a subclass of "Warning")

      * "filename": the file name where the warning occurred ("str")

      * "lineno": the line number in the file ("int")

      * "file": the file object used for output (if any), or "None"

      * "line": the line of source code (if available), or "None"

      * "source": the original object that generated the warning (if
        available), or "None"

   Distinto en la versión 3.6: The "source" attribute was added.

   The type of these objects is not specified and may change; only the
   presence of these attributes is guaranteed.

   The *module* argument takes a module that will be used instead of
   the module returned when you import "warnings" whose filter will be
   protected. This argument exists primarily for testing the
   "warnings" module itself.

   Si el argumento *action* es diferente a "None", los demás
   argumentos serán enviados a la función "simplefilter()" como si
   fueran invocados inmediatamente al entrar al contexto.

   See El filtro de advertencias for the meaning of the *category* and
   *lineno* parameters.

   Nota:

     See Concurrent safety of Context Managers for details on the
     concurrency-safety of the "catch_warnings" context manager when
     used in programs using multiple threads or async functions.

   Distinto en la versión 3.11: Agrega los parámetros *action*,
   *category*, *lineno* y *append*.

## Concurrent safety of Context Managers

The behavior of "catch_warnings" context manager depends on the
"sys.flags.context_aware_warnings" flag.  If the flag is true, the
context manager behaves in a concurrent-safe fashion and otherwise
not. Concurrent-safe means that it is both thread-safe and safe to use
within asyncio coroutines and tasks.  Being thread-safe means that
behavior is predictable in a multi-threaded program.  The flag
defaults to true for free-threaded builds and false otherwise.

If the "context_aware_warnings" flag is false, then "catch_warnings"
will modify the global attributes of the "warnings" module.  This is
not safe if used within a concurrent program (using multiple threads
or using asyncio coroutines).  For example, if two or more threads use
the "catch_warnings" class at the same time, the behavior is
undefined.

If the flag is true, "catch_warnings" will not modify global
attributes and will instead use a "ContextVar" to store the newly
established warning filtering state.  A context variable provides
thread-local storage and it makes the use of "catch_warnings" thread-
safe.

The *record* parameter of the context handler also behaves differently
depending on the value of the flag.  When *record* is true and the
flag is false, the context manager works by replacing and then later
restoring the module's "showwarning()" function.  That is not
concurrent-safe.

When *record* is true and the flag is true, the "showwarning()"
function is not replaced.  Instead, the recording status is indicated
by an internal property in the context variable.  In this case, the
"showwarning()" function will not be restored when exiting the context
handler.

The "context_aware_warnings" flag can be set the "-X
context_aware_warnings" command-line option or by the
"PYTHON_CONTEXT_AWARE_WARNINGS" environment variable.

   Nota:

     It is likely that most programs that desire thread-safe behaviour
     of the warnings module will also want to set the
     "thread_inherit_context" flag to true.  That flag causes threads
     created by "threading.Thread" to start with a copy of the context
     variables from the thread starting it.  When true, the context
     established by "catch_warnings" in one thread will also apply to
     new threads started by it.  If false, new threads will start with
     an empty warnings context variable, meaning that any filtering
     that was established by a "catch_warnings" context manager will
     no longer be active.

Distinto en la versión 3.14: Added the
"sys.flags.context_aware_warnings" flag and the use of a context
variable for "catch_warnings" if the flag is true.  Previous versions
of Python acted as if the flag was always set to false.
