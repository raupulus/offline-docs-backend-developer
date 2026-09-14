---
title: Gestión de la memoria
source_url: https://docs.python.org/es/3
source_path: c-api/memory.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 470
---

# Gestión de la memoria

## Visión general

La gestión de memoria en Python implica un montón privado que contiene
todos los objetos de Python y estructuras de datos. El *administrador
de memoria de Python* garantiza internamente la gestión de este montón
privado. El administrador de memoria de Python tiene diferentes
componentes que se ocupan de varios aspectos de la gestión dinámica
del almacenamiento, como compartir, segmentación, asignación previa o
almacenamiento en caché.

En el nivel más bajo, un asignador de memoria sin procesar asegura que
haya suficiente espacio en el montón privado para almacenar todos los
datos relacionados con Python al interactuar con el administrador de
memoria del sistema operativo. Además del asignador de memoria sin
procesar, varios asignadores específicos de objeto operan en el mismo
montón e implementan políticas de administración de memoria distintas
adaptadas a las peculiaridades de cada tipo de objeto. Por ejemplo,
los objetos enteros se administran de manera diferente dentro del
montón que las cadenas, tuplas o diccionarios porque los enteros
implican diferentes requisitos de almacenamiento y compensaciones de
velocidad / espacio. El administrador de memoria de Python delega
parte del trabajo a los asignadores específicos de objeto, pero
asegura que este último opere dentro de los límites del montón
privado.

Es importante comprender que la gestión del montón de Python la
realiza el propio intérprete y que el usuario no tiene control sobre
él, incluso si manipulan regularmente punteros de objetos a bloques de
memoria dentro de ese montón. El administrador de memoria de Python
realiza la asignación de espacio de almacenamiento dinámico para los
objetos de Python y otros búferes internos a pedido a través de las
funciones de API de Python/C enumeradas en este documento.

Para evitar daños en la memoria, los escritores de extensiones nunca
deberían intentar operar en objetos Python con las funciones
exportadas por la biblioteca C: "malloc()", "calloc()", "realloc()" y
"free()". Esto dará como resultado llamadas mixtas entre el asignador
de C y el administrador de memoria de Python con consecuencias
fatales, ya que implementan diferentes algoritmos y operan en
diferentes montones. Sin embargo, uno puede asignar y liberar de forma
segura bloques de memoria con el asignador de la biblioteca C para
fines individuales, como se muestra en el siguiente ejemplo:

   PyObject *res;
   char *buf = (char *) malloc(BUFSIZ); /* para I/O */

   if (buf == NULL)
       return PyErr_NoMemory();
   ...Hacer algunas operaciones I/O incluyendo buf...
   res = PyBytes_FromString(buf);
   free(buf); /* malloc'ed */
   return res;

En este ejemplo, la solicitud de memoria para el búfer de E/S es
manejada por el asignador de la biblioteca C. El administrador de
memoria de Python solo participa en la asignación del objeto de bytes
retornado como resultado.

In most situations, however, it is recommended to allocate memory from
the Python heap specifically because the latter is under control of
the Python memory manager. For example, this is required when the
interpreter is extended with new object types written in C. Another
reason for using the Python heap is the desire to *inform* the Python
memory manager about the memory needs of the extension module. Even
when the requested memory is used exclusively for internal, highly
specific purposes, delegating all memory requests to the Python memory
manager causes the interpreter to have a more accurate image of its
memory footprint as a whole. Consequently, under certain
circumstances, the Python memory manager may or may not trigger
appropriate actions, like garbage collection, memory compaction or
other preventive procedures. Note that by using the C library
allocator as shown in the previous example, the allocated memory for
the I/O buffer completely escapes the Python memory manager.

Ver también:

  La variable de entorno "PYTHONMALLOC" puede usarse para configurar
  los asignadores de memoria utilizados por Python.

  La variable de entorno "PYTHONMALLOCSTATS" se puede utilizar para
  imprimir estadísticas de asignador de memoria pymalloc cada vez que
  se crea un nuevo escenario de objetos pymalloc, y en el apagado.

## Dominios del asignador

All allocating functions belong to one of three different "domains"
(see also "PyMemAllocatorDomain"). These domains represent different
allocation strategies and are optimized for different purposes. The
specific details on how every domain allocates memory or what internal
functions each domain calls is considered an implementation detail,
but for debugging purposes a simplified table can be found at
Asignadores de memoria predeterminados. The APIs used to allocate and
free a block of memory must be from the same domain. For example,
"PyMem_Free()" must be used to free memory allocated using
"PyMem_Malloc()".

