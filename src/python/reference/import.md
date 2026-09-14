---
title: 5. El sistema de importación
source_url: https://docs.python.org/es/3
source_path: reference/import.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4800
---

# 5. El sistema de importación

El código Python en un *módulo* obtiene acceso al código en otro
módulo por el proceso de *importarlo*.  La instrucción "import" es la
forma más común de invocar la maquinaria de importación, pero no es la
única manera.  Funciones como "importlib.import_module()" y built-in
"__import__()" también se pueden utilizar para invocar la maquinaria
de importación.

La instrucción "import" combina dos operaciones; busca el módulo con
nombre y, a continuación, enlaza los resultados de esa búsqueda a un
nombre en el ámbito local.  La operación de búsqueda de la instrucción
"import" se define como una llamada a la función "__import__()", con
los argumentos adecuados. El valor retornado de "__import__()" se
utiliza para realizar la operación de enlace de nombre de la
instrucción "import".  Consulte la instrucción "import" para obtener
los detalles exactos de esa operación de enlace de nombres.

Una llamada directa a "__import__()" realiza solo la búsqueda del
módulo y, si se encuentra, la operación de creación del módulo.
Aunque pueden producirse ciertos efectos secundarios, como la
importación de paquetes primarios y la actualización de varias
memorias caché (incluidas "sys.modules"), solo la instrucción "import"
realiza una operación de enlace de nombres.

Cuando se ejecuta una instrucción "import", se llama a la función
estándar incorporada "__import__()". Otros mecanismos para invocar el
sistema de importación (como "importlib.import_module()") pueden optar
por omitir "__import__()" y utilizar sus propias soluciones para
implementar la semántica de importación.

Cuando se importa un módulo por primera vez, Python busca el módulo y,
si se encuentra, crea un objeto de módulo [1], inicializándolo.  Si no
se encuentra el módulo con nombre, se genera un "ModuleNotFoundError".
Python implementa varias estrategias para buscar el módulo con nombre
cuando se invoca la maquinaria de importación.  Estas estrategias se
pueden modificar y ampliar mediante el uso de varios ganchos descritos
en las secciones siguientes.

Distinto en la versión 3.3: El sistema de importación se ha
actualizado para aplicar plenamente la segunda fase de **PEP 302**. Ya
no hay ninguna maquinaria de importación implícita: todo el sistema de
importación se expone a través de "sys.meta_path". Además, se ha
implementado la compatibilidad con paquetes de espacio de nombres
nativos (consulte **PEP 420**).

## 5.1. "importlib"

El módulo "importlib" proporciona una API enriquecida para interactuar
con el sistema de importación.  Por ejemplo
"importlib.import_module()" proporciona una API recomendada y más
sencilla que la integrada "__import__()" para invocar la maquinaria de
importación.  Consulte la documentación de la biblioteca "importlib"
para obtener más detalles.

## 5.2. Paquetes

Python sólo tiene un tipo de objeto módulo, y todos los módulos son de
este tipo, independientemente de si el módulo está implementado en
Python, C, o en cualquier otro lenguaje.  Para ayudar a organizar los
módulos y proporcionar una jerarquía de nombres, Python tiene un
concepto de *paquete*.

Puedes pensar en los paquetes como los directorios de un sistema de
archivos y en los módulos como archivos dentro de los directorios,
pero no te tomes esta analogía demasiado literalmente, ya que los
paquetes y los módulos no tienen por qué originarse en el sistema de
archivos.  Para los propósitos de esta documentación, usaremos esta
conveniente analogía de directorios y archivos.  Al igual que los
directorios del sistema de archivos, los paquetes están organizados de
forma jerárquica, y los paquetes pueden contener subpaquetes, así como
módulos regulares.

Es importante tener en cuenta que todos los paquetes son módulos, pero
no todos los módulos son paquetes.  O dicho de otro modo, los paquetes
son sólo un tipo especial de módulo. Específicamente, cualquier módulo
que contenga un atributo "__path__" se considera un paquete.

Todos los módulos tienen un nombre. Los nombres de los subpaquetes
están separados de su nombre de paquete principal por un punto,
similar a la sintaxis de acceso de atributo estándar de Python. Por lo
tanto, podría tener un paquete llamado "email", que a su vez tiene un
subpaquete llamado "email.mime" y un módulo dentro de ese subpaquete
llamado "email.mime.text".

### 5.2.1. Paquetes regulares

Python define dos tipos de paquetes, *paquetes regulares* y *paquetes
de espacio de nombres*.  Los paquetes regulares son los paquetes
tradicionales tal y como existían en Python 3.2 y anteriores. Un
paquete regular se implementa típicamente como un directorio que
contiene un archivo "init__.py".  Cuando se importa un paquete
regular, este archivo "__init__.py" se ejecuta implícitamente, y los
objetos que define están vinculados a nombres en el espacio de nombres
del paquete.  El archivo "__init__.py" puede contener el mismo código
Python que puede contener cualquier otro módulo, y Python añadirá
algunos atributos adicionales al módulo cuando se importe.

Por ejemplo, la siguiente disposición del sistema de archivos define
un paquete "parent" de nivel superior con tres subpaquetes:

   parent/
       __init__.py
       one/
           __init__.py
       two/
           __init__.py
       three/
           __init__.py

