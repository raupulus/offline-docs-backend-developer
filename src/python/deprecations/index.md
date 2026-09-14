---
title: Desusos
source_url: https://docs.python.org/es/3
source_path: deprecations/index.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 870
---

# Desusos

## Pending removal in Python 3.15

* The import system:

  * Setting "__cached__" on a module while failing to set
    "__spec__.cached" is deprecated. In Python 3.15, "__cached__" will
    cease to be set or take into consideration by the import system or
    standard library. (gh-97879)

  * Setting "__package__" on a module while failing to set
    "__spec__.parent" is deprecated. In Python 3.15, "__package__"
    will cease to be set or take into consideration by the import
    system or standard library. (gh-97879)

* "ctypes":

  * La función "ctypes.SetPointerType()" no documentada ha quedado
    obsoleta desde Python 3.13.

* "http.server":

  * El obsoleto y poco utilizado "CGIHTTPRequestHandler" ha quedado
    obsoleto desde Python 3.13. No existe un reemplazo directo.
    *Anything* es mejor que CGI para interconectar un servidor web con
    un controlador de solicitudes.

  * La bandera "--cgi" de la interfaz de línea de comandos **python -m
    http.server** ha quedado obsoleta desde Python 3.13.

* "importlib":

  * Método "load_module()": utilice "exec_module()" en su lugar.

* "pathlib":

  * "PurePath.is_reserved()" ha quedado obsoleto desde Python 3.13.
    Utilice "os.path.isreserved()" para detectar rutas reservadas en
    Windows.

* "platform":

  * "java_ver()" ha quedado obsoleto desde Python 3.13. Esta función
    solo es útil para la compatibilidad con Jython, tiene una API
    confusa y, en gran medida, no se ha probado.

* "sysconfig":

  * The *check_home* argument of "sysconfig.is_python_build()" has
    been deprecated since Python 3.12.

* "threading":

  * "RLock()" will take no arguments in Python 3.15. Passing any
    arguments has been deprecated since Python 3.14, as the Python
    version does not permit any arguments, but the C version allows
    any number of positional or keyword arguments, ignoring every
    argument.

* "types":

  * "types.CodeType": Accessing "co_lnotab" was deprecated in **PEP
    626** since 3.10 and was planned to be removed in 3.12, but it
    only got a proper "DeprecationWarning" in 3.12. May be removed in
    3.15. (Contributed by Nikita Sobolev in gh-101866.)

* "typing":

  * The undocumented keyword argument syntax for creating "NamedTuple"
    classes (for example, "Point = NamedTuple("Point", x=int, y=int)")
    has been deprecated since Python 3.13. Use the class-based syntax
    or the functional syntax instead.

  * When using the functional syntax of "TypedDict"s, failing to pass
    a value to the *fields* parameter ("TD = TypedDict("TD")") or
    passing "None" ("TD = TypedDict("TD", None)") has been deprecated
    since Python 3.13. Use "class TD(TypedDict): pass" or "TD =
    TypedDict("TD", {})" to create a TypedDict with zero field.

  * The "@typing.no_type_check_decorator" decorator function has been
    deprecated since Python 3.13. After eight years in the "typing"
    module, it has yet to be supported by any major type checker.

* "wave":

  * Los métodos "getmark()", "setmark()" y "getmarkers()" de las
    clases "Wave_read" y "Wave_write" han quedado obsoletos desde
    Python 3.13.

* "zipimport":

  * "load_module()" has been deprecated since Python 3.10. Use
    "exec_module()" instead. (Contributed by Jiahao Li in gh-125746.)

## Pending removal in Python 3.16

* The import system:

  * Setting "__loader__" on a module while failing to set
    "__spec__.loader" is deprecated. In Python 3.16, "__loader__" will
    cease to be set or taken into consideration by the import system
    or the standard library.

