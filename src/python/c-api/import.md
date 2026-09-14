---
title: Importando módulos
source_url: https://docs.python.org/es/3
source_path: c-api/import.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 340
---

# Importando módulos

PyObject *PyImport_ImportModule(const char *name)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta es una envoltura alrededor de "PyImport_Import()" que toma un
   const char* como argumento en lugar de un PyObject*.

PyObject *PyImport_ImportModuleNoBlock(const char *name)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta función es un alias obsoleto de "PyImport_ImportModule()".

   Distinto en la versión 3.3: Esta función solía fallar
   inmediatamente cuando el bloqueo de importación era retenido por
   otro hilo. Sin embargo, en Python 3.3, el esquema de bloqueo cambió
   a bloqueos por módulo para la mayoría de los propósitos, por lo que
   el comportamiento especial de esta función ya no es necesario.

   Deprecated since version 3.13, will be removed in version 3.15: Usa
   "PyImport_ImportModule()" en su lugar.

PyObject *PyImport_ImportModuleEx(const char *name, PyObject *globals, PyObject *locals, PyObject *fromlist)
    *Return value: New reference.*

   Importa un módulo. Esto se describe mejor refiriéndose a la función
   incorporada de Python "__import__()".

   El valor de retorno es una nueva referencia al módulo importado o
   paquete de nivel superior, o "NULL" con una excepción establecida
   en caso de error. Como para "__import__()", el valor de retorno
   cuando se solicita un submódulo de un paquete es normalmente el
   paquete de nivel superior, a menos que se proporcione una
   *fromlist* no vacía.

   Las importaciones que fallan eliminan objetos de módulo
   incompletos, como con "PyImport_ImportModule()".

PyObject *PyImport_ImportModuleLevelObject(PyObject *name, PyObject *globals, PyObject *locals, PyObject *fromlist, int level)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Importa un módulo. Esto se describe mejor haciendo referencia a la
   función Python incorporada "__import__()", ya que la función
   estándar "__import__()" llama a esta función directamente.

   El valor de retorno es una nueva referencia al módulo importado o
   paquete de nivel superior, o "NULL" con una excepción establecida
   en caso de error. Como para "__import__()", el valor de retorno
   cuando se solicita un submódulo de un paquete es normalmente el
   paquete de nivel superior, a menos que se proporcione una
   *fromlist* no vacía.

   Added in version 3.3.

PyObject *PyImport_ImportModuleLevel(const char *name, PyObject *globals, PyObject *locals, PyObject *fromlist, int level)
    *Return value: New reference.** Part of the Stable ABI.*

   Similar a "PyImport_ImportModuleLevelObject()", pero el nombre es
   una cadena de caracteres codificada UTF-8 en lugar de un objeto
   Unicode.

   Distinto en la versión 3.3: Los valores negativos para *level* ya
   no se aceptan.

PyObject *PyImport_Import(PyObject *name)
    *Return value: New reference.** Part of the Stable ABI.*

   Esta es una interfaz de nivel superior que llama a la "función de
   enlace de importación" actual (con un nivel explícito de 0, que
   significa importación absoluta). Invoca la función "__import__()"
   de las "__builtins__" de los globales (*globals*) actuales. Esto
   significa que la importación se realiza utilizando los ganchos de
   importación instalados en el entorno actual.

   Esta función siempre usa importaciones absolutas.

PyObject *PyImport_ReloadModule(PyObject *m)
    *Return value: New reference.** Part of the Stable ABI.*

   Recarga un módulo. Retorna una nueva referencia al módulo
   recargado, o "NULL" con una excepción establecida en caso de error
   (el módulo todavía existe en este caso).

PyObject *PyImport_AddModuleRef(const char *name)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.13.*

   Retorna el objeto módulo correspondiente a un nombre de módulo.

   El argumento *name* puede tener la forma "package.module". Primero
   verifica el diccionario de módulos si hay uno allí, y si no, crea
   uno nuevo y lo inserta en el diccionario de módulos.

   Retorna una *referencia fuerte* al módulo en caso de éxito. Retorna
   "NULL" con una excepción establecida en caso de error.

   El nombre del módulo *name* se decodifica desde UTF-8.

   Esta función no carga ni importa el módulo; si el módulo no estaba
   cargado, obtendrás un objeto de módulo vacío. Utiliza
   "PyImport_ImportModule()" o una de sus variantes para importar un
   módulo. Las estructuras de paquete implicadas por un nombre
   punteado para *name* no se crean si aún no están presentes.

   Added in version 3.13.

PyObject *PyImport_AddModuleObject(PyObject *name)
    *Return value: Borrowed reference.** Part of the Stable ABI since
   version 3.7.*

   Similar a "PyImport_AddModuleRef()", pero retorna una *referencia
   prestada* y *name* es un objeto Python "str".

   Added in version 3.3.

PyObject *PyImport_AddModule(const char *name)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Similar a "PyImport_AddModuleRef()", pero retorna una *referencia
   prestada*.

