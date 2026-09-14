---
title: Extendiendo/Embebiendo FAQ
source_url: https://docs.python.org/es/3
source_path: faq/extending.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: faq
order: 1050
---

# Extendiendo/Embebiendo FAQ

## ¿Puedo crear mis propias funciones en C?

Si, puedes crear módulos incorporados que contengan funciones,
variables, excepciones y incluso nuevos tipos en C. Esto esta
explicado en el documento Ampliación e incrustación del intérprete de
Python.

La mayoría de los libros intermedios o avanzados de Python también
tratan este tema.

## ¿Puedo crear mis propias funciones en C++?

Si, utilizando las características de compatibilidad encontradas en
C++. Coloca "extern "C" { ... }" alrededor los archivos incluidos
Python y pon "extern "C"" antes de cada función que será llamada por
el interprete Python. Objetos globales o estáticos C++ con
constructores no son una buena idea seguramente.

## Escribir en C es difícil; ¿no hay otra alternativa?

There are a number of alternatives to writing your own C extensions,
depending on what you're trying to do. Recommended third party tools
offer both simpler and more sophisticated approaches to creating C and
C++ extensions for Python.

## ¿Cómo puedo ejecutar declaraciones arbitrarias de Python desde C?

La función de más alto nivel para hacer esto es "PyRun_SimpleString()"
que toma un solo argumento de cadena de caracteres para ser ejecutado
en el contexto del módulo "__main__" y retorna "0" si tiene éxito y
"-1" cuando ocurre una excepción (incluyendo "SyntaxError"). Si
quieres mas control, usa "PyRun_String()"; mira la fuente para
"PyRun_SimpleString()" en "Python/pythonrun.c".

## ¿Cómo puedo evaluar una expresión arbitraria de Python desde C?

Llama a la función "PyRun_String()" de la pregunta anterior con el
símbolo de comienzo "Py_eval_input"; analiza una expresión, evalúa y
retorna su valor.

## ¿Cómo extraigo valores C de un objeto Python?

That depends on the object's type.  If it's a tuple, "PyTuple_Size()"
returns its length and "PyTuple_GetItem()" returns the item at a
specified index.  Lists have similar functions, "PyList_Size()" and
"PyList_GetItem()".

For bytes, "PyBytes_Size()" returns its length and
"PyBytes_AsStringAndSize()" provides a pointer to its value and its
length.  Note that Python bytes objects may contain null bytes so C's
"strlen()" should not be used.

Para testear el tipo de un objeto, primero debes estar seguro que no
es "NULL", y luego usa "PyBytes_Check()", "PyTuple_Check()",
"PyList_Check()", etc.

También hay una API de alto nivel para objetos Python que son
provistos por la supuestamente llamada interfaz 'abstracta' -- lee
"Include/abstract.h" para mas detalles. Permite realizar una interfaz
con cualquier tipo de secuencia Python usando llamadas como
"PySequence_Length()", "PySequence_GetItem()", etc. así como otros
protocolos útiles como números ("PyNumber_Index()" et al.) y mapeos en
las *PyMapping APIs*.

## ¿Cómo utilizo Py_BuildValue() para crear una tupla de un tamaño arbitrario?

No puedes hacerlo. Utiliza a cambio "PyTuple_Pack()".

## ¿Cómo puedo llamar un método de un objeto desde C?

Se puede utilizar la función "PyObject_CallMethod()" para llamar a un
método arbitrario de un objeto. Los parámetros son el objeto, el
nombre del método a llamar, una cadena de caracteres de formato como
las usadas con  "Py_BuildValue()", y los valores de argumento

   PyObject *
   PyObject_CallMethod(PyObject *object, const char *method_name,
                       const char *arg_format, ...);

Esto funciona para cualquier objeto que tenga métodos -- sean estos
incorporados o definidos por el usuario. Eres responsable si
eventualmente usas "Py_DECREF()" en el valor de retorno.

Para llamar, por ejemplo, un método "seek" de un objeto archivo con
argumentos 10, 0 (considerando que puntero del objeto archivo es "f"):

   res = PyObject_CallMethod(f, "seek", "(ii)", 10, 0);
   if (res == NULL) {
           ... an exception occurred ...
   }
   else {
           Py_DECREF(res);
   }

Note que debido a "PyObject_CallObject()" *siempre* necesita una tupla
para la lista de argumento, para llamar una función sin argumentos,
deberás pasar "()" para el formato, y para llamar a una función con un
solo argumento, encierra el argumento entre paréntesis, por ejemplo
"(i)".

## ¿Cómo obtengo la salida de PyErr_Print() (o cualquier cosa que se imprime a stdout/stderr)?

En código Python, define un objeto que soporta el método "write()".
Asigna este objeto a "sys.stdout" y "sys.stderr". Llama a print_error,
o solo permite que el mecanismo estándar de rastreo funcione. Luego,
la salida se hará cuando invoques "write()".

