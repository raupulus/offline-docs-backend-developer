---
title: '"marshal" --- Internal Python object serialization'
source_url: https://docs.python.org/es/3
source_path: library/marshal.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3190
---

# "marshal" --- Internal Python object serialization

======================================================================

This module contains functions that can read and write Python values
in a binary format.  The format is specific to Python, but independent
of machine architecture issues (e.g., you can write a Python value to
a file on a PC, transport the file to a Mac, and read it back there).
Details of the format are undocumented on purpose; it may change
between Python versions (although it rarely does). [1]

This is not a general "persistence" module.  For general persistence
and transfer of Python objects through RPC calls, see the modules
"pickle" and "shelve".  The "marshal" module exists mainly to support
reading and writing the "pseudo-compiled" code for Python modules of
".pyc" files. Therefore, the Python maintainers reserve the right to
modify the marshal format in backward incompatible ways should the
need arise. The format of code objects is not compatible between
Python versions, even if the version of the format is the same. De-
serializing a code object in the incorrect Python version has
undefined behavior. If you're serializing and de-serializing Python
objects, use the "pickle" module instead -- the performance is
comparable, version independence is guaranteed, and pickle supports a
substantially wider range of objects than marshal.

Advertencia:

  The "marshal" module is not intended to be secure against erroneous
  or maliciously constructed data.  Never unmarshal data received from
  an untrusted or unauthenticated source.

Hay funciones que leen/escriben archivos, así como funciones que
operan en objetos similares a bytes.

Not all Python object types are supported; in general, only objects
whose value is independent from a particular invocation of Python can
be written and read by this module.  The following types are
supported:

* Numeric types: "int", "bool", "float", "complex".

* Strings ("str") and "bytes". *Bytes-like objects* like "bytearray"
  are marshalled as "bytes".

* Containers: "tuple", "list", "set", "frozenset", and (since
  "version" 5), "slice". It should be understood that these are
  supported only if the values contained therein are themselves
  supported. Recursive containers are supported since "version" 3.

* The singletons "None", "Ellipsis" and "StopIteration".

* "code" objects, if *allow_code* is true. See note above about
  version dependence.

Distinto en la versión 3.4:

* Added format version 3, which supports marshalling recursive lists,
  sets and dictionaries.

* Added format version 4, which supports efficient representations of
  short strings.

Distinto en la versión 3.14: Added format version 5, which allows
marshalling slices.

El módulo define estas funciones:

marshal.dump(value, file, version=version, /, *, allow_code=True)

   Escribe el valor en el archivo abierto.  El valor debe ser un tipo
   admitido.  El archivo debe ser un archivo *binary file* en el que
   se pueda escribir.

   If the value has (or contains an object that has) an unsupported
   type, a "ValueError" exception is raised --- but garbage data will
   also be written to the file.  The object will not be properly read
   back by "load()". Code objects are only supported if *allow_code*
   is true.

   El argumento *version* indica el formato de datos que "dump" debe
   usar (véase más adelante).

   Lanza un evento de auditoría "marshal.dumps" con argumentos
   "value", "version".

   Distinto en la versión 3.13: Added the *allow_code* parameter.

marshal.load(file, /, *, allow_code=True)

   Read one value from the open file and return it.  If no valid value
   is read (e.g. because the data has a different Python version's
   incompatible marshal format), raise "EOFError", "ValueError" or
   "TypeError". Code objects are only supported if *allow_code* is
   true. The file must be a readable *binary file*.

   Lanza un evento de auditoría "marshal.load" sin argumentos.

   Nota:

     Si un objeto que contiene un tipo no admitido se calcula con
     "dump()", "load()" sustituirá "None" por el tipo
     "unmarshallable".

   Distinto en la versión 3.10: Esta llamada solía lanzar un evento de
   auditoría "code.__new__" para cada objeto código. Ahora lanza un
   único evento "marshal.load" para toda la operación de carga.

   Distinto en la versión 3.13: Added the *allow_code* parameter.

marshal.dumps(value, version=version, /, *, allow_code=True)

   Return the bytes object that would be written to a file by
   "dump(value, file)".  The value must be a supported type.  Raise a
   "ValueError" exception if value has (or contains an object that
   has) an unsupported type. Code objects are only supported if
   *allow_code* is true.

   El argumento *version* indica el formato de datos que "dumps" debe
   usar (véase más adelante).

   Lanza un evento de auditoría "marshal.dumps" con argumentos
   "value", "version".

   Distinto en la versión 3.13: Added the *allow_code* parameter.

marshal.loads(bytes, /, *, allow_code=True)

   Convert the *bytes-like object* to a value.  If no valid value is
   found, raise "EOFError", "ValueError" or "TypeError". Code objects
   are only supported if *allow_code* is true. Extra bytes in the
   input are ignored.

   Lanza un evento de auditoría "marshal.loads" con argumento "bytes".

   Distinto en la versión 3.10: Esta llamada solía lanzar un evento de
   auditoría "code.__new__" para cada objeto código. Ahora lanza un
   único evento "marshal.loads" para toda la operación de carga.

   Distinto en la versión 3.13: Added the *allow_code* parameter.

Además, se definen las siguientes constantes:

marshal.version

   Indicates the format that the module uses. Version 0 is the
   historical first version; subsequent versions add new features.
   Generally, a new version becomes the default when it is introduced.

   +---------+-----------------+------------------------------------------------------+
   | Version | Available since | New features                                         |
   |=========|=================|======================================================|
   | 1       | Python 2.4      | Sharing interned strings                             |
   +---------+-----------------+------------------------------------------------------+
   | 2       | Python 2.5      | Binary representation of floats                      |
   +---------+-----------------+------------------------------------------------------+
   | 3       | Python 3.4      | Support for object instancing and recursion          |
   +---------+-----------------+------------------------------------------------------+
   | 4       | Python 3.4      | Efficient representation of short strings            |
   +---------+-----------------+------------------------------------------------------+
   | 5       | Python 3.14     | Support for "slice" objects                          |
   +---------+-----------------+------------------------------------------------------+

-[ Notas al pie ]-

[1] El nombre de este módulo proviene de algunos términos utilizados
    por los diseñadores de Modula-3 (entre otros), que utilizan el
    término "marshalling" para el envío de datos de forma auto-
    contenida. Estrictamente hablando "marshalling", significa
    convertir algunos datos internos en un formato externo (por
    ejemplo, en un búfer RPC) y "unmarshalling" es el proceso inverso.