Importando "parent.one" se ejecutará implícitamente
"parent/__init__.py" y "parent/one/__init__.py".  La importación
posterior de "parent.two" o "parent.three" ejecutará
"parent/two/__init__.py" y "parent/three/__init__.py" respectivamente.

A subdirectory inside a regular package that does not contain an
"__init__.py" file is treated as an implicit namespace package (a
"namespace subpackage") rooted in that parent.  See **PEP 420** for
the underlying specification.

### 5.2.2. Paquetes de espacio de nombres

Un paquete de espacio de nombres es un compuesto de varias
*porciones*, donde cada porción contribuye con un subpaquete al
paquete padre.  Las porciones pueden residir en diferentes lugares del
sistema de archivos.  Las porciones también pueden encontrarse en
archivos zip, en la red, o en cualquier otro lugar que Python busque
durante la importación.  Los paquetes de espacios de nombres pueden
corresponder o no directamente a objetos del sistema de archivos;
pueden ser módulos virtuales que no tienen una representación
concreta.

Los paquetes de espacios de nombres no usan una lista ordinaria para
su atributo "__path__". En su lugar utilizan un tipo iterable
personalizado que realizará automáticamente una nueva búsqueda de
porciones de paquete en el siguiente intento de importación dentro de
ese paquete si la ruta de su paquete padre (o "sys.path`" para un
paquete de nivel superior) cambia.

Con los paquetes de espacio de nombres, no hay ningún archivo
"parent/__init__.py".  De hecho, puede haber varios directorios
"padre" encontrados durante la búsqueda de importación, donde cada uno
de ellos es proporcionado por una parte diferente.  Por lo tanto,
"padre/one" no puede estar físicamente situado junto a "padre/two".
En este caso, Python creará un paquete de espacio de nombres para el
paquete "parent" de nivel superior siempre que se importe él o uno de
sus subpaquetes.

Namespace packages may also be nested inside a regular package.  When
the import system searches a regular package's "__path__" and
encounters a subdirectory that does not contain an "__init__.py" file,
that subdirectory becomes a *portion* contributing to a namespace
subpackage of the enclosing regular package.

Consulte también **PEP 420** para conocer la especificación del
paquete de espacio de nombres.

## 5.3. Buscando

Para comenzar la búsqueda, Python necesita el nombre *totalmente
calificado* del módulo (o paquete, pero para los fines de esta
discusión, la diferencia es irrelevante) que se está importando.  Este
nombre puede provenir de varios argumentos a la instrucción "import",
o de los parámetros de las funciones "importlib.import_module()" o
"__import__()".

Este nombre se utilizará en varias fases de la búsqueda de
importación, y puede ser la ruta de acceso punteada a un submódulo,
por ejemplo, "foo.bar.baz".  En este caso, Python primero intenta
importar "foo", luego "foo.bar", y finalmente "foo.bar.baz". Si se
produce un error en cualquiera de las importaciones intermedias, se
genera un "ModuleNotFoundError".

### 5.3.1. La caché del módulo

El primer lugar comprobado durante la búsqueda de importación es
"sys.modules".  Esta asignación sirve como caché de todos los módulos
que se han importado previamente, incluidas las rutas intermedias.
Por lo tanto, si "foo.bar.baz" se importó previamente, "sys.modules"
contendrá entradas para "foo", "foo.bar", y "foo.bar.baz".  Cada clave
tendrá como valor el objeto de módulo correspondiente.

Durante la importación, el nombre del módulo se busca en "sys.modules"
y si está presente, el valor asociado es el módulo que satisface la
importación y el proceso se completa.  Sin embargo, si el valor es
"None", se genera un "ModuleNotFoundError".  Si falta el nombre del
módulo, Python continuará buscando el módulo.

"sys.modules" se puede escribir.  La eliminación de una clave no puede
destruir el módulo asociado (ya que otros módulos pueden contener
referencias a él), pero invalidará la entrada de caché para el módulo
con nombre, lo que hará que Python busque de nuevo el módulo con
nombre en su próxima importación. La clave también se puede asignar a
"None", lo que obliga a la siguiente importación del módulo a dar como
resultado un "ModuleNotFoundError".

Tenga cuidado, sin embargo, como si mantiene una referencia al objeto
module, invalide su entrada de caché en "sys.modules" y, a
continuación, vuelva a importar el módulo con nombre, los dos objetos
de módulo *no* serán los mismos. Por el contrario,
"importlib.reload()" reutilizará el objeto de módulo *same* y
simplemente reinicializará el contenido del módulo volviendo a
ejecutar el código del módulo.

### 5.3.2. Buscadores y cargadores

Si el módulo con nombre no se encuentra en "sys.modules", se invoca el
protocolo de importación de Python para buscar y cargar el módulo.
Este protocolo consta de dos objetos conceptuales, *buscadores* y
*cargadores*. El trabajo de un buscador es determinar si puede
encontrar el módulo con nombre utilizando cualquier estrategia que
conozca. Los objetos que implementan ambas interfaces se conocen como
*importadores* se retornan a sí mismos cuando descubren que pueden
cargar el módulo solicitado.

Python incluye una serie de buscadores e importadores predeterminados.
El primero sabe cómo localizar módulos integrados, y el segundo sabe
cómo localizar módulos congelados.  Un tercer buscador predeterminado
busca módulos en *import path*.  El *import path* es una lista de
ubicaciones que pueden nombrar rutas del sistema de archivos o
archivos zip.  También se puede ampliar para buscar cualquier recurso
localizable, como los identificados por las direcciones URL.

