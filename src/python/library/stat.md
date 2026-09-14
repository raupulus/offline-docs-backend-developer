---
title: '"stat" --- Interpreting "stat()" results'
source_url: https://docs.python.org/es/3
source_path: library/stat.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3890
---

# "stat" --- Interpreting "stat()" results

**Código fuente:** Lib/stat.py

======================================================================

The "stat" module defines constants and functions for interpreting the
results of "os.stat()", "os.fstat()" and "os.lstat()" (if they exist).
For complete details about the "stat()", "fstat()" and "lstat()"
calls, consult the documentation for your system.

Distinto en la versión 3.4: El módulo *stat* se apoya en una
implementación en C.

The "stat" module defines the following functions to test for specific
file types:

stat.S_ISDIR(mode)

   Retorna un valor no nulo si el modo es de un directorio.

stat.S_ISCHR(mode)

   Retorna un valor no nulo si el modo es de un archivo de un
   dispositivo especial de caracteres.

stat.S_ISBLK(mode)

   Retorna un valor no nulo si el modo es de un archivo de un
   dispositivo especial de bloques.

stat.S_ISREG(mode)

   Retorna un valor no nulo si el modo es de un archivo normal.

stat.S_ISFIFO(mode)

   Retorna un valor no nulo si el modo es de un *FIFO* (tubería con
   nombre).

stat.S_ISLNK(mode)

   Retorna un valor no nulo si el modo es de un enlace simbólico.

stat.S_ISSOCK(mode)

   Retorna un valor no nulo si el modo es de un socket.

stat.S_ISDOOR(mode)

   Retorna un valor no nulo si el modo es de un *door*.

   Added in version 3.4.

stat.S_ISPORT(mode)

   Retorna un valor no nulo si el modo es de un *event port*.

   Added in version 3.4.

stat.S_ISWHT(mode)

   Retorna un valor no nulo si el modo es de un *whiteout*.

   Added in version 3.4.

Se definen dos funciones adicionales para una manipulación más general
del modo del archivo:

stat.S_IMODE(mode)

   Retorna la porción del modo del archivo que puede ser establecida
   por "os.chmod()"--- esto es, los bits de los permisos del archivo
   más los bits *sticky bit*, *set-group-id* y *set-user-id* (en los
   sistemas que lo soporten).

stat.S_IFMT(mode)

   Retorna la porción del modo del archivo que describe el tipo de
   archivo (usado por las funciones "S_IS*()" de más arriba).

Normalmente se usarían las funciones "os.path.is*()" para comprobar el
tipo de un archivo; estas funciones de aquí son útiles cuando se hacen
múltiples comprobaciones sobre el mismo archivo y se desea evitar la
sobrecarga causada por la llamada al sistema "stat()" en cada
comprobación. También son útiles cuando se comprueba información de un
archivo que no es gestionada por "os.path", como buscar dispositivos
de bloques o caracteres.

Ejemplo:

   import os, sys
   from stat import *

   def walktree(top, callback):
       '''recursively descend the directory tree rooted at top,
          calling the callback function for each regular file'''

       for f in os.listdir(top):
           pathname = os.path.join(top, f)
           mode = os.lstat(pathname).st_mode
           if S_ISDIR(mode):
               # It's a directory, recurse into it
               walktree(pathname, callback)
           elif S_ISREG(mode):
               # It's a file, call the callback function
               callback(pathname)
           else:
               # Unknown file type, print a message
               print('Skipping %s' % pathname)

   def visitfile(file):
       print('visiting', file)

   if __name__ == '__main__':
       walktree(sys.argv[1], visitfile)

Se proporciona una función de utilidad adicional para convertir el
modo del archivo en una cadena de caracteres legible por humanos:

stat.filemode(mode)

   Convierte el modo del archivo a una cadena de caracteres de la
   forma '-rwxrwxrwx'.

   Added in version 3.3.

   Distinto en la versión 3.4: La función soporta "S_IFDOOR",
   "S_IFPORT" y "S_IFWHT".

Todas las variables de debajo son simplemente índices simbólicos sobre
la tupla de 10 elementos retornada por "os.stat()", "os.fstat()" o
"os.lstat()".

stat.ST_MODE

   Modo de protección del *inode*.

stat.ST_INO

   Número del *inode*.