Los tres dominios de asignación son:

* Raw domain: intended for allocating memory for general-purpose
  memory buffers where the allocation *must* go to the system
  allocator or where the allocator can operate without an *attached
  thread state*. The memory is requested directly from the system. See
  Raw Memory Interface.

* "Mem" domain: intended for allocating memory for Python buffers and
  general-purpose memory buffers where the allocation must be
  performed with an *attached thread state*. The memory is taken from
  the Python private heap. See Memory Interface.

* Dominio de objeto: destinado a asignar memoria perteneciente a
  objetos de Python. La memoria se toma del montículo privado de
  Python. Consulte Asignadores de objetos.

Nota:

  La compilación *free-threaded* requiere que solamente objetos de
  Python se asignen usando el dominio de "object" y que todos los
  objetos de Python se asignan usando ese dominio. Esto es diferente
  que los versiones anteriores de Python, donde esto fue una práctica
  buena y no un requisito.Por ejemplo, *buffers* (objetos que no son
  de Python) deben asignarse usando "PyMem_Malloc()",
  "PyMem_RawMalloc()", o "malloc()", pero no
  "PyObject_Malloc()".Consulte APIs de Asignación de Memoria.

## Interfaz de memoria sin procesar

The following function sets are wrappers to the system allocator.
These functions are thread-safe, so a *thread state* does not need to
be *attached*.

El asignador de memoria sin formato usa las siguientes funciones:
"malloc()", "calloc()", "realloc()" y "free()"; llame a "malloc(1)" (o
"calloc(1, 1)") cuando solicita cero bytes.

Added in version 3.4.

void *PyMem_RawMalloc(size_t n)
    * Part of the Stable ABI since version 3.13.*

   Asigna *n* bytes y retorna un puntero de tipo void* a la memoria
   asignada, o "NULL" si la solicitud falla.

   Solicitar cero bytes retorna un puntero distinto que no sea "NULL"
   si es posible, como si en su lugar se hubiera llamado a
   "PyMem_RawMalloc(1)". La memoria no se habrá inicializado de
   ninguna manera.

void *PyMem_RawCalloc(size_t nelem, size_t elsize)
    * Part of the Stable ABI since version 3.13.*

   Allocates *nelem* elements each of size *elsize* bytes and returns
   a pointer of type void* to the allocated memory, or "NULL" if the
   request fails. The memory is initialized to zeros.

   Solicitar elementos cero o elementos de tamaño cero bytes retorna
   un puntero distinto "NULL" si es posible, como si en su lugar se
   hubiera llamado "PyMem_RawCalloc(1, 1)".

   Added in version 3.5.

void *PyMem_RawRealloc(void *p, size_t n)
    * Part of the Stable ABI since version 3.13.*

   Cambia el tamaño del bloque de memoria señalado por *p* a *n*
   bytes. Los contenidos no se modificarán al mínimo de los tamaños
   antiguo y nuevo.

   Si *p* es "NULL", la llamada es equivalente a "PyMem_RawMalloc(n)";
   de lo contrario, si *n* es igual a cero, el bloque de memoria
   cambia de tamaño pero no se libera, y el puntero retornado no es
   "NULL".

   A menos que *p* sea "NULL", debe haber sido retornado por una
   llamada previa a "PyMem_RawMalloc()", "PyMem_RawRealloc()" o
   "PyMem_RawCalloc()".

   Si la solicitud falla, "PyMem_RawRealloc()" retorna "NULL" y *p*
   sigue siendo un puntero válido al área de memoria anterior.

void PyMem_RawFree(void *p)
    * Part of the Stable ABI since version 3.13.*

   Libera el bloque de memoria al que apunta *p*, que debe haber sido
   retornado por una llamada anterior a "PyMem_RawMalloc()",
   "PyMem_RawRealloc()" o "PyMem_RawCalloc()". De lo contrario, o si
   se ha llamado antes a "PyMem_RawFree(p)", se produce un
   comportamiento indefinido.

   Si *p* es "NULL", no se realiza ninguna operación.

## Interfaz de memoria

Los siguientes conjuntos de funciones, modelados según el estándar
ANSI C, pero que especifican el comportamiento cuando se solicitan
cero bytes, están disponibles para asignar y liberar memoria del
montón de Python.

In the GIL-enabled build (default build) the default memory allocator
uses the pymalloc memory allocator, whereas in the *free-threaded
build*, the default is the mimalloc memory allocator instead.