La maquinaria de importación es extensible, por lo que se pueden
añadir nuevos buscadores para ampliar el alcance y el alcance de la
búsqueda de módulos.

En realidad, los buscadores no cargan módulos.  Si pueden encontrar el
módulo con nombre, retornan un *module spec*, una encapsulación de la
información relacionada con la importación del módulo, que la
maquinaria de importación utiliza al cargar el módulo.

En las secciones siguientes se describe el protocolo para buscadores y
cargadores con más detalle, incluido cómo puede crear y registrar
otros nuevos para ampliar la maquinaria de importación.

Distinto en la versión 3.4: En versiones anteriores de Python, los
buscadores retornaban *cargadores* directamente, mientras que ahora
retornen especificaciones de módulo que *contienen* cargadores. Los
cargadores todavía se utilizan durante la importación, pero tienen
menos responsabilidades.

### 5.3.3. Ganchos de importación

La maquinaria de importación está diseñada para ser extensible; el
mecanismo principal para esto son los *ganchos de importación* (import
hooks).  Hay dos tipos de ganchos de importación: *meta hooks* (meta
ganchos) y *import path hooks* (ganchos de ruta de acceso de
importación).

Los meta ganchos se llaman al inicio del procesamiento de importación,
antes de que se haya producido cualquier otro procesamiento de
importación, que no sea búsqueda de caché de "sys.modules". Esto
permite que los metaganchos reemplacen el procesamiento de "sys.path",
módulos congelados o incluso módulos integrados.  Los meta ganchos se
registran agregando nuevos objetos de buscador a "sys.meta_path", como
se describe a continuación.

Los ganchos de ruta de acceso de importación se invocan como parte del
procesamiento "sys.path" (o "package.__path__"), en el punto donde se
encuentra su elemento de ruta de acceso asociado. Los ganchos de ruta
de acceso de importación se registran agregando nuevos invocables a
"sys.path_hooks" como se describe a continuación.

### 5.3.4. La meta ruta (*path*)

When the named module is not found in "sys.modules", Python next
searches "sys.meta_path", which contains a list of meta path finder
objects.  These finders are queried in order to see if they know how
to handle the named module.  Meta path finders must implement a method
called "find_spec()" which takes three arguments: a name, an import
path, and (optionally) a target module.  The meta path finder can use
any strategy it wants to determine whether it can handle the named
module or not.

Si el buscador de metarutas sabe cómo controlar el módulo con nombre,
retorna un objeto de especificación.  Si no puede controlar el módulo
con nombre, retorna "None".  Si el procesamiento de "sys.meta_path"
llega al final de su lista sin retornar una especificación, se genera
un "ModuleNotFoundError".  Cualquier otra excepción provocada
simplemente se propaga hacia arriba, anulando el proceso de
importación.

The "find_spec()" method of meta path finders is called with two or
three arguments.  The first is the fully qualified name of the module
being imported, for example "foo.bar.baz". The second argument is the
path entries to use for the module search.  For top-level modules, the
second argument is "None", but for submodules or subpackages, the
second argument is the value of the parent package's "__path__"
attribute. If the appropriate "__path__" attribute cannot be accessed,
a "ModuleNotFoundError" is raised.  The third argument is an existing
module object that will be the target of loading later. The import
system passes in a target module only during reload.

La metaruta se puede recorrer varias veces para una sola solicitud de
importación. Por ejemplo, suponiendo que ninguno de los módulos
implicados ya se haya almacenado en caché, la importación de
"foo.bar.baz" realizará primero una importación de nivel superior,
llamando a "mpf.find_spec("foo", None, None)" en cada buscador de
metarutas ("mpf"). Después de importar "foo" , "foo.bar" se importará
atravesando la meta ruta por segunda vez, llamando a
"mpf.find_spec("foo.bar", foo.__path__, None)". Una vez importado
"foo.bar", el recorrido final llamará a "mpf.find_spec("foo.bar.baz",
foo.bar.__path__, None)".

Algunos buscadores de metarutas solo admiten importaciones de nivel
superior. Estos importadores siempre retornarán "None" cuando se pase
algo distinto de "None" como segundo argumento.

El valor predeterminado de Python "sys.meta_path" tiene tres
buscadores de metarutas, uno que sabe cómo importar módulos
integrados, uno que sabe cómo importar módulos congelados y otro que
sabe cómo importar módulos desde un *import path* (es decir, el *path
based finder*).

Distinto en la versión 3.4: The "find_spec()" method of meta path
finders replaced "find_module()", which is now deprecated.  While it
will continue to work without change, the import machinery will try it
only if the finder does not implement "find_spec()".

Distinto en la versión 3.10: Use of "find_module()" by the import
system now raises "ImportWarning".

Distinto en la versión 3.12: "find_module()" has been removed. Use
"find_spec()" instead.

## 5.4. Cargando