stat.ST_DEV

   Dispositivo en el que reside el *inode*.

stat.ST_NLINK

   Número de enlaces al *inode*.

stat.ST_UID

   *Id* de usuario del propietario.

stat.ST_GID

   *Id* del grupo del propietario.

stat.ST_SIZE

   Tamaño en bytes de un archivo normal; cantidad de datos esperando
   en algunos archivos especiales.

stat.ST_ATIME

   Momento del último acceso.

stat.ST_MTIME

   Momento de la última modificación.

stat.ST_CTIME

   El "ctime" reportado por el sistema operativo. En algunos sistemas
   (como Unix) es el momento del último cambio en los metadatos, y en
   otros (como Windows), es el momento de creación (véase la
   documentación de la plataforma para más detalles).

La interpretación de "tamaño de archivo" cambia dependiendo del tipo
de archivo. Para archivos normales es el tamaño del archivo en bytes.
En la mayoría de sistemas Unix (incluyendo Linux en particular), para
*FIFOs* y sockets es el número de bytes que esperan ser leídos en el
momento de la llamada a "os.stat()", "os.fstat()", o "os.lstat()"; en
ocasiones, esto puede ser útil, especialmente para sondear uno de
estos archivos especiales después de una apertura no bloqueante. Para
otros dispositivos de caracteres y bloques el significado del campo
*size* es más variado, dependiendo de la implementación de la llamada
al sistema subyacente.

Las variables de debajo definen los flags usados en el campo
"ST_MODE".

El uso de las funciones de arriba es más portable que el uso del
primer juego de flags:

stat.S_IFSOCK

   *Socket*.

stat.S_IFLNK

   Enlace simbólico.

stat.S_IFREG

   Archivo normal.

stat.S_IFBLK

   Dispositivo de bloques.

stat.S_IFDIR

   Directorio.

stat.S_IFCHR

   Dispositivo de caracteres.

stat.S_IFIFO

   *FIFO*.

stat.S_IFDOOR

   *Door*.

   Added in version 3.4.

stat.S_IFPORT

   *Event port*.

   Added in version 3.4.

stat.S_IFWHT

   *Whiteout*.

   Added in version 3.4.

Nota:

  "S_IFDOOR", "S_IFPORT" o "S_IFWHT" se definen como 0 cuando la
  plataforma no soporta los tipos de archivo.

Los siguientes flags también pueden usarse en el argumento *mode* de
"os.chmod()":

stat.S_ISUID

   Establecer el bit *UID*.

stat.S_ISGID

   Bit *Set-group-ID*. Este bit tiene varios usos especiales. Para un
   directorio indica que la semántica BSD debe usarse para ese
   directorio: los archivos creados ahí heredan el *ID* de grupo del
   directorio, no del *ID* de grupo efectivo del proceso que los crea,
   y los directorios creados ahí también tendrán activado el bit
   "S_ISGID". Para un archivo que no tiene activado el bit de
   ejecución de grupo ("S_IXGRP"), el bit *Set-group-ID* indica el
   bloqueo obligatorio del archivo/registro (véase también "S_ENFMT").

stat.S_ISVTX

   *Sticky bit*. Cuando este bit está activado en un directorio,
   significa que un archivo dentro de ese directorio puede ser
   renombrado o borrado sólo por el propietario del archivo, por el
   propietario del directorio, o por un proceso con privilegios.

stat.S_IRWXU

   Máscara para los permisos del propietario del archivo.

stat.S_IRUSR

   El propietario tiene permiso de lectura.

stat.S_IWUSR

   El propietario tiene permiso de escritura.

stat.S_IXUSR

   El propietario tiene permiso de ejecución.

stat.S_IRWXG

   Máscara para los permisos del grupo.

stat.S_IRGRP

   El grupo tiene permiso de lectura.

stat.S_IWGRP

   El grupo tiene permiso de escritura.

stat.S_IXGRP

   El grupo tiene permiso de ejecución.

stat.S_IRWXO

   Máscara para permisos de los otros (no en el grupo).

stat.S_IROTH

   Los otros tienen permiso de lectura.

stat.S_IWOTH

   Los otros tienen permiso de escritura.

stat.S_IXOTH

   Los otros tienen permiso de ejecución.

