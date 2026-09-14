---
title: Utilidades del sistema operativo
source_url: https://docs.python.org/es/3
source_path: c-api/sys.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 680
---

# Utilidades del sistema operativo

PyObject *PyOS_FSPath(PyObject *path)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.6.*

   Retorna la representación del sistema de archivos para *path*. Si
   el objeto es "str" o "bytes", entonces se retorna una nueva
   *referencia fuerte*. Si el objeto implementa la interfaz
   "os.PathLike", entonces "__fspath__()" se retorna siempre que sea
   un objeto "str" o "bytes". De lo contrario "TypeError" se lanza y
   se retorna "NULL".

   Added in version 3.6.

int Py_FdIsInteractive(FILE *fp, const char *filename)

   Retorna verdadero (distinto de cero) si el archivo de E/S (*I/O*)
   estándar *fp* con nombre *filename* se considera interactivo. Este
   es el caso de los archivos para los que "isatty(fileno(fp))" es
   verdadero. Si "PyConfig.interactive" es distinto de cero, esta
   función también retorna verdadero si el puntero *filename* es
   "NULL" o si el nombre es igual a una de las cadenas de caracteres
   "'<stdin>'" o "'???'".

   Esta función no debe ser llamada antes de que Python sea
   inicializado.

void PyOS_BeforeFork()
    * Part of the Stable ABI on platforms with fork() since version
   3.7.*

   Función para preparar algún estado interno antes de una bifurcación
   de proceso (*process fork*). Esto debería llamarse antes de llamar
   a "fork()" o cualquier función similar que clone el proceso actual.
   Solo disponible en sistemas donde "fork()" está definido.

   Advertencia:

     La llamada C "fork()" solo debe hacerse desde hilo "principal"
     (del intérprete "principal"). Lo mismo es cierto para
     "PyOS_BeforeFork()".

   Added in version 3.7.

void PyOS_AfterFork_Parent()
    * Part of the Stable ABI on platforms with fork() since version
   3.7.*

   Función para actualizar algún estado interno después de una
   bifurcación de proceso. Se debe invocar desde el proceso principal
   después de llamar a "fork()" o cualquier función similar que clone
   el proceso actual, independientemente de si la clonación del
   proceso fue exitosa. Solo disponible en sistemas donde "fork()"
   está definido.

   Advertencia:

     La llamada C "fork()" solo debe hacerse desde hilo "principal"
     (del intérprete "principal"). Lo mismo es cierto para
     "PyOS_AfterFork_Parent()".

   Added in version 3.7.

void PyOS_AfterFork_Child()
    * Part of the Stable ABI on platforms with fork() since version
   3.7.*

   Función para actualizar el estado del intérprete interno después de
   una bifurcación de proceso (*process fork*). Debe llamarse desde el
   proceso secundario después de llamar a "fork()", o cualquier
   función similar que clone el proceso actual, si existe alguna
   posibilidad de que el proceso vuelva a llamar al intérprete de
   Python. Solo disponible en sistemas donde "fork()" está definido.

   Advertencia:

     La llamada C "fork()" solo debe hacerse desde hilo "principal"
     (del intérprete "principal"). Lo mismo es cierto para
     "PyOS_AfterFork_Child()".

   Added in version 3.7.

   Ver también:

     "os.register_at_fork()" permite registrar funciones
     personalizadas de Python a las que puede llamar
     "PyOS_BeforeFork()", "PyOS_AfterFork_Parent()" y
     "PyOS_AfterFork_Child()".

void PyOS_AfterFork()
    * Part of the Stable ABI on platforms with fork().*

   Función para actualizar algún estado interno después de una
   bifurcación de proceso (*process fork*); Esto debería llamarse en
   el nuevo proceso si el intérprete de Python continuará siendo
   utilizado. Si se carga un nuevo ejecutable en el nuevo proceso, no
   es necesario llamar a esta función.

   Obsoleto desde la versión 3.7: Esta función es reemplazada por
   "PyOS_AfterFork_Child()".

