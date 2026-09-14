---
title: '"types" --- Dynamic type creation and names for built-in types'
source_url: https://docs.python.org/es/3
source_path: library/types.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4330
---

# "types" --- Dynamic type creation and names for built-in types

**Código fuente:** Lib/types.py

======================================================================

Este módulo define funciones de utilidad para ayudar en la creación
dinámica de tipos nuevos.

Este también define nombres para algunos tipos de objetos que son
utilizados por el intérprete estándar de Python, pero no expuestos
como integrados como lo son "int" o "str".

Por último, este proporciona algunas clases de utilidad y funciones
adicionales relacionadas con tipos que no son lo suficientemente
fundamentales como para ser integradas.

## Creación dinámica de tipos

types.new_class(name, bases=(), kwds=None, exec_body=None)

   Crea un objeto de clase dinámicamente utilizando la metaclase
   adecuada.

   Los tres primeros argumentos son los componentes que componen un
   encabezado de definición de clase: el nombre de la clase, las
   clases base (en orden), los argumentos por palabra clave (tal como
   "metaclass").

   El argumento *exec_body* es una retrollamada que se usa para
   rellenar el espacio de nombres de clase recién creado. Debe aceptar
   el espacio de nombre de clase como su único argumento y actualizar
   el espacio de nombres directamente con el contenido de la clase. Si
   no se proporciona ninguna retrollamada, tiene el mismo efecto que
   pasar "lambda ns: None".

   Added in version 3.3.

types.prepare_class(name, bases=(), kwds=None)

   Calcula la metaclase adecuada y crea el espacio de nombre de clase.

   Los argumentos son los componentes que constituyen un encabezado de
   definición de clase: el nombre de la clase, las clases base (en
   orden) y los argumentos de palabra clave (como "metaclass").

   El valor retornado es una tupla de 3: "metaclass, namespace, kwds"

   *metaclass* es la metaclase adecuada, *namespace* es el espacio de
   nombre de clase preparado y *kwds* es una copia actualizada del
   pasado en el argumento *kwds* con cualquier entrada "'metaclass'"
   eliminada. Si no se pasa ningún argumento *kwds*, será un
   diccionario vacío.

   Added in version 3.3.

   Distinto en la versión 3.6: El valor predeterminado para el
   elemento "namespace" de la tupla retornada ha cambiado.  Ahora una
   asignación de inserción-orden-conservación es utilizada cuando la
   metaclase no tiene un método "__prepare__".

Ver también:

  Metaclases
     Detalles completos del proceso de creación de clases soportado
     por estas funciones

  **PEP 3115** - Metaclases en Python 3000
     Se presenta el *hook* de espacio de nombres "__prepare__"

types.resolve_bases(bases)

   Resuelve las entradas MRO dinámicamente según lo especificado por
   **PEP 560**.

   Esta función busca elementos en *bases* que no sean instancias de
   "type", y retorna una tupla donde cada objeto que tenga un método
   "__mro_entries__()" es reemplazado por el resultado desempaquetado
   de llamar a dicho método. Si un elemento de *bases* es una
   instancia de "type", o no tiene un método "__mro_entries__()",
   entonces es incluido sin cambios en la tupla de retorno.

   Added in version 3.7.

types.get_original_bases(cls, /)

   Retorna la tupla de objetos originalmente dados como bases de *cls*
   antes de que el método "__mro_entries__()" sea llamado en cualquier
   base (siguiendo los mecanismos establecidos en **PEP 560**). Esto
   es útil para introspección Genéricos.

   For classes that have an "__orig_bases__" attribute, this function
   returns the value of "cls.__orig_bases__". For classes without the
   "__orig_bases__" attribute, "cls.__bases__" is returned.

   Ejemplos:

      from typing import TypeVar, Generic, NamedTuple, TypedDict

      T = TypeVar("T")
      class Foo(Generic[T]): ...
      class Bar(Foo[int], float): ...
      class Baz(list[str]): ...
      Eggs = NamedTuple("Eggs", [("a", int), ("b", str)])
      Spam = TypedDict("Spam", {"a": int, "b": str})

      assert Bar.__bases__ == (Foo, float)
      assert get_original_bases(Bar) == (Foo[int], float)

      assert Baz.__bases__ == (list,)
      assert get_original_bases(Baz) == (list[str],)

      assert Eggs.__bases__ == (tuple,)
      assert get_original_bases(Eggs) == (NamedTuple,)

      assert Spam.__bases__ == (dict,)
      assert get_original_bases(Spam) == (TypedDict,)

      assert int.__bases__ == (object,)
      assert get_original_bases(int) == (object,)

   Added in version 3.12.