stat.S_ENFMT

   Imposición del bloqueo de archivos de System V. Este flag se
   comparte con "S_ISGID": se impone el bloqueo de archivos/registros
   en archivos que no tengan activado el bit de ejecución por el grupo
   ("S_IXGRP").

stat.S_IREAD

   Sinónimo de "S_IRUSR" en Unix V7.

stat.S_IWRITE

   Sinónimo de "S_IWUSR" en Unix V7.

stat.S_IEXEC

   Sinónimo de "S_IXUSR" en Unix V7.

Los siguientes flags pueden usarse como argumento *flags* de
"os.chflags()":

stat.UF_SETTABLE

   All user settable flags.

   Added in version 3.13.

stat.UF_NODUMP

   No volcar el archivo.

stat.UF_IMMUTABLE

   El archivo no puede ser modificado.

stat.UF_APPEND

   Sólo se puede añadir al archivo.

stat.UF_OPAQUE

   El directorio es opaco cuando se mira a través de un *union stack*.

stat.UF_NOUNLINK

   El archivo no puede ser renombrado o borrado.

stat.UF_COMPRESSED

   El archivo se almacena comprimido (macOS 10.6+).

stat.UF_TRACKED

   Used for handling document IDs (macOS)

   Added in version 3.13.

stat.UF_DATAVAULT

   The file needs an entitlement for reading or writing (macOS 10.13+)

   Added in version 3.13.

stat.UF_HIDDEN

   El archivo no debe ser mostrado en una GUI (macOS 10.5+).

stat.SF_SETTABLE

   All super-user changeable flags

   Added in version 3.13.

stat.SF_SUPPORTED

   All super-user supported flags

   Availability: macOS

   Added in version 3.13.

stat.SF_SYNTHETIC

   All super-user read-only synthetic flags

   Availability: macOS

   Added in version 3.13.

stat.SF_ARCHIVED

   El archivo puede ser archivado.

stat.SF_IMMUTABLE

   El archivo no puede ser modificado.

stat.SF_APPEND

   Sólo se puede añadir al archivo.

stat.SF_RESTRICTED

   The file needs an entitlement to write to (macOS 10.13+)

   Added in version 3.13.

stat.SF_NOUNLINK

   El archivo no puede ser renombrado o borrado.

stat.SF_SNAPSHOT

   El archivo es una instantánea.

stat.SF_FIRMLINK

   The file is a firmlink (macOS 10.15+)

   Added in version 3.13.

stat.SF_DATALESS

   The file is a dataless object (macOS 10.15+)

   Added in version 3.13.

Consulte la página de manual de sistemas * BSD o macOS *chflags(2)*
para obtener más información.

En Windows, las siguientes constantes de atributos de fichero están
disponibles para ser usadas al comprobar los bits del miembro
"st_file_attributes" retornado por "os.stat()". Véase Windows API
documentation para más detalles sobre el significado de estas
constantes.

stat.FILE_ATTRIBUTE_ARCHIVE
stat.FILE_ATTRIBUTE_COMPRESSED
stat.FILE_ATTRIBUTE_DEVICE
stat.FILE_ATTRIBUTE_DIRECTORY
stat.FILE_ATTRIBUTE_ENCRYPTED
stat.FILE_ATTRIBUTE_HIDDEN
stat.FILE_ATTRIBUTE_INTEGRITY_STREAM
stat.FILE_ATTRIBUTE_NORMAL
stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
stat.FILE_ATTRIBUTE_NO_SCRUB_DATA
stat.FILE_ATTRIBUTE_OFFLINE
stat.FILE_ATTRIBUTE_READONLY
stat.FILE_ATTRIBUTE_REPARSE_POINT
stat.FILE_ATTRIBUTE_SPARSE_FILE
stat.FILE_ATTRIBUTE_SYSTEM
stat.FILE_ATTRIBUTE_TEMPORARY
stat.FILE_ATTRIBUTE_VIRTUAL

   Added in version 3.5.

En Windows, las siguientes constantes están disponibles para la
comparación con el miembro "st_reparse_tag" retornado por
"os.lstat()". Estas constantes son muy conocidas, pero no se trata de
una lista exhaustiva.

stat.IO_REPARSE_TAG_SYMLINK
stat.IO_REPARSE_TAG_MOUNT_POINT
stat.IO_REPARSE_TAG_APPEXECLINK

   Added in version 3.8.
