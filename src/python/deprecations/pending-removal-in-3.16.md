---
title: Pending removal in Python 3.16
source_url: https://docs.python.org/es/3
source_path: deprecations/pending-removal-in-3.16.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 910
---

# Pending removal in Python 3.16

* The import system:

  * Setting "__loader__" on a module while failing to set
    "__spec__.loader" is deprecated. In Python 3.16, "__loader__" will
    cease to be set or taken into consideration by the import system
    or the standard library.

* "array":

  * El código de formato "'u'" ("wchar_t") ha quedado obsoleto en la
    documentación desde Python 3.3 y en tiempo de ejecución desde
    Python 3.13. En su lugar, se utiliza el código de formato "'w'"
    ("Py_UCS4") para caracteres Unicode.

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

  * La inversión bit a bit en tipos booleanos, "~True" o "~False" ha
    quedado obsoleta desde Python 3.12, ya que produce resultados
    sorprendentes y poco intuitivos ("-2" y "-1"). En su lugar, se
    utiliza "not x" para la negación lógica de un booleano. En el caso
    poco frecuente de que se necesite la inversión bit a bit del
    entero subyacente, convertir a "int" explícitamente ("~int(x)").

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
    se ha utilizado por ninguna función en "shutil" desde Python 3.4,
    y ahora es un alias de "RuntimeError".

* "symtable":

  * El método "Class.get_methods" ha quedado obsoleto desde Python
    3.14.

* "sys":

  * La función "_enablelegacywindowsfsencoding()" ha quedado obsoleta
    desde Python 3.13. En su lugar, se utiliza la variable de entorno
    "PYTHONLEGACYWINDOWSFSENCODING".

* "sysconfig":

  * The "sysconfig.expand_makefile_vars()" function has been
    deprecated since Python 3.14. Use the "vars" argument of
    "sysconfig.get_paths()" instead.

* "tarfile":

  * El atributo "TarFile.tarfile" que no se ha documentado ni
    utilizado ha quedado obsoleto desde Python 3.13.
