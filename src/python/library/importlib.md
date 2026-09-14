---
title: '"importlib" --- La implementación de "import"'
source_url: https://docs.python.org/es/3
source_path: library/importlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2980
---

# "importlib" --- La implementación de "import"

Added in version 3.1.

**Código fuente:** Lib/importlib/__init__.py

======================================================================

## Introducción

The purpose of the "importlib" package is three-fold.

Uno es proveer la implementación de la declaración de "import" (y así,
por extensión, el método "__import__()" ) en el código fuente de
Python. Esto provee una implementación de la "import" la cual es
compatible con cualquier intérprete de Python. También provee una
implementación que es más fácil de comprender que una implementada en
un lenguajes que no es Python.

Dos, los componentes incluidos para implementar "import"  están
expuestos en este paquete para que sea más fácil para los usuarios
crear sus propios objetos (conocidos de forma genérica como
*importer*) para participar en el proceso de importación.

Tres, el paquete contiene módulos exponiendo funcionalidad adicional
para administrar aspectos de paquetes de Python:

* "importlib.metadata" presenta acceso a metadatos de distribuciones
  de terceros.

* "importlib.resources" provee rutinas para acceder a *recursos* que
  no son código de paquetes de Python.

Ver también:

  La declaración import
     La referencia en el lenguaje para la declaración de "import".

  Especificaciones de paquetes
     Especificaciones originales de los paquetes. Algunas semánticas
     han cambiado desde que este documento fue escrito (ejemplo,
     redirección de acuerdo a "None" en "sys.modules").

  La función "__import__()"
     La declaración de "import" es una decoración sintáctica para esta
     función.

  La inicialización de la ruta de búsqueda de módulo de sys.path
     La inicialización de "sys.path".

  **PEP 235**
     Importar en sistemas que no distinguen entre mayúsculas y
     minúsculas

  **PEP 263**
     Definiendo las codificaciones del código fuente de Python

  **PEP 302**
     Nuevos ganchos de importación

  **PEP 328**
     Importaciones: Multilíneas, y absolutos/relativos

  **PEP 366**
     Importaciones relativas, explicitas, del módulo principal

  **PEP 420**
     Paquetes implícitos en el espacio de nombres

  **PEP 451**
     Un tipo de ModuleSpec para el sistema de importación

  **PEP 488**
     Eliminación de archivos PYO

  **PEP 489**
     Inicialización de extensión de módulo en múltiples fases

  **PEP 552**
     Pycs determinísticos

  **PEP 3120**
     Usando UTF-8 como la codificación fuente por defecto

  **PEP 3147**
     Repositorio de directorios PYC

## Funciones

importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)

   Una implementación de la función "__import__()" incorporada.

   Nota:

     La importación programática los módulos debe usar
     "import_module()" en lugar de esta función.

importlib.import_module(name, package=None)

   Importar un módulo. El argumento llamado *name* especifica qué
   módulo importar en términos absolutos o relativos (ejemplo, puede
   ser "pkg.mod" o "..mod"). Si el nombre fuera especificado en
   términos relativos, entonces el argumento llamado *package* debe
   ser igual al nombre del paquete que será el ancla para resolver el
   nombre del paquete (ejemplo "import_module('..mod', 'pkg.subpkg')"
   importará "pkg.mod").

   La función "import_module()" actúa como un envoltorio simplificador
   alrededor de "importlib.__import__()".  Esto quiere decir que las
   semánticas de la función son derivadas de "importlib.__import__()".
   La diferencia más importante entre las dos funciones es que
   "import_module()" retorna el paquete especificado o el módulo
   (ejemplo "pkg.mod"), mientras que "__import__()" retorna el paquete
   o módulo del nivel superior (ejemplo "pkg").

   Si está importando dinámicamente un módulo que se creó desde que el
   intérprete comenzó la ejecución (por ejemplo, creó un archivo
   fuente de Python), es posible que deba llamar a
   "invalidate_caches()" para que el nuevo módulo sea detectado por el
   sistema de importación.

   Distinto en la versión 3.3: Paquetes padres son importados
   automáticamente.

importlib.invalidate_caches()

   Invalide los cache internos de ubicadores encontrados en
   "sys.meta_path".Si un buscador implementa "invalidate_caches()"
   entonces será llamado para realizar la invalidación.Esta función
   debe ser llamada si cualquier módulo ha sido creado/instalado
   mientras tu programa esta siendo ejecutado para garantizar que
   todos los buscadores noten la existencia del nuevo módulo.

   Added in version 3.3.

   Distinto en la versión 3.10: Paquetes de espacio de nombres
   creados/instalados en una ubicación "sys.path" distinta después de
   que el mismo espacio de nombres fue importado son notados.

importlib.reload(module)

   Recarga un *modulo* previamente importado. El argumento debe ser un
   objeto módulo, por lo que debe haber sido importado exitosamente.
   Esto es útil cuando has editado el código fuente de un archivo
   usando un editor externo y deseas probar la nueva versión sin
   abandonar el interprete de Python. El valor retornado es el objeto
   módulo (que puede ser diferente si la reimportación crea un nuevo
   objeto en "sys.modules").

   Cuando "reload()" es ejecutada:

   * El código de un módulo de Python es recompilado y el código del
     módulo reejecutado, definiendo un nuevo conjunto de objetos que
     son asignados a los nombres de los módulos en el diccionario,
     reusando el *loader* que originalmente carga los módulos. El
     método "init" de los módulos de extension no es llamado de nuevo.

   * Al igual que con todos los demás objetos en Python, los objetos
     antiguos solo se recuperan después de que sus recuentos de
     referencias caen a cero.

   * Los nombres en el espacio de nombres del módulo se actualizan
     para señalar cualquier objeto nuevo o modificado.

   * Otras referencias a los objetos antiguos (como los nombres
     externos al módulo) no se vuelven a vincular para hacer
     referencia a los nuevos objetos y deben actualizarse en cada
     espacio de nombres donde se produzcan si se desea.

   Hay una serie de otras advertencias:

   Cuando se vuelve a cargar un módulo, se conserva su diccionario
   (que contiene las variables globales del módulo). Las
   redefiniciones de nombres anularán las antiguas definiciones, por
   lo que generalmente esto no es un problema. Si la nueva versión de
   un módulo no define un nombre que fue definido por la versión
   anterior, la definición anterior permanece. Esta característica se
   puede utilizar en beneficio del módulo si mantiene una tabla global
   o caché de objetos --- con una declaración "try" puede probar la
   presencia de la tabla y omitir su inicialización si lo desea:

      try:
          cache
      except NameError:
          cache = {}

   Por lo general, no es muy útil recargar módulos integrados o
   cargados dinámicamente. No se recomienda recargar "sys",
   "__main__", "builtins" y otros módulos clave. En muchos casos, los
   módulos de extensión no están diseñados para inicializarse más de
   una vez y pueden fallar de manera arbitraria cuando se vuelven a
   cargar.

   Si un módulo importa objetos de otro módulo usando "from" ...
   "import" ..., al llamar a "reload()" para el otro módulo no
   redefine los objetos importados de él --- una forma de evitar esto
   es volver a ejecutar la instrucción "from", otra es usar "import" y
   nombres calificados (*module.name*) en su lugar.

   Si un módulo crea instancias de una clase, volver a cargar el
   módulo que define la clase no afecta las definiciones de método de
   las instancias --- continúan usando la definición de clase
   anterior. Lo mismo ocurre con las clases derivadas.

   Added in version 3.4.

   Distinto en la versión 3.7: "ModuleNotFoundError" se lanza cuando
   el módulo que se está recargando carece de "ModuleSpec".

   Advertencia:

     This function is not thread-safe. Calling it from multiple
     threads can result in unexpected behavior. It's recommended to
     use the "threading.Lock" or other synchronization primitives for
     thread-safe module reloading.

