---
title: '"dbm" --- Interfaces to Unix "databases"'
source_url: https://docs.python.org/es/3
source_path: library/dbm.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2270
---

# "dbm" --- Interfaces to Unix "databases"

**Código fuente:** Lib/dbm/__init__.py

======================================================================

"dbm" is a generic interface to variants of the DBM database:

* "dbm.sqlite3"

* "dbm.gnu"

* "dbm.ndbm"

If none of these modules are installed, the slow-but-simple
implementation in module "dbm.dumb" will be used.  There is a third
party interface to the Oracle Berkeley DB.

exception dbm.error

   Una tupla que contiene las excepciones que pueden ser lanzadas por
   cada uno de los módulos soportados, con una excepción única también
   denominada "dbm.error" como el primer elemento — el último se usa
   cuando se genera "dbm.error".

dbm.whichdb(filename)

   This function attempts to guess which of the several simple
   database modules available --- "dbm.sqlite3", "dbm.gnu",
   "dbm.ndbm", or "dbm.dumb" --- should be used to open a given file.

   Return one of the following values:

   * "None" if the file can't be opened because it's unreadable or
     doesn't exist

   * the empty string ("''") if the file's format can't be guessed

   * a string containing the required module name, such as
     "'dbm.ndbm'" or "'dbm.gnu'"

   Distinto en la versión 3.11: *filename* accepts a *path-like
   object*.

dbm.open(file, flag='r', mode=0o666)

   Open a database and return the corresponding database object.

   Parámetros:
      * **file** (*path-like object*) --

        The database file to open.

        If the database file already exists, the "whichdb()" function
        is used to determine its type and the appropriate module is
        used; if it does not exist, the first submodule listed above
        that can be imported is used.

      * **flag** (*str*) --

        * "'r'" (default): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Distinto en la versión 3.11: *file* accepts a *path-like object*.

The object returned by "open()" supports the basic functionality of
mutable *mappings*; keys and their corresponding values can be stored,
retrieved, and deleted, and iteration, the "in" operator and methods
"keys()", "get()", "setdefault()" and "clear()" are available. The
"keys()" method returns a list instead of a view object. The
"setdefault()" method requires two arguments.

Key and values are always stored as "bytes". This means that when
strings are used they are implicitly converted to the default encoding
before being stored.

Estos objetos también admiten el uso en una instrucción "with", que
los cerrará automáticamente cuando termine.

Distinto en la versión 3.2: "get()" and "setdefault()" methods are now
available for all "dbm" backends.

Distinto en la versión 3.4: Added native support for the context
management protocol to the objects returned by "open()".

Distinto en la versión 3.8: Deleting a key from a read-only database
raises a database module specific exception instead of "KeyError".

Distinto en la versión 3.13: "clear()" methods are now available for
all "dbm" backends.

El siguiente ejemplo registra algunos nombres de host y un título
correspondiente, y luego imprime el contenido de la base de datos:

   import dbm

   # Open database, creating it if necessary.
   with dbm.open('cache', 'c') as db:

       # Record some values
       db[b'hello'] = b'there'
       db['www.python.org'] = 'Python Website'
       db['www.cnn.com'] = 'Cable News Network'

       # Note that the keys are considered bytes now.
       assert db[b'www.python.org'] == b'Python Website'
       # Notice how the value is now in bytes.
       assert db['www.cnn.com'] == b'Cable News Network'

       # Often-used methods of the dict interface work too.
       print(db.get('python.org', b'not present'))

       # Storing a non-string key or value will raise an exception (most
       # likely a TypeError).
       db['www.yahoo.com'] = 4

   # db is automatically closed when leaving the with statement.

Ver también:

  Módulo "shelve"
     Módulo de persistencia que almacena datos que no son cadenas de
     caracteres.

Los submódulos individuales se describen en las siguientes secciones.

## "dbm.sqlite3" --- SQLite backend for dbm

Added in version 3.13.

**Source code:** Lib/dbm/sqlite3.py

