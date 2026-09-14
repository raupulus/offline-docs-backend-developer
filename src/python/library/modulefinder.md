---
title: '"modulefinder" --- Find modules used by a script'
source_url: https://docs.python.org/es/3
source_path: library/modulefinder.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3240
---

# "modulefinder" --- Find modules used by a script

**Código fuente:** Lib/modulefinder.py

======================================================================

Este módulo provee una clase "ModuleFinder" que puede ser usada para
determinar el conjunto de módulos importados en un script.
"modulefinder.py" puede también ejecutarse como un script, dando el
nombre de un archivo de Python como argumento, tras lo cual se
imprimirá un reporte de los módulos importados.

modulefinder.AddPackagePath(pkg_name, path)

   Registra que el paquete llamado *pkg_name* pueda ser encontrado en
   el *path* especificado.

modulefinder.ReplacePackage(oldname, newname)

   Permite especificar que el módulo llamado *oldname* es de hecho el
   paquete llamado *newname*.

class modulefinder.ModuleFinder(path=None, debug=0, excludes=[], replace_paths=[])

   Esta clase provee los métodos "run_script()" y "report()" que
   determinan el conjunto de módulos importados por un script. *path*
   puede ser un listado de directorios a buscar por módulos; si no es
   especificado, se usará "sys.path". *debug* define el nivel de
   depuración; valores más altos hacen que la clase imprima mensajes
   de depuración acerca de lo que está haciendo. *excludes* es una
   lista de nombres de módulos que serán excluidos del análisis.
   *replace_paths* es una lista de tuplas "(oldpath, newpath)" que
   serán remplazadas en las rutas de los módulos.

   report()

      Imprime un reporte a la salida estándar que lista los módulos
      importados por el script y sus rutas, así como los módulos que
      faltan o parecieran faltar.

   run_script(pathname)

      Analiza los contenidos del archivo *pathname*, que debe contener
      código Python.

   modules

      Un diccionario que mapea los nombres de los módulos a los
      módulos. Vea Ejemplo de uso de ModuleFinder.

## Ejemplo de uso de "ModuleFinder"

El script que será analizado más adelante (bacon.py):

   import re, itertools

   try:
       import baconhameggs
   except ImportError:
       pass

   try:
       import guido.python.ham
   except ImportError:
       pass

El script que generará el reporte de bacon.py:

   from modulefinder import ModuleFinder

   finder = ModuleFinder()
   finder.run_script('bacon.py')

   print('Loaded modules:')
   for name, mod in finder.modules.items():
       print('%s: ' % name, end='')
       print(','.join(list(mod.globalnames.keys())[:3]))

   print('-'*50)
   print('Modules not imported:')
   print('\n'.join(finder.badmodules.keys()))

Resultado de ejemplo (puede variar dependiendo de la arquitectura):

   Loaded modules:
   _types:
   copyreg:  _inverted_registry,_slotnames,__all__
   re._compiler:  isstring,_sre,_optimize_unicode
   _sre:
   re._constants:  REPEAT_ONE,makedict,AT_END_LINE
   sys:
   re:  __module__,finditer,_expand
   itertools:
   __main__:  re,itertools,baconhameggs
   re._parser:  _PATTERNENDERS,SRE_FLAG_UNICODE
   array:
   types:  __module__,IntType,TypeType
   ---------------------------------------------------
   Modules not imported:
   guido.python.ham
   baconhameggs