Ver también:

  **PEP 560** - Soporte principal para módulos de tipo y tipos
  genéricos

## Tipos de Intérpretes Estándar

Este módulo proporciona nombres para muchos de los tipos necesarios
para implementar un intérprete de Python. Esto evita deliberadamente
incluir algunos de los tipos que surgen sólo accidentalmente durante
el procesamiento, tal como el tipo "listiterator".

El uso típico de estos nombres es para verificar "isinstance()" o
"issubclass()".

Si se crea una instancia de cualquiera de estos tipos, tenga en cuenta
que las firmas pueden variar entre las versiones de Python.

Los nombres estándar son definidos para los siguientes tipos:

class types.NoneType

   El tipo de "None".

   Added in version 3.10.

class types.FunctionType
class types.LambdaType

   El tipo de funciones definidas por el usuario y funciones creadas
   por expresiones  "lambda".

   Lanza un auditing event "function.__new__" con el argumento "code".

   El evento auditor solo ocurre para la instanciación directa de
   objetos de código y no se genera para la compilación normal.

class types.GeneratorType

   El tipo de iterador *generator* de objetos, creados por funciones
   generadoras.

class types.CoroutineType

   El tipo de objetos *coroutine*, creados por funciones "async def".

   Added in version 3.5.

class types.AsyncGeneratorType

   El tipo de iterador *asynchronous generator* de objetos, creados
   por funciones generadoras asíncronas.

   Added in version 3.6.

class types.CodeType(**kwargs)

   The type of code objects such as returned by "compile()".

   Lanza un evento auditor "code.__new__" con los argumentos "code",
   "filename", "name", "argcount", "posonlyargcount",
   "kwonlyargcount", "nlocals", "stacksize", "flags".

   Tenga en cuenta que los argumentos auditados pueden no coincidir
   con los nombres o posiciones requeridos por el inicializador. El
   evento auditor solo ocurre para la instanciación directa de objetos
   de código y no se genera para la compilación normal.

class types.CellType

   The type for cell objects: such objects are used as containers for
   a function's *closure variables*.

   Added in version 3.8.

class types.MethodType

   El tipo de métodos de instancias de clase definidas por el usuario.

class types.BuiltinFunctionType
class types.BuiltinMethodType

   El tipo de funciones integradas como "len()" o "sys.exit()" y
   métodos de clases integradas.  (Aquí, el término "incorporado"
   significa "escrito en C".)

class types.WrapperDescriptorType

   El tipo de métodos de algunos tipos de datos integrados y clases
   base como "object.__init__()" o "object.__lt__()".

   Added in version 3.7.

class types.MethodWrapperType

   El tipo de métodos *bound* de algunos tipos de datos integrados y
   clases base. Por ejemplo, es el tipo de "object().__str__".

   Added in version 3.7.

class types.NotImplementedType

   El tipo de "NotImplemented".

   Added in version 3.10.

class types.MethodDescriptorType

   El tipo de métodos de algunos tipos de datos integrados como
   "str.join()".

   Added in version 3.7.

class types.ClassMethodDescriptorType

   El tipo de métodos de clase *unbound* de algunos tipos de datos
   integrados como "dict.__dict__['fromkeys']".

   Added in version 3.7.