Si se encuentra una especificación de módulo, la maquinaria de
importación la utilizará (y el cargador que contiene) al cargar el
módulo.  Aquí está una aproximación de lo que sucede durante la
porción de carga de la importación:

   module = None
   if spec.loader is not None and hasattr(spec.loader, 'create_module'):
       # It is assumed 'exec_module' will also be defined on the loader.
       module = spec.loader.create_module(spec)
   if module is None:
       module = ModuleType(spec.name)
   # The import-related module attributes get set here:
   _init_module_attrs(spec, module)

   if spec.loader is None:
       # unsupported
       raise ImportError
   if spec.origin is None and spec.submodule_search_locations is not None:
       # namespace package
       sys.modules[spec.name] = module
   elif not hasattr(spec.loader, 'exec_module'):
       module = spec.loader.load_module(spec.name)
   else:
       sys.modules[spec.name] = module
       try:
           spec.loader.exec_module(module)
       except BaseException:
           try:
               del sys.modules[spec.name]
           except KeyError:
               pass
           raise
   return sys.modules[spec.name]

Tenga en cuenta los siguientes detalles:

* Si hay un objeto de módulo existente con el nombre dado en
  "sys.modules", la importación ya lo habrá retornado.

* El módulo existirá en "sys.modules" antes de que el cargador ejecute
  el código del módulo.  Esto es crucial porque el código del módulo
  puede (directa o indirectamente) importarse a sí mismo; agregándolo
  a "sys.modules" de antemano evita la recursividad sin límites en el
  peor de los casos y la carga múltiple en el mejor.

* Si se produce un error en la carga, el módulo con errores -- y solo
  el módulo con errores -- se elimina de "sys.modules".  Cualquier
  módulo que ya esté en la caché de "sys.modules" y cualquier módulo
  que se haya cargado correctamente como efecto secundario, debe
  permanecer en la memoria caché.  Esto contrasta con la recarga donde
  incluso el módulo que falla se deja en "sys.modules".

* Después de crear el módulo pero antes de la ejecución, la maquinaria
  de importación establece los atributos del módulo relacionados con
  la importación ("_init_module_attrs" en el ejemplo de pseudocódigo
  anterior), como se resume en una sección posterior.

* La ejecución del módulo es el momento clave de la carga en el que se
  rellena el espacio de nombres del módulo.  La ejecución se delega
  por completo en el cargador, lo que llega a decidir qué se rellena y
  cómo.

* El módulo creado durante la carga y pasado a exec_module() puede no
  ser el que se retorna al final de la importación [2].

Distinto en la versión 3.4: El sistema de importación se ha hecho
cargo de las responsabilidades reutilizables de los cargadores.  Estos
fueron realizados previamente por el método
"importlib.abc.Loader.load_module()".

### 5.4.1. Cargadores

Los cargadores de módulos proporcionan la función crítica de carga:
ejecución del módulo. La maquinaria de importación llama al método
"importlib.abc.Loader.exec_module()" con un único argumento, el objeto
module que se va a ejecutar.  Se omite cualquier valor retornado de
"exec_module()".

Los cargadores deben cumplir los siguientes requisitos:

* Si el módulo es un módulo Python (a diferencia de un módulo
  integrado o una extensión cargada dinámicamente), el cargador debe
  ejecutar el código del módulo en el espacio de nombres global del
  módulo ("module.__dict__").

* Si el cargador no puede ejecutar el módulo, debe generar un
  "ImportError", aunque se propagará cualquier otra excepción
  provocada durante "exec_module()".

En muchos casos, el buscador y el cargador pueden ser el mismo objeto;
en tales casos, el método "find_spec()" simplemente retornaría una
especificación con el cargador establecido en "self".

Los cargadores de módulos pueden optar por crear el objeto de módulo
durante la carga mediante la implementación de un método
"create_module()". Toma un argumento, la especificación del módulo, y
retorna el nuevo objeto de módulo que se usará durante la carga.
"create_module()" no necesita establecer ningún atributo en el objeto
module.  Si el método retorna "None", la maquinaria de importación
creará el nuevo módulo en sí.

Added in version 3.4: El método de cargadores "create_module()".

Distinto en la versión 3.4: El método "load_module()" fue reemplazado
por "exec_module()" y la maquinaria de importación asumió todas las
responsabilidades reutilizables de la carga.Para la compatibilidad con
los cargadores existentes, la maquinaria de importación utilizará el
método de cargadores "load_module()" si existe y el cargador no
implementa también "exec_module()".  Sin embargo, "load_module()" ha
quedado obsoleto y los cargadores deben implementar "exec_module()" en
su lugar.El método "load_module()" debe implementar toda la
funcionalidad de carga reutilizable descrita anteriormente, además de
ejecutar el módulo.  Se aplican todas las mismas restricciones, con
algunas aclaraciones adicionales:

* Si hay un objeto de módulo existente con el nombre dado en
  "sys.modules", el cargador debe utilizar ese módulo existente. (De
  lo contrario, "importlib.reload()" no funcionará correctamente.)  Si
  el módulo con nombre no existe en "sys.modules", el cargador debe
  crear un nuevo objeto de módulo y agregarlo a "sys.modules".

* El módulo *debe* existir en "sys.modules" antes de que el cargador
  ejecute el código del módulo, para evitar la recursividad sin
  límites o la carga múltiple.

* Si se produce un error en la carga, el cargador debe quitar los
  módulos que ha insertado en "sys.modules", pero debe quitar **solo**
  los módulos con errores, y solo si el propio cargador ha cargado los
  módulos explícitamente.

Distinto en la versión 3.5: A "DeprecationWarning" se genera cuando se
define "exec_module()" pero "create_module()" no lo es.

Distinto en la versión 3.6: Un "ImportError" se genera cuando
"exec_module()" está definido, pero "create_module()" no lo es.

