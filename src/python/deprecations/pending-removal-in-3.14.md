---
title: Pending removal in Python 3.14
source_url: https://docs.python.org/es/3
source_path: deprecations/pending-removal-in-3.14.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 890
---

# Pending removal in Python 3.14

* "argparse": Los parámetros de "argparse.BooleanOptionalAction",
  *type*, *choices*, y *metavar*, son obsoletos y serán eliminados en
  la versión 3.14 (Contribución de Nikita Sobolev en gh-92248.)

* "ast": Las siguientes capacidades han quedado obsoletas en la
  documentación desde Python 3.8, ahora hacen que se emita una
  excepción "DeprecationWarning" en tiempo de ejecución cuando se
  accede a ellas o se utilizan, y se eliminarán en Python 3.14:

  * "ast.Num"

  * "ast.Str"

  * "ast.Bytes"

  * "ast.NameConstant"

  * "ast.Ellipsis"

  Use "ast.Constant" en su lugar. (Contribución de Serhiy Storchaka en
  gh-90953.)

* "asyncio":

  * The child watcher classes "asyncio.MultiLoopChildWatcher",
    "asyncio.FastChildWatcher", "asyncio.AbstractChildWatcher" and
    "asyncio.SafeChildWatcher" are deprecated and will be removed in
    Python 3.14. (Contributed by Kumar Aditya in gh-94597.)

  * "asyncio.set_child_watcher()", "asyncio.get_child_watcher()",
    "asyncio.AbstractEventLoopPolicy.set_child_watcher()" and
    "asyncio.AbstractEventLoopPolicy.get_child_watcher()" are
    deprecated and will be removed in Python 3.14. (Contributed by
    Kumar Aditya in gh-94597.)

  * El método "get_event_loop()" de la política de bucle de eventos
    predeterminada ahora emite un "DeprecationWarning" si no hay
    ningún bucle de eventos definido actualmente y decide crear uno.
    (Contribución de Serhiy Storchaka y Guido van Rossum en
    gh-100160.)

* "email": Se ha descontinuado el parámetro *isdst* en
  "email.utils.localtime()". (Contribución de Alan Williams en
  gh-72346.)

* Clases obsoletas de "importlib.abc":

  * "importlib.abc.ResourceReader"

  * "importlib.abc.Traversable"

  * "importlib.abc.TraversableResources"

  Use las clases "importlib.resources.abc" en su lugar:

  * "importlib.resources.abc.Traversable"

  * "importlib.resources.abc.TraversableResources"

  (Contribución de Jason R. Coombs y Hugo van Kemenade en gh-93963.)

* "itertools" tenía un soporte indocumentado, ineficiente,
  históricamente lleno de errores e inconsistente para operaciones de
  copia, copia profunda y *pickle*. Esto se eliminará en la versión
  3.14 para lograr una reducción significativa en el volumen de código
  y la carga de mantenimiento. (Contribución de Raymond Hettinger en
  gh-101588.)

* "multiprocessing": El método de inicio predeterminado cambiará a uno
  más seguro en Linux, BSDs y otras plataformas POSIX que no sean
  macOS donde "'fork'" es actualmente el predeterminado (gh-84559).
  Agregar una advertencia de tiempo de ejecución sobre esto se
  consideró demasiado disruptivo, ya que no se espera que la mayoría
  del código tenga en cuenta esto. Use las APIs "get_context()" o
  "set_start_method()" para especificar explícitamente cuándo su
  código *requires* "'fork'". Consulte Contextos y métodos de inicio.

* "pathlib": "is_relative_to()" y "relative_to()": pasar argumentos
  adicionales está obsoleto.

* "pkgutil": "pkgutil.find_loader()" and "pkgutil.get_loader()" now
  raise "DeprecationWarning"; use "importlib.util.find_spec()"
  instead. (Contributed by Nikita Sobolev in gh-97850.)

* "pty":

  * "master_open()": use "pty.openpty()".

  * "slave_open()": use "pty.openpty()".

* "sqlite3":

  * "version" and "version_info".

  * "execute()" y "executemany()" si se utilizan marcadores de
    posición con nombre y *parameters* es una secuencia en lugar de
    "dict".

* "urllib": "urllib.parse.Quoter" está obsoleto: no estaba destinado a
  ser una API pública. (Contribución de Gregory P. Smith en gh-88168.)
