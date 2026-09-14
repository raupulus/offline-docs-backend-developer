---
title: '"io" --- Core tools for working with streams'
source_url: https://docs.python.org/es/3
source_path: library/io.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3030
---

# "io" --- Core tools for working with streams

**Código fuente:** Lib/io.py

======================================================================

## Resumen

The "io" module provides Python's main facilities for dealing with
various types of I/O.  There are three main types of I/O: *text I/O*,
*binary I/O* and *raw I/O*.  These are generic categories, and various
backing stores can be used for each of them.  A concrete object
belonging to any of these categories is called a *file object*.  Other
common terms are *stream* and *file-like object*.

Independiente de su categoría, cada objeto *stream* también tendrá
varias capacidades: puede ser solamente para lectura, solo escritura,
or lectura y escritura. También permite arbitrariamente acceso
aleatorio (buscando adelante o hacia atrás en cualquier lugar) o
solamente acceso secuencial (por ejemplo en el caso de un *socket* o
*pipe*).

All streams are careful about the type of data you give to them.  For
example giving a "str" object to the "write()" method of a binary
stream will raise a "TypeError".  So will giving a "bytes" object to
the "write()" method of a text stream.

Distinto en la versión 3.3: Operaciones que lanzarán un "IOError"
ahora lanzan "OSError", ya que "IOError" es un alias de "OSError".

### E/S Texto

E/S de tipo texto espera y produce objetos de clase "str". Esto
significa que cuando el respaldo de almacenamiento está compuesto de
forma nativa de *bytes* (como en el caso de un archivo), la
codificación y descodificación de datos está hecho de forma
transparente tanto como traducción opcional de caracteres de nueva
línea específicos de la plataforma.

The easiest way to create a text stream is with "open()", optionally
specifying an encoding:

   f = open("myfile.txt", "r", encoding="utf-8")

*Streams* de texto en memoria también están disponibles como objetos
de tipo "StringIO":

   f = io.StringIO("some initial text data")

Nota:

  When working with a non-blocking stream, be aware that read
  operations on text I/O objects might raise a "BlockingIOError" if
  the stream cannot perform the operation immediately.

El *API* (interfaz de programación de aplicaciones) de *streams* tipo
texto está descrito con detalle en la documentación de "TextIOBase".

### E/S Binaria

E/S binaria (también conocido como *buffered E/S*) espera *objetos
tipo bytes* y produce objetos tipo "bytes". No se hace codificación,
descodificación, o traducciones de nueva línea. Esta categoría de
*streams* puede ser usada para todos tipos de datos sin texto, y
también cuando se desea control manual sobre el manejo de dato
textual.

The easiest way to create a binary stream is with "open()" with "'b'"
in the mode string:

   f = open("myfile.jpg", "rb")

Los *streams* binarios en memoria también están disponibles como
objetos tipo "BytesIO":

   f = io.BytesIO(b"some initial binary data: \x00\x01")

El *API* de *stream* binario está descrito con detalle en la
documentación de "BufferedIOBase".

Otros módulos bibliotecarios pueden proveer maneras alternativas para
crear *streams* de tipo texto o binario. Ver
"socket.socket.makefile()" como ejemplo.

### E/S sin formato

E/S sin formato (también conocido como *unbuffered E/S*) es
generalmente usado como un fundamento de nivel bajo para *streams*
binario y tipo texto; es raramente útil para manipular directamente
*streams* sin formatos del código de usuario. Sin embargo puedes crear
un *stream* sin formato abriendo un archivo en modo binario con el
búfer apagado:

   f = open("myfile.jpg", "rb", buffering=0)

El *API* de *streams* sin formato está descrito con detalle en la
documentación de "RawIOBase".

Advertencia:

  Raw I/O is a low-level interface and methods generally must have
  their return values checked and be explicitly retried to ensure an
  operation completes. For instance "write()" returns the number of
  bytes written which may be less than the number of bytes provided (a
  partial write). High-level I/O objects like E/S Binaria and E/S
  Texto implement retry behavior.

## Codificación de texto

The default encoding of "TextIOWrapper" and "open()" is locale-
specific ("locale.getencoding()").

Sin embargo, muchos desarrolladores olvidan especificar la
codificación al abrir archivos de texto codificados en UTF-8 (por
ejemplo, JSON, TOML, Markdown, etc.) ya que la mayoría de las
plataformas Unix usan la configuración regional UTF-8 de forma
predeterminada. Esto causa errores porque la codificación local no es
UTF-8 para la mayoría de los usuarios de Windows. Por ejemplo:

   # May not work on Windows when non-ASCII characters in the file.
   with open("README.md") as f:
       long_description = f.read()

Accordingly, it is highly recommended that you specify the encoding
explicitly when opening text files. If you want to use UTF-8, pass
"encoding="utf-8"". To use the current locale encoding,
"encoding="locale"" is supported since Python 3.10.

Ver también:

  Modo Python UTF-8
     El modo UTF-8 de Python se puede utilizar para cambiar la
     codificación predeterminada a UTF-8 desde la codificación
     específica de la configuración regional.

  **PEP 686**
     Python 3.15 hará que Modo Python UTF-8 sea el valor
     predeterminado.

### EncodingWarning opcional

Added in version 3.10: Consulte **PEP 597** para más detalles.

To find where the default locale encoding is used, you can enable the
"-X warn_default_encoding" command line option or set the
"PYTHONWARNDEFAULTENCODING" environment variable, which will emit an
"EncodingWarning" when the default encoding is used.

Si está proporcionando una API que usa "open()" o "TextIOWrapper" y
pasa "encoding=None" como parámetro, puede usar "text_encoding()" para
que las personas que llaman a la API emitan un "EncodingWarning" si no
pasan un "encoding". Sin embargo, considere usar UTF-8 de forma
predeterminada (es decir, "encoding="utf-8"") para las nuevas API.

