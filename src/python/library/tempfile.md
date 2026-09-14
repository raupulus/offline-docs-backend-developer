---
title: '"tempfile" --- Generate temporary files and directories'
source_url: https://docs.python.org/es/3
source_path: library/tempfile.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4080
---

# "tempfile" --- Generate temporary files and directories

**Código fuente:** Lib/tempfile.py

======================================================================

This module creates temporary files and directories.  It works on all
supported platforms. "TemporaryFile", "NamedTemporaryFile",
"TemporaryDirectory", and "SpooledTemporaryFile" are high-level
interfaces which provide automatic cleanup and can be used as *context
managers*. "mkstemp()" and "mkdtemp()" are lower-level functions which
require manual cleanup.

Todas las funciones y constructores invocables por el usuario toman
argumentos adicionales que permiten el control directo sobre la
ubicación y el nombre de los archivos y directorios temporales. Los
nombres de archivos utilizados por este módulo incluyen una cadena de
caracteres aleatorios que permite que esos archivos se creen de forma
segura en directorios temporales compartidos. Para mantener la
compatibilidad con versiones anteriores, el orden de argumentos es
algo extraño; se recomienda utilizar argumentos nombrados para mayor
claridad.

El módulo define los siguientes elementos invocables por el usuario:

tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

   Retorna un *file-like object* que se puede usar como área de
   almacenamiento temporal. El archivo se crea de forma segura, usando
   las mismas reglas que "mkstemp()". Este se destruirá tan pronto
   como se cierre (incluido un cierre implícito cuando el objeto es
   recolectado como basura). Bajo Unix, la entrada de directorio para
   el archivo no se crea en lo absoluto o se elimina inmediatamente
   después de crear el archivo. Otras plataformas no soportan esto; tu
   código no debería depender en un archivo temporal creado con esta
   función teniendo o no un nombre visible en el sistema de archivos.

   The resulting object can be used as a *context manager* (see
   Ejemplos).  On completion of the context or destruction of the file
   object the temporary file will be removed from the filesystem.

   El parámetro *mode* por defecto es "'w+b'" para que el archivo
   creado pueda leerse y escribirse sin cerrarse.  El modo binario se
   utiliza para que se comporte consistentemente en todas las
   plataformas sin tener en cuenta los datos que se almacenan.
   *buffering*, *encoding*, *errors* y *newline* se interpretan como
   en "open()".

   Los parámetros *dir*, *prefix* y *suffix* tienen el mismo
   significado y valores predeterminados de "mkstemp()".

   El objeto retornado es un objeto de archivo verdadero en las
   plataformas POSIX. En otras plataformas, es un objeto similar a un
   archivo cuyo atributo "file" es el objeto de archivo verdadero
   subyacente.

   El indicador "os.O_TMPFILE" se usa si está disponible y funciona
   (específico de Linux, requiere el kernel de Linux 3.11 o
   posterior).

   En plataformas que no son ni Posix ni Cygwin, TemporaryFile es un
   alias de NamedTemporaryFile.

   Lanza un evento de auditoria "tempfile.mkstemp" con argumento
   "fullpath".

   Distinto en la versión 3.5: El indicador "os.O_TMPFILE" ahora se
   usa si está disponible.

   Distinto en la versión 3.8: Se agregó el parámetro *errors*.

tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None, delete_on_close=True)

   Esta función opera exactamente como "TemporaryFile()", excepto por
   las siguientes diferencias:

   * Esta función retorna un archivo que tiene garantizado un nombre
     visible en el sistema de archivos.

   * Para administrar el archivo nombrado, amplía los parámetros de
     "TemporaryFile()" con los parámetros *delete* y *delete_on_close*
     que determinan si el archivo nombrado debe eliminarse
     automáticamente y cómo.

   The returned object is always a *file-like object* whose "file"
   attribute is the underlying true file object. This file-like object
   can be used in a "with" statement, just like a normal file.  The
   name of the temporary file can be retrieved from the "name"
   attribute of the returned file-like object. On Unix, unlike with
   the "TemporaryFile()", the directory entry does not get unlinked
   immediately after the file creation.

   Si *delete* es true (el valor predeterminado) y *delete_on_close*
   es true (el valor predeterminado), el archivo se elimina tan pronto
   como se cierra. Si *delete* es true y *delete_on_close* es false,
   el archivo se elimina solo al salir del administrador de contexto,
   o bien cuando se finaliza el *file-like object*. La eliminación no
   siempre está garantizada en este caso (ver "object.__del__()"). Si
   *delete* es false, se omite el valor de *delete_on_close*.

   Por lo tanto, para usar el nombre del archivo temporal para volver
   a abrir el archivo después de cerrarlo, asegúrese de no eliminar el
   archivo al cerrarlo (establezca el parámetro *delete* en false) o,
   en caso de que el archivo temporal se cree en una declaración
   "with", establezca el parámetro *delete_on_close* en false. Se
   recomienda este último enfoque, ya que proporciona asistencia en la
   limpieza automática del archivo temporal al salir del administrador
   de contexto.

   Abrir el archivo temporal de nuevo por su nombre mientras todavía
   está abierto funciona de la siguiente forma:

   * En POSIX el archivo siempre se puede volver a abrir.

   * En Windows, asegúrese de que se cumple al menos una de las
     siguientes condiciones:

     * *delete* es falso

     * la función de apertura adicional comparte el acceso de
       eliminación (por ejemplo, llamando "os.open()" con la opción
       "O_TEMPORARY")

     * *delete* es verdadero, pero *delete_on_close* es falso. Tenga
       en cuenta que, en este caso, las funciones de apertura
       adicional que no comparten el acceso de eliminación (por
       ejemplo, creado mediante el tipo integrado "open()") deben
       cerrarse antes de salir del gestor de contexto, sino la llamada
       "os.unlink()" al salir del gestor de contexto fallará con un
       "PermissionError".

   En Windows, si *delete_on_close* es falso y el archivo se crea en
   un directorio para el que el usuario carece de acceso de
   eliminación, la llamada "os.unlink()" al salir del gestor de
   contexto fallará con un "PermissionError". Esto no puede suceder
   cuando *delete_on_close* es true, porque el acceso de eliminación
   es solicitado por la función de apertura, que falla inmediatamente
   si no se concede el acceso solicitado.

   En POSIX (solo), un proceso que finaliza abruptamente con SIGKILL
   no puede eliminar automáticamente ningún NamedTemporaryFiles que se
   haya creado.

   Lanza un evento de auditoria "tempfile.mkstemp" con argumento
   "fullpath".

   Distinto en la versión 3.8: Se agregó el parámetro *errors*.

   Distinto en la versión 3.12: Se agregó el parámetro
   *delete_on_close*.

class tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

   This class operates exactly as "TemporaryFile()" does, except that
   data is spooled in memory until the file size exceeds *max_size*,
   or until the file's "fileno()" method is called, at which point the
   contents are written to disk and operation proceeds as with
   "TemporaryFile()".

   rollover()

      The resulting file has one additional method, "rollover()",
      which causes the file to roll over to an on-disk file regardless
      of its size.

   The returned object is a file-like object whose "_file" attribute
   is either an "io.BytesIO" or "io.TextIOWrapper" object (depending
   on whether binary or text *mode* was specified) or a true file
   object, depending on whether "rollover()" has been called.  This
   file-like object can be used in a "with" statement, just like a
   normal file.

   Distinto en la versión 3.3: the truncate method now accepts a
   *size* argument.

   Distinto en la versión 3.8: Se agregó el parámetro *errors*.

   Distinto en la versión 3.11: Implementa completamente las clases
   base abstractas "io.BufferedIOBase" y "io.TextIOBase" (dependiendo
   de si se especificó *modo* binario o de texto).

class tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None, ignore_cleanup_errors=False, *, delete=True)

   This class securely creates a temporary directory using the same
   rules as "mkdtemp()". The resulting object can be used as a
   *context manager* (see Ejemplos).  On completion of the context or
   destruction of the temporary directory object, the newly created
   temporary directory and all its contents are removed from the
   filesystem.

   name

      The directory name can be retrieved from the "name" attribute of
      the returned object.  When the returned object is used as a
      *context manager*, the "name" will be assigned to the target of
      the "as" clause in the "with" statement, if there is one.

   cleanup()

      The directory can be explicitly cleaned up by calling the
      "cleanup()" method. If *ignore_cleanup_errors* is true, any
      unhandled exceptions during explicit or implicit cleanup (such
      as a "PermissionError" removing open files on Windows) will be
      ignored, and the remaining removable items deleted on a "best-
      effort" basis. Otherwise, errors will be raised in whatever
      context cleanup occurs (the "cleanup()" call, exiting the
      context manager, when the object is garbage-collected or during
      interpreter shutdown).

   El parámetro *delete* se puede utilizar para deshabilitar la
   limpieza del árbol de directorios al salir del contexto. Aunque
   puede parecer inusual que un administrador de contexto deshabilite
   la acción realizada al salir del contexto, puede ser útil durante
   la depuración o cuando necesita que el comportamiento de limpieza
   sea condicional en función de otra lógica.

   Lanza un evento de auditoria "tempfile.mkdtemp" con argumento
   "fullpath".

   Added in version 3.2.

   Distinto en la versión 3.10: Se agregó el parámetro
   *ignore_cleanup_errors*.

   Distinto en la versión 3.12: Se agregó el parámetro *delete*.

tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)

   Creates a temporary file in the most secure manner possible.  There
   are no race conditions in the file's creation, assuming that the
   platform properly implements the "os.O_EXCL" flag for "os.open()".
   The file is readable and writable only by the creating user ID.  If
   the platform uses permission bits to indicate whether a file is
   executable, the file is executable by no one.

   The file descriptor is not inherited by child processes.

   Unlike "TemporaryFile()", the user of "mkstemp()" is responsible
   for closing the file descriptor (for example, using "os.close()")
   and deleting the temporary file (for example, using "os.remove()").

   Si *suffix* no es "None", el nombre del archivo terminará con ese
   sufijo, de lo contrario no habrá sufijo.  "mkstemp()" no pone un
   punto entre el nombre del archivo y el sufijo; si necesita uno,
   póngalo al comienzo del *suffix*.

   Si *prefix* no es "None", el nombre del archivo comenzará con ese
   prefijo; de lo contrario, se usa un prefijo predeterminado.  El
   valor predeterminado es el valor de retorno de "gettempprefix()" o
   "gettempprefixb()", según corresponda.

   Si *dir* no es "None", el archivo se creará en ese directorio; de
   lo contrario, se usa un directorio predeterminado. El directorio
   predeterminado se elige de una lista dependiente de la plataforma,
   pero el usuario de la aplicación puede controlar la ubicación del
   directorio configurando las variables de entorno *TMPDIR*, *TEMP* o
   *TMP* .  Por lo tanto, no hay garantía de que el nombre de archivo
   generado tenga buenas propiedades, como no requerir comillas cuando
   se pasa a comandos externos a través de "os.popen()".

   Si alguno de los argumentos *suffix*, *prefix*, y *dir* no son
   "None", estos deben ser del mismo tipo. Si son bytes, el nombre
   retornado será bytes en lugar de str. Si desea forzar un valor de
   retorno de bytes con un comportamiento predeterminado, pase
   "suffix=b’’".

   Si se especifica *text* y es verdadero, el archivo se abre en modo
   texto. De lo contrario, (por defecto) el archivo se abre en modo
   binario.

   "mkstemp()" retorna una tupla que contiene un controlador de nivel
   de sistema operativo a un archivo abierto (como sería retornado por
   "os.open()") y la ruta absoluta de ese archivo, en ese orden.

   Lanza un evento de auditoria "tempfile.mkstemp" con argumento
   "fullpath".

   Distinto en la versión 3.5: *suffix*, *prefix*, y *dir* ahora se
   pueden suministrar en bytes para obtener el valor de retorno en
   bytes.  Antes de esto, solo str se permitía. *suffix* y *prefix*
   ahora aceptan y por defecto "None" para hacer que se use un valor
   predeterminado apropiado.

   Distinto en la versión 3.6: El parámetro *dir* ahora acepta un
   *path-like object*.

