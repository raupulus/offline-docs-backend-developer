---
title: '"zipfile" --- Work with ZIP archives'
source_url: https://docs.python.org/es/3
source_path: library/zipfile.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4700
---

# "zipfile" --- Work with ZIP archives

**Código fuente:** Lib/zipfile/

======================================================================

El formato de archivo ZIP es un estándar común de archivo y
compresión. Este módulo proporciona herramientas para crear, leer,
escribir, agregar y listar un archivo ZIP. Cualquier uso avanzado de
este módulo requerirá una comprensión del formato, tal como se define
en la PKZIP Application Note.

This module does not handle multipart ZIP files. It can handle ZIP
files that use the ZIP64 extensions (that is ZIP files that are more
than 4 GiB in size).  It supports decryption of encrypted files in ZIP
archives, but it cannot create an encrypted file.  Decryption is
extremely slow as it is implemented in native Python rather than C.

Handling compressed archives requires *optional modules* such as
"zlib", "bz2", "lzma", and "compression.zstd". If any of them are
missing from your copy of CPython, look for documentation from your
distributor (that is, whoever provided Python to you). If you are the
distributor, see Requirements for optional modules.

El módulo define los siguientes elementos:

exception zipfile.BadZipFile

   El error lanzado para archivos ZIP incorrectos.

   Added in version 3.2.

exception zipfile.BadZipfile

   Alias de "BadZipFile", para compatibilidad con versiones anteriores
   de Python.

   Obsoleto desde la versión 3.2.

exception zipfile.LargeZipFile

   El error lanzado cuando un archivo ZIP requiera la funcionalidad
   ZIP64 pero no ha sido habilitado.

class zipfile.ZipFile

   La clase para leer y escribir archivos ZIP. Vea la sección ZipFile
   objects para detalles del constructor.

class zipfile.Path

   Clase que implementa un subconjunto de la interfaz proporcionada
   por "pathlib.Path", incluyendo la interfaz completa
   "importlib.resources.abc.Traversable".

   Added in version 3.8.

class zipfile.PyZipFile

   Clase para crear archivos ZIP que contienen bibliotecas de Python.

class zipfile.ZipInfo(filename='NoName', date_time=(1980, 1, 1, 0, 0, 0))

   Class used to represent information about a member of an archive.
   Instances of this class are returned by the "getinfo()" and
   "infolist()" methods of "ZipFile" objects.  Most users of the
   "zipfile" module will not need to create these, but only use those
   created by this module. *filename* should be the full name of the
   archive member, and *date_time* should be a tuple containing six
   fields which describe the time of the last modification to the
   file; the fields are described in section ZipInfo objects.

   Distinto en la versión 3.13: A public "compress_level" attribute
   has been added to expose the formerly protected "_compresslevel".
   The older protected name continues to work as a property for
   backwards compatibility.

   _for_archive(archive)

      Resolve the date_time, compression attributes, and external
      attributes to suitable defaults as used by "ZipFile.writestr()".

      Returns self for chaining.

      Added in version 3.14.

zipfile.is_zipfile(filename)

   Retorna "True" si *filename* es un archivo ZIP válido basado en su
   número mágico; de lo contrario, retorna "False". *filename* también
   puede ser un archivo o un objeto similar a un archivo.

   Distinto en la versión 3.1: Soporte para archivos y objetos
   similares a archivos.

zipfile.ZIP_STORED

   La constante numérica para un miembro de archivo sin comprimir.

zipfile.ZIP_DEFLATED

   La constante numérica para el método de compresión ZIP habitual.
   Esto requiere el módulo "zlib".

zipfile.ZIP_BZIP2

   La constante numérica para el método de compresión BZIP2. Esto
   requiere el módulo "bz2".

   Added in version 3.3.

zipfile.ZIP_LZMA

   La constante numérica para el método de compresión LZMA. Esto
   requiere el módulo "lzma".

   Added in version 3.3.

zipfile.ZIP_ZSTANDARD

   The numeric constant for Zstandard compression. This requires the
   "compression.zstd" module.

   Nota:

     In APPNOTE 6.3.7, the method ID "20" was assigned to Zstandard
     compression. This was changed in APPNOTE 6.3.8 to method ID "93"
     to avoid conflicts, with method ID "20" being deprecated. For
     compatibility, the "zipfile" module reads both method IDs but
     will only write data with method ID "93".

   Added in version 3.14.

Nota:

  The ZIP file format specification has included support for bzip2
  compression since 2001, for LZMA compression since 2006, and
  Zstandard compression since 2020. However, some tools (including
  older Python releases) do not support these compression methods, and
  may either refuse to process the ZIP file altogether, or fail to
  extract individual files.