## Interfaz de módulo de alto nivel

io.DEFAULT_BUFFER_SIZE

   Un *int* que contiene el búfer de tamaño predeterminado usado por
   las clases de tipo E/S. "open()" utiliza el *blksize* del archivo
   (obtenido por "os.stat()") si es posible.

io.open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

   Esto es un alias para la función incorporada "open()".

   This function raises an auditing event "open" with arguments
   *path*, *mode* and *flags*. The *mode* and *flags* arguments may
   have been modified or inferred from the original call.

io.open_code(path)

   Abre el archivo dado con el modo "'rb'". Esta función debe ser
   usado cuando la intención es tratar el contenido como código
   ejecutable.

   *path* should be a "str" and an absolute path.

   The behavior of this function may be overridden by an earlier call
   to the "PyFile_SetOpenCodeHook()". However, assuming that *path* is
   a "str" and an absolute path, "open_code(path)" should always
   behave the same as "open(path, 'rb')". Overriding the behavior is
   intended for additional validation or preprocessing of the file.

   Added in version 3.8.

io.text_encoding(encoding, stacklevel=2, /)

   Esta es una función auxiliar para personas que llaman que usan
   "open()" o "TextIOWrapper" y tienen un parámetro "encoding=None".

   This function returns *encoding* if it is not "None". Otherwise, it
   returns ""locale"" or ""utf-8"" depending on UTF-8 Mode.

   This function emits an "EncodingWarning" if
   "sys.flags.warn_default_encoding" is true and *encoding* is "None".
   *stacklevel* specifies where the warning is emitted. For example:

      def read_text(path, encoding=None):
          encoding = io.text_encoding(encoding)  # stacklevel=2
          with open(path, encoding) as f:
              return f.read()

   En este ejemplo, se emite un "EncodingWarning" para el llamador de
   "read_text()".

   Consulte Codificación de texto para obtener más información.

   Added in version 3.10.

   Distinto en la versión 3.11: "text_encoding()" retornará "utf-8"
   cuando esté habilitado el modo UTF-8 y el *encoding* es "None".

exception io.BlockingIOError

   Esto es un alias de compatibilidad para la incorporada excepción
   "BlockingIOError".

exception io.UnsupportedOperation

   Una excepción heredando "OSError" y "ValueError" que es generado
   cuando se llama a una operación no admitida en un *stream*.

Ver también:

  "sys"
     contiene los *streams* estándar de IO "sys.stdin", "sys.stdout",
     y "sys.stderr".

## Jerarquía de clases

La implementación de *streams* E/S está organizada como una jerarquía
de clases. Primero *abstract base classes* (ABC), que son usados para
especificar las varias categorías de *streams*, luego las clases
concretas proveen un *stream* estándar de implementaciones.

Nota:

  The abstract base classes also provide default implementations of
  some methods in order to help implementation of concrete stream
  classes.  For example, "BufferedIOBase" provides unoptimized
  implementations of "readinto()" and "readline()".

En la parte superior de la jerarquía E/S está la clase abstracta base
"IOBase". Define la interfaz básica del *stream*. Tenga en cuenta que
no hay separación entre *streams* de lectura y escritura;
implementaciones están permitidos lanzar "UnsupportedOperation" si no
apoyan la operación.

La clase "RawIOBase" extiende "IOBase". Maneja la lectura y escritura
de bytes a un *stream*. "FileIO" subclasifica "RawIOBase" para proveer
una interfaz a los archivos en el sistema de archivos de la máquina.

The "BufferedIOBase" ABC extends "IOBase".  It deals with buffering on
a raw binary stream ("RawIOBase").  Its subclasses, "BufferedWriter",
"BufferedReader", and "BufferedRWPair" buffer raw binary streams that
are writable, readable, and both readable and writable, respectively.
"BufferedRandom" provides a buffered interface to seekable streams.
Another "BufferedIOBase" subclass, "BytesIO", is a stream of in-memory
bytes.

El "TextIOBase" ABC, otra subclasificación de "IOBase", trata con los
streams cuyos bytes representan texto, y maneja la codificación y
decodificación para cadenas de caracteres y de estos mismos.
"TextIOWrapper", que extiende "TextIOBase", es un interfaz textual
almacenado un *stream* sin formato amortiguado ("BufferedIOBase").
Finalmente, "StringIO"  es una stream en memoria para texto.

Los nombres de los argumentos no son parte de la especificación, y
solo los argumentos de "open()" están destinados a ser utilizados como
argumentos de palabras clave.

The following table summarizes the ABCs provided by the "io" module:

+---------------------------+--------------------+--------------------------+----------------------------------------------------+
| ABC                       | Hereda             | Métodos de trozos        | Métodos mixin y propiedades                        |
|                           |                    | (*Stub*)                 |                                                    |
|===========================|====================|==========================|====================================================|
| "IOBase"                  |                    | "fileno", "seek", and    | "close", "closed", "__enter__", "__exit__",        |
|                           |                    | "truncate"               | "flush", "isatty", "__iter__", "__next__",         |
|                           |                    |                          | "readable", "readline", "readlines", "seekable",   |
## |                           |                    |                          | "tell", "writable", and "writelines"               |

## | "RawIOBase"               | "IOBase"           | "readinto" and "write"   | Métodos "IOBase" heredados, "read", and "readall"  |

| "BufferedIOBase"          | "IOBase"           | "detach", "read",        | Métodos "IOBase" heredados, "readinto", and        |
## |                           |                    | "read1", and "write"     | "readinto1"                                        |

| "TextIOBase"              | "IOBase"           | "detach", "read",        | Métodos "IOBase" heredados, "encoding", "errors",  |
## |                           |                    | "readline", and "write"  | and "newlines"                                     |

