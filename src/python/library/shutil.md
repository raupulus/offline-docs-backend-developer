---
title: '"shutil" --- High-level file operations'
source_url: https://docs.python.org/es/3
source_path: library/shutil.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3780
---

# "shutil" --- High-level file operations

Código fuente: Lib/shutil.py

======================================================================

The "shutil" module offers a number of high-level operations on files
and collections of files.  In particular, functions are provided
which support file copying and removal. For operations on individual
files, see also the "os" module.

Advertencia:

  Incluso las funciones de copia de archivos de nivel superior
  ("shutil.copy()", "shutil.copy2()") no pueden copiar todos los
  metadatos del archivo.En las plataformas POSIX, esto significa que
  tanto el propietario como el grupo del archivo se pierden, al igual
  que las ACLs (*access control lists* o lista de control de acceso).
  En Mac OS, la bifurcación (*fork*) de recursos y de otros metadatos
  no se utilizan. Esto quiere decir que los recursos se perderán y que
  el tipo de archivo y los códigos de creador no serán correctos. En
  Windows, los propietarios de archivos, las ACLs y secuencias de
  datos alternativas no se copian.

## Operaciones de directorios y archivos

shutil.copyfileobj(fsrc, fdst[, length])

   Copy the contents of the *file-like object* *fsrc* to the file-like
   object *fdst*. The integer *length*, if given, is the buffer size.
   In particular, a negative *length* value means to copy the data
   without looping over the source data in chunks; by default the data
   is read in chunks to avoid uncontrolled memory consumption. Note
   that if the current file position of the *fsrc* object is not 0,
   only the contents from the current file position to the end of the
   file will be copied.

   "copyfileobj()" will *not* guarantee that the destination stream
   has been flushed on completion of the copy. If you want to read
   from the destination at the completion of the copy operation (for
   example, reading the contents of a temporary file that has been
   copied from a HTTP stream), you must ensure that you have called
   "flush()" or "close()" on the file-like object before attempting to
   read the destination file.

shutil.copyfile(src, dst, *, follow_symlinks=True)

   Copy the contents (no metadata) of the file named *src* to a file
   named *dst* and return *dst* in the most efficient way possible.
   *src* and *dst* are *path-like objects* or path names given as
   strings.

   *dst* debe ser el nombre completo del archivo destino; véase
   "shutil.copy()" para una copia que acepta una ruta de directorio
   destino. Si *src* y *dst* refieren al mismo archivo, se lanza
   "SameFileError".

   El local de destino debe tener permisos de escritura; de lo
   contrario, se genera una excepción "OSError". Si *dst* ya existe,
   se reemplazará. Los archivos especiales, como los dispositivos de
   caracteres o de bloques y *pipes*, no se pueden copiar con esta
   función.

   Si *follow_symlinks* es falso y *src* es un enlace simbólico, un
   enlace simbólico nuevo se creará en lugar de copiar el archivo al
   que *src* apunta.

   Se genera un evento de auditoría "shutil.copyfile" con argumentos
   "src", "dst".

   Distinto en la versión 3.3: Solía generarse "IOError" en lugar de
   "OSError". Se añadió el argumento *follow_symlinks*. Ahora retorna
   *dst*.

   Distinto en la versión 3.4: Genera "SameFileError" en lugar de
   "Error". Dado que la primera es una subclase de la segunda, el
   cambio es compatible con versiones anteriores.

   Distinto en la versión 3.8: Las llamadas a sistema de copia rápida
   específicas de la plataforma se pueden usar internamente para
   copiar el archivo de manera más eficiente. Véase la sección
   Operaciones de copia eficientes dependientes de la plataforma.

exception shutil.SpecialFileError

   This exception is raised when "copyfile()" or "copytree()" attempt
   to copy a named pipe.

   Added in version 2.7.

exception shutil.SameFileError

   Esta excepción se genera si el origen y destino en "copyfile()" son
   el mismo archivo.

   Added in version 3.4.

shutil.copymode(src, dst, *, follow_symlinks=True)

   Copy the permission bits from *src* to *dst*.  The file contents,
   owner, and group are unaffected.  *src* and *dst* are *path-like
   objects* or path names given as strings. If *follow_symlinks* is
   false, and both *src* and *dst* are symbolic links, "copymode()"
   will attempt to modify the mode of *dst* itself (rather than the
   file it points to).  This functionality is not available on every
   platform; please see "copystat()" for more information.  If
   "copymode()" cannot modify symbolic links on the local platform,
   and it is asked to do so, it will do nothing and return.

   Genera un evento de auditoría "shutil.copymode" con argumentos
   "src", "dst".

   Distinto en la versión 3.3: Se añadió el argumento
   *follow_symlinks*.

