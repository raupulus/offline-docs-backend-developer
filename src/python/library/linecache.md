---
title: '"linecache" --- Random access to text lines'
source_url: https://docs.python.org/es/3
source_path: library/linecache.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3100
---

# "linecache" --- Random access to text lines

**Código fuente:** Lib/linecache.py

======================================================================

The "linecache" module allows one to get any line from a Python source
file, while attempting to optimize internally, using a cache, the
common case where many lines are read from a single file.  This is
used by the "traceback" module to retrieve source lines for inclusion
in  the formatted traceback.

La función "tokenize.open()" se utiliza para abrir archivos. Esta
función usa "tokenize.detect_encoding()" para obtener la codificación
del archivo; en la ausencia de un token de codificación, la
codificación del archivo es por defecto UTF-8.

The "linecache" module defines the following functions:

linecache.getline(filename, lineno, module_globals=None)

   Obtiene la línea *lineno* del archivo llamado *filename*. Esta
   función nunca lanzará una excepción --- retornará "''" en los
   errores (el carácter de la nueva línea de terminación se incluirá
   para las líneas que se encuentren).

   If *filename* indicates a frozen module (starting with "'<frozen
   '"), the function will attempt to get the real file name from
   "module_globals['__file__']" if *module_globals* is not "None".

   Si un archivo llamado *filename* no se encuentra, la función
   primero verifica un "__loader__" en *module_globals* **PEP 302**.
   Si existe tal cargador y define un método "get_source", entonces
   eso determina las líneas de origen (si "get_source()" retorna
   "None", entonces se retorna "''"). Finalmente, si *filename* es un
   nombre de fichero relativo, se busca en relación a las entradas en
   la ruta de búsqueda del módulo, "sys.path".

   Distinto en la versión 3.14: Support *filename* of frozen modules.

linecache.clearcache()

   Borra el caché. Use esta función si ya no necesita las líneas de
   archivos leídos previamente usando "getline()".

linecache.checkcache(filename=None)

   Comprueba la validez de la caché. Use esta función si los archivos
   de la caché pueden haber cambiado en disco y necesita la versión
   actualizada. Si se omite *filename*, comprobará todas las entradas
   en la caché.

linecache.lazycache(filename, module_globals)

   Captura suficientes detalles sobre un módulo no basado en archivos
   para permitir obtener sus líneas más tarde a través de "getline()"
   incluso si *module_globals* es "None" en la llamada posterior. Esto
   evita hacer E/S hasta que una línea es realmente necesaria, sin
   tener que llevar los módulo globales indefinidamente.

   Added in version 3.5.

Ejemplo:

   >>> import linecache
   >>> linecache.getline(linecache.__file__, 8)
   'import sys\n'
