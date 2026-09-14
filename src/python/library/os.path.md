---
title: '"os.path" --- Common pathname manipulations'
source_url: https://docs.python.org/es/3
source_path: library/os.path.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3380
---

# "os.path" --- Common pathname manipulations

**Source code:** Lib/genericpath.py, Lib/posixpath.py (for POSIX) and
Lib/ntpath.py (for Windows).

======================================================================

Este módulo implementa algunas funciones útiles sobre los nombres de
rutas. Para leer o escribir archivos consulte "open()", y para acceder
a archivos del sistema vea el "os". Los parámetros para las rutas
pueden ser pasados como caracteres, o bytes ,o cualquier objeto
implementado en el protocolo "os.PathLike".

A diferencia de un shell Unix, Python no realiza ninguna expansión de
ruta *automática*. Las funciones como "expanduser()" y "expandvars()"
puede ser invocadas de manera explicita cuando una aplicación desea
realizar una expansión de ruta *shell-like*. (Consulte el módulo
"glob".)

Ver también: El módulo "pathlib" ofrece objetos de ruta de alto nivel.

Nota:

  Todas estas funciones aceptan solo bytes o solo objetos de cadena
  como sus parámetros. El resultado es un objeto del mismo tipo, si se
  retorna una ruta o un nombre de archivo.

Nota:

  Since different operating systems have different path name
  conventions, there are several versions of this module in the
  standard library.  The "os.path" module is always the path module
  suitable for the operating system Python is running on, and
  therefore usable for local paths.  However, you can also import and
  use the individual modules if you want to manipulate a path that is
  *always* in one of the different formats.  They all have the same
  interface:

  * "posixpath" for UNIX-style paths

  * "ntpath" for Windows paths

Distinto en la versión 3.8: "exists()", "lexists()", "isdir()",
"isfile()", "islink()", y "ismount()" ahora retornan "False" en lugar
de lanzar una excepción para rutas que contienen caracteres o bytes
que no se puedan representar a nivel de sistema operativo.

os.path.abspath(path)

   Return a normalized absolutized version of the pathname *path*. On
   most platforms, this is equivalent to calling
   "normpath(join(os.getcwd(), path))".

   Ver también: "os.path.join()" and "os.path.normpath()".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.basename(path, /)

   Retorna un nombre base de nombre de ruta *path*. Este es el segundo
   elemento del par retornado al pasar *path* a la función "split()".
   Toma en cuenta que el resultado de esta función es diferente a la
   del programa de Unix **basename**; donde **basename** para
   "'/foo/bar/'" retorna "'bar'", la función "basename()" retorna una
   cadena vacía ("''").

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.commonpath(paths)

   Return the longest common sub-path of each pathname in the iterable
   *paths*.  Raise "ValueError" if *paths* contain both absolute and
   relative pathnames, if *paths* are on different drives, or if
   *paths* is empty.  Unlike "commonprefix()", this returns a valid
   path.

   Added in version 3.5.

   Distinto en la versión 3.6: Acepta una secuencia de *path-like
   objects*.

   Distinto en la versión 3.13: Any iterable can now be passed, rather
   than just sequences.

