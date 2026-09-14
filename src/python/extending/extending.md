---
title: 1. Extendiendo Python con C o C++
source_url: https://docs.python.org/es/3
source_path: extending/extending.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 990
---

# 1. Extendiendo Python con C o C++

Es muy fácil agregar nuevos módulos incorporados a Python, si sabe
cómo programar en C. Tales como *módulos de extensión* pueden hacer
dos cosas que no se pueden hacer directamente en Python: pueden
implementar nuevos tipos objetos incorporados, y pueden llamar a
funciones de biblioteca C y llamadas de sistema.

Para admitir extensiones, la API de Python (interfaz de programadores
de aplicaciones) define un conjunto de funciones, macros y variables
que proporcionan acceso a la mayoría de los aspectos del sistema de
tiempo de ejecución de Python. La API de Python se incorpora en un
archivo fuente C incluyendo el encabezado ""Python.h"".

La compilación de un módulo de extensión depende de su uso previsto,
así como de la configuración de su sistema; los detalles se dan en
capítulos posteriores.

Nota:

  La interfaz de extensión C es específica de CPython, y los módulos
  de extensión no funcionan en otras implementaciones de Python. En
  muchos casos, es posible evitar escribir extensiones C y preservar
  la portabilidad a otras implementaciones. Por ejemplo, si su caso de
  uso es llamar a funciones de biblioteca C o llamadas de sistema,
  debería considerar usar el módulo "ctypes" o la biblioteca cffi en
  lugar de escribir código personalizado C. Estos módulos le permiten
  escribir código Python para interactuar con el código C y son más
  portátiles entre las implementaciones de Python que escribir y
  compilar un módulo de extensión C.

## 1.1. Un ejemplo simple

Creemos un módulo de extensión llamado "spam" (la comida favorita de
los fanáticos de Monty Python ...) y digamos que queremos crear una
interfaz de Python para la función de biblioteca C "system()" [1] .
Esta función toma una cadena de caracteres con terminación nula como
argumento y retorna un entero. Queremos que esta función se pueda
llamar desde Python de la siguiente manera:

   >>> import spam
   >>> status = spam.system("ls -l")

Comience creando un archivo "spammodule.c". (Históricamente, si un
módulo se llama "spam", el archivo C que contiene su implementación se
llama "spammodule.c"; si el nombre del módulo es muy largo, como
"spammify", el nombre del módulo puede sea solo "spammify.c".)

Las dos primeras líneas de nuestro archivo pueden ser:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

que extrae la API de Python (puede agregar un comentario que describa
el propósito del módulo y un aviso de copyright si lo desea).

Nota:

  Dado que Python puede definir algunas definiciones de preprocesador
  que afectan los encabezados estándar en algunos sistemas, *debe*
  incluir "Python.h" antes de incluir encabezados estándar."#define
  PY_SSIZE_T_CLEAN" was used to indicate that "Py_ssize_t" should be
  used in some APIs instead of "int". It is not necessary since Python
  3.13, but we keep it here for backward compatibility. See Cadena de
  caracteres y búferes for a description of this macro.

All user-visible symbols defined by "Python.h" have a prefix of "Py"
or "PY", except those defined in standard header files.

Truco:

  For backward compatibility, "Python.h" includes several standard
  header files. C extensions should include the standard headers that
  they use, and should not rely on these implicit includes. If using
  the limited C API version 3.13 or newer, the implicit includes are:

  * "<assert.h>"

  * "<intrin.h>" (on Windows)

  * "<inttypes.h>"

  * "<limits.h>"

  * "<math.h>"

  * "<stdarg.h>"

  * "<wchar.h>"

  * "<sys/types.h>" (if present)

  If "Py_LIMITED_API" is not defined, or is set to version 3.12 or
  older, the headers below are also included:

  * "<ctype.h>"

  * "<unistd.h>" (on POSIX)

  If "Py_LIMITED_API" is not defined, or is set to version 3.10 or
  older, the headers below are also included:

  * "<errno.h>"

  * "<stdio.h>"

  * "<stdlib.h>"

  * "<string.h>"

Lo siguiente que agregamos a nuestro archivo de módulo es la función C
que se llamará cuando se evalúe la expresión Python
"spam.system(string)" (veremos en breve cómo termina siendo llamado):

   static PyObject *
   spam_system(PyObject *self, PyObject *args)
   {
       const char *command;
       int sts;

       if (!PyArg_ParseTuple(args, "s", &command))
           return NULL;
       sts = system(command);
       return PyLong_FromLong(sts);
   }

Hay una traducción directa de la lista de argumentos en Python (por
ejemplo, la única expresión ""ls -l"") a los argumentos pasados a la
función C. La función C siempre tiene dos argumentos, llamados
convencionalmente *self* y *args*.

El argumento *self* apunta al objeto del módulo para funciones a nivel
de módulo; para un método apuntaría a la instancia del objeto.

El argumento *args* será un puntero a un objeto de tupla de Python que
contiene los argumentos. Cada elemento de la tupla corresponde a un
argumento en la lista de argumentos de la llamada. Los argumentos son
objetos de Python --- para hacer algo con ellos en nuestra función C
tenemos que convertirlos a valores C. La función "PyArg_ParseTuple()"
en la API de Python verifica los tipos de argumento y los convierte a
valores C. Utiliza una cadena de plantilla para determinar los tipos
requeridos de los argumentos, así como los tipos de las variables C en
las que almacenar los valores convertidos. Más sobre esto más tarde.

"PyArg_ParseTuple()" retorna verdadero (distinto de cero) si todos los
argumentos tienen el tipo correcto y sus componentes se han almacenado
en las variables cuyas direcciones se pasan. Retorna falso (cero) si
se pasó una lista de argumentos no válidos. En el último caso, también
genera una excepción apropiada para que la función de llamada pueda
retornar "NULL" inmediatamente (como vimos en el ejemplo).

## 1.2. Intermezzo: errores y excepciones

Una convención importante en todo el intérprete de Python es la
siguiente: cuando una función falla, debe establecer una condición de
excepción y retornar un valor de error (generalmente "-1" o un puntero
"NULL"). La información de excepción se almacena en tres miembros del
estado del subproceso del intérprete. Estos son "NULL" si no hay
excepción. De lo contrario, son los equivalentes en C de los miembros
de la tupla Python retornada por "sys.exc_info()". Estos son el tipo
de excepción, la instancia de excepción y un objeto de rastreo. Es
importante conocerlos para comprender cómo se transmiten los errores.

La API de Python define una serie de funciones para establecer varios
tipos de excepciones.

El más común es "PyErr_SetString()". Sus argumentos son un objeto de
excepción y una cadena C. El objeto de excepción suele ser un objeto
predefinido como "PyExc_ZeroDivisionError". La cadena C indica la
causa del error y se convierte en un objeto de cadena Python y se
almacena como el "valor asociado" de la excepción.

Otra función útil es "PyErr_SetFromErrno()", que solo toma un
argumento de excepción y construye el valor asociado mediante la
inspección de la variable global "errno". La función más general es
"PyErr_SetObject()", que toma dos argumentos de objeto, la excepción y
su valor asociado. No necesita "Py_INCREF()" los objetos pasados a
cualquiera de estas funciones.