## "importlib.abc" -- Abstract base classes related to import

**Código fuente:** Lib/importlib/abc.py

======================================================================

The "importlib.abc" module contains all of the core abstract base
classes used by "import". Some subclasses of the core abstract base
classes are also provided to help in implementing the core ABCs.

Jerarquía ABC:

   object
    +-- MetaPathFinder
    +-- PathEntryFinder
    +-- Loader
         +-- ResourceLoader --------+
         +-- InspectLoader          |
              +-- ExecutionLoader --+
                                    +-- FileLoader
                                    +-- SourceLoader

class importlib.abc.MetaPathFinder

   Una clase base abstracta que representa *meta path finder*.

   Added in version 3.3.

   Distinto en la versión 3.10: Ya no hereda de "Finder".

   find_spec(fullname, path, target=None)

      An abstract method for finding a *spec* for the specified
      module.  If this is a top-level import, *path* will be "None".
      Otherwise, this is a search for a subpackage or module and
      *path* will be the value of "__path__" from the parent package.
      If a spec cannot be found, "None" is returned. When passed in,
      "target" is a module object that the finder may use to make a
      more educated guess about what spec to return.
      "importlib.util.spec_from_loader()" may be useful for
      implementing concrete "MetaPathFinders".

      Added in version 3.4.

   invalidate_caches()

      Un método opcional que, cuando se llama, debería invalidar
      cualquier caché interno utilizado por el buscador. Utilizado por
      "importlib.invalidate_caches()" al invalidar los cachés de todos
      los buscadores en "sys.meta_path".

      Distinto en la versión 3.4: Retorna "None" cuando se llama en
      lugar de "NotImplemented".

class importlib.abc.PathEntryFinder

   Una clase base abstracta que representa un *buscador de entradas de
   ruta*. Aunque tiene algunas similitudes con "MetaPathFinder",
   "PathEntryFinder" está diseñado para usarse solo dentro del
   subsistema de importación basado en rutas proporcionado por
   "importlib.machinery.PathFinder".

   Added in version 3.3.

   Distinto en la versión 3.10: Ya no hereda de "Finder".

   find_spec(fullname, target=None)

      Un método abstracto para encontrar un *spec* para el módulo
      especificado. El buscador buscará el módulo solo dentro del
      *path entry* a la que está asignado. Si no se puede encontrar
      una especificación, se retorna "None". Cuando se pasa, "target"
      es un objeto de módulo que el buscador puede usar para hacer una
      suposición más informada sobre qué especificación retornar.
      "importlib.util.spec_from_loader()" puede ser útil para
      implementar "PathEntryFinders" concretos.

      Added in version 3.4.

   invalidate_caches()

      Un método opcional que, cuando se llama, debería invalidar
      cualquier caché interno utilizado por el buscador. Usado por
      "importlib.machinery.PathFinder.invalidate_caches()" al
      invalidar las cachés de todos los buscadores en caché.

class importlib.abc.Loader

   Una clase base abstracta para un *loader*. Consulte **PEP 302**
   para obtener la definición exacta de cargador.

   Los cargadores que deseen admitir la lectura de recursos deben
   implementar un método "get_resource_reader()" según lo especificado
   por "importlib.abc.ResourceReader".

   Distinto en la versión 3.7: Introducido el método opcional
   "get_resource_reader()".

   create_module(spec)

      Un método que retorna el objeto de módulo que se utilizará al
      importar un módulo. Este método puede retornar "None", lo que
      indica que se debe llevar a cabo la semántica de creación de
      módulos predeterminada.

      Added in version 3.4.

      Distinto en la versión 3.6: Este método ya no es opcional cuando
      se defina "exec_module()".

   exec_module(module)

      Un método abstracto que ejecuta el módulo en su propio espacio
      de nombres cuando se importa o se vuelve a cargar un módulo. El
      módulo ya debería estar inicializado cuando se llama a
      "exec_module()". Cuando existe este método, se debe definir
      "create_module()".

      Added in version 3.4.

      Distinto en la versión 3.6: "create_module()" también debe
      definirse.

   load_module(fullname)

      Un método heredado para cargar un módulo. Si el módulo no se
      puede cargar, se lanza "ImportError"; de lo contrario, se
      retorna el módulo cargado.

      Si el módulo solicitado ya existe en "sys.modules", ese módulo
      debe usarse y recargarse. De lo contrario, el cargador debe
      crear un nuevo módulo e insertarlo en "sys.modules" antes de que
      comience la carga, para evitar la recursividad de la
      importación. Si el cargador insertó un módulo y la carga falla,
      el cargador debe eliminarlo de "sys.modules"; los módulos que ya
      estaban en "sys.modules" antes de que el cargador comenzara a
      ejecutarse deben dejarse intactos.

      El cargador debe establecer varios atributos en el módulo (tenga
      en cuenta que algunos de estos atributos pueden cambiar cuando
      se recarga un módulo):

      * "module.__name__"

      * "module.__file__"

      * "module.__cached__" *(deprecated)*

      * "module.__path__"

      * "module.__package__" *(deprecated)*

      * "module.__loader__" *(deprecated)*

      Cuando "exec_module()" está disponible, se proporciona una
      funcionalidad compatible con versiones anteriores.

      Distinto en la versión 3.4: Lanza "ImportError" cuando se llama
      en lugar de "NotImplementedError". Funcionalidad proporcionada
      cuando "exec_module()" está disponible.

      Deprecated since version 3.4, will be removed in version 3.15:
      La API recomendada para cargar un módulo es "exec_module()" (y
      "create_module()"). Los cargadores deberían implementarlo en
      lugar de "load_module()". La maquinaria de importación se
      encarga de todas las demás responsabilidades de "load_module()"
      cuando se implementa "exec_module()".

