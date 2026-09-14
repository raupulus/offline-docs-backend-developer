---
title: '"shelve" --- Python object persistence'
source_url: https://docs.python.org/es/3
source_path: library/shelve.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3760
---

# "shelve" --- Python object persistence

**Source code:** Lib/shelve.py

======================================================================

Un "estante" o *shelve*, es un objeto persistente similar a un
diccionario.  La diferencia con las bases de datos "dbm" es que los
valores (¡no las claves!) en un estante pueden ser esencialmente
objetos Python arbitrarios --- cualquier cosa que el módulo "pickle"
pueda manejar. Esto incluye la mayoría de las instancias de clase,
tipos de datos recursivos y objetos que contienen muchos subobjetos
compartidos.  Las claves son cadenas ordinarias.

shelve.open(filename, flag='c', protocol=None, writeback=False)

   Abre un diccionario persistente.  El nombre de archivo especificado
   es el nombre de archivo base para la base de datos subyacente.
   Como efecto secundario, se puede agregar una extensión al nombre de
   archivo y se puede crear más de un archivo.  De forma
   predeterminada, el archivo de base de datos subyacente se abre para
   leer y escribir.  El parámetro opcional *flag* tiene la misma
   interpretación que el parámetro *flag* de "dbm.open()".

   By default, pickles created with "pickle.DEFAULT_PROTOCOL" are used
   to serialize values.  The version of the pickle protocol can be
   specified with the *protocol* parameter.

   Debido a la semántica de Python, un estante no puede saber cuándo
   se modifica una entrada de diccionario persistente mutable.  De
   forma predeterminada, los objetos modificados se escriben *sólo*
   cuando se asignan al estante (consulte Ejemplo).  Si el parámetro
   opcional *writeback* se establece en "True", todas las entradas a
   las que se accede también se almacenan en caché en la memoria y se
   vuelven a escribir en "sync()" y "close()"; esto puede hacer que
   sea más práctico mutar entradas mutables en el diccionario
   persistente, pero, si se accede a muchas entradas, puede consumir
   grandes cantidades de memoria para la memoria caché, y puede hacer
   que la operación de cierre sea muy lenta ya que todas las entradas
   a las que se accede se vuelven a escribir (no hay manera de
   determinar qué entradas a las que se accede son mutables, ni cuáles
   se mutaron realmente).

   Distinto en la versión 3.10: "pickle.DEFAULT_PROTOCOL" is now used
   as the default pickle protocol.

   Distinto en la versión 3.11: Acepta *path-like object* por nombre
   de archivo.

   Nota:

     No confíe en que el estante se cerrará automáticamente; siempre
     llame a "close()"  explícitamente cuando ya no lo necesite, o use
     "shelve.open()" como administrador de contexto:

        with shelve.open('spam') as db:
            db['eggs'] = 'eggs'

Advertencia:

  Because the "shelve" module is backed by "pickle", it is insecure to
  load a shelf from an untrusted source.  Like with pickle, loading a
  shelf can execute arbitrary code.

Shelf objects support most of the methods and operations supported by
dictionaries (except copying, constructors and operators "|" and
"|=").  This eases the transition from dictionary based scripts to
those requiring persistent storage.

Se admiten dos métodos adicionales:

Shelf.sync()

   Escriba todas las entradas en la caché si el estante se abrió con
   *writeback* establecido en "True". También vacíe la caché y
   sincronice el diccionario persistente en el disco, si es posible.
   Esto se llama automáticamente cuando el estante se cierra con
   "close()".

Shelf.close()

   Sincronice y cierre el objeto persistente *dict*. Las operaciones
   en un estante cerrado fallarán con un "ValueError".

Ver también:

  Persistent dictionary recipe with widely supported storage formats
  and having the speed of native dictionaries.

## Restricciones

* La elección de qué paquete de base de datos se utilizará (como
  "dbm.ndbm" o "dbm.gnu") depende de la interfaz disponible. Por lo
  tanto, no es seguro abrir la base de datos directamente usando
  "dbm". La base de datos también está (desafortunadamente) sujeta a
  las limitaciones de "dbm", si se usa --- esto significa que (la
  representación *pickle* de) los objetos almacenados en la base de
  datos debe ser bastante pequeña, y en casos raros las colisiones de
  claves pueden hacer que la base de datos rechace las
  actualizaciones.