shutil.copystat(src, dst, *, follow_symlinks=True)

   Copy the permission bits, last access time, last modification time,
   and flags from *src* to *dst*.  On Linux, "copystat()" also copies
   the "extended attributes" where possible.  The file contents,
   owner, and group are unaffected.  *src* and *dst* are *path-like
   objects* or path names given as strings.

   Si *follow_symlinks* es falso, y *src* y *dst* hacen referencia los
   enlaces simbólicos, "copystat()" funcionará con los enlaces
   simbólicos en lugar de en los archivos a los que estos se refieren:
   leer la información del enlace simbólico *src* y escribirla en el
   enlace simbólico *dst*.

   Nota:

     No todas las plataformas proporcionan la capacidad de examinar y
     modificar enlaces simbólicos. Python puede indicarte qué
     funcionalidad está disponible localmente.

     * Si "os.chmod in os.supports_follow_symlinks" es "True",
       "copystat()" puede modificar los bits de permiso de un enlace
       simbólico.

     * Si "os.utime in os.supports_follow_symlinks" es "True",
       "copystat()" puede modificar el último acceso y las veces que
       un enlace simbólico fue modificado.

     * Si "os.chflags in os.supports_follow_symlinks" es "True",
       "copystat()" puede modificar las flags de un enlace simbólico.
       ("os.chflags" no está disponible en todas las plataformas.)

     En plataformas donde parte o toda esta funcionalidad no está
     disponible, cuando se le pida modificar un enlace simbólico,
     "copystat()" copiará todo lo que pueda. "copystat()" nunca
     retorna un error.Véase "os.supports_follow_symlinks" para más
     información.

   Genera un evento de auditoría "shutil.copystat" con argumentos
   "src", "dst".

   Distinto en la versión 3.3: Se ha añadido el argumento
   *follow_symlinks* y el soporte para atributos extendidos de Linux.

shutil.copy(src, dst, *, follow_symlinks=True)

   Copia el archivo *src* al archivo o directorio *dst*. *src* y *dst*
   deberían ser *objetos tipo ruta* o cadenas de caracteres
   (*strings*). Si *dst* especifica un directorio, el archivo será
   copiado en *dst* usando el nombre de archivo base de *src*. Si
   *dst* especifica un archivo que existe, será reemplazado. Retorna
   la ruta del archivo recién creado.

   Si *follow_symlinks* es falso, y *src* es un enlace simbólico,
   *dst* se creará como enlace simbólico. Si *follow_symlinks* es
   verdadero y *src* es un enlace simbólico, *dst* será una copia del
   archivo al que *src* hace referencia.

   "copy()" copia los datos del archivo y el modo de permiso del
   archivo (véase "os.chmod()"). Otros metadatos, como los tiempos de
   creación y modificación de archivos, no se preservan. Para
   preservar todos los metadatos del archivo, usa "copy2()" en su
   lugar.

   Se genera un evento de auditoría "shutil.copyfile" con argumentos
   "src", "dst".

   Genera un evento de auditoría "shutil.copymode" con argumentos
   "src", "dst".

   Distinto en la versión 3.3: Se ha añadido el argumento
   *follow_symlinks*. Ahora retorna la ruta de acceso al archivo
   recién creado.

   Distinto en la versión 3.8: Las llamadas a sistema de copia rápida
   específicas de la plataforma se pueden usar internamente para
   copiar el archivo de manera más eficiente. Véase la sección
   Operaciones de copia eficientes dependientes de la plataforma.

