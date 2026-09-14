---
title: '"runpy" --- Localización y ejecución de módulos Python'
source_url: https://docs.python.org/es/3
source_path: library/runpy.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3700
---

# "runpy" --- Localización y ejecución de módulos Python

**Código Fuente:** Lib/runpy.py

======================================================================

The "runpy" module is used to locate and run Python modules without
importing them first. Its main use is to implement the "-m" command
line switch that allows scripts to be located using the Python module
namespace rather than the filesystem.

Tenga en cuenta que este *no* es un módulo de espacio aislado - todo
el código es ejecutado en el proceso actual, y cualquier efecto
secundario (como las importaciones en cache de otros módulos)
permanecerán en su lugar después de que las funciones hayan retornado.

Furthermore, any functions and classes defined by the executed code
are not guaranteed to work correctly after a "runpy" function has
returned. If that limitation is not acceptable for a given use case,
"importlib" is likely to be a more suitable choice than this module.

The "runpy" module provides two functions:

runpy.run_module(mod_name, init_globals=None, run_name=None, alter_sys=False)

   Ejecuta el código del módulo especificado y devuelve el diccionario
   de globales del módulo resultante. El código del módulo se
   encuentra primero mediante el mecanismo de importación estándar
   (consulte **PEP 302** para más detalles) y luego se ejecuta en un
   espacio de nombres de módulo nuevo.

   El argumento *mod_name* debe ser un nombre de módulo absoluto. Si
   el nombre del módulo se refiere a un paquete en lugar de a un
   módulo normal, entonces ese paquete se importa y el submódulo
   "__main__" dentro de ese paquete se ejecuta y se devuelve el
   diccionario de globales del módulo resultante.

   El argumento de diccionario opcional *init_globals* se puede
   utilizar para rellenar previamente el diccionario global del módulo
   antes de ejecutar el código. *init_globals* no se modificará. Si
   alguna de las variables globales especiales siguientes se define en
   *init_globals*, esas definiciones se reemplazan por "run_module()".

   Las variables globales especiales "__name__", "__spec__",
   "__file__", "__cached__", "__loader__" y "__package__" se
   establecen en el diccionario global antes del que el código del
   módulo sea ejecutado (tenga en cuenta que esto es un conjunto
   mínimo de variables - otras variables pueden establecerse
   implícitamente como un detalle de implementación del intérprete).

   "__name__" se establece en *run_name* si el argumento opcional no
   es "None", para "mod_name + ‘.__main__’" si módulo nombrado es un
   paquete y al argumento *mod_name* en caso contrario.

   "__spec__" se configura apropiadamente para el módulo *realmente*
   importado (es decir, "__spec__.name" siempre será un *mod_name* o
   "mod_name + '.__main__'", nunca *run_name*).

   "__file__", "__cached__", "__loader__" y "__package__" son
   establecidos de forma normal  basados en la especificación del
   módulo.

   Si el argumento *alter_sys* es proporcionado y evaluado a "True",
   entonces "sys.argv[0]" es actualizado y el valor de "__file__" y
   "sys.modules[__name__]" es actualizado con un objeto de módulo
   temporal para el módulo que se esta ejecutado. Ambas "sys.argv[0]"
   y "sys.modules[__name__]" son restauradas a sus valores originales
   antes del retorno de la función.

   Tenga en cuenta que esta manipulación de "sys" no es segura para
   los hilos. Otros hilos pueden ver el módulo parcialmente
   inicializado, así como la lista de argumentos alterada. Se
   recomienda no utilizar el módulo "sys" cuando se invoque a esta
   función desde código con hilos.

   Ver también:

     La opción "-m" ofrece una funcionalidad equivalente desde la
     línea de comandos.

   Distinto en la versión 3.1: Se agrego la capacidad de ejecutar
   paquetes buscando un submódulo "__main__".

   Distinto en la versión 3.2: Se agrego la variable global
   "__cached__" (consultar **PEP 3147**).

   Distinto en la versión 3.4: Se ha actualizado para aprovechar la
   función de especificación de módulos añadida por **PEP 451**. Esto
   permite que "__cached__" se establezca correctamente para que los
   módulos se ejecuten de esta manera, así como asegurar que el nombre
   real del módulo siempre sea accesible como "__spec__.name".

   Distinto en la versión 3.12: El establecimiento de "__cached__",
   "__loader__", y "__package__" están obsoletos. Véase "ModuleSpec"
   para alternativas.