class importlib.abc.ResourceLoader

   *Reemplazado por TraversableResources*

      Una clase base abstracta para un *loader* que implementa el
      protocolo opcional **PEP 302** para cargar recursos arbitrarios
      desde el back-end de almacenamiento.

      Obsoleto desde la versión 3.7: This ABC is deprecated in favour
      of supporting resource loading through
      "importlib.resources.abc.TraversableResources". This class
      exists for backwards compatibility only with other ABCs in this
      module.

      abstractmethod get_data(path)

            An abstract method to return the bytes for the data
            located at *path*. Loaders that have a file-like storage
            back-end that allows storing arbitrary data can implement
            this abstract method to give direct access to the data
            stored. "OSError" is to be raised if the *path* cannot be
            found. The *path* is expected to be constructed using a
            module's "__file__" attribute or an item from a package's
            "__path__".

            Distinto en la versión 3.4: Lanza "OSError" en vez de
            "NotImplementedError".

class importlib.abc.InspectLoader

   Una clase base abstracta para un *loader* que implementa el
   protocolo opcional **PEP 302** para cargadores que inspeccionan
   módulos.

   get_code(fullname)

      Retorna el objeto código para un módulo, o "None" si el módulo
      no tiene un objeto código (como sería el caso, por ejemplo, para
      un módulo integrado). Lanza un "ImportError" si el cargador no
      puede encontrar el módulo solicitado.

      Nota:

        Si bien el método tiene una implementación predeterminada, se
        sugiere que se anule si es posible para mejorar el
        rendimiento.

      Distinto en la versión 3.4: Ya no es un método abstracto y se
      proporciona una implementación concreta.

   abstractmethod get_source(fullname)

         Un método abstracto para retornar la fuente de un módulo. Se
         retorna como una cadena de caracteres de texto usando
         *universal newlines*, traduciendo todos los separadores de
         línea reconocidos en caracteres "'\n'". Retorna "None" si no
         hay una fuente disponible (por ejemplo, un módulo integrado).
         Lanza la excepción "ImportError" si el cargador no puede
         encontrar el módulo especificado.

         Distinto en la versión 3.4: Lanza "ImportError" en vez de
         "NotImplementedError".

   is_package(fullname)

      Un método opcional para retornar un valor verdadero si el módulo
      es un paquete, un valor falso en caso contrario. Se lanza
      "ImportError" si el *cargador* no puede encontrar el módulo.

      Distinto en la versión 3.4: Lanza "ImportError" en vez de
      "NotImplementedError".

   static source_to_code(data, path='<string>')

      Cree un objeto de código a partir de la fuente de Python.

      El argumento *data* puede ser cualquier cosa que admita la
      función "compile()" (es decir, cadena de caracteres o bytes). El
      argumento *path* debe ser la "ruta" de donde se originó el
      código fuente, que puede ser un concepto abstracto (por ejemplo,
      ubicación en un archivo zip).

      Con el objeto de código subsiguiente, uno puede ejecutarlo en un
      módulo ejecutando "exec(code, module.__dict__)".

      Added in version 3.4.

      Distinto en la versión 3.5: Hace el método estático.

   exec_module(module)

      Implementación de "Loader.exec_module()".

      Added in version 3.4.

   load_module(fullname)

      Implementación de "Loader.load_module()".

      Deprecated since version 3.4, will be removed in version 3.15:
      use "exec_module()" en su lugar.

class importlib.abc.ExecutionLoader

   Una clase base abstracta que hereda de "InspectLoader" que, cuando
   se implementa, ayuda a que un módulo se ejecute como un script. El
   ABC representa un protocolo opcional **PEP 302**.

   abstractmethod get_filename(fullname)

         An abstract method that is to return the value of "__file__"
         for the specified module. If no path is available,
         "ImportError" is raised.

         Si el código fuente está disponible, entonces el método debe
         devolver la ruta al archivo fuente, independientemente de si
         se utilizó un código de bytes para cargar el módulo.

         Distinto en la versión 3.4: Lanza "ImportError" en vez de
         "NotImplementedError".

class importlib.abc.FileLoader(fullname, path)

   Una clase base abstracta que hereda de "ResourceLoader" y
   "ExecutionLoader", proporcionando implementaciones concretas de
   "ResourceLoader.get_data()" y "ExecutionLoader.get_filename()".

   El argumento *fullname* es un nombre completamente resuelto del
   módulo que el cargador debe manejar. El argumento *path* es la ruta
   al archivo del módulo.

   Added in version 3.3.

   name

      El nombre del módulo que puede manejar el cargador.

   path

      Ruta al archivo del módulo.

   load_module(fullname)

      Llama a super's "load_module()".

      Deprecated since version 3.4, will be removed in version 3.15:
      Utilice "Loader.exec_module()" en su lugar.

   abstractmethod get_filename(fullname)

      Retorna "path".

   abstractmethod get_data(path)

      Lee *path* como un archivo binario y retorna los bytes de él.