shutil.copy2(src, dst, *, follow_symlinks=True)

   Idéntico a "copy()" , excepto que "copy2()" también intenta
   conservar los metadatos del archivo.

   Cuando *follow_symlinks* es falso, y *src* es un enlace simbólico,
   "copy2()" intenta copiar todos los metadatos del enlace simbólico
   *src* en el enlace simbólico *dst* recién creado. Sin embargo, esta
   funcionalidad no está disponible en todas las plataformas. En las
   plataformas donde parte o toda esta funcionalidad no está
   disponible, "copy2()" conservará todos los metadatos que pueda;
   "copy2()" nunca genera una excepción porque no puede conservar los
   metadatos del archivo.

   "copy2()" usa "copystat()" para copiar todos los metadatos del
   archivo. Véase "copystat()" para más información sobre la
   compatibilidad con la plataforma para modificar los metadatos del
   enlace simbólico.

   Se genera un evento de auditoría "shutil.copyfile" con argumentos
   "src", "dst".

   Genera un evento de auditoría "shutil.copystat" con argumentos
   "src", "dst".

   Distinto en la versión 3.3: Añadido el argumento *follow_symlinks*,
   intenta copiar también los atributos del sistema de archivos
   extendidos (actualmente solo en Linux). Ahora retorna la ruta de
   acceso al archivo recién creado.

   Distinto en la versión 3.8: Las llamadas a sistema de copia rápida
   específicas de la plataforma se pueden usar internamente para
   copiar el archivo de manera más eficiente. Véase la sección
   Operaciones de copia eficientes dependientes de la plataforma.

shutil.ignore_patterns(*patterns)

   Esta función de fábrica crea una función que puede ser usada como
   un invocable para el argumento *ignore* de "copytree()", ignorando
   los archivos y directorios que coinciden con uno de los patrones
   *patterns* de estilo glob provistos. Véase el ejemplo siguiente.

shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

   Copia recursivamente un directorio completo que inicia en *src*
   hasta un directorio llamado *dst* y devuelve el directorio destino.
   Todos los directorios intermedios necesarios para contener *dst*
   serán creados por default.

   Los permisos y los tiempos de directorios son copiados con
   "copystat()"; los archivos individuales son copiados usando
   "copy2()".

   Si *symlinks* es verdadero, los enlaces simbólicos en el árbol de
   origen son representados como enlaces simbólicos en el árbol nuevo
   y los metadatos de los enlaces originales serán copiados mientras
   la plataforma lo permita; si es falso o se omite, los contenidos y
   los metadatos de los archivos vinculados se copiarán en el árbol
   nuevo.

   When *symlinks* is false, if the file pointed to by the symlink
   doesn't exist, an exception will be added in the list of errors
   raised in an "Error" exception at the end of the copy process. You
   can set the optional *ignore_dangling_symlinks* flag to true if you
   want to silence this exception. Notice that this option has no
   effect on platforms that don't support "os.symlink()".

   Si se proporciona *ignore*, debe ser un invocable que recibirá como
   argumentos el directorio visitado por "copytree()" y una lista de
   sus contenidos, tal como los retorna "os.listdir()". Ya que
   "copytree()" se invoca recursivamente, el invocable *ignore* se
   llamará una vez por cada directorio que se copia. El invocable debe
   retornar una secuencia de directorio y de nombres de archivo en
   relación con el directorio actual (es decir, un subconjunto de los
   elementos en su segundo argumento); estos nombres serán ignorados
   en el proceso de copia. "ignore_patterns()" se pueden usar para
   crear un invocable que ignora los nombres basados en patrones de
   estilo gob.

   Si ocurren excepciones, se genera, un "Error" con una lista de
   razones.

   Si *copy_function* está dado, debe ser un invocable que se usará
   para copiar cada archivo. Se le invocará con la ruta de origen y la
   ruta de destino como argumentos. Por defecto, se usa "copy2()",
   pero se puede usar cualquier función que admita la misma (como
   "copy()").

   Si *dirs_exist_ok* es falso (el default) y *dst* existe, la
   excepción "FileExistsError" es lanzada. Si *dirs_exist_ok* es
   verdadero, la operación de copiado continuara si encuentra
   directorios existentes, los archivos dentro del árbol de *dst*
   serán sobreescritos por los archivos correspondientes del árbol
   *src*.

   Se genera un evento de auditoría "shutil.copytree" con argumentos
   "src", "dst".

   Distinto en la versión 3.2: Se añadió el argumento *copy_function*
   para poder proporcionar una función de copia personalizada. Se
   añadió el argumento *ignore_dangling_symlinks* para silenciar los
   errores de enlaces colgantes cuando *symlinks* es falso.

   Distinto en la versión 3.3: Copia los metadatos cuando *symlinks*
   es falso. Ahora retorna *dst*.

   Distinto en la versión 3.8: Las llamadas a sistema de copia rápida
   específicas de la plataforma se pueden usar internamente para
   copiar el archivo de manera más eficiente. Véase la sección
   Operaciones de copia eficientes dependientes de la plataforma.

   Distinto en la versión 3.8: Added the *dirs_exist_ok* parameter.

