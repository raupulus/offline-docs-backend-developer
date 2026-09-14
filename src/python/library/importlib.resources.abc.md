---
title: '"importlib.resources.abc" -- Abstract base classes for resources'
source_url: https://docs.python.org/es/3
source_path: library/importlib.resources.abc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2960
---

# "importlib.resources.abc" -- Abstract base classes for resources

**Source code:** Lib/importlib/resources/abc.py

======================================================================

Added in version 3.11.

class importlib.resources.abc.ResourceReader

   *Superseded by TraversableResources*

   Un *abstract base class* para proporcionar la capacidad de leer
   *resources*.

   From the perspective of this ABC, a *resource* is a binary artifact
   that is shipped within a package. Typically this is something like
   a data file that lives next to the "__init__.py" file of the
   package. The purpose of this class is to help abstract out the
   accessing of such data files so that it does not matter if the
   package and its data file(s) are stored e.g. in a zip file versus
   on the file system.

   Para cualquiera de los métodos de esta clase, se espera que un
   argumento *resource* sea un *path-like object* que represente
   conceptualmente solo un nombre de archivo. Esto significa que no se
   deben incluir rutas de subdirectorios en el argumento *resource*.
   Esto se debe a que la ubicación del paquete para el que se
   encuentra el lector actúa como el "directorio". Por lo tanto, la
   metáfora de directorios y nombres de archivos es paquetes y
   recursos, respectivamente. Esta es también la razón por la que se
   espera que las instancias de esta clase se correlacionen
   directamente con un paquete específico (en lugar de representar
   potencialmente varios paquetes o un módulo).

   Se espera que los cargadores que deseen admitir la lectura de
   recursos proporcionen un método llamado
   "get_resource_reader(fullname)" que retorna un objeto que
   implementa la interfaz de este ABC. Si el módulo especificado por
   nombre completo no es un paquete, este método debería retornar
   "None". Un objeto compatible con este ABC solo debe retornarse
   cuando el módulo especificado es un paquete.

   Obsoleto desde la versión 3.12: Use
   "importlib.resources.abc.TraversableResources" instead.

   abstractmethod open_resource(resource)

      Retorna un *file-like object* abierto para la lectura binaria
      del *resource*.

      Si no se puede encontrar el recurso, se genera
      "FileNotFoundError".

   abstractmethod resource_path(resource)

      Retorna la ruta del sistema de archivos al *resource*.

      Si el recurso no existe concretamente en el sistema de archivos,
      lanza "FileNotFoundError".

   abstractmethod is_resource(path)

      Returns "True" if the named *path* is considered a resource.
      "FileNotFoundError" is raised if *path* does not exist.

      Distinto en la versión 3.10: The argument *name* was renamed to
      *path*.

   abstractmethod contents()

      Retorna un *iterable* de cadenas sobre el contenido del paquete.
      Tenga en cuenta que no se requiere que todos los nombres
      devueltos por el iterador sean recursos reales, p. es aceptable
      devolver nombres para los que "is_resource()" sería falso.

      Permitir que se retornen nombres que no son de recursos es
      permitir situaciones en las que se conoce a priori cómo se
      almacenan un paquete y sus recursos y los nombres que no son de
      recursos serían útiles. Por ejemplo, se permite devolver nombres
      de subdirectorios para que cuando se sepa que el paquete y los
      recursos están almacenados en el sistema de archivos, esos
      nombres de subdirectorios se puedan usar directamente.

      El método abstracto retorna un iterable sin elementos.

class importlib.resources.abc.Traversable

   An object with a subset of "pathlib.Path" methods suitable for
   traversing directories and opening files.

   For a representation of the object on the file-system, use
   "importlib.resources.as_file()".

   name

      Resumen. El nombre base de este objeto sin ninguna referencia
      principal.

   abstractmethod iterdir()

      Produce generador iterador de objetos Traversable en self.

   abstractmethod is_dir()

      Return "True" if self is a directory.

   abstractmethod is_file()

      Return "True" if self is a file.

   abstractmethod joinpath(*pathsegments)

      Traverse directories according to *pathsegments* and return the
      result as "Traversable".

      Each *pathsegments* argument may contain multiple names
      separated by forward slashes ("/", "posixpath.sep" ). For
      example, the following are equivalent:

         files.joinpath('subdir', 'subsuddir', 'file.txt')
         files.joinpath('subdir/subsuddir/file.txt')

      Note that some "Traversable" implementations might not be
      updated to the latest version of the protocol. For compatibility
      with such implementations, provide a single argument without
      path separators to each call to "joinpath". For example:

         files.joinpath('subdir').joinpath('subsubdir').joinpath('file.txt')

      Distinto en la versión 3.11: "joinpath" accepts multiple
      *pathsegments*, and these segments may contain forward slashes
      as path separators. Previously, only a single *child* argument
      was accepted.

   abstractmethod __truediv__(child)

      Return Traversable child in self. Equivalent to
      "joinpath(child)".

   abstractmethod open(mode='r', *args, **kwargs)

      *mode* puede ser 'r' o 'rb' para abrir como texto o binario.
      Retorna un identificador adecuado para la lectura (igual que
      "pathlib.Path.open").

      When opening as text, accepts encoding parameters such as those
      accepted by "io.TextIOWrapper".

   read_bytes()

      Lee el contenido de self como bytes.

   read_text(encoding=None)

      Lee el contenido de self como texto.

class importlib.resources.abc.TraversableResources

   An abstract base class for resource readers capable of serving the
   "importlib.resources.files()" interface. Subclasses
   "ResourceReader" and provides concrete implementations of the
   "ResourceReader"'s abstract methods. Therefore, any loader
   supplying "TraversableResources" also supplies "ResourceReader".

   Se espera que los cargadores que deseen admitir la lectura de
   recursos implementen esta interfaz.

   abstractmethod files()

      Retorna un objeto "importlib.resources.abc.Traversable" para el
      paquete cargado.
