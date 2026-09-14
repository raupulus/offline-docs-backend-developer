---
title: '"tarfile" --- Read and write tar archive files'
source_url: https://docs.python.org/es/3
source_path: library/tarfile.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4060
---

# "tarfile" --- Read and write tar archive files

**Código fuente:** Lib/tarfile.py

======================================================================

The "tarfile" module makes it possible to read and write tar archives,
including those using gzip, bz2 and lzma compression. Use the
"zipfile" module to read or write ".zip" files, or the higher-level
functions in shutil.

Algunos hechos y cifras:

* reads and writes "gzip", "bz2", "compression.zstd", and "lzma"
  compressed archives if the respective modules are available.

  If any of these *optional modules* are missing from your copy of
  CPython, look for documentation from your distributor (that is,
  whoever provided Python to you). If you are the distributor, see
  Requirements for optional modules.

* soporte de lectura/escritura para el formato POSIX.1-1988 (ustar).

* soporte de lectura/escritura para el formato GNU tar incluyendo
  extensiones *longname* y *longlink*, soporte de solo escritura para
  todas las variantes de extensiones de *sparse* (archivo disperso)
  incluyendo restablecimiento de archivos dispersos.

* soporte de lectura/escritura para el formato POSIX.1-2001 (pax).

* gestiona directorios, archivos regulares, enlaces duros, enlaces
  simbólicos, fifos, dispositivos de carácter, dispositivos de bloque
  y puede adquirir y restaurar información de archivo como marca de
  tiempo, permisos de acceso y dueño.

Distinto en la versión 3.3: Añadido soporte para compresión "lzma".

Distinto en la versión 3.12: Archives are extracted using a filter,
which makes it possible to either limit surprising/dangerous features,
or to acknowledge that they are expected and the archive is fully
trusted.

Distinto en la versión 3.14: Set the default extraction filter to
"data", which disallows some dangerous features such as links to
absolute paths or paths outside of the destination. Previously, the
filter strategy was equivalent to "fully_trusted".

Distinto en la versión 3.14: Added support for Zstandard compression
using "compression.zstd".

tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)

   Retorna un objeto "TarFile" para el nombre de ruta *name*. Para
   información detallada en los objetos de la clase "TarFile" y los
   argumentos por palabra clave que están permitidos, dirígete a
   Objetos TarFile.

   *mode* tiene que ser una cadena de texto en el formato
   "'filemode[:compression]'", adquiere el valor de "'r'" de forma
   predeterminada. Aquí hay una lista completa de combinaciones de
   modo:

   +--------------------+-----------------------------------------------+
   | modo               | acción                                        |
   |====================|===============================================|
   | "'r'" or "'r:*'"   | Abrir para leer con compresión transparente   |
   |                    | (recomendado).                                |
   +--------------------+-----------------------------------------------+
   | "'r:'"             | Abrir para leer exclusivamente sin            |
   |                    | compresión.                                   |
   +--------------------+-----------------------------------------------+
   | "'r:gz'"           | Abrir para leer con compresión gzip.          |
   +--------------------+-----------------------------------------------+
   | "'r:bz2'"          | Abrir para leer con compresión bzip2.         |
   +--------------------+-----------------------------------------------+
   | "'r:xz'"           | Abrir para leer con compresión lzma.          |
   +--------------------+-----------------------------------------------+
   | "'r:zst'"          | Open for reading with Zstandard compression.  |
   +--------------------+-----------------------------------------------+
   | "'x'" o "'x:'"     | Create a tarfile exclusively without          |
   |                    | compression. Raise a "FileExistsError"        |
   |                    | exception if it already exists.               |
   +--------------------+-----------------------------------------------+
   | "'x:gz'"           | Create a tarfile with gzip compression. Raise |
   |                    | a "FileExistsError" exception if it already   |
   |                    | exists.                                       |
   +--------------------+-----------------------------------------------+
   | "'x:bz2'"          | Create a tarfile with bzip2 compression.      |
   |                    | Raise a "FileExistsError" exception if it     |
   |                    | already exists.                               |
   +--------------------+-----------------------------------------------+
   | "'x:xz'"           | Create a tarfile with lzma compression. Raise |
   |                    | a "FileExistsError" exception if it already   |
   |                    | exists.                                       |
   +--------------------+-----------------------------------------------+
   | "'x:zst'"          | Create a tarfile with Zstandard compression.  |
   |                    | Raise a "FileExistsError" exception if it     |
   |                    | already exists.                               |
   +--------------------+-----------------------------------------------+
   | "'a'" or "'a:'"    | Abrir para anexar sin compresión. El archivo  |
   |                    | se crea si no existe.                         |
   +--------------------+-----------------------------------------------+
   | "'w'" or "'w:'"    | Abrir para escritura con compresión lzma.     |
   +--------------------+-----------------------------------------------+
   | "'w:gz'"           | Abrir para escritura con compresión gzip.     |
   +--------------------+-----------------------------------------------+
   | "'w:bz2'"          | Abrir para escritura con compresión bzip2.    |
   +--------------------+-----------------------------------------------+
   | "'w:xz'"           | Abrir para escritura con compresión lzma.     |
   +--------------------+-----------------------------------------------+
   | "'w:zst'"          | Open for Zstandard compressed writing.        |
   +--------------------+-----------------------------------------------+

   Ten en cuenta que "'a:gz'", "'a:bz2'" or "'a:xz'" no son posibles.
   Si *mode* no es apropiado para abrir ciertos archivos (comprimidos)
   para lectura, se lanza una excepción de tipo "ReadError". Usa el
   *modo* "'r'" para evitar esto. Si el método de compresión no es
   admitido, se lanza una excepción "CompressionError".

   Si *fileobj* es especificado, se utiliza como alternativa a *file
   object* abierto en modo binario para *name*. Debe estar en la
   posición 0.

   For modes "'w:gz'", "'x:gz'", "'w|gz'", "'w:bz2'", "'x:bz2'",
   "'w|bz2'", "tarfile.open()" accepts the keyword argument
   *compresslevel* (default "9") to specify the compression level of
   the file.

   For modes "'w:xz'", "'x:xz'" and "'w|xz'", "tarfile.open()" accepts
   the keyword argument *preset* to specify the compression level of
   the file.

   For modes "'w:zst'", "'x:zst'" and "'w|zst'", "tarfile.open()"
   accepts the keyword argument *level* to specify the compression
   level of the file. The keyword argument *options* may also be
   passed, providing advanced Zstandard compression parameters
   described by "CompressionParameter". The keyword argument
   *zstd_dict* can be passed to provide a "ZstdDict", a Zstandard
   dictionary used to improve compression of smaller amounts of data.

   For special purposes, there is a second format for *mode*:
   "'filemode|[compression]'".  "tarfile.open()" will return a
   "TarFile" object that processes its data as a stream of blocks.  No
   random seeking will be done on the file. If given, *fileobj* may be
   any object that has a "read()" or "write()" method (depending on
   the *mode*) that works with bytes. *bufsize* specifies the
   blocksize and defaults to "20 * 512" bytes. Use this variant in
   combination with e.g. "sys.stdin.buffer", a socket *file object* or
   a tape device. However, such a "TarFile" object is limited in that
   it does not allow random access, see Ejemplos.  The currently
   possible modes:

   +---------------+----------------------------------------------+
   | Modo          | Acción                                       |
   |===============|==============================================|
   | "'r|*'"       | Abre un *stream* de bloques tar para leer    |
   |               | con compresión transparente.                 |
   +---------------+----------------------------------------------+
   | "'r|'"        | Abre un *stream* de bloques tar sin          |
   |               | comprimir para lectura.                      |
   +---------------+----------------------------------------------+
   | "'r|gz'"      | Abre un *stream* comprimido con gzip para    |
   |               | lectura.                                     |
   +---------------+----------------------------------------------+
   | "'r|bz2'"     | Abre un *stream* bzip2 comprimido para       |
   |               | lectura.                                     |
   +---------------+----------------------------------------------+
   | "'r|xz'"      | Abre un *stream* lzma comprimido para        |
   |               | lectura.                                     |
   +---------------+----------------------------------------------+
   | "'r|zst'"     | Open a Zstandard compressed *stream* for     |
   |               | reading.                                     |
   +---------------+----------------------------------------------+
   | "'w|'"        | Abre un *stream* sin comprimir para          |
   |               | escritura.                                   |
   +---------------+----------------------------------------------+
   | "'w|gz'"      | Abre un *stream* gzip comprimido para        |
   |               | escritura.                                   |
   +---------------+----------------------------------------------+
   | "'w|bz2'"     | Abre un *stream* bzip2 comprimido para       |
   |               | escritura.                                   |
   +---------------+----------------------------------------------+
   | "'w|xz'"      | Abre un *stream* lzma comprimido para        |
   |               | escritura.                                   |
   +---------------+----------------------------------------------+
   | "'w|zst'"     | Open a Zstandard compressed *stream* for     |
   |               | writing.                                     |
   +---------------+----------------------------------------------+

   Distinto en la versión 3.5: El modo "'x'" (creación exclusiva) fue
   añadido.

   Distinto en la versión 3.6: El parámetro *name* acepta un objeto
   *path-like object*.

   Distinto en la versión 3.12: The *compresslevel* keyword argument
   also works for streams.

   Distinto en la versión 3.14: The *preset* keyword argument also
   works for streams.