class importlib.abc.SourceLoader

   Una clase base abstracta para implementar la carga de archivos
   fuente (y opcionalmente bytecode). La clase hereda tanto de
   "ResourceLoader" como de "ExecutionLoader", lo que requiere la
   implementación de:

   * "ResourceLoader.get_data()"

   * "ExecutionLoader.get_filename()"
        Solo debe devolver la ruta al archivo de origen; la carga sin
        fuente no es compatible.

   Los métodos abstractos definidos por esta clase son para agregar
   soporte de archivo de código de bytes opcional. No implementar
   estos métodos opcionales (o hacer que se lance
   "NotImplementedError") hace que el cargador solo funcione con el
   código fuente. La implementación de los métodos permite que el
   cargador trabaje con archivos fuente *y* código de bytes; no
   permite la carga *sin fuente* donde solo se proporciona un código
   de bytes. Los archivos de código de bytes son una optimización para
   acelerar la carga al eliminar el paso de análisis del compilador de
   Python, por lo que no se expone ninguna API específica de código de
   bytes.

   path_stats(path)

      Método abstracto opcional que retorna un "dict" que contiene
      metadatos sobre la ruta especificada. Las claves de diccionario
      admitidas son:

      * "'mtime'" (obligatorio): un número entero o de punto flotante
        que representa la hora de modificación del código fuente;

      * "'size'" (opcional): el tamaño en bytes del código fuente.

      Cualquier otra clave del diccionario se ignora para permitir
      futuras extensiones. Si no se puede manejar la ruta, se genera
      "OSError".

      Added in version 3.3.

      Distinto en la versión 3.4: Lanza "OSError" en vez de
      "NotImplementedError".

   path_mtime(path)

      Método abstracto opcional que retorna la hora de modificación de
      la ruta especificada.

      Obsoleto desde la versión 3.3: Este método está obsoleto en
      favor de "path_stats()". No tiene que implementarlo, pero aún
      está disponible para fines de compatibilidad. Lanza "OSError" si
      la ruta no se puede manejar.

      Distinto en la versión 3.4: Lanza "OSError" en vez de
      "NotImplementedError".

   set_data(path, data)

      Método abstracto opcional que escribe los bytes especificados en
      una ruta de archivo. Los directorios intermedios que no existan
      se crearán automáticamente.

      Cuando la escritura en la ruta falla porque la ruta es de solo
      lectura ("errno.EACCES"/"PermissionError"), no propague la
      excepción.

      Distinto en la versión 3.4: Ya no lanza "NotImplementedError"
      cuando se llama.

   get_code(fullname)

      Implementación concreta de "InspectLoader.get_code()".

   exec_module(module)

      Implementación concreta de "Loader.exec_module()".

      Added in version 3.4.

   load_module(fullname)

      Implementación concreta de "Loader.load_module()".

      Deprecated since version 3.4, will be removed in version 3.15:
      Utilice "exec_module()" en su lugar.

   get_source(fullname)

      Implementación concreta de "InspectLoader.get_source()".

   is_package(fullname)

      Implementación concreta de "InspectLoader.is_package()". Se
      determina que un módulo es un paquete si su ruta de archivo
      (proporcionada por "ExecutionLoader.get_filename()") es un
      archivo llamado "__init__" cuando se elimina la extensión del
      archivo **y** el nombre del módulo sí lo hace no termina en
      "__init__".

## "importlib.machinery" -- Importers and path hooks

**Código fuente:** Lib/importlib/machinery.py

======================================================================

Este módulo contiene varios objetos que ayudan "import" buscar y
cargar módulos.

importlib.machinery.SOURCE_SUFFIXES

   Una lista de cadenas de caracteres que representan los sufijos de
   archivo reconocidos para los módulos de origen.

   Added in version 3.3.

importlib.machinery.DEBUG_BYTECODE_SUFFIXES

   Una lista de cadenas que representan los sufijos de archivo para
   módulos de código de bytes no optimizados.

   Added in version 3.3.

   Obsoleto desde la versión 3.5: Use "BYTECODE_SUFFIXES" instead.

importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES

   Una lista de cadenas de caracteres que representan los sufijos de
   archivo para módulos de código de bytes optimizados.

   Added in version 3.3.

   Obsoleto desde la versión 3.5: Use "BYTECODE_SUFFIXES" instead.

importlib.machinery.BYTECODE_SUFFIXES

   Una lista de cadenas de caracteres que representan los sufijos de
   archivo reconocidos para los módulos de código de bytes (incluido
   el punto inicial).

   Added in version 3.3.

   Distinto en la versión 3.5: El valor ya no depende de "__debug__".

importlib.machinery.EXTENSION_SUFFIXES

   Una lista de cadenas de caracteres que representan los sufijos de
   archivo reconocidos para los módulos de extensión.

   Added in version 3.3.

importlib.machinery.all_suffixes()

   Retorna una lista combinada de cadenas de caracteres que
   representan todos los sufijos de archivo para módulos reconocidos
   por la maquinaria de importación estándar. Este es un ayudante para
   el código que simplemente necesita saber si una ruta del sistema de
   archivos potencialmente se refiere a un módulo sin necesidad de
   detalles sobre el tipo de módulo (por ejemplo,
   "inspect.getmodulename()").

   Added in version 3.3.

class importlib.machinery.BuiltinImporter

   Un *importer* para módulos integrados. Todos los módulos integrados
   conocidos se enumeran en "sys.builtin_module_names". Esta clase
   implementa los ABC "importlib.abc.MetaPathFinder" y
   "importlib.abc.InspectLoader".

   Esta clase solo define los métodos de clase para aliviar la
   necesidad de instanciación.

   Distinto en la versión 3.5: Como parte de **PEP 489**, el
   importador integrado ahora implementa "Loader.create_module()" y
   "Loader.exec_module()"

class importlib.machinery.FrozenImporter

   Un *importer* para módulos congelados. Esta clase implementa los
   ABC "importlib.abc.MetaPathFinder" y "importlib.abc.InspectLoader".

   Esta clase solo define los métodos de clase para aliviar la
   necesidad de instanciación.

   Distinto en la versión 3.4: Métodos obtenidos "create_module()" y
   "exec_module()".

class importlib.machinery.WindowsRegistryFinder

   *Finder* para los módulos declarados en el registro de Windows.
   Esta clase implementa el "importlib.abc.MetaPathFinder" ABC.

   Esta clase solo define los métodos de clase para aliviar la
   necesidad de instanciación.

   Added in version 3.3.

   Obsoleto desde la versión 3.6: Utilice la configuración de "site"
   en su lugar. Es posible que las versiones futuras de Python no
   habiliten este buscador de forma predeterminada.

class importlib.machinery.PathFinder

   Un *Finder* para "sys.path" y atributos del paquete "__path__".
   Esta clase implementa el "importlib.abc.MetaPathFinder" ABC.

   Esta clase solo define los métodos de clase para aliviar la
   necesidad de instanciación.

   classmethod find_spec(fullname, path=None, target=None)

      Método de clase que intenta encontrar un *spec* para el módulo
      especificado por *fullname* en "sys.path" o, si está definido,
      en *path*. Para cada entrada de ruta que se busca, se comprueba
      "sys.path_importer_cache". Si se encuentra un objeto que no es
      falso, se utiliza como *path entry finder* para buscar el módulo
      que se está buscando. Si no se encuentra ninguna entrada en
      "sys.path_importer_cache", entonces "sys.path_hooks" se busca un
      buscador para la entrada de ruta y, si se encuentra, se almacena
      en "sys.path_importer_cache" junto con ser consultado sobre el
      módulo. Si nunca se encuentra ningún buscador, entonces "None"
      se almacena en el caché y se retorna.

      Added in version 3.4.

      Distinto en la versión 3.5: Si el directorio de trabajo actual,
      representado por una cadena de caracteres vacía, ya no es
      válido, se retorna "None" pero no se almacena ningún valor en
      "sys.path_importer_cache".

   classmethod invalidate_caches()

      Llama "importlib.abc.PathEntryFinder.invalidate_caches()" en
      todos los buscadores almacenados en "sys.path_importer_cache"
      que definen el método. De lo contrario, las entradas en
      "sys.path_importer_cache" establecidas en "None" se eliminan.

      Distinto en la versión 3.7: Se eliminan las entradas de "None"
      en "sys.path_importer_cache".

   Distinto en la versión 3.4: Llama a objetos en "sys.path_hooks" con
   el directorio de trabajo actual para "''" (es decir, la cadena de
   caracteres vacía).