Advertencia:

  There must be an *attached thread state* when using these functions.

Distinto en la versión 3.6: El asignador predeterminado ahora es
pymalloc en lugar del "malloc()" del sistema.

Distinto en la versión 3.13: In the *free-threaded* build, the default
allocator is now mimalloc.

void *PyMem_Malloc(size_t n)
    * Part of the Stable ABI.*

   Asigna *n* bytes y retorna un puntero de tipo void* a la memoria
   asignada, o "NULL" si la solicitud falla.

   Solicitar cero bytes retorna un puntero distinto que no sea "NULL"
   si es posible, como si en su lugar se hubiera llamado a
   "PyMem_Malloc(1)". La memoria no se habrá inicializado de ninguna
   manera.

void *PyMem_Calloc(size_t nelem, size_t elsize)
    * Part of the Stable ABI since version 3.7.*

   Allocates *nelem* elements each of size *elsize* bytes and returns
   a pointer of type void* to the allocated memory, or "NULL" if the
   request fails. The memory is initialized to zeros.

   Solicitar elementos cero o elementos de tamaño cero bytes retorna
   un puntero distinto "NULL" si es posible, como si en su lugar se
   hubiera llamado "PyMem_Calloc(1, 1)".

   Added in version 3.5.

void *PyMem_Realloc(void *p, size_t n)
    * Part of the Stable ABI.*

   Cambia el tamaño del bloque de memoria señalado por *p* a *n*
   bytes. Los contenidos no se modificarán al mínimo de los tamaños
   antiguo y nuevo.

   Si *p* es "NULL", la llamada es equivalente a "PyMem_Malloc(n)"; de
   lo contrario, si *n* es igual a cero, el bloque de memoria cambia
   de tamaño pero no se libera, y el puntero retornado no es "NULL".

   A menos que *p* sea "NULL", debe haber sido retornado por una
   llamada previa a "PyMem_Malloc()", "PyMem_Realloc()" o
   "PyMem_Calloc()".

   Si la solicitud falla, "PyMem_Realloc()" retorna "NULL" y *p* sigue
   siendo un puntero válido al área de memoria anterior.

void PyMem_Free(void *p)
    * Part of the Stable ABI.*

   Libera el bloque de memoria señalado por *p*, que debe haber sido
   retornado por una llamada anterior a "PyMem_Malloc()",
   "PyMem_Realloc()" o "PyMem_Calloc()". De lo contrario, o si se ha
   llamado antes a "PyMem_Free(p)", se produce un comportamiento
   indefinido.

   Si *p* es "NULL", no se realiza ninguna operación.

Las siguientes macros orientadas a tipos se proporcionan por
conveniencia. Tenga en cuenta que *TYPE* se refiere a cualquier tipo
de C.

PyMem_New(TYPE, n)

   Igual que "PyMem_Malloc()", pero asigna "(n * sizeof(TYPE))" bytes
   de memoria. Retorna una conversión de puntero a "TYPE*". La memoria
   no se habrá inicializado de ninguna manera.

PyMem_Resize(p, TYPE, n)

   Igual que "PyMem_Realloc()", pero el bloque de memoria cambia de
   tamaño a "(n * sizeof(TYPE))" bytes. Retorna una conversión de
   puntero a "TYPE*". Al retornar, *p* será un puntero a la nueva área
   de memoria, o "NULL" en caso de falla.

   Esta es una macro de preprocesador C; *p* siempre se reasigna.
   Guarde el valor original de *p* para evitar perder memoria al
   manejar errores.

void PyMem_Del(void *p)

   La misma que "PyMem_Free()".

### Deprecated aliases

These are *soft deprecated* aliases to existing functions and macros.
They exist solely for backwards compatibility.

+----------------------------------------------------+----------------------------------------------------+
| Deprecated alias                                   | Corresponding function or macro                    |
|====================================================|====================================================|
## | PyMem_MALLOC(size)                                 | "PyMem_Malloc()"                                   |

## | PyMem_NEW(type, size)                              | "PyMem_New"                                        |

## | PyMem_REALLOC(ptr, size)                           | "PyMem_Realloc()"                                  |

## | PyMem_RESIZE(ptr, type, size)                      | "PyMem_Resize"                                     |

## | PyMem_FREE(ptr)                                    | "PyMem_Free()"                                     |

## | PyMem_DEL(ptr)                                     | "PyMem_Free()"                                     |