os.path.commonprefix(list, /)

   Return the longest string prefix (taken character-by-character)
   that is a prefix of all strings in *list*.  If *list* is empty,
   return the empty string ("''").

   Advertencia:

     This function may return invalid paths because it works a
     character at a time. If you need a **common path prefix**, then
     the algorithm implemented in this function is not secure. Use
     "commonpath()" for finding a common path prefix.

        >>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
        '/usr/l'

        >>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
        '/usr'

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.dirname(path, /)

   Retorna el nombre del directorio de la ruta *path*. Es el primer
   elemento del par retornado al pasar *path* a la función "split()".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.exists(path)

   Retorna "True" si *path* se refiere a una ruta existente o un
   descriptor de archivo abierto. Retorna "False" para enlaces
   simbólicos rotos. En algunas plataformas, esta función puede
   retornar "False" si no se concede permiso para ejecutar "os.stat()"
   en el archivo solicitado, incluso la ruta *path* existe
   físicamente.

   Distinto en la versión 3.3: *path* ahora puede ser un valor entero:
   retorna "True" si es un descriptor de archivo abierto, de otro modo
   retorna "False".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.lexists(path)

   Return "True" if *path* refers to an existing path, including
   broken symbolic links.   Equivalent to "exists()" on platforms
   lacking "os.lstat()".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.expanduser(path)

   En Unix y Windows, retorna el argumento con un componente inicial
   de "~" o "~user" reemplazado por el directorio *home* de *user*.

   En Unix, el "~" inicial es reemplazado por la variable de entorno
   "HOME" si está activada; si no, el directorio principal del usuario
   actual se busca en el directorio de contraseñas a través del módulo
   incorporado "pwd". Un "~user" inicial es buscado directamente en el
   directorio de contraseñas.

   En Windows, se usará "USERPROFILE" si se establece, de lo contrario
   se usará una combinación de "HOMEPATH" y "HOMEDRIVE".  Un "~user"
   inicial se maneja comprobando que el último componente de
   directorio del directorio de inicio del usuario actual coincide con
   "USERNAME", y reemplazándolo si es así.

   Si la expansión falla o si la ruta no comienza con una tilde, la
   ruta se retorna sin cambios.

   Distinto en la versión 3.6: Acepta un *path-like object*.

   Distinto en la versión 3.8: Ya no utiliza "HOME" en Windows.

os.path.expandvars(path)

   Retorna el argumento con variables de entorno expandidas. Las sub-
   cadenas de la forma "$name" or "${name}" se reemplazan por el valor
   de la variable de entorno *name*. Los nombres de variables mal
   formadas y las referencias a variables no existentes se dejan sin
   cambios.

   En Windows, las expansiones "%name%" están soportadas además de
   "$name" y "${name}".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.getatime(path, /)

   Return the time of last access of *path*.  The return value is a
   floating-point number giving the number of seconds since the epoch
   (see the  "time" module).  Raise "OSError" if the file does not
   exist or is inaccessible.

os.path.getmtime(path, /)

   Return the time of last modification of *path*.  The return value
   is a floating-point number giving the number of seconds since the
   epoch (see the  "time" module). Raise "OSError" if the file does
   not exist or is inaccessible.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.getctime(path, /)

   Retorna el *ctime* del sistema que, en algunos sistemas (como Unix)
   es la hora del último cambio de metadatos y, en otros (como
   Windows), es el tiempo de creación de *path*. El valor retornado es
   un número que da el número de segundos desde la época (consulta el
   módulo "time"). Lanza una excepción "OSError" si el archivo no
   existe o es inaccesible.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.getsize(path, /)

   Retorna el tamaño en bytes de *path*, Lanza una excepción "OSError"
   si el archivo no existe o es inaccesible.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.isabs(path, /)

   Return "True" if *path* is an absolute pathname.  On Unix, that
   means it begins with a slash, on Windows that it begins with two
   (back)slashes, or a drive letter, colon, and (back)slash together.

   Ver también: "abspath()"

   Distinto en la versión 3.6: Acepta un *path-like object*.

   Distinto en la versión 3.13: On Windows, returns "False" if the
   given path starts with exactly one (back)slash.

os.path.isfile(path)

   Retorna "True" si *path* es un archivo "existing". Esto sigue los
   enlaces simbólicos, por lo que tanto "islink()" como "isfile()"
   pueden ser verdaderos para la misma ruta.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.isdir(path, /)

   Retorna "True" si *path* es un directorio "existing". Esto sigue
   los enlaces simbólicos, por lo que tanto "islink()" como "isdir()"
   pueden ser verdaderos para la misma ruta.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.isjunction(path)

   Return "True" if *path* refers to an "existing" directory entry
   that is a junction.  Always return "False" if junctions are not
   supported on the current platform.

   Added in version 3.12.