int PyOS_CheckStack()
    * Part of the Stable ABI on platforms with USE_STACKCHECK since
   version 3.7.*

   Retorna verdadero cuando el intérprete se queda sin espacio de pila
   (*stack space*). Esta es una verificación confiable, pero solo está
   disponible cuando "USE_STACKCHECK" está definido (actualmente en
   algunas versiones de Windows usando el compilador de *Microsoft
   Visual C++*). "USE_STACKCHECK" se definirá automáticamente; nunca
   debe cambiar la definición en su propio código.

typedef void (*PyOS_sighandler_t)(int)
    * Part of the Stable ABI.*

PyOS_sighandler_t PyOS_getsig(int i)
    * Part of the Stable ABI.*

   Retorna el controlador de señal actual para la señal *i*. Esta es
   una pequeña envoltura alrededor de "sigaction()" o "signal()". ¡No
   llame a esas funciones directamente!

PyOS_sighandler_t PyOS_setsig(int i, PyOS_sighandler_t h)
    * Part of the Stable ABI.*

   Configura el controlador de señal para la señal *i* como *h*;
   retorna el antiguo controlador de señal. Esta es una pequeña
   envoltura alrededor de "sigaction()" o "signal()". ¡No llame a esas
   funciones directamente!

int PyOS_InterruptOccurred(void)
    * Part of the Stable ABI.*

   Check if a "SIGINT" signal has been received.

   Returns "1" if a "SIGINT" has occurred and clears the signal flag,
   or "0" otherwise.

   In most cases, you should prefer "PyErr_CheckSignals()" over this
   function. "PyErr_CheckSignals()" invokes the appropriate signal
   handlers for all pending signals, allowing Python code to handle
   the signal properly. This function only detects "SIGINT" and does
   not invoke any Python signal handlers.

   This function is async-signal-safe and this function cannot fail.
   The caller must hold an *attached thread state*.

wchar_t *Py_DecodeLocale(const char *arg, size_t *size)
    * Part of the Stable ABI since version 3.7.*

   Advertencia:

     Esta función no debe llamarse directamente: utilice la API
     "PyConfig" con la función "PyConfig_SetBytesString()" que asegura
     que Python está preinicializado.Esta función no debe llamarse
     antes de que Python esté preinicializado y para que la
     configuración local LC_CTYPE esté correctamente configurada:
     véase la función "Py_PreInitialize()".

   Decodifica una cadena de bytes a partir del *manejador de
   codificación y errores del sistema de archivos*. Si el controlador
   de error es el controlador de error surrogateescape, los bytes no
   codificables se decodifican como caracteres en el rango
   U+DC80..U+DCFF; y si una secuencia de bytes se puede decodificar
   como un carácter sustituto, escape los bytes usando el controlador
   de error surrogateescape en lugar de decodificarlos.

   Retorna un puntero a una cadena de caracteres anchos recientemente
   asignada, use "PyMem_RawFree()" para liberar la memoria. Si el
   tamaño no es "NULL", escribe el número de caracteres anchos
   excluyendo el carácter nulo en "*size"

   Retorna "NULL" en caso de error de decodificación o error de
   asignación de memoria. Si *size* no es "NULL", "*size" se establece
   en "(size_t) -1" en caso de error de memoria o en "(size_t) -2" en
   caso de error de decodificación.

   El *filesystem encoding and error handler* son seleccionados por
   "PyConfig_Read()": ver "filesystem_encoding" y "filesystem_errors"
   que pertenecen a "PyConfig".

   Los errores de decodificación nunca deberían ocurrir, a menos que
   haya un error en la biblioteca C.

   Utilice la función "Py_EncodeLocale()" para codificar la cadena de
   caracteres en una cadena de bytes.

   Ver también:

     Las funciones "PyUnicode_DecodeFSDefaultAndSize()" y
     "PyUnicode_DecodeLocaleAndSize()".

   Added in version 3.5.

   Distinto en la versión 3.7: La función ahora utiliza la
   codificación UTF-8 en el Modo Python UTF-8.

   Distinto en la versión 3.8: La función ahora usa la codificación
   UTF-8 en Windows si "PyPreConfig.legacy_windows_fs_encoding" es
   cero;

