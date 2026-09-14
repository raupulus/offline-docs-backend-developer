---
title: 5. Creación de extensiones C y C++ en Windows
source_url: https://docs.python.org/es/3
source_path: extending/windows.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 1030
---

# 5. Creación de extensiones C y C++ en Windows

Este capítulo explica brevemente cómo crear un módulo de extensión de
Windows para Python usando Microsoft Visual C++, y sigue con
información de fondo más detallada sobre cómo funciona. El material
explicativo es útil tanto para el programador de Windows que está
aprendiendo a construir extensiones de Python como para el programador
de Unix interesado en producir software que se pueda construir con
éxito tanto en Unix como en Windows.

Se alienta a los autores de módulos a utilizar el enfoque distutils
para construir módulos de extensión, en lugar del descrito en esta
sección. Aún necesitará el compilador de C que se utilizó para
construir Python; típicamente Microsoft Visual C++.

Nota:

  Este capítulo menciona varios nombres de archivo que incluyen un
  número de versión codificado de Python. Estos nombres de archivo se
  representan con el número de versión que se muestra como "XY"; en la
  práctica, "'X'" será el número de versión principal y "'Y'" será el
  número de versión menor de la versión de Python con la que está
  trabajando. Por ejemplo, si está utilizando Python 2.2.1, "XY" en
  realidad será "22".

## 5.1. Un enfoque de libro de cocina

There are two approaches to building extension modules on Windows,
just as there are on Unix: use the "setuptools" package to control the
build process, or do things manually.  The setuptools approach works
well for most extensions; documentation on using "setuptools" to build
and package extension modules is available in Building C and C++
Extensions with setuptools.  If you find you really need to do things
manually, it may be instructive to study the project file for the
winsound standard library module.

## 5.2. Diferencias entre Unix y Windows

Unix y Windows usan paradigmas completamente diferentes para la carga
de código en tiempo de ejecución. Antes de intentar construir un
módulo que se pueda cargar dinámicamente, tenga en cuenta cómo
funciona su sistema.

En Unix, un archivo de objeto compartido (".so") contiene código para
ser utilizado por el programa, y también los nombres de funciones y
datos que espera encontrar en el programa. Cuando el archivo se une al
programa, todas las referencias a esas funciones y datos en el código
del archivo se cambian para apuntar a las ubicaciones reales en el
programa donde las funciones y los datos se colocan en la memoria.
Esto es básicamente una operación de enlace.

En Windows, un archivo de biblioteca de enlace dinámico (".dll") no
tiene referencias colgantes. En cambio, un acceso a funciones o datos
pasa por una tabla de búsqueda. Por lo tanto, el código DLL no tiene
que repararse en tiempo de ejecución para referirse a la memoria del
programa; en cambio, el código ya usa la tabla de búsqueda de la DLL,
y la tabla de búsqueda se modifica en tiempo de ejecución para apuntar
a las funciones y los datos.

En Unix, solo hay un tipo de archivo de biblioteca (".a") que contiene
código de varios archivos de objeto (".o"). Durante el paso de enlace
para crear un archivo de objeto compartido (".so"), el enlazador puede
encontrar que no sabe dónde se define un identificador. El enlazador
lo buscará en los archivos de objetos en las bibliotecas; si lo
encuentra, incluirá todo el código de ese archivo de objeto.

En Windows, hay dos tipos de biblioteca, una biblioteca estática y una
biblioteca de importación (ambas llamadas ".lib"). Una biblioteca
estática es como un archivo Unix ".a"; Contiene código para ser
incluido según sea necesario. Una biblioteca de importación se usa
básicamente solo para asegurarle al enlazador que cierto identificador
es legal y estará presente en el programa cuando se cargue la DLL. Por
lo tanto, el enlazador utiliza la información de la biblioteca de
importación para crear la tabla de búsqueda para usar identificadores
que no están incluidos en la DLL. Cuando se vincula una aplicación o
una DLL, se puede generar una biblioteca de importación, que deberá
usarse para todas las DLL futuras que dependan de los símbolos en la
aplicación o DLL.

Suponga que está creando dos módulos de carga dinámica, B y C, que
deberían compartir otro bloque de código A. En Unix, *no* pasaría
"A.a" al enlazador para "B.so" y "C.so"; eso haría que se incluyera
dos veces, de modo que B y C tengan cada uno su propia copia. En
Windows, compilar "A.dll" también compilará "A.lib". Usted *si* pasa
"A.lib" al enlazador para B y C. "A.lib" no contiene código; solo
contiene información que se usará en tiempo de ejecución para acceder
al código de A.

En Windows, usar una biblioteca de importación es como usar "importar
spam"; le da acceso a los nombres de spam, pero no crea una copia
separada. En Unix, vincular con una biblioteca es más como "from spam
import*"; crea una copia separada.

Py_NO_LINK_LIB

   Turn off the implicit, "#pragma"-based linkage with the Python
   library, performed inside CPython header files.

   Added in version 3.14.

## 5.3. Usar DLL en la práctica

Windows Python is built in Microsoft Visual C++; using other compilers
may or may not work.  The rest of this section is MSVC++ specific.

When creating DLLs in Windows, you can use the CPython library in two
ways:

1. By default, inclusion of "PC/pyconfig.h" directly or via "Python.h"
   triggers an implicit, configure-aware link with the library.  The
   header file chooses "pythonXY_d.lib" for Debug, "pythonXY.lib" for
   Release, and "pythonX.lib" for Release with the Limited API
   enabled.

   To build two DLLs, spam and ni (which uses C functions found in
   spam), you could use these commands:

      cl /LD /I/python/include spam.c
      cl /LD /I/python/include ni.c spam.lib

   The first command created three files: "spam.obj", "spam.dll" and
   "spam.lib".  "Spam.dll" does not contain any Python functions (such
   as "PyArg_ParseTuple()"), but it does know how to find the Python
   code thanks to the implicitly linked "pythonXY.lib".

   El segundo comando creó "ni.dll" (y ".obj" y ".lib"), que sabe cómo
   encontrar las funciones necesarias del spam, y también del
   ejecutable de Python.

2. Manually by defining "Py_NO_LINK_LIB" macro before including
   "Python.h". You must pass "pythonXY.lib" to the linker.

   To build two DLLs, spam and ni (which uses C functions found in
   spam), you could use these commands:

      cl /LD /DPy_NO_LINK_LIB /I/python/include spam.c ../libs/pythonXY.lib
      cl /LD /DPy_NO_LINK_LIB /I/python/include ni.c spam.lib ../libs/pythonXY.lib

   El primer comando creó tres archivos: "spam.obj", "spam.dll" y
   "spam.lib". "Spam.dll" no contiene ninguna función de Python (como
   "PyArg_ParseTuple()"), pero sabe cómo encontrar el código de Python
   gracias a "pythonXY.lib".

   El segundo comando creó "ni.dll" (y ".obj" y ".lib"), que sabe cómo
   encontrar las funciones necesarias del spam, y también del
   ejecutable de Python.

No todos los identificadores se exportan a la tabla de búsqueda. Si
desea que cualquier otro módulo (incluido Python) pueda ver sus
identificadores, debe decir "_declspec(dllexport)", como en "void
_declspec(dllexport) initspam(void)" o "PyObject_declspec(dllexport)
*NiGetSpamData(void)".

Developer Studio will throw in a lot of import libraries that you do
not really need, adding about 100K to your executable.  To get rid of
them, use the Project Settings dialog, Link tab, to specify *ignore
default libraries*.  Add the correct "msvcrt*xx*.lib" to the list of
libraries.
