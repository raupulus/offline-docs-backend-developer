---
title: '"mimetypes" --- Map filenames to MIME types'
source_url: https://docs.python.org/es/3
source_path: library/mimetypes.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3210
---

# "mimetypes" --- Map filenames to MIME types

**Código fuente:** Lib/mimetypes.py

======================================================================

The "mimetypes" module converts between a filename or URL and the MIME
type associated with the filename extension.  Conversions are provided
from filename to MIME type and from MIME type to filename extension;
encodings are not supported for the latter conversion.

El módulo proporciona una clase y varias funciones de conveniencia.
Las funciones son la interfaz normal de este módulo, pero algunas
aplicaciones pueden estar interesadas en la clase también.

Las funciones que se describen a continuación constituyen la interfaz
principal de este módulo. Si el módulo no ha sido inicializado,
llamarán "init()" si se basan en la información que "init()"
establece.

mimetypes.guess_type(url, strict=True)

   Adivina el tipo de un archivo basado en su nombre de archivo, ruta
   o URL, dado por *url*. La URL puede ser una cadena o un objeto
   *path-like object*.

   El valor de retorno es una tupla "(type, encoding)" donde *type* es
   "None" si el tipo no puede ser adivinado (por sufijo ausente o
   desconocido) o una cadena de la forma "type/subtype'", utilizable
   para un encabezado MIME *content-type*.

   *encoding* es "None" para no codificar o el nombre del programa
   usado para codificar (por ejemplo **compress** o **gzip**). La
   codificación es adecuada para ser usada como una cabecera de
   *Content-Encoding*, **no** como una cabecera de *Content-Transfer-
   Encoding*. Los mapeos son conducidos por tablas. Los sufijos de
   codificación son sensibles a las mayúsculas y minúsculas; los
   sufijos de tipo se prueban primero distinguiendo entre mayúsculas y
   minúsculas, y luego sin dicha distinción.

   The optional *strict* argument is a flag specifying whether the
   list of known MIME types is limited to only the official types
   registered with IANA. However, the behavior of this module also
   depends on the underlying operating system. Only file types
   recognized by the OS or explicitly registered with Python's
   internal database can be identified. When *strict* is "True" (the
   default), only the IANA types are supported; when *strict* is
   "False", some additional non-standard but commonly used MIME types
   are also recognized.

   Distinto en la versión 3.8: Added support for *url* being a *path-
   like object*.

   Soft deprecated since version 3.13: Passing a file path instead of
   URL. Use "guess_file_type()" for this.

mimetypes.guess_file_type(path, *, strict=True)

   Guess the type of a file based on its path, given by *path*.
   Similar to the "guess_type()" function, but accepts a path instead
   of URL. Path can be a string, a bytes object or a *path-like
   object*.

   Added in version 3.13.

mimetypes.guess_all_extensions(type, strict=True)

   Guess the extensions for a file based on its MIME type, given by
   *type*. The return value is a list of strings giving all possible
   filename extensions, including the leading dot ("'.'").  The
   extensions are not guaranteed to have been associated with any
   particular data stream, but would be mapped to the MIME type *type*
   by "guess_type()" and "guess_file_type()".

   El argumento opcional *strict* tiene el mismo significado que con
   la función "guess_type()".

mimetypes.guess_extension(type, strict=True)

   Guess the extension for a file based on its MIME type, given by
   *type*. The return value is a string giving a filename extension,
   including the leading dot ("'.'").  The extension is not guaranteed
   to have been associated with any particular data stream, but would
   be mapped to the MIME type *type* by "guess_type()" and
   "guess_file_type()". If no extension can be guessed for *type*,
   "None" is returned.

   El argumento opcional *strict* tiene el mismo significado que con
   la función "guess_type()".

Algunas funciones adicionales y elementos de datos están disponibles
para controlar el comportamiento del módulo.

mimetypes.init(files=None)

   Inicializa las estructuras de datos internos. Si se proporciona
   *files* debe ser una secuencia de nombres de archivos que deben
   utilizarse para aumentar el mapa de tipo por defecto. Si se omite,
   los nombres de archivo a utilizar se toman de "knownfiles"; en
   Windows, se cargan las configuraciones actuales del registro. Cada
   archivo nombrado en *files* o "knownfiles" tiene prioridad sobre
   los nombrados antes de él. Se permite llamar repetidamente a
   "init()".

   Si se especifica una lista vacía para *files* se evitará que se
   apliquen los valores predeterminados del sistema: sólo estarán
   presentes los valores conocidos de una lista incorporada.

   Si *files* es "None" la estructura interna de datos se reconstruye
   completamente a su valor inicial por defecto. Esta es una operación
   estable y producirá los mismos resultados cuando se llame varias
   veces.

   Distinto en la versión 3.2: Anteriormente, la configuración del
   registro de Windows se ignoraba.

