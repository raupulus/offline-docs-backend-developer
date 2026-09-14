---
title: '"pkgutil" --- Package extension utility'
source_url: https://docs.python.org/es/3
source_path: library/pkgutil.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3470
---

# "pkgutil" --- Package extension utility

**Código fuente:** Lib/pkgutil.py

======================================================================

Este módulo proporciona utilidades para el sistema de importación, en
particular soporte para paquetes.

class pkgutil.ModuleInfo(module_finder, name, ispkg)

   Una tupla nombrada que contiene un breve resumen de la información
   del módulo.

   Added in version 3.6.

pkgutil.extend_path(path, name)

   Extiende la ruta de búsqueda de los módulos que componen un
   paquete. El uso previsto es colocar el siguiente código en
   "__init__.py": de un paquete:

      from pkgutil import extend_path
      __path__ = extend_path(__path__, __name__)

   For each directory on "sys.path" that has a subdirectory that
   matches the package name, add the subdirectory to the package's
   "__path__". This is useful if one wants to distribute different
   parts of a single logical package as multiple directories.

   It also looks for "*.pkg" files beginning where "*" matches the
   *name* argument.  This feature is similar to "*.pth" files (see the
   "site" module for more information), except that it doesn't
   special-case lines starting with "import".  A "*.pkg" file is
   trusted at face value: apart from skipping blank lines and ignoring
   comments, all entries found in a "*.pkg" file are added to the
   path, regardless of whether they exist on the filesystem (this is a
   feature).

   Si la ruta de entrada no es una lista (como es el caso de los
   paquetes congelados), se retorna sin cambios. La ruta de entrada no
   se modifica; se retorna una copia ampliada. Los elementos solo se
   adjuntan a la copia al final.

   Se supone que "sys.path" es una secuencia. Los elementos de
   "sys.path" que no sean cadenas de caracteres que se refieran a
   directorios existentes se ignoran. Los elementos Unicode en
   "sys.path" que causan errores cuando se utilizan como nombres de
   archivo pueden hacer que esta función lance una excepción (en línea
   con el comportamiento de "os.path.isdir()").

pkgutil.get_importer(path_item)

   Recupera un *finder* para el *path_item*.

   El buscador retornado se almacena en caché en
   "sys.path_importer_cache" si fue creado recientemente por un enlace
   de ruta.

   La caché (o parte de ella) puede ser borrada manualmente si el
   escaneo de "sys.path_hooks" es necesario.

   Distinto en la versión 3.3: Actualizado para basarse directamente
   en "importlib" en lugar de depender del paquete interno **PEP 302**
   emulación de importación.

pkgutil.iter_importers(fullname='')

   Cede (*yield*) objetos *finder* para el nombre de módulo dado.

   If *fullname* contains a "'.'", the finders will be for the package
   containing *fullname*, otherwise they will be all registered top
   level finders (i.e. those on both "sys.meta_path" and
   "sys.path_hooks").

   Si el módulo nombrado está en un paquete, ese paquete se importa
   como un efecto secundario de invocar esta función.

   Si no se especifica ningún nombre de módulo, se generan todos los
   buscadores de nivel superior.

   Distinto en la versión 3.3: Actualizado para basarse directamente
   en "importlib" en lugar de depender del paquete interno **PEP 302**
   emulación de importación.

pkgutil.iter_modules(path=None, prefix='')

   Yields "ModuleInfo" for all submodules on *path*, or, if *path* is
   "None", all top-level modules on "sys.path".

   *path* tendría que ser "None" o una list de rutas en las que buscar
   módulos.

   *prefix* es una cadena para mostrar delante de cada nombre de
   módulo en la salida.

   Nota:

     Sólo funciona para un *finder* que define un método
     "iter_modules()". Esta interfaz no es estándar, por lo que el
     módulo también proporciona implementaciones para
     "importlib.machinery.FileFinder" y "zipimport.zipimporter".

   Distinto en la versión 3.3: Actualizado para basarse directamente
   en "importlib" en lugar de depender del paquete interno **PEP 302**
   emulación de importación.