### Clases base E/S

class io.IOBase

   La clase base abstracta para todas las clases de E/S.

   Esta clase provee implementaciones abstractas vacías para muchos
   métodos que clases que derivadas pueden anular selectivamente; la
   implementación predeterminada representa un archivo que no se puede
   leer, grabar o ser buscado.

   Even though "IOBase" does not declare "read()" or "write()" because
   their signatures will vary, implementations and clients should
   consider those methods part of the interface.  Also,
   implementations may raise a "ValueError" (or
   "UnsupportedOperation") when operations they do not support are
   called.

   El tipo básico usado para leer datos binarios o grabar un archivo
   es "bytes". Otros *bytes-like objects* son aceptados como
   argumentos para métodos también. Clases de tipo E/S funcionan
   usando datos de tipo "str".

   Tenga en cuenta que llamando cualquier método (incluso
   indagaciones) en un *stream* cerrada es indefinido. En este caso
   implementaciones podrían lanzar un error "ValueError".

   "IOBase" (y sus subclasificaciones) apoyan el protocolo iterador,
   significando que un objeto de clase "IOBase" puede ser iterado
   sobre el rendimiento de las líneas en un *stream* de datos. Líneas
   son definidas un poco diferente dependiendo si el *stream* es de
   tipo binario (produciendo *bytes*), o un *stream* de texto
   (produciendo cadenas de caracteres). Ver "readline()" abajo.

   "IOBase" es también un gestor de contexto y por ende apoya la
   declaración "with". En este ejemplo, *file* es cerrado después de
   que la declaración "with" termina--incluso si alguna excepción
   ocurre:

      with open('spam.txt', 'w') as file:
          file.write('Spam and eggs!')

   "IOBase" provee los siguientes atributos y métodos:

   close()

      Cierra el *stream*. Este método no tiene efecto si el archivo ya
      está cerrado. Cuándo está cerrado, cualquier operación que se le
      haga al archivo (ej. leer or grabar) lanzará el error
      "ValueError".

      Como conveniencia, se permite llamar este método más que una
      vez. Sin embargo, solamente el primer llamado tenderá efecto.

   closed

      "True" si está cerrada el *stream*.

   fileno()

      Retorna el descriptor de archivo subyacente (un número de tipo
      entero) de el *stream* si existe. Un "OSError" se lanza si el
      objeto IO no tiene un archivo descriptor.

   flush()

      Vacía los buffers de grabación del *stream* si corresponde. Esto
      no hace nada para *streams* que son solamente de lectura o
      *streams* sin bloqueo.

   isatty()

      Retorna "True"  si el *stream* es interactiva (ej., si está
      conectado a un terminal o dispositivo tty).

   readable()

      Return "True" if the stream can be read from. If "False",
      "read()" will raise "OSError".

   readline(size=-1, /)

      Lee y retorna una línea del *stream*. Si *size* (tamaño) es
      especificado, se capturará un máximo de ése mismo tamaño
      especificado en *bytes*.

      El terminador de la línea siempre es "b'\n'" para archivos de
      tipo binario; para archivos de tipo texto el argumento *newline*
      para la función "open()" pueden ser usados para seleccionar las
      líneas terminadoras reconocidas.

   readlines(hint=-1, /)

      Lee y retorna una lista de líneas del *stream*. *hint* puede ser
      especificado para controlar el número de líneas que se lee: no
      se leerán más líneas si el tamaño total (en *bytes* /
      caracteres) de todas las líneas excede *hint*.

      Los valores *hint* de "0" o menos, así como "None", se tratan
      como sin pista.

      Note that it's already possible to iterate on file objects using
      "for line in file: ..." without calling "file.readlines()".

   seek(offset, whence=os.SEEK_SET, /)

      Change the stream position to the given byte *offset*,
      interpreted relative to the position indicated by *whence*, and
      return the new absolute position. Values for *whence* are:

      * "os.SEEK_SET" or "0" -- start of the stream (the default);
        *offset* should be zero or positive

      * "os.SEEK_CUR" or "1" -- current stream position; *offset* may
        be negative

      * "os.SEEK_END" or "2" -- end of the stream; *offset* is usually
        negative

      Added in version 3.1: The "SEEK_*" constants.

      Added in version 3.3: Some operating systems could support
      additional values, like "os.SEEK_HOLE" or "os.SEEK_DATA". The
      valid values for a file could depend on it being open in text or
      binary mode.

   seekable()

      Retorna "True" si el *stream* apoya acceso aleatorio. Si retorna
      "False", "seek()", "tell()" y "truncate()"  lanzarán "OSError".

   tell()

      Retorna la posición actual del *stream*.

   truncate(size=None, /)

      Cambia el tamaño del *stream* al *size* dado en *bytes* (o la
      posición actual si no se especifica *size*). La posición actual
      del *stream* no se cambia. Este cambio de tamaño puede
      incrementar o reducir el tamaño actual del archivo. En caso de
      extensión, los contenidos del área del nuevo archivo depende de
      la plataforma (en la mayoría de los sistemas *bytes* adicionales
      son llenos de cero). Se retorna el nuevo tamaño del archivo.

      Distinto en la versión 3.5: *Windows* llenará los archivos con
      cero cuando extienda.

   writable()

      Return "True" if the stream supports writing.  If "False",
      "write()" and "truncate()" will raise "OSError".

   writelines(lines, /)

      Escribir una lista de líneas al *stream*. No se agrega
      separadores de líneas, así que es usual que las líneas tengan
      separador al final.

   __del__()

      Prepara para la destrucción de un objeto. "IOBase" proporciona
      una implementación dada de este método que ejecuta las
      instancias del método "close()".