Puede probar de forma no destructiva si se ha establecido una
excepción con "PyErr_Occurred()". Esto retorna el objeto de excepción
actual o "NULL" si no se ha producido ninguna excepción. Normalmente
no necesita llamar a "PyErr_Occurred()" para ver si se produjo un
error en una llamada a la función, ya que debería poder distinguir el
valor de retorno.

Cuando una función *f* que llama a otra función *g* detecta que esta
última falla, *f* debería retornar un valor de error (normalmente
"NULL" o "-1"). Debería *no* llamar a una de las funciones "PyErr_*"
--- *g* ya ha llamado a una. Se supone que la persona que llama a *f*
también retornará una indicación de error a *su* persona que la llama,
nuevamente *sin* llama a "PyErr_*", y así sucesivamente --- la función
que lo detectó primero ya informó la causa más detallada del error.
Una vez que el error llega al bucle principal del intérprete de
Python, este aborta el código de Python que se está ejecutando
actualmente e intenta encontrar un controlador de excepciones
especificado por el programador de Python.

(Hay situaciones en las que un módulo puede dar un mensaje de error
más detallado llamando a otra función "PyErr_*", y en tales casos está
bien hacerlo. Sin embargo, como regla general, esto no es necesario y
puede causar que se pierda información sobre la causa del error: la
mayoría de las operaciones pueden fallar por una variedad de razones).

Para ignorar una excepción establecida por una llamada de función que
falló, la condición de excepción debe borrarse explícitamente llamando
a "PyErr_Clear()". La única vez que el código C debe llamar
"PyErr_Clear()" es si no quiere pasar el error al intérprete pero
quiere manejarlo completamente por sí mismo (posiblemente probando
algo más o pretendiendo que nada salió mal) )

Cada llamada fallida a "malloc()" debe convertirse en una excepción
--- la persona que llama directamente de "malloc()" (o "realloc()")
debe llamar "PyErr_NoMemory()" y retorna un indicador de falla en sí
mismo. Todas las funciones de creación de objetos (por ejemplo,
"PyLong_FromLong()") ya hacen esto, por lo que esta nota solo es
relevante para aquellos que llaman "malloc()" directamente.

También tenga en cuenta que, con la importante excepción de
"PyArg_ParseTuple()" y sus amigos, las funciones que retornan un
estado entero generalmente retornan un valor positivo o cero para el
éxito y "-1" para el fracaso, como las llamadas al sistema Unix.

Finalmente, tenga cuidado de limpiar la basura (haciendo
"Py_XDECREF()" o "Py_DECREF()" requiere objetos que ya ha creado)
cuando retorna un indicador de error!

The choice of which exception to raise is entirely yours.  There are
predeclared C objects corresponding to all built-in Python exceptions,
such as "PyExc_ZeroDivisionError", which you can use directly. Of
course, you should choose exceptions wisely --- don't use
"PyExc_TypeError" to mean that a file couldn't be opened (that should
probably be "PyExc_OSError"). If something's wrong with the argument
list, the "PyArg_ParseTuple()" function usually raises
"PyExc_TypeError".  If you have an argument whose value must be in a
particular range or must satisfy other conditions, "PyExc_ValueError"
is appropriate.

You can also define a new exception that is unique to your module. The
simplest way to do this is to declare a static global object variable
at the beginning of the file:

   static PyObject *SpamError = NULL;

and initialize it by calling "PyErr_NewException()" in the module's
"Py_mod_exec" function ("spam_module_exec()"):

   SpamError = PyErr_NewException("spam.error", NULL, NULL);

Since "SpamError" is a global variable, it will be overwritten every
time the module is reinitialized, when the "Py_mod_exec" function is
called.