Distinto en la versión 3.10: El uso de "load_module()" lanzará
"ImportWarning".

### 5.4.2. Submódulos

Cuando se carga un submódulo mediante cualquier mecanismo (por
ejemplo, API "importlib", las instrucciones "import" o "import-from",
o "__import__()") integradas, se coloca un enlace en el espacio de
nombres del módulo primario al objeto submodule. Por ejemplo, si el
paquete "spam" tiene un submódulo "foo", después de importar
"spam.foo", "spam" tendrá un atributo "foo" que está enlazado al
submódulo.  Supongamos que tiene la siguiente estructura de
directorios:

   spam/
       __init__.py
       foo.py

y "spam/__init__.py" tiene la siguiente línea:

   from .foo import Foo

a continuación, la ejecución de lo siguiente pone un nombre vinculante
para "foo" y "Foo" en el módulo "spam":

   >>> import spam
   >>> spam.foo
   <module 'spam.foo' from '/tmp/imports/spam/foo.py'>
   >>> spam.Foo
   <class 'spam.foo.Foo'>

Dadas las reglas de enlace de nombres familiares de Python, esto puede
parecer sorprendente, pero en realidad es una característica
fundamental del sistema de importación.  La retención invariable es
que si tiene "sys.modules[`spam`]" y "sys.modules[`spam.foo`]" (como
lo haría después de la importación anterior), este último debe
aparecer como el atributo "foo" de la primera.

### 5.4.3. Module specs

La maquinaria de importación utiliza una variedad de información sobre
cada módulo durante la importación, especialmente antes de la carga.
La mayor parte de la información es común a todos los módulos.  El
propósito de las especificaciones de un módulo es encapsular esta
información relacionada con la importación por módulo.

El uso de una especificación durante la importación permite transferir
el estado entre los componentes del sistema de importación, por
ejemplo, entre el buscador que crea la especificación del módulo y el
cargador que la ejecuta.  Lo más importante es que permite a la
maquinaria de importación realizar las operaciones de caldera de
carga, mientras que sin una especificación de módulo el cargador tenía
esa responsabilidad.

The module's spec is exposed as "module.__spec__". Setting "__spec__"
appropriately applies equally to modules initialized during
interpreter startup. The one exception is "__main__", where "__spec__"
is set to None in some cases.

See "ModuleSpec" for details on the contents of the module spec.

Added in version 3.4.

### 5.4.4. __path__ attributes on modules

The "__path__" attribute should be a (possibly empty) *sequence* of
strings enumerating the locations where the package's submodules will
be found. By definition, if a module has a "__path__" attribute, it is
a *package*.

A package's "__path__" attribute is used during imports of its
subpackages. Within the import machinery, it functions much the same
as "sys.path", i.e. providing a list of locations to search for
modules during import. However, "__path__" is typically much more
constrained than "sys.path".

The same rules used for "sys.path" also apply to a package's
"__path__". "sys.path_hooks" (described below) are consulted when
traversing a package's "__path__".

A package's "__init__.py" file may set or alter the package's
"__path__" attribute, and this was typically the way namespace
packages were implemented prior to **PEP 420**.  With the adoption of
**PEP 420**, namespace packages no longer need to supply "__init__.py"
files containing only "__path__" manipulation code; the import
machinery automatically sets "__path__" correctly for the namespace
package.

### 5.4.5. Representación (*Reprs*) de módulos

De forma predeterminada, todos los módulos tienen un repr utilizable,
sin embargo, dependiendo de los atributos establecidos anteriormente,
y en las especificaciones del módulo, puede controlar más
explícitamente el repr de los objetos de módulo.

Si el módulo tiene una especificación ("__spec__"), la maquinaria de
importación intentará generar un repr a partir de él.  Si eso falla o
no hay ninguna especificación, el sistema de importación creará un
repr predeterminado usando cualquier información disponible en el
módulo.  Intentará utilizar el "module.__name__", "module.__file__" y
"module.__loader__" como entrada en el repr, con valores
predeterminados para cualquier información que falte.

Aquí están las reglas exactas utilizadas:

* Si el módulo tiene un atributo "__spec__", la información de la
  especificación se utiliza para generar el repr.  Se consultan los
  atributos "name", "loader", "origin" y "has_location".

* Si el módulo tiene un atributo "__file__", se utiliza como parte del
  repr del módulo.

* Si el módulo no tiene "__file__" pero tiene un "__loader__" que no
  es "None", entonces el repr del cargador se utiliza como parte del
  repr del módulo.

* De lo contrario, sólo tiene que utilizar el "__name__" del módulo en
  el repr.

Distinto en la versión 3.12: El uso de "module_repr()", al ser
obsoleto desde Python 3.4, fue eliminado en Python 3.12 y no es
llamado durante la resolución de la representación (repr) de un
módulo.

### 5.4.6. Invalidación del código de bytes en caché

Antes de que Python cargue el código de bytes en caché de un archivo
".pyc", verifica si el caché está actualizado con el archivo ".py" de
origen. De forma predeterminada, Python hace esto almacenando la marca
de tiempo y el tamaño de la última modificación de la fuente en el
archivo de caché al escribirlo. En tiempo de ejecución, el sistema de
importación valida el archivo de caché comprobando los metadatos
almacenados en el archivo de caché con los metadatos de la fuente.

