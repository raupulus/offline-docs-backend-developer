---
title: '"filecmp" --- File and Directory Comparisons'
source_url: https://docs.python.org/es/3
source_path: library/filecmp.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2600
---

# "filecmp" --- File and Directory Comparisons

**Código fuente:**Lib/filecmp.py

======================================================================

The "filecmp" module defines functions to compare files and
directories, with various optional time/correctness trade-offs. For
comparing files, see also the "difflib" module.

The "filecmp" module defines the following functions:

filecmp.cmp(f1, f2, shallow=True)

   Compara los ficheros llamados *f1* y *f2*, retornando "True" si son
   iguales, "False" en caso contrario.

   Si *shallow* es verdadero y las firmas "os.stat()" (tipo de
   fichero, tamaño, y tiempo de modificación) de los dos ficheros son
   idénticas, los ficheros se consideran iguales.

   De lo contrario, los ficheros son tratados como diferentes si sus
   tamaños o contenidos difieren.

   Note que ningún programa externo es llamado desde esta función,
   dándole portabilidad y eficiencia.

   La función utiliza un caché para comparaciones pasadas y los
   resultados, con entradas de caché invalidadas si la información de
   "os.stat()" para el fichero cambia. El caché entero puede ser
   limpiado utilizando "clear_cache()".

filecmp.cmpfiles(a, b, common, shallow=True)

   Compare the files in the two directories *a* and *b* whose names
   are given by *common*.

   Retorna tres listas de nombres de fichero: *match*, *mismatch*,
   *errors*. *match* contiene la lista de ficheros que coinciden,
   *mismatch* contiene los nombres de aquellos que no, y *errors*
   lista los nombres de los ficheros que no deberían ser comparados.
   Los ficheros son listados en *errors* si no existen en uno de los
   directorios, el usuario carece de permisos para leerlos o si la
   comparación no puede hacerse por alguna razón.

   El parámetro *shallow* tiene el mismo significado y valor por
   defecto en cuanto a "filecmp.cmp()".

   Por ejemplo, "cmpfiles('a', 'b', ['c', 'd/e'])" comparará "a/c" con
   "b/c" y "a/d/e" con "b/d/e". "'c'" y "'d/e'" estará cada uno en una
   de las tres listas retornadas.

filecmp.clear_cache()

   Limpia el caché de filecmp. Esto podría ser útil si un fichero es
   comparado muy rápido después de que es modificado que está dentro
   de la resolución mtime del sistema de archivos subyacente.

   Added in version 3.4.

## La clase "dircmp"

class filecmp.dircmp(a, b, ignore=None, hide=None, *, shallow=True)

   Construye un nuevo objeto de comparación de directorio, para
   comparar los directorios *a* y *b*. *ignore* es una lista de
   nombres a ignorar, y predetermina a "filecmp.DEFAULT_IGNORES".
   *hide* es una lista de nombres a ocultar, y predetermina a
   "[os.curdir, os.pardir]".

   The "dircmp" class compares files by doing *shallow* comparisons as
   described for "filecmp.cmp()" by default using the *shallow*
   parameter.

   Distinto en la versión 3.13: Added the *shallow* parameter.

   La clase "dircmp" provee los siguientes métodos:

   report()

      Imprime (a "sys.stdout") una comparación entre *a* y *b*.

   report_partial_closure()

      Imprime una comparación entre *a* y *b* y subdirectorios
      inmediatos comunes.

   report_full_closure()

      Imprime una comparación entre *a* y *b* y subdirectorios comunes
      (recursivamente).

   La clase "dircmp" ofrece un número de atributos interesantes que
   pueden ser utilizados para obtener varios bits de información sobre
   los árboles de directorio que están siendo comparados.

   Note que vía los hooks "__getattr__()", todos los atributos son
   perezosamente computados, así que no hay penalización de velocidad
   si sólo esos atributos que son ligeros de computar son utilizados.

   left

      El directorio *a*.

   right

      El directorio *b*.

   left_list

      Ficheros y subdirectorios en *a*, filtrados por *hide* e
      *ignore*.

   right_list

      Ficheros y subdirectorios en *b*, filtrados por *hide* e
      *ignore*.

   common

      Ficheros y subdirectorios en *a* y *b*.

   left_only

      Ficheros y subdirectorios sólo en *a*.

   right_only

      Ficheros y subdirectorios sólo en *b*.

   common_dirs

      Subdirectorios en *a* y *b*.

   common_files

      Ficheros en *a* y *b*.

   common_funny

      Nombres en *a* y *b*, de forma que el tipo difiera entre los
      directorios, o los nombres por los que "os.stat()" reporta un
      error.

   same_files

      Ficheros que son idénticos en *a* y *b*, utilizando el operador
      de comparación de fichero de la clase.

   diff_files

      Ficheros que están en *a* y *b*, cuyos contenidos difieren
      acorde al operador de comparación del fichero de clase.

   funny_files

      Ficheros que están en *a* y *b*, pero no deberían ser
      comparados.

   subdirs

      Un diccionario que asigna nombres en "common_dirs" a instancias
      "dircmp" (o instancias MyDirCmp si esa instancias es del tipo
      MyDirCmp, una subclase de "dircmp").

      Distinto en la versión 3.10: Anteriormente las entradas siempre
      eran instancias "dircmp". Ahora son del mismo tipo que *self*,
      si *self* es una subclase de "dircmp".

filecmp.DEFAULT_IGNORES

   Added in version 3.4.

   Lista de directorios ignorados por "dircmp" por defecto.

Aquí hay un ejemplo simplificado de uso del atributo "subdirs" para
buscar recursivamente a través de dos directorios para mostrar
diferentes ficheros comunes:

   >>> from filecmp import dircmp
   >>> def print_diff_files(dcmp):
   ...     for name in dcmp.diff_files:
   ...         print("diff_file %s found in %s and %s" % (name, dcmp.left,
   ...               dcmp.right))
   ...     for sub_dcmp in dcmp.subdirs.values():
   ...         print_diff_files(sub_dcmp)
   ...
   >>> dcmp = dircmp('dir1', 'dir2')
   >>> print_diff_files(dcmp)