class types.ModuleType(name, doc=None)

   El tipo de *módulos*. El constructor toma el nombre del módulo que
   se va a crear y de forma opcional su *docstring*.

   Ver también:

     Documentation on module objects
        Provides details on the special attributes that can be found
        on instances of "ModuleType".

     "importlib.util.module_from_spec()"
        Modules created using the "ModuleType" constructor are created
        with many of their special attributes unset or set to default
        values. "module_from_spec()" provides a more robust way of
        creating "ModuleType" instances which ensures the various
        attributes are set appropriately.

class types.EllipsisType

   El tipo de "Ellipsis".

   Added in version 3.10.

class types.GenericAlias(t_origin, t_args)

   El tipo de parameterized generics como "list[int]".

   "t_origin" debería ser una clase genérica no parametrizada, como
   "list", "tuple" o "dict". "t_args" debe ser una "tuple"
   (posiblemente de longitud 1) de tipos que parametriza "t_origin":

      >>> from types import GenericAlias

      >>> list[int] == GenericAlias(list, (int,))
      True
      >>> dict[str, int] == GenericAlias(dict, (str, int))
      True

   Added in version 3.9.

   Distinto en la versión 3.9.2: Este tipo ahora puede heredarse.

   Ver también:

     Tipos de alias genéricos
        Documentación detallada sobre instancias de
        "types.GenericAlias"

     **PEP 585** - Sugerencias de tipo genéricas en colecciones
     estándar
        Presentando la clase "types.GenericAlias"

class types.UnionType

   El tipo de union type expressions.

   Added in version 3.10.

   Distinto en la versión 3.14: This is now an alias for
   "typing.Union".

class types.TracebackType(tb_next, tb_frame, tb_lasti, tb_lineno)

   El tipo de objetos de rastreo como los que se encuentran en
   "sys.exception().__traceback__".

   Consulte la referencia de lenguaje para obtener detalles de los
   atributos y operaciones disponibles, y orientación sobre cómo crear
   *tracebacks* dinámicamente.

class types.FrameType

   The type of frame objects such as found in "tb.tb_frame" if "tb" is
   a traceback object.

class types.GetSetDescriptorType

   The type of objects defined in extension modules with
   "PyGetSetDef", such as "FrameType.f_locals" or
   "array.array.typecode". This type is used as descriptor for object
   attributes; it has the same purpose as the "property" type, but for
   classes defined in extension modules.

class types.MemberDescriptorType

   El tipo de objetos definidos en módulos de extensión con
   "PyMemberDef", como "datetime.timedelta.days".  Este tipo se
   utiliza como descriptor para miembros de datos C simples que
   utilizan funciones de conversión estándar; tiene el mismo propósito
   que el tipo "property", pero para las clases definidas en los
   módulos de extensión.

   In addition, when a class is defined with a "__slots__" attribute,
   then for each slot, an instance of "MemberDescriptorType" will be
   added as an attribute on the class. This allows the slot to appear
   in the class's "__dict__".

   En otras implementaciones de Python, este tipo puede ser idéntico a
   "GetSetDescriptorType".

class types.MappingProxyType(mapping)

   Proxy de solo lectura de un mapeo. Proporciona una vista dinámica
   en las entradas de la asignación, lo que significa que cuando
   cambia la asignación, la vista refleja estos cambios.

   "MappingProxyType"s are generic over two types, signifying
   (respectively) the types of the underlying mapping's keys and
   values.

   Added in version 3.3.

   Distinto en la versión 3.9: Actualizado para soportar el nuevo
   operador de unión ("|") de **PEP 584**, que simplemente delega al
   mapeo subyacente.

   key in proxy

      Retorna "True" si la asignación subyacente tiene una clave
      *key*, de lo contrario "False".

   proxy[key]

      Retorna el elemento de la asignación subyacente con la clave
      *key*.  Lanza un "KeyError" si *key* no está en la asignación
      subyacente.

   iter(proxy)

      Retorna un iterador sobre las claves de la asignación
      subyacente.  Este es un método abreviado para
      "iter(proxy.keys())".

   len(proxy)

      Retorna el número de elementos de la asignación subyacente.

   copy()

      Retorna una copia superficial de la asignación subyacente.

   get(key[, default])

      Retorna el valor de *key* si *key* está en la asignación
      subyacente, de lo contrario *default*.  Si no se proporciona
      *default*, el valor predeterminado es "None", por lo que este
      método nunca lanza un "KeyError".

   items()

      Retorna una nueva vista de los elementos de la asignación
      subyacente (en pares "(key, value)").

   keys()

      Retorna una nueva vista de las claves de la asignación
      subyacente.

   values()

      Retorna una nueva vista de los valores de la asignación
      subyacente.

   reversed(proxy)

      Retorna un iterador inverso sobre las claves de la asignación
      subyacente.

      Added in version 3.9.

   hash(proxy)

      Retorna un hash del mapeo subyacente.

      Added in version 3.12.