class importlib.machinery.FileFinder(path, *loader_details)

   Una implementación concreta de "importlib.abc.PathEntryFinder" que
   almacena en caché los resultados del sistema de archivos.

   El argumento *path* es el directorio que el buscador se encarga de
   buscar.

   El argumento *loader_details* es un número variable de tuplas de 2
   elementos, cada una de las cuales contiene un cargador y una
   secuencia de sufijos de archivo que el cargador reconoce. Se espera
   que los cargadores sean invocables que acepten dos argumentos del
   nombre del módulo y la ruta al archivo encontrado.

   El buscador almacenará en caché el contenido del directorio según
   sea necesario, haciendo llamadas estadísticas para cada búsqueda de
   módulo para verificar que la caché no esté desactualizada. Debido a
   que la obsolescencia de la caché se basa en la granularidad de la
   información de estado del sistema operativo del sistema de
   archivos, existe una condición de carrera potencial de buscar un
   módulo, crear un nuevo archivo y luego buscar el módulo que
   representa el nuevo archivo. Si las operaciones ocurren lo
   suficientemente rápido como para ajustarse a la granularidad de las
   llamadas estadísticas, la búsqueda del módulo fallará. Para evitar
   que esto suceda, cuando cree un módulo dinámicamente, asegúrese de
   llamar a "importlib.invalidate_caches()".

   Added in version 3.3.

   path

      La ruta en la que buscará el buscador.

   find_spec(fullname, target=None)

      Intente encontrar la especificación para manejar *fullname*
      dentro de "path".

      Added in version 3.4.

   invalidate_caches()

      Borrar el caché interno.

   classmethod path_hook(*loader_details)

      Un método de clase que retorna un cierre para su uso en
      "sys.path_hooks". El cierre retorna una instancia de
      "FileFinder" utilizando el argumento de ruta proporcionado al
      cierre directamente y *loader_details* indirectamente.

      Si el argumento del cierre no es un directorio existente, se
      lanza "ImportError".

class importlib.machinery.SourceFileLoader(fullname, path)

   Una implementación concreta de "importlib.abc.SourceLoader"
   subclasificando "importlib.abc.FileLoader" y proporcionando algunas
   implementaciones concretas de otros métodos.

   Added in version 3.3.

   name

      El nombre del módulo que manejará este cargador.

   path

      La ruta al archivo de origen.

   is_package(fullname)

      Retorna "True" si "path" parece ser para un paquete.

   path_stats(path)

      Implementación concreta de
      "importlib.abc.SourceLoader.path_stats()".

   set_data(path, data)

      Implementación concreta de
      "importlib.abc.SourceLoader.set_data()".

   load_module(name=None)

      Implementación concreta de "importlib.abc.Loader.load_module()"
      donde especificar el nombre del módulo a cargar es opcional.

      Deprecated since version 3.6, will be removed in version 3.15:
      Utilice "importlib.abc.Loader.exec_module()" en su lugar.

class importlib.machinery.SourcelessFileLoader(fullname, path)

   Una implementación concreta de "importlib.abc.FileLoader" que puede
   importar archivos de código de bytes (es decir, no existen archivos
   de código fuente).

   Tenga en cuenta que el uso directo de archivos de código de bytes
   (y, por lo tanto, no de archivos de código fuente) impide que sus
   módulos sean utilizables por todas las implementaciones de Python o
   las nuevas versiones de Python que cambian el formato de código de
   bytes.

   Added in version 3.3.

   name

      El nombre del módulo que manejará el cargador.

   path

      La ruta al archivo de código de bytes.

   is_package(fullname)

      Determina si el módulo es un paquete basado en "path".

   get_code(fullname)

      Retorna el objeto de código para "name" creado a partir de
      "path".

   get_source(fullname)

      Retorna "None" ya que los archivos de código de bytes no tienen
      fuente cuando se usa este cargador.

   load_module(name=None)

   Implementación concreta de "importlib.abc.Loader.load_module()"
   donde especificar el nombre del módulo a cargar es opcional.

   Deprecated since version 3.6, will be removed in version 3.15:
   Utilice "importlib.abc.Loader.exec_module()" en su lugar.

class importlib.machinery.ExtensionFileLoader(fullname, path)

   Una implementación concreta de "importlib.abc.ExecutionLoader" para
   módulos de extensión.

   El argumento *fullname* especifica el nombre del módulo que el
   cargador debe admitir. El argumento *path* es la ruta al archivo
   del módulo de extensión.

   Tenga en cuenta que, de manera predeterminada, la importación de un
   módulo de extensión fallará en los subintérpretes si no implementa
   la inicialización multifase (ver **PEP 489**), incluso si de lo
   contrario se importaría correctamente.

   Added in version 3.3.

   Distinto en la versión 3.12: Ahora se requiere inicialización
   multifase para el uso en subintérpretes.

   name

      Nombre del módulo que admite el cargador.

   path

      Ruta al módulo de extensión.

   create_module(spec)

      Crea el objeto de módulo a partir de la especificación dada de
      acuerdo con **PEP 489**.

      Added in version 3.5.

   exec_module(module)

      Inicializa el objeto de módulo dado de acuerdo con **PEP 489**.

      Added in version 3.5.

   is_package(fullname)

      Returns "True" if the file path points to a package's "__init__"
      module based on "EXTENSION_SUFFIXES".

   get_code(fullname)

      Retorna "None" ya que los módulos de extensión carecen de un
      objeto de código.

   get_source(fullname)

      Retorna "None" ya que los módulos de extensión no tienen código
      fuente.

   get_filename(fullname)

      Retorna "path".

      Added in version 3.4.

class importlib.machinery.NamespaceLoader(name, path, path_finder)

   Una implementación concreta de "importlib.abc.InspectLoader" para
   paquetes de espacio de nombres. Ésta es un alias para una clase
   privada y sólo se hace pública para introspeccionar el atributo
   "__loader__" en paquetes de espacio de nombres:

      >>> from importlib.machinery import NamespaceLoader
      >>> import my_namespace
      >>> isinstance(my_namespace.__loader__, NamespaceLoader)
      True
      >>> import importlib.abc
      >>> isinstance(my_namespace.__loader__, importlib.abc.Loader)
      True

   Added in version 3.11.