char *Py_EncodeLocale(const wchar_t *text, size_t *error_pos)
    * Part of the Stable ABI since version 3.7.*

   Codifica una cadena de caracteres amplios según el término
   *filesystem encoding and error handler*. Si el gestor de errores es
   surrogateescape error handler, los caracteres sustituidos en el
   rango U+DC80..U+DCFF se convierten en bytes 0x80..0xFF.

   Retorna un puntero a una cadena de bytes recién asignada, usa
   "PyMem_Free()" para liberar la memoria. Retorna "NULL" si se genera
   un error de codificación o error de asignación de memoria.

   Si *error_pos* no es "NULL", "*error_pos" se establece en
   "(size_t)-1" en caso de éxito, o se establece en el índice del
   carácter no válido en el error de codificación.

   El *filesystem encoding and error handler* son seleccionados por
   "PyConfig_Read()": ver "filesystem_encoding" y "filesystem_errors"
   que pertenecen a "PyConfig".

   Use la función "Py_DecodeLocale()" para decodificar la cadena de
   bytes en una cadena de caracteres anchos.

   Advertencia:

     Esta función no debe llamarse antes de que Python esté
     preinicializado y para que la configuración local LC_CTYPE esté
     correctamente configurada: véase la función "Py_PreInitialize()".

   Ver también:

     Las funciones "PyUnicode_EncodeFSDefault()" y
     "PyUnicode_EncodeLocale()".

   Added in version 3.5.

   Distinto en la versión 3.7: La función ahora utiliza la
   codificación UTF-8 en el Modo Python UTF-8.

   Distinto en la versión 3.8: La función ahora usa la codificación
   UTF-8 en Windows si "PyPreConfig.legacy_windows_fs_encoding" es
   cero.

FILE *Py_fopen(PyObject *path, const char *mode)

   Similar a "fopen()", pero *path* es un objeto Python y se establece
   una excepción en caso de error.

   *path* debe ser un objeto "str", un objeto "bytes" o un *path-like
   object*.

   En caso de éxito, devuelve el nuevo puntero de archivo. En caso de
   error, se establece una excepción y se devuelve "NULL".

   El archivo debe cerrarse mediante "Py_fclose()" en lugar de llamar
   directamente a "fclose()".

   El descriptor de archivo se crea no heredable (**PEP 446**).

   Quien llama debe tener un *attached thread state*.

   Added in version 3.14.

int Py_fclose(FILE *file)

   Cerrar un archivo abierto mediante "Py_fopen()".

   En caso de éxito, devuelve "0". En caso de error, devuelve "EOF" y
   se establece "errno" para indicar el error. En cualquiera de los
   casos, cualquier acceso posterior (incluida otra llamada a
   "Py_fclose()") al flujo produce un comportamiento indefinido.

   Added in version 3.14.

# Funciones del Sistema

Estas son funciones de utilidad que hacen que la funcionalidad del
módulo "sys" sea accesible para el código C. Todos funcionan con el
diccionario del módulo "sys" del subproceso actual del intérprete, que
está contenido en la estructura interna del estado del subproceso.

PyObject *PySys_GetObject(const char *name)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna el objeto *name* del módulo "sys" o "NULL" si no existe,
   sin establecer una excepción.

int PySys_SetObject(const char *name, PyObject *v)
    * Part of the Stable ABI.*

   Establece *name* en el módulo "sys" en *v* a menos que *v* sea
   "NULL", en cuyo caso *name* se elimina del módulo *sys*. Retorna
   "0" en caso de éxito, "-1" en caso de error.