La manera mas fácil de hacer esto es usar la clase "io.StringIO":

   >>> import io, sys
   >>> sys.stdout = io.StringIO()
   >>> print('foo')
   >>> print('hello world!')
   >>> sys.stderr.write(sys.stdout.getvalue())
   foo
   hello world!

Un objeto personalizado para hacer lo mismo se vería así:

   >>> import io, sys
   >>> class StdoutCatcher(io.TextIOBase):
   ...     def __init__(self):
   ...         self.data = []
   ...     def write(self, stuff):
   ...         self.data.append(stuff)
   ...
   >>> import sys
   >>> sys.stdout = StdoutCatcher()
   >>> print('foo')
   >>> print('hello world!')
   >>> sys.stderr.write(''.join(sys.stdout.data))
   foo
   hello world!

## ¿Cómo accedo al módulo escrito en Python desde C?

Puedes obtener un puntero al módulo objeto de esta manera:

   module = PyImport_ImportModule("<modulename>");

Si el módulo todavía no se importó, (por ejemplo aún no esta presente
en "sys.modules"), esto inicializa el módulo, de otra forma
simplemente retorna el valor de "sys.modules["<modulename>"]". Nota
que no entra el módulo a ningún espacio de nombres (*namespace*)
--solo asegura que fue inicializado y guardado en "sys.modules".

Puedes acceder luego a los atributos del módulo (por ejemplo a
cualquier nombre definido en el módulo) de esta forma:

   attr = PyObject_GetAttrString(module, "<attrname>");

También funciona llamar a "PyObject_SetAttrString()" para asignar a
variables en el módulo.

## ¿Cómo hago una interface a objetos C++ desde Python?

Dependiendo de lo que necesites, hay varias maneras de hacerlo. Para
hacerlo manualmente empieza por leer the "Extending and Embedding"
document.Fíjate que para el sistema de tiempo de ejecución Python, no
hay una gran diferencia entre C y C++, por lo que la estrategia de
construir un nuevo tipo Python alrededor de una estructura de C de
tipo puntero, también funcionará para objetos C++.

Para bibliotecas C++, mira Escribir en C es difícil; ¿no hay otra
alternativa?.

## He agregado un módulo usando el archivo de configuración y el *make* falla. ¿Porque?

La configuración debe terminar en una nueva linea, si esta no está,
entonces el proceso *build* falla. (reparar esto requiere algún truco
de linea de comandos que puede ser no muy prolijo, y seguramente el
error es tan pequeño que no valdrá el esfuerzo.)

## ¿Cómo puedo depurar una extensión?

Cuando se usa GDB con extensiones cargadas de forma dinámica, puedes
configurar un punto de verificación (*breakpoint*) en tu extensión
hasta que esta se cargue.

En tu archivo ".gdbinit" (o interactivamente), agrega el comando:

   br _PyImport_LoadDynamicModule

Luego, cuando corras GDB:

   $ gdb /local/bin/python
   gdb) run myscript.py
   gdb) continue # repeat until your extension is loaded
   gdb) finish   # so that your extension is loaded
   gdb) br myfunction.c:50
   gdb) continue

## Quiero compilar un módulo Python en mi sistema Linux, pero me faltan algunos archivos . ¿Por qué?

Most packaged versions of Python omit some files required for
compiling Python extensions.

For Red Hat, install the python3-devel RPM to get the necessary files.

For Debian, run "apt-get install python3-dev".

## ¿Cómo digo "entrada incompleta" desde "entrada inválida"?

A veces quieres emular el comportamiento del interprete interactivo de
Python, que te da una continuación del *prompt* cuando la entrada esta
incompleta (por ejemplo si comenzaste tu instrucción "if" o no
cerraste un paréntesis o triples comillas), pero te da un mensaje de
error de sintaxis inmediatamente cuando la entrada es invalida.

En Python puedes usar el módulo "codeop", que aproxima el
comportamiento del analizador gramatical (*parser*) . IDLE usa esto,
por ejemplo.

La manera mas fácil de hacerlo en C es llamar a
"PyRun_InteractiveLoop()" (quizá en un hilo separado) y dejar que el
interprete Python gestione la entrada por ti. Puedes también
configurar "PyOS_ReadlineFunctionPointer()" para apuntar a tu función
de entrada personalizada.

## ¿Cómo encuentro símbolos g++ __builtin_new o __pure_virtual?

Para cargar dinámicamente módulos de extensión g++, debes recompilar
Python, hacer un nuevo *link* usando g++ (cambia LINKCC en el Python
Modules Makefile) y enlaza *link* tu extensión usando g++ (por ejemplo
"g++ -shared -o mymodule.so mymodule.o").

## ¿Puedo crear una clase objeto con algunos métodos implementado en C y otros en Python (por ejemplo a través de la herencia)?

Si, puedes heredar de clases integradas como "int", "list", "dict",
etc.

The Boost Python Library (BPL,
https://www.boost.org/libs/python/doc/index.html) provides a way of
doing this from C++ (i.e. you can inherit from an extension class
written in C++ using the BPL).