class importlib.machinery.ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None)

   A specification for a module's import-system-related state.  This
   is typically exposed as the module's "__spec__" attribute.  Many of
   these attributes are also available directly on a module: for
   example, "module.__spec__.origin == module.__file__".  Note,
   however, that while the *values* are usually equivalent, they can
   differ since there is no synchronization between the two objects.
   For example, it is possible to update the module's "__file__" at
   runtime and this will not be automatically reflected in the
   module's "__spec__.origin", and vice versa.

   Added in version 3.4.

   name

      The module's fully qualified name (see "module.__name__"). The
      *finder* should always set this attribute to a non-empty string.

   loader

      The *loader* used to load the module (see "module.__loader__").
      The *finder* should always set this attribute.

   origin

      The location the *loader* should use to load the module (see
      "module.__file__"). For example, for modules loaded from a ".py"
      file this is the filename. The *finder* should always set this
      attribute to a meaningful value for the *loader* to use.  In the
      uncommon case that there is not one (like for namespace
      packages), it should be set to "None".

   submodule_search_locations

      A (possibly empty) *sequence* of strings enumerating the
      locations in which a package's submodules will be found (see
      "module.__path__"). Most of the time there will only be a single
      directory in this list.

      The *finder* should set this attribute to a sequence, even an
      empty one, to indicate to the import system that the module is a
      package.  It should be set to "None" for non-package modules.
      It is set automatically later to a special object for namespace
      packages.

   loader_state

      El *buscador* podría establecer este atributo a un objeto
      conteniendo datos adicionales y específicos al módulo para usar
      cuando se carga el módulo.. De lo contrario, debe establecerse
      en "None".

   cached

      The filename of a compiled version of the module's code (see
      "module.__cached__"). The *finder* should always set this
      attribute but it may be "None" for modules that do not need
      compiled code stored.

   parent

      (Read-only) The fully qualified name of the package the module
      is in (or the empty string for a top-level module). See
      "module.__package__". If the module is a package then this is
      the same as "name".

   has_location

      "True" if the spec's "origin" refers to a loadable location,
      "False" otherwise.  This value impacts how "origin" is
      interpreted and how the module's "__file__" is populated.

class importlib.machinery.AppleFrameworkLoader(name, path)

   Una especialización de "importlib.machinery.ExtensionFileLoader"
   que puede cargar módulos de extensión en formato Framework.

   Para que sea compatible con la App Store de iOS, *todos* los
   módulos binarios de una aplicación de iOS deben ser bibliotecas
   dinámicas, contenidas en un marco con metadatos apropiados,
   almacenados en la carpeta "Frameworks" de la aplicación
   empaquetada. Solo puede haber un único binario por marco y no puede
   haber material binario ejecutable fuera de la carpeta Frameworks.

   To accommodate this requirement, when running on iOS, extension
   module binaries are *not* packaged as ".so" files on "sys.path",
   but as individual standalone frameworks. To discover those
   frameworks, this loader is registered against the ".fwork" file
   extension, with a ".fwork" file acting as a placeholder in the
   original location of the binary on "sys.path". The ".fwork" file
   contains the path of the actual binary in the "Frameworks" folder,
   relative to the app bundle. To allow for resolving a framework-
   packaged binary back to the original location, the framework is
   expected to contain a ".origin" file that contains the location of
   the ".fwork" file, relative to the app bundle.

   Por ejemplo, considere el caso de una importación "from foo.bar
   import _whiz", donde "_whiz" se implementa con el módulo binario
   "sources/foo/bar/_whiz.abi3.so", donde "sources" es la ubicación
   registrada en "sys.path", relativa al paquete de la aplicación.
   Este módulo *debe* distribuirse como
   "Frameworks/foo.bar._whiz.framework/foo.bar._whiz" (creando el
   nombre del marco a partir de la ruta de importación completa del
   módulo), con un archivo "Info.plist" en el directorio ".framework"
   que identifica el binario como un marco. El módulo "foo.bar._whiz"
   se representaría en la ubicación original con un archivo marcador
   "sources/foo/bar/_whiz.abi3.fwork", que contiene la ruta
   "Frameworks/foo.bar._whiz/foo.bar._whiz". El framework también
   contendría
   "Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin", que
   contiene la ruta al archivo ".fwork".

   When a module is loaded with this loader, the "__file__" for the
   module will report as the location of the ".fwork" file. This
   allows code to use the "__file__" of a  module as an anchor for
   file system traversal. However, the spec origin will reference the
   location of the *actual* binary in the ".framework" folder.

   El proyecto Xcode que crea la aplicación es responsable de
   convertir los archivos ".so" desde donde se encuentren en
   "PYTHONPATH" en marcos en la carpeta "Frameworks" (lo que incluye
   quitar las extensiones del archivo del módulo, agregar metadatos
   del marco y firmar el marco resultante), y crear los archivos
   ".fwork" y ".origin". Esto generalmente se hará con un paso de
   compilación en el proyecto Xcode; consulte la documentación de iOS
   para obtener detalles sobre cómo construir este paso de
   compilación.

   Added in version 3.13.

   Availability: iOS.

   name

      Nombre del módulo que admite el cargador.

   path

      Ruta al archivo ".fwork" para el módulo de extensión.

## "importlib.util" -- Utility code for importers

**Código fuente:** Lib/importlib/util.py

======================================================================

Este módulo contiene los diversos objetos que ayudan en la
construcción de un *importer*.

importlib.util.MAGIC_NUMBER

   Los bytes que representan el número de versión del código de bytes.
   Si necesita ayuda para cargar/escribir código de bytes, considere
   "importlib.abc.SourceLoader".

   Added in version 3.4.