void PySys_ResetWarnOptions()
    * Part of the Stable ABI.*

   Restablece "sys.warnoptions" a una lista vacía. Esta función puede
   llamarse antes de "Py_Initialize()".

   Deprecated since version 3.13, will be removed in version 3.15: En
   su lugar, borra "sys.warnoptions" y "warnings.filters".

void PySys_WriteStdout(const char *format, ...)
    * Part of the Stable ABI.*

   Escribe la cadena de caracteres de salida descrita por *format* en
   "sys.stdout". No se lanzan excepciones, incluso si se produce el
   truncamiento (ver más abajo).

   *format* debe limitar el tamaño total de la cadena de caracteres de
   salida formateada a 1000 bytes o menos; después de 1000 bytes, la
   cadena de caracteres de salida se trunca. En particular, esto
   significa que no deben existir formatos "%s" sin restricciones;
   estos deben limitarse usando "%.<N>s" donde <N> es un número
   decimal calculado de modo que <N> más el tamaño máximo de otro
   texto formateado no exceda los 1000 bytes. También tenga cuidado
   con "%f", que puede imprimir cientos de dígitos para números muy
   grandes.

   Si ocurre un problema, o "sys.stdout" no está configurado, el
   mensaje formateado se escribe en el real (nivel C) *stdout*.

void PySys_WriteStderr(const char *format, ...)
    * Part of the Stable ABI.*

   Como "PySys_WriteStdout()", pero escribe a "sys.stderr" o *stderr*
   en su lugar.

void PySys_FormatStdout(const char *format, ...)
    * Part of the Stable ABI.*

   Función similar a "PySys_WriteStdout()" pero formatea el mensaje
   usando "PyUnicode_FromFormatV()" y no trunca el mensaje a una
   longitud arbitraria.

   Added in version 3.2.

void PySys_FormatStderr(const char *format, ...)
    * Part of the Stable ABI.*

   Como "PySys_FormatStdout()", pero escribe a "sys.stderr" o *stderr*
   en su lugar.

   Added in version 3.2.

PyObject *PySys_GetXOptions()
    *Return value: Borrowed reference.** Part of the Stable ABI since
   version 3.7.*

   Retorna el diccionario actual de opciones "-X", de manera similar a
   "sys._xoptions". En caso de error, se retorna "NULL" y se establece
   una excepción.

   Added in version 3.2.

int PySys_Audit(const char *event, const char *format, ...)
    * Part of the Stable ABI since version 3.13.*

   Lanza un evento de auditoría con cualquier gancho activo. Retorna
   cero para el éxito y no cero con una excepción establecida en caso
   de error.

   El argumento de cadena *event* no debe ser *NULL*.

   Si se han agregado ganchos, *format* y otros argumentos se
   utilizarán para construir una tupla para pasar. Además de "N",
   están disponibles los mismos caracteres de formato que los
   utilizados en "Py_BuildValue()". Si el valor generado no es una
   tupla, se agregará a una tupla de un solo elemento.

   La opción de formato "N" no debe usarse. Consume una referencia,
   pero dado que no hay forma de saber si los argumentos de esta
   función serán consumidos, usarla puede causar fugas de referencia.

   Tenga en cuenta que los caracteres de formato "#" deben tratarse
   como "Py_ssize_t", independientemente de si se definió
   "PY_SSIZE_T_CLEAN".

   "sys.audit()" realiza la misma función del código Python.

   Ver también "PySys_AuditTuple()".

   Added in version 3.8.

   Distinto en la versión 3.8.2: Requiere "Py_ssize_t" para los
   caracteres de formato "#". Anteriormente, se lanzaba una
   advertencia de deprecación inevitable.

int PySys_AuditTuple(const char *event, PyObject *args)
    * Part of the Stable ABI since version 3.13.*

   Similar a "PySys_Audit()", pero pasa argumentos como un objeto
   Python. *args* debe ser una "tuple". Para no pasar argumentos,
   *args* puede ser *NULL*.

   Added in version 3.13.

