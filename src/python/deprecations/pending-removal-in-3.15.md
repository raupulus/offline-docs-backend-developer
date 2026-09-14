---
title: Pending removal in Python 3.15
source_url: https://docs.python.org/es/3
source_path: deprecations/pending-removal-in-3.15.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 900
---

# Pending removal in Python 3.15

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

  * La función indocumentada "ctypes.SetPointerType()" ha quedado
    obsoleta desde Python 3.13.

* "http.server":

  * La clase obsoleta y raramente usada "CGIHTTPRequestHandler" ha
    quedado obsoleta desde Python 3.13. No existe un reemplazo
    directo. *Cualquier cosa* es mejor que CGI para interconectar un
    servidor web con un controlador de solicitudes.

  * El indicador "--cgi" a la interfaz de línea de comandos **python
    -m http.server** ha quedado obsoleto desde Python 3.13.

* "importlib":

  * "load_module()" method: use "exec_module()" instead.

* "pathlib":

  * "PurePath.is_reserved()" ha quedado obsoleto desde Python 3.13.
    Utilice "os.path.isreserved()" para detectar rutas reservadas en
    Windows.

* "platform":

  * "java_ver()" ha quedado obsoleta desde Python 3.13. Esta función
    es útil solo para la compatibilidad con Jython, tiene una API
    confusa y, en gran parte, falta pruebas.

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

  * Los métodos "getmark()", "setmark()", y "getmarkers()" de las
    clases "Wave_read" y "Wave_write" han quedado obsoletos desde
    Python 3.13.

* "zipimport":

  * "load_module()" has been deprecated since Python 3.10. Use
    "exec_module()" instead. (Contributed by Jiahao Li in gh-125746.)
