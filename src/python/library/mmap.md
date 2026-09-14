---
title: '"mmap" --- Memory-mapped file support'
source_url: https://docs.python.org/es/3
source_path: library/mmap.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3230
---

# "mmap" --- Memory-mapped file support

======================================================================

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

Los objetos de archivos mapeados en memoria se comportan como objetos
de tipo "bytearray" y *objetos archivo*.  Puedes usar objetos mmap en
la mayoría de lugares donde se esperen objetos de tipo "bytearray";
por ejemplo, puedes usar el módulo "re" para buscar entre un archivo
mapeado en memoria.  También puedes cambiar un solo byte al hacer
"obj[index]==97", o cambiar una subsecuencia al asignarle una
rebanada: "obj[i1:i2] = b'...'".  También puedes leer y escribir datos
que empiezan en la posición del archivo actual, y utilizar el método
"seek()" a través del archivo para cambiar la posición actual.

A memory-mapped file is created by the "mmap" constructor, which is
different on Unix and on Windows.  In either case you must provide a
file descriptor for a file opened for update. If you wish to map an
existing Python file object, use its "fileno()" method to obtain the
correct value for the *fileno* parameter.  Otherwise, you can open the
file using the "os.open()" function, which returns a file descriptor
directly (the file still needs to be closed when done).

Nota:

  Si quieres crear un mapeado en memoria para un archivo con permisos
  de escritura y en el búfer, debes ejecutar la función "flush()". Es
  necesario para asegurar que las modificaciones locales a los búfer
  estén realmente disponible para el mapeado.

Para las versiones del constructor de tanto Unix como de Windows,
*access* puede ser especificado como un parámetro nombrado opcional.
*access* acepta uno de cuatro valores: "ACCESS_READ", "ACCESS_WRITE",
o "ACCESS_COPY" para especificar una memoria de solo lectura, *write-
through*, o *copy-on-write* respectivamente, o "ACCES_DEFAULT" para
deferir a *prot*. El parámetro *access* se puede usar tanto en Unix
como en Windows.  Si *access* no es especificado, el mmap de Windows
retorna un mapeado *write-through*.  Los valores de la memoria inicial
para los tres tipos de acceso son tomados del archivo especificado.
La asignación a una mapa de memoria "ACCESS_READ" lanza una excepción
"TypeError".  La asignación a un mapa de memoria "ACCESS_WRITE" afecta
tanto a la memoria como al archivo subyacente.  La asignación a un
mapa de memoria "ACCES_COPY" afecta a la memoria pero no actualiza el
archivo subyacente.

Distinto en la versión 3.7: Se añadió la constante "ACCESS_DEFAULT".

Para mapear memoria anónima, se debe pasar -1 como el *fileno* junto
con la longitud.

class mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT, offset=0)

   **(En la versión de Windows)** Mapea *length* bytes desde el
   archivo especificado por el gestor de archivo *fileno*, y crea un
   objeto mmap. Si *length* es más largo que el tamaño actual del
   archivo, el archivo es extendido para contener *length* bytes. Si
   *length* es "0", la longitud máxima del map es la tamaño actual del
   archivo, salvo que si el archivo está vacío Windows lanza una
   excepción (no puedes crear un mapeado vacío en Windows)

   *tagname*, if specified and not "None", is a string giving a tag
   name for the mapping.  Windows allows you to have many different
   mappings against the same file.  If you specify the name of an
   existing tag, that tag is opened, otherwise a new tag of this name
   is created.  If this parameter is omitted or "None", the mapping is
   created without a name.  Avoiding the use of the *tagname*
   parameter will assist in keeping your code portable between Unix
   and Windows.

   *offset* puede ser especificado como un *offset* entero no
   negativo. las referencias de mmap serán relativas al *offset* desde
   el comienzo del archivo. *offset* es por defecto 0. *offset* debe
   ser un múltiplo de "ALLOCATIONGRANULARITY".

   Lanza un evento de inspección "mmap.__new__" con los argumentos
   "fileno", "length", "access", "offset".

class mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE | PROT_READ, access=ACCESS_DEFAULT, offset=0, *, trackfd=True)

   **(En la versión de Unix)** Mapea *length* bytes desde el archivo
   especificado por el descriptor de archivo *fileno*, y retorna un
   objeto mmap.  Si *length* es "0", la longitud máxima del map será
   el tamaño actual del archivo cuando "mmap" sea llamado.

   *flags* especifica la naturaleza del mapeado. "MAP_PRIVATE" crea un
   mapeado *copy-on-write* privado, por lo que los cambios al
   contenido del objeto mmap serán privados para este proceso, y
   "MAP_SHARED" crea un mapeado que es compartido con todos los demás
   procesos que mapean las mismas áreas del archivo.  El valor por
   defecto es "MAP_SHARED". Algunos tipos tienen posibles banderas
   adicionales con la lista completa en MAP_* constants.

   *prot*, si se especifica, proporciona la protección de memoria
   deseado; los dos valores más útiles son "PROT_READ" y "PROT_WRITE",
   para especificar que las páginas puedan ser escritas o leídas.
   *prot* es por defecto "PROT_READ|PROT_WRITE".

   *access* puede ser especificado en lugar de *flags* y *prot* como
   un parámetro nombrado opcional.  Es un error especificar tanto
   *flags*, *prot* como *access*. Véase la descripción de *access*
   arriba por información de cómo usar este parámetro.

   *offset* puede ser especificado como un *offset* entero no
   negativo. Las referencias serán relativas al *offset* desde el
   comienzo del archivo. *offset* por defecto es 0. *offset* debe ser
   un múltiplo de "ALLOCATIONGRANULARITY" que es igual a "PAGESIZE" en
   los sistemas Unix.

   If *trackfd* is "False", the file descriptor specified by *fileno*
   will not be duplicated, and the resulting "mmap" object will not be
   associated with the map's underlying file. This means that the
   "size()" and "resize()" methods will fail. This mode is useful to
   limit the number of open file descriptors.

   To ensure validity of the created memory mapping the file specified
   by the descriptor *fileno* is internally automatically synchronized
   with the physical backing store on macOS.

   Distinto en la versión 3.13: The *trackfd* parameter was added.

   Este ejemplo muestra un forma simple de usar "mmap":

      import mmap

      # write a simple example file
      with open("hello.txt", "wb") as f:
          f.write(b"Hello Python!\n")

      with open("hello.txt", "r+b") as f:
          # memory-map the file, size 0 means whole file
          mm = mmap.mmap(f.fileno(), 0)
          # read content via standard file methods
          print(mm.readline())  # prints b"Hello Python!\n"
          # read content via slice notation
          print(mm[:5])  # prints b"Hello"
          # update content using slice notation;
          # note that new content must have same size
          mm[6:] = b" world!\n"
          # ... and read again using standard file methods
          mm.seek(0)
          print(mm.readline())  # prints b"Hello  world!\n"
          # close the map
          mm.close()

   "mmap" también puede ser usado como un gestor de contexto en una
   sentencia "with"

      import mmap

      with mmap.mmap(-1, 13) as mm:
          mm.write(b"Hello world!")

   Added in version 3.2: Soporte del gestor de contexto.

   El siguiente ejemplo demuestra como crear un mapa anónimo y cambiar
   los datos entre los procesos padre e hijo:

      import mmap
      import os

      mm = mmap.mmap(-1, 13)
      mm.write(b"Hello world!")

      pid = os.fork()

      if pid == 0:  # In a child process
          mm.seek(0)
          print(mm.readline())

          mm.close()

   Lanza un evento de inspección "mmap.__new__" con los argumentos
   "fileno", "length", "access", "offset".

   Los objetos de archivos mapeados en memoria soportan los siguiente
   métodos:

   close()

      Cierra el mmap. Las llamadas posteriores a otros métodos del
      objeto resultarán en que se lance una excepción *ValueError*.
      Esto no cerrará el archivo abierto.

   closed

      "True" si el archivo está cerrado.

      Added in version 3.2.

   find(sub[, start[, end]])

      Retorna el índice mínimo en el objeto donde la subsecuencia
      *sub* es hallada, tal que *sub* este contenido en el rango
      [*start*, *end*]. Los argumentos opcionales *start* y *end* son
      interpretados como en una notación de rebanada. Retorna "-1" si
      falla.

      Distinto en la versión 3.5: Ahora el objeto *bytes-like object*
      con permisos de escritura se acepta.

   flush()
   flush(offset, size, /)

      Transmite los cambios hechos a la copia en memoria de una
      archivo de vuelta al archivo. Sin el uso de esta llamada no hay
      garantía que los cambios sean escritos de vuelta antes de que
      los objetos sean destruidos.  Si *offset* y *size* son
      especificados, solo los cambios al rango de bytes dado serán
      transmitidos al disco; de otra forma, la extensión completa al
      mapeado se transmite.  *offset* debe ser un múltiplo de la
      constante "PAGESIZE" o "ALLOCATIONGRANULARITY".

      Se retorna "None" para indicar éxito.  Una excepción es lanzada
      cuando la llamada falla.

      Distinto en la versión 3.8: Anteriormente, se retornaba un valor
      diferente de cero cuando era exitoso; se retornaba cero cuando
      pasaba un error en Windows.  Se retornaba un valor de cero
      cuando era exitoso; se lanzaba una excepción cuando pasaba un
      error en Unix.

   madvise(option[, start[, length]])

      Envía un aviso *option* al kernel sobre la región de la memoria
      que comienza con *start* y se extiende *length* bytes.  *option*
      debe ser una de las constantes MADV_* disponibles en el sistema.
      Si *start* y *end* se omiten, se abarca al mapeo entero.  En
      algunos sistemas (incluyendo Linux), *start* debe ser un
      múltiplo de "PAGESIZE".

      Disponibilidad: Sistemas con la llamada al sistema "madvise()".

      Added in version 3.8.

   move(dest, src, count)

      Copia los *count* bytes empezando en el *offset* *src* al índice
      de destino *dest*.  Si el mmap fue creado con "ACCESS_READ",
      entonces las llamadas lanzaran una excepción "TypeError".

   read([n])

      Retorna una clase "bytes" que contiene hasta *n* bytes empezando
      desde la posición del archivo actual. Si se omite el argumento,
      es "None" o negativo, retorna todos los bytes desde la posición
      actual del archivo hasta el final del mapeado. Se actualiza la
      posición del archivo para apuntar después de los bytes que se
      retornaron.

      Distinto en la versión 3.3: El argumento puede ser omitido o ser
      "None".

   read_byte()

      Retorna un byte en la posición actual del archivo como un
      entero, y avanza la posición del archivo por 1.

   readline()

      Retorna una sola línea, comenzando en la posición actual del
      archivo y hasta la siguiente nueva línea. La posición del
      archivo se actualiza para apuntar después de los bytes que se
      retornaron.

   resize(newsize)

      Resizes the map and the underlying file, if any.

      Resizing a map created with *access* of "ACCESS_READ" or
      "ACCESS_COPY", will raise a "TypeError" exception. Resizing a
      map created with *trackfd* set to "False", will raise a
      "ValueError" exception.

      **En Windows**: cambiar el tamaño del mapa generará un "OSError"
      si hay otros mapas contra el archivo con el mismo nombre.
      Cambiar el tamaño de un mapa anónimo (es decir, contra el
      archivo de paginación) creará silenciosamente un nuevo mapa con
      los datos originales copiado hasta la longitud del nuevo tamaño.

      Distinto en la versión 3.11: Falla correctamente si se intenta
      cambiar el tamaño cuando se sostiene otro mapa. Permite cambiar
      el tamaño contra un mapa anónimo en Windows

   rfind(sub[, start[, end]])

      Retorna el índice más alto en el objeto donde la subsecuencia
      *sub* se encuentre, tal que *sub* sea contenido en el rango
      [*start*, *end*]. Los argumentos opcionales *start* y *end* son
      interpretados como un notación de rebanada. Retorna "-1" si
      falla.

      Distinto en la versión 3.5: Ahora el objeto *bytes-like object*
      con permisos de escritura se acepta.

   seek(pos[, whence])

      Establece la posición actual del archivo.  El argumento *whence*
      es opcional y es por defecto "os.SEEK_SET" o "0"
      (posicionamiento del archivo absoluto); otros valores son
      "os.SEEK_CUR" o "1" (búsqueda relativa a la posición actual) y
      "os.SEEK_END" o "2" (búsqueda relativa al final del archivo).

      Distinto en la versión 3.13: Return the new absolute position
      instead of "None".

   seekable()

      Return whether the file supports seeking, and the return value
      is always "True".

      Added in version 3.13.

   size()

      Retorna el tamaño del archivo, que puede ser más grande que el
      tamaño del área mapeado en memoria.

   tell()

      Retorna la posición actual del puntero del archivo.

   write(bytes)

      Escribe los bytes en *bytes* en memoria en la posición actual
      del puntero del archivo y retorna el números de bytes escritos
      (nunca menos que "len(bytes)", ya que si la escritura falla, una
      excepción "ValueError" será lanzada).  La posición del archivo
      es actualizada para apuntar después de los bytes escritos.  Si
      el mmap fue creado con "ACCESS_READ", entonces escribirlo
      lanzará una excepción "TypeError".

      Distinto en la versión 3.5: Ahora el objeto *bytes-like object*
      con permisos de escritura se acepta.

      Distinto en la versión 3.6: Ahora se retorna el número de bytes
      escritos.

   write_byte(byte)

      Escribe el entero *byte* en la memoria en la posición actual del
      puntero del archivo; se avanza la posición del archivo por "1".
      Si el mmap es creado con "ACCES_READ", entonces escribirlo hará
      que se lance la excepción "TypeError".

