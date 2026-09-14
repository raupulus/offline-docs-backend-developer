---
title: '"pydoc" --- Documentation generator and online help system'
source_url: https://docs.python.org/es/3
source_path: library/pydoc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3580
---

# "pydoc" --- Documentation generator and online help system

**Código fuente:** Lib/pydoc.py

======================================================================

The "pydoc" module automatically generates documentation from Python
modules.  The documentation can be presented as pages of text on the
console, served to a web browser, or saved to HTML files.

For modules, classes, functions and methods, the displayed
documentation is derived from the docstring (i.e. the "__doc__"
attribute) of the object, and recursively of its documentable members.
If there is no docstring, "pydoc" tries to obtain a description from
the block of comment lines just above the definition of the class,
function or method in the source file, or at the top of the module
(see "inspect.getcomments()").

The built-in function "help()" invokes the online help system in the
interactive interpreter, which uses "pydoc" to generate its
documentation as text on the console.  The same text documentation can
also be viewed from outside the Python interpreter by running
**pydoc** as a script at the operating system's command prompt. For
example, running

   python -m pydoc sys

en la entrada de la consola mostrará la documentación sobre el módulo
"sys", en un estilo similar a las páginas del manual que se muestran
por el comando **man** de Unix.  El argumento de **pydoc** puede ser
el nombre de una función, módulo, o paquete, o una referencia con
puntos (*dotted reference*) de una clase, método, o función dentro de
un módulo o módulo en un paquete.  Si el argumento de **pydoc** se
parece a una ruta (*path*) (es decir, que contiene el separador de
rutas para tu sistema operativo como una barra en Unix), y hace
referencia a un archivo fuente de Python existente, entonces se
produce la documentación para ese archivo.

Nota:

  In order to find objects and their documentation, "pydoc" imports
  the module(s) to be documented.  Therefore, any code on module level
  will be executed on that occasion.  Use an "if __name__ ==
  '__main__':" guard to only execute code when a file is invoked as a
  script and not just imported.

When printing output to the console, **pydoc** attempts to paginate
the output for easier reading.  If either the "MANPAGER" or the
"PAGER" environment variable is set, **pydoc** will use its value as a
pagination program. When both are set, "MANPAGER" is used.

Especificar un bandera (*flag*) "-w" antes del argumento hará que la
documentación HTML sea escrita en un archivo de la carpeta actual, en
vez de mostrar el texto en la consola.

Especificar una bandera (*flag*) "-k" antes del argumento buscará las
líneas de la sinopsis de todos los módulos disponibles por la palabra
clave (*keyword*) dada como argumento, de nuevo en una manera similar
al comando **man** de Unix.  La sinopsis de un módulo es la primera
línea de su cadena de documentación.

You can also use **pydoc** to start an HTTP server on the local
machine that will serve documentation to visiting web browsers.
**python -m pydoc -p 1234** will start a HTTP server on port 1234,
allowing you to browse the documentation at "http://localhost:1234/"
in your preferred web browser. Specifying "0" as the port number will
select an arbitrary unused port.

Advertencia:

  The "pydoc" HTTP server is intended for local use during development
  and is not suitable for production use.

**python -m pydoc -n <hostname>** will start the server listening at
the given hostname.  By default the hostname is 'localhost' but if you
want the server to be reached from other machines, you may want to
change the host name that the server responds to.  During development
this is especially useful if you want to run pydoc from within a
container.

**python -m pydoc -b** will start the server and additionally open a
web browser to a module index page.  Each served page has a navigation
bar at the top where you can *Get* help on an individual item,
*Search* all modules with a keyword in their synopsis line, and go to
the *Module index*, *Topics* and *Keywords* pages.

Cuando **pydoc** genera la documentación, se usa el entorno y ruta
actual para localizar los módulos.  Así, invocar **pydoc spam**
precisamente documenta la versión del módulo que tu obtendrías si
empezaras el interpretador de Python y escribieras "import spam".

Module docs for core modules are assumed to reside in
"https://docs.python.org/X.Y/library/" where "X" and "Y" are the major
and minor version numbers of the Python interpreter.  This can be
overridden by setting the "PYTHONDOCS" environment variable to a
different URL or to a local directory containing the Library Reference
Manual pages.

Distinto en la versión 3.2: Se añadió la opción "-b".

Distinto en la versión 3.3: La opción de la línea de comandos "-g" se
eliminó.

Distinto en la versión 3.4: "pydoc" now uses "inspect.signature()"
rather than "inspect.getfullargspec()" to extract signature
information from callables.

Distinto en la versión 3.7: Se añadió la opción "-n".