Distinto en la versión 3.4: The macros are now aliases of the
corresponding functions and macros. Previously, their behavior was the
same, but their use did not necessarily preserve binary compatibility
across Python versions.

Obsoleto desde la versión 2.0.

## Asignadores de objetos

Los siguientes conjuntos de funciones, modelados según el estándar
ANSI C, pero que especifican el comportamiento cuando se solicitan
cero bytes, están disponibles para asignar y liberar memoria del
montón de Python.

Nota:

  No hay garantía de que la memoria retornada por estos asignadores se
  pueda convertir con éxito en un objeto Python al interceptar las
  funciones de asignación en este dominio mediante los métodos
  descritos en la sección Personalizar Asignadores de Memoria.

The default object allocator uses the pymalloc memory allocator.  In
the *free-threaded* build, the default is the mimalloc memory
allocator instead.

Advertencia:

  There must be an *attached thread state* when using these functions.

void *PyObject_Malloc(size_t n)
    * Part of the Stable ABI.*

   Asigna *n* bytes y retorna un puntero de tipo void* a la memoria
   asignada, o "NULL" si la solicitud falla.

   Solicitar cero bytes retorna un puntero distinto que no sea "NULL"
   si es posible, como si en su lugar se hubiera llamado a
   "PyObject_Malloc(1)". La memoria no se habrá inicializado de
   ninguna manera.

void *PyObject_Calloc(size_t nelem, size_t elsize)
    * Part of the Stable ABI since version 3.7.*

   Allocates *nelem* elements each of size *elsize* bytes and returns
   a pointer of type void* to the allocated memory, or "NULL" if the
   request fails. The memory is initialized to zeros.

   Solicitar elementos cero o elementos de tamaño cero bytes retorna
   un puntero distinto "NULL" si es posible, como si en su lugar se
   hubiera llamado "PyObject_Calloc(1, 1)".

   Added in version 3.5.

void *PyObject_Realloc(void *p, size_t n)
    * Part of the Stable ABI.*

   Cambia el tamaño del bloque de memoria señalado por *p* a *n*
   bytes. Los contenidos no se modificarán al mínimo de los tamaños
   antiguo y nuevo.

   Si *p* es "NULL", la llamada es equivalente a "PyObject_Malloc(n)";
   de lo contrario, si *n* es igual a cero, el bloque de memoria
   cambia de tamaño pero no se libera, y el puntero retornado no es
   "NULL".

   A menos que *p* sea "NULL", debe haber sido retornado por una
   llamada previa a "PyObject_Malloc()", "PyObject_Realloc()" o
   "PyObject_Calloc()".

   Si la solicitud falla, "PyObject_Realloc()" retorna "NULL" y *p*
   sigue siendo un puntero válido al área de memoria anterior.

void PyObject_Free(void *p)
    * Part of the Stable ABI.*

   Libera el bloque de memoria al que apunta *p*, que debe haber sido
   retornado por una llamada anterior a "PyObject_Malloc()",
   "PyObject_Realloc()" o "PyObject_Calloc()". De lo contrario, o si
   se ha llamado antes a "PyObject_Free(p)", se produce un
   comportamiento indefinido.

   Si *p* es "NULL", no se realiza ninguna operación.

   Do not call this directly to free an object's memory; call the
   type's "tp_free" slot instead.

   Do not use this for memory allocated by "PyObject_GC_New" or
   "PyObject_GC_NewVar"; use "PyObject_GC_Del()" instead.

   Ver también:

     * "PyObject_GC_Del()" is the equivalent of this function for
       memory allocated by types that support garbage collection.

     * "PyObject_Malloc()"

     * "PyObject_Realloc()"

     * "PyObject_Calloc()"

     * "PyObject_New"

     * "PyObject_NewVar"

     * "PyType_GenericAlloc()"

     * "tp_free"

## Asignadores de memoria predeterminados

Asignadores de memoria predeterminados:

+-------------------------------------+-------------------------+----------------------+------------------------+------------------------+
| Configuración                       | Nombre                  | PyMem_RawMalloc      | PyMem_Malloc           | PyObject_Malloc        |
|=====================================|=========================|======================|========================|========================|
## | Lanzamiento de compilación          | ""pymalloc""            | "malloc"             | "malloc" + debug       | "malloc" + debug       |

## | Compilación de depuración           | ""pymalloc_debug""      | "malloc" + debug     | "pymalloc" + debug     | "pymalloc" + debug     |