## Constantes MADV_*

mmap.MADV_NORMAL
mmap.MADV_RANDOM
mmap.MADV_SEQUENTIAL
mmap.MADV_WILLNEED
mmap.MADV_DONTNEED
mmap.MADV_REMOVE
mmap.MADV_DONTFORK
mmap.MADV_DOFORK
mmap.MADV_HWPOISON
mmap.MADV_MERGEABLE
mmap.MADV_UNMERGEABLE
mmap.MADV_SOFT_OFFLINE
mmap.MADV_HUGEPAGE
mmap.MADV_NOHUGEPAGE
mmap.MADV_DONTDUMP
mmap.MADV_DODUMP
mmap.MADV_FREE
mmap.MADV_NOSYNC
mmap.MADV_AUTOSYNC
mmap.MADV_NOCORE
mmap.MADV_CORE
mmap.MADV_PROTECT
mmap.MADV_FREE_REUSABLE
mmap.MADV_FREE_REUSE

   Se pueden pasar estas opciones al método "mmap.madvise()".  No
   todas las opciones estarán presentes en todos los sistemas.

   Disponibilidad: Sistemas con la llamada al sistema *madvise()*.

   Added in version 3.8.

## Constantes MAP_*

mmap.MAP_SHARED
mmap.MAP_PRIVATE
mmap.MAP_32BIT
mmap.MAP_ALIGNED_SUPER
mmap.MAP_ANON
mmap.MAP_ANONYMOUS
mmap.MAP_CONCEAL
mmap.MAP_DENYWRITE
mmap.MAP_EXECUTABLE
mmap.MAP_HASSEMAPHORE
mmap.MAP_JIT
mmap.MAP_NOCACHE
mmap.MAP_NOEXTEND
mmap.MAP_NORESERVE
mmap.MAP_POPULATE
mmap.MAP_RESILIENT_CODESIGN
mmap.MAP_RESILIENT_MEDIA
mmap.MAP_STACK
mmap.MAP_TPRO
mmap.MAP_TRANSLATED_ALLOW_EXECUTE
mmap.MAP_UNIX03

   These are the various flags that can be passed to "mmap.mmap()".
   "MAP_ALIGNED_SUPER" is only available at FreeBSD and "MAP_CONCEAL"
   is only available at OpenBSD.  Note that some options might not be
   present on some systems.

   Distinto en la versión 3.10: Added "MAP_POPULATE" constant.

   Added in version 3.11: Added "MAP_STACK" constant.

   Added in version 3.12: Added "MAP_ALIGNED_SUPER" and "MAP_CONCEAL"
   constants.

   Added in version 3.13: Added "MAP_32BIT", "MAP_HASSEMAPHORE",
   "MAP_JIT", "MAP_NOCACHE", "MAP_NOEXTEND", "MAP_NORESERVE",
   "MAP_RESILIENT_CODESIGN", "MAP_RESILIENT_MEDIA", "MAP_TPRO",
   "MAP_TRANSLATED_ALLOW_EXECUTE", and "MAP_UNIX03" constants.