tempfile.mkdtemp(suffix=None, prefix=None, dir=None)

   Crea un directorio temporal de la manera más segura posible. No hay
   condiciones de carrera en la creación del directorio.  El
   directorio se puede leer, escribir y buscar solo por el ID del
   usuario creador.

   El usuario de "mkdtemp()" es responsable de eliminar el directorio
   temporal y su contenido cuando haya terminado con él.

   Los argumentos *prefix*, *suffix*, y *dir* son los mismos que para
   "mkstemp()".

   "mkdtemp()" retorna la ruta absoluta del nuevo directorio.

   Lanza un evento de auditoria "tempfile.mkdtemp" con argumento
   "fullpath".

   Distinto en la versión 3.5: *suffix*, *prefix*, y *dir* ahora se
   pueden suministrar en bytes para obtener el valor de retorno en
   bytes.  Antes de esto, solo str se permitía. *suffix* y *prefix*
   ahora aceptan y por defecto "None" para hacer que se use un valor
   predeterminado apropiado.

   Distinto en la versión 3.6: El parámetro *dir* ahora acepta un
   *path-like object*.

   Distinto en la versión 3.12: "mkdtemp()" no siempre retorna la ruta
   absoluta del nuevo directorio, incluso si *dir* es relativo.

tempfile.gettempdir()

   Retorna el nombre del directorio utilizado para archivos
   temporales. Esto define el valor predeterminado para el argumento
   *dir* para todas las funciones en este módulo.

   Python busca en una lista estándar de directorios para encontrar
   uno dentro del cual el usuario pueda crear archivos.  La lista es:

   1. El directorio nombrado por la variable de entorno "TMPDIR".

   2. El directorio nombrado por la variable de entorno "TEMP".

   3. El directorio nombrado por la variable de entorno "TMP".

   4. Una ubicación especifica de la plataforma:

      * En Windows, los directorios "C:\TEMP", "C:\TMP", "\TEMP", y
        "\TMP", en ese orden.

      * En todas las otras plataformas, los directorios "/tmp",
        "/var/tmp", y "/usr/tmp", en ese orden.

   5. Y como última alternativa, el directorio de trabajo actual.

   El resultado de la búsqueda es cacheada, vea la descripción de
   "tempdir" abajo.

   Distinto en la versión 3.10: Siempre retorna str. Anteriormente
   retornaría cualquier valor "tempdir" independientemente del tipo
   siempre que no fuera "None".

tempfile.gettempdirb()

   Igual a "gettempdir()" pero el valor retornado es en bytes.

   Added in version 3.5.

tempfile.gettempprefix()

   Retorna el prefijo del nombre de archivo utilizado para crear
   archivos temporales. Este no contiene el componente de directorio.

tempfile.gettempprefixb()

   Igual que "gettempprefix()" pero el valor retornado es en bytes.

   Added in version 3.5.

El módulo utiliza una variable global para almacenar el nombre del
directorio utilizado para los archivos temporales retornados por
"gettempdir()".  Se puede configurar directamente para sobrescribir el
proceso de selección, pero esto no se recomienda. Todas las funciones
en este módulo toman un argumento *dir* que puede usarse para
especificar el directorio. Este es el enfoque recomendado que no toma
por sorpresa otro código inesperado al cambiar el comportamiento
global de la API.