class tarfile.TarFile

   Clase para leer y escribir archivos tar. No utilices esta clase
   directamente; usa "tarfile.open()" en su lugar. Consulta Objetos
   TarFile.

tarfile.is_tarfile(name)

   Return "True" if *name* is a tar archive file, that the "tarfile"
   module can read. *name* may be a "str", file, or file-like object.

   Distinto en la versión 3.9: Soporte para archivos y objetos
   similares a archivos.

The "tarfile" module defines the following exceptions:

exception tarfile.TarError

   Base class for all "tarfile" exceptions.

exception tarfile.ReadError

   Is raised when a tar archive is opened, that either cannot be
   handled by the "tarfile" module or is somehow invalid.

exception tarfile.CompressionError

   Se lanza cuando un método de compresión no tiene soporte o cuando
   la información no puede ser decodificada de manera apropiada.

exception tarfile.StreamError

   Se lanza para limitaciones que son comunes para objetos *stream-
   like* "TarFile".

exception tarfile.ExtractError

   Se lanza para errores no fatales cuando se utiliza
   "TarFile.extract()", pero solo si "TarFile.errorlevel""== 2".

exception tarfile.HeaderError

   Se lanza por "TarInfo.frombuf()" si el buffer que obtiene es
   invalido.

exception tarfile.FilterError

   Base class for members refused by filters.

   tarinfo

      Information about the member that the filter refused to extract,
      as TarInfo.

exception tarfile.AbsolutePathError

   Raised to refuse extracting a member with an absolute path.

exception tarfile.OutsideDestinationError

   Raised to refuse extracting a member outside the destination
   directory.

exception tarfile.SpecialFileError

   Raised to refuse extracting a special file (e.g. a device or pipe).

exception tarfile.AbsoluteLinkError

   Raised to refuse extracting a symbolic link with an absolute path.

exception tarfile.LinkOutsideDestinationError

   Raised to refuse extracting a symbolic link pointing outside the
   destination directory.

exception tarfile.LinkFallbackError

   Raised to refuse emulating a link (hard or symbolic) by extracting
   another archive member, when that member would be rejected by the
   filter location. The exception that was raised to reject the
   replacement member is available as "BaseException.__context__".

   Added in version 3.14.

Las siguientes constantes están disponibles a nivel de módulo:

tarfile.ENCODING

   La codificación para caracteres predeterminada: "'utf-8'" en
   Windows, de otra manera, el valor retornado por
   "sys.getfilesystemencoding()".

tarfile.REGTYPE
tarfile.AREGTYPE

   A regular file "type".

tarfile.LNKTYPE

   A link (inside tarfile) "type".

tarfile.SYMTYPE

   A symbolic link "type".

tarfile.CHRTYPE

   A character special device "type".

tarfile.BLKTYPE

   A block special device "type".

tarfile.DIRTYPE

   A directory "type".