class io.RawIOBase

   Base class for raw binary streams.  It inherits from "IOBase".

   Los flujos binarios sin procesar generalmente brindan acceso de
   bajo nivel a un dispositivo OS subyacente o API, y no intentan
   encapsularlos en primitivas de alto nivel (esta funcionalidad se
   realiza en un nivel superior en flujos binarios almacenados en
   búfer y flujos de texto, que se describen más adelante en esta
   página).

   "RawIOBase" proporciona estos métodos además de los de "IOBase":

   read(size=-1, /)

      Read up to *size* bytes from the object and return them.  As a
      convenience, if *size* is unspecified or -1, all bytes until EOF
      are returned.

      Attempts to make only one system call but will retry if
      interrupted and the signal handler does not raise an exception
      (see **PEP 475** for the rationale). This means fewer than
      *size* bytes may be returned if the operating system call
      returns fewer than *size* bytes.

      Si se retorna 0 *bytes* y el *size* no era 0, esto indica que es
      el fin del archivo. Si el objeto está en modo sin bloqueo y no
      hay *bytes* disponibles, se retorna "None".

      La implementación dada difiera al método "readall()" y
      "readinto()".

   readall()

      Lee y retorna todos los *bytes* del *stream* hasta llegar al fin
      del archivo, usando, si es necesario, varias llamadas al
      *stream*.

      If "0" bytes are returned this indicates end of file. If the
      object is in non-blocking mode and the underlying "read()"
      returns "None" indicating no bytes are available, "None" is
      returned.

   readinto(b, /)

      Read bytes into a pre-allocated, writable *bytes-like object*
      *b*, and return the number of bytes read.  For example, *b*
      might be a "bytearray".

      If "0" is returned and "len(b)" is not "0", this indicates end
      of file. If the object is in non-blocking mode and no bytes are
      available, "None" is returned.

   write(b, /)

      Escribe *bytes-like object* dado, *b*, al *stream* subyacente y
      retorna la cantidad de *bytes* grabadas. Esto puede ser menos
      que la longitud de *b* en *bytes*, dependiendo de la
      especificaciones del *stream* subyacente, especialmente si no
      está en modo no-bloqueo. "None" se retorna si el *stream* sin
      formato está configurado para no bloquear y ningún *byte* puede
      ser rápidamente grabada. El llamador puede deshacer o mutar *b*
      después que retorne este método, así que la implementación solo
      debería acceder *b* durante la ejecución al método.

      Advertencia:

        This function does not ensure all bytes are written or an
        exception is thrown. Callers may implement that behavior by
        checking the return value and, if it is less than the length
        of *b*, looping with additional write calls until all
        unwritten bytes are written. High-level I/O objects like E/S
        Binaria and E/S Texto implement retry behavior.

class io.BufferedIOBase

   Base class for binary streams that support some kind of buffering.
   It inherits from "IOBase".

   The main difference with "RawIOBase" is that methods "read()",
   "readinto()" and "write()" will try (respectively) to read as much
   input as requested or to emit all provided data.

   In addition, if the underlying raw stream is in non-blocking mode,
   when the system returns would block "write()" will raise
   "BlockingIOError" with "BlockingIOError.characters_written" and
   "read()" will return data read so far or "None" if no data is
   available.

   Además, el método "read()" no tiene una implementación dada que
   difiere al método "readinto()".

   Una implementación típica de "BufferedIOBase" no debería heredar
   una implementación de "RawIOBase", es más, debería envolver como
   uno, así como hacen las clases "BufferedWriter" y "BufferedReader".

   "BufferedIOBase" proporciona o anula estos atributos y métodos de
   datos además de los de "IOBase":

   raw

      El *stream* sin formato subyacente ( una instancia "RawIOBase")
      que "BufferedIOBase" maneja. Esto no es parte de la API
      "BufferedIOBase" y posiblemente no exista en algunas
      implementaciones.

   detach()

      Separa el *stream* subyacente del búfer y lo retorna.

      Luego que el *stream* sin formato ha sido separado, el búfer
      está en un estado inutilizable.

      Algunos búfer, como "BytesIO", no tienen el concepto de un
      *stream* sin formato singular para retornar de este método.
      Lanza un "UnsupportedOperation".

      Added in version 3.1.

   read(size=-1, /)

      Read and return up to *size* bytes. If the argument is omitted,
      "None", or negative read as much as possible.

      Fewer bytes may be returned than requested. An empty "bytes"
      object is returned if the stream is already at EOF. More than
      one read may be made and calls may be retried if specific errors
      are encountered, see "os.read()" and **PEP 475** for more
      details. Less than size bytes being returned does not imply that
      EOF is imminent.

      When reading as much as possible the default implementation will
      use "raw.readall" if available (which should implement
      "RawIOBase.readall()"), otherwise will read in a loop until read
      returns "None", an empty "bytes", or a non-retryable error. For
      most streams this is to EOF, but for non-blocking streams more
      data may become available.

      Nota:

        When the underlying raw stream is non-blocking,
        implementations may either raise "BlockingIOError" or return
        "None" if no data is available. "io" implementations return
        "None".

   read1(size=-1, /)

      Read and return up to *size* bytes, calling "readinto()" which
      may retry if "EINTR" is encountered per **PEP 475**. If *size*
      is "-1" or not provided, the implementation will choose an
      arbitrary value for *size*.

      Nota:

        When the underlying raw stream is non-blocking,
        implementations may either raise "BlockingIOError" or return
        "None" if no data is available. "io" implementations return
        "None".

   readinto(b, /)

      Lee *bytes* a un objeto predeterminado y grabable *bytes-like
      object* *b* y retorna el número de *bytes* leídos. Por ejemplo,
      *b* puede ser un "bytearray".

      Como "read()", varias lecturas pueden ser otorgadas al *stream*
      sin formato subyacente al menos que esto último sea interactivo.

      Un "BlockingIOError" se lanza si el *stream* subyacente está en
      modo no bloqueo y no tiene datos al momento.

   readinto1(b, /)

      Leer *bytes* a un objeto predeterminado y grabable *bytes-like
      object* *b* usando por lo menos una llamada al método "read()"
      (o "readinto()") del *stream* subyacente. Retorna la cantidad de
      *bytes* leídas.

      Un "BlockingIOError" se lanza si el *stream* subyacente está en
      modo no bloqueo y no tiene datos al momento.

      Added in version 3.5.

   write(b, /)

      Escribe el *bytes-like object* dado, *b*, y retorna el número de
      bytes grabados (siempre el equivalente en longitud de *b* en
      bytes, ya que si falla la grabación se lanza un "OSError").
      Dependiendo en la implementación actual estos bytes pueden ser
      grabados rápidamente al *stream* subyacente o mantenido en un
      búfer por razones de rendimiento y latencia.

      Cuando estás en modo no bloqueo, se lanza un "BlockingIOError"
      si los datos tenían que ser grabadas al *stream* sin formato
      pero no pudo aceptar todos los datos sin bloquear.

      El llamador puede otorgar o mutar *b* después que este método
      retorne algo, entonces la implementación debería acceder
      solamente a *b* durante la llamada al método.