tempfile.tempdir

   Cuando se establece en un valor distinto de "None", esta variable
   define el valor predeterminado para el argumento *dir* para las
   funciones definidas en este módulo, incluyendo su tipo, bytes o
   str. No puede ser un *path-like object*.

   Si "tempdir" es "None" (por defecto) en cualquier llamada a
   cualquiera de las funciones anteriores excepto "gettempprefix()" se
   inicializa siguiendo el algoritmo descrito en "gettempdir()".

   Nota:

     Tenga en cuenta que si establece "tempdir" en un valor de bytes,
     hay un efecto secundario desagradable: el tipo de retorno global
     predeterminado de "mkstemp()" y "mkdtemp()" cambia a bytes cuando
     no se proporcionan argumentos explícitos "prefix", "suffix" o
     "dir" de tipo str. Por favor, no escriba código esperando o
     dependiendo de esto. Este comportamiento incómodo se mantiene por
     compatibilidad con la implementación histórica.

## Ejemplos

Here are some examples of typical usage of the "tempfile" module:

   >>> import tempfile

   # create a temporary file and write some data to it
   >>> fp = tempfile.TemporaryFile()
   >>> fp.write(b'Hello world!')
   # read data from file
   >>> fp.seek(0)
   >>> fp.read()
   b'Hello world!'
   # close the file, it will be removed
   >>> fp.close()

   # create a temporary file using a context manager
   >>> with tempfile.TemporaryFile() as fp:
   ...     fp.write(b'Hello world!')
   ...     fp.seek(0)
   ...     fp.read()
   b'Hello world!'
   >>>
   # file is now closed and removed

   # create a temporary file using a context manager
   # close the file, use the name to open the file again
   >>> with tempfile.NamedTemporaryFile(delete_on_close=False) as fp:
   ...     fp.write(b'Hello world!')
   ...     fp.close()
   ... # the file is closed, but not removed
   ... # open the file again by using its name
   ...     with open(fp.name, mode='rb') as f:
   ...         f.read()
   b'Hello world!'
   >>>
   # file is now removed

   # create a temporary directory using the context manager
   >>> with tempfile.TemporaryDirectory() as tmpdirname:
   ...     print('created temporary directory', tmpdirname)
   >>>
   # directory and contents have been removed

## Funciones y variables deprecadas

Una forma histórica de crear archivos temporales era generar primero
un nombre de archivo con la función "mktemp()" y luego crear un
archivo con este nombre. Desafortunadamente, esto no es seguro, porque
un proceso diferente puede crear un archivo con este nombre en el
tiempo entre la llamada a "mktemp()" y el intento posterior de crear
el archivo mediante el primer proceso. La solución es combinar los dos
pasos y crear el archivo de inmediato. Este enfoque es utilizado por
"mkstemp()" y las otras funciones descritas anteriormente.

tempfile.mktemp(suffix='', prefix='tmp', dir=None)

   Obsoleto desde la versión 2.3: Utilice "mkstemp()" en su lugar.

   Retorna el nombre de la ruta absoluta de un archivo que no existía
   en el momento en que se realiza la llamada. Los argumentos
   *prefix*, *suffix* y *dir* son similares a los de "mkstemp()",
   excepto los nombres de archivo de bytes, "suffix=None" y
   "prefix=None" no son soportados.

   Advertencia:

     El uso de esta función puede introducir un agujero de seguridad
     en su programa. Para cuando llegues a hacer algo con el nombre de
     archivo que retorna, alguien más pudo haberse adelantado.  El uso
     de "mktemp()" se puede reemplazar fácilmente con
     "NamedTemporaryFile()", pasándole el parámetro "delete=False":

        >>> f = NamedTemporaryFile(delete=False)
        >>> f.name
        '/tmp/tmptjujjt'
        >>> f.write(b"Hello World!\n")
        13
        >>> f.close()
        >>> os.unlink(f.name)
        >>> os.path.exists(f.name)
        False