======================================================================

This module uses the standard library "sqlite3" module to provide an
SQLite backend for the "dbm" module. The files created by
"dbm.sqlite3" can thus be opened by "sqlite3", or any other SQLite
browser, including the SQLite CLI.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

dbm.sqlite3.open(filename, /, flag='r', mode=0o666)

   Open an SQLite database.

   Parámetros:
      * **filename** (*path-like object*) -- The path to the database
        to be opened.

      * **flag** (*str*) --

        * "'r'" (default): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** -- The Unix file access mode of the file (default:
        octal "0o666"), used only when the database has to be created.

   The returned database object behaves similar to a mutable
   *mapping*, but the "keys()" method returns a list, and the
   "setdefault()" method requires two arguments. It also supports a
   "closing" context manager via the "with" keyword.

   The following method is also provided:

   sqlite3.close()

      Close the SQLite database.

## "dbm.gnu" --- GNU database manager

**Código fuente:** Lib/dbm/gnu.py

======================================================================

The "dbm.gnu" module provides an interface to the GDBM (GNU dbm)
library, similar to the "dbm.ndbm" module, but with additional
functionality like crash tolerance.

Nota:

  The file formats created by "dbm.gnu" and "dbm.ndbm" are
  incompatible and can not be used interchangeably.

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

Availability: Unix.

exception dbm.gnu.error

   Raised on "dbm.gnu"-specific errors, such as I/O errors. "KeyError"
   is raised for general mapping errors like specifying an incorrect
   key.

dbm.gnu.open_flags

   A string of characters the *flag* parameter of "open()" supports.

dbm.gnu.open(filename, flag='r', mode=0o666, /)

   Open a GDBM database and return a "gdbm" object.

   Parámetros:
      * **filename** (*path-like object*) -- The database file to
        open.

      * **flag** (*str*) --

        * "'r'" (default): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

        The following additional characters may be appended to control
        how the database is opened:

        * "'f'": Open the database in fast mode. Writes to the
          database will not be synchronized.

        * "'s'": Synchronized mode. Changes to the database will be
          written immediately to the file.

        * "'u'": Do not lock database.

        Not all flags are valid for all versions of GDBM. See the
        "open_flags" member for a list of supported flag characters.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Muestra:
      **error** -- If an invalid *flag* argument is passed.

   Distinto en la versión 3.11: *filename* accepts a *path-like
   object*.

   "gdbm" objects behave similar to mutable *mappings*, but methods
   "items()", "values()", "pop()", "popitem()", and "update()" are not
   supported, the "keys()" method returns a list, and the
   "setdefault()" method requires two arguments. It also supports a
   "closing" context manager via the "with" keyword.

   Distinto en la versión 3.2: Added the "get()" and "setdefault()"
   methods.

   Distinto en la versión 3.13: Added the "clear()" method.

   The following methods are also provided:

   gdbm.close()

      Close the GDBM database.

   gdbm.firstkey()

      It's possible to loop over every key in the database using this
      method  and the "nextkey()" method.  The traversal is ordered by
      GDBM's internal hash values, and won't be sorted by the key
      values.  This method returns the starting key.

   gdbm.nextkey(key)

      Retorna la clave que sigue a *key* en el recorrido. El siguiente
      código imprime todas las claves en la base de datos "db", sin
      tener que crear una lista en la memoria que las contenga todas:

         k = db.firstkey()
         while k is not None:
             print(k)
             k = db.nextkey(k)

   gdbm.reorganize()

      If you have carried out a lot of deletions and would like to
      shrink the space used by the GDBM file, this routine will
      reorganize the database.  "gdbm" objects will not shorten the
      length of a database file except by using this reorganization;
      otherwise, deleted file space will be kept and reused as new
      (key, value) pairs are added.

   gdbm.sync()

      Cuando la base de datos se ha abierto en modo rápido, este
      método obliga a que los datos no escritos se escriban en el
      disco.

## "dbm.ndbm" --- New Database Manager