tarfile.FIFOTYPE

   A FIFO special device "type".

tarfile.CONTTYPE

   A contiguous file "type".

tarfile.GNUTYPE_LONGNAME

   A GNU tar longname "type".

tarfile.GNUTYPE_LONGLINK

   A GNU tar longlink "type".

tarfile.GNUTYPE_SPARSE

   A GNU tar sparse file "type".

Each of the following constants defines a tar archive format that the
"tarfile" module is able to create. See section Formatos tar con
soporte for details.

tarfile.USTAR_FORMAT

   Formato POSIX.1-1988 (ustar).

tarfile.GNU_FORMAT

   Formato GNU tar.

tarfile.PAX_FORMAT

   Formato POSIX.1-2001 (pax).

tarfile.DEFAULT_FORMAT

   El formato predeterminado para crear archivos. Es actualmente
   "PAX_FORMAT".

   Distinto en la versión 3.8: El formato predeterminado para nuevos
   archivos fue cambiado de "GNU_FORMAT" a "PAX_FORMAT".

Ver también:

  Módulo "zipfile"
     Documentación del módulo estándar "zipfile".

  Operaciones de archivado
     Documentación para las facilidades de archivos de más alto nivel
     proporcionadas por el módulo estándar "shutil".

  Manual GNU tar, formato básico tar
     Documentación para archivos de tipo tar, incluyendo extensiones
     GNU tar.

## Objetos *TarFile*

El objeto "TarFile" provee una interfaz a un archivo tar. Un archivo
tar es una secuencia de bloques. Un miembro de archivos (un archivo
almacenado) está hecho de un bloque de encabezado seguido de bloques
de datos. Es posible almacenar un archivo dentro de un tar múltiples
veces. Cada archivo miembro está representado por un objeto "TarInfo",
consulta Objetos TarInfo para más detalles.

Un objeto "TarFile" puede ser usado como un administrador de contexto
en una declaración "with". Será automáticamente cerrado cuando el
bloque sea completado. Ten en cuenta que en el evento de una excepción
un archivo abierto para escritura no será terminado; solo el objeto de
archivo interno será cerrado. Consulta la sección Ejemplos para un
caso de uso.

Added in version 3.2: Añadido soporte para el protocolo de
administración de contexto.

class tarfile.TarFile(name=None, mode='r', fileobj=None, format=DEFAULT_FORMAT, tarinfo=TarInfo, dereference=False, ignore_zeros=False, encoding=ENCODING, errors='surrogateescape', pax_headers=None, debug=0, errorlevel=1, stream=False)

   Los siguientes argumentos son opcionales y también se pueden
   acceder como atributos de instancia.

   *name* is the pathname of the archive. *name* may be a *path-like
   object*. It can be omitted if *fileobj* is given. In this case, the
   file object's "name" attribute is used if it exists.

   *mode* puede ser "'r'" para leer desde un archivo existente, "'a'"
   para adjuntar datos a un archivo existente,``'w'`` para crear un
   nuevo archivo sobrescribiendo uno existente, o "'x'" para crear un
   nuevo archivo únicamente si este no existe.

   Si *fileobj* es proporcionado, se utiliza para escritura o lectura
   de datos. Si puede ser determinado, *mode* puede ser anulado por el
   modo de *fileobj*. *fileobj* será usado desde la posición 0.

   Nota:

     *fileobj* no se cierra cuando "TarFile" se cierra.

   *format* controla el formato de archivo para la escritura. Debe ser
   una de las constantes "USTAR_FORMAT", "GNU_FORMAT" o "PAX_FORMAT"
   que se definen a nivel de módulo. Al leer, el formato se detectará
   automáticamente, incluso si hay diferentes formatos en un solo
   archivo.

   El argumento *tarinfo* puede ser utilizado para reemplazar la clase
   predeterminada "TarInfo" con una diferente.

   Si *dereference* tiene el valor de "False", añade enlaces
   simbólicos y duros al archivo. Si tiene el valor de "True", añade
   el contenido de archivos objetivo al archivo. Esto no tiene ningún
   efecto en los sistemas que no admiten enlaces simbólicos.

   Si *ignore_zeros* tiene el valor de "False", trata un bloque vacío
   como el final del archivo. Si es "True", omite los bloques vacíos
   (y no válidos) e intenta obtener tantos miembros como sea posible.
   Esto solo es útil para leer archivos concatenados o dañados.

   *debug* puede ser establecido con valores desde "0" (sin mensajes
   de depuración) hasta "3" (todos los mensajes de depuración). Los
   mensajes son escritos en "sys.stderr".

   *errorlevel* controls how extraction errors are handled, see "the
   corresponding attribute".

   Los argumentos *encoding* y *errors* definen la codificación de
   caracteres que se utilizará para lectura o escritura del archivo y
   como los errores de conversión van a ser manejados. La
   configuración predeterminada funcionará para la mayoría de los
   usuarios. Mira la sección Problemas unicode para más información a
   detalle.

   El argumento *pax_headers* es un diccionario opcional de cadenas
   las cuales serán añadidas como un encabezado pax global si el valor
   de *format* es "PAX_FORMAT".

   If *stream* is set to "True" then while reading the archive info
   about files in the archive are not cached, saving memory.

   Distinto en la versión 3.2: Utiliza "'surrogateescape'" como valor
   predeterminado del argumento *errors*.

   Distinto en la versión 3.5: El modo "'x'" (creación exclusiva) fue
   añadido.

   Distinto en la versión 3.6: El parámetro *name* acepta un objeto
   *path-like object*.

   Distinto en la versión 3.13: Add the *stream* parameter.

classmethod TarFile.open(...)

   Constructor alternativo. La función "tarfile.open()" es un acceso
   directo a este método de la clase.

TarFile.getmember(name)

   Retorna un objeto "TarInfo" para el miembro *name*. Si *name* no
   puede ser encontrado, entonces una excepción de tipo "KeyError"
   será lanzada.

   Nota:

     Si un miembro aparece más de una vez en el archivo, se asume que
     su última aparición es la versión más actualizada.

TarFile.getmembers()

   Retorna los miembros del archivo como una lista de objetos
   "TarInfo". La lista tiene el mismo orden que los miembros del
   archivo.