importlib.util.cache_from_source(path, debug_override=None, *, optimization=None)

   Retorna la ruta **PEP 3147**/**PEP 488** al archivo compilado por
   bytes asociado con la *path* de origen. Por ejemplo, si *path* es
   "/foo/bar/baz.py", el valor de retorno sería
   "/foo/bar/__pycache__/baz.cpython-32.pyc" para Python 3.2. La
   cadena de caracteres "cpython-32" proviene de la etiqueta mágica
   actual (ver "get_tag()"; si "sys.implementation.cache_tag" no está
   definido, se lanzará "NotImplementedError").

   El parámetro *optimization* se utiliza para especificar el nivel de
   optimización del archivo de código de bytes. Una cadena de
   caracteres vacía no representa optimización, por lo que
   "/foo/bar/baz.py" con una *optimization* de "''" dará como
   resultado una ruta de código de bytes de
   "/foo/bar/__pycache__/baz.cpython-32.pyc". "None" hace que se
   utilice el nivel de optimización del intérprete. Se usa la
   representación de cadena de caracteres de cualquier otro valor, por
   lo que "/foo/bar/baz.py" con una *optimization* de "2" conducirá a
   la ruta del código de bytes de
   "/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc". La representación
   de cadena de caracteres *optimization* solo puede ser alfanumérica,
   de lo contrario se lanza "ValueError".

   El parámetro *debug_override* está obsoleto y se puede usar para
   anular el valor del sistema para "__debug__". Un valor "True" es el
   equivalente a establecer *optimization* en la cadena de caracteres
   vacía. Un valor "False" es lo mismo que establecer *optimization*
   en "1". Si tanto *debug_override* como *optimization* no es "None",
   entonces se lanza "TypeError".

   Added in version 3.4.

   Distinto en la versión 3.5: Se agregó el parámetro *optimization* y
   el parámetro *debug_override* quedó obsoleto.

   Distinto en la versión 3.6: Acepta un *path-like object*.

importlib.util.source_from_cache(path)

   Dado el *path* a un nombre de archivo **PEP 3147**, retorna la ruta
   del archivo del código fuente asociado. Por ejemplo, si *path* es
   "/foo/bar/__pycache__/baz.cpython-32.pyc", la ruta retornada sería
   "/foo/bar/baz.py". *path* no necesita existir, sin embargo, si no
   se ajusta al formato **PEP 3147** o **PEP 488**, se lanza un
   "ValueError". Si "sys.implementation.cache_tag" no está definido,
   se lanza "NotImplementedError".

   Added in version 3.4.

   Distinto en la versión 3.6: Acepta un *path-like object*.

importlib.util.decode_source(source_bytes)

   Decodifica los bytes dados que representan el código fuente y los
   retorna como una cadena de caracteres con nuevas líneas universales
   (como lo requiere "importlib.abc.InspectLoader.get_source()").

   Added in version 3.4.

importlib.util.resolve_name(name, package)

   Resuelve un nombre de módulo relativo a uno absoluto.

   Si **name** no tiene puntos iniciales, entonces **name**
   simplemente se retorna. Esto permite el uso como
   "importlib.util.resolve_name('sys', __spec__.parent)" sin hacer una
   verificación para ver si se necesita el argumento **package**.

   "ImportError" se lanza si **name** es un nombre de módulo relativo
   pero **package** es un valor falso (por ejemplo, "None" o la cadena
   de caracteres vacía). También se lanza "ImportError" si un nombre
   relativo escaparía del paquete que lo contiene (por ejemplo,
   solicitando "..bacon" desde el paquete "spam").

   Added in version 3.3.

   Distinto en la versión 3.9: Para mejorar la coherencia con las
   declaraciones de importación, aumente "ImportError" en lugar de
   "ValueError" para intentos de importación relativa no válidos.

importlib.util.find_spec(name, package=None)

   Busque el *spec* de un módulo, opcionalmente relativa al nombre del
   **paquete** especificado. Si el módulo está en "sys.modules", se
   retorna "sys.modules[name].__spec__" (a menos que la especificación
   sea "None" o no esté configurada, en cuyo caso se lanza una
   excepción "ValueError"). De lo contrario, se realiza una búsqueda
   utilizando "sys.meta_path". Se retorna "None" si no se encuentra
   ninguna especificación.

   Si **name** es para un submódulo (contiene un punto), el módulo
   principal se importa automáticamente.

   **name** y **package** funcionan igual que para "import_module()".

   Added in version 3.4.

   Distinto en la versión 3.7: Raises "ModuleNotFoundError" instead of
   "AttributeError" if **package** is in fact not a package (i.e.
   lacks a "__path__" attribute).

importlib.util.module_from_spec(spec)

   Cree un nuevo módulo basado en **spec** y
   "spec.loader.create_module".

   Si "spec.loader.create_module" no retorna "None", no se
   restablecerán los atributos preexistentes. Además, no se lanzará
   "AttributeError" si se activa mientras se accede a **spec** o se
   establece un atributo en el módulo.

   Esta función es preferible a usar "types.ModuleType" para crear un
   nuevo módulo ya que **spec** se usa para establecer tantos
   atributos de importación controlados en el módulo como sea posible.

   Added in version 3.5.

importlib.util.spec_from_loader(name, loader, *, origin=None, is_package=None)

   Una función de fábrica para crear una instancia de "ModuleSpec"
   basada en un cargador. Los parámetros tienen el mismo significado
   que para ModuleSpec. La función utiliza APIs disponibles de
   *loader*, tal como "InspectLoader.is_package()", para completar
   cualquier información que falte en la especificación.

   Added in version 3.4.

importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)

   Una función de fábrica para crear una instancia de "ModuleSpec"
   basada en la ruta a un archivo. La información que falte se
   completará en la especificación mediante el uso de las API de
   loader y la implicación de que el módulo estará basado en archivos.

   Added in version 3.4.

   Distinto en la versión 3.6: Acepta un *path-like object*.

importlib.util.source_hash(source_bytes)

   Retorna el hash de *source_bytes* como bytes. Un archivo ".pyc"
   basado en hash incrusta "source_hash()" del contenido del archivo
   fuente correspondiente en su encabezado.

   Added in version 3.7.

importlib.util._incompatible_extension_module_restrictions(*, disable_check)

   Un administrador de contexto que puede omitir temporalmente la
   comprobación de compatibilidad para módulos de extensión. De manera
   predeterminada, la comprobación está habilitada y fallará cuando se
   importe un módulo de inicialización de una sola fase en un
   subintérprete. También fallará para un módulo de inicialización de
   varias fases que no admita explícitamente una GIL por intérprete,
   cuando se importe en un intérprete con su propia GIL.

   Tenga en cuenta que esta función está pensada para dar cabida a un
   caso inusual, que probablemente desaparecerá en algún momento. Es
   muy probable que esto no sea lo que estaba buscando.

   Puede obtener el mismo efecto que esta función implementando la
   interfaz básica de init multifase (**PEP 489**) y mintiendo acerca
   del soporte para múltiples intérpretes (o por intérprete GIL).

   Advertencia:

     El uso de esta función para desactivar la comprobación puede
     provocar un comportamiento inesperado e incluso fallos. Solo debe
     utilizarse durante el desarrollo de módulos de extensión.

   Added in version 3.12.

class importlib.util.LazyLoader(loader)

   Una clase que pospone la ejecución del cargador de un módulo hasta
   que el módulo tiene acceso a un atributo.

   Esta clase **solo** funciona con cargadores que definen
   "exec_module()", ya que se requiere control sobre qué tipo de
   módulo se usa para el módulo. Por esas mismas razones, el método
   "create_module()" del cargador debe retornar "None" o un tipo para
   el cual se pueda mutar su atributo "__class__" junto con no usar
   *slots*. Finalmente, los módulos que sustituyen el objeto colocado
   en "sys.modules" no funcionarán ya que no hay forma de reemplazar
   correctamente las referencias del módulo en todo el intérprete de
   manera segura; "ValueError" se lanza si se detecta dicha
   sustitución.

   Nota:

     Para proyectos donde el tiempo de inicio es crítico, esta clase
     permite minimizar potencialmente el costo de cargar un módulo si
     nunca se usa. Para proyectos en los que el tiempo de inicio no es
     esencial, el uso de esta clase se desaconseja **en gran medida**
     debido a que los mensajes de error creados durante la carga se
     posponen y, por lo tanto, ocurren fuera de contexto.

   Added in version 3.5.

   Distinto en la versión 3.6: Comenzó a llamar "create_module()",
   eliminando la advertencia de compatibilidad para
   "importlib.machinery.BuiltinImporter" y
   "importlib.machinery.ExtensionFileLoader".

   classmethod factory(loader)

      Un método de clase que retorna un elemento invocable que crea un
      cargador diferido. Está pensado para usarse en situaciones en
      las que el cargador se pasa por clase en lugar de por instancia.

         suffixes = importlib.machinery.SOURCE_SUFFIXES
         loader = importlib.machinery.SourceFileLoader
         lazy_loader = importlib.util.LazyLoader.factory(loader)
         finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes))

## Ejemplos

### Importar programáticamente

Para importar un módulo mediante programación, use
"importlib.import_module()".

   import importlib

   itertools = importlib.import_module('itertools')

### Comprobando si se puede importar un módulo

Si necesita averiguar si un módulo se puede importar sin realmente
realizar la importación, entonces debe usar
"importlib.util.find_spec()".

Note que si "name" es un sub-módulo (contiene sólo un punto),
"importlib.util.find_spec()" importará el módulo padre.

   import importlib.util
   import sys

   # Con fines ilustrativos.
   name = 'itertools'

   if name in sys.modules:
       print(f"{name!r} already in sys.modules")
   elif (spec := importlib.util.find_spec(name)) is not None:
   # Si eligió realizar la importación real ...
   module = importlib.util.module_from_spec(spec)
   sys.modules[name] = module
   spec.loader.exec_module(module)
   print(f"{name!r} ha sido importado")
   else:
       print(f"no puede ser encontrado el módulo {name!r}")

### Importar un archivo fuente directamente

Esta receta debe usarse con precaución: es una aproximación de una
declaración de importación donde se especifica directamente la ruta
del archivo, en lugar de buscar "sys.path". Primero se deben
considerar alternativas, como modificar "sys.path" cuando se requiere
un módulo adecuado o usar "runpy.run_path()" cuando el espacio de
nombres global resultante de la ejecución de un archivo Python es
apropiado.

Para importar un archivo fuente de Python directamente desde una ruta,
use la siguiente receta:

   import importlib.util
   import sys

   def import_from_path(module_name, file_path):
       spec = importlib.util.spec_from_file_location(module_name, file_path)
       module = importlib.util.module_from_spec(spec)
       sys.modules[module_name] = module
       spec.loader.exec_module(module)
       return module

   # Sólo con fines ilustrativos. (el uso de `json` es arbitrario).
   import json
   file_path = json.__file__
   module_name = json.__name__

   # Resultado similar a `import json`.
   json = import_from_path(module_name, file_path)

### Implementar importaciones diferidas

El ejemplo de abajo muestra cómo implementar importaciones diferidas:

   >>> import importlib.util
   >>> import sys
   >>> def lazy_import(name):
   ...     spec = importlib.util.find_spec(name)
   ...     loader = importlib.util.LazyLoader(spec.loader)
   ...     spec.loader = loader
   ...     module = importlib.util.module_from_spec(spec)
   ...     sys.modules[name] = module
   ...     loader.exec_module(module)
   ...     return module
   ...
   >>> lazy_typing = lazy_import("typing")
   >>> #lazy_typing es un objeto de módulo real,
   >>> #pero aún no está cargado en la memoria.
   >>> lazy_typing.TYPE_CHECKING
   False

### Configurar un importador

Para personalizaciones profundas de importación, normalmente querrá
implementar un *importador*. Esto significa gestionar tanto el
*buscador* como el *cargador*. Para los buscadores hay dos opciones
para elegir según sus necesidades: un *meta path finder* o un *path
entry finder*. El primero es lo que pondría en "sys.meta_path"
mientras que el segundo es lo que crea utilizando un *path entry hook*
en "sys.path_hooks" que funciona con entradas "sys.path" para crear
potencialmente un buscador. Este ejemplo le mostrará cómo registrar
sus propios importadores para que la importación los utilice (para
crear un importador para usted, lea la documentación de las clases
apropiadas definidas dentro de este paquete):

   import importlib.machinery
   import sys

   # Sólo con fines ilustrativos.
   SpamMetaPathFinder = importlib.machinery.PathFinder
   SpamPathEntryFinder = importlib.machinery.FileFinder
   detalles_del_cargador = (importlib.machinery.SourceFileLoader,
                                               importlib.machinery.SOURCE_SUFFIXES)

   # Configuración de un meta buscador de rutas.
   # Asegúrese de colocar el buscador en la ubicación adecuada en la lista en términos de
   # prioridad.
   sys.meta_path.append(SpamMetaPathFinder)

   # Configuración de un buscador de entradas de ruta.
   # Asegúrese de colocar el gancho de ruta en la ubicación adecuada en la lista en términos
   # de prioridad.
   sys.path_hooks.append(SpamPathEntryFinder.path_hook(detalles_del_cargador))

### Aproximando "importlib.import_module()"

La importación en sí está implementada en código Python, lo que
permite exponer la mayor parte de la maquinaria de importación a
través de importlib. Lo siguiente ayuda a ilustrar las diversas API
que importlib expone al proporcionar una implementación aproximada de
"importlib.import_module()":

   import importlib.util
   import sys

   def import_module(name, package=None):
       """An approximate implementation of import."""
       absolute_name = importlib.util.resolve_name(name, package)
       try:
           return sys.modules[absolute_name]
       except KeyError:
           pass

       path = None
       if '.' in absolute_name:
           parent_name, _, child_name = absolute_name.rpartition('.')
           parent_module = import_module(parent_name)
           path = parent_module.__spec__.submodule_search_locations
       for finder in sys.meta_path:
           spec = finder.find_spec(absolute_name, path)
           if spec is not None:
               break
       else:
           msg = f'No module named {absolute_name!r}'
           raise ModuleNotFoundError(msg, name=absolute_name)
       module = importlib.util.module_from_spec(spec)
       sys.modules[absolute_name] = module
       spec.loader.exec_module(module)
       if path is not None:
           setattr(parent_module, child_name, module)
       return module