shutil.rmtree(path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None)

   Delete an entire directory tree; *path* must point to a directory
   (but not a symbolic link to a directory).  If *ignore_errors* is
   true, errors resulting from failed removals will be ignored; if
   false or omitted, such errors are handled by calling a handler
   specified by *onexc* or *onerror* or, if both are omitted,
   exceptions are propagated to the caller.

   Esta función puede soportar rutas relativas a descriptores de
   directorio.

   Nota:

     En plataformas que admiten las funciones basadas en descriptores
     de archivo necesarias, una versión resistente de "rmtree()" al
     ataque de enlace simbólico se usa por defecto. En otras
     plataformas, la implementación "rmtree()" es susceptible a un
     ataque de enlace simbólico; dados el tiempo y las circunstancias
     adecuados, los atacantes pueden manipular los enlaces simbólicos
     en el sistema de archivos para eliminar archivos a los que no
     podrían acceder de otra manera. Las aplicaciones pueden usar el
     atributo de función "rmtree.avoids_symlink_attacks" para
     determinar qué caso aplica.

   If *onexc* is provided, it must be a callable that accepts three
   parameters: *function*, *path*, and *excinfo*.

   The first parameter, *function*, is the function which raised the
   exception; it depends on the platform and implementation.  The
   second parameter, *path*, will be the path name passed to
   *function*.  The third parameter, *excinfo*, is the exception that
   was raised. Exceptions raised by *onexc* will not be caught.

   The deprecated *onerror* is similar to *onexc*, except that the
   third parameter it receives is the tuple returned from
   "sys.exc_info()".

   Ver también:

     ejemplo de rmtree for an example of handling the removal of a
     directory tree that contains read-only files.

   Genera un evento de auditoría "shutil.rmtree" con argumentos
   "path", "dir_fd".

   Distinto en la versión 3.3: Se añadió una versión resistente a los
   ataques de enlaces simbólicos que se usan automáticamente si la
   plataforma admite funciones pasadas en descriptores de archivo.

   Distinto en la versión 3.8: En Windows, ya no eliminará los
   contenidos de un cruce de directorios antes de quitar el cruce.

   Distinto en la versión 3.11: Added the *dir_fd* parameter.

   Distinto en la versión 3.12: Added the *onexc* parameter,
   deprecated *onerror*.

   Distinto en la versión 3.13: "rmtree()" now ignores
   "FileNotFoundError" exceptions for all but the top-level path.
   Exceptions other than "OSError" and subclasses of "OSError" are now
   always propagated to the caller.

   rmtree.avoids_symlink_attacks

      Indica si la plataforma actual y la implementación proporciona
      una versión de "rmtree()" resistente al ataque de enlace
      simbólico. Actualmente, esto solo sucede para plataformas que
      admitan funciones de acceso a directorios basadas en
      descriptores de archivo.

      Added in version 3.3.

shutil.move(src, dst, copy_function=copy2)

   Recursively move a file or directory (*src*) to another location
   and return the destination.

   If *dst* is an existing directory or a symlink to a directory, then
   *src* is moved inside that directory. The destination path in that
   directory must not already exist.

   If *dst* already exists but is not a directory, it may be
   overwritten depending on "os.rename()" semantics.

   "os.rename()" is preferably used internally when *src* and the
   destination are on the same filesystem. In case "os.rename()" fails
   due to "OSError" (e.g. the user has write permission to the
   destination file but not to its parent directory), this method
   falls back to using *copy_function*, in which case *src* is copied
   to the destination using *copy_function* and then removed.

   In case of symlinks, a new symlink pointing to the target of *src*
   will be created in or as the destination, and *src* will be
   removed.

   If *copy_function* is given, it must be a callable that takes two
   arguments, *src* and the destination, and will be used to copy
   *src* to the destination if "os.rename()" cannot be used.  If the
   source is a directory, "copytree()" is called, passing it the
   *copy_function*. The default *copy_function* is "copy2()".  Using
   "copy()" as the *copy_function* allows the move to succeed when it
   is not possible to also copy the metadata, at the expense of not
   copying any of the metadata.

   Genera un evento de auditoría "shutil.move" con argumentos "src",
   "dst".

   Distinto en la versión 3.3: Se añadió el manejo explícito de
   enlaces simbólicos para sistemas de archivos extranjeros, de manera
   que se adapta al comportamiento del **mv** del GNU. Ahora retorna
   *dst*.

   Distinto en la versión 3.5: Se agregó el argumento de keyword
   *copy_function*.

   Distinto en la versión 3.8: Las llamadas a sistema de copia rápida
   específicas de la plataforma se pueden usar internamente para
   copiar el archivo de manera más eficiente. Véase la sección
   Operaciones de copia eficientes dependientes de la plataforma.

   Distinto en la versión 3.9: Acepta un *objeto tipo ruta* como *src*
   y *dst*.