| Lanzamiento de compilación, sin     | ""malloc""              | "malloc"             | "malloc"               | "malloc"               |
## | pymalloc                            |                         |                      |                        |                        |

| Compilación de depuración, sin      | ""malloc_debug""        | "malloc" + debug     | "malloc" + debug       | "malloc" + debug       |
## | pymalloc                            |                         |                      |                        |                        |

## | Free-threaded build                 | ""mimalloc""            | "mimalloc"           | "mimalloc"             | "mimalloc"             |

## | Free-threaded debug build           | ""mimalloc_debug""      | "mimalloc" + debug   | "mimalloc" + debug     | "mimalloc" + debug     |

Leyenda:

* Nombre: valor para variable de entorno "PYTHONMALLOC".

* "malloc": asignadores del sistema de la biblioteca C estándar,
  funciones C: "malloc()", "calloc()", "realloc()" y "free()".

* "pymalloc": asignador de memoria pymalloc.

* "mimalloc": mimalloc memory allocator.

* "+ debug": con enlaces de depuración en los asignadores de memoria
  de Python.

* "Debug build": Compilación de Python en modo de depuración.

## Personalizar asignadores de memoria

Added in version 3.4.

type PyMemAllocatorEx

   Estructura utilizada para describir un asignador de bloque de
   memoria. La estructura tiene cuatro campos:

   +------------------------------------------------------------+-----------------------------------------+
   | Campo                                                      | Significado                             |
   |============================================================|=========================================|
   | "void *ctx"                                                | contexto de usuario pasado como primer  |
   |                                                            | argumento                               |
   +------------------------------------------------------------+-----------------------------------------+
   | "void* malloc(void *ctx, size_t size)"                     | asignar un bloque de memoria            |
   +------------------------------------------------------------+-----------------------------------------+
   | "void* calloc(void *ctx, size_t nelem, size_t elsize)"     | asignar un bloque de memoria            |
   |                                                            | inicializado con ceros                  |
   +------------------------------------------------------------+-----------------------------------------+
   | "void* realloc(void *ctx, void *ptr, size_t new_size)"     | asignar o cambiar el tamaño de un       |
   |                                                            | bloque de memoria                       |
   +------------------------------------------------------------+-----------------------------------------+
   | "void free(void *ctx, void *ptr)"                          | liberar un bloque de memoria            |
   +------------------------------------------------------------+-----------------------------------------+

   Distinto en la versión 3.5: La estructura "PyMemAllocator" se
   renombró a "PyMemAllocatorEx" y se agregó un nuevo campo "calloc".

type PyMemAllocatorDomain

   Enum se utiliza para identificar un dominio asignador. Dominios:

   PYMEM_DOMAIN_RAW

      Funciones:

      * "PyMem_RawMalloc()"

      * "PyMem_RawRealloc()"

      * "PyMem_RawCalloc()"

      * "PyMem_RawFree()"

   PYMEM_DOMAIN_MEM

      Funciones:

      * "PyMem_Malloc()",

      * "PyMem_Realloc()"

      * "PyMem_Calloc()"

      * "PyMem_Free()"

   PYMEM_DOMAIN_OBJ

      Funciones:

      * "PyObject_Malloc()"

      * "PyObject_Realloc()"

      * "PyObject_Calloc()"

      * "PyObject_Free()"

void PyMem_GetAllocator(PyMemAllocatorDomain domain, PyMemAllocatorEx *allocator)

   Obtenga el asignador de bloque de memoria del dominio especificado.

void PyMem_SetAllocator(PyMemAllocatorDomain domain, PyMemAllocatorEx *allocator)

   Establece el asignador de bloque de memoria del dominio
   especificado.

   El nuevo asignador debe retornar un puntero distinto "NULL" al
   solicitar cero bytes.

   For the "PYMEM_DOMAIN_RAW" domain, the allocator must be thread-
   safe: a *thread state* is not *attached* when the allocator is
   called.

   For the remaining domains, the allocator must also be thread-safe:
   the allocator may be called in different interpreters that do not
   share a *GIL*.

   Si el nuevo asignador no es un enlace (no llama al asignador
   anterior), se debe llamar a la función "PyMem_SetupDebugHooks()"
   para reinstalar los enlaces de depuración en la parte superior del
   nuevo asignador.

   Vea también "PyPreConfig.allocator" y Preinicialización de Python
   con PyPreConfig.

   Advertencia:

     "PyMem_SetAllocator()" tiene el contrato siguiente:

     * It can be called after "Py_PreInitialize()" and before
       "Py_InitializeFromConfig()" to install a custom memory
       allocator. There are no restrictions over the installed
       allocator other than the ones imposed by the domain (for
       instance, the Raw Domain allows the allocator to be called
       without an *attached thread state*). See the section on
       allocator domains for more information.

     * Si se llama después de que Python haya terminado
       inicializándose (después de llamar "Py_InitializeFromConfig()")
       el asignador **debe** envolver el asignador existente.
       Substituyendo el asignador actual con otro arbitrario **no es
       compatible**.

   Distinto en la versión 3.12: Todos los asignadores deben ser seguro
   para los hilos.