PyObject *PyImport_ExecCodeModule(const char *name, PyObject *co)
    *Return value: New reference.** Part of the Stable ABI.*

   Dado un nombre de módulo (posiblemente de la forma
   "package.module") y un objeto código leído desde un archivo de
   *bytecode* de Python u obtenido de la función incorporada
   "compile()", carga el módulo. Retorna una nueva referencia al
   objeto módulo, o "NULL" con una excepción establecida si se produjo
   un error. *name* se elimina de "sys.modules" en casos de error,
   incluso si *name* ya estaba en "sys.modules" en la entrada a
   "PyImport_ExecCodeModule()". Dejar módulos inicializados de forma
   incompleta en "sys.modules" es peligroso, ya que las importaciones
   de dichos módulos no tienen forma de saber que el objeto del módulo
   es un estado desconocido (y probablemente dañado con respecto a las
   intenciones del autor del módulo).

   The module's "__spec__" and "__loader__" will be set, if not set
   already, with the appropriate values.  The spec's loader will be
   set to the module's "__loader__" (if set) and to an instance of
   "SourceFileLoader" otherwise.

   The module's "__file__" attribute will be set to the code object's
   "co_filename".  If applicable, "__cached__" will also be set.

   Esta función volverá a cargar el módulo si ya se importó. Consulte
   "PyImport_ReloadModule()" para conocer la forma prevista de volver
   a cargar un módulo.

   Si *name* apunta a un nombre punteado de la forma "package.module",
   cualquier estructura de paquete que no se haya creado aún no se
   creará.

   Ver también "PyImport_ExecCodeModuleEx()" y
   "PyImport_ExecCodeModuleWithPathnames()".

   Distinto en la versión 3.12: The setting of "__cached__" and
   "__loader__" is deprecated. See "ModuleSpec" for alternatives.

PyObject *PyImport_ExecCodeModuleEx(const char *name, PyObject *co, const char *pathname)
    *Return value: New reference.** Part of the Stable ABI.*

   Like "PyImport_ExecCodeModule()", but the "__file__" attribute of
   the module object is set to *pathname* if it is non-"NULL".

   Ver también "PyImport_ExecCodeModuleWithPathnames()".

PyObject *PyImport_ExecCodeModuleObject(PyObject *name, PyObject *co, PyObject *pathname, PyObject *cpathname)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.7.*

   Like "PyImport_ExecCodeModuleEx()", but the "__cached__" attribute
   of the module object is set to *cpathname* if it is non-"NULL".  Of
   the three functions, this is the preferred one to use.

   Added in version 3.3.

   Distinto en la versión 3.12: Setting "__cached__" is deprecated.
   See "ModuleSpec" for alternatives.

PyObject *PyImport_ExecCodeModuleWithPathnames(const char *name, PyObject *co, const char *pathname, const char *cpathname)
    *Return value: New reference.** Part of the Stable ABI.*

   Como "PyImport_ExecCodeModuleObject()", pero *name*, *pathname* y
   *cpathname* son cadenas codificadas UTF-8. También se hacen
   intentos de averiguar cuál debería ser el valor para *pathname*
   desde *cpathname* si el primero se establece en "NULL".

   Added in version 3.2.

   Distinto en la versión 3.3: Utiliza "imp.source_from_cache()" para
   calcular la ruta de origen si solo se proporciona la ruta del
   *bytecode*.

   Distinto en la versión 3.12: Ya no usa el módulo "imp" eliminado.

long PyImport_GetMagicNumber()
    * Part of the Stable ABI.*

   Retorna el número mágico para archivos de bytecode de Python
   (también conocidos como archivos ".pyc"). El número mágico debería
   estar presente en los primeros cuatro bytes del archivo bytecode,
   en orden de bytes little-endian. Retorna "-1" en caso de error.

   Distinto en la versión 3.3: Retorna un valor de "-1" en caso de
   error.

const char *PyImport_GetMagicTag()
    * Part of the Stable ABI.*

   Retorna la cadena de caracteres de etiqueta mágica para nombres de
   archivo de código de bytes Python en formato **PEP 3147**. Tenga en
   cuenta que el valor en "sys.implementation.cache_tag" es
   autoritario y debe usarse en lugar de esta función.

   Added in version 3.2.

PyObject *PyImport_GetModuleDict()
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Retorna el diccionario utilizado para la administración del módulo
   (también conocido como "sys.modules"). Tenga en cuenta que esta es
   una variable por intérprete.

PyObject *PyImport_GetModule(PyObject *name)
    *Return value: New reference.** Part of the Stable ABI since
   version 3.8.*

   Retorna el módulo ya importado con el nombre dado. Si el módulo aún
   no se ha importado, retorna "NULL" pero no establece un error.
   Retorna "NULL" y establece un error si falla la búsqueda.

   Added in version 3.7.

PyObject *PyImport_GetImporter(PyObject *path)
    *Return value: New reference.** Part of the Stable ABI.*

   Retorna un objeto buscador para un elemento *path*
   "sys.path"/"pkg.__path__", posiblemente obteniéndolo del
   diccionario "sys.path_importer_cache". Si aún no estaba en caché,
   atraviesa "sys.path_hooks" hasta que se encuentre un gancho
   (*hook*) que pueda manejar el elemento de ruta. Retorna "None" si
   ningún gancho (*hook*) podría; esto le dice a la persona que llama
   que *path based finder* no pudo encontrar un buscador para este
   elemento de ruta. Guarda en el resultado (caché) en
   "sys.path_importer_cache". Retorna una nueva referencia al objeto
   del buscador.