TarFile.getnames()

   Retorna los miembros como una lista de sus nombres. Tiene el mismo
   orden que la lista retornada por "getmembers()".

TarFile.list(verbose=True, *, members=None)

   Imprime en "sys.stdout" una tabla de contenidos. Si *verbose* es
   "False", solo los nombres de los miembros son impresos. si es
   "True", se produce una salida de impresión similar a la de **ls
   -l**. Si el parámetro *members* es proporcionado, debe ser un
   subconjunto de la lista retornada por "getmembers()".

   Distinto en la versión 3.5: Se agregó el parámetro *members*.

TarFile.next()

   Retorna el siguiente miembro del archivo como un objeto "TarInfo"
   cuando "TarFile" se abre para lectura. Retorna "None" si no hay más
   miembros disponibles.

TarFile.extractall(path='.', members=None, *, numeric_owner=False, filter=None)

   Extrae todos los miembros de un archivo al directorio de trabajo
   actual o al directorio de *path*. Si se proporciona el parámetro
   opcional *members*, debe ser un subconjunto de la lista retornada
   por el método "getmembers()". Información de directorio como dueño,
   fecha de modificación y permisos son establecidos una vez que todos
   los miembros han sido extraídos. Esto se realiza para trabajar con
   dos problemáticas: La fecha de modificación de un directorio es
   modificada cada vez que un archivo es creado en el. Y si los
   permisos de un directorio no permiten escritura, extraer archivos
   en el no será posible.

   Si *numeric_owner* tiene el valor de "True", los números uid y gid
   del archivo tar se utilizan para establecer el dueño/grupo de los
   archivos extraídos. De lo contrario, se utilizan los valores
   nombrados del archivo tar.

   The *filter* argument specifies how "members" are modified or
   rejected before extraction. See Extraction filters for details. It
   is recommended to set this explicitly only if specific *tar*
   features are required, or as "filter='data'" to support Python
   versions with a less secure default (3.13 and lower).

   Advertencia:

     Never extract archives from untrusted sources without prior
     inspection.Since Python 3.14, the default ("data") will prevent
     the most dangerous security issues. However, it will not prevent
     *all* unintended or insecure behavior. Read the Extraction
     filters section for details.

   Distinto en la versión 3.5: Se agregó el parámetro *numeric_owner*.

   Distinto en la versión 3.6: El parámetro *path* acepta a *path-like
   object*.

   Distinto en la versión 3.12: Se agregó el parámetro *filter*.

   Distinto en la versión 3.14: The *filter* parameter now defaults to
   "'data'".

TarFile.extract(member, path='', set_attrs=True, *, numeric_owner=False, filter=None)

   Extrae un miembro del archivo al directorio de trabajo actual
   utilizando su nombre completo. La información de su archivo se
   extrae con la mayor precisión posible. *member* puede ser un nombre
   de archivo o un objeto "TarInfo". Puedes especificar un directorio
   diferente utilizando *path*. *path* puede ser un *path-like
   object*. Los atributos de archivo (dueño, fecha de modificación,
   modo) son establecidos a no ser que *set_attrs* sea falso.

   The *numeric_owner* and *filter* arguments are the same as for
   "extractall()".

   Nota:

     El método "extract()" no cuida de varios problemas de extracción.
     En la mayoría de los casos deberías considerar utilizar el método
     "extractall()".

   Advertencia:

     Never extract archives from untrusted sources without prior
     inspection. See the warning for "extractall()" for details.

   Distinto en la versión 3.2: Se agregó el parámetro *set_attrs*.

   Distinto en la versión 3.5: Se agregó el parámetro *numeric_owner*.

   Distinto en la versión 3.6: El parámetro *path* acepta a *path-like
   object*.

   Distinto en la versión 3.12: Se agregó el parámetro *filter*.

TarFile.extractfile(member)

   Extrae un miembro del archivo como un objeto de archivo. *member*
   puede ser un nombre de archivo o un objeto "TarInfo". Si *member*
   es un archivo normal o un enlace, se retorna un objeto
   "io.BufferedReader". Para todos los demás miembros existentes, se
   retorna "None". Si *member* no aparece en el archivo, se lanza
   "KeyError".

   Distinto en la versión 3.3: Retorna un objeto "io.BufferedReader".

   Distinto en la versión 3.13: The returned "io.BufferedReader"
   object has the "mode" attribute which is always equal to "'rb'".

TarFile.errorlevel: int

   If *errorlevel* is "0", errors are ignored when using
   "TarFile.extract()" and "TarFile.extractall()". Nevertheless, they
   appear as error messages in the debug output when *debug* is
   greater than 0. If "1" (the default), all *fatal* errors are raised
   as "OSError" or "FilterError" exceptions. If "2", all *non-fatal*
   errors are raised as "TarError" exceptions as well.

   Some exceptions, e.g. ones caused by wrong argument types or data
   corruption, are always raised.

   Custom extraction filters should raise "FilterError" for *fatal*
   errors and "ExtractError" for *non-fatal* ones.

   Note that when an exception is raised, the archive may be partially
   extracted. It is the user’s responsibility to clean up.

TarFile.extraction_filter

   Added in version 3.12.

   The extraction filter used as a default for the *filter* argument
   of "extract()" and "extractall()".

   The attribute may be "None" or a callable. String names are not
   allowed for this attribute, unlike the *filter* argument to
   "extract()".

   If "extraction_filter" is "None" (the default), extraction methods
   will use the "data" filter by default.

   The attribute may be set on instances or overridden in subclasses.
   It also is possible to set it on the "TarFile" class itself to set
   a global default, although, since it affects all uses of *tarfile*,
   it is best practice to only do so in top-level applications or
   "site configuration". To set a global default this way, a filter
   function needs to be wrapped in "@staticmethod" to prevent
   injection of a "self" argument.

   Distinto en la versión 3.14: The default filter is set to "data",
   which disallows some dangerous features such as links to absolute
   paths or paths outside of the destination. Previously, the default
   was equivalent to "fully_trusted".