void PyMem_SetupDebugHooks(void)

   Configurar enlaces de depuración en los asignadores de memoria de
   Python para detectar errores de memoria.

## Configurar enlaces para detectar errores en las funciones del asignador de memoria de Python

Cuando Python está construido en modo de depuración, la función
"PyMem_SetupDebugHooks()" se llama en Preinicialización de Python para
configurar los enlaces de depuración en Python asignadores de memoria
para detectar errores de memoria.

La variable de entorno "PYTHONMALLOC" se puede utilizar para instalar
enlaces de depuración en un Python compilado en modo de lanzamiento
(por ejemplo: "PYTHONMALLOC=debug").

La función "PyMem_SetupDebugHooks()" se puede utilizar para establecer
enlaces de depuración después de llamar a "PyMem_SetAllocator()".

Estos enlaces de depuración llenan bloques de memoria asignados
dinámicamente con patrones de bits especiales y reconocibles. La
memoria recién asignada se llena con el byte "0xCD"
("PYMEM_CLEANBYTE"), la memoria liberada se llena con el byte "0xDD"
("PYMEM_DEADBYTE"). Los bloques de memoria están rodeados por "bytes
prohibidos" rellenos con el byte "0xFD" ("PYMEM_FORBIDDENBYTE"). Es
poco probable que las cadenas de estos bytes sean direcciones válidas,
flotantes o cadenas ASCII.

Verificaciones de tiempo de ejecución:

* Detecte violaciones de API, por ejemplo: "PyObject_Free()" llamado
  en un búfer asignado por "PyMem_Malloc()".

* Detectar escritura antes del inicio del búfer (desbordamiento del
  búfer)

* Detectar escritura después del final del búfer (desbordamiento del
  búfer)

* Check that there is an *attached thread state* when allocator
  functions of "PYMEM_DOMAIN_OBJ" (ex: "PyObject_Malloc()") and
  "PYMEM_DOMAIN_MEM" (ex: "PyMem_Malloc()") domains are called.

En caso de error, los enlaces de depuración usan el módulo
"tracemalloc" para obtener el rastreo donde se asignó un bloque de
memoria. El rastreo solo se muestra si "tracemalloc" rastrea las
asignaciones de memoria de Python y se rastrea el bloque de memoria.

Sea *S* = "sizeof(size_t)". Se agregan "2*S" bytes en cada extremo de
cada bloque de *N* bytes solicitados. El diseño de la memoria es así,
donde p representa la dirección retornada por una función similar a
malloc o realloc ("p[i:j]" significa el segmento de bytes de "*(p+i)"
inclusive hasta "*(p+j)" exclusivo; tenga en cuenta que el tratamiento
de los índices negativos difiere de un segmento de Python):

"p[-2*S:-S]"
   Número de bytes solicitados originalmente. Este es un size_t, big-
   endian (más fácil de leer en un volcado de memoria).

"p[-S]"
   Identificador de API (carácter ASCII):

   * "'r'" para "PYMEM_DOMAIN_RAW".

   * "'m'" para "PYMEM_DOMAIN_MEM".

   * "'o'" para "PYMEM_DOMAIN_OBJ".

"p[-S+1:0]"
   Copias de PYMEM_FORBIDDENBYTE. Se utiliza para detectar
   suscripciones y lecturas.

"p[0:N]"
   La memoria solicitada, llena de copias de PYMEM_CLEANBYTE,
   utilizada para capturar la referencia a la memoria no inicializada.
   Cuando se llama a una función similar a realloc solicitando un
   bloque de memoria más grande, los nuevos bytes en exceso también se
   llenan con PYMEM_CLEANBYTE. Cuando se llama a una función de tipo
   free, se sobrescriben con PYMEM_DEADBYTE, para captar la referencia
   a la memoria liberada. Cuando se llama a una función similar a la
   realloc solicitando un bloque de memoria más pequeño, los bytes
   antiguos sobrantes también se llenan con PYMEM_DEADBYTE.