pkgutil.walk_packages(path=None, prefix='', onerror=None)

   Cede (*yield*) "ModuleInfo" para todos los módulos de forma
   recursiva en *path*, o, si *path* es "None", todos los módulos
   accesibles.

   *path* tendría que ser "None" o una list de rutas en las que buscar
   módulos.

   *prefix* es una cadena para mostrar delante de cada nombre de
   módulo en la salida.

   Note que esta función debe importar todos los *packages* (¡*no*
   todos los módulos!) en el *path* especificado, para acceder al
   atributo "__path__" para encontrar submódulos.

   *onerror* es una función que se llama con un argumento (el nombre
   del paquete que se estaba importando) si se produce alguna
   excepción al intentar importar un paquete. Si no se proporciona
   ninguna función *onerror*, los "ImportError" se capturan e ignoran,
   mientras que todas las demás excepciones se propagan, terminando la
   búsqueda.

   Ejemplos:

      # list all modules python can access
      walk_packages()

      # list all submodules of ctypes
      walk_packages(ctypes.__path__, ctypes.__name__ + '.')

   Nota:

     Sólo funciona para un *finder* que define un método
     "iter_modules()". Esta interfaz no es estándar, por lo que el
     módulo también proporciona implementaciones para
     "importlib.machinery.FileFinder" y "zipimport.zipimporter".

   Distinto en la versión 3.3: Actualizado para basarse directamente
   en "importlib" en lugar de depender del paquete interno **PEP 302**
   emulación de importación.

pkgutil.get_data(package, resource)

   Obtiene un recurso de un paquete.

   This is a wrapper for the *loader* "get_data" API.  The *package*
   argument should be the name of a package, in standard module format
   ("foo.bar").  The *resource* argument should be in the form of a
   relative filename, using "/" as the path separator.

   La función retorna una cadena de caracteres binaria que es el
   contenido del recurso especificado.

   This function uses the *loader* method "get_data()" to support
   modules installed in the filesystem, but also in zip files,
   databases, or elsewhere.

   Para los paquetes ubicados en el sistema de archivos, que ya se han
   importado, este es el equivalente aproximado de:

      d = os.path.dirname(sys.modules[package].__file__)
      data = open(os.path.join(d, resource), 'rb').read()

   Like the "open()" function, "get_data()" can follow parent
   directories ("../") and absolute paths (starting with "/" or "C:/",
   for example). It can open compilation/installation artifacts like
   ".py" and ".pyc" files or files with "reserved filenames". To be
   compatible with non-filesystem loaders, avoid using these features.

   Advertencia:

     This function is intended for trusted input. It does not verify
     that *resource* "belongs" to *package*.

   If you use a user-provided *resource* path, consider verifying it.
   For example, require an alphanumeric filename with a known
   extension, or install and check a list of known resources.

   Si el paquete no puede ser localizado o cargado, o usa un *loader*
   el cuál no soporta "get_data", entonces retorna "None". En
   particular, el: término *loader* para *namespace packages* no
   soporta "get_data".

   Ver también:

     The "importlib.resources" module provides structured access to
     module resources.

pkgutil.resolve_name(name)

   Resuelve un nombre a un objeto.

   Esta funcionalidad es usada en numerosos lugares en la librería
   estándar (ver bpo-12915) - y existe funcionalidad equivalente
   también en librerías de terceros ampliamente usadas, tales como
   setuptools, Django y Pyramid.

   Se espera que *name* sea una cadena de caracteres en uno de los
   siguientes formatos, donde W representa un identificador de Python
   válido, y un punto representa literalmente un punto en las
   siguientes pseudo-expresiones regulares:

   * "W(.W)*"

   * "W(.W)*:(W(.W)*)?"

   La primera forma existe sólo para mantener compatibilidad con
   versiones anteriores. Asume que parte del nombre con puntos es un
   paquete, y el resto es un objeto en algún lugar dentro de ese
   paquete, posiblemente anidado dentro de otros objetos. Dado que el
   lugar donde el paquete termina y la jerarquía de objetos comienza
   no puede ser inferida por inspección, con esta forma se debe
   realizar repetidos intentos de importación.

   En la segunda forma, el usuario hace claro el punto de división al
   proveer un signo de dos puntos: el nombre con puntos a la izquierda
   de los dos puntos es el paquete a ser importado, y el nombre con
   puntos a la derecha es la jerarquía de nombres dentro de ese
   paquete. Sólo una importación se necesaria con esta forma. Si
   termina con dos puntos, entonces se retorna un objeto módulo.

   La función retornará un objeto (el cual puede ser un módulo), o
   lanzará una de las siguientes excepciones:

   "ValueError" -- si *name* no tiene un formato reconocido.

   "ImportError" -- si una importación falló cuando no lo debería
   haber hecho.

   "AttributeError" -- Si un fallo ocurrió mientras se atravesaba la
   jerarquía de objetos dentro del paquete importado para obtener el
   objeto deseado.

   Added in version 3.9.