int PySys_AddAuditHook(Py_AuditHookFunction hook, void *userData)

   Agrega el *hook* invocable a la lista de hooks de auditoría
   activos. Retorna cero para el éxito y no cero en caso de error. Si
   el tiempo de ejecución se ha inicializado, también configura un
   error en caso de fallo. Los hooks agregados a través de esta API se
   llaman para todos los intérpretes creados por el tiempo de
   ejecución.

   El puntero *userData* se pasa a la función gancho. Dado que las
   funciones de enlace pueden llamarse desde diferentes tiempos de
   ejecución, este puntero no debe referirse directamente al estado de
   Python.

   Es seguro llamar a esta función antes de "Py_Initialize()". Cuando
   se llama después de la inicialización del tiempo de ejecución, se
   notifican los enlaces de auditoría existentes y pueden anular
   silenciosamente la operación al generar un error subclasificado de
   "Exception" (otros errores no se silenciarán).

   La función hook siempre se invoca con un *attached thread state*
   por el intérprete de Python que lanzó el evento.

   Ver **PEP 578** para una descripción detallada de la auditoría. Las
   funciones en el tiempo de ejecución y la biblioteca estándar que
   generan eventos se enumeran en table de eventos de auditoria. Los
   detalles se encuentran en la documentación de cada función.

   Si el intérprete se inicializa, esta función lanza un evento de
   auditoría "sys.addaudithook" sin argumentos. Si algún gancho
   existente lanza una excepción derivada de "Exception", el nuevo
   gancho no se agregará y la excepción se borrará. Como resultado,
   las personas que llaman no pueden asumir que su gancho ha sido
   agregado a menos que controlen todos los ganchos existentes.

   typedef int (*Py_AuditHookFunction)(const char *event, PyObject *args, void *userData)

      El tipo de la función gancho. *event* es el argumento de cadena
      C de evento pasado a "PySys_Audit()" o "PySys_AuditTuple()". Se
      garantiza que *args* es un "PyTupleObject". *userData* es el
      argumento pasado a PySys_AddAuditHook().

   Added in version 3.8.

# Control de procesos

void Py_FatalError(const char *message)
    * Part of the Stable ABI.*

   Imprime un mensaje de error fatal y elimina el proceso. No se
   realiza limpieza. Esta función solo debe invocarse cuando se
   detecta una condición que haría peligroso continuar usando el
   intérprete de Python; por ejemplo, cuando la administración del
   objeto parece estar dañada. En Unix, se llama a la función de
   biblioteca C estándar "abort()" que intentará producir un archivo
   "core".

   La función "Py_FatalError()" se reemplaza con una macro que
   registra automáticamente el nombre de la función actual, a menos
   que se defina la macro "Py_LIMITED_API".

   Distinto en la versión 3.9: Registra el nombre de la función
   automáticamente.

void Py_Exit(int status)
    * Part of the Stable ABI.*

   Sale del proceso actual. Esto llama "Py_FinalizeEx()" y luego llama
   a la función estándar de la biblioteca C "exit(status)". Si
   "Py_FinalizeEx()" indica un error, el estado de salida se establece
   en 120.

   Distinto en la versión 3.6: Los errores de finalización ya no se
   ignoran.

int Py_AtExit(void (*func)())
    * Part of the Stable ABI.*

   Registra una función de limpieza a la que llamará
   "Py_FinalizeEx()". Se llamará a la función de limpieza sin
   argumentos y no debería retornar ningún valor. Como máximo se
   pueden registrar 32 funciones de limpieza. Cuando el registro es
   exitoso, "Py_AtExit()" retorna "0"; en caso de error, retorna "-1".
   La última función de limpieza registrada se llama primero. Cada
   función de limpieza se llamará como máximo una vez. Dado que la
   finalización interna de Python se habrá completado antes de la
   función de limpieza, *func* no debería llamar a las API de Python.

   Ver también:

     "PyUnstable_AtExit()" para pasar un argumento "void *data".