mimetypes.read_mime_types(file)

   Load the type map given in the file named by *file*, if it exists.
   *file* must be a string specifying the name of the file to read.
   The type map is returned as a dictionary mapping file extensions,
   including the leading dot ("'.'"), to strings of the form
   "'type/subtype'".  If the file does not exist or cannot be read,
   "None" is returned.

mimetypes.add_type(type, ext, strict=True)

   Añade un mapeo del tipo MIME *type* a la extensión *ext*. Cuando la
   extensión ya se conoce, el nuevo tipo reemplazará al antiguo.
   Cuando el tipo ya se conoce la extensión se añadirá a la lista de
   extensiones conocidas.

   Cuando *strict* es "True" (el valor por defecto), el mapeo se
   añadirá a los tipos MIME oficiales, de lo contrario a los no
   estándar.

mimetypes.inited

   Flag que indica si se han inicializado o no las estructuras de
   datos globales. Esto se establece como "True" por "init()".

mimetypes.knownfiles

   Lista de los nombres de los archivos de mapas de tipo comúnmente
   instalados.  Estos archivos se llaman típicamente  "mime.types" y
   se instalan en diferentes lugares por diferentes paquetes.

mimetypes.suffix_map

   Diccionario que mapea sufijos a sufijos. Se utiliza para permitir
   el reconocimiento de archivos codificados cuya codificación y tipo
   se indican con la misma extensión. Por ejemplo, la extensión ".tgz"
   se mapea a ".tar.gz" para permitir que la codificación y el tipo se
   reconozcan por separado.

mimetypes.encodings_map

   El diccionario mapea las extensiones de los nombres de archivo a
   los tipos de codificación.

mimetypes.types_map

   Diccionario que mapea extensiones de los nombres de archivo a tipos
   MIME.

mimetypes.common_types

   Diccionario que mapea extensiones de los nombres de archivo a tipos
   MIME no estándar, pero comúnmente encontrados.

Un ejemplo de utilización del módulo:

   >>> import mimetypes
   >>> mimetypes.init()
   >>> mimetypes.knownfiles
   ['/etc/mime.types', '/etc/httpd/mime.types', ... ]
   >>> mimetypes.suffix_map['.tgz']
   '.tar.gz'
   >>> mimetypes.encodings_map['.gz']
   'gzip'
   >>> mimetypes.types_map['.tgz']
   'application/x-tar-gz'

## MimeTypes objects

The "MimeTypes" class may be useful for applications which may want
more than one MIME-type database; it provides an interface similar to
the one of the "mimetypes" module.