os.path.islink(path)

   Retorna  "True" si *path* hace referencia a una entrada de
   directorio "existing" que es un enlace simbólico. Siempre "False"
   si el entorno de ejecución de Python no admite vínculos
   simbólicos..

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.ismount(path)

   Return "True" if pathname *path* is a *mount point*: a point in a
   file system where a different file system has been mounted.  On
   POSIX, the function checks whether *path*'s parent, "*path*/..", is
   on a different device than *path*, or whether "*path*/.." and
   *path* point to the same i-node on the same device --- this should
   detect mount points for all Unix and POSIX variants.  It is not
   able to reliably detect bind mounts on the same filesystem. On
   Linux systems, it will always return "True" for btrfs subvolumes,
   even if they aren't mount points. On Windows, a drive letter root
   and a share UNC are always mount points, and for any other path
   "GetVolumePathName" is called to see if it is different from the
   input path.

   Distinto en la versión 3.4: Added support for detecting non-root
   mount points on Windows.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.isdevdrive(path)

   Return "True" if pathname *path* is located on a Windows Dev Drive.
   A Dev Drive is optimized for developer scenarios, and offers faster
   performance for reading and writing files. It is recommended for
   use for source code, temporary build directories, package caches,
   and other IO-intensive operations.

   May raise an error for an invalid path, for example, one without a
   recognizable drive, but returns "False" on platforms that do not
   support Dev Drives. See the Windows documentation for information
   on enabling and creating Dev Drives.

   Added in version 3.12.

   Distinto en la versión 3.13: The function is now available on all
   platforms, and will always return "False" on those that have no
   support for Dev Drives