Ver también:

  PKZIP Application Note
     Documentación sobre el formato de archivo ZIP por Phil Katz, el
     creador del formato y los algoritmos utilizados.

  Página principal de Info-ZIP
     Información sobre los programas de archivo ZIP del proyecto Info-
     ZIP y las bibliotecas de desarrollo.

## ZipFile objects

class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True, metadata_encoding=None)

   Abra un archivo ZIP, donde *file* puede ser una ruta a un archivo
   (una cadena), un objeto similar a un archivo o un *path-like
   object*.

   El parámetro *mode* debe ser "'r'" para leer un archivo existente,
   "'w'" para truncar y escribir un nuevo archivo, "'a'" para
   agregarlo a un archivo existente, o "'x'" para crear y escribir
   exclusivamente un nuevo archivo. Si *mode* es "'x'" y *file* se
   refiere a un archivo existente, se lanzará un "FileExistsError". Si
   *mode* es "'a'" y *file* se refiere a un archivo ZIP existente,
   entonces se le agregan archivos adicionales. Si *file* no se
   refiere a un archivo ZIP, se agrega un nuevo archivo ZIP al
   archivo. Esto está destinado a agregar un archivo ZIP a otro
   archivo (como "python.exe"). Si *mode* es "'a'" y el archivo no
   existe en absoluto, se crea. Si *mode* es "'r'" o "'a'", el archivo
   debe poder buscarse.

   *compression* is the ZIP compression method to use when writing the
   archive, and should be "ZIP_STORED", "ZIP_DEFLATED", "ZIP_BZIP2",
   "ZIP_LZMA", or "ZIP_ZSTANDARD"; unrecognized values will cause
   "NotImplementedError" to be raised.  If "ZIP_DEFLATED",
   "ZIP_BZIP2", "ZIP_LZMA", or "ZIP_ZSTANDARD" is specified but the
   corresponding module ("zlib", "bz2", "lzma", or "compression.zstd")
   is not available, "RuntimeError" is raised. The default is
   "ZIP_STORED".

   If *allowZip64* is "True" (the default) zipfile will create ZIP
   files that use the ZIP64 extensions when the zipfile is larger than
   4 GiB. If it is "false" "zipfile" will raise an exception when the
   ZIP file would require ZIP64 extensions.

   The *compresslevel* parameter controls the compression level to use
   when writing files to the archive. When using "ZIP_STORED" or
   "ZIP_LZMA" it has no effect. When using "ZIP_DEFLATED" integers "0"
   through "9" are accepted (see "zlib" for more information). When
   using "ZIP_BZIP2" integers "1" through "9" are accepted (see "bz2"
   for more information). When using "ZIP_ZSTANDARD" integers
   "-131072" through "22" are commonly accepted (see
   "CompressionParameter.compression_level" for more on retrieving
   valid values and their meaning).

   El argumento *strictly_timestamps*, cuando se establece en "False",
   permite comprimir archivos anteriores a 1980-01-01 a costa de
   establecer la marca de tiempo en 1980-01-01. Un comportamiento
   similar ocurre con archivos más nuevos que 2107-12-31, la marca de
   tiempo también se establece en el límite.

   Cuando el parámetro *mode* es "'r'", el *metadata_encoding* podría
   ser asignado al nombre del codec, el cual será usado para
   decodificar metadata como los nombres de los miembros y comentarios
   ZIP.

   Si el archivo se crea con el modo "'w'", "'x'" o "'a'" y luego
   "closed" sin agregar ningún archivo al archivo, Las estructuras ZIP
   apropiadas para un archivo vacío se escribirán en el archivo.

   ZipFile también es un manejador de contexto y por lo tanto, admite
   la declaración "with". En el ejemplo, *myzip* se cierra después que
   el conjunto de instrucciones "with" se termine---incluso si se
   produce una excepción:

      with ZipFile('spam.zip', 'w') as myzip:
          myzip.write('eggs.txt')

   Nota:

     *metadata_encoding* is an instance-wide setting for the ZipFile.
     It is not possible to set this on a per-member basis.Este
     atributo es una solución alterna para implementaciones heredadas
     que producen archivos con nombres basados en la codificación
     regional o la página de códigos actual (con mayor frecuencia en
     Windows). De acuerdo con el estándar .ZIP, la codificación de la
     metadata podría ser especificada por la página de códigos de IBM
     (por defecto) or por UTF-8 mediante un flag en la cabecera. Este
     flag toma precedencia sobre *metadata_encoding*, el cual es una
     extensión específica a Python.

   Distinto en la versión 3.2: Se agregó la capacidad de usar
   "ZipFile" como administrador de contexto.

   Distinto en la versión 3.3: Soporte agregado para "bzip2" y
   compresión "lzma".

   Distinto en la versión 3.4: Las extensiones ZIP64 están habilitadas
   por defecto.

   Distinto en la versión 3.5: Se agregó soporte para escribir en
   secuencias que no se pueden buscar. Se agregó soporte para el modo
   "'x'".

   Distinto en la versión 3.6: Anteriormente, se generó un simple
   "RuntimeError" para valores de compresión no reconocidos.

   Distinto en la versión 3.6.2: El parámetro *file* acepta un *path-
   like object*.

   Distinto en la versión 3.7: Agregue el parámetro *compresslevel*.

   Distinto en la versión 3.8: The *strict_timestamps* keyword-only
   parameter.

   Distinto en la versión 3.11: Se ha añadido soporte para especificar
   la codificación del nombre del miembro para leer metadatos en las
   cabeceras de directorio y archivo del archivo zip.