"p[N:N+S]"
   Copias de PYMEM_FORBIDDENBYTE. Se utiliza para detectar
   sobrescrituras y lecturas.

"p[N+S:N+2*S]"
   Solo se utiliza si la macro "PYMEM_DEBUG_SERIALNO" está definida
   (no definida por defecto).

   Un número de serie, incrementado en 1 en cada llamada a una función
   similar a malloc o realloc. Big-endian "size_t". Si se detecta
   "mala memoria" más tarde, el número de serie ofrece una excelente
   manera de establecer un punto de interrupción en la siguiente
   ejecución, para capturar el instante en el que se pasó este bloque.
   La función estática bumpserialno() en obmalloc.c es el único lugar
   donde se incrementa el número de serie, y existe para que pueda
   establecer un punto de interrupción fácilmente.

Una función de tipo realloc o de tipo free primero verifica que los
bytes PYMEM_FORBIDDENBYTE en cada extremo estén intactos. Si se han
modificado, la salida de diagnóstico se escribe en stderr y el
programa se aborta mediante Py_FatalError(). El otro modo de falla
principal es provocar un error de memoria cuando un programa lee uno
de los patrones de bits especiales e intenta usarlo como una
dirección. Si ingresa a un depurador y observa el objeto, es probable
que vea que está completamente lleno de PYMEM_DEADBYTE (lo que
significa que se está usando la memoria liberada) o PYMEM_CLEANBYTE
(que significa que se está usando la memoria no inicializada).

Distinto en la versión 3.6: The "PyMem_SetupDebugHooks()" function now
also works on Python compiled in release mode.  On error, the debug
hooks now use "tracemalloc" to get the traceback where a memory block
was allocated. The debug hooks now also check if there is an *attached
thread state* when functions of "PYMEM_DOMAIN_OBJ" and
"PYMEM_DOMAIN_MEM" domains are called.

Distinto en la versión 3.8: Los patrones de bytes "0xCB"
("PYMEM_CLEANBYTE"), "0xDB" ("PYMEM_DEADBYTE") y "0xFB"
("PYMEM_FORBIDDENBYTE") se han reemplazado por "0xCD", "0xDD" y "0xFD"
para usar los mismos valores que la depuración de Windows CRT
"malloc()" y "free()".

## El asignador pymalloc

Python tiene un asignador *pymalloc* optimizado para objetos pequeños
(más pequeños o iguales a 512 bytes) con una vida útil corta. Utiliza
asignaciones de memoria llamadas "arenas" con un tamaño fijo de 256
KiB en plataformas de 32 bits o 1 MiB en plataformas de 64 bits.
Vuelve a "PyMem_RawMalloc()" y "PyMem_RawRealloc()" para asignaciones
de más de 512 bytes.

*pymalloc* es el asignador por defecto de "PYMEM_DOMAIN_MEM" (por
ejemplo: "PyMem_Malloc()") y "PYMEM_DOMAIN_OBJ" (por ejemplo:
"PyObject_Malloc()") dominios.

El asignador de arena utiliza las siguientes funciones:

* "VirtualAlloc()" y "VirtualFree()" en Windows,

* "mmap()" y "munmap()" si está disponible,

* "malloc()" y "free()" en caso contrario.

Este asignador está deshabilitado si Python está configurado con la
opción "--without-pymalloc". También se puede deshabilitar en tiempo
de ejecución usando la variable de entorno "PYTHONMALLOC" (por
ejemplo: "PYTHONMALLOC=malloc").

Typically, it makes sense to disable the pymalloc allocator when
building Python with AddressSanitizer ("--with-address-sanitizer")
which helps uncover low level bugs within the C code.

### Personalizar asignador de arena de pymalloc

Added in version 3.4.

type PyObjectArenaAllocator

   Estructura utilizada para describir un asignador de arena. La
   estructura tiene tres campos:

   +----------------------------------------------------+-----------------------------------------+
   | Campo                                              | Significado                             |
   |====================================================|=========================================|
   | "void *ctx"                                        | contexto de usuario pasado como primer  |
   |                                                    | argumento                               |
   +----------------------------------------------------+-----------------------------------------+
   | "void* alloc(void *ctx, size_t size)"              | asignar una arena de bytes de tamaño    |
   +----------------------------------------------------+-----------------------------------------+
   | "void free(void *ctx, void *ptr, size_t size)"     | liberar la arena                        |
   +----------------------------------------------------+-----------------------------------------+

