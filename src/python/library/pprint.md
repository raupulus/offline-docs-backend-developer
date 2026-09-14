---
title: '"pprint" --- Data pretty printer'
source_url: https://docs.python.org/es/3
source_path: library/pprint.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3520
---

# "pprint" --- Data pretty printer

**Código fuente:** Lib/pprint.py

======================================================================

The "pprint" module provides a capability to "pretty-print" arbitrary
Python data structures in a form which can be used as input to the
interpreter. If the formatted structures include objects which are not
fundamental Python types, the representation may not be loadable.
This may be the case if objects such as files, sockets or classes are
included, as well as many other objects which are not representable as
Python literals.

The formatted representation keeps objects on a single line if it can,
and breaks them onto multiple lines if they don't fit within the
allowed width, adjustable by the *width* parameter defaulting to 80
characters.

Distinto en la versión 3.9: Soporte añadido para imprimir de forma
bonita "types.SimpleNamespace".

Distinto en la versión 3.10: Soporte añadido para imprimir de forma
bonita "dataclasses.dataclass".

## Functions

pprint.pp(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=False, underscore_numbers=False)

   Prints the formatted representation of *object*, followed by a
   newline. This function may be used in the interactive interpreter
   instead of the "print()" function for inspecting values. Tip: you
   can reassign "print = pprint.pp" for use within a scope.

   Parámetros:
      * **object** -- The object to be printed.

      * **stream** (*file-like object* | None) -- A file-like object
        to which the output will be written by calling its "write()"
        method. If "None" (the default), "sys.stdout" is used.

      * **indent** (*int*) -- The amount of indentation added for each
        nesting level.

      * **width** (*int*) -- The desired maximum number of characters
        per line in the output. If a structure cannot be formatted
        within the width constraint, a best effort will be made.

      * **depth** (*int** | **None*) -- The number of nesting levels
        which may be printed. If the data structure being printed is
        too deep, the next contained level is replaced by "...". If
        "None" (the default), there is no constraint on the depth of
        the objects being formatted.

      * **compact** (*bool*) -- Control the way long *sequences* are
        formatted. If "False" (the default), each item of a sequence
        will be formatted on a separate line, otherwise as many items
        as will fit within the *width* will be formatted on each
        output line.

      * **sort_dicts** (*bool*) -- If "True", dictionaries will be
        formatted with their keys sorted, otherwise they will be
        displayed in insertion order (the default).

      * **underscore_numbers** (*bool*) -- If "True", integers will be
        formatted with the "_" character for a thousands separator,
        otherwise underscores are not displayed (the default).

   >>> import pprint
   >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
   >>> stuff.insert(0, stuff)
   >>> pprint.pp(stuff)
   [<Recursion on list with id=...>,
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']

   Added in version 3.8.

pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

   Alias for "pp()" with *sort_dicts* set to "True" by default, which
   would automatically sort the dictionaries' keys, you might want to
   use "pp()" instead where it is "False" by default.

pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

   Return the formatted representation of *object* as a string.
   *indent*, *width*, *depth*, *compact*, *sort_dicts* and
   *underscore_numbers* are passed to the "PrettyPrinter" constructor
   as formatting parameters and their meanings are as described in the
   documentation above.

pprint.isreadable(object)

   Determina si la representación formateada de *object* es "legible"
   o si puede usarse para reconstruir el objeto usando "eval()".
   Siempre retorna "False" para objetos recursivos.

   >>> pprint.isreadable(stuff)
   False

pprint.isrecursive(object)

   Determine if *object* requires a recursive representation.  This
   function is subject to the same limitations as noted in
   "saferepr()" below and may raise an "RecursionError" if it fails to
   detect a recursive object.

pprint.saferepr(object)

   Return a string representation of *object*, protected against
   recursion in some common data structures, namely instances of
   "dict", "list" and "tuple" or subclasses whose "__repr__" has not
   been overridden.  If the representation of object exposes a
   recursive entry, the recursive reference will be represented as
   "<Recursion on typename with id=number>".  The representation is
   not otherwise formatted.

   >>> pprint.saferepr(stuff)
   "[<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']"

## Objetos *PrettyPrinter*

class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

   Construct a "PrettyPrinter" instance.

   Arguments have the same meaning as for "pp()". Note that they are
   in a different order, and that *sort_dicts* defaults to "True".

   >>> import pprint
   >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
   >>> stuff.insert(0, stuff[:])
   >>> pp = pprint.PrettyPrinter(indent=4)
   >>> pp.pprint(stuff)
   [   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
       'spam',
       'eggs',
       'lumberjack',
       'knights',
       'ni']
   >>> pp = pprint.PrettyPrinter(width=41, compact=True)
   >>> pp.pprint(stuff)
   [['spam', 'eggs', 'lumberjack',
     'knights', 'ni'],
    'spam', 'eggs', 'lumberjack', 'knights',
    'ni']
   >>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
   ... ('parrot', ('fresh fruit',))))))))
   >>> pp = pprint.PrettyPrinter(depth=6)
   >>> pp.pprint(tup)
   ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))

   Distinto en la versión 3.4: Añadido el argumento *compact*.

   Distinto en la versión 3.8: Añadido el argumento *sort_dicts*.

   Distinto en la versión 3.10: Se agregó el parámetro
   *underscore_numbers*.

   Distinto en la versión 3.11: No longer attempts to write to
   "sys.stdout" if it is "None".