ZipFile.close()

   Cierra el archivo. Debe llamar a "close()" antes de salir de su
   programa o no se escribirán registros esenciales.

ZipFile.getinfo(name)

   Retorna un objeto "ZipInfo" con información sobre el miembro del
   archivo *name*. Llamando a "getinfo()" para obtener un nombre que
   no figura actualmente en el archivo lanzará un "KeyError".

ZipFile.infolist()

   Retorna una lista que contiene un objeto "ZipInfo" para cada
   miembro del archivo. Los objetos están en el mismo orden que sus
   entradas en el archivo ZIP real en el disco si se abrió un archivo
   existente.

ZipFile.namelist()

   Retorna una lista de miembros del archivo por nombre.

ZipFile.open(name, mode='r', pwd=None, *, force_zip64=False)

   Acceda a un miembro del archivo comprimido como un objeto binario
   similar a un archivo. *name* puede ser el nombre de un archivo
   dentro del archivo comprimido o un objeto "ZipInfo". El parámetro
   *mode*, si está incluido, debe ser "'r'" (el valor predeterminado)
   o "'w'". *pwd* es la contraseña utilizada para descifrar archivos
   ZIP encriptados como un objeto "bytes".

   "open()" también es un administrador de contexto y por lo tanto,
   soporta "with" "statement":

      with ZipFile('spam.zip') as myzip:
          with myzip.open('eggs.txt') as myfile:
              print(myfile.read())

   Con *mode* "'r'", el objeto tipo archivo ("ZipExtFile") es de solo
   lectura y proporciona los siguientes métodos: "read()",
   "readline()", "readlines()", "seek()", "tell()", "__iter__()", "__
   next__()". Estos objetos pueden funcionar independientemente del
   archivo Zip.

   Con "mode = 'w'", se retorna un controlador de archivo escribible,
   que admite el método "write()". Mientras está abierto un
   identificador de archivo escribible, intentar leer o escribir otros
   archivos en el archivo ZIP lanzará un "ValueError".

   In both cases the file-like object has also attributes "name",
   which is equivalent to the name of a file within the archive, and
   "mode", which is "'rb'" or "'wb'" depending on the input mode.

   Al escribir un archivo, si el tamaño del archivo no se conoce de
   antemano pero puede exceder los 2 GB, pase "force_zip64 = True"
   para asegurarse de que el formato del encabezado sea capaz de
   admitir archivos grandes. Si el tamaño del archivo se conoce de
   antemano, construya un objeto "ZipInfo" con "file_size"
   establecido, y úselo como parámetro *name*.

   Nota:

     Los métodos "open()", "read()" y "extract()" pueden tomar un
     nombre de archivo o un objeto "ZipInfo". Apreciará esto cuando
     intente leer un archivo ZIP que contiene miembros con nombres
     duplicados.

   Distinto en la versión 3.6: Se eliminó el soporte de "mode='U'".
   Use "io.TextIOWrapper" para leer archivos de texto comprimido en
   modo *universal newlines*.

   Distinto en la versión 3.6: "ZipFile.open()" ahora se puede usar
   para escribir archivos en el archivo comprimido con la opción
   "mode='w'".

   Distinto en la versión 3.6: Llamar a "open()" en un ZipFile cerrado
   lanzará un "ValueError". Anteriormente, se planteó a
   "RuntimeError".

   Distinto en la versión 3.13: Added attributes "name" and "mode" for
   the writeable file-like object. The value of the "mode" attribute
   for the readable file-like object was changed from "'r'" to "'rb'".