os.path.isreserved(path)

   Return "True" if *path* is a reserved pathname on the current
   system.

   On Windows, reserved filenames include those that end with a space
   or dot; those that contain colons (i.e. file streams such as
   "name:stream"), wildcard characters (i.e. "'*?"<>'"), pipe, or
   ASCII control characters; as well as DOS device names such as
   "NUL", "CON", "CONIN$", "CONOUT$", "AUX", "PRN", "COM1", and
   "LPT1".

   Nota:

     This function approximates rules for reserved paths on most
     Windows systems. These rules change over time in various Windows
     releases. This function may be updated in future Python releases
     as changes to the rules become broadly available.

   Availability: Windows.

   Added in version 3.13.

os.path.join(path, /, *paths)

   Join one or more path segments intelligently.  The return value is
   the concatenation of *path* and all members of **paths*, with
   exactly one directory separator following each non-empty part,
   except the last. That is, the result will only end in a separator
   if the last part is either empty or ends in a separator.

   If a segment is an absolute path (which on Windows requires both a
   drive and a root), then all previous segments are ignored and
   joining continues from the absolute path segment. On Linux, for
   example:

      >>> os.path.join('/home/foo', 'bar')
      '/home/foo/bar'
      >>> os.path.join('/home/foo', '/home/bar')
      '/home/bar'

   On Windows, the drive is not reset when a rooted path segment
   (e.g., "r'\foo'") is encountered. If a segment is on a different
   drive or is an absolute path, all previous segments are ignored and
   the drive is reset. For example:

      >>> os.path.join('c:\\', 'foo')
      'c:\\foo'
      >>> os.path.join('c:\\foo', 'd:\\bar')
      'd:\\bar'

   Note that since there is a current directory for each drive,
   "os.path.join("c:", "foo")" represents a path relative to the
   current directory on drive "C:" ("c:foo"), not "c:\foo".

   Distinto en la versión 3.6: Acepta un objeto *path-like object*
   para *path* y *paths*.

os.path.normcase(path, /)

   Normaliza las mayúsculas y minúsculas de un nombre de ruta. En
   Windows convierte todos los caracteres en el nombre de ruta a
   minúsculas y también convierte las barras inclinadas hacia atrás en
   barras inclinadas hacia atrás. En otros sistemas operativos,
   retorna la ruta sin cambios.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.normpath(path)

   Normaliza un nombre de ruta colapsando separadores redundantes y
   referencias de nivel superior para que "A//B", "A/B/", "A/./B" y
   "A/foo/../B" se transformen en "A/B". Esta modificación de cadena
   puede que modifique el significado de la ruta que contenga enlaces
   simbólicos. En Windows, convierte las barras inclinadas hacia
   adelante en barras hacia atrás. Para normalizar mayúsculas y
   minúsculas, utiliza "normcase()".

   Nota:

     En sistemas POSIX, de acuerdo con IEEE Std 1003.1 Edición 2013;
     4.13 Resolución de Nombres de Rutas, si el nombre de ruta
     comienza con exactamente dos barras diagonales, el primer
     componente que sigue a los caracteres principales puede
     interpretarse de una manera definida por la implementación,
     aunque más de dos caracteres principales se tratarán como un solo
     carácter.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.realpath(path, /, *, strict=False)

   Return the canonical path of the specified filename, eliminating
   any symbolic links encountered in the path (if they are supported
   by the operating system). On Windows, this function will also
   resolve MS-DOS (also called 8.3) style names such as "C:\\PROGRA~1"
   to "C:\\Program Files".

   By default, the path is evaluated up to the first component that
   does not exist, is a symlink loop, or whose evaluation raises
   "OSError". All such components are appended unchanged to the
   existing part of the path.

   Some errors that are handled this way include "access denied", "not
   a directory", or "bad argument to internal function". Thus, the
   resulting path may be missing or inaccessible, may still contain
   links or loops, and may traverse non-directories.

   This behavior can be modified by keyword arguments:

   If *strict* is "True", the first error encountered when evaluating
   the path is re-raised. In particular, "FileNotFoundError" is raised
   if *path* does not exist, or another "OSError" if it is otherwise
   inaccessible.

   If *strict* is "os.path.ALLOW_MISSING", errors other than
   "FileNotFoundError" are re-raised (as with "strict=True"). Thus,
   the returned path will not contain any symbolic links, but the
   named file and some of its parent directories may be missing.

   Nota:

     Esta función emula el procedimiento del sistema operativo para
     hacer que una ruta sea canónica, que difiere ligeramente entre
     Windows y UNIX con respecto a cómo interactúan los enlaces y los
     componentes de la ruta posterior.Las API del sistema operativo
     hacen que las rutas sean canónicas según sea necesario, por lo
     que normalmente no es necesario llamar a esta función.

   Distinto en la versión 3.6: Acepta un *path-like object*.

   Distinto en la versión 3.8: Los enlaces y uniones simbólicos ahora
   se resuelven en Windows.

   Distinto en la versión 3.10: Se agregó el parámetro *strict*.

   Distinto en la versión 3.14: The "ALLOW_MISSING" value for the
   *strict* parameter was added.

os.path.ALLOW_MISSING

   Special value used for the *strict* argument in "realpath()".

   Added in version 3.14.

os.path.relpath(path, start=os.curdir)

   Retorna un nombre de ruta relativo a *path* desde el directorio
   actual o de un directorio *start* opcional. Este es un cálculo de
   ruta: No se accede al sistema de archivos para confirmar la
   existencia o la naturaleza de *path* o *start*. En Windows, se
   lanza "ValueError"  cuando *path* y *start* están en discos
   diferentes.

   *start* defaults to "os.curdir".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.samefile(path1, path2, /)

   Retorna "True" si ambos argumentos de nombre de ruta refieren al
   mismo archivo o directorio. Esto se determina por el número de
   dispositivo y el número de *i-node* y lanza una excepción si una
   llamada de "os.stat()" en alguno de los nombres de ruta falla.

   Distinto en la versión 3.2: Añadido soporte para Windows.

   Distinto en la versión 3.4: Windows ahora utiliza la misma
   implementación que en el resto de las plataformas.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.sameopenfile(fp1, fp2)

   Retorna "True" si los descriptores de archivo *fp1* y *fp2* se
   refieren al mismo archivo.

   Distinto en la versión 3.2: Añadido soporte para Windows.

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.samestat(stat1, stat2, /)

   Retorna "True" si las tuplas de *stat* (*stat1* y *stat2*) refieren
   al mismo archivo. Estas estructuras pueden haber sido retornadas
   por "os.fstat()", "os.lstat()", o "os.stat()". Esta función
   implementa la comparación subyacente utilizada por: "samefile()" y
   "sameopenfile()".

   Distinto en la versión 3.4: Añadido soporte para Windows.

os.path.split(path, /)

   Split the pathname *path* into a pair, "(head, tail)" where *tail*
   is the last pathname component and *head* is everything leading up
   to that.  The *tail* part will never contain a slash; if *path*
   ends in a slash, *tail* will be empty.  If there is no slash in
   *path*, *head* will be empty.  If *path* is empty, both *head* and
   *tail* are empty.  Trailing slashes are stripped from *head* unless
   it is the root (one or more slashes only).  In all cases,
   "join(head, tail)" returns a path to the same location as *path*
   (but the strings may differ).  Also see the functions "join()",
   "dirname()" and "basename()".

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.splitdrive(path, /)

   Divide el nombre de ruta *path* en un par "(drive, tail)" donde
   *drive* es un punto de montaje o una cadena vacía. En sistemas que
   no utilizan especificaciones de unidad, *drive* siempre será una
   cadena vacía. En todos los casos, "drive + tail" será lo mismo que
   *path*.

   En Windows, divide un nombre de ruta en unidad / punto compartido
   UNC y ruta relativa.

   Si la ruta contiene una letra de unidad, la unidad contendrá todo
   hasta los dos puntos inclusive:

      >>> splitdrive("c:/dir")
      ("c:", "/dir")

   If the path contains a UNC path, drive will contain the host name
   and share:

      >>> splitdrive("//host/computer/dir")
      ("//host/computer", "/dir")

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.splitroot(path, /)

   Split the pathname *path* into a 3-item tuple "(drive, root, tail)"
   where *drive* is a device name or mount point, *root* is a string
   of separators after the drive, and *tail* is everything after the
   root. Any of these items may be the empty string. In all cases,
   "drive + root + tail" will be the same as *path*.

   On POSIX systems, *drive* is always empty. The *root* may be empty
   (if *path* is relative), a single forward slash (if *path* is
   absolute), or two forward slashes (implementation-defined per IEEE
   Std 1003.1-2017; 4.13 Pathname Resolution.) For example:

      >>> splitroot('/home/sam')
      ('', '/', 'home/sam')
      >>> splitroot('//home/sam')
      ('', '//', 'home/sam')
      >>> splitroot('///home/sam')
      ('', '/', '//home/sam')

   On Windows, *drive* may be empty, a drive-letter name, a UNC share,
   or a device name. The *root* may be empty, a forward slash, or a
   backward slash. For example:

      >>> splitroot('C:/Users/Sam')
      ('C:', '/', 'Users/Sam')
      >>> splitroot('//Server/Share/Users/Sam')
      ('//Server/Share', '/', 'Users/Sam')

   Added in version 3.12.

os.path.splitext(path, /)

   Divide el nombre de la ruta *path* en un par "(root, ext)" de tal
   forma que "root + ext == path", y *ext* queda vacío o inicia con un
   punto y contiene a lo mucho un punto.

   Si la ruta no contiene ninguna extensión, *ext* será  "’’":

      >>> splitext('bar')
      ('bar', '')

   Si la ruta contiene una extensión, *ext* se establecerá como esta
   extensión, incluido el punto por delante. Tenga en cuenta que los
   puntos anteriores se ignorarán:

      >>> splitext('foo.bar.exe')
      ('foo.bar', '.exe')
      >>> splitext('/foo/bar.exe')
      ('/foo/bar', '.exe')

   Los puntos que están por delante del último componente de la ruta
   son considerados parte de la raíz:

      >>> splitext('.cshrc')
      ('.cshrc', '')
      >>> splitext('/foo/....jpg')
      ('/foo/....jpg', '')

   Distinto en la versión 3.6: Acepta un *path-like object*.

os.path.supports_unicode_filenames

   "True" si se pueden utilizar cadenas Unicode arbitrarias como
   nombres de archivo (dentro de las limitaciones impuestas por el
   sistema de archivos).