* "array":

  * El código de formato "'u'" ("wchar_t") ha quedado obsoleto en la
    documentación desde Python 3.3 y en el entorno de ejecución desde
    Python 3.13. Utilice el código de formato "'w'" ("Py_UCS4") para
    caracteres Unicode.

* "asyncio":

  * "asyncio.iscoroutinefunction()" is deprecated and will be removed
    in Python 3.16; use "inspect.iscoroutinefunction()" instead.
    (Contributed by Jiahao Li and Kumar Aditya in gh-122875.)

  * "asyncio" policy system is deprecated and will be removed in
    Python 3.16. In particular, the following classes and functions
    are deprecated:

    * "asyncio.AbstractEventLoopPolicy"

    * "asyncio.DefaultEventLoopPolicy"

    * "asyncio.WindowsSelectorEventLoopPolicy"

    * "asyncio.WindowsProactorEventLoopPolicy"

    * "asyncio.get_event_loop_policy()"

    * "asyncio.set_event_loop_policy()"

    Users should use "asyncio.run()" or "asyncio.Runner" with
    *loop_factory* to use the desired event loop implementation.

    For example, to use "asyncio.SelectorEventLoop" on Windows:

       import asyncio

       async def main():
           ...

       asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

    (Contributed by Kumar Aditya in gh-127949.)

* "builtins":

  * La inversión bit a bit en tipos booleanos, "~True" o "~False", ha
    quedado obsoleta desde Python 3.12, ya que produce resultados
    sorprendentes y poco intuitivos ("-2" y "-1"). En su lugar,
    utilice "not x" para la negación lógica de un valor booleano. En
    el caso poco frecuente de que necesite la inversión bit a bit del
    entero subyacente, convierta a "int" explícitamente ("~int(x)").

* "functools":

  * Calling the Python implementation of "functools.reduce()" with
    *function* or *sequence* as keyword arguments has been deprecated
    since Python 3.14.

* "logging":

  Support for custom logging handlers with the *strm* argument is
  deprecated and scheduled for removal in Python 3.16. Define handlers
  with the *stream* argument instead. (Contributed by Mariusz Felisiak
  in gh-115032.)

* "mimetypes":

  * Valid extensions start with a '.' or are empty for
    "mimetypes.MimeTypes.add_type()". Undotted extensions are
    deprecated and will raise a "ValueError" in Python 3.16.
    (Contributed by Hugo van Kemenade in gh-75223.)

* "shutil":

  * La excepción "ExecError" ha quedado obsoleta desde Python 3.14. No
    ha sido utilizada por ninguna función en "shutil" desde Python 3.4
    y ahora es un alias de "RuntimeError".

* "symtable":

  * El método "Class.get_methods" ha quedado obsoleto desde Python
    3.14.

* "sys":

  * La función "_enablelegacywindowsfsencoding()" ha quedado obsoleta
    desde Python 3.13. En su lugar, utilice la variable de entorno
    "PYTHONLEGACYWINDOWSFSENCODING".

* "sysconfig":

  * The "sysconfig.expand_makefile_vars()" function has been
    deprecated since Python 3.14. Use the "vars" argument of
    "sysconfig.get_paths()" instead.

* "tarfile":

  * El atributo "TarFile.tarfile", no documentado ni utilizado, ha
    quedado obsoleto desde Python 3.13.

## Pending removal in Python 3.17