runpy.run_path(path_name, init_globals=None, run_name=None)

   Ejecuta el código en la ubicación del sistema de ficheros indicada
   y devuelve el diccionario global del módulo resultante. Al igual
   que con un nombre de script suministrado a la línea de comandos de
   CPython, *file_path* puede referirse a un archivo fuente de Python,
   un archivo de código de bytes compilado o una entrada "sys.path"
   válida que contenga un módulo "__main__" (por ejemplo, un archivo
   zip que contenga un archivo de nivel superior "__main__.py").

   Para un script simple, el código especificado simplemente se
   ejecuta en un espacio de nombres de módulo nuevo. Para una entrada
   "sys.path" válida (normalmente un archivo zip o directorio), la
   entrada se añade primero al principio de "sys.path". A
   continuación, la función busca y ejecuta un módulo "__main__"
   utilizando la ruta actualizada. Tenga en cuenta que no hay ninguna
   protección especial contra la invocación de una entrada "__main__"
   existente ubicada en otro lugar de "sys.path" si no existe tal
   módulo en la ubicación especificada.

   El argumento de diccionario opcional *init_globals* se puede
   utilizar para rellenar previamente el diccionario global del módulo
   antes de ejecutar el código. *init_globals* no se modificará. Si
   alguna de las variables globales especiales siguientes se define en
   *init_globals*, esas definiciones se reemplazan por "run_path()".

   Las variables globales especiales "__name__", "__spec__",
   "__file__", "__cached__", "__loader__" y "__package__" se
   establecen en el diccionario global antes del que el código del
   módulo sea ejecutado (tenga en cuenta que esto es un conjunto
   mínimo de variables - otras variables pueden establecerse
   implícitamente como un detalle de implementación del intérprete).

   "__name__" se establece para *run_name* si el argumento opcional no
   es "None" y a "'<run_path>'" de lo contrario.

   Si *file_path* hace referencia directamente a un archivo script (ya
   sea como fuente o un código de bytes precompilado), entonces
   "__file__" se establecerá en *file_path*, y "__spec__",
   "__cached__", "__loader__" y "__package__" se establecerán todos en
   "None".

   Si *file_path* es una referencia a una entrada válida de
   "sys.path", entonces "__spec__" se establecerá apropiadamente para
   el módulo importado "__main__" (es decir, "__spec__.name" siempre
   será "__main__"). "__file__", "__cached__", "__loader__" y
   "__package__" serán set as normal basándose en la especificación
   del módulo.

   También se realizan una serie de modificaciones en el módulo "sys".
   En primer lugar, "sys.path" puede alterarse como se ha descrito
   anteriormente. Se actualiza "sys.argv[0]" con el valor de
   *file_path* y se actualiza "sys.modules[__name__]" con un objeto
   módulo temporal para el módulo que se está ejecutando. Todas las
   modificaciones a los elementos en "sys" son revertidas antes de que
   la función retorne.

   Tenga en cuenta que, a diferencia de "run_module()", las
   alteraciones realizadas en "sys" no son opcionales en esta función,
   ya que estos ajustes son esenciales para permitir la ejecución de
   las entradas de "sys.path". Como las limitaciones de seguridad de
   hilos aún se aplican, el uso de esta función en código con hilos
   debe ser serializado con el bloqueo de importación o delegado a un
   proceso separado.

   Ver también:

     Opciones de interfaz para una funcionalidad equivalente en la
     línea de comandos ("python path/to/script").

   Added in version 3.2.

   Distinto en la versión 3.4: Se ha actualizado para aprovechar la
   función de especificación de módulos añadida por **PEP 451**. Esto
   permite que "__cached__" se establezca correctamente en el caso de
   que "__main__" se importe desde una entrada "sys.path" válida en
   lugar de ejecutarse directamente.

   Distinto en la versión 3.12: El establecimiento de "__cached__",
   "__loader__" y "__package__" están en desuso.

Ver también:

  **PEP 338** -- Ejecutando módulos como scripts
     PEP escrito e implementado por Nick Coghlan.

  **PEP 366** -- Importaciones relativas explícitas del módulo
  principal
     PEP escrito e implementado por Nick Coghlan.

  **PEP 451** — Un tipo ModuleSpec para el sistema de Importación
     PEP escrito e implementado por Eric Snow

  Línea de comandos y entorno - Detalles de la línea de comandos
  CPython

  La función "importlib.import_module()"