TarFile.add(name, arcname=None, recursive=True, *, filter=None)

   Añade el archivo *name* al archivo. *name* puede ser cualquier tipo
   de archivo (directorio, fifo, enlace simbólico, etc.). Si se
   proporciona, *arcname* especifica un nombre alternativo para el
   archivo en el archivo. Los directorios se agregan de forma
   recursiva de forma predeterminada. Esto se puede evitar
   estableciendo *recursive* con el valor de "False". La recursividad
   agrega entradas en orden ordenado. Si se proporciona *filter*,
   debería ser una función que tome un argumento de objeto "TarInfo" y
   retorna el objeto "TarInfo" modificado. Si en cambio retorna
   "None", el objeto "TarInfo" será excluido del archivo. Consulta
   Ejemplos para ver un ejemplo.

   Distinto en la versión 3.2: Se agregó el parámetro *filter*.

   Distinto en la versión 3.7: La recursividad agrega entradas en
   orden ordenado.

TarFile.addfile(tarinfo, fileobj=None)

   Add the "TarInfo" object *tarinfo* to the archive. If *tarinfo*
   represents a non zero-size regular file, the *fileobj* argument
   should be a *binary file*, and "tarinfo.size" bytes are read from
   it and added to the archive.  You can create "TarInfo" objects
   directly, or by using "gettarinfo()".

   Distinto en la versión 3.13: *fileobj* must be given for non-zero-
   sized regular files.

TarFile.gettarinfo(name=None, arcname=None, fileobj=None)

   Crea un objeto "TarInfo" a partir del resultado de "os.stat()" o
   equivalente en un archivo existente. El archivo es nombrado por
   *name* o especificado como un objeto *file object* *fileobj* con un
   descriptor de archivo. *name* puede ser un objeto *path-like
   object*. Si es proporcionado, *arcname* especifica un nombre
   alternativo para el archivo en el archivo, de otra forma, el nombre
   es tomado del atributo *fileobj*’s "name", o el argumento *name*.
   El nombre puede ser una cadena de texto.

   Puedes modificar algunos de los atributos de la clase "TarInfo"’
   antes de que lo añadas utilizado el método "addfile()". Si el
   archivo objeto no es un archivo objeto ordinario posicionado al
   principio del archivo, atributos como "size" puede que necesiten
   modificaciones. Este es el caso para objetos como "GzipFile". El
   atributo "name" también puede ser modificado, en cuyo caso
   *arcname* podría ser una cadena ficticia.

   Distinto en la versión 3.6: El parámetro *name* acepta un objeto
   *path-like object*.

TarFile.close()

   Cierra "TarFile". En el modo de escritura, se añaden dos bloques de
   cero de finalización al archivo.

TarFile.pax_headers: dict

   Un diccionario que contiene pares claves-valor de los encabezados
   globales pax.

## Objetos TarInfo

Un objeto "TarInfo" representa un miembro en "TarFile". Además de
almacenar todos los atributos requeridos de un archivo (como tipo de
archivo, tamaño, fecha, permisos, dueño, etc.), provee de algunos
métodos útiles para determinar su tipo. No contiene los datos del
archivo por si mismo.

"TarInfo" objects are returned by "TarFile"'s methods "getmember()",
"getmembers()" and "gettarinfo()".

Modifying the objects returned by "getmember()" or "getmembers()" will
affect all subsequent operations on the archive. For cases where this
is unwanted, you can use "copy.copy()" or call the "replace()" method
to create a modified copy in one step.

Several attributes can be set to "None" to indicate that a piece of
metadata is unused or unknown. Different "TarInfo" methods handle
"None" differently:

* The "extract()" or "extractall()" methods will ignore the
  corresponding metadata, leaving it set to a default.

* "addfile()" will fail.

* "list()" will print a placeholder string.

class tarfile.TarInfo(name='')

   Crea un objeto "TarInfo".

classmethod TarInfo.frombuf(buf, encoding, errors)

   Crea y retorna un objeto "TarInfo".

   Lanza una excepción "HeaderError" si el buffer es invalido.

classmethod TarInfo.fromtarfile(tarfile)

   Lee el siguiente miembro del objeto de la clase "TarFile" *tarfile*
   y lo retorna como un objeto "TarInfo".