For now, let's avoid the issue: we will block repeated initialization
by raising an "ImportError":

   static PyObject *SpamError = NULL;

   static int
   spam_module_exec(PyObject *m)
   {
       if (SpamError != NULL) {
           PyErr_SetString(PyExc_ImportError,
                           "cannot initialize spam module more than once");
           return -1;
       }
       SpamError = PyErr_NewException("spam.error", NULL, NULL);
       if (PyModule_AddObjectRef(m, "SpamError", SpamError) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot spam_module_slots[] = {
       {Py_mod_exec, spam_module_exec},
       {0, NULL}
   };

   static struct PyModuleDef spam_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "spam",
       .m_size = 0,  // non-negative
       .m_slots = spam_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_spam(void)
   {
       return PyModuleDef_Init(&spam_module);
   }

Note that the Python name for the exception object is "spam.error".
The "PyErr_NewException()" function may create a class with the base
class being "Exception" (unless another class is passed in instead of
"NULL"), described in Excepciones incorporadas.

Note also that the "SpamError" variable retains a reference to the
newly created exception class; this is intentional!  Since the
exception could be removed from the module by external code, an owned
reference to the class is needed to ensure that it will not be
discarded, causing "SpamError" to become a dangling pointer. Should it
become a dangling pointer, C code which raises the exception could
cause a core dump or other unintended side effects.

For now, the "Py_DECREF()" call to remove this reference is missing.
Even when the Python interpreter shuts down, the global "SpamError"
variable will not be garbage-collected. It will "leak". We did,
however, ensure that this will happen at most once per process.

We discuss the use of "PyMODINIT_FUNC" as a function return type later
in this sample.

The "spam.error" exception can be raised in your extension module
using a call to "PyErr_SetString()" as shown below:

   static PyObject *
   spam_system(PyObject *self, PyObject *args)
   {
       const char *command;
       int sts;

       if (!PyArg_ParseTuple(args, "s", &command))
           return NULL;
       sts = system(command);
       if (sts < 0) {
           PyErr_SetString(SpamError, "System command failed");
           return NULL;
       }
       return PyLong_FromLong(sts);
   }

## 1.3. De vuelta al ejemplo

Volviendo a nuestra función de ejemplo, ahora debería poder comprender
esta declaración:

   if (!PyArg_ParseTuple(args, "s", &command))
       return NULL;

It returns "NULL" (the error indicator for functions returning object
pointers) if an error is detected in the argument list, relying on the
exception set by "PyArg_ParseTuple()".  Otherwise the string value of
the argument has been copied to the local variable "command".  This is
a pointer assignment and you are not supposed to modify the string to
which it points (so in Standard C, the variable "command" should
properly be declared as "const char *command").

La siguiente declaración es una llamada a la función Unix "system()",
pasándole la cadena que acabamos de obtener de "PyArg_ParseTuple()":

   sts = system(command);

Our "spam.system()" function must return the value of "sts" as a
Python object.  This is done using the function "PyLong_FromLong()".

   return PyLong_FromLong(sts);

En este caso, retornará un objeto entero. (Sí, ¡incluso los enteros
son objetos en el montículo (*heap*) en Python!)

Si tiene una función C que no retorna ningún argumento útil (una
función que retorna void), la función de Python correspondiente debe
retornar "None". Necesita esta expresión para hacerlo (que se
implementa mediante la macro "Py_RETURN_NONE"):

   Py_INCREF(Py_None);
   return Py_None;

"Py_None" es el nombre C para el objeto especial de Python "None". Es
un objeto genuino de Python en lugar de un puntero "NULL", que
significa "error" en la mayoría de los contextos, como hemos visto.

## 1.4. La tabla de métodos del módulo y la función de inicialización

I promised to show how "spam_system()" is called from Python programs.
First, we need to list its name and address in a "method table":

   static PyMethodDef spam_methods[] = {
       ...
       {"system",  spam_system, METH_VARARGS,
        "Execute a shell command."},
       ...
       {NULL, NULL, 0, NULL}        /* Sentinel */
   };

Tenga en cuenta la tercera entrada ("METH_VARARGS"). Esta es una
bandera que le dice al intérprete la convención de llamada que se
utilizará para la función C. Normalmente debería ser siempre
"METH_VARARGS" o "METH_VARARGS | METH_KEYWORDS"; un valor de "0"
significa que se usa una variante obsoleta de "PyArg_ParseTuple()".

Cuando se usa solo "METH_VARARGS", la función debe esperar que los
parámetros a nivel de Python se pasen como una tupla aceptable para el
análisis mediante "PyArg_ParseTuple()"; A continuación se proporciona
más información sobre esta función.

The "METH_KEYWORDS" bit may be set in the third field if keyword
arguments should be passed to the function.  In this case, the C
function should accept a third "PyObject *" parameter which will be a
dictionary of keywords. Use "PyArg_ParseTupleAndKeywords()" to parse
the arguments to such a function.

La tabla de métodos debe ser referenciada en la estructura de
definición del módulo:

   static struct PyModuleDef spam_module = {
       ...
       .m_methods = spam_methods,
       ...
   };

This structure, in turn, must be passed to the interpreter in the
module's initialization function.  The initialization function must be
named "PyInit_name()", where *name* is the name of the module, and
should be the only non-"static" item defined in the module file:

   PyMODINIT_FUNC
   PyInit_spam(void)
   {
       return PyModuleDef_Init(&spam_module);
   }

Note that "PyMODINIT_FUNC" declares the function as "PyObject *"
return type, declares any special linkage declarations required by the
platform, and for C++ declares the function as "extern "C"".

"PyInit_spam()" is called when each interpreter imports its module
"spam" for the first time.  (See below for comments about embedding
Python.) A pointer to the module definition must be returned via
"PyModuleDef_Init()", so that the import machinery can create the
module and store it in "sys.modules".

When embedding Python, the "PyInit_spam()" function is not called
automatically unless there's an entry in the "PyImport_Inittab" table.
To add the module to the initialization table, use
"PyImport_AppendInittab()", optionally followed by an import of the
module:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   int
   main(int argc, char *argv[])
   {
       PyStatus status;
       PyConfig config;
       PyConfig_InitPythonConfig(&config);

       /* Add a built-in module, before Py_Initialize */
       if (PyImport_AppendInittab("spam", PyInit_spam) == -1) {
           fprintf(stderr, "Error: could not extend in-built modules table\n");
           exit(1);
       }

       /* Pass argv[0] to the Python interpreter */
       status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
       if (PyStatus_Exception(status)) {
           goto exception;
       }

       /* Initialize the Python interpreter.  Required.
          If this step fails, it will be a fatal error. */
       status = Py_InitializeFromConfig(&config);
       if (PyStatus_Exception(status)) {
           goto exception;
       }
       PyConfig_Clear(&config);

       /* Optionally import the module; alternatively,
          import can be deferred until the embedded script
          imports it. */
       PyObject *pmodule = PyImport_ImportModule("spam");
       if (!pmodule) {
           PyErr_Print();
           fprintf(stderr, "Error: could not import module 'spam'\n");
       }

       // ... use Python C API here ...

       return 0;

     exception:
        PyConfig_Clear(&config);
        Py_ExitStatusException(status);
   }

Nota:

  If you declare a global variable or a local static one, the module
  may experience unintended side-effects on re-initialisation, for
  example when removing entries from "sys.modules" or importing
  compiled modules into multiple interpreters within a process (or
  following a "fork()" without an intervening "exec()"). If module
  state is not yet fully isolated, authors should consider marking the
  module as having no support for subinterpreters (via
  "Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED").

A more substantial example module is included in the Python source
distribution as "Modules/xxlimited.c".  This file may be used as a
template or simply read as an example.

## 1.5. Compilación y enlazamiento

Hay dos cosas más que hacer antes de que pueda usar su nueva
extensión: compilarla y vincularla con el sistema Python. Si usa carga
dinámica, los detalles pueden depender del estilo de carga dinámica
que usa su sistema; Para obtener más información al respecto, consulte
los capítulos sobre la creación de módulos de extensión (capítulo
Construyendo extensiones C y C++) e información adicional que se
refiere solo a la construcción en Windows (capítulo Creación de
extensiones C y C++ en Windows).

Si no puede utilizar la carga dinámica, o si desea que su módulo sea
una parte permanente del intérprete de Python, tendrá que cambiar la
configuración (*setup*) y reconstruir el intérprete. Afortunadamente,
esto es muy simple en Unix: simplemente coloque su archivo
("spammodule.c" por ejemplo) en el directorio "Modules/ ` de una
distribución fuente desempaquetada, agregue una línea al archivo
:file:`Modules/Setup.local" que describe su archivo:

   spam spammodule.o

y reconstruya el intérprete ejecutando **make** en el directorio de
nivel superior. También puede ejecutar **make** en el subdirectorio
"Modules/", pero primero debe reconstruir "Makefile" ejecutando
'**make** Makefile'. (Esto es necesario cada vez que cambia el archivo
"Configuración").

Si su módulo requiere bibliotecas adicionales para vincular, también
se pueden enumerar en la línea del archivo de configuración, por
ejemplo:

   spam spammodule.o -lX11

## 1.6. Llamando funciones Python desde C

Hasta ahora nos hemos concentrado en hacer que las funciones de C
puedan llamarse desde Python. Lo contrario también es útil: llamar a
las funciones de Python desde C. Este es especialmente el caso de las
bibliotecas que admiten las llamadas funciones de "retrollamada". Si
una interfaz C utiliza retrollamadas, el Python equivalente a menudo
necesita proporcionar un mecanismo de retrollamada al programador de
Python; la implementación requerirá llamar a las funciones de
retrollamada de Python desde una retrollamada en C. Otros usos también
son imaginables.

Fortunately, the Python interpreter is easily called recursively, and
there is a standard interface to call a Python function.  (If you're
interested in how to call the Python parser with a particular string
as input, see La capa de muy alto nivel.)

Llamar a una función de Python es fácil. Primero, el programa Python
debe de alguna manera pasar el objeto de función Python. Debe
proporcionar una función (o alguna otra interfaz) para hacer esto.
Cuando se llama a esta función, guarde un puntero en el objeto de la
función Python (tenga cuidado de usar "Py_INCREF()") En una variable
global --- o donde mejor le parezca. Por ejemplo, la siguiente función
podría ser parte de una definición de módulo:

   static PyObject *my_callback = NULL;

   static PyObject *
   my_set_callback(PyObject *dummy, PyObject *args)
   {
       PyObject *result = NULL;
       PyObject *temp;

       if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
           if (!PyCallable_Check(temp)) {
               PyErr_SetString(PyExc_TypeError, "parameter must be callable");
               return NULL;
           }
           Py_XINCREF(temp);         /* Add a reference to new callback */
           Py_XDECREF(my_callback);  /* Dispose of previous callback */
           my_callback = temp;       /* Remember new callback */
           /* Boilerplate to return "None" */
           Py_INCREF(Py_None);
           result = Py_None;
       }
       return result;
   }

This function must be registered with the interpreter using the
"METH_VARARGS" flag; this is described in section La tabla de métodos
del módulo y la función de inicialización.  The "PyArg_ParseTuple()"
function and its arguments are documented in section Extracción de
parámetros en funciones de extensión.

Las macros "Py_XINCREF()" y "Py_XDECREF()" incrementan/disminuyen el
recuento de referencia de un objeto y son seguros en presencia de
punteros "NULL" (pero tenga en cuenta que *temp* no lo hará ser "NULL"
en este contexto). Más información sobre ellos en la sección Conteo de
referencias.

Más tarde, cuando es hora de llamar a la función, llama a la función C
"PyObject_CallObject()". Esta función tiene dos argumentos, ambos
punteros a objetos arbitrarios de Python: la función Python y la lista
de argumentos. La lista de argumentos siempre debe ser un objeto de
tupla, cuya longitud es el número de argumentos. Para llamar a la
función Python sin argumentos, pase "NULL" o una tupla vacía; para
llamarlo con un argumento, pasa una tupla singleton. "Py_BuildValue()"
retorna una tupla cuando su cadena de formato consta de cero o más
códigos de formato entre paréntesis. Por ejemplo:

   int arg;
   PyObject *arglist;
   PyObject *result;
   ...
   arg = 123;
   ...
   /* Time to call the callback */
   arglist = Py_BuildValue("(i)", arg);
   result = PyObject_CallObject(my_callback, arglist);
   Py_DECREF(arglist);

"PyObject_CallObject()" retorna un puntero de objeto Python: este es
el valor de retorno de la función Python. "PyObject_CallObject()" es
"recuento-referencia-neutral" con respecto a sus argumentos. En el
ejemplo, se creó una nueva tupla para servir como lista de argumentos,
a la cual se le llama "Py_DECREF()" inmediatamente después de la
llamada "PyObject_CallObject()".

El valor de retorno de "PyObject_CallObject()" es "nuevo": o bien es
un objeto nuevo o es un objeto existente cuyo recuento de referencias
se ha incrementado. Por lo tanto, a menos que desee guardarlo en una
variable global, debería de alguna manera "Py_DECREF()" el resultado,
incluso (¡especialmente!) Si no está interesado en su valor.

Sin embargo, antes de hacer esto, es importante verificar que el valor
de retorno no sea "NULL". Si es así, la función de Python terminó
generando una excepción. Si el código C que llamó
"PyObject_CallObject()" se llama desde Python, ahora debería retornar
una indicación de error a su llamador de Python, para que el
intérprete pueda imprimir un seguimiento de la pila, o el código de
Python que llama puede manejar la excepción. Si esto no es posible o
deseable, la excepción se debe eliminar llamando a "PyErr_Clear()".
Por ejemplo:

   if (result == NULL)
       return NULL; /* Pass error back */
   ...use result...
   Py_DECREF(result);

Dependiendo de la interfaz deseada para la función de retrollamada de
Python, es posible que también deba proporcionar una lista de
argumentos para "PyObject_CallObject()". En algunos casos, el programa
Python también proporciona la lista de argumentos, a través de la
misma interfaz que especificó la función de retrollamada. Luego se
puede guardar y usar de la misma manera que el objeto de función. En
otros casos, puede que tenga que construir una nueva tupla para
pasarla como lista de argumentos. La forma más sencilla de hacer esto
es llamar a "Py_BuildValue()". Por ejemplo, si desea pasar un código
de evento integral, puede usar el siguiente código:

   PyObject *arglist;
   ...
   arglist = Py_BuildValue("(l)", eventcode);
   result = PyObject_CallObject(my_callback, arglist);
   Py_DECREF(arglist);
   if (result == NULL)
       return NULL; /* Pass error back */
   /* Here maybe use the result */
   Py_DECREF(result);

¡Observe la ubicación de "Py_DECREF(arglist)" inmediatamente después
de la llamada, antes de la verificación de errores! También tenga en
cuenta que, estrictamente hablando, este código no está completo:
"Py_BuildValue()" puede quedarse sin memoria, y esto debe verificarse.

También puede llamar a una función con argumentos de palabras clave
utilizando "PyObject_Call()", que admite argumentos y argumentos de
palabras clave. Como en el ejemplo anterior, usamos "Py_BuildValue()"
para construir el diccionario.

   PyObject *dict;
   ...
   dict = Py_BuildValue("{s:i}", "name", val);
   result = PyObject_Call(my_callback, NULL, dict);
   Py_DECREF(dict);
   if (result == NULL)
       return NULL; /* Pass error back */
   /* Here maybe use the result */
   Py_DECREF(result);

## 1.7. Extracción de parámetros en funciones de extensión

La función "PyArg_ParseTuple()" se declara de la siguiente manera:

   int PyArg_ParseTuple(PyObject *arg, const char *format, ...);

El argumento *arg* debe ser un objeto de tupla que contenga una lista
de argumentos pasada de Python a una función C. El argumento *format*
debe ser una cadena de formato, cuya sintaxis se explica en Analizando
argumentos y construyendo valores en el Manual de referencia de la API
de Python/C. Los argumentos restantes deben ser direcciones de
variables cuyo tipo está determinado por la cadena de formato.

Tenga en cuenta que si bien "PyArg_ParseTuple()" verifica que los
argumentos de Python tengan los tipos requeridos, no puede verificar
la validez de las direcciones de las variables C pasadas a la llamada:
si comete errores allí, su código probablemente se bloqueará o al
menos sobrescribir bits aleatorios en la memoria. ¡Así que ten
cuidado!

Tenga en cuenta que las referencias de objetos de Python que se
proporcionan a quien llama son referencias prestadas (*borrowed*); ¡no
disminuya su recuento de referencias!

Algunas llamadas de ejemplo:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   int ok;
   int i, j;
   long k, l;
   const char *s;
   Py_ssize_t size;

   ok = PyArg_ParseTuple(args, ""); /* No arguments */
       /* Python call: f() */

   ok = PyArg_ParseTuple(args, "s", &s); /* A string */
       /* Possible Python call: f('whoops!') */

   ok = PyArg_ParseTuple(args, "lls", &k, &l, &s); /* Two longs and a string */
       /* Possible Python call: f(1, 2, 'three') */

   ok = PyArg_ParseTuple(args, "(ii)s#", &i, &j, &s, &size);
       /* A pair of ints and a string, whose size is also returned */
       /* Possible Python call: f((1, 2), 'three') */

   {
       const char *file;
       const char *mode = "r";
       int bufsize = 0;
       ok = PyArg_ParseTuple(args, "s|si", &file, &mode, &bufsize);
       /* A string, and optionally another string and an integer */
       /* Possible Python calls:
          f('spam')
          f('spam', 'w')
          f('spam', 'wb', 100000) */
   }

   {
       int left, top, right, bottom, h, v;
       ok = PyArg_ParseTuple(args, "((ii)(ii))(ii)",
                &left, &top, &right, &bottom, &h, &v);
       /* A rectangle and a point */
       /* Possible Python call:
          f(((0, 0), (400, 300)), (10, 10)) */
   }

   {
       Py_complex c;
       ok = PyArg_ParseTuple(args, "D:myfunction", &c);
       /* a complex, also providing a function name for errors */
       /* Possible Python call: myfunction(1+2j) */
   }

## 1.8. Parámetros de palabras clave para funciones de extensión

La función "PyArg_ParseTupleAndKeywords()" se declara de la siguiente
manera:

   int PyArg_ParseTupleAndKeywords(PyObject *arg, PyObject *kwdict,
                                   const char *format, char * const *kwlist, ...);

Los parámetros *arg* y *format* son idénticos a los de la función
"PyArg_ParseTuple()". El parámetro *kwdict* es el diccionario de
palabras clave recibidas como tercer parámetro del tiempo de ejecución
de Python. El parámetro *kwlist* es una lista de cadenas terminadas en
"NULL" que identifican los parámetros; los nombres se corresponden con
la información de tipo de *format* de izquierda a derecha. En caso de
éxito, "PyArg_ParseTupleAndKeywords()" retorna verdadero; de lo
contrario, retorna falso y genera una excepción apropiada.

Nota:

  ¡Las tuplas anidadas no se pueden analizar al usar argumentos de
  palabras clave! Los parámetros de palabras clave pasados que no
  están presentes en la *kwlist* provocarán que se genere "TypeError".

Aquí hay un módulo de ejemplo que usa palabras clave, basado en un
ejemplo de *Geoff Philbrick (philbrick@hks.com)*:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   static PyObject *
   keywdarg_parrot(PyObject *self, PyObject *args, PyObject *keywds)
   {
       int voltage;
       const char *state = "a stiff";
       const char *action = "voom";
       const char *type = "Norwegian Blue";

       static char *kwlist[] = {"voltage", "state", "action", "type", NULL};

       if (!PyArg_ParseTupleAndKeywords(args, keywds, "i|sss", kwlist,
                                        &voltage, &state, &action, &type))
           return NULL;

       printf("-- This parrot wouldn't %s if you put %i Volts through it.\n",
              action, voltage);
       printf("-- Lovely plumage, the %s -- It's %s!\n", type, state);

       Py_RETURN_NONE;
   }

   static PyMethodDef keywdarg_methods[] = {
       /* The cast of the function is necessary since PyCFunction values
        * only take two PyObject* parameters, and keywdarg_parrot() takes
        * three.
        */
       {"parrot", (PyCFunction)(void(*)(void))keywdarg_parrot, METH_VARARGS | METH_KEYWORDS,
        "Print a lovely skit to standard output."},
       {NULL, NULL, 0, NULL}   /* sentinel */
   };

   static struct PyModuleDef keywdarg_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "keywdarg",
       .m_size = 0,
       .m_methods = keywdarg_methods,
   };

   PyMODINIT_FUNC
   PyInit_keywdarg(void)
   {
       return PyModuleDef_Init(&keywdarg_module);
   }

## 1.9. Construyendo valores arbitrarios

Esta función es la contraparte de "PyArg_ParseTuple()". Se declara de
la siguiente manera:

   PyObject *Py_BuildValue(const char *format, ...);

Reconoce un conjunto de unidades de formato similares a las
reconocidas por "PyArg_ParseTuple()", pero los argumentos (que son de
entrada a la función, no de salida) no deben ser punteros, solo
valores. Retorna un nuevo objeto Python, adecuado para regresar de una
función C llamada desde Python.

Una diferencia con "PyArg_ParseTuple()": mientras que este último
requiere que su primer argumento sea una tupla (ya que las listas de
argumentos de Python siempre se representan como tuplas internamente),
"Py_BuildValue()" no siempre construye una tupla . Construye una tupla
solo si su cadena de formato contiene dos o más unidades de formato.
Si la cadena de formato está vacía, retorna "None"; si contiene
exactamente una unidad de formato, retorna el objeto que describa esa
unidad de formato. Para forzarlo a retornar una tupla de tamaño 0 o
uno, agregar paréntesis a la cadena de formato.

Ejemplos (a la izquierda la llamada, a la derecha el valor de Python
resultante):

   Py_BuildValue("")                        None
   Py_BuildValue("i", 123)                  123
   Py_BuildValue("iii", 123, 456, 789)      (123, 456, 789)
   Py_BuildValue("s", "hello")              'hello'
   Py_BuildValue("y", "hello")              b'hello'
   Py_BuildValue("ss", "hello", "world")    ('hello', 'world')
   Py_BuildValue("s#", "hello", 4)          'hell'
   Py_BuildValue("y#", "hello", 4)          b'hell'
   Py_BuildValue("()")                      ()
   Py_BuildValue("(i)", 123)                (123,)
   Py_BuildValue("(ii)", 123, 456)          (123, 456)
   Py_BuildValue("(i,i)", 123, 456)         (123, 456)
   Py_BuildValue("[i,i]", 123, 456)         [123, 456]
   Py_BuildValue("{s:i,s:i}",
                 "abc", 123, "def", 456)    {'abc': 123, 'def': 456}
   Py_BuildValue("((ii)(ii)) (ii)",
                 1, 2, 3, 4, 5, 6)          (((1, 2), (3, 4)), (5, 6))

## 1.10. Conteo de referencias

En lenguajes como C o C++, el programador es responsable de la
asignación dinámica y la desasignación de memoria en el montón. En C,
esto se hace usando las funciones "malloc()" y "free()". En C++, los
operadores "new" y "delete" se usan esencialmente con el mismo
significado y restringiremos la siguiente discusión al caso C.

Every block of memory allocated with "malloc()" should eventually be
returned to the pool of available memory by exactly one call to
"free()". It is important to call "free()" at the right time.  If a
block's address is forgotten but "free()" is not called for it, the
memory it occupies cannot be reused until the program terminates.
This is called a *memory leak*.  On the other hand, if a program calls
"free()" for a block and then continues to use the block, it creates a
conflict with reuse of the block through another "malloc()" call.
This is called *using freed memory*. It has the same bad consequences
as referencing uninitialized data --- core dumps, wrong results,
mysterious crashes.

Las causas comunes de pérdidas de memoria son rutas inusuales a través
del código. Por ejemplo, una función puede asignar un bloque de
memoria, hacer algunos cálculos y luego liberar el bloque nuevamente.
Ahora, un cambio en los requisitos de la función puede agregar una
prueba al cálculo que detecta una condición de error y puede regresar
prematuramente de la función. Es fácil olvidar liberar el bloque de
memoria asignado al tomar esta salida prematura, especialmente cuando
se agrega más tarde al código. Tales filtraciones, una vez
introducidas, a menudo pasan desapercibidas durante mucho tiempo: la
salida del error se toma solo en una pequeña fracción de todas las
llamadas, y la mayoría de las máquinas modernas tienen mucha memoria
virtual, por lo que la filtración solo se hace evidente en un proceso
de larga ejecución que usa la función de fugas con frecuencia. Por lo
tanto, es importante evitar que se produzcan fugas mediante una
convención o estrategia de codificación que minimice este tipo de
errores.

Dado que Python hace un uso intensivo de "malloc()" y "free()",
necesita una estrategia para evitar pérdidas de memoria, así como el
uso de memoria liberada. El método elegido se llama *recuento de
referencias*. El principio es simple: cada objeto contiene un
contador, que se incrementa cuando se almacena una referencia al
objeto en algún lugar, y que se reduce cuando se elimina una
referencia al mismo. Cuando el contador llega a cero, la última
referencia al objeto se ha eliminado y el objeto se libera.

An alternative strategy is called *automatic garbage collection*.
(Sometimes, reference counting is also referred to as a garbage
collection strategy, hence the use of "automatic" to distinguish the
two.)  The big advantage of automatic garbage collection is that the
user doesn't need to call "free()" explicitly.  (Another claimed
advantage is an improvement in speed or memory usage --- this is no
hard fact however.)  The disadvantage is that for C, there is no truly
portable automatic garbage collector, while reference counting can be
implemented portably (as long as the functions "malloc()" and "free()"
are available --- which the C Standard guarantees). Maybe some day a
sufficiently portable automatic garbage collector will be available
for C. Until then, we'll have to live with reference counts.

Si bien Python utiliza la implementación tradicional de conteo de
referencias, también ofrece un detector de ciclos que funciona para
detectar ciclos de referencia. Esto permite que las aplicaciones no se
preocupen por crear referencias circulares directas o indirectas;
Estas son las debilidades de la recolección de basura implementada
utilizando solo el conteo de referencias. Los ciclos de referencia
consisten en objetos que contienen referencias (posiblemente
indirectas) a sí mismos, de modo que cada objeto en el ciclo tiene un
recuento de referencias que no es cero. Las implementaciones típicas
de recuento de referencias no pueden recuperar la memoria que
pertenece a algún objeto en un ciclo de referencia, o referenciada a
partir de los objetos en el ciclo, a pesar de que no hay más
referencias al ciclo en sí.

El detector de ciclos es capaz de detectar ciclos basura y puede
recuperarlos. El módulo "gc" expone una forma de ejecutar el detector
(la función "collect()"), así como interfaces de configuración y la
posibilidad de desactivar el detector en tiempo de ejecución.

### 1.10.1. Conteo de referencias en Python

Hay dos macros, "Py_INCREF(x)" y "Py_DECREF(x)", que manejan el
incremento y la disminución del recuento de referencias. "Py_DECREF()"
también libera el objeto cuando el recuento llega a cero. Por
flexibilidad, no llama a "free()" directamente --- más bien, realiza
una llamada a través de un puntero de función en el objeto *type
object*. Para este propósito (y otros), cada objeto también contiene
un puntero a su objeto de tipo.

La gran pregunta ahora permanece: ¿cuándo usar "Py_INCREF(x)" y
"Py_DECREF(x)"? Primero introduzcamos algunos términos. Nadie "posee"
un objeto; sin embargo, puede *poseer una referencia* a un objeto. El
recuento de referencias de un objeto ahora se define como el número de
referencias que posee. El propietario de una referencia es responsable
de llamar a "Py_DECREF()" cuando la referencia ya no es necesaria. La
propiedad de una referencia puede ser transferida. Hay tres formas de
deshacerse de una referencia de propiedad: pasarla, almacenarla o
llamar a "Py_DECREF()". Olvidar deshacerse de una referencia de
propiedad crea una pérdida de memoria.

También es posible *tomar prestada* [2] una referencia a un objeto. El
prestatario de una referencia no debe llamar a "Py_DECREF()". El
prestatario no debe retener el objeto por más tiempo que el
propietario del cual fue prestado. El uso de una referencia prestada
después de que el propietario la haya eliminado corre el riesgo de
usar memoria liberada y debe evitarse por completo [3].

La ventaja de pedir prestado sobre tener una referencia es que no
necesita ocuparse de disponer de la referencia en todas las rutas
posibles a través del código --- en otras palabras, con una referencia
prestada no corre el riesgo de fugas cuando se toma una salida
prematura. La desventaja de pedir prestado sobre la posesión es que
hay algunas situaciones sutiles en las que, en un código aparentemente
correcto, una referencia prestada se puede usar después de que el
propietario del que se tomó prestado la haya eliminado.

Una referencia prestada se puede cambiar en una referencia de
propiedad llamando a "Py_INCREF()". Esto no afecta el estado del
propietario del cual se tomó prestada la referencia: crea una nueva
referencia de propiedad y otorga responsabilidades completas al
propietario (el nuevo propietario debe disponer de la referencia
correctamente, así como el propietario anterior).

### 1.10.2. Reglas de propiedad

Cuando una referencia de objeto se pasa dentro o fuera de una función,
es parte de la especificación de la interfaz de la función si la
propiedad se transfiere con la referencia o no.

La mayoría de las funciones que retornan una referencia a un objeto
pasan de propiedad con la referencia. En particular, todas las
funciones cuya función es crear un nuevo objeto, como
"PyLong_FromLong()" y "Py_BuildValue()", pasan la propiedad al
receptor. Incluso si el objeto no es realmente nuevo, aún recibirá la
propiedad de una nueva referencia a ese objeto. Por ejemplo,
"PyLong_FromLong()" mantiene un caché de valores populares y puede
retornar una referencia a un elemento en caché.

Muchas funciones que extraen objetos de otros objetos también
transfieren la propiedad con la referencia, por ejemplo
"PyObject_GetAttrString()". Sin embargo, la imagen es menos clara
aquí, ya que algunas rutinas comunes son excepciones:
"PyTuple_GetItem()", "PyList_GetItem()", "PyDict_GetItem()", y
"PyDict_GetItemString()" todas las referencias retornadas que tomaste
prestadas de la tupla, lista o diccionario.

La función "PyImport_AddModule()" también retorna una referencia
prestada, aunque en realidad puede crear el objeto que retorna: esto
es posible porque una referencia de propiedad del objeto se almacena
en "sys.modules".

Cuando pasa una referencia de objeto a otra función, en general, la
función toma prestada la referencia de usted --- si necesita
almacenarla, usará "Py_INCREF()" para convertirse en un propietario
independiente. Hay exactamente dos excepciones importantes a esta
regla: "PyTuple_SetItem()" y "PyList_SetItem()". Estas funciones se
hacen cargo de la propiedad del artículo que se les pasa, ¡incluso si
fallan! (Tenga en cuenta que "PyDict_SetItem()" y sus amigos no se
hacen cargo de la propiedad --- son "normales")

Cuando se llama a una función C desde Python, toma de la persona que
llama referencias a sus argumentos. Quien llama posee una referencia
al objeto, por lo que la vida útil de la referencia prestada está
garantizada hasta que la función regrese. Solo cuando dicha referencia
prestada debe almacenarse o transmitirse, debe convertirse en una
referencia propia llamando a "Py_INCREF()".

La referencia de objeto retornada desde una función C que se llama
desde Python debe ser una referencia de propiedad: la propiedad se
transfiere de la función a su llamador.

### 1.10.3. Hielo delgado

Hay algunas situaciones en las que el uso aparentemente inofensivo de
una referencia prestada puede generar problemas. Todo esto tiene que
ver con invocaciones implícitas del intérprete, lo que puede hacer que
el propietario de una referencia se deshaga de él.

El primer y más importante caso que debe conocer es el uso de
"Py_DECREF()" en un objeto no relacionado mientras toma prestada una
referencia a un elemento de la lista. Por ejemplo:

   void
   bug(PyObject *list)
   {
       PyObject *item = PyList_GetItem(list, 0);

       PyList_SetItem(list, 1, PyLong_FromLong(0L));
       PyObject_Print(item, stdout, 0); /* BUG! */
   }

Esta función primero toma prestada una referencia a "list[0]", luego
reemplaza "list[1]" con el valor "0", y finalmente imprime la
referencia prestada. Parece inofensivo, ¿verdad? ¡Pero no lo es!

Let's follow the control flow into "PyList_SetItem()".  The list owns
references to all its items, so when item 1 is replaced, it has to
dispose of the original item 1.  Now let's suppose the original item 1
was an instance of a user-defined class, and let's further suppose
that the class defined a "__del__()" method.  If this class instance
has a reference count of 1, disposing of it will call its "__del__()"
method. Internally, "PyList_SetItem()" calls "Py_DECREF()" on the
replaced item, which invokes replaced item's corresponding
"tp_dealloc" function. During deallocation, "tp_dealloc" calls
"tp_finalize", which is mapped to the "__del__()" method for class
instances (see **PEP 442**). This entire sequence happens
synchronously within the "PyList_SetItem()" call.

Since it is written in Python, the "__del__()" method can execute
arbitrary Python code.  Could it perhaps do something to invalidate
the reference to "item" in "bug()"?  You bet!  Assuming that the list
passed into "bug()" is accessible to the "__del__()" method, it could
execute a statement to the effect of "del list[0]", and assuming this
was the last reference to that object, it would free the memory
associated with it, thereby invalidating "item".

La solución, una vez que conoce el origen del problema, es fácil:
incremente temporalmente el recuento de referencia. La versión
correcta de la función dice:

   void
   no_bug(PyObject *list)
   {
       PyObject *item = PyList_GetItem(list, 0);

       Py_INCREF(item);
       PyList_SetItem(list, 1, PyLong_FromLong(0L));
       PyObject_Print(item, stdout, 0);
       Py_DECREF(item);
   }

This is a true story.  An older version of Python contained variants
of this bug and someone spent a considerable amount of time in a C
debugger to figure out why his "__del__()" methods would fail...

The second case of problems with a borrowed reference is a variant
involving threads.  Normally, multiple threads in the Python
interpreter can't get in each other's way, because there is a *global
lock* protecting Python's entire object space. However, it is possible
to temporarily release this lock using the macro
"Py_BEGIN_ALLOW_THREADS", and to re-acquire it using
"Py_END_ALLOW_THREADS".  This is common around blocking I/O calls, to
let other threads use the processor while waiting for the I/O to
complete. Obviously, the following function has the same problem as
the previous one:

   void
   bug(PyObject *list)
   {
       PyObject *item = PyList_GetItem(list, 0);
       Py_BEGIN_ALLOW_THREADS
       ...some blocking I/O call...
       Py_END_ALLOW_THREADS
       PyObject_Print(item, stdout, 0); /* BUG! */
   }

### 1.10.4. Punteros NULL

En general, las funciones que toman referencias de objetos como
argumentos no esperan que les pase los punteros "NULL", y volcará el
núcleo (o causará volcados de núcleo posteriores) si lo hace. Las
funciones que retornan referencias a objetos generalmente retornan
"NULL" solo para indicar que ocurrió una excepción. La razón para no
probar los argumentos "NULL" es que las funciones a menudo pasan los
objetos que reciben a otra función --- si cada función probara "NULL",
habría muchas pruebas redundantes y el código correría más lentamente.

Es mejor probar "NULL" solo en "source:" cuando se recibe un puntero
que puede ser "NULL", por ejemplo, de "malloc()" o de una función que
puede plantear una excepción.

Las macros "Py_INCREF()" y "Py_DECREF()" no comprueban los punteros
"NULL" --- sin embargo, sus variantes "Py_XINCREF()" y "Py_XDECREF()"
lo hacen.

Las macros para verificar un tipo de objeto en particular
("Pytype_Check()") no verifican los punteros "NULL" --- nuevamente,
hay mucho código que llama a varios de estos en una fila para probar
un objeto contra varios tipos esperados diferentes, y esto generaría
pruebas redundantes. No hay variantes con comprobación "NULL".

El mecanismo de llamada a la función C garantiza que la lista de
argumentos pasada a las funciones C ("args" en los ejemplos) nunca sea
"NULL" --- de hecho, garantiza que siempre sea una tupla [4].

Es un error grave dejar que un puntero "NULL" "escape" al usuario de
Python.

## 1.11. Escribiendo extensiones en C++

Es posible escribir módulos de extensión en C++. Se aplican algunas
restricciones. Si el compilador de C compila y vincula el programa
principal (el intérprete de Python), no se pueden usar objetos
globales o estáticos con constructores. Esto no es un problema si el
programa principal está vinculado por el compilador de C++. Las
funciones que serán llamadas por el intérprete de Python (en
particular, las funciones de inicialización del módulo) deben
declararse usando "extern "C"". No es necesario encerrar los archivos
de encabezado de Python en "extern "C" {...}" --- ya usan este
formulario si el símbolo "__cplusplus" está definido (todos los
compiladores recientes de C++ definen este símbolo) .

## 1.12. Proporcionar una API C para un módulo de extensión

Muchos módulos de extensión solo proporcionan nuevas funciones y tipos
para ser utilizados desde Python, pero a veces el código en un módulo
de extensión puede ser útil para otros módulos de extensión. Por
ejemplo, un módulo de extensión podría implementar un tipo de
"colección" que funciona como listas sin orden. Al igual que el tipo
de lista Python estándar tiene una API C que permite a los módulos de
extensión crear y manipular listas, este nuevo tipo de colección debe
tener un conjunto de funciones C para la manipulación directa desde
otros módulos de extensión.

A primera vista, esto parece fácil: simplemente escriba las funciones
(sin declararlas "static", por supuesto), proporcione un archivo de
encabezado apropiado y documente la API de C. Y, de hecho, esto
funcionaría si todos los módulos de extensión siempre estuvieran
vinculados estáticamente con el intérprete de Python. Sin embargo,
cuando los módulos se usan como bibliotecas compartidas, los símbolos
definidos en un módulo pueden no ser visibles para otro módulo. Los
detalles de visibilidad dependen del sistema operativo; algunos
sistemas usan un espacio de nombres global para el intérprete de
Python y todos los módulos de extensión (Windows, por ejemplo),
mientras que otros requieren una lista explícita de símbolos
importados en el momento del enlace del módulo (AIX es un ejemplo) u
ofrecen una variedad de estrategias diferentes (la mayoría Unices). E
incluso si los símbolos son visibles a nivel mundial, ¡el módulo cuyas
funciones uno desea llamar podría no haberse cargado todavía!

Por lo tanto, la portabilidad requiere no hacer suposiciones sobre la
visibilidad del símbolo. Esto significa que todos los símbolos en los
módulos de extensión deben declararse "static", excepto la función de
inicialización del módulo, para evitar conflictos de nombres con otros
módulos de extensión (como se discutió en la sección La tabla de
métodos del módulo y la función de inicialización). Y significa que
los símbolos que *deberían* ser accesibles desde otros módulos de
extensión deben exportarse de una manera diferente.

Python proporciona un mecanismo especial para pasar información de
nivel C (punteros) de un módulo de extensión a otro: cápsulas. Una
cápsula es un tipo de datos de Python que almacena un puntero (void*).
Solo se puede crear y acceder a las cápsulas a través de su API C,
pero se pueden pasar como cualquier otro objeto de Python. En
particular, se pueden asignar a un nombre en el espacio de nombres de
un módulo de extensión. Otros módulos de extensión pueden importar
este módulo, recuperar el valor de este nombre y luego recuperar el
puntero de la Cápsula.

Hay muchas formas en que las Cápsulas se pueden usar para exportar la
API de C de un módulo de extensión. Cada función podría tener su
propia cápsula, o todos los punteros de API C podrían almacenarse en
una matriz cuya dirección se publica en una cápsula. Y las diversas
tareas de almacenamiento y recuperación de los punteros se pueden
distribuir de diferentes maneras entre el módulo que proporciona el
código y los módulos del cliente.

Cualquiera que sea el método que elija, es importante nombrar
correctamente sus Cápsulas. La función "PyCapsule_New()" toma un
parámetro de nombre (const char*); se le permite pasar un nombre
"NULL", pero le recomendamos encarecidamente que especifique un
nombre. Las Cápsulas correctamente nombradas brindan un grado de
seguridad de tipo de tiempo de ejecución; no hay una forma factible de
distinguir una Cápsula sin nombre de otra.

En particular, las cápsulas utilizadas para exponer las API de C deben
recibir un nombre siguiendo esta convención:

   modulename.attributename

La función de conveniencia "PyCapsule_Import()" facilita la carga de
una API C proporcionada a través de una cápsula, pero solo si el
nombre de la cápsula coincide con esta convención. Este comportamiento
brinda a los usuarios de C API un alto grado de certeza de que la
Cápsula que cargan contiene la API de C correcta.

El siguiente ejemplo demuestra un enfoque que pone la mayor parte de
la carga sobre el escritor del módulo de exportación, que es apropiado
para los módulos de biblioteca de uso común. Almacena todos los
punteros de la API de C (¡solo uno en el ejemplo!) en un arreglo de
punteros void que se convierte en el valor de una Cápsula. El archivo
de encabezado correspondiente al módulo proporciona una macro que se
encarga de importar el módulo y recuperar sus punteros C API; los
módulos de cliente solo tienen que llamar a esta macro antes de
acceder a la API de C.

The exporting module is a modification of the "spam" module from
section Un ejemplo simple. The function "spam.system()" does not call
the C library function "system()" directly, but a function
"PySpam_System()", which would of course do something more complicated
in reality (such as adding "spam" to every command). This function
"PySpam_System()" is also exported to other extension modules.

The function "PySpam_System()" is a plain C function, declared
"static" like everything else:

   static int
   PySpam_System(const char *command)
   {
       return system(command);
   }

The function "spam_system()" is modified in a trivial way:

   static PyObject *
   spam_system(PyObject *self, PyObject *args)
   {
       const char *command;
       int sts;

       if (!PyArg_ParseTuple(args, "s", &command))
           return NULL;
       sts = PySpam_System(command);
       return PyLong_FromLong(sts);
   }

Al comienzo del módulo, justo después de la línea:

   #include <Python.h>

se deben agregar dos líneas más:

   #define SPAM_MODULE
   #include "spammodule.h"

The "#define" is used to tell the header file that it is being
included in the exporting module, not a client module. Finally, the
module's "mod_exec" function must take care of initializing the C API
pointer array:

   static int
   spam_module_exec(PyObject *m)
   {
       static void *PySpam_API[PySpam_API_pointers];
       PyObject *c_api_object;

       /* Initialize the C API pointer array */
       PySpam_API[PySpam_System_NUM] = (void *)PySpam_System;

       /* Create a Capsule containing the API pointer array's address */
       c_api_object = PyCapsule_New((void *)PySpam_API, "spam._C_API", NULL);

       if (PyModule_Add(m, "_C_API", c_api_object) < 0) {
           return -1;
       }

       return 0;
   }

Note that "PySpam_API" is declared "static"; otherwise the pointer
array would disappear when "PyInit_spam()" terminates!

La mayor parte del trabajo está en el archivo de encabezado
"spammodule.h", que se ve así:

   #ifndef Py_SPAMMODULE_H
   #define Py_SPAMMODULE_H
   #ifdef __cplusplus
   extern "C" {
   #endif

   /* Header file for spammodule */

   /* C API functions */
   #define PySpam_System_NUM 0
   #define PySpam_System_RETURN int
   #define PySpam_System_PROTO (const char *command)

   /* Total number of C API pointers */
   #define PySpam_API_pointers 1

   #ifdef SPAM_MODULE
   /* This section is used when compiling spammodule.c */

   static PySpam_System_RETURN PySpam_System PySpam_System_PROTO;

   #else
   /* This section is used in modules that use spammodule's API */

   static void **PySpam_API;

   #define PySpam_System \
    (*(PySpam_System_RETURN (*)PySpam_System_PROTO) PySpam_API[PySpam_System_NUM])

   /* Return -1 on error, 0 on success.
    * PyCapsule_Import will set an exception if there's an error.
    */
   static int
   import_spam(void)
   {
       PySpam_API = (void **)PyCapsule_Import("spam._C_API", 0);
       return (PySpam_API != NULL) ? 0 : -1;
   }

   #endif

   #ifdef __cplusplus
   }
   #endif

   #endif /* !defined(Py_SPAMMODULE_H) */

All that a client module must do in order to have access to the
function "PySpam_System()" is to call the function (or rather macro)
"import_spam()" in its "mod_exec" function:

   static int
   client_module_exec(PyObject *m)
   {
       if (import_spam() < 0) {
           return -1;
       }
       /* additional initialization can happen here */
       return 0;
   }

La principal desventaja de este enfoque es que el archivo
"spammodule.h" es bastante complicado. Sin embargo, la estructura
básica es la misma para cada función que se exporta, por lo que solo
se debe aprender una vez.

Finalmente, debe mencionarse que las cápsulas ofrecen una
funcionalidad adicional, que es especialmente útil para la asignación
de memoria y la desasignación del puntero almacenado en una cápsula.
Los detalles se describen en el Manual de referencia de Python/C API
en la sección Cápsulas y en la implementación de Capsules (archivos
"Include/pycapsule.h" y "Objects/pycapsule.c" en la distribución del
código fuente de Python).

-[ Notas al pie de página ]-

[1] Ya existe una interfaz para esta función en el módulo estándar
    "os" --- se eligió como un ejemplo simple y directo.

[2] La metáfora de "pedir prestado" una referencia no es completamente
    correcta: el propietario todavía tiene una copia de la referencia.

[3] ¡Comprobar que el recuento de referencia es al menos 1 **no
    funciona** --- el recuento de referencia en sí podría estar en la
    memoria liberada y, por lo tanto, puede reutilizarse para otro
    objeto!

[4] Estas garantías no se cumplen cuando utiliza la convención de
    llamadas de estilo "antiguo", que todavía se encuentra en muchos
    códigos existentes.