ZipFile.extract(member, path=None, pwd=None)

   Extraer un miembro del archivo comprimido al directorio de trabajo
   actual; *member* debe ser su nombre completo o un objeto "ZipInfo".
   La información de su archivo se extrae con la mayor precisión
   posible. *path* especifica un directorio diferente para extraer.
   *member* puede ser un nombre de archivo o un objeto "ZipInfo".
   *pwd* es la contraseña utilizada para archivos encriptados como un
   objeto "bytes".

   Retorna la ruta normalizada creada (un directorio o archivo nuevo).

   Nota:

     Si el nombre de archivo de un miembro es una ruta absoluta, se
     eliminarán un punto compartido de "drive/UNC" y las barras
     diagonales (hacia atrás), ej: "///foo/bar" se convierte en
     "foo/bar" en Unix y "C:\foo\bar" se convierte en "foo\bar" en
     Windows. Y todos los componentes "".."" en un nombre de archivo
     miembro se eliminarán, ej: "../../foo../../ba..r" se convierte en
     "foo../ba..r". En Windows, los caracteres ilegales (":", "<",
     ">", "|", """, "?" Y "*") se reemplazan por guion bajo ("_").

   Distinto en la versión 3.6: Llamando "extract()" en un ZipFile
   cerrado lanzará un "ValueError". Anteriormente, se planteó a
   "RuntimeError".

   Distinto en la versión 3.6.2: El parámetro *path* acepta un *path-
   like object*.

ZipFile.extractall(path=None, members=None, pwd=None)

   Extrae todos los miembros del archivo comprimido al directorio de
   trabajo actual. *path* especifica un directorio diferente para
   extraer. *members* es opcional y debe ser un subconjunto de la
   lista devuelta por "namelist()". *pwd* es la contraseña utilizada
   para archivos encriptados como un objeto "bytes".

   Advertencia:

     Never extract archives from untrusted sources without prior
     inspection. It is possible that files are created outside of
     *path*, for example, members that have absolute filenames or
     filenames with ".." components. This module attempts to prevent
     that. See "extract()" note.

   Distinto en la versión 3.6: Llamar a "extractall()" en un ZipFile
   cerrado lanzará un "ValueError". Anteriormente, se planteó a
   "RuntimeError".

   Distinto en la versión 3.6.2: El parámetro *path* acepta un *path-
   like object*.

ZipFile.printdir()

   Imprime una tabla de contenido para el archivo en "sys.stdout".

ZipFile.setpassword(pwd)

   Establece *pwd* (un objeto "bytes") como contraseña predeterminada
   para  extraer archivos encriptados.

ZipFile.read(name, pwd=None)

   Return the bytes of the file *name* in the archive.  *name* is the
   name of the file in the archive, or a "ZipInfo" object.  The
   archive must be open for read or append. *pwd* is the password used
   for encrypted files as a "bytes" object and, if specified,
   overrides the default password set with "setpassword()". Calling
   "read()" on a ZipFile that uses a compression method other than
   "ZIP_STORED", "ZIP_DEFLATED", "ZIP_BZIP2", "ZIP_LZMA", or
   "ZIP_ZSTANDARD" will raise a "NotImplementedError". An error will
   also be raised if the corresponding compression module is not
   available.

   Distinto en la versión 3.6: Llamando "read()" en un ZipFile cerrado
   lanzará un "ValueError". Anteriormente, se planteó a
   "RuntimeError".

ZipFile.testzip()

   Lee todos los archivos en el archivo y verifica sus CRC y
   encabezados de archivo. Retorna el nombre del primer archivo
   incorrecto o retorna "None".

   Distinto en la versión 3.6: Llamar a "testzip()" en un ZipFile
   cerrado lanzará un "ValueError". Anteriormente, se planteó a
   "RuntimeError".

ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None)

   Escribe el archivo llamado *filename* en el archivo, dándole el
   nombre de archivo *arcname* (por defecto, será el mismo que
   *filename*, pero sin una letra de unidad y con los separadores de
   ruta principales eliminados). Si se proporciona, *compress_type*
   anula el valor dado para el parámetro *compression* al constructor
   para la nueva entrada. Del mismo modo, *compresslevel* anulará el
   constructor si se proporciona. El archivo debe estar abierto con el
   modo "'w'", "'x'" o "'a'".

   Nota:

     Históricamente, el estándar del archivo ZIP no especificaba una
     codificación para la metadata, pero si era fuertemente
     recomendado usar CP437(la codificación original de IBM PC) con
     fines de interoperabilidad. Versiones recientes permiten el uso
     de UTF-8 (exclusivamente). En éste modulo, UTF-8 será usada
     automáticamente para escribir los nombres de los miembros si es
     que estos contienen algún caracter no-ASCII. No es posible
     escribir nombres de miembros en otra codificación que no sea
     ASCII o UTF-8.

   Nota:

     Los nombres de archivo deben ser relativos a la raíz del archivo,
     es decir, no deben comenzar con un separador de ruta.

   Nota:

     Si "arcname" (o "filename", si "arcname" no se proporciona)
     contiene un byte nulo, el nombre del archivo en el archivo se
     truncará en el byte nulo.

   Nota:

     Un barra al frente en el nombre del archivo puede hacer que el
     archivo sea imposible de abrir en algunos programas zip en
     sistemas Windows.

   Distinto en la versión 3.6: Llamando "write()" en un ZipFile creado
   con el modo "'r'" o un ZipFile cerrado lanzará un "ValueError".
   Anteriormente, se planteó a "RuntimeError".

ZipFile.writestr(zinfo_or_arcname, data, compress_type=None, compresslevel=None)

   Escribe un registro en el archivo. El contenido es *data*, que
   puede ser una instancia de "str" o a "bytes"; si es una "str",
   primero se codifica como UTF-8. *zinfo_or_arcname* es el nombre del
   archivo que se le dará en el archivo o una instancia de "ZipInfo".
   Si se trata de una instancia, se debe proporcionar al menos el
   nombre de archivo, la fecha y la hora. Si es un nombre, la fecha y
   la hora se configuran en la fecha y hora actuales. El archivo debe
   abrirse con el modo "'w'", "'x'" o "'a'".

   Si se proporciona, *compress_type* anula el valor dado para el
   parámetro *compression* al constructor para la nueva entrada, o en
   *zinfo_or_arcname* (si es una instancia de "ZipInfo"). Del mismo
   modo, *compresslevel* anulará el constructor si se proporciona.

   Nota:

     Al pasar una instancia de "ZipInfo" como el parámetro
     *zinfo_or_arcname*, el método de compresión utilizado será el
     especificado en el miembro *compress_type* de la instancia dada
     "ZipInfo". Por defecto, el constructor "ZipInfo" establece este
     miembro en "ZIP_STORED".

   Distinto en la versión 3.2: El argumento *compress_type*.

   Distinto en la versión 3.6: Llamando "writestr()" en un ZipFile
   creado con el modo "'r'" o un ZipFile cerrado lanzará un
   "ValueError". Anteriormente, se planteó a "RuntimeError".

   Distinto en la versión 3.14: Now respects the "SOURCE_DATE_EPOCH"
   environment variable. If set, it uses this value as the
   modification timestamp for the file written into the ZIP archive,
   instead of using the current time.

ZipFile.mkdir(zinfo_or_directory, mode=511)

   Crea un directorio dentro del archivo. Si *zinfo_or_directory* es
   un string, el directorio es creado dentro del archivo con el modo
   especificado en el argumento *mode*. Si del contrario,
   *zinfo_or_directory* es una instancia de "ZipInfo" entonces el
   argumento *mode* es ignorado.

   El archivo debe estar abierto en modo "'w'", "'x'" o "'a'".

   Added in version 3.11.

Los siguientes atributos de datos también están disponibles:

ZipFile.filename

   Nombre del archivo ZIP.

ZipFile.debug

   El nivel de salida de depuración a usar. Esto se puede configurar
   de "0" (el valor predeterminado, sin salida) a "3" (la mayor
   cantidad de salida). La información de depuración se escribe en
   "sys.stdout".

ZipFile.comment

   El comentario asociado con el archivo ZIP como un objeto "bytes".
   Si se asigna un comentario a una instancia de "ZipFile" creada con
   el modo "'w'", "'x'" o "'a'", no debe tener más de 65535 bytes. Los
   comentarios más largos que esto se truncarán.

## Path objects

class zipfile.Path(root, at='')

   Construye un objeto Path a partir de un archivo zip "root" (que
   puede ser una instancia "ZipFile" o "file" adecuado para pasar al
   constructor "ZipFile").

   "at" especifica la ubicación de esta ruta dentro del archivo zip,
   ej. 'dir/file.txt', 'dir/' o ''.El valor predeterminado es la
   cadena vacía, que indica la raíz.

   Nota:

     The "Path" class does not sanitize filenames within the ZIP
     archive. Unlike the "ZipFile.extract()" and
     "ZipFile.extractall()" methods, it is the caller's responsibility
     to validate or sanitize filenames to prevent path traversal
     vulnerabilities (for example, absolute paths or paths with ".."
     components). When handling untrusted archives, consider resolving
     filenames using "os.path.abspath()" and checking against the
     target directory with "os.path.commonpath()".

Los objetos de ruta exponen las siguientes características de objetos
"pathlib.Path":

Los objetos de ruta son transitables utilizando el operador "/" o
utilizando "joinpath".

Path.name

   El componente final de la ruta.

Path.open(mode='r', *, pwd, **)

   Invoca "ZipFile.open()" en la ruta actual. Permite la apertura para
   lectura o escritura, texto o binario a través de los modos
   admitidos: 'r', 'w', 'rb', 'wb'. Los argumentos posicionales y de
   palabras clave se pasan a través de "io.TextIOWrapper" cuando se
   abren como texto y se ignoran en caso contrario. "pwd" es el
   parámetro "pwd" para "ZipFile.open()".

   Distinto en la versión 3.9: Se agregó soporte para modos de texto y
   binarios para abrir. El modo predeterminado ahora es texto.

   Distinto en la versión 3.11.2: El parámetro "encoding" puede
   proporcionarse como un argumento posicional sin causar un
   "TypeError". Tal y como podía ocurrir en la versión 3.9. El código
   que necesite ser compatible con versiones no parcheadas 3.10 y 3.11
   debe pasar como palabras clave todos los argumentos de
   "io.TextIOWrapper", incluido "encoding".

Path.iterdir()

   Enumera los hijos del directorio actual.

Path.is_dir()

   Retorna "True" si el contexto actual hace referencia a un
   directorio.

Path.is_file()

   Retorna "True" si el contexto actual hace referencia a un archivo.

Path.is_symlink()

   Return "True" if the current context references a symbolic link.

   Added in version 3.12.

   Distinto en la versión 3.13: Previously, "is_symlink" would
   unconditionally return "False".

Path.exists()

   Retorna "True" si el contexto actual hace referencia a un archivo o
   directorio en el archivo zip.

Path.suffix

   The last dot-separated portion of the final component, if any. This
   is commonly called the file extension.

   Added in version 3.11: Propiedad agregada "Path.suffix".

Path.stem

   El componente final de la ruta, sin su sufijo.

   Added in version 3.11: Propiedad agregada "Path.stem".

Path.suffixes

   A list of the path’s suffixes, commonly called file extensions.

   Added in version 3.11: Propiedad agregada "Path.suffixes".

Path.read_text(*, **)

   Lee el archivo actual como texto unicode. Los argumentos
   posicionales y de palabras clave se pasan a "io.TextIOWrapper"
   (excepto "buffer", que está implícito en el contexto).

   Distinto en la versión 3.11.2: El parámetro "encoding" puede
   proporcionarse como un argumento posicional sin causar un
   "TypeError". Tal y como podía ocurrir en la versión 3.9. El código
   que necesite ser compatible con versiones no parcheadas 3.10 y 3.11
   debe pasar como palabras clave todos los argumentos de
   "io.TextIOWrapper", incluido "encoding".

Path.read_bytes()

   Lee el archivo actual como bytes.

Path.joinpath(*other)

   Retorna un nuevo objeto de ruta con cada argumentos *other* unidos.
   Los siguientes son equivalentes:

      >>> Path(...).joinpath('child').joinpath('grandchild')
      >>> Path(...).joinpath('child', 'grandchild')
      >>> Path(...) / 'child' / 'grandchild'

   Distinto en la versión 3.10: Antes de 3.10, "joinpath" no estaba
   documentado y aceptaba exactamente un parámetro.

The zipp project provides backports of the latest path object
functionality to older Pythons. Use "zipp.Path" in place of
"zipfile.Path" for early access to changes.

## PyZipFile objects

El constructor "PyZipFile" toma los mismos parámetros que el
constructor "ZipFile", y un parámetro adicional, *optimize*.

class zipfile.PyZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, optimize=-1)

   Distinto en la versión 3.2: Added the *optimize* parameter.

   Distinto en la versión 3.4: Las extensiones ZIP64 están habilitadas
   por defecto.

   Las instancias tienen un método ademas de los objetos "ZipFile":

   writepy(pathname, basename='', filterfunc=None)

      Busca archivos "*.py" y agrega el archivo correspondiente al
      archivo.

      Si no se proporcionó el parámetro *optimize* a "PyZipFile" o
      "-1", el archivo correspondiente es un archivo "*.pyc",
      compilando si es necesario.

      Si el parámetro *optimize* a "PyZipFile" era "0", "1" or "2",
      solo se agregarán a ese archivo los archivos con ese nivel de
      optimización (ver "compile()") el archivo, compilando si es
      necesario.

      Si *pathname* es un archivo, el nombre del archivo debe terminar
      con ".py", y solo el archivo (correspondiente "*.pyc") se agrega
      en el nivel superior (sin información de ruta). Si *pathname* es
      un archivo que no termina con ".py", se lanzará "RuntimeError".
      Si es un directorio, y el directorio no es un directorio de
      paquetes, entonces todos los archivos "*.pyc" se agregan en el
      nivel superior. Si el directorio es un directorio de paquetes,
      todos "*.pyc" se agregan bajo el nombre del paquete como una
      ruta de archivo, y si alguno de los subdirectorios son
      directorios de paquetes, todos estos se agregan recursivamente
      en orden ordenado.

      *basename* está destinado solo para uso interno.

      *filterfunc*, si se proporciona, debe ser una función que tome
      un único argumento de cadena. Se le pasará cada ruta (incluida
      cada ruta de archivo completa individual) antes de que se
      agregue al archivo. Si *filterfunc* retorna un valor falso, la
      ruta no se agregará y si se trata de un directorio se ignorará
      su contenido. Por ejemplo, si nuestros archivos de prueba están
      todos en directorios de "test" o comienzan con la cadena
      "test_", podemos usar un *filterfunc* para excluirlos

         >>> zf = PyZipFile('myprog.zip')
         >>> def notests(s):
         ...     fn = os.path.basename(s)
         ...     return (not (fn == 'test' or fn.startswith('test_')))
         ...
         >>> zf.writepy('myprog', filterfunc=notests)

      El método "writepy()" crea archivos con nombres de archivo como
      este

         string.pyc                   # Top level name
         test/__init__.pyc            # Package directory
         test/testall.pyc             # Module test.testall
         test/bogus/__init__.pyc      # Subpackage directory
         test/bogus/myfile.pyc        # Submodule test.bogus.myfile

      Distinto en la versión 3.4: Added the *filterfunc* parameter.

      Distinto en la versión 3.6.2: El parámetro *pathname* acepta un
      *path-like object*.

      Distinto en la versión 3.7: La recursividad ordena las entradas
      del directorio.

## ZipInfo objects

Las instancias de la clase "ZipInfo" son retornadas por los métodos
"getinfo()" y "infolist()" de "ZipFile". Cada objeto almacena
información sobre un solo miembro del archivo ZIP.

Hay un método de clase para hacer una instancia de "ZipInfo" para un
archivo de sistema de archivos:

classmethod ZipInfo.from_file(filename, arcname=None, *, strict_timestamps=True)

   Construye una instancia de "ZipInfo" para un archivo en el sistema
   de archivos, en preparación para agregarlo a un archivo zip.

   *filename* debe ser la ruta a un archivo o directorio en el sistema
   de archivos.

   Si se especifica *arcname*, este es usado como el nombre dentro del
   archivo. Si no se especifica *arcname*, el nombre será el mismo que
   *filename*, pero con cualquier letra de unidad y separadores de
   ruta principales eliminados.

   El argumento *strictly_timestamps*, cuando se establece en "False",
   permite comprimir archivos anteriores a 1980-01-01 a costa de
   establecer la marca de tiempo en 1980-01-01. Un comportamiento
   similar ocurre con archivos más nuevos que 2107-12-31, la marca de
   tiempo también se establece en el límite.

   Added in version 3.6.

   Distinto en la versión 3.6.2: El parámetro *filename* acepta un
   *path-like object*.

   Distinto en la versión 3.8: Added the *strict_timestamps* keyword-
   only parameter.

Las instancias tienen los siguientes métodos y atributos:

ZipInfo.is_dir()

   Retorna "True" si este miembro del archivo es un directorio.

   Utiliza el nombre de la entrada: los directorios siempre deben
   terminar con "/".

   Added in version 3.6.

ZipInfo.filename

   Nombre del archivo en el archivo.

ZipInfo.date_time

   The time and date of the last modification to the archive member.
   This is a tuple of six values representing the "last [modified]
   file time" and "last [modified] file date" fields from the ZIP
   file's central directory.

   The tuple contains:

   +---------+----------------------------+
   | Índice  | Valor                      |
   |=========|============================|
   | "0"     | Año (>= 1980)              |
   +---------+----------------------------+
   | "1"     | Mes (basado en uno)        |
   +---------+----------------------------+
   | "2"     | Día del mes (basado en     |
   |         | uno)                       |
   +---------+----------------------------+
   | "3"     | Horas (basados en cero)    |
   +---------+----------------------------+
   | "4"     | Minutos (basados en cero)  |
   +---------+----------------------------+
   | "5"     | Segundos (basado en cero)  |
   +---------+----------------------------+

   Nota:

     The ZIP format supports multiple timestamp fields in different
     locations (central directory, extra fields for NTFS/UNIX systems,
     etc.). This attribute specifically returns the timestamp from the
     central directory. The central directory timestamp format in ZIP
     files does not support timestamps before 1980. While some extra
     field formats (such as UNIX timestamps) can represent earlier
     dates, this attribute only returns the central directory
     timestamp.The central directory timestamp is interpreted as
     representing local time, rather than UTC time, to match the
     behavior of other zip tools.

ZipInfo.compress_type

   Tipo de compresión para la miembro del archivo.

ZipInfo.comment

   Comenta para el miembro de archivo individual como un objeto
   "bytes".

ZipInfo.extra

   Datos de campo de expansión. La PKZIP Application Note contiene
   algunos comentarios sobre la estructura interna de los datos
   contenidos en este objeto "bytes".

ZipInfo.create_system

   Sistema que creó el archivo ZIP.

ZipInfo.create_version

   Versión PKZIP que creó el archivo ZIP.

ZipInfo.extract_version

   Se necesita la versión PKZIP para extraer el archivo.

ZipInfo.reserved

   Debe ser cero.

ZipInfo.flag_bits

   Bits de bandera ZIP.

ZipInfo.volume

   Número de volumen del encabezado del archivo.

ZipInfo.internal_attr

   Atributos internos.

ZipInfo.external_attr

   Atributos de archivo externo.

ZipInfo.header_offset

   Byte desplazado al encabezado del archivo.

ZipInfo.CRC

   CRC-32 del archivo sin comprimir.

ZipInfo.compress_size

   Tamaño de los datos comprimidos.

ZipInfo.file_size

   Tamaño del archivo sin comprimir.

## Command-line interface

The "zipfile" module provides a simple command-line interface to
interact with ZIP archives.

Si desea crear un nuevo archivo ZIP, especifique su nombre después de
la opción "-c" y luego enumere los nombres de archivo que deben
incluirse:

   $ python -m zipfile -c monty.zip spam.txt eggs.txt

Pasar un directorio también es aceptable:

   $ python -m zipfile -c monty.zip life-of-brian_1979/

Si desea extraer un archivo ZIP en el directorio especificado, use la
opción "-e":

   $ python -m zipfile -e monty.zip target-dir/

Para obtener una lista de los archivos en un archivo ZIP, use la
opción "-l":

   $ python -m zipfile -l monty.zip

### Opciones de línea de comando

-l <zipfile>
--list <zipfile>

   Lista de archivos en un archivo zip.

-c <zipfile> <source1> ... <sourceN>
--create <zipfile> <source1> ... <sourceN>

   Crea el archivo zip a partir de archivos fuente.

-e <zipfile> <output_dir>
--extract <zipfile> <output_dir>

   Extrae el archivo zip en el directorio de destino.

-t <zipfile>
--test <zipfile>

   Prueba si el archivo zip es válido o no.

--metadata-encoding <encoding>

   Especifica la codificación de nombre de miembros para "-l", "-e" y
   "-t".

   Added in version 3.11.

## Problemas de descompresión

La extracción en el módulo zipfile puede fallar debido a algunos
problemas que se enumeran a continuación.

### Del archivo mismo

La descompresión puede fallar debido a una contraseña incorrecta /
suma de verificación CRC / formato ZIP o método / descifrado de
compresión no compatible.

### File system limitations

Exceder las limitaciones en diferentes sistemas de archivos puede
causar que la descompresión falle. Como los caracteres permitidos en
las entradas del directorio, la longitud del nombre del archivo, la
longitud de la ruta, el tamaño de un solo archivo y la cantidad de
archivos, etc.

### Limitaciones de recursos

La falta de memoria o volumen de disco conduciría a la descompresión
fallida. Por ejemplo, las bombas de descompresión (también conocido
como ZIP bomb) se aplican a la biblioteca de archivos zip que pueden
causar el agotamiento del volumen del disco.

### Interrupción

La interrupción durante la descompresión, como presionar control-C o
matar el proceso de descompresión, puede dar como resultado una
descompresión incompleta del archivo.

### Comportamientos predeterminados de extracción

No conocer los comportamientos de extracción predeterminados puede
causar resultados de descompresión inesperados. Por ejemplo, al
extraer el mismo archivo dos veces, sobrescribe los archivos sin
preguntar.