TarInfo.tobuf(format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape')

   Crear un *buffer* de cadena a partir de un objeto "TarInfo". Para
   información sobre los argumentos consulta el constructor de la
   clase "TarFile".

   Distinto en la versión 3.2: Utiliza "'surrogateescape'" como valor
   predeterminado del argumento *errors*.

Un objeto "TarInfo" tiene los siguientes atributos de dato públicos:

TarInfo.name: str

   Nombre del archivo miembro.

TarInfo.size: int

   Tamaño en bytes.

TarInfo.mtime: int | float

   Time of last modification in seconds since the epoch, as in
   "os.stat_result.st_mtime".

   Distinto en la versión 3.12: Can be set to "None" for "extract()"
   and "extractall()", causing extraction to skip applying this
   attribute.

TarInfo.mode: int

   Permission bits, as for "os.chmod()".

   Distinto en la versión 3.12: Can be set to "None" for "extract()"
   and "extractall()", causing extraction to skip applying this
   attribute.

TarInfo.type

   Tipo de archivo. *type* es por lo general una de las siguientes
   constantes: "REGTYPE", "AREGTYPE", "LNKTYPE", "SYMTYPE", "DIRTYPE",
   "FIFOTYPE", "CONTTYPE", "CHRTYPE", "BLKTYPE", "GNUTYPE_SPARSE".
   Para determinar el tipo de un objeto "TarInfo" de forma más
   conveniente, utiliza los métodos "is*()" de abajo.

TarInfo.linkname: str

   Nombre del archivo objetivo, el cual solo está presente en los
   objetos "TarInfo" de tipo "LNKTYPE" y del tipo "SYMTYPE".

   For symbolic links ("SYMTYPE"), the *linkname* is relative to the
   directory that contains the link. For hard links ("LNKTYPE"), the
   *linkname* is relative to the root of the archive.

TarInfo.uid: int

   ID de usuario que originalmente almacenó este miembro.

   Distinto en la versión 3.12: Can be set to "None" for "extract()"
   and "extractall()", causing extraction to skip applying this
   attribute.

TarInfo.gid: int

   ID de grupo del usuario que originalmente almacenó este miembro.

   Distinto en la versión 3.12: Can be set to "None" for "extract()"
   and "extractall()", causing extraction to skip applying this
   attribute.

TarInfo.uname: str

   Nombre de usuario.

   Distinto en la versión 3.12: Can be set to "None" for "extract()"
   and "extractall()", causing extraction to skip applying this
   attribute.

TarInfo.gname: str

   Nombre del grupo.

   Distinto en la versión 3.12: Can be set to "None" for "extract()"
   and "extractall()", causing extraction to skip applying this
   attribute.

TarInfo.chksum: int

   Header checksum.

TarInfo.devmajor: int

   Device major number.

TarInfo.devminor: int

   Device minor number.

TarInfo.offset: int

   The tar header starts here.

TarInfo.offset_data: int

   The file's data starts here.

TarInfo.sparse

   Sparse member information.

TarInfo.pax_headers: dict

   Un diccionario que contiene pares *key-value* de un encabezado *pax
   extended*.

TarInfo.replace(name=..., mtime=..., mode=..., linkname=..., uid=..., gid=..., uname=..., gname=..., deep=True)

   Added in version 3.12.

   Return a *new* copy of the "TarInfo" object with the given
   attributes changed. For example, to return a "TarInfo" with the
   group name set to "'staff'", use:

      new_tarinfo = old_tarinfo.replace(gname='staff')

   By default, a deep copy is made. If *deep* is false, the copy is
   shallow, i.e. "pax_headers" and any custom attributes are shared
   with the original "TarInfo" object.

Un objeto "TarInfo" también provee de algunos métodos de consulta
convenientes:

TarInfo.isfile()

   Return "True" if the "TarInfo" object is a regular file.

TarInfo.isreg()

   Igual que "isfile()".

TarInfo.isdir()

   Retorna "True" si es un directorio.

TarInfo.issym()

   Retorna "True" si es un enlace simbólico.

TarInfo.islnk()

   Retorna "True" si es un enlace duro.

TarInfo.ischr()

   Retorna "True" si es un dispositivo de caracter.

TarInfo.isblk()

   Retorna "True" si es un dispositivo de bloque.

TarInfo.isfifo()

   Retorna "True" si es un FIFO.

TarInfo.isdev()

   Retorna "True" si es uno de los caracteres de dispositivo,
   dispositivo de bloque o FIFO.

## Extraction filters

Added in version 3.12.

The *tar* format is designed to capture all details of a UNIX-like
filesystem, which makes it very powerful. Unfortunately, the features
make it easy to create tar files that have unintended -- and possibly
malicious -- effects when extracted. For example, extracting a tar
file can overwrite arbitrary files in various ways (e.g.  by using
absolute paths, ".." path components, or symlinks that affect later
members).

In most cases, the full functionality is not needed. Therefore,
*tarfile* supports extraction filters: a mechanism to limit
functionality, and thus mitigate some of the security issues.

Advertencia:

  None of the available filters blocks *all* dangerous archive
  features. Never extract archives from untrusted sources without
  prior inspection. See also Hints for further verification.

Ver también:

  **PEP 706**
     Contains further motivation and rationale behind the design.

The *filter* argument to "TarFile.extract()" or "extractall()" can be:

* the string "'fully_trusted'": Honor all metadata as specified in the
  archive. Should be used if the user trusts the archive completely,
  or implements their own complex verification.

* the string "'tar'": Honor most *tar*-specific features (i.e.
  features of UNIX-like filesystems), but block features that are very
  likely to be surprising or malicious. See "tar_filter()" for
  details.

* the string "'data'": Ignore or block most features specific to UNIX-
  like filesystems. Intended for extracting cross-platform data
  archives. See "data_filter()" for details.

* "None" (default): Use "TarFile.extraction_filter".

  If that is also "None" (the default), the "'data'" filter will be
  used.

     Distinto en la versión 3.14: The default filter is set to "data".
     Previously, the default was equivalent to "fully_trusted".

* A callable which will be called for each extracted member with a
  TarInfo describing the member and the destination path to where the
  archive is extracted (i.e. the same path is used for all members):

     filter(member: TarInfo, path: str, /) -> TarInfo | None

  The callable is called just before each member is extracted, so it
  can take the current state of the disk into account. It can:

  * return a "TarInfo" object which will be used instead of the
    metadata in the archive, or

  * return "None", in which case the member will be skipped, or

  * raise an exception to abort the operation or skip the member,
    depending on "errorlevel". Note that when extraction is aborted,
    "extractall()" may leave the archive partially extracted. It does
    not attempt to clean up.

### Default named filters

The pre-defined, named filters are available as functions, so they can
be reused in custom filters:

tarfile.fully_trusted_filter(member, path)

   Return *member* unchanged.

   This implements the "'fully_trusted'" filter.

tarfile.tar_filter(member, path)

   Implements the "'tar'" filter.

   * Strip leading slashes ("/" and "os.sep") from filenames.

   * Refuse to extract files with absolute paths (in case the name is
     absolute even after stripping slashes, e.g. "C:/foo" on Windows).
     This raises "AbsolutePathError".

   * Refuse to extract files whose absolute path (after following
     symlinks) would end up outside the destination. This raises
     "OutsideDestinationError".

   * Clear high mode bits (setuid, setgid, sticky) and group/other
     write bits ("S_IWGRP" | "S_IWOTH").

   Return the modified "TarInfo" member.

tarfile.data_filter(member, path)

   Implements the "'data'" filter. In addition to what "tar_filter"
   does:

   * Normalize link targets ("TarInfo.linkname") using
     "os.path.normpath()". Note that this removes internal ".."
     components, which may change the meaning of the link if the path
     in "TarInfo.linkname" traverses symbolic links.

   * Refuse to extract links (hard or soft) that link to absolute
     paths, or ones that link outside the destination.

     This raises "AbsoluteLinkError" or "LinkOutsideDestinationError".

     Note that such files are refused even on platforms that do not
     support symbolic links.

   * Refuse to extract device files (including pipes). This raises
     "SpecialFileError".

   * For regular files, including hard links:

     * Set the owner read and write permissions ("S_IRUSR" |
       "S_IWUSR").

     * Remove the group & other executable permission ("S_IXGRP" |
       "S_IXOTH") if the owner doesn’t have it ("S_IXUSR").

   * For other files (directories), set "mode" to "None", so that
     extraction methods skip applying permission bits.

   * Set user and group info ("uid", "gid", "uname", "gname") to
     "None", so that extraction methods skip setting it.

   Return the modified "TarInfo" member.

   Note that this filter does not block *all* dangerous archive
   features. See Hints for further verification  for details.

   Distinto en la versión 3.14: Link targets are now normalized.

### Filter errors

When a filter refuses to extract a file, it will raise an appropriate
exception, a subclass of "FilterError". This will abort the extraction
if "TarFile.errorlevel" is 1 or more. With "errorlevel=0" the error
will be logged and the member will be skipped, but extraction will
continue.

### Hints for further verification

Even with "filter='data'", *tarfile* is not suited for extracting
untrusted files without prior inspection. Among other issues, the pre-
defined filters do not prevent denial-of-service attacks. Users should
do additional checks.

Here is an incomplete list of things to consider:

* Extract to a "new temporary directory" to prevent e.g. exploiting
  pre-existing links, and to make it easier to clean up after a failed
  extraction.

* Disallow symbolic links if you do not need the functionality.

* When working with untrusted data, use external (e.g. OS-level)
  limits on disk, memory and CPU usage.

* Check filenames against an allow-list of characters (to filter out
  control characters, confusables, foreign path separators, and so
  on).

* Check that filenames have expected extensions (discouraging files
  that execute when you “click on them”, or extension-less files like
  Windows special device names).

* Limit the number of extracted files, total size of extracted data,
  filename length (including symlink length), and size of individual
  files.

* Check for files that would be shadowed on case-insensitive
  filesystems.

Also note that:

* Tar files may contain multiple versions of the same file. Later ones
  are expected to overwrite any earlier ones. This feature is crucial
  to allow updating tape archives, but can be abused maliciously.

* *tarfile* does not protect against issues with “live” data, e.g. an
  attacker tinkering with the destination (or source) directory while
  extraction (or archiving) is in progress.

### Supporting older Python versions

Extraction filters were added to Python 3.12, but may be backported to
older versions as security updates. To check whether the feature is
available, use e.g. "hasattr(tarfile, 'data_filter')" rather than
checking the Python version.

The following examples show how to support Python versions with and
without the feature. Note that setting "extraction_filter" will affect
any subsequent operations.

* Fully trusted archive:

     my_tarfile.extraction_filter = (lambda member, path: member)
     my_tarfile.extractall()

* Use the "'data'" filter if available, but revert to Python 3.11
  behavior ("'fully_trusted'") if this feature is not available:

     my_tarfile.extraction_filter = getattr(tarfile, 'data_filter',
                                            (lambda member, path: member))
     my_tarfile.extractall()

* Use the "'data'" filter; *fail* if it is not available:

     my_tarfile.extractall(filter=tarfile.data_filter)

  or:

     my_tarfile.extraction_filter = tarfile.data_filter
     my_tarfile.extractall()

* Use the "'data'" filter; *warn* if it is not available:

     if hasattr(tarfile, 'data_filter'):
         my_tarfile.extractall(filter='data')
     else:
         # remove this when no longer needed
         warn_the_user('Extracting may be unsafe; consider updating Python')
         my_tarfile.extractall()

### Stateful extraction filter example

While *tarfile*'s extraction methods take a simple *filter* callable,
custom filters may be more complex objects with an internal state. It
may be useful to write these as context managers, to be used like
this:

   with StatefulFilter() as filter_func:
       tar.extractall(path, filter=filter_func)

Such a filter can be written as, for example:

   class StatefulFilter:
       def __init__(self):
           self.file_count = 0

       def __enter__(self):
           return self

       def __call__(self, member, path):
           self.file_count += 1
           return member

       def __exit__(self, *exc_info):
           print(f'{self.file_count} files extracted')

## Interfaz de línea de comandos

Added in version 3.4.

The "tarfile" module provides a simple command-line interface to
interact with tar archives.

Si quieres crear un nuevo archivo tar, especifica su nombre después de
la opción "-c" y después lista el nombre de archivo(s) que deberían
ser incluidos:

   $ python -m tarfile -c monty.tar  spam.txt eggs.txt

Proporcionar un directorio también es aceptable:

   $ python -m tarfile -c monty.tar life-of-brian_1979/

Si deseas extraer un archivo tar en el directorio actual, utiliza la
opción "-e":

   $ python -m tarfile -e monty.tar

También puedes extraer un archivo tar en un directorio diferente
pasando el nombre del directorio como parámetro:

   $ python -m tarfile -e monty.tar  other-dir/

Para obtener una lista de archivos dentro de un archivo tar, utiliza
la opción  "-l":

   $ python -m tarfile -l monty.tar

### Opciones de línea de comandos

-l <tarfile>
--list <tarfile>

   Listar archivos en un tar.

-c <tarfile> <source1> ... <sourceN>
--create <tarfile> <source1> ... <sourceN>

   Crear archivo tar desde archivos fuente.

-e <tarfile> [<output_dir>]
--extract <tarfile> [<output_dir>]

   Extrae el archivo tar en el directorio actual si *output_dir* no es
   especificado.

-t <tarfile>
--test <tarfile>

   Probar si el archivo tar es valido o no.

-v, --verbose

   Output *verbose*.

--filter <filtername>

   Specifies the *filter* for "--extract". See Extraction filters for
   details. Only string names are accepted (that is, "fully_trusted",
   "tar", and "data").

## Ejemplos

### Reading examples

Cómo extraer un archivo tar entero al directorio de trabajo actual:

   import tarfile
   tar = tarfile.open("sample.tar.gz")
   tar.extractall(filter='data')
   tar.close()

Cómo extraer un subconjunto de un archivo tar con
"TarFile.extractall()" utilizando una función generadora en lugar de
una lista:

   import os
   import tarfile

   def py_files(members):
       for tarinfo in members:
           if os.path.splitext(tarinfo.name)[1] == ".py":
               yield tarinfo

   tar = tarfile.open("sample.tar.gz")
   tar.extractall(members=py_files(tar))
   tar.close()

Cómo leer un archivo tar comprimido con gzip y desplegar un poco de
información del miembro:

   import tarfile
   tar = tarfile.open("sample.tar.gz", "r:gz")
   for tarinfo in tar:
       print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end="")
       if tarinfo.isreg():
           print("a regular file.")
       elif tarinfo.isdir():
           print("a directory.")
       else:
           print("something else.")
   tar.close()