class types.CapsuleType

   The type of capsule objects.

   Added in version 3.13.

## Clases y funciones de utilidad adicionales

class types.SimpleNamespace

   Una subclase simple "object" que proporciona acceso de atributo a
   su espacio de nombre, así como una representación significativa.

   Unlike "object", with "SimpleNamespace" you can add and remove
   attributes.

   "SimpleNamespace" objects may be initialized in the same way as
   "dict": either with keyword arguments, with a single positional
   argument, or with both. When initialized with keyword arguments,
   those are directly added to the underlying namespace.
   Alternatively, when initialized with a positional argument, the
   underlying namespace will be updated with key-value pairs from that
   argument (either a mapping object or an *iterable* object producing
   key-value pairs). All such keys must be strings.

   El tipo es aproximadamente equivalente al código siguiente:

      class SimpleNamespace:
          def __init__(self, mapping_or_iterable=(), /, **kwargs):
              self.__dict__.update(mapping_or_iterable)
              self.__dict__.update(kwargs)

          def __repr__(self):
              items = (f"{k}={v!r}" for k, v in self.__dict__.items())
              return "{}({})".format(type(self).__name__, ", ".join(items))

          def __eq__(self, other):
              if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
                 return self.__dict__ == other.__dict__
              return NotImplemented

   "SimpleNamespace" puede ser útil como reemplazo para "class NS:
   pass". Sin embargo, para un tipo de registro estructurado, utilice
   "namedtuple()" en su lugar.

   "SimpleNamespace" objects are supported by "copy.replace()".

   Added in version 3.3.

   Distinto en la versión 3.9: El orden de los atributos en el *repr*
   cambió de alfabético a orden de inserción (como "dict").

   Distinto en la versión 3.13: Added support for an optional
   positional argument.

types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)

   Acceso de atributo de ruta en una clase para __getattr__.

   Se trata de un descriptor, que se utiliza para definir atributos
   que actúan de forma diferente cuando se accede a través de una
   instancia y a través de una clase.  El acceso a la instancia sigue
   siendo normal, pero el acceso a un atributo a través de una clase
   se enrutará al método __getattr__ de la clase; esto se hace
   lanzando AttributeError.

   Esto permite tener propiedades activas en una instancia y tener
   atributos virtuales en la clase con el mismo nombre (véase
   "enum.Enum" para obtener un ejemplo).

   Added in version 3.4.

## Funciones de utilidad de corutina

types.coroutine(gen_func)

   Esta función transforma una función *generator* en una *coroutine
   function* que retorna una corrutina basada en generador. La
   corrutina basada en generador sigue siendo un *generator iterator*,
   pero también se considera un objeto *coroutine* y es
   *awaitable*.Sin embargo, es posible que no implemente
   necesariamente el método "__await__()".

   Si *gen_func* es una función generadora, se modificará en el lugar.

   Si *gen_func* no es una función generadora, se envolverá. Si
   retorna una instancia de "collections.abc.Generator", la instancia
   se ajustará en un objeto proxy *awaitable*.  Todos los demás tipos
   de objetos se retornarán tal cual.

   Added in version 3.5.