Python también admite archivos de caché "basados en hash", que
almacenan un hash del contenido del archivo de origen en lugar de sus
metadatos. Hay dos variantes de archivos ".pyc" basados en hash:
marcados y desmarcados. Para los archivos ".pyc" marcados basados en
hash, Python valida el archivo de caché mediante el hash del archivo
de origen y la comparación del hash resultante con el hash en el
archivo de caché. Si se encuentra que un archivo de caché basado en
hash comprobado no es válido, Python lo regenera y escribe un nuevo
archivo de caché basado en hash comprobado. Para los archivos ".pyc"
sin marcar en hash, Python simplemente asume que el archivo de caché
es válido si existe. El comportamiento de validación de archivos
basado en hash ".pyc" se puede invalidar con el indicador "--check-
hash-based-pycs".

Distinto en la versión 3.7: Se han añadido archivos ".pyc" basados en
hash. Anteriormente, Python solo admitía la invalidación basada en la
marca de tiempo de la caché del código de bytes.

## 5.5. El buscador basado en rutas

Como se mencionó anteriormente, Python viene con varios buscadores de
meta rutas predeterminados. Uno de ellos, llamado el buscador *path
based finder* ("PathFinder"), busca una *import path*, que contiene
una lista de *entradas de ruta*. Cada entrada de ruta de acceso nombra
una ubicación para buscar módulos.

El buscador basado en rutas en sí no sabe cómo importar nada. En su
lugar, atraviesa las entradas de ruta individuales, asociando cada una
de ellas con un buscador de entrada de ruta que sabe cómo manejar ese
tipo particular de ruta de acceso.

El conjunto predeterminado de buscadores de entradas de ruta
implementa toda la semántica para encontrar módulos en el sistema de
archivos, controlando tipos de archivos especiales como el código
fuente de Python (archivos "`.py"), el código de bytes de Python
(archivos ".pyc") y las bibliotecas compartidas (por ejemplo, archivos
".so`"). Cuando es compatible con el módulo "zipimport" en la
biblioteca estándar, los buscadores de entradas de ruta de acceso
predeterminados también controlan la carga de todos estos tipos de
archivo (excepto las bibliotecas compartidas) desde zipfiles.

Las entradas de ruta de acceso no deben limitarse a las ubicaciones
del sistema de archivos.  Pueden hacer referencia a direcciones URL,
consultas de base de datos o cualquier otra ubicación que se pueda
especificar como una cadena.

El buscador basado en rutas proporciona enlaces y protocolos
adicionales para que pueda ampliar y personalizar los tipos de
entradas de ruta de acceso que se pueden buscar.  Por ejemplo, si
desea admitir entradas de ruta de acceso como direcciones URL de red,
podría escribir un enlace que implemente la semántica HTTP para buscar
módulos en la web.  Este gancho (un al que se puede llamar) retornaría
un *path entry finder* compatible con el protocolo descrito a
continuación, que luego se utilizó para obtener un cargador para el
módulo de la web.

Una palabra de advertencia: esta sección y la anterior utilizan el
término *finder*, distinguiendo entre ellos utilizando los términos
*meta path finder* y *path entry finder*.  Estos dos tipos de
buscadores son muy similares, admiten protocolos similares y funcionan
de maneras similares durante el proceso de importación, pero es
importante tener en cuenta que son sutilmente diferentes. En
particular, los buscadores de meta path operan al principio del
proceso de importación, como se indica en el recorrido
"sys.meta_path".

Por el contrario, los buscadores de entradas de ruta son en cierto
sentido un detalle de implementación del buscador basado en rutas y,
de hecho, si el buscador basado en rutas se eliminara de
"sys.meta_path", no se invocaría ninguna semántica del buscador de
entradas de ruta.

### 5.5.1. Buscadores de entradas de ruta

El *path based finder* es responsable de encontrar y cargar módulos y
paquetes de Python cuya ubicación se especifica con una cadena *path
entry*.  La mayoría de las ubicaciones de nombres de entradas de ruta
de acceso en el sistema de archivos, pero no es necesario limitarlas a
esto.

Como buscador de meta rutas, el buscador *path based finder*
implementa el protocolo "find_spec()" descrito anteriormente, sin
embargo, expone enlaces adicionales que se pueden usar para
personalizar cómo se encuentran y cargan los módulos desde la ruta
*import path*.

Tres variables son usadas por *path based finder*, "sys.path",
"sys.path_hooks" y "sys.path_importer_cache".  También se utilizan los
atributos "__path__" en los objetos de paquete.  Estos proporcionan
formas adicionales de personalizar la maquinaria de importación.

"sys.path" contains a list of strings providing search locations for
modules and packages.  It is initialized from the "PYTHONPATH"
environment variable and various other installation- and
implementation-specific defaults.  Entries in "sys.path" can name
directories on the file system, zip files, and potentially other
"locations" (see the "site" module) that should be searched for
modules, such as URLs, or database queries.  Only strings should be
present on "sys.path"; all other data types are ignored.

El buscador *path based finder* es un *meta path finder*, por lo que
la maquinaria de importación comienza la búsqueda *import path*
llamando al método "find_spec()" basado en la ruta de acceso, tal como
se describió anteriormente.  Cuando se proporciona el argumento "path"
a "find_spec()", será una lista de rutas de acceso de cadena para
recorrer - normalmente el atributo "__path__" de un paquete para una
importación dentro de ese paquete.  Si el argumento "path" es "None",
esto indica una importación de nivel superior y se utiliza "sys.path".