Las instancias de "PrettyPrinter" tienen los siguientes métodos:

PrettyPrinter.pformat(object)

   Retorna la representación formateada de *object*.  Tiene en cuenta
   las opciones pasadas al constructor de la clase "PrettyPrinter".

PrettyPrinter.pprint(object)

   Imprime la representación formateada de *object* en la secuencia
   configurada, seguida de una nueva línea.

Los siguientes métodos proporcionan las implementaciones para las
funciones correspondientes con los mismos nombres. Usar estos métodos
en una instancia es algo más eficiente, ya que no es necesario crear
nuevos objetos "PrettyPrinter".

PrettyPrinter.isreadable(object)

   Determina si la representación formateada de *object* es "legible"
   o si se puede usar para reconstruir su valor usando "eval()". Se
   debe tener en cuenta que se retorna "False" para objetos
   recursivos. Si el parámetro *depth* de "PrettyPrinter" es
   proporcionado y el objeto es más profundo de lo permitido, también
   se retorna "False".

PrettyPrinter.isrecursive(object)

   Determina si *object* requiere una representación recursiva.

Este método se proporciona como un punto de entrada o método de enlace
automático (*hook* en inglés) para permitir que las subclases
modifiquen la forma en que los objetos se convierten en cadenas de
caracteres. La implementación por defecto utiliza la implementación
interna de "saferepr()".

PrettyPrinter.format(object, context, maxlevels, level)

   Retorna tres valores: la versión formateada de *object* como una
   cadena de caracteres, una bandera que indica si el resultado es
   legible y una bandera que indica si se detectó recursividad. El
   primer argumento es el objeto a representar. El segundo es un
   diccionario que contiene la "id()" de los objetos que son parte del
   contexto de representación actual (contenedores directos e
   indirectos para *object* que están afectando a la representación),
   como las claves; si es necesario representar un objeto que ya está
   representado en *context*, el tercer valor de retorno será "True".
   Las llamadas recursivas al método "format()" deben agregar entradas
   adicionales a los contenedores de este diccionario. El tercer
   argumento, *maxlevels*, proporciona el límite máximo de
   recursividad; su valor por defecto es "0". Este argumento debe
   pasarse sin modificaciones a las llamadas recursivas. El cuarto
   argumento, *level*, da el nivel actual; las llamadas recursivas
   sucesivas deben pasar un valor menor que el de la llamada actual.

## Ejemplo

To demonstrate several uses of the "pp()" function and its parameters,
let's fetch information about a project from PyPI:

   >>> import json
   >>> import pprint
   >>> from urllib.request import urlopen
   >>> with urlopen('https://pypi.org/pypi/sampleproject/1.2.0/json') as resp:
   ...     project_info = json.load(resp)['info']

