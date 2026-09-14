---
title: '"importlib.metadata" -- Acceso a los metadatos de los paquetes'
source_url: https://docs.python.org/es/3
source_path: library/importlib.metadata.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2950
---

# "importlib.metadata" -- Acceso a los metadatos de los paquetes

Added in version 3.8.

Distinto en la versión 3.10: "importlib.metadata" ya no es
provisional.

**Source code:** Lib/importlib/metadata/__init__.py

"importlib.metadata" is a library that provides access to the metadata
of an installed Distribution Package, such as its entry points or its
top-level names (Import Packages, modules, if any). Built in part on
Python's import system, this library provides the entry point and
metadata APIs that were previously exposed by the now-removed
"pkg_resources" package. Along with "importlib.resources", it
supersedes "pkg_resources".

"importlib.metadata" operates on third-party *distribution packages*
installed into Python's "site-packages" directory via tools such as
pip. Specifically, it works with distributions with discoverable
"dist-info" or "egg-info" directories, and metadata defined by the
Core metadata specifications.

Importante:

  These are *not* necessarily equivalent to or correspond 1:1 with the
  top-level *import package* names that can be imported inside Python
  code. One *distribution package* can contain multiple *import
  packages* (and single modules), and one top-level *import package*
  may map to multiple *distribution packages* if it is a namespace
  package. You can use packages_distributions() to get a mapping
  between them.

By default, distribution metadata can live on the file system or in
zip archives on "sys.path". Through an extension mechanism, the
metadata can live almost anywhere.

Ver también:

  https://importlib-metadata.readthedocs.io/
     La documentación de "importlib_metadata", que proporciona un
     backport de "importlib.metadata". Esto incluye una Referencia API
     para las clases y funciones de este módulo, así como una Guía de
     migración para los usuarios existentes de "pkg_resources".

## Descripción general

Let's say you wanted to get the version string for a Distribution
Package you've installed using "pip". We start by creating a virtual
environment and installing something into it:

   $ python -m venv example
   $ source example/bin/activate
   (example) $ python -m pip install wheel

Se puede obtener la cadena de versión para "wheel" ejecutando lo
siguiente:

   (example) $ python
   >>> from importlib.metadata import version
   >>> version('wheel')
   '0.32.3'

You can also get a collection of entry points selectable by properties
of the EntryPoint (typically 'group' or 'name'), such as
"console_scripts", "distutils.commands" and others. Each group
contains a collection of EntryPoint objects.