### Writing examples

Cómo crear un archivo tar sin comprimir desde una lista de nombres de
archivo:

   import tarfile
   tar = tarfile.open("sample.tar", "w")
   for name in ["foo", "bar", "quux"]:
       tar.add(name)
   tar.close()

El mismo ejemplo utilizando la declaración "with":

   import tarfile
   with tarfile.open("sample.tar", "w") as tar:
       for name in ["foo", "bar", "quux"]:
           tar.add(name)

How to create and write an archive to stdout using "sys.stdout.buffer"
in the *fileobj* parameter in "TarFile.add()":

   import sys
   import tarfile
   with tarfile.open("sample.tar.gz", "w|gz", fileobj=sys.stdout.buffer) as tar:
       for name in ["foo", "bar", "quux"]:
           tar.add(name)

Cómo crear un archivo y reiniciar la información del usuario usando el
parámetro *filter* en "TarFile.add()":

   import tarfile
   def reset(tarinfo):
       tarinfo.uid = tarinfo.gid = 0
       tarinfo.uname = tarinfo.gname = "root"
       return tarinfo
   tar = tarfile.open("sample.tar.gz", "w:gz")
   tar.add("foo", filter=reset)
   tar.close()

## Formatos tar con soporte

There are three tar formats that can be created with the "tarfile"
module:

