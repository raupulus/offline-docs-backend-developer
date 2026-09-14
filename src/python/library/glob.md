---
title: '"glob" --- Unix style pathname pattern expansion'
source_url: https://docs.python.org/es/3
source_path: library/glob.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2750
---

# "glob" --- Unix style pathname pattern expansion

**Código fuente:** Lib/glob.py

======================================================================

The "glob" module finds pathnames using pattern matching rules similar
to the Unix shell. No tilde expansion is done, but "*", "?", and
character ranges expressed with "[]" will be correctly matched.  This
is done by using the "os.scandir()" and "fnmatch.fnmatch()" functions
in concert, and not by actually invoking a subshell.

Nota:

  The pathnames are returned in no particular order.  If you need a
  specific order, sort the results.

By default, files beginning with a dot (".") can only be matched by
patterns that also start with a dot, unlike "fnmatch.fnmatch()" or
"pathlib.Path.glob()". For tilde and shell variable expansion, use
"os.path.expanduser()" and "os.path.expandvars()".

Para una coincidencia literal, envuelve los meta-caracteres en
corchetes. Por ejemplo, "'[?]'" empareja el caracter "'?'".

The "glob" module defines the following functions:

glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

   Return a possibly empty list of path names that match *pathname*,
   which must be a string containing a path specification. *pathname*
   can be either absolute (like "/usr/src/Python-1.5/Makefile") or
   relative (like "../../Tools/*/*.gif"), and can contain shell-style
   wildcards. Broken symlinks are included in the results (as in the
   shell). Whether or not the results are sorted depends on the file
   system.  If a file that satisfies conditions is removed or added
   during the call of this function, whether a path name for that file
   will be included is unspecified.

   If *root_dir* is not "None", it should be a *path-like object*
   specifying the root directory for searching.  It has the same
   effect on "glob()" as changing the current directory before calling
   it.  If *pathname* is relative, the result will contain paths
   relative to *root_dir*.

   Esta función puede admitir rutas relativas a descriptores de
   directorio con el parámetro *dir_fd*.

   Si *recursive* es verdadero, el patrón ""**"" coincidirá con
   cualquier fichero y cero o más directorios, subdirectorios y
   enlaces simbólicos a directorios.  Si el patrón va seguido de un
   "os.sep" o "os.altsep" los ficheros no coincidirán.

   If *include_hidden* is true, wildcards can match path segments that
   begin with a dot (".").

   Lanza un evento de auditoría "glob.glob" con los argumentos
   "pathname", "recursive".

   Lanza un auditing event "glob.glob/2" con argumentos "pathname",
   "recursive", "root_dir", "dir_fd".

   Nota:

     El uso del patrón ""**"" en árboles de directorios grandes podría
     consumir una cantidad de tiempo excesiva.

   Nota:

     This function may return duplicate path names if *pathname*
     contains multiple ""**"" patterns and *recursive* is true.

   Nota:

     Any "OSError" exceptions raised from scanning the filesystem are
     suppressed. This includes "PermissionError" when accessing
     directories without read permission.

   Distinto en la versión 3.5: Soporte para globs recursivos usando
   ""**"".

   Distinto en la versión 3.10: Se agregaron los parámetros *root_dir*
   y *dir_fd*.

   Distinto en la versión 3.11: Agregado el parámetro
   *include_hidden*.

glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

   Retorna un *iterador* el cual produce los mismos valores que
   "glob()" sin necesidad de almacenarlos todos de forma simultánea.

   Lanza un evento de auditoría "glob.glob" con los argumentos
   "pathname", "recursive".

   Lanza un auditing event "glob.glob/2" con argumentos "pathname",
   "recursive", "root_dir", "dir_fd".

   Nota:

     This function may return duplicate path names if *pathname*
     contains multiple ""**"" patterns and *recursive* is true.

   Nota:

     Any "OSError" exceptions raised from scanning the filesystem are
     suppressed. This includes "PermissionError" when accessing
     directories without read permission.

   Distinto en la versión 3.5: Soporte para globs recursivos usando
   ""**"".

   Distinto en la versión 3.10: Se agregaron los parámetros *root_dir*
   y *dir_fd*.

   Distinto en la versión 3.11: Agregado el parámetro
   *include_hidden*.

glob.escape(pathname)

   Escape all special characters ("'?'", "'*'" and "'['"). This is
   useful if you want to match an arbitrary literal string that may
   have special characters in it.  Special characters in drive/UNC
   sharepoints are not escaped, for example on Windows
   "escape('//?/c:/Quo vadis?.txt')" returns "'//?/c:/Quo
   vadis[?].txt'".

   Added in version 3.4.

glob.translate(pathname, *, recursive=False, include_hidden=False, seps=None)

   Convert the given path specification to a regular expression for
   use with "re.match()". The path specification can contain shell-
   style wildcards.

   For example:

   >>> import glob, re
   >>>
   >>> regex = glob.translate('**/*.txt', recursive=True, include_hidden=True)
   >>> regex
   '(?s:(?:.+/)?[^/]*\\.txt)\\z'
   >>> reobj = re.compile(regex)
   >>> reobj.match('foo/bar/baz.txt')
   <re.Match object; span=(0, 15), match='foo/bar/baz.txt'>

   Path separators and segments are meaningful to this function,
   unlike "fnmatch.translate()". By default wildcards do not match
   path separators, and "*" pattern segments match precisely one path
   segment.

   If *recursive* is true, the pattern segment ""**"" will match any
   number of path segments.

   If *include_hidden* is true, wildcards can match path segments that
   start with a dot (".").

   A sequence of path separators may be supplied to the *seps*
   argument. If not given, "os.sep" and "altsep" (if available) are
   used.

   Ver también:

     "pathlib.PurePath.full_match()" and "pathlib.Path.glob()"
     methods, which call this function to implement pattern matching
     and globbing.

   Added in version 3.13.

## Examples

Consider a directory containing the following files: "1.gif", "2.txt",
"card.gif" and a subdirectory "sub" which contains only the file
"3.txt".  "glob()" will produce the following results.  Notice how any
leading components of the path are preserved.

   >>> import glob
   >>> glob.glob('./[0-9].*')
   ['./1.gif', './2.txt']
   >>> glob.glob('*.gif')
   ['1.gif', 'card.gif']
   >>> glob.glob('?.gif')
   ['1.gif']
   >>> glob.glob('**/*.txt', recursive=True)
   ['2.txt', 'sub/3.txt']
   >>> glob.glob('./**/', recursive=True)
   ['./', './sub/']

Si un directorio contiene ficheros que comienzan con "." no coincidirá
por defecto. Por ejemplo, considera un directorio que contiene
"card.gif" y ".card.gif":

   >>> import glob
   >>> glob.glob('*.gif')
   ['card.gif']
   >>> glob.glob('.c*')
   ['.card.gif']

Ver también:

  The "fnmatch" module offers shell-style filename (not path)
  expansion.

Ver también: El módulo "pathlib" ofrece objetos ruta de alto nivel.