### Archivo sin formato E/S

class io.FileIO(name, mode='r', closefd=True, opener=None)

   A raw binary stream representing an OS-level file containing bytes
   data.  It inherits from "RawIOBase" and implements its low-level
   access design. This means "write()" does not guarantee all bytes
   are written and "read()" may read less bytes than requested even
   when more bytes may be present in the underlying file. To get
   "write all" and "read at least" behavior, use E/S Binaria.

   El *name* puede ser una de dos cosas:

   * una cadena de caracteres u objeto de tipo "bytes" representando
     la ruta del archivo en la que fue abierto. En este caso *closefd*
     es "True" (el valor dado) de otra manera un error será dada.

   * un *integer* representando el número de descriptores de archivos
     de nivel OS que resultan dando acceso a través del objeto
     "FileIO". Cuando el objeto *FileIO* está cerrado este fd cerrará
     también a no ser que *closefd* esté configurado a "False".

   El *mode* puede ser "'r'", "'w'", "'x'" o "'a'" para lectura (el
   valor dado), grabación, creación exclusiva o anexando. Si no existe
   el archivo se creará cuando se abra para grabar o anexar; se
   truncará cuando se abra para grabar. Se lanzará un error
   "FileExistsError"   si ya existe cuando se abra para crear.
   Abriendo un archivo para crear implica grabar entonces este modo se
   comporta similarmente a "'w'". Agrega un "'+'"  al modo para
   permitir lectura y grabación simultáneas.

   Un abridor personalizado puede ser usado pasando un llamador como
   *opener*. El descriptor de archivo subyacente es obtenido llamando
   *opener* con (*name*, *flags*). *opener* debe retornar un
   descriptor de archivo abierto (pasando "os.open" como *opener*
   resulta con funcionamiento similar a pasando "None").

   El archivo recién creado es non-inheritable.

   Ver la función incorporada "open()" para ejemplos usando el
   parámetro *opener*.

   Advertencia:

     "FileIO" is a low-level I/O object and members, such as "read()"
     and "write()", need to have their return values checked
     explicitly in a retry loop to implement "write all" and "read at
     least" behavior. High-level I/O objects E/S Binaria and E/S Texto
     implement retry behavior.

   Distinto en la versión 3.3: El parámetro *opener* fue agregado. El
   modo "'x'" fue agregado.

   Distinto en la versión 3.4: El archivo ahora no es heredable.

   "FileIO" proporciona estos atributos de datos además de los de
   "RawIOBase" y "IOBase":

   mode

      El modo dado en el constructor.

   name

      El nombre del archivo. Este es el descriptor del archivo cuando
      no se proporciona ningún nombre en el constructor.

### *Streams* almacenados (búfer)

*Streams* E/S almacenadas (búfer) proveen una interfaz de más alto
nivel a un dispositivo E/S que a un E/S sin formato.

class io.BytesIO(initial_bytes=b'')

   A binary stream using an in-memory bytes buffer.  It inherits from
   "BufferedIOBase".  The buffer is discarded when the "close()"
   method is called.

   El argumento opcional *initial_bytes* es un *bytes-like object* que
   contiene datos iniciales.

   "BytesIO" provee o anula estos métodos además de los de
   "BufferedIOBase" y "IOBase":

   getbuffer()

      Retorna una vista legible y grabable acerca de los contenidos
      del búfer sin copiarlos. Además mutando la vista actualizará de
      forma transparente los contenidos del búfer:

         >>> b = io.BytesIO(b"abcdef")
         >>> view = b.getbuffer()
         >>> view[2:4] = b"56"
         >>> b.getvalue()
         b'ab56ef'

      Nota:

        Mientras exista la vista el objeto "BytesIO" no se le puede
        cambiar el tamaño o cerrado.

      Added in version 3.2.

   getvalue()

      Retorna "bytes" que contiene los contenidos enteros del búfer.

   read1(size=-1, /)

      En la clase "BytesIO" esto es lo mismo que "read()".

      Distinto en la versión 3.7: Ahora es opcional el argumento
      *size*.

   readinto1(b, /)

      En la clase "BytesIO" esto es lo mismo que "readinto()".

      Added in version 3.5.