**Código fuente:** Lib/dbm/ndbm.py

======================================================================

The "dbm.ndbm" module provides an interface to the NDBM (New Database
Manager) library. This module can be used with the "classic" NDBM
interface or the GDBM (GNU dbm) compatibility interface.

Nota:

  The file formats created by "dbm.gnu" and "dbm.ndbm" are
  incompatible and can not be used interchangeably.

Advertencia:

  The NDBM library shipped as part of macOS has an undocumented
  limitation on the size of values, which can result in corrupted
  database files when storing values larger than this limit. Reading
  such corrupted files can result in a hard crash (segmentation
  fault).

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

Availability: Unix.

exception dbm.ndbm.error

   Raised on "dbm.ndbm"-specific errors, such as I/O errors.
   "KeyError" is raised for general mapping errors like specifying an
   incorrect key.

dbm.ndbm.library

   Name of the NDBM implementation library used.

dbm.ndbm.open(filename, flag='r', mode=0o666, /)

   Open an NDBM database and return an "ndbm" object.

   Parámetros:
      * **filename** (*path-like object*) -- The basename of the
        database file (without the ".dir" or ".pag" extensions).

      * **flag** (*str*) --

        * "'r'" (default): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Distinto en la versión 3.11: Acepta *path-like object* como nombre
   de archivo.

   "ndbm" objects behave similar to mutable *mappings*, but methods
   "items()", "values()", "pop()", "popitem()", and "update()" are not
   supported, the "keys()" method returns a list, and the
   "setdefault()" method requires two arguments. It also supports a
   "closing" context manager via the "with" keyword.

   Distinto en la versión 3.2: Added the "get()" and "setdefault()"
   methods.

   Distinto en la versión 3.13: Added the "clear()" method.

   The following method is also provided:

   ndbm.close()

      Close the NDBM database.

## "dbm.dumb" --- Portable DBM implementation

**Código fuente:** Lib/dbm/dumb.py

Nota:

  The "dbm.dumb" module is intended as a last resort fallback for the
  "dbm" module when a more robust module is not available. The
  "dbm.dumb" module is not written for speed and is not nearly as
  heavily used as the other database modules.

======================================================================

The "dbm.dumb" module provides a persistent "dict"-like interface
which is written entirely in Python. Unlike other "dbm" backends, such
as "dbm.gnu", no external library is required.

The "dbm.dumb" module defines the following:

exception dbm.dumb.error

   Raised on "dbm.dumb"-specific errors, such as I/O errors.
   "KeyError" is raised for general mapping errors like specifying an
   incorrect key.

dbm.dumb.open(filename, flag='c', mode=0o666)

   Open a "dbm.dumb" database.

   Parámetros:
      * **filename** --

        The basename of the database file (without extensions). A new
        database creates the following files:

        * "*filename*.dat"

        * "*filename*.dir"

      * **flag** (*str*) --

        * "'r'": Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'" (default): Open database for reading and writing,
          creating it if it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Advertencia:

     Es posible bloquear el intérprete de Python cuando se carga una
     base de datos con una entrada suficientemente grande/compleja
     debido a las limitaciones de profundidad de la pila en el
     compilador AST de Python.

   Distinto en la versión 3.5: "open()" always creates a new database
   when *flag* is "'n'".

   Distinto en la versión 3.8: A database opened read-only if *flag*
   is "'r'". A database is not created if it does not exist if *flag*
   is "'r'" or "'w'".

   Distinto en la versión 3.11: *filename* accepts a *path-like
   object*.

   The returned database object behaves similar to a mutable
   *mapping*, but the "keys()" and "items()" methods return lists, and
   the "setdefault()" method requires two arguments. It also supports
   a "closing" context manager via the "with" keyword.

   The following methods are also provided:

   dumbdbm.close()

      Close the database.

   dumbdbm.sync()

      Synchronize the on-disk directory and data files.  This method
      is called by the "shelve.Shelf.sync()" method.