* El formato ("USTAR_FORMAT") POSIX.1-1988 ustar. Admite nombres de
  archivos de hasta una longitud de 256 caracteres y nombres de enlace
  de hasta 100 caracteres. El tamaño máximo de archivo es de 8 GiB.
  Este es un formato viejo y limitado pero con amplio soporte.

* The GNU tar format ("GNU_FORMAT"). It supports long filenames and
  linknames, files bigger than 8 GiB and sparse files. It is the de
  facto standard on GNU/Linux systems. "tarfile" fully supports the
  GNU tar extensions for long names, sparse file support is read-only.

* The POSIX.1-2001 pax format ("PAX_FORMAT"). It is the most flexible
  format with virtually no limits. It supports long filenames and
  linknames, large files and stores pathnames in a portable way.
  Modern tar implementations, including GNU tar, bsdtar/libarchive and
  star, fully support extended *pax* features; some old or
  unmaintained libraries may not, but should treat *pax* archives as
  if they were in the universally supported *ustar* format. It is the
  current default format for new archives.

  Extiende el formato existente *ustar* con cabeceras adicionales para
  información que no puede ser almacenada de otra manera. Hay dos
  variaciones de encabezados pax: Los encabezados extendidos solo
  afectan al encabezado del archivo posterior, las encabezados
  globales son validos para el archivo entero y afectan todos los
  siguientes archivos. Todos los datos en un encabezado pax son
  codificados en *UTF-8* por razones de portabilidad.

Existen más variantes del formato tar que puede ser leídas, pero no
creadas:

* El antiguo formato V7. Este es el primer formato tar de *Unix
  Seventh Edition*, almacena solo archivos y directorios normales. Los
  nombres no deben tener más de 100 caracteres, no hay información de
  nombre de usuario/grupo disponible. Algunos archivos tienen sumas de
  comprobación de encabezado mal calculadas en el caso de campos con
  caracteres que no son ASCII.

* El formato extendido tar de SunOS. Este formato es una variante del
  formato POSIX.1-2001 pax, pero no es compatible.

## Problemas unicode

El formato tar fue originalmente concebido para realizar respaldos en
unidades de cinta con el objetivo principal de preservar la
información del sistema de archivos. Hoy en día los archivos tar son
comúnmente utilizados para distribución de archivos e intercambio de
archivos sobre redes. Un problema del formato original (el cual es la
base de todos los demás formatos) es que no hay concepto de soporte
para diferentes codificaciones de caracteres. Por ejemplo, un archivo
tar ordinario creado en un sistema *UTF-8* no puede ser leído
correctamente en un sistema *Latin-1* si este contiene caracteres de
tipo no ASCII. Los meta-datos textuales (como nombres de archivos,
nombres de enlace, nombres de usuario/grupo) aparecerán dañados.
Desafortunadamente, no hay manera de detectar de forma automática la
codificación de un archivo. El formato *pax* fue diseñado para
resolver este problema. Almacena los metadatos no ASCII usando una
codificación de caracteres universal *UTF-8*.

The details of character conversion in "tarfile" are controlled by the
*encoding* and *errors* keyword arguments of the "TarFile" class.

*encoding* define la codificación de caracteres a utilizar para los
metadatos del archivo. El valor predeterminado es
"sys.getfilesystemencoding()" o "'ascii'" como una alternativa.
Dependiendo de si el archivo se lee o escribe, los metadatos deben
decodificarse o codificarse. Si el *encoding* no se configura
correctamente, esta conversión puede fallar.

El argumento *errors* define como van a ser tratados los caracteres
que no pueden ser transformados. Los valores admitidos están listados
en la sección Manejadores de errores. El esquema predeterminado es
"'surrogateescape'" el cual Python también utiliza para sus llamadas
al sistema de archivos. Consulta Nombres de archivos, argumentos de la
línea de comandos y variables de entorno.

Para archivos "PAX_FORMAT" (el formato default), el *encoding*
generalmente no es necesario porque todos los meta-datos son
almacenados utilizando *UTF-8*, el *encoding* solo es utilizado en
aquellos casos cuando las cabeceras binarias PAX son decodificadas o
cuando se almacenan cadenas de texto con caracteres sustitutos.