class io.BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)

   A buffered binary stream providing higher-level access to a
   readable, non seekable "RawIOBase" raw binary stream.  It inherits
   from "BufferedIOBase".

   Al leer datos de este objeto, es posible que se solicite una mayor
   cantidad de datos del flujo sin procesar subyacente y se mantenga
   en un búfer interno. Los datos almacenados en búfer se pueden
   retornar directamente en lecturas posteriores.

   El constructor crea un "BufferedReader" para el *stream* legible
   sin formato *raw* y *buffer_size*. Si se omite *buffer_size* se usa
   "DEFAULT_BUFFER_SIZE".

   "BufferedReader" provee o anula los métodos en adición a los de
   "BufferedIOBase" y "IOBase":

   peek(size=0, /)

      Return bytes from the stream without advancing the position. The
      number of bytes returned may be less or more than requested. If
      the underlying raw stream is non-blocking and the operation
      would block, returns empty bytes.

   read(size=-1, /)

      In "BufferedReader" this is the same as
      "io.BufferedIOBase.read()"

   read1(size=-1, /)

      In "BufferedReader" this is the same as
      "io.BufferedIOBase.read1()"

      Distinto en la versión 3.7: Ahora es opcional el argumento
      *size*.

class io.BufferedWriter(raw, buffer_size=DEFAULT_BUFFER_SIZE)

   A buffered binary stream providing higher-level access to a
   writeable, non seekable "RawIOBase" raw binary stream.  It inherits
   from "BufferedIOBase".

   Al escribir en este objeto, los datos normalmente se colocan en un
   búfer interno. El búfer se escribirá en el objeto "RawIOBase"
   subyacente en varias condiciones, que incluyen:

   * cuando el búfer se vuelve demasiado pequeño para todos los datos
     pendientes;

   * when "flush()" is called;

   * when a "seek()" is requested (for "BufferedRandom" objects);

   * cuando el objeto "BufferedWriter" is cerrado o anulado.

   El constructor crea un "BufferedWriter" para el *stream* grabable
   *raw*. Si no es dado el *buffer_size*, recurre el valor
   "DEFAULT_BUFFER_SIZE".

   "BufferedWriter" provee o anula estos métodos además de los de
   "BufferedIOBase" y "IOBase":

   flush()

      Forzar bytes retenidos en el búfer al *stream* sin formato. Un
      "BlockingIOError" debería ser lanzado si el *stream* sin formato
      bloquea.

   write(b, /)

      Write the *bytes-like object*, *b*, and return the number of
      bytes written.  When in non-blocking mode, a "BlockingIOError"
      with "BlockingIOError.characters_written" set is raised if the
      buffer needs to be written out but the raw stream blocks.

class io.BufferedRandom(raw, buffer_size=DEFAULT_BUFFER_SIZE)

   A buffered binary stream implementing "BufferedIOBase" interfaces
   providing higher-level access to a seekable "RawIOBase" raw binary
   stream.

   El constructor crea un lector y una grabación para un *stream* sin
   formato buscable, dado en el primer argumento. Si se omite el
   *buffer_size* este recae sobre el valor predeterminado
   "DEFAULT_BUFFER_SIZE".

   "BufferedRandom" is capable of anything "BufferedReader" or
   "BufferedWriter" can do.  In addition, "seek()" and "tell()" are
   guaranteed to be implemented.

class io.BufferedRWPair(reader, writer, buffer_size=DEFAULT_BUFFER_SIZE, /)

   A buffered binary stream providing higher-level access to two non
   seekable "RawIOBase" raw binary streams---one readable, the other
   writeable. It inherits from "BufferedIOBase".

   *reader* y *writer* son objetos "RawIOBase" que son respectivamente
   legibles y escribibles. Si se omite *buffer_size* este se recae
   sobre el valor predeterminado "DEFAULT_BUFFER_SIZE".

   "BufferedRWPair" implementa todos los métodos de "BufferedIOBase"
   excepto por "detach()", que lanza un "UnsupportedOperation".

   Advertencia:

     "BufferedRWPair" no intenta sincronizar accesos al *stream* sin
     formato subyacente. No debes pasar el mismo objeto como legible y
     escribible; usa "BufferedRandom" en su lugar.

### E/S Texto

class io.TextIOBase

   Base class for text streams.  This class provides a character and
   line based interface to stream I/O.  It inherits from "IOBase".

   "TextIOBase" provee o anula estos atributos y métodos de datos
   además de los de "IOBase":

   encoding

      El nombre de la codificación utilizada para decodificar los
      *bytes* del *stream* a cadenas de caracteres y para codificar
      cadenas de caracteres en bytes.

   errors

      La configuración de error del decodificador o codificador.

   newlines

      Una cadena de caracteres, una tupla de cadena de caracteres, o
      "None", indicando las nuevas líneas traducidas hasta ese
      momento. Dependiendo de la implementación y los indicadores
      iniciales del constructor, esto puede no estar disponible.

   buffer

      The underlying binary buffer (a "BufferedIOBase" or "RawIOBase"
      instance) that "TextIOBase" deals with. This is not part of the
      "TextIOBase" API and may not exist in some implementations.

   detach()

      Separa el búfer binario subyacente de "TextIOBase" y lo retorna.

      Una vez que se ha separado el búfer subyacente, la "TextIOBase"
      está en un estado inutilizable.

      Algunas implementaciones de "TextIOBase", como "StringIO", puede
      no tener el concepto de un búfer subyacente y llamar a este
      método se lanzará "UnsupportedOperation".

      Added in version 3.1.

   read(size=-1, /)

      Lee y retorna como máximo *size* caracteres del *stream* como un
      "str" singular. Si *size* es negativo o "None", lee hasta llegar
      al fin del archivo.

   readline(size=-1, /)

      Read until newline or EOF and return a single "str".  If the
      stream is already at EOF, an empty string is returned.

      Si se especifica *size* como máximo *size* de caracteres será
      leído.

   seek(offset, whence=SEEK_SET, /)

      Change the stream position to the given *offset*.  Behaviour
      depends on the *whence* parameter.  The default value for
      *whence* is "SEEK_SET".

      * "SEEK_SET" or "0": seek from the start of the stream (the
        default); *offset* must either be a number returned by
        "TextIOBase.tell()", or zero.  Any other *offset* value
        produces undefined behaviour.

      * "SEEK_CUR" or "1": "seek" to the current position; *offset*
        must be zero, which is a no-operation (all other values are
        unsupported).

      * "SEEK_END" or "2": seek to the end of the stream; *offset*
        must be zero (all other values are unsupported).

      Retorna la nueva posición absoluta como un número opaco.

      Added in version 3.1: The "SEEK_*" constants.

   tell()

      Retorna la posición actual de la secuencia como un número opaco.
      El número no suele representar una cantidad de bytes en el
      almacenamiento binario subyacente.

   write(s, /)

      Escribe la cadena de caracteres *s* al *stream* y retorna el
      número de caracteres grabadas.