shutil.disk_usage(path)

   Retorna las estadísticas de uso de disco sobre la ruta de acceso
   dada como un *named tuple* con los atributos *total*, *used* y
   *free*, que son las cantidades del espacio total, el usado y el
   libre, en bytes. *path* puede ser un archivo o un directorio.

   Nota:

     On Unix filesystems, *path* must point to a path within a
     **mounted** filesystem partition. On those platforms, CPython
     doesn't attempt to retrieve disk usage information from non-
     mounted filesystems.

   Added in version 3.3.

   Distinto en la versión 3.8: En Windows, *path* ahora puede ser un
   archivo o un directorio.

   Availability: Unix, Windows.

shutil.chown(path, user=None, group=None, *, dir_fd=None, follow_symlinks=True)

   Cambia el propietario *user* y/o *group* de la *ruta* dada.

   *user* puede ser un nombre usuario de sistema o un UID
   (identificador de usuario); lo mismo aplica a *group*. Se requiere
   al menos un argumento.

   Véase también "os.chown()", la función subyacente.

   Genera un evento de auditoría "shutil.chown" con argumentos "path",
   "user", "group".

   Availability: Unix.

   Added in version 3.3.

   Distinto en la versión 3.13: Added *dir_fd* and *follow_symlinks*
   parameters.

shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)

   Retorna la ruta de acceso a un ejecutable que se ejecutaría si el
   *cmd* dado se invoca. Si no se invoca a *cmd*, retorna "None".

   *mode* is a permission mask passed to "os.access()", by default
   determining if the file exists and is executable.

   *path* is a ""PATH" string" specifying the directories to look in,
   delimited by "os.pathsep". When no *path* is specified, the "PATH"
   environment variable is read from "os.environ", falling back to
   "os.defpath" if it is not set.

   If *cmd* contains a directory component, "which()" only checks the
   specified path directly and does not search the directories listed
   in *path* or in the system's "PATH" environment variable.

   On Windows, the current directory is prepended to the *path* if
   *mode* does not include "os.X_OK". When the *mode* does include
   "os.X_OK", the Windows API "NeedCurrentDirectoryForExePathW" will
   be consulted to determine if the current directory should be
   prepended to *path*. To avoid consulting the current working
   directory for executables: set the environment variable
   "NoDefaultCurrentDirectoryInExePath".

   Also on Windows, the "PATHEXT" environment variable is used to
   resolve commands that may not already include an extension. For
   example, if you call "shutil.which("python")", "which()" will
   search "PATHEXT" to know that it should look for "python.exe"
   within the *path* directories. For example, on Windows:

      >>> shutil.which("python")
      'C:\\Python33\\python.EXE'

   This is also applied when *cmd* is a path that contains a directory
   component:

      >>> shutil.which("C:\\Python33\\python")
      'C:\\Python33\\python.EXE'

   Added in version 3.3.

   Distinto en la versión 3.8: Ahora se acepta el tipo "bytes". Si el
   tipo *cmd* es "bytes", el tipo resultante también es "bytes".

   Distinto en la versión 3.12: On Windows, the current directory is
   no longer prepended to the search path if *mode* includes "os.X_OK"
   and WinAPI "NeedCurrentDirectoryForExePathW(cmd)" is false, else
   the current directory is prepended even if it is already in the
   search path; "PATHEXT" is used now even when *cmd* includes a
   directory component or ends with an extension that is in "PATHEXT";
   and filenames that have no extension can now be found.

exception shutil.Error

   Esta excepción recopila las excepciones que se generan durante una
   operación de varios archivos. Para "copytree()", el argumento de
   excepción es una lista de 3 tuplas (*scrname*, *dstname*,
   *exception*).

### Operaciones de copia eficientes dependientes de la plataforma

A partir de Python 3.8, todas las funciones que incluyen una copia de
archivo ("copyfile()", "copy()", "copy2()", "copytree()", y "move()")
puede usar llamadas a sistema de "copia rápida" específicas a cada
plataforma para poder copiar el archivo de forma más eficiente (véase
bpo-33671). "copia rápida" significa que la operación de copia ocurre
dentro del núcleo, evitando el uso de búferes en espacio de usuario en
Python como en ""outfd.write(infd.read())"".