In its basic form, "pp()" shows the whole object:

   >>> pprint.pp(project_info)
   {'author': 'The Python Packaging Authority',
    'author_email': 'pypa-dev@googlegroups.com',
    'bugtrack_url': None,
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.6',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.2',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Topic :: Software Development :: Build Tools'],
    'description': 'A sample Python project\n'
                   '=======================\n'
                   '\n'
                   'This is the description file for the project.\n'
                   '\n'
                   'The file should use UTF-8 encoding and be written using '
                   'ReStructured Text. It\n'
                   'will be used to generate the project webpage on PyPI, and '
                   'should be written for\n'
                   'that purpose.\n'
                   '\n'
                   'Typical contents for this file would include an overview of '
                   'the project, basic\n'
                   'usage examples, etc. Generally, including the project '
                   'changelog in here is not\n'
                   'a good idea, although a simple "What\'s New" section for the '
                   'most recent version\n'
                   'may be appropriate.',
    'description_content_type': None,
    'docs_url': None,
    'download_url': 'UNKNOWN',
    'downloads': {'last_day': -1, 'last_month': -1, 'last_week': -1},
    'home_page': 'https://github.com/pypa/sampleproject',
    'keywords': 'sample setuptools development',
    'license': 'MIT',
    'maintainer': None,
    'maintainer_email': None,
    'name': 'sampleproject',
    'package_url': 'https://pypi.org/project/sampleproject/',
    'platform': 'UNKNOWN',
    'project_url': 'https://pypi.org/project/sampleproject/',
    'project_urls': {'Download': 'UNKNOWN',
                     'Homepage': 'https://github.com/pypa/sampleproject'},
    'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
    'requires_dist': None,
    'requires_python': None,
    'summary': 'A sample Python project',
    'version': '1.2.0'}

El resultado puede limitarse a una cierta profundidad asignando un
valor al argumento *depth* ("..." se utiliza para contenidos más
"profundos"):

   >>> pprint.pp(project_info, depth=1)
   {'author': 'The Python Packaging Authority',
    'author_email': 'pypa-dev@googlegroups.com',
    'bugtrack_url': None,
    'classifiers': [...],
    'description': 'A sample Python project\n'
                   '=======================\n'
                   '\n'
                   'This is the description file for the project.\n'
                   '\n'
                   'The file should use UTF-8 encoding and be written using '
                   'ReStructured Text. It\n'
                   'will be used to generate the project webpage on PyPI, and '
                   'should be written for\n'
                   'that purpose.\n'
                   '\n'
                   'Typical contents for this file would include an overview of '
                   'the project, basic\n'
                   'usage examples, etc. Generally, including the project '
                   'changelog in here is not\n'
                   'a good idea, although a simple "What\'s New" section for the '
                   'most recent version\n'
                   'may be appropriate.',
    'description_content_type': None,
    'docs_url': None,
    'download_url': 'UNKNOWN',
    'downloads': {...},
    'home_page': 'https://github.com/pypa/sampleproject',
    'keywords': 'sample setuptools development',
    'license': 'MIT',
    'maintainer': None,
    'maintainer_email': None,
    'name': 'sampleproject',
    'package_url': 'https://pypi.org/project/sampleproject/',
    'platform': 'UNKNOWN',
    'project_url': 'https://pypi.org/project/sampleproject/',
    'project_urls': {...},
    'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
    'requires_dist': None,
    'requires_python': None,
    'summary': 'A sample Python project',
    'version': '1.2.0'}

Además, se puede establecer un valor máximo de caracteres por línea
asignando un valor al parámetro *width*. Si un objeto largo no se
puede dividir, el valor dado al ancho se anulará y será excedido:

   >>> pprint.pp(project_info, depth=1, width=60)
   {'author': 'The Python Packaging Authority',
    'author_email': 'pypa-dev@googlegroups.com',
    'bugtrack_url': None,
    'classifiers': [...],
    'description': 'A sample Python project\n'
                   '=======================\n'
                   '\n'
                   'This is the description file for the '
                   'project.\n'
                   '\n'
                   'The file should use UTF-8 encoding and be '
                   'written using ReStructured Text. It\n'
                   'will be used to generate the project '
                   'webpage on PyPI, and should be written '
                   'for\n'
                   'that purpose.\n'
                   '\n'
                   'Typical contents for this file would '
                   'include an overview of the project, '
                   'basic\n'
                   'usage examples, etc. Generally, including '
                   'the project changelog in here is not\n'
                   'a good idea, although a simple "What\'s '
                   'New" section for the most recent version\n'
                   'may be appropriate.',
    'description_content_type': None,
    'docs_url': None,
    'download_url': 'UNKNOWN',
    'downloads': {...},
    'home_page': 'https://github.com/pypa/sampleproject',
    'keywords': 'sample setuptools development',
    'license': 'MIT',
    'maintainer': None,
    'maintainer_email': None,
    'name': 'sampleproject',
    'package_url': 'https://pypi.org/project/sampleproject/',
    'platform': 'UNKNOWN',
    'project_url': 'https://pypi.org/project/sampleproject/',
    'project_urls': {...},
    'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
    'requires_dist': None,
    'requires_python': None,
    'summary': 'A sample Python project',
    'version': '1.2.0'}