void PyObject_GetArenaAllocator(PyObjectArenaAllocator *allocator)

   Consigue el asignador de arena.

void PyObject_SetArenaAllocator(PyObjectArenaAllocator *allocator)

   Establecer el asignador de arena.

## El asignador mimalloc

Added in version 3.13.

Python supports the mimalloc allocator when the underlying platform
support is available. mimalloc is a general purpose allocator with
excellent performance characteristics, initially developed by Daan
Leijen for the runtime systems of the Koka and Lean languages.

Unlike pymalloc, which is optimized for small objects (512 bytes or
fewer), mimalloc handles allocations of any size.

In the *free-threaded* build, mimalloc is the default and **required**
allocator for the "PYMEM_DOMAIN_MEM" and "PYMEM_DOMAIN_OBJ" domains.
It cannot be disabled in free-threaded builds.  The free-threaded
build uses per-thread mimalloc heaps, which allows allocation and
deallocation to proceed without locking in most cases.

In the default (non-free-threaded) build, mimalloc is available but
not the default allocator.  It can be selected at runtime using
"PYTHONMALLOC""=mimalloc" (or "mimalloc_debug" to include debug
hooks).  It can be disabled at build time using the "--without-
mimalloc" configure option, but this option cannot be combined with "
--disable-gil".

## tracemalloc C API

Added in version 3.7.

int PyTraceMalloc_Track(unsigned int domain, uintptr_t ptr, size_t size)

   Rastree un bloque de memoria asignado en el módulo "tracemalloc".

   Retorna "0" en caso de éxito, retorna "-1" en caso de error (no se
   pudo asignar memoria para almacenar la traza). Retorna "-2" si
   tracemalloc está deshabilitado.

   Si el bloque de memoria ya está rastreado, actualice el rastreo
   existente.

int PyTraceMalloc_Untrack(unsigned int domain, uintptr_t ptr)

   Descomprima un bloque de memoria asignado en el módulo
   "tracemalloc". No haga nada si el bloque no fue rastreado.

   Retorna "-2" si tracemalloc está deshabilitado; de lo contrario,
   retorna "0".

## Ejemplos

Aquí está el ejemplo de la sección Visión general, reescrito para que
el búfer de E/S se asigne desde el montón de Python utilizando el
primer conjunto de funciones:

   PyObject *res;
   char *buf = (char *) PyMem_Malloc(BUFSIZ); /* para I/O */

   if (buf == NULL)
       return PyErr_NoMemory();
   /* ...Hacer algunas operaciones I/O incluyendo buf... */
   res = PyBytes_FromString(buf);
   PyMem_Free(buf); /* destinado con PyMem_Malloc */
   return res;

El mismo código que utiliza el conjunto de funciones orientado a
tipos:

   PyObject *res;
   char *buf = PyMem_New(char, BUFSIZ); /* for I/O */

   if (buf == NULL)
       return PyErr_NoMemory();
   /* ...Do some I/O operation involving buf... */
   res = PyBytes_FromString(buf);
   PyMem_Free(buf); /* allocated with PyMem_New */
   return res;

Tenga en cuenta que en los dos ejemplos anteriores, el búfer siempre
se manipula a través de funciones que pertenecen al mismo conjunto. De
hecho, es necesario usar la misma familia de API de memoria para un
bloque de memoria dado, de modo que el riesgo de mezclar diferentes
asignadores se reduzca al mínimo. La siguiente secuencia de código
contiene dos errores, uno de los cuales está etiquetado como *fatal*
porque mezcla dos asignadores diferentes que operan en montones
diferentes.:

   char *buf1 = PyMem_New(char, BUFSIZ);
   char *buf2 = (char *) malloc(BUFSIZ);
   char *buf3 = (char *) PyMem_Malloc(BUFSIZ);
   ...
   PyMem_Del(buf3);  /* Wrong -- should be PyMem_Free() */
   free(buf2);       /* Right -- allocated via malloc() */
   free(buf1);       /* Fatal -- should be PyMem_Free()  */

In addition to the functions aimed at handling raw memory blocks from
the Python heap, objects in Python are allocated and released with
"PyObject_New", "PyObject_NewVar" and "PyObject_Free()".

Esto se explicará en el próximo capítulo sobre cómo definir e
implementar nuevos tipos de objetos en C.