class io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)

   A buffered text stream providing higher-level access to a
   "BufferedIOBase" buffered binary stream.  It inherits from
   "TextIOBase".

   *encoding* gives the name of the encoding that the stream will be
   decoded or encoded with.  In UTF-8 Mode, this defaults to UTF-8.
   Otherwise, it defaults to "locale.getencoding()".
   "encoding="locale"" can be used to specify the current locale's
   encoding explicitly. See Codificación de texto for more
   information.

   *errors* es una cadena de caracteres opcional que especifica cómo
   se manejan los errores codificados y descodificados. Pasa
   "'strict'" para lanzar una excepción "ValueError" si hay un error
   codificado (el valor predeterminado "None" tiene el mismo efecto),
   o pasa "'ignore'" para ignorar errores. (Tenga en cuenta que
   ignorar errores puede llevar a perder datos). "'replace'" causa un
   marcador de reemplazo (como "'?'") para ser insertado donde haya
   datos mal formados. "'backslashreplace'" reemplaza datos mal
   formados con una secuencia de escape de tipo barra invertida.
   Cuando se escribe, "'xmlcharrefreplace'"  (reemplazar con la
   referencia apropiada de XML) o "'namereplace'" (reemplazar con
   secuencias de caracteres "\N{…}") pueden ser usadas. Cualquier otro
   nombre de manejador de errores que hayan sido registrados con
   "codecs.register_error()" también son validas.

   *newline* controla cómo finalizar las terminaciones de líneas.
   Pueden ser "None", "''", "'\n'", "'\r'", and "'\r\n'". Funciona de
   la siguiente manera:

   * Al leer la entrada de la secuencia, si *newline* es "None", el
     modo *universal newlines* está habilitado. Las líneas de la
     entrada pueden terminar en "'\n'", "'\r'" o "'\r\n'", y se
     traducen a "'\n'" antes de retornarse al llamador. Si *newline*
     es "''", el modo de salto de línea universal está habilitado,
     pero los finales de línea se retornan a la persona que llama sin
     traducir. Si *newline* tiene alguno de los otros valores legales,
     las líneas de entrada solo terminan con la cadena dada y la línea
     final se retorna al llamador sin traducir.

   * Al escribir la salida al *stream*, si *newline* es "None",
     cualquier carácter "'\n'" escrito son traducidos a la línea
     separador *default* del sistema, "os.linesep". Si *newline* es
     "''" o "'\n'", la traducción no ocurre. Si *newline* es de
     cualquier de los otros valores legales, cualquier carácter "'\n'"
     escrito es traducido a la cadena de caracteres dada.

   If *line_buffering* is "True", "flush()" is implied when a call to
   write contains a newline character or a carriage return.

   If *write_through* is "True", calls to "write()" are guaranteed not
   to be buffered: any data written on the "TextIOWrapper" object is
   immediately handled to its underlying binary *buffer*.

   Distinto en la versión 3.3: Se ha agregado el argumento
   *write_through*.

   Distinto en la versión 3.3: La codificación (*encoding*) por
   defecto es ahora "locale.getpreferredencoding(False)" en vez de
   "locale.getpreferredencoding()". No cambie temporalmente la
   codificación local usando "locale.setlocale()", use la codificación
   local actual en vez del preferido del usuario.

   Distinto en la versión 3.10: El argumento *encoding* ahora admite
   el nombre de codificación ficticia ""locale"".

   Nota:

     When the underlying raw stream is non-blocking, a
     "BlockingIOError" may be raised if a read operation cannot be
     completed immediately.

   "TextIOWrapper" proporciona estos atributos y métodos de datos
   además de los de "TextIOBase" y "IOBase":

   line_buffering

      Si el almacenamiento en línea está habilitado.

   write_through

      Si grabaciones son pasadas inmediatamente al búfer binario
      subyacente.

      Added in version 3.7.

   reconfigure(*, encoding=None, errors=None, newline=None, line_buffering=None, write_through=None)

      Reconfigura este *stream* textual usando las nuevas
      configuraciones de *encoding*, *errors*, *newline*,
      *line_buffering* y *write_through*.

      Los parámetros que no son especificados mantienen las
      configuraciones actuales, excepto por "errors='strict'" cuando
      *encoding* se especifica pero *errors* no está especificado.

      No es posible cambiar la codificación o nueva línea si algunos
      datos han sido captados por el *stream*. Sin embargo, cambiando
      la codificación después de grabar es posible.

      Este método hace una nivelación implícita del *stream* antes de
      configurar los nuevos parámetros.

      Added in version 3.7.

      Distinto en la versión 3.11: El método admite la opción
      "encoding="locale"".

   seek(cookie, whence=os.SEEK_SET, /)

      Set the stream position. Return the new stream position as an
      "int".

      Four operations are supported, given by the following argument
      combinations:

      * "seek(0, SEEK_SET)": Rewind to the start of the stream.

      * "seek(cookie, SEEK_SET)": Restore a previous position;
        *cookie* **must be** a number returned by "tell()".

      * "seek(0, SEEK_END)": Fast-forward to the end of the stream.

      * "seek(0, SEEK_CUR)": Leave the current stream position
        unchanged.

      Any other argument combinations are invalid, and may raise
      exceptions.

      Ver también: "os.SEEK_SET", "os.SEEK_CUR", and "os.SEEK_END".

   tell()

      Return the stream position as an opaque number. The return value
      of "tell()" can be given as input to "seek()", to restore a
      previous stream position.