En macOS, se usa fcopyfile para copiar el contenido del archivo (pero
no los metadatos).

On Linux "os.copy_file_range()" or "os.sendfile()" is used.

On Solaris "os.sendfile()" is used.

En Windows, "shutil.copyfile()" usa un tamaño de búfer predeterminado
más grande (1 MiB en lugar de 64 KiB) y se usa una variante de
"shutil.copyfileobj()" basada en "memoryview()".

If the fast-copy operation fails and no data was written in the
destination file then shutil will silently fall back to less efficient
"copyfileobj()" function internally.

Distinto en la versión 3.8.

Distinto en la versión 3.14: Solaris now uses "os.sendfile()".

Distinto en la versión 3.14: Copy-on-write or server-side copy may be
used internally via "os.copy_file_range()" on supported Linux
filesystems.

### ejemplo de *copytree*

Un ejemplo que usa el auxiliar "ignore_patterns()":

   from shutil import copytree, ignore_patterns

   copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

Esto copiará todo excepto archivos ".pyc" y archivos o directorios
cuyo nombre comience con "tmp".

Otro ejemplo que usa el argumento *ignore* para agregar una llamada a
iniciar sesión:

   from shutil import copytree
   import logging

   def _logpath(path, names):
       logging.info('Working in %s', path)
       return []   # nothing will be ignored

   copytree(source, destination, ignore=_logpath)

### ejemplo de rmtree

This example shows how to remove a directory tree on Windows where
some of the files have their read-only bit set. It uses the onexc
callback to clear the readonly bit and reattempt the remove. Any
subsequent failure will propagate.

   import os, stat
   import shutil

   def remove_readonly(func, path, _):
       "Clear the readonly bit and reattempt the removal"
       os.chmod(path, stat.S_IWRITE)
       func(path)

   shutil.rmtree(directory, onexc=remove_readonly)

## Operaciones de archivado

Added in version 3.2.

Distinto en la versión 3.5: Se agregó soporte para el formato *xztar*.

Se proveen también las utilidades de alto nivel para crear y leer
archivos comprimidos y archivados. Utilizan para esto los módulos
"zipfile" y "tarfile".

shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])

   Crea un documento de archivado (como zip o tar) y retorna su
   nombre.

   *base_name* is the name of the file to create, including the path,
   minus any format-specific extension.

   *format* is the archive format: one of "zip" (if the "zlib" module
   is available), "tar", "gztar" (if the "zlib" module is available),
   "bztar" (if the "bz2" module is available), "xztar" (if the "lzma"
   module is available), or "zstdtar" (if the "compression.zstd"
   module is available).

   *root_dir* es un directorio que será el directorio raíz del
   archivo, todas las rutas en el archivo serán relativas a él; por
   ejemplo, típicamente nos cambiaremos de directorio (*chdir*) a
   *root_dir* antes de crear el archivo.

   *base_dir* es el directorio desde donde iniciamos el archivado;
   i.e, *base_dir* será el prefijo común para todos los archivos y
   directorios en el archivo. *base_dir* debe ser dado de forma
   relativa a *root_dir*. En Ejemplo de archivado con base_dir se ve
   un ejemplo de cómo usar *base_dir* y *root_dir* juntos.

   *root_dir* y *base_dir* irán por defecto al directorio actual.

   If *dry_run* es verdadero, no se crea un archivo, pero las
   operaciones que se ejecutarán están registradas en *logger*.

   *owner* y *group* se usan al crear un archivador tar. Por defecto,
   usa el propietario y el grupo actual.

   *logger* debe ser un objeto compatible con  **PEP 282**, usualmente
   una instancia de "logging.Logger".

   El argumento *verbose* está fuera de uso y es obsoleto.

   Genera un evento de auditoría "shutil.make_archive" con argumentos
   "base_name", "format", "root_dir", "base_dir".

   Nota:

     This function is not thread-safe when custom archivers registered
     with "register_archive_format()" do not support the *root_dir*
     argument.  In this case it temporarily changes the current
     working directory of the process to *root_dir* to perform
     archiving.

   Distinto en la versión 3.8: El formato de *pax* moderno
   (POSIX.1-2001) se usa ahora en lugar del formato de legado GNU para
   archivadores creados con "format="tar"".

   Distinto en la versión 3.10.6: Esta función ahora es segura para
   hilos durante la creación de archivos estándar ".zip" y tar.