Se pueden obtener los metadatos para una distribución:

   >>> list(metadata('wheel'))
   ['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'Maintainer', 'Maintainer-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python', 'Provides-Extra', 'Requires-Dist', 'Requires-Dist']

También se puede obtener el número de versión de una distribución,
enumerar sus archivos constituyentes y obtener una lista de los
Requerimientos de la distribución de la distribución.

exception importlib.metadata.PackageNotFoundError

   Subclass of "ModuleNotFoundError" raised by several functions in
   this module when queried for a distribution package which is not
   installed in the current Python environment.

## API funcional

Este paquete provee la siguiente funcionalidad a través de su API
pública.

### Puntos de entrada

importlib.metadata.entry_points(**select_params)

   Returns a "EntryPoints" instance describing entry points for the
   current environment. Any given keyword parameters are passed to the
   "select()" method for comparison to the attributes of the
   individual entry point definitions.

   Note: it is not currently possible to query for entry points based
   on their "EntryPoint.dist" attribute (as different "Distribution"
   instances do not currently compare equal, even if they have the
   same attributes)

class importlib.metadata.EntryPoints

   Details of a collection of installed entry points.

   Also provides a ".groups" attribute that reports all identified
   entry point groups, and a ".names" attribute that reports all
   identified entry point names.

class importlib.metadata.EntryPoint

   Details of an installed entry point.

   Each "EntryPoint" instance has ".name", ".group", and ".value"
   attributes and a ".load()" method to resolve the value. There are
   also ".module", ".attr", and ".extras" attributes for getting the
   components of the ".value" attribute, and ".dist" for obtaining
   information regarding the distribution package that provides the
   entry point.

Consultar todos los puntos de entrada:

   >>> eps = entry_points()

The "entry_points()" function returns a "EntryPoints" object, a
collection of all "EntryPoint" objects with "names" and "groups"
attributes for convenience:

   >>> sorted(eps.groups)
   ['console_scripts', 'distutils.commands', 'distutils.setup_keywords', 'egg_info.writers', 'setuptools.installation']

"EntryPoints" has a "select()" method to select entry points matching
specific properties. Select entry points in the "console_scripts"
group:

   >>> scripts = eps.select(group='console_scripts')

Equivalently, since "entry_points()" passes keyword arguments through
to select:

   >>> scripts = entry_points(group='console_scripts')

Elige un script específico llamado "wheel" (que se encuentra en el
proyecto *wheel*):

   >>> 'wheel' in scripts.names
   True
   >>> wheel = scripts['wheel']

De manera equivalente, consulta por ese punto de entrada durante la
selección:

   >>> (wheel,) = entry_points(group='console_scripts', name='wheel')
   >>> (wheel,) = entry_points().select(group='console_scripts', name='wheel')

Inspeccionar el punto de entrada resuelto:

   >>> wheel
   EntryPoint(name='wheel', value='wheel.cli:main', group='console_scripts')
   >>> wheel.module
   'wheel.cli'
   >>> wheel.attr
   'main'
   >>> wheel.extras
   []
   >>> main = wheel.load()
   >>> main
   <function main at 0x103528488>

The "group" and "name" are arbitrary values defined by the package
author and usually a client will wish to resolve all entry points for
a particular group. Read the setuptools docs for more information on
entry points, their definition, and usage.

Distinto en la versión 3.12: The "selectable" entry points were
introduced in "importlib_metadata" 3.6 and Python 3.10. Prior to those
changes, "entry_points" accepted no parameters and always returned a
dictionary of entry points, keyed by group. With "importlib_metadata"
5.0 and Python 3.12, "entry_points" always returns an "EntryPoints"
object. See backports.entry_points_selectable for compatibility
options.

Distinto en la versión 3.13: "EntryPoint" objects no longer present a
tuple-like interface ("__getitem__()").

### Metadatos de distribución

importlib.metadata.metadata(distribution_name)

   Return the distribution metadata corresponding to the named
   distribution package as a "PackageMetadata" instance.

   Raises "PackageNotFoundError" if the named distribution package is
   not installed in the current Python environment.

class importlib.metadata.PackageMetadata

   A concrete implementation of the PackageMetadata protocol.

   In addition to providing the defined protocol methods and
   attributes, subscripting the instance is equivalent to calling the
   "get()" method.

Every Distribution Package includes some metadata, which you can
extract using the "metadata()" function:

   >>> wheel_metadata = metadata('wheel')

The keys of the returned data structure name the metadata keywords,
and the values are returned unparsed from the distribution metadata:

   >>> wheel_metadata['Requires-Python']
   '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

"PackageMetadata" also presents a "json" attribute that returns all
the metadata in a JSON-compatible form per **PEP 566**:

   >>> wheel_metadata.json['requires_python']
   '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

The full set of available metadata is not described here. See the PyPA
Core metadata specification for additional details.

Distinto en la versión 3.10: La "Descripción" ahora se incluye en los
metadatos cuando se presenta a través de la carga útil. Se han
eliminado los caracteres de continuación de línea.El atributo "json"
fue añadido.

### Versiones de distribución

importlib.metadata.version(distribution_name)

   Return the installed distribution package version for the named
   distribution package.

   Raises "PackageNotFoundError" if the named distribution package is
   not installed in the current Python environment.

The "version()" function is the quickest way to get a Distribution
Package's version number, as a string:

   >>> version('wheel')
   '0.32.3'

### Archivos de distribución

importlib.metadata.files(distribution_name)

   Return the full set of files contained within the named
   distribution package.

   Raises "PackageNotFoundError" if the named distribution package is
   not installed in the current Python environment.

   Returns "None" if the distribution is found but the installation
   database records reporting the files associated with the
   distribution package are missing.

class importlib.metadata.PackagePath

   A "pathlib.PurePath" derived object with additional "dist", "size",
   and "hash" properties corresponding to the distribution package's
   installation metadata for that file.

The "files()" function takes a Distribution Package name and returns
all of the files installed by this distribution. Each file is reported
as a "PackagePath" instance. For example:

   >>> util = [p for p in files('wheel') if 'util.py' in str(p)][0]
   >>> util
   PackagePath('wheel/util.py')
   >>> util.size
   859
   >>> util.dist
   <importlib.metadata._hooks.PathDistribution object at 0x101e0cef0>
   >>> util.hash
   <FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>

Una vez que se tiene el archivo, también se puede leer su contenido:

   >>> print(util.read_text())
   import base64
   import sys
   ...
   def as_bytes(s):
       if isinstance(s, text_type):
           return s.encode('utf-8')
       return s

You can also use the "locate()" method to get the absolute path to the
file:

   >>> util.locate()
   PosixPath('/home/gustav/example/lib/site-packages/wheel/util.py')

In the case where the metadata file listing files ("RECORD" or
"SOURCES.txt") is missing, "files()" will return "None". The caller
may wish to wrap calls to "files()" in always_iterable or otherwise
guard against this condition if the target distribution is not known
to have the metadata present.

### Requerimientos de la distribución

importlib.metadata.requires(distribution_name)

   Return the declared dependency specifiers for the named
   distribution package.

   Raises "PackageNotFoundError" if the named distribution package is
   not installed in the current Python environment.

To get the full set of requirements for a Distribution Package, use
the "requires()" function:

   >>> requires('wheel')
   ["pytest (>=3.0.0) ; extra == 'test'", "pytest-cov ; extra == 'test'"]

### Mapeo de paquetes de importación a distribución

importlib.metadata.packages_distributions()

   Return a mapping from the top level module and import package names
   found via "sys.meta_path" to the names of the distribution packages
   (if any) that provide the corresponding files.

   To allow for namespace packages (which may have members provided by
   multiple distribution packages), each top level import name maps to
   a list of distribution names rather than mapping directly to a
   single name.

Un método práctico para resolver el nombre del Paquete de distribución
(o nombres, en el caso de un paquete de espacio de nombres) que
proporciona cada módulo Python de nivel superior importable o Paquete
de importación:

   >>> packages_distributions()
   {'importlib_metadata': ['importlib-metadata'], 'yaml': ['PyYAML'], 'jaraco': ['jaraco.classes', 'jaraco.functools'], ...}

Algunas instalaciones editables, no suministran nombres de nivel
superior, por lo que esta función no es fiable con dichas
instalaciones.

Added in version 3.10.

## Distribuciones

importlib.metadata.distribution(distribution_name)

   Return a "Distribution" instance describing the named distribution
   package.

   Raises "PackageNotFoundError" if the named distribution package is
   not installed in the current Python environment.

class importlib.metadata.Distribution

   Details of an installed distribution package.

   Note: different "Distribution" instances do not currently compare
   equal, even if they relate to the same installed distribution and
   accordingly have the same attributes.

While the module level API described above is the most common and
convenient usage, you can get all of that information from the
"Distribution" class. "Distribution" is an abstract object that
represents the metadata for a Python Distribution Package. You can get
the concrete "Distribution" subclass instance for an installed
distribution package by calling the "distribution()" function:

   >>> from importlib.metadata import distribution
   >>> dist = distribution('wheel')
   >>> type(dist)
   <class 'importlib.metadata.PathDistribution'>

Thus, an alternative way to get the version number is through the
"Distribution" instance:

   >>> dist.version
   '0.32.3'

There are all kinds of additional metadata available on "Distribution"
instances:

   >>> dist.metadata['Requires-Python']
   '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
   >>> dist.metadata['License']
   'MIT'

For editable packages, an "origin" property may present **PEP 610**
metadata:

   >>> dist.origin.url
   'file:///path/to/wheel-0.32.3.editable-py3-none-any.whl'

The full set of available metadata is not described here. See the PyPA
Core metadata specification for additional details.

Added in version 3.13: The ".origin" property was added.

## Distribution Discovery

Por defecto, este paquete proporciona soporte incorporado para el
descubrimiento de metadatos para el sistema de archivos y archivos zip
Distribution Packages. Este buscador de metadatos busca por defecto
"sys.path", pero varía ligeramente en cómo interpreta esos valores
respecto a cómo lo hace otra maquinaria de importación. En particular:

* "importlib.metadata" does not honor "bytes" objects on "sys.path".

* "importlib.metadata" respetará incidentalmente los objetos
  "pathlib.Path`" en "sys.path" aunque tales valores serán ignorados
  para las importaciones.

## Implementing Custom Providers

"importlib.metadata" address two API surfaces, one for *consumers* and
another for *providers*. Most users are consumers, consuming metadata
provided by the packages. There are other use-cases, however, where
users wish to expose metadata through some other mechanism, such as
alongside a custom importer. Such a use case calls for a *custom
provider*.

Because Distribution Package metadata is not available through
"sys.path" searches, or package loaders directly, the metadata for a
distribution is found through import system finders. To find a
distribution package's metadata, "importlib.metadata" queries the list
of *meta path finders* on "sys.meta_path".

The implementation has hooks integrated into the "PathFinder", serving
metadata for distribution packages found on the file system.

La clase abstracta "importlib.abc.MetaPathFinder" define la interfaz
que se espera de los buscadores por el sistema de importación de
Python. "importlib.metadata" amplía este protocolo buscando una
"find_distributions" opcional invocable en los buscadores desde
"sys.meta_path" y presenta esta interfaz extendida como la clase base
abstracta "DistributionFinder", que define este método abstracto:

   @abc.abstractmethod
   def find_distributions(context=DistributionFinder.Context()) -> Iterable[Distribution]:
       """Return an iterable of all Distribution instances capable of
       loading the metadata for packages for the indicated ``context``.
       """

The "DistributionFinder.Context" object provides ".path" and ".name"
properties indicating the path to search and name to match and may
supply other relevant context sought by the consumer.

In practice, to support finding distribution package metadata in
locations other than the file system, subclass "Distribution" and
implement the abstract methods. Then from a custom finder, return
instances of this derived "Distribution" in the "find_distributions()"
method.

### Example

Imagine a custom finder that loads Python modules from a database:

   class DatabaseImporter(importlib.abc.MetaPathFinder):
       def __init__(self, db):
           self.db = db

       def find_spec(self, fullname, target=None) -> ModuleSpec:
           return self.db.spec_from_name(fullname)

   sys.meta_path.append(DatabaseImporter(connect_db(...)))

That importer now presumably provides importable modules from a
database, but it provides no metadata or entry points. For this custom
importer to provide metadata, it would also need to implement
"DistributionFinder":

   from importlib.metadata import DistributionFinder

   class DatabaseImporter(DistributionFinder):
       ...

       def find_distributions(self, context=DistributionFinder.Context()):
           query = dict(name=context.name) if context.name else {}
           for dist_record in self.db.query_distributions(query):
               yield DatabaseDistribution(dist_record)

In this way, "query_distributions" would return records for each
distribution served by the database matching the query. For example,
if "requests-1.0" is in the database, "find_distributions" would yield
a "DatabaseDistribution" for "Context(name='requests')" or
"Context(name=None)".

For the sake of simplicity, this example ignores "context.path". The
"path" attribute defaults to "sys.path" and is the set of import paths
to be considered in the search. A "DatabaseImporter" could potentially
function without any concern for a search path. Assuming the importer
does no partitioning, the "path" would be irrelevant. In order to
illustrate the purpose of "path", the example would need to illustrate
a more complex "DatabaseImporter" whose behavior varied depending on
"sys.path"/"PYTHONPATH". In that case, the "find_distributions" should
honor the "context.path" and only yield "Distribution"s pertinent to
that path.

"DatabaseDistribution", then, would look something like:

   class DatabaseDistribution(importlib.metadata.Distribution):
       def __init__(self, record):
           self.record = record

       def read_text(self, filename):
           """
           Read a file like "METADATA" for the current distribution.
           """
           if filename == "METADATA":
               return f"""Name: {self.record.name}
   Version: {self.record.version}
   """
           if filename == "entry_points.txt":
               return "\n".join(
                 f"""[{ep.group}]\n{ep.name}={ep.value}"""
                 for ep in self.record.entry_points)

       def locate_file(self, path):
           raise RuntimeError("This distribution has no file system")

This basic implementation should provide metadata and entry points for
packages served by the "DatabaseImporter", assuming that the "record"
supplies suitable ".name", ".version", and ".entry_points" attributes.

The "DatabaseDistribution" may also provide other metadata files, like
"RECORD" (required for "Distribution.files") or override the
implementation of "Distribution.files". See the source for more
inspiration.