int PyImport_ImportFrozenModuleObject(PyObject *name)
    * Part of the Stable ABI since version 3.7.*

   Carga un módulo congelado llamado *name*. Retorna "1" para el
   éxito, "0" si no se encuentra el módulo y "-1" con una excepción
   establecida si falla la inicialización. Para acceder al módulo
   importado con una carga exitosa, use "PyImport_ImportModule()".
   (Tenga en cuenta el nombre inapropiado --- esta función volvería a
   cargar el módulo si ya se importó).

   Added in version 3.3.

   Distinto en la versión 3.4: El atributo "__file__" ya no está
   establecido en el módulo.

int PyImport_ImportFrozenModule(const char *name)
    * Part of the Stable ABI.*

   Similar a "PyImport_ImportFrozenModuleObject()", pero el nombre es
   una cadena de caracteres codificada UTF-8 en lugar de un objeto
   Unicode.

struct _frozen

   Esta es la definición del tipo de estructura para los descriptores
   de módulos congelados, según lo generado con la herramienta
   **freeze** (ver "Tools/freeze" en la distribución de código fuente
   de Python). Su definición, que se encuentra en "Include/import.h",
   es:

      struct _frozen {
          const char *name;
          const unsigned char *code;
          int size;
          bool is_package;
      };

   Distinto en la versión 3.11: El nuevo campo "is_package" indica si
   el módulo es un paquete o no. Esto sustituye a la configuración del
   campo "size" con un valor negativo.

const struct _frozen *PyImport_FrozenModules

   Este puntero se inicializa para apuntar a un arreglo de registros
   "_frozen", terminado por uno cuyos registros son todos "NULL" o
   cero. Cuando se importa un módulo congelado, se busca en esta
   tabla. El código de terceros podría jugar con esto para
   proporcionar una colección de módulos congelados creada
   dinámicamente.

int PyImport_AppendInittab(const char *name, PyObject *(*initfunc)(void))
    * Part of the Stable ABI.*

   Agrega un solo módulo a la tabla existente de módulos incorporados.
   Este es un contenedor conveniente "PyImport_ExtendInittab()", que
   retorna "-1" si la tabla no se puede extender. El nuevo módulo se
   puede importar con el nombre *name*, y utiliza la función
   *initfunc* como la función de inicialización llamada en el primer
   intento de importación. Esto debería llamarse antes de
   "Py_Initialize()".

struct _inittab

   Estructura que describe una sola entrada en la lista de módulos
   incorporados. Cada una de estas estructuras proporciona el nombre y
   la función de inicialización de un módulo incorporado en el
   intérprete. El nombre es una cadena de caracteres codificada ASCII.
   Los programas que incorporan Python pueden usar una matriz de estas
   estructuras junto con "PyImport_ExtendInittab()" para proporcionar
   módulos integrados adicionales. La estructura se define en
   "Include/import.h" como:

   const char *name

      El nombre del módulo, como una cadena codificada ASCII.

   PyObject *(*initfunc)(void)

      Función de inicialización para un módulo incorporado en el
      intérprete.

int PyImport_ExtendInittab(struct _inittab *newtab)

   Agrega una colección de módulos a la tabla de módulos integrados.
   El arreglo *newtab* debe terminar con una entrada centinela que
   contiene "NULL" para el campo "name"; Si no se proporciona el valor
   centinela, se puede producir un error de memoria. Retorna "0" en
   caso de éxito o "-1" si se puede asignar memoria insuficiente para
   ampliar la tabla interna. En caso de error, no se agregan módulos a
   la tabla interna. Esta función debe ser llamada antes de
   "Py_Initialize()".

   Si Python es inicializado múltiples veces, se debe llamar
   "PyImport_AppendInittab()" o "PyImport_ExtendInittab()" antes de
   cada inicialización de Python.

struct _inittab *PyImport_Inittab

   The table of built-in modules used by Python initialization. Do not
   use this directly; use "PyImport_AppendInittab()" and
   "PyImport_ExtendInittab()" instead.

PyObject *PyImport_ImportModuleAttr(PyObject *mod_name, PyObject *attr_name)
    *Return value: New reference.*

   Import the module *mod_name* and get its attribute *attr_name*.

   Names must be Python "str" objects.

   Helper function combining "PyImport_Import()" and
   "PyObject_GetAttr()". For example, it can raise "ImportError" if
   the module is not found, and "AttributeError" if the attribute
   doesn't exist.

   Added in version 3.14.

PyObject *PyImport_ImportModuleAttrString(const char *mod_name, const char *attr_name)
    *Return value: New reference.*

   Similar to "PyImport_ImportModuleAttr()", but names are UTF-8
   encoded strings instead of Python "str" objects.

   Added in version 3.14.