class io.StringIO(initial_value='', newline='\n')

   A text stream using an in-memory text buffer.  It inherits from
   "TextIOBase".

   El búfer de texto se descarta cuando se llama al método "close()".

   El valor inicial del búfer se puede establecer proporcionando
   *initial_value*. Si la traducción de nuevas líneas está habilitada,
   las nuevas líneas se codificarán como si fueran "write()". La
   secuencia se coloca al comienzo del búfer que emula la apertura de
   un archivo existente en un modo "w+" , preparándolo para una
   escritura inmediata desde el principio o para una escritura que
   sobrescribiría el valor inicial. Para emular la apertura de un
   archivo en un modo "a+" listo para anexar, use "f.seek(0,
   io.SEEK_END)" para reponer la secuencia al final del búfer.

   El argumento *newline* funciona como el de la clase
   "TextIOWrapper", excepto que cuando escribe al flujo de salida, si
   *newline* es "None", se escriben líneas nuevas como "\n" en todas
   las plataformas

   "StringIO" proporciona este método además de los de "TextIOBase" y
   "IOBase":

   getvalue()

      Return a "str" containing the entire contents of the buffer.
      Newlines are decoded as if by "read()", although the stream
      position is not changed.

   Ejemplos de uso:

      import io

      output = io.StringIO()
      output.write('First line.\n')
      print('Second line.', file=output)

      # Retrieve file contents -- this will be
      # 'First line.\nSecond line.\n'
      contents = output.getvalue()

      # Close object and discard memory buffer --
      # .getvalue() will now raise an exception.
      output.close()

class io.IncrementalNewlineDecoder

   A helper codec that decodes newlines for *universal newlines* mode.
   It inherits from "codecs.IncrementalDecoder".

## Static Typing

The following protocols can be used for annotating function and method
arguments for simple stream reading or writing operations. They are
decorated with "@typing.runtime_checkable".

class io.Reader[T]

   Generic protocol for reading from a file or other input stream. "T"
   will usually be "str" or "bytes", but can be any type that is read
   from the stream.

   Added in version 3.14.

   read()
   read(size, /)

      Read data from the input stream and return it. If *size* is
      specified, it should be an integer, and at most *size* items
      (bytes/characters) will be read.

   For example:

      def read_it(reader: Reader[str]):
          data = reader.read(11)
          assert isinstance(data, str)

class io.Writer[T]

   Generic protocol for writing to a file or other output stream. "T"
   will usually be "str" or "bytes", but can be any type that can be
   written to the stream.

   Added in version 3.14.

   write(data, /)

      Write *data* to the output stream and return the number of items
      (bytes/characters) written.

   For example:

      def write_binary(writer: Writer[bytes]):
          writer.write(b"Hello world!\n")

See ABCs and Protocols for working with I/O for other I/O related
protocols and classes that can be used for static type checking.

## Rendimiento

Esta sección discute el rendimiento de las implementaciones concretas
de E/S proporcionadas.

### E/S Binaria

Leyendo y grabando solamente grandes porciones de datos incluso cuando
el usuario pide para solo un byte, E/S de tipo búfer esconde toda
ineficiencia llamando y ejecutando las rutinas E/S del sistema
operativo que no ha pasado por el proceso de búfer. La ganancia
depende en el OS y el tipo de E/S que se ejecuta. Por ejemplo, en
algunos sistemas operativos modernos como Linux, un disco E/S sin
búfer puede ser rápido como un E/S búfer. Al final, sin embargo, es
que el E/S búfer ofrece rendimiento predecible independientemente de
la plataforma y el dispositivo de respaldo. Entonces es siempre
preferible user E/S búfer que E/S sin búfer para datos binarios.

### E/S Texto

Text I/O over a binary storage (such as a file) is significantly
slower than binary I/O over the same storage, because it requires
conversions between unicode and binary data using a character codec.
This can become noticeable handling huge amounts of text data like
large log files.  Also, "tell()" and "seek()" are both quite slow due
to the reconstruction algorithm used.

"StringIO", sin embargo, es un contenedor unicode nativo en memoria y
exhibirá una velocidad similar a "BytesIO".

### Multihilo

"FileIO" objects are thread-safe to the extent that the operating
system calls (such as *read(2)* under Unix) they wrap are thread-safe
too.

Objetos binarios búfer (instancias de "BufferedReader",
"BufferedWriter", "BufferedRandom" y "BufferedRWPair") protegen sus
estructuras internas usando un bloqueo; es seguro, entonces, llamarlos
de varios hilos a la vez.

objetos "TextIOWrapper" no son seguros para subprocesos.

### Reentrada

Objetos binarios búfer (instancias de "BufferedReader",
"BufferedWriter", "BufferedRandom" y "BufferedRWPair") no son
reentrante. Mientras llamadas reentrantes no ocurren en situaciones
normales pueden surgir haciendo E/S en un manejador "signal". Si un
hilo trata de entrar de nuevo a un objeto búfer que se está accediendo
actualmente, se lanza un "RuntimeError". Tenga en cuenta que esto no
prohíbe un hilo diferente entrando un objeto búfer.

The above implicitly extends to text files, since the "open()"
function will wrap a buffered object inside a "TextIOWrapper".  This
includes standard streams and therefore affects the built-in "print()"
function as well.