class mimetypes.MimeTypes(filenames=(), strict=True)

   Esta clase representa una base de datos de tipos MIME. Por defecto,
   proporciona acceso a la misma base de datos que el resto de este
   módulo. La base de datos inicial es una copia de la proporcionada
   por el módulo, y puede ser extendida cargando archivos adicionales
   de tipo "mime.types" en la base de datos usando los métodos
   "read()" o "readfp()". Los diccionarios de mapeo también pueden ser
   borrados antes de cargar datos adicionales si no se desean los
   datos por defecto.

   El parámetro opcional *filenames* puede utilizarse para hacer que
   se carguen archivos adicionales "encima" de la base de datos
   predeterminada.

   suffix_map

      El diccionario mapea sufijos a sufijos. Se utiliza para permitir
      el reconocimiento de archivos codificados cuya codificación y
      tipo se indican con la misma extensión. Por ejemplo, la
      extensión ".tgz" se mapea a ".tar.gz" para permitir que la
      codificación y el tipo se reconozcan por separado. Esto es
      inicialmente una copia del global "suffix_map" definido en el
      módulo.

   encodings_map

      El diccionario mapea las extensiones de los nombres de archivo a
      los tipos de codificación. Es inicialmente una copia del global
      "encodings_map" definido en el módulo.

   types_map

      Una tupla que contiene dos diccionarios, mapeando las
      extensiones de los nombres de archivo a los tipos MIME: el
      primer diccionario es para los tipos no estándar y el segundo
      para los tipos estándar. Están inicializados por "common_types"
      y "types_map".

   types_map_inv

      Una tupla que contiene dos diccionarios, mapeando los tipos MIME
      a una lista de extensiones de nombres de archivos: el primer
      diccionario es para los tipos no estándar y el segundo para los
      tipos estándar. Están inicializados por "common_types" y
      "types_map".

   guess_extension(type, strict=True)

      Similar a la función "guess_extension()", usando las tablas
      almacenadas como parte del objeto.

   guess_type(url, strict=True)

      Similar a la función "guess_type()", usando las tablas
      almacenadas como parte del objeto.

   guess_file_type(path, *, strict=True)

      Similar to the "guess_file_type()" function, using the tables
      stored as part of the object.

      Added in version 3.13.

   guess_all_extensions(type, strict=True)

      Similar a la función "guess_all_extensions()", usando las tablas
      almacenadas como parte del objeto.

   read(filename, strict=True)

      Carga información MIME de un archivo llamado *filename*. Esto
      usa "readfp()" para analizar el archivo.

      Si *strict* es "True", la información se añadirá a la lista de
      tipos estándar, si no a la lista de tipos no estándar.

   readfp(fp, strict=True)

      Carga información de tipo MIME de un archivo abierto *fp*.  El
      archivo debe tener el formato de los archivos estándar
      "mime.types".

      Si *strict* es "True", la información se va a añadir a la lista
      de tipos estándar, de otro modo se añadirá a la lista de tipos
      no estándar.

   read_windows_registry(strict=True)

      Carga información desde el registro de Windows del tipo de
      metadato MIME.

      Availability: Windows.

      Si *strict* es "True", la información se va a añadir a la lista
      de tipos estándar, de otro modo se añadirá a la lista de tipos
      no estándar.

      Added in version 3.2.

   add_type(type, ext, strict=True)

      Add a mapping from the MIME type *type* to the extension *ext*.
      Valid extensions start with a '.' or are empty. When the
      extension is already known, the new type will replace the old
      one. When the type is already known the extension will be added
      to the list of known extensions.

      Cuando *strict* es "True" (el valor por defecto), el mapeo se
      añadirá a los tipos MIME oficiales, de lo contrario a los no
      estándar.

      Deprecated since version 3.14, will be removed in version 3.16:
      Invalid, undotted extensions will raise a "ValueError" in Python
      3.16.

## Command-line usage

The "mimetypes" module can be executed as a script from the command
line.

   python -m mimetypes [-h] [-e] [-l] type [type ...]

The following options are accepted:

-h
--help

   Show the help message and exit.

-e
--extension

   Guess extension instead of type.

-l
--lenient

   Additionally search for some common, but non-standard types.

By default the script converts MIME types to file extensions. However,
if "--extension" is specified, it converts file extensions to MIME
types.

For each "type" entry, the script writes a line into the standard
output stream. If an unknown type occurs, it writes an error message
into the standard output stream and exits with the return code "1".

## Command-line example

Here are some examples of typical usage of the "mimetypes" command-
line interface:

   $ # get a MIME type by a file name
   $ python -m mimetypes filename.png
   type: image/png encoding: None

   $ # get a MIME type by a URL
   $ python -m mimetypes https://example.com/filename.txt
   type: text/plain encoding: None

   $ # get a complex MIME type
   $ python -m mimetypes filename.tar.gz
   type: application/x-tar encoding: gzip

   $ # get a MIME type for a rare file extension
   $ python -m mimetypes filename.pict
   error: media type unknown for filename.pict

   $ # now look in the extended database built into Python
   $ python -m mimetypes --lenient filename.pict
   type: image/pict encoding: None

   $ # get a file extension by a MIME type
   $ python -m mimetypes --extension text/javascript
   .js

   $ # get a file extension by a rare MIME type
   $ python -m mimetypes --extension text/xul
   error: unknown type text/xul

   $ # now look in the extended database again
   $ python -m mimetypes --extension --lenient text/xul
   .xul

   $ # try to feed an unknown file extension
   $ python -m mimetypes filename.sh filename.nc filename.xxx filename.txt
   type: application/x-sh encoding: None
   type: application/x-netcdf encoding: None
   error: media type unknown for filename.xxx
   type: text/plain encoding: None

   $ # try to feed an unknown MIME type
   $ python -m mimetypes --extension audio/aac audio/opus audio/future audio/x-wav
   .aac
   .opus
   error: unknown type audio/future