The path based finder iterates over every entry in the search path,
and for each of these, looks for an appropriate *path entry finder*
("PathEntryFinder") for the path entry.  Because this can be an
expensive operation (e.g. there may be "stat()" call overheads for
this search), the path based finder maintains a cache mapping path
entries to path entry finders.  This cache is maintained in
"sys.path_importer_cache" (despite the name, this cache actually
stores finder objects rather than being limited to *importer*
objects). In this way, the expensive search for a particular *path
entry* location's *path entry finder* need only be done once.  User
code is free to remove cache entries from "sys.path_importer_cache"
forcing the path based finder to perform the path entry search again.

Si la entrada de ruta de acceso no está presente en la memoria caché,
el buscador basado en rutas de acceso recorre en iteración cada
llamada que se puede llamar en "sys.path_hooks".  Cada uno de los
enlaces de *ganchos de rutas de entrada* en esta lista se llama con un
solo argumento, la entrada de ruta de acceso que se va a buscar.  Esta
invocable puede retornar un *path entry finder* que puede controlar la
entrada de ruta de acceso, o puede generar "ImportError".  Un
"ImportError" es utilizado por el buscador basado en ruta para indicar
que el gancho no puede encontrar un *path entry finder* para eso
*entrada de ruta*.  Se omite la excepción y la iteración *import path*
continúa.  El enlace debe esperar un objeto de rutas o bytes; la
codificación de objetos bytes está hasta el enlace (por ejemplo, puede
ser una codificación del sistema de archivos, UTF-8, o algo más), y si
el gancho no puede decodificar el argumento, debe generar
"ImportError".

Si la iteración "sys.path_hooks" termina sin que se retorne ningún
valor *path entry finder*, a continuación, el método de búsqueda
basado en la ruta de acceso "find_spec()" almacenará "None" en
"sys.path_importer_cache" (para indicar que no hay ningún buscador
para esta entrada de ruta) y retornará "None", lo que indica que este
*meta path finder* no pudo encontrar el módulo.

Si un *path entry finder* *is* retornado por uno de los *path entry
hook* invocables en "sys.path_hooks", entonces el siguiente protocolo
se utiliza para pedir al buscador una especificación de módulo, que
luego se utiliza al cargar el módulo.

The current working directory -- denoted by an empty string -- is
handled slightly differently from other entries on "sys.path". First,
if the current working directory cannot be determined or is found not
to exist, no value is stored in "sys.path_importer_cache". Second, the
value for the current working directory is looked up fresh for each
module lookup. Third, the path used for "sys.path_importer_cache" and
returned by "importlib.machinery.PathFinder.find_spec()" will be the
actual current working directory and not the empty string.

### 5.5.2. Buscadores de entradas de ruta

Para admitir las importaciones de módulos y paquetes inicializados y
también para contribuir con partes a paquetes de espacio de nombres,
los buscadores de entradas de ruta de acceso deben implementar el
método "importlib.abc.PathEntryFinder.find_spec()".

"importlib.abc.PathEntryFinder.find_spec`()" toma dos argumentos: el
nombre completo del módulo que se va a importar y el módulo de destino
(opcional).  "find_spec()" retorna una especificación completamente
poblada para el módulo. Esta especificación siempre tendrá "cargador"
establecido (con una excepción).

To indicate to the import machinery that the spec represents a
namespace *portion*, the path entry finder sets
"submodule_search_locations" to a list containing the portion.

Distinto en la versión 3.4: "find_spec()" replaced "find_loader()" and
"find_module()", both of which are now deprecated, but will be used if
"find_spec()" is not defined.Los buscadores de entradas de ruta más
antiguos pueden implementar uno de estos dos métodos en desuso en
lugar de "find_spec()".  Los métodos todavía se respetan en aras de la
compatibilidad con versiones anteriores.  Sin embargo, si
"find_spec()" se implementa en el buscador de entrada de ruta, se
omiten los métodos heredados."find_loader()" takes one argument, the
fully qualified name of the module being imported.  "find_loader()"
returns a 2-tuple where the first item is the loader and the second
item is a namespace *portion*.Para la compatibilidad con versiones
anteriores con otras implementaciones del protocolo de importación,
muchos buscadores de entradas de ruta de acceso también admiten el
mismo método tradicional "find_module()" que admiten los buscadores de
rutas de acceso meta. Sin embargo, nunca se llama a los métodos del
buscador de entradas de ruta "find_module()" con un argumento "path"
(se espera que registren la información de ruta adecuada desde la
llamada inicial al enlace de ruta).El método "find_module()" en los
buscadores de entrada de ruta está en desuso, ya que no permite que el
buscador de entradas de ruta de acceso aporte partes a paquetes de
espacio de nombres.  Si existen tanto "find_loader()" como
"find_module()" en un buscador de entrada de ruta, el sistema de
importación siempre llamará a "find_loader()" en lugar de
"find_module()".

Distinto en la versión 3.10: Calls to "find_module()" and
"find_loader()" by the import system will raise "ImportWarning".

Distinto en la versión 3.12: Los métodos "find_module()" y
"find_loader()" fueron eliminados.

## 5.6. Reemplazando el sistema de importación estándar

El mecanismo más confiable para reemplazar todo el sistema de
importación es eliminar el contenido predeterminado de
"sys.meta_path", sustituyéndolos por completo por un enlace de meta
path personalizado.