* The "shelve" module does not support *concurrent* read/write access
  to shelved objects.  (Multiple simultaneous read accesses are safe.)
  When a program has a shelf open for writing, no other program should
  have it open for reading or writing.  Unix file locking can be used
  to solve this, but this differs across Unix versions and requires
  knowledge about the database implementation used.

* On macOS "dbm.ndbm" can silently corrupt the database file on
  updates, which can cause hard crashes when trying to read from the
  database.

class shelve.Shelf(dict, protocol=None, writeback=False, keyencoding='utf-8')

   Una subclase de "collections.abc.MutableMapping" que almacena
   valores *pickle* en el objeto *dict*.

   By default, pickles created with "pickle.DEFAULT_PROTOCOL" are used
   to serialize values.  The version of the pickle protocol can be
   specified with the *protocol* parameter.  See the "pickle"
   documentation for a discussion of the pickle protocols.

   Si el parámetro *writeback* es "True", el objeto mantendrá un caché
   de todas las entradas a las que se accedió y las volverá a escribir
   en el *dict* en las horas de sincronización y cierre. Esto permite
   operaciones naturales en entradas mutables, pero puede consumir
   mucha más memoria y hacer que la sincronización y el cierre tomen
   mucho tiempo.

   El parámetro *keyencoding* es la codificación utilizada para
   codificar las claves antes de que se utilicen con el *dict*
   subyacente.

   El objeto "Shelf" también se puede utilizar como administrador de
   contexto, en cuyo caso se cerrará automáticamente cuando finalice
   el bloque "with".

   Distinto en la versión 3.2: Se agregó el parámetro *keyencoding*;
   anteriormente, las claves siempre estaban codificadas en UTF-8.

   Distinto en la versión 3.4: Agregado soporte para administrador de
   contexto.

   Distinto en la versión 3.10: "pickle.DEFAULT_PROTOCOL" is now used
   as the default pickle protocol.

class shelve.BsdDbShelf(dict, protocol=None, writeback=False, keyencoding='utf-8')

   A subclass of "Shelf" which exposes "first()", "next()",
   "previous()", "last()" and "set_location()" methods. These are
   available in the third-party "bsddb" module from pybsddb but not in
   other database modules.  The *dict* object passed to the
   constructor must support those methods.  This is generally
   accomplished by calling one of "bsddb.hashopen()", "bsddb.btopen()"
   or "bsddb.rnopen()".  The optional *protocol*, *writeback*, and
   *keyencoding* parameters have the same interpretation as for the
   "Shelf" class.

class shelve.DbfilenameShelf(filename, flag='c', protocol=None, writeback=False)

   Una subclase de "Shelf" que acepta un *filename* en lugar de un
   objeto tipo diccionario (*dict*). El archivo subyacente se abrirá
   usando "dbm.open()". De forma predeterminada, el archivo se creará
   y se abrirá tanto para lectura como para escritura. El parámetro
   opcional *flag* tiene la misma interpretación que para la función
   "open()". Los parámetros opcionales *protocol* y *writeback* tienen
   la misma interpretación que para la clase "Shelf".

## Ejemplo

Para resumir la interfaz ("key" es una cadena de caracteres, "data" es
un objeto arbitrario):

   import shelve

   d = shelve.open(filename)  # open -- file may get suffix added by low-level
                              # library

   d[key] = data              # store data at key (overwrites old data if
                              # using an existing key)
   data = d[key]              # retrieve a COPY of data at key (raise KeyError
                              # if no such key)
   del d[key]                 # delete data stored at key (raises KeyError
                              # if no such key)

   flag = key in d            # true if the key exists
   klist = list(d.keys())     # a list of all existing keys (slow!)

   # as d was opened WITHOUT writeback=True, beware:
   d['xx'] = [0, 1, 2]        # this works as expected, but...
   d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

   # having opened d without writeback=True, you need to code carefully:
   temp = d['xx']             # extracts the copy
   temp.append(5)             # mutates the copy
   d['xx'] = temp             # stores the copy right back, to persist it

   # or, d=shelve.open(filename,writeback=True) would let you just code
   # d['xx'].append(5) and have it work as expected, BUT it would also
   # consume more memory and make the d.close() operation slower.

   d.close()                  # close it

Ver también:

  Módulo "dbm"
     Interfaz genérica para bases de datos estilo "dbm".

  Módulo "pickle"
     Object serialization used by "shelve".