* "collections.abc":

  * "collections.abc.ByteString" is scheduled for removal in Python
    3.17.

    Use "isinstance(obj, collections.abc.Buffer)" to test if "obj"
    implements the buffer protocol at runtime. For use in type
    annotations, either use "Buffer" or a union that explicitly
    specifies the types your code supports (e.g., "bytes | bytearray |
    memoryview").

    "ByteString" was originally intended to be an abstract class that
    would serve as a supertype of both "bytes" and "bytearray".
    However, since the ABC never had any methods, knowing that an
    object was an instance of "ByteString" never actually told you
    anything useful about the object. Other common buffer types such
    as "memoryview" were also never understood as subtypes of
    "ByteString" (either at runtime or by static type checkers).

    See **PEP 688** for more details. (Contributed by Shantanu Jain in
    gh-91896.)

* "typing":

  * Before Python 3.14, old-style unions were implemented using the
    private class "typing._UnionGenericAlias". This class is no longer
    needed for the implementation, but it has been retained for
    backward compatibility, with removal scheduled for Python 3.17.
    Users should use documented introspection helpers like
    "typing.get_origin()" and "typing.get_args()" instead of relying
    on private implementation details.

  * "typing.ByteString", deprecated since Python 3.9, is scheduled for
    removal in Python 3.17.

    Use "isinstance(obj, collections.abc.Buffer)" to test if "obj"
    implements the buffer protocol at runtime. For use in type
    annotations, either use "Buffer" or a union that explicitly
    specifies the types your code supports (e.g., "bytes | bytearray |
    memoryview").

    "ByteString" was originally intended to be an abstract class that
    would serve as a supertype of both "bytes" and "bytearray".
    However, since the ABC never had any methods, knowing that an
    object was an instance of "ByteString" never actually told you
    anything useful about the object. Other common buffer types such
    as "memoryview" were also never understood as subtypes of
    "ByteString" (either at runtime or by static type checkers).

    See **PEP 688** for more details. (Contributed by Shantanu Jain in
    gh-91896.)

## Pending removal in Python 3.18

* "decimal":

  * The non-standard and undocumented "Decimal" format specifier
    "'N'", which is only supported in the "decimal" module's C
    implementation, has been deprecated since Python 3.13.
    (Contributed by Serhiy Storchaka in gh-89902.)

## Pending removal in Python 3.19

* "ctypes":

  * Implicitly switching to the MSVC-compatible struct layout by
    setting "_pack_" but not "_layout_" on non-Windows platforms.

## Pending removal in future versions

Las siguientes API se eliminarán en el futuro, aunque actualmente no
hay una fecha programada para su eliminación.

* "argparse":

  * Nesting argument groups and nesting mutually exclusive groups are
    deprecated.

  * Passing the undocumented keyword argument *prefix_chars* to
    "add_argument_group()" is now deprecated.

  * The "argparse.FileType" type converter is deprecated.

* "builtins":

  * Generadores: las firmas "throw(type, exc, tb)" y "athrow(type,
    exc, tb)" están obsoletas: utilice "throw(exc)" y "athrow(exc)" en
    su lugar, la firma de argumento único.

  * Actualmente, Python acepta literales numéricos seguidos
    inmediatamente de palabras clave, por ejemplo, "0in x", "1or x",
    "0if 1else 2". Permite expresiones confusas y ambiguas como
    "[0x1for x in y]" (que se puede interpretar como "[0x1 for x in
    y]" o "[0x1f or x in y]"). Se genera una advertencia de sintaxis
    si el literal numérico va seguido inmediatamente de una de las
    palabras clave "and", "else", "for", "if", "in", "is" y "or". En
    una versión futura, se cambiará a un error de sintaxis. (gh-87999)

  * Compatibilidad con los métodos "__index__()" y "__int__()" que
    devuelven un tipo que no es int: estos métodos serán necesarios
    para devolver una instancia de una subclase estricta de "int".

  * Compatibilidad con el método "__float__()" que devuelve una
    subclase estricta de "float": estos métodos serán necesarios para
    devolver una instancia de "float".

  * Compatibilidad con el método "__complex__()" que devuelve una
    subclase estricta de "complex": estos métodos serán necesarios
    para devolver una instancia de "complex".

  * Ahora está obsoleto el paso de un número complejo como argumento
    *real* o *imag* en el constructor "complex()"; solo debe pasarse
    como un único argumento posicional. (Contribuido por Serhiy
    Storchaka en gh-109218.)

* "calendar": Las constantes "calendar.January" y "calendar.February"
  han quedado obsoletas y han sido reemplazadas por "calendar.JANUARY"
  y "calendar.FEBRUARY". (Contribuido por Prince Roshan en gh-103636.)

* "codecs": use "open()" instead of "codecs.open()". (gh-133038)

* "codeobject.co_lnotab": utilice el método "codeobject.co_lines()" en
  su lugar.

* "datetime":

  * "utcnow()": utilice "datetime.datetime.now(tz=datetime.UTC)".

  * "utcfromtimestamp()": utilice
    "datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)".

* "gettext": El valor plural debe ser un número entero.

* "importlib":

  * "cache_from_source()" El parámetro *debug_override* está obsoleto:
    utilice el parámetro *optimization* en su lugar.

* "importlib.metadata":

  * Interfaz de tupla "EntryPoints".

  * "None" implícito en los valores de retorno.

* "logging": el método "warn()" ha quedado obsoleto desde Python 3.3,
  utilice "warning()" en su lugar.

* "mailbox": El uso del modo de entrada y texto StringIO está
  obsoleto; en su lugar, utilice BytesIO y el modo binario.

* "os": Llamada a "os.register_at_fork()" en un proceso multiproceso.

* "pydoc.ErrorDuringImport": Un valor de tupla para el parámetro
  *exc_info* está obsoleto, utilice una instancia de excepción.

* "re": Ahora se aplican reglas más estrictas para las referencias
  numéricas de grupos y los nombres de grupos en expresiones
  regulares. Ahora solo se aceptan secuencias de dígitos ASCII como
  referencia numérica. El nombre de grupo en patrones de bytes y
  cadenas de reemplazo ahora solo puede contener letras y dígitos
  ASCII y guiones bajos. (Contribuido por Serhiy Storchaka en
  gh-91760.)

* Módulos "sre_compile", "sre_constants" y "sre_parse".

* "shutil": El parámetro *onerror* de "rmtree()" está obsoleto en
  Python 3.12; utilice el parámetro *onexc* en su lugar.

* Opciones y protocolos "ssl":

  * "ssl.SSLContext" sin argumento de protocolo está obsoleto.

  * "ssl.SSLContext": "set_npn_protocols()" y
    "selected_npn_protocol()" están obsoletos: utilice ALPN en su
    lugar.

  * Opciones de "ssl.OP_NO_SSL*"

  * Opciones de "ssl.OP_NO_TLS*"

  * "ssl.PROTOCOL_SSLv3"

  * "ssl.PROTOCOL_TLS"

  * "ssl.PROTOCOL_TLSv1"

  * "ssl.PROTOCOL_TLSv1_1"

  * "ssl.PROTOCOL_TLSv1_2"

  * "ssl.TLSVersion.SSLv3"

  * "ssl.TLSVersion.TLSv1"

  * "ssl.TLSVersion.TLSv1_1"

* Métodos "threading":

  * "threading.Condition.notifyAll()": utilice "notify_all()".

  * "threading.Event.isSet()": utilice "is_set()".

  * "threading.Thread.isDaemon()", "threading.Thread.setDaemon()":
    utilice el atributo "threading.Thread.daemon".

  * "threading.Thread.getName()", "threading.Thread.setName()":
    utilice el atributo "threading.Thread.name".

  * "threading.currentThread()": utilice "threading.current_thread()".

  * "threading.activeCount()": utilice "threading.active_count()".

* "typing.Text" (gh-92332).

* The internal class "typing._UnionGenericAlias" is no longer used to
  implement "typing.Union". To preserve compatibility with users using
  this private class, a compatibility shim will be provided until at
  least Python 3.17. (Contributed by Jelle Zijlstra in gh-105499.)

* "unittest.IsolatedAsyncioTestCase": está obsoleto devolver un valor
  que no sea "None" de un caso de prueba.

* Funciones obsoletas de "urllib.parse": "urlparse()" en su lugar

  * "splitattr()"

  * "splithost()"

  * "splitnport()"

  * "splitpasswd()"

  * "splitport()"

  * "splitquery()"

  * "splittag()"

  * "splittype()"

  * "splituser()"

  * "splitvalue()"

  * "to_bytes()"

* "wsgiref": "SimpleHandler.stdout.write()" no debería realizar
  escrituras parciales.

* "xml.etree.ElementTree": La prueba del valor de verdad de un
  "Element" está obsoleta. En una versión futura, siempre devolverá
  "True". En su lugar, es preferible realizar pruebas explícitas
  "len(elem)" o "elem is not None".

* "sys._clear_type_cache()" is deprecated: use
  "sys._clear_internal_caches()" instead.

## C API deprecations

### Pending removal in Python 3.15

* "PyImport_ImportModuleNoBlock()": utilice "PyImport_ImportModule()"
  en su lugar.

* "PyWeakref_GetObject()" and "PyWeakref_GET_OBJECT()": Use
  "PyWeakref_GetRef()" instead. The pythoncapi-compat project can be
  used to get "PyWeakref_GetRef()" on Python 3.12 and older.

* Tipo "Py_UNICODE" y macro "Py_UNICODE_WIDE": utilice "wchar_t" en su
  lugar.

* "PyUnicode_AsDecodedObject()": Utilice "PyCodec_Decode()" en su
  lugar.

* "PyUnicode_AsDecodedUnicode()": Use "PyCodec_Decode()" instead; Note
  that some codecs (for example, "base64") may return a type other
  than "str", such as "bytes".

* "PyUnicode_AsEncodedObject()": Utilice "PyCodec_Encode()" en su
  lugar.

* "PyUnicode_AsEncodedUnicode()": Use "PyCodec_Encode()" instead; Note
  that some codecs (for example, "base64") may return a type other
  than "bytes", such as "str".

* Python initialization functions, deprecated in Python 3.13:

  * "Py_GetPath()": Use "PyConfig_Get("module_search_paths")"
    ("sys.path") instead.

  * "Py_GetPrefix()": Use "PyConfig_Get("base_prefix")"
    ("sys.base_prefix") instead. Use "PyConfig_Get("prefix")"
    ("sys.prefix") if virtual environments need to be handled.

  * "Py_GetExecPrefix()": Use "PyConfig_Get("base_exec_prefix")"
    ("sys.base_exec_prefix") instead. Use
    "PyConfig_Get("exec_prefix")" ("sys.exec_prefix") if virtual
    environments need to be handled.

  * "Py_GetProgramFullPath()": Use "PyConfig_Get("executable")"
    ("sys.executable") instead.

  * "Py_GetProgramName()": Use "PyConfig_Get("executable")"
    ("sys.executable") instead.

  * "Py_GetPythonHome()": Use "PyConfig_Get("home")" or the
    "PYTHONHOME" environment variable instead.

  The pythoncapi-compat project can be used to get "PyConfig_Get()" on
  Python 3.13 and older.

* Funciones para configurar la inicialización de Python, obsoletas en
  Python 3.11:

  * "PySys_SetArgvEx()": Establezca "PyConfig.argv" en su lugar.

  * "PySys_SetArgv()": Establezca "PyConfig.argv" en su lugar.

  * "Py_SetProgramName()": Establezca "PyConfig.program_name" en su
    lugar.

  * "Py_SetPythonHome()": Establezca "PyConfig.home" en su lugar.

  * "PySys_ResetWarnOptions()": borre "sys.warnoptions" y
    "warnings.filters" en su lugar.

  La API "Py_InitializeFromConfig()" debe utilizarse con "PyConfig".

* Variables de configuración global:

  * "Py_DebugFlag": Use "PyConfig.parser_debug" or
    "PyConfig_Get("parser_debug")" instead.

  * "Py_VerboseFlag": Use "PyConfig.verbose" or
    "PyConfig_Get("verbose")" instead.

  * "Py_QuietFlag": Use "PyConfig.quiet" or "PyConfig_Get("quiet")"
    instead.

  * "Py_InteractiveFlag": Use "PyConfig.interactive" or
    "PyConfig_Get("interactive")" instead.

  * "Py_InspectFlag": Use "PyConfig.inspect" or
    "PyConfig_Get("inspect")" instead.

  * "Py_OptimizeFlag": Use "PyConfig.optimization_level" or
    "PyConfig_Get("optimization_level")" instead.

  * "Py_NoSiteFlag": Use "PyConfig.site_import" or
    "PyConfig_Get("site_import")" instead.

  * "Py_BytesWarningFlag": Use "PyConfig.bytes_warning" or
    "PyConfig_Get("bytes_warning")" instead.

  * "Py_FrozenFlag": Use "PyConfig.pathconfig_warnings" or
    "PyConfig_Get("pathconfig_warnings")" instead.

  * "Py_IgnoreEnvironmentFlag": Use "PyConfig.use_environment" or
    "PyConfig_Get("use_environment")" instead.

  * "Py_DontWriteBytecodeFlag": Use "PyConfig.write_bytecode" or
    "PyConfig_Get("write_bytecode")" instead.

  * "Py_NoUserSiteDirectory": Use "PyConfig.user_site_directory" or
    "PyConfig_Get("user_site_directory")" instead.

  * "Py_UnbufferedStdioFlag": Use "PyConfig.buffered_stdio" or
    "PyConfig_Get("buffered_stdio")" instead.

  * "Py_HashRandomizationFlag": Use "PyConfig.use_hash_seed" and
    "PyConfig.hash_seed" or "PyConfig_Get("hash_seed")" instead.

  * "Py_IsolatedFlag": Use "PyConfig.isolated" or
    "PyConfig_Get("isolated")" instead.

  * "Py_LegacyWindowsFSEncodingFlag": Use
    "PyPreConfig.legacy_windows_fs_encoding" or
    "PyConfig_Get("legacy_windows_fs_encoding")" instead.

  * "Py_LegacyWindowsStdioFlag": Use "PyConfig.legacy_windows_stdio"
    or "PyConfig_Get("legacy_windows_stdio")" instead.

  * "Py_FileSystemDefaultEncoding", "Py_HasFileSystemDefaultEncoding":
    Use "PyConfig.filesystem_encoding" or
    "PyConfig_Get("filesystem_encoding")" instead.

  * "Py_FileSystemDefaultEncodeErrors": Use
    "PyConfig.filesystem_errors" or
    "PyConfig_Get("filesystem_errors")" instead.

  * "Py_UTF8Mode": Use "PyPreConfig.utf8_mode" or
    "PyConfig_Get("utf8_mode")" instead. (see "Py_PreInitialize()")

  The "Py_InitializeFromConfig()" API should be used with "PyConfig"
  to set these options. Or "PyConfig_Get()" can be used to get these
  options at runtime.

### Pending removal in Python 3.18

* The following private functions are deprecated and planned for
  removal in Python 3.18:

  * "_PyBytes_Join()": use "PyBytes_Join()".

  * "_PyDict_GetItemStringWithError()": use
    "PyDict_GetItemStringRef()".

  * "_PyDict_Pop()": use "PyDict_Pop()".

  * "_PyLong_Sign()": use "PyLong_GetSign()".

  * "_PyLong_FromDigits()" and "_PyLong_New()": use
    "PyLongWriter_Create()".

  * "_PyThreadState_UncheckedGet()": use
    "PyThreadState_GetUnchecked()".

  * "_PyUnicode_AsString()": use "PyUnicode_AsUTF8()".

  * "_PyUnicodeWriter_Init()": replace
    "_PyUnicodeWriter_Init(&writer)" with "writer =
    PyUnicodeWriter_Create(0)".

  * "_PyUnicodeWriter_Finish()": replace
    "_PyUnicodeWriter_Finish(&writer)" with
    "PyUnicodeWriter_Finish(writer)".

  * "_PyUnicodeWriter_Dealloc()": replace
    "_PyUnicodeWriter_Dealloc(&writer)" with
    "PyUnicodeWriter_Discard(writer)".

  * "_PyUnicodeWriter_WriteChar()": replace
    "_PyUnicodeWriter_WriteChar(&writer, ch)" with
    "PyUnicodeWriter_WriteChar(writer, ch)".

  * "_PyUnicodeWriter_WriteStr()": replace
    "_PyUnicodeWriter_WriteStr(&writer, str)" with
    "PyUnicodeWriter_WriteStr(writer, str)".

  * "_PyUnicodeWriter_WriteSubstring()": replace
    "_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)" with
    "PyUnicodeWriter_WriteSubstring(writer, str, start, end)".

  * "_PyUnicodeWriter_WriteASCIIString()": replace
    "_PyUnicodeWriter_WriteASCIIString(&writer, str)" with
    "PyUnicodeWriter_WriteASCII(writer, str)".

  * "_PyUnicodeWriter_WriteLatin1String()": replace
    "_PyUnicodeWriter_WriteLatin1String(&writer, str)" with
    "PyUnicodeWriter_WriteUTF8(writer, str)".

  * "_PyUnicodeWriter_Prepare()": (no replacement).

  * "_PyUnicodeWriter_PrepareKind()": (no replacement).

  * "_Py_HashPointer()": use "Py_HashPointer()".

  * "_Py_fopen_obj()": use "Py_fopen()".

  The pythoncapi-compat project can be used to get these new public
  functions on Python 3.13 and older. (Contributed by Victor Stinner
  in gh-128863.)

### Pending removal in future versions

Las siguientes API están obsoletas y se eliminarán, aunque actualmente
no hay una fecha programada para su eliminación.

* "Py_TPFLAGS_HAVE_FINALIZE": Innecesario desde Python 3.8.

* "PyErr_Fetch()": Utilice "PyErr_GetRaisedException()" en su lugar.

* "PyErr_NormalizeException()": Utilice "PyErr_GetRaisedException()"
  en su lugar.

* "PyErr_Restore()": Utilice "PyErr_SetRaisedException()" en su lugar.

* "PyModule_GetFilename()": Utilice "PyModule_GetFilenameObject()" en
  su lugar.

* "PyOS_AfterFork()": Utilice "PyOS_AfterFork_Child()" en su lugar.

* "PySlice_GetIndicesEx()": Utilice "PySlice_Unpack()" y
  "PySlice_AdjustIndices()" en su lugar.

* "PyUnicode_READY()": Innecesario desde Python 3.12

* "PyErr_Display()": Utilice "PyErr_DisplayException()" en su lugar.

* "_PyErr_ChainExceptions()": Utilice "_PyErr_ChainExceptions1()" en
  su lugar.

* Miembro de "PyBytesObject.ob_shash": llame a "PyObject_Hash()" en su
  lugar.

* API de almacenamiento local de subprocesos (TLS):

  * "PyThread_create_key()": Utilice "PyThread_tss_alloc()" en su
    lugar.

  * "PyThread_delete_key()": Utilice "PyThread_tss_free()" en su
    lugar.

  * "PyThread_set_key_value()": Utilice "PyThread_tss_set()" en su
    lugar.

  * "PyThread_get_key_value()": Utilice "PyThread_tss_get()" en su
    lugar.

  * "PyThread_delete_key_value()": Utilice "PyThread_tss_delete()" en
    su lugar.

  * "PyThread_ReInitTLS()": Innecesario desde Python 3.7.