shutil.get_archive_formats()

   Retorna una lista de formatos admitidos para archivado. Cada
   elemento de una secuencia retornada es una tupla "(name,
   description)".

   By default "shutil" provides these formats:

   * *zip*: archivo ZIP (si el módulo "zlib" está disponible).

   * *tar*: archivo tar sin comprimir. Utiliza el formato pax
     POSIX.1-2001 para archivos nuevos.

   * *gztar*: archivo tar comprimido con gzip (si el módulo "zlib"
     está disponible).

   * *bztar*: archivo tar comprimido con bzip2 (si el módulo "bz2"
     está disponible).

   * *xztar*: archivo tar comprimido con xz (si el módulo "lzma" está
     disponible).

   * *zstdtar*: Zstandard compressed tar-file (if the
     "compression.zstd" module is available).

   Puedes registrar formatos nuevos o proporcionar tu propio
   archivador para cualquier formato existente, usando
   "register_archive_format()".

shutil.register_archive_format(name, function[, extra_args[, description]])

   Registra un archivador para el formato *name*.

   *function* is the callable that will be used to create archives.
   The callable will receive the *base_name* of the file to create,
   followed by the *base_dir* (which defaults to "os.curdir") to start
   archiving from. Further arguments are passed as keyword arguments:
   *owner*, *group*, *dry_run* and *logger* (as passed in
   "make_archive()").

   If *function* has the custom attribute "function.supports_root_dir"
   set to "True", the *root_dir* argument is passed as a keyword
   argument. Otherwise the current working directory of the process is
   temporarily changed to *root_dir* before calling *function*. In
   this case "make_archive()" is not thread-safe.

   Si está dado, *extra_args* es una secuencia de pares "(name,
   value)"  que se usarán como argumentos de palabras clave extra
   cuando se usa el archivador invocable.

   *description* se usa por "get_archive_formats()" que retorna la
   lista de archivadores. Cae por defecto en una cadena de caracteres
   vacía.

   Distinto en la versión 3.12: Added support for functions supporting
   the *root_dir* argument.

shutil.unregister_archive_format(name)

   Elimina el formato de archivo *name* de la lista de formatos
   admitidos.

shutil.unpack_archive(filename[, extract_dir[, format[, filter]]])

   Desempaqueta un archivo. *filename* es la ruta completa del
   archivo.

   *extract_dir* es el nombre del directorio donde se desempaca el
   archivo. Si no está provisto, se usa el nombre del directorio
   actual.

   *format* is the archive format: one of "zip", "tar", "gztar",
   "bztar", "xztar", or "zstdtar".  Or any other format registered
   with "register_unpack_format()".  If not provided,
   "unpack_archive()" will use the archive file name extension and see
   if an unpacker was registered for that extension.  In case none is
   found, a "ValueError" is raised.

   The keyword-only *filter* argument is passed to the underlying
   unpacking function. For zip files, *filter* is not accepted. For
   tar files, it is recommended to use "'data'" (default since Python
   3.14), unless using features specific to tar and UNIX-like
   filesystems. (See Extraction filters for details.)

   Se genera un evento de auditoría "shutil.unpack_archive" con
   argumentos "filename", "extract_dir", "format".

   Advertencia:

     Never extract archives from untrusted sources without prior
     inspection. It is possible that files are created outside of the
     path specified in the *extract_dir* argument, for example,
     members that have absolute filenames or filenames with ".."
     components.Since Python 3.14, the defaults for both built-in
     formats (zip and tar files) will prevent the most dangerous of
     such security issues, but will not prevent *all* unintended
     behavior. Read the Hints for further verification section for
     tar-specific details.

   Distinto en la versión 3.7: Acepta un *path-like object* como
   *filename* y *extract_dir*.

   Distinto en la versión 3.12: Added the *filter* argument.

shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])

   Registra un formato de desempaque. *name* es el nombre del formato
   y *extensions* es una lista de extensiones que corresponden al
   formato, como ".zip" para archivos zip.

   *function* is the callable that will be used to unpack archives.
   The callable will receive:

   * the path of the archive, as a positional argument;

   * the directory the archive must be extracted to, as a positional
     argument;

   * possibly a *filter* keyword argument, if it was given to
     "unpack_archive()";

   * additional keyword arguments, specified by *extra_args* as a
     sequence of "(name, value)" tuples.

   *description* se puede proporcionar para describir el formato y
   será retornado por la función "get_unpack_formats()".