If it is acceptable to only alter the behaviour of import statements
without affecting other APIs that access the import system, then
replacing the builtin "__import__()" function may be sufficient.

Para evitar selectivamente la importación de algunos módulos de un
enlace al principio de la meta path (en lugar de deshabilitar
completamente el sistema de importación estándar), es suficiente
elevar "ModuleNotFoundError" directamente desde "find_spec()" en lugar
de retornar "None". Este último indica que la búsqueda de meta path
debe continuar, mientras que la generación de una excepción termina
inmediatamente.

## 5.7. Paquete Importaciones relativas

Las importaciones relativas utilizan puntos iniciales. Un único punto
inicial indica una importación relativa, empezando por el paquete
actual. Dos o más puntos iniciales indican una importación relativa a
los elementos primarios del paquete actual, un nivel por punto después
del primero. Por ejemplo, dado el siguiente diseño de paquete:

   package/
       __init__.py
       subpackage1/
           __init__.py
           moduleX.py
           moduleY.py
       subpackage2/
           __init__.py
           moduleZ.py
       moduleA.py

En "subpackage1/moduleX.py" o "subpackage1/__init__.py", las
siguientes son importaciones relativas válidas:

   from .moduleY import spam
   from .moduleY import spam as ham
   from . import moduleY
   from ..subpackage1 import moduleY
   from ..subpackage2.moduleZ import eggs
   from ..moduleA import foo

Las importaciones absolutas pueden utilizar la sintaxis "import <>" o
"from <> import <>", pero las importaciones relativas solo pueden usar
el segundo formulario; la razón de esto es que:

   import XXX.YYY.ZZZ

debe exponer "XXX. Yyy. ZZZ" como una expresión utilizable, pero
.moduleY no es una expresión válida.

## 5.8. Consideraciones especiales para __main__

El módulo "__main__" es un caso especial relativo al sistema de
importación de Python. Como se señaló elsewhere, el módulo "__main__"
se inicializa directamente al inicio del intérprete, al igual que
"sys" y "builtins". Sin embargo, a diferencia de esos dos, no califica
estrictamente como un módulo integrado. Esto se debe a que la forma en
que se inicializa "__main__" depende de las marcas y otras opciones
con las que se invoca el intérprete.

### 5.8.1. __main__.__spec__

Dependiendo de cómo se inicializa "__main__", "__main__.__spec__" se
establece correctamente o en "None".

Cuando Python se inicia con la opción "-m", "__spec__" se establece en
la especificación de módulo del módulo o paquete correspondiente.
"__spec__" también se rellena cuando el módulo "__main__" se carga
como parte de la ejecución de un directorio, zipfile u otro "sys.path"
entrada.

En los casos restantes "__main__.__spec__" se establece en "None", ya
que el código utilizado para rellenar el "__main__" no se corresponde
directamente con un módulo importable:

* mensaje interactivo

* opción "-c"

* ejecutando desde stdin

* que se ejecuta directamente desde un archivo de código fuente o de
  código de bytes

Tenga en cuenta que "__main__.__spec__" siempre es "None" en el último
caso, *incluso si* el archivo técnicamente podría importarse
directamente como un módulo en su lugar. Utilice el modificador "-m"
si se desean metadatos de módulo válidos en "__main__".

Tenga en cuenta también que incluso cuando "__main__" corresponde a un
módulo importable y "__main__.__spec__" se establece en consecuencia,
todavía se consideran módulos *distinct*. Esto se debe al hecho de que
los bloques protegidos por las comprobaciones "if __name__ ==
"__main__":" solo se ejecutan cuando el módulo se utiliza para
rellenar el espacio de nombres "__main__", y no durante la importación
normal.

## 5.9. Referencias

La maquinaria de importación ha evolucionado considerablemente desde
los primeros días de Python.  La especificación original para paquetes
todavía está disponible para leer, aunque algunos detalles han
cambiado desde la escritura de ese documento.

La especificación original de "sys.meta_path" era **PEP 302**, con
posterior extensión en **PEP 420**.

**PEP 420** introduced *namespace packages* for Python 3.3.  **PEP
420** also introduced the "find_loader()" protocol as an alternative
to "find_module()".

**PEP 366** describe la adición del atributo "__package__" para las
importaciones relativas explícitas en los módulos principales.

**PEP 328** introdujo importaciones relativas absolutas y explícitas e
inicialmente propuestas "__name__" para la semántica **PEP 366**
eventualmente especificaría para "__package__".

**PEP 338** define la ejecución de módulos como scripts.

**PEP 451** agrega la encapsulación del estado de importación por
módulo en los objetos de especificación. También descargara la mayoría
de las responsabilidades de los cargadores en la maquinaria de
importación. Estos cambios permiten el desuso de varias API en el
sistema de importación y también la adición de nuevos métodos a los
buscadores y cargadores.

-[ Notas al Pie de Pagina ]-

[1] Véase "types. ModuleType".

[2] La implementación de importlib evita usar el valor retornado
    directamente. En su lugar, obtiene el objeto module buscando el
    nombre del módulo en "sys.modules".  El efecto indirecto de esto
    es que un módulo importado puede sustituirse a sí mismo en
    "sys.modules".  Este es un comportamiento específico de la
    implementación que no se garantiza que funcione en otras
    implementaciones de Python.