shutil.unregister_unpack_format(name)

   Anula el registro del formato de desempaque. *name* es el nombre
   del formato.

shutil.get_unpack_formats()

   Retorna una lista de todos los formatos registrados para
   desempaquetar. Cada elemento de la secuencia es una tupla "(name,
   extensions, description)".

   By default "shutil" provides these formats:

   * *zip*: archivo zip (desempaquetar archivos comprimidos funciona
     solo si el módulo correspondiente está disponible).

   * *tar*: archivo tar sin comprimir.

   * *gztar*: archivo tar comprimido con gzip (si el módulo "zlib"
     está disponible).

   * *bztar*: archivo tar comprimido con bzip2 (si el módulo "bz2"
     está disponible).

   * *xztar*: archivo tar comprimido con xz (si el módulo "lzma" está
     disponible).

   * *zstdtar*: Zstandard compressed tar-file (if the
     "compression.zstd" module is available).

   Puedes registrar formatos nuevos o proporcionar tu propio
   desempaquetado para cualquier formato existente, usando
   "register_unpack_format()".

### Ejemplo de archivado

En este ejemplo, creamos un archivo tar de tipo gzip que contiene
todos los archivos que se encuentran en el directorio ".ssh" del
usuario:

   >>> from shutil import make_archive
   >>> import os
   >>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
   >>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
   >>> make_archive(archive_name, 'gztar', root_dir)
   '/Users/tarek/myarchive.tar.gz'

El archivo resultante contiene:

   $ tar -tzvf /Users/tarek/myarchive.tar.gz
   drwx------ tarek/staff       0 2010-02-01 16:23:40 ./
   -rw-r--r-- tarek/staff     609 2008-06-09 13:26:54 ./authorized_keys
   -rwxr-xr-x tarek/staff      65 2008-06-09 13:26:54 ./config
   -rwx------ tarek/staff     668 2008-06-09 13:26:54 ./id_dsa
   -rwxr-xr-x tarek/staff     609 2008-06-09 13:26:54 ./id_dsa.pub
   -rw------- tarek/staff    1675 2008-06-09 13:26:54 ./id_rsa
   -rw-r--r-- tarek/staff     397 2008-06-09 13:26:54 ./id_rsa.pub
   -rw-r--r-- tarek/staff   37192 2010-02-06 18:23:10 ./known_hosts

### Ejemplo de archivado con *base_dir*

En este ejemplo, similar al de arriba, mostramos cómo usar
"make_archive()", pero esta vez utilizando *base_dir*.  Ahora tenemos
la siguiente estructura de directorios:

   $ tree tmp
   tmp
   └── root
       └── structure
           ├── content
               └── please_add.txt
           └── do_not_add.txt

En el archivo final, "please_add.txt" debería estar incluido, pero
"do_not_add.txt" no.  Por lo tanto usamos lo siguiente:

   >>> from shutil import make_archive
   >>> import os
   >>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
   >>> make_archive(
   ...     archive_name,
   ...     'tar',
   ...     root_dir='tmp/root',
   ...     base_dir='structure/content',
   ... )
   '/Users/tarek/myarchive.tar'

Listando los archivos en el archivo resultante nos da:

   $ python -m tarfile -l /Users/tarek/myarchive.tar
   structure/content/
   structure/content/please_add.txt

## Consulta el tamaño de la terminal de salida

shutil.get_terminal_size(fallback=(columns, lines))

   Obtén el tamaño de la ventana de la terminal.

   Para cada una de las dos dimensiones, se comprueba la variable de
   entorno "COLUMNS" y "LINES" respectivamente. Si la variable está
   definida y el valor es un entero positivo, se utiliza.

   Cuando "COLUMNS" o "LINES" no está definido, como suele ocurrir, la
   terminal conectada a "sys.__stdout__" se consulta invocando
   "os.get_terminal_size()".

   Si el tamaño de la terminal no se puede consultar correctamente, ya
   sea porque el sistema no admite consultas o porque no estamos
   conectados a una terminal, se usa el valor dado en el parámetro
   "fallback". "fallback" tiene por defecto "(80, 24)", que es el
   tamaño por defecto que se usa en muchos emuladores de terminal.

   El valor retornado es una tupla con su respectivo nombre, de tipo
   "os.terminal_size".

   Ver también: *The Single UNIX Specification*, Versión 2, Other
   Environment Variables.

   Added in version 3.3.

   Distinto en la versión 3.11: Los valores "fallback" son usados
   también si "os.get_terminal_size()" devuelve zeros.
