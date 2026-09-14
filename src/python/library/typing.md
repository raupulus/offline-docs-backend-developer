---
title: '"typing" --- Support for type hints'
source_url: https://docs.python.org/es/3
source_path: library/typing.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4340
---

# "typing" --- Support for type hints

Added in version 3.5.

**Source code:** Lib/typing.py

Nota:

  El entorno de ejecución de Python no exige anotaciones de tipos de
  funciones y variables. Pueden ser utilizadas por herramientas de
  terceros como *type checkers*, IDE, linters, etc.

======================================================================

Este módulo proporciona soporte en tiempo de ejecución para
sugerencias de tipo.

Considere la función a continuación:

   def surface_area_of_cube(edge_length: float) -> str:
       return f"The surface area of the cube is {6 * edge_length ** 2}."

La función "surface_area_of_cube" toma un argumento que se espera que
sea una instancia de "float", como lo indica *type hint* "edge_length:
float". Se espera que la función devuelva una instancia de "str", como
lo indica la sugerencia "-> str".

Si bien las sugerencias de tipos pueden ser clases simples como
"float" o "str", también pueden ser más complejas. El módulo "typing"
proporciona un vocabulario de sugerencias de tipos más avanzadas.

Con frecuencia se agregan nuevas funciones al módulo "typing". El
paquete typing_extensions proporciona versiones anteriores de estas
nuevas funciones para versiones anteriores de Python.

Ver también:

  Typing cheat sheet
     Una visión general de los indicadores de tipo (hospedado por mypy
     docs, en inglés.)

  Type System Reference section of the mypy docs
     El sistema de tipos de Python es estandarizado por medio de las
     PEPs, así que esta referencia debe aplicarse a la mayoría de
     validadores de tipo de Python. (Algunas partes pueden referirse
     específicamente a mypy.)

  Static Typing with Python
     Documentación independiente del validador de tipos escrita por la
     comunidad que detalla las características del sistema de tipos,
     herramientas útiles relacionadas con el tipado y mejores
     prácticas.

## Especificación del sistema de tipos de Python

The canonical, up-to-date specification of the Python type system can
be found at Specification for the Python type system.

## Alias de tipo

Un alias de tipo se define usando la declaración "type", el cual crea
una instancia de "TypeAliasType". En este ejemplo, "Vector" y
"list[float]" serán tratados de manera equivalente a los validadores
de tipo estático:

   type Vector = list[float]

   def scale(scalar: float, vector: Vector) -> Vector:
       return [scalar * num for num in vector]

   # pasa las verificaciones de tipo; una lista de float califica como Vector.
   new_vector = scale(2.0, [1.0, -4.2, 5.4])

Los alias de tipo son útiles para simplificar firmas de tipo
complejas. Por ejemplo:

   from collections.abc import Sequence

   type ConnectionOptions = dict[str, str]
   type Address = tuple[str, int]
   type Server = tuple[Address, ConnectionOptions]

   def broadcast_message(message: str, servers: Sequence[Server]) -> None:
       ...

   # El verificador de tipos estáticos tratará la firma de tipo anterior como
   # exactamente equivalente a esta.
   def broadcast_message(
       message: str,
       servers: Sequence[tuple[tuple[str, int], dict[str, str]]]
   ) -> None:
       ...

La declaración "type" es nueva en Python 3.12. Para compatibilidad con
versiones anteriores, los alias de tipo también se pueden crear
mediante una asignación simple.:

   Vector = list[float]

O marcarse con "TypeAlias" para dejar explícito que se trata de un
alias de tipo, no de una asignación de variable normal:

   from typing import TypeAlias

   Vector: TypeAlias = list[float]

## NewType

Use la clase auxiliar "NewType" para crear tipos distintos:

   from typing import NewType

   UserId = NewType('UserId', int)
   some_id = UserId(524313)

El validador estático de tipos tratará el nuevo tipo como si fuera una
subclase del tipo original. Esto es útil para capturar errores
lógicos:

   def get_user_name(user_id: UserId) -> str:
       ...

   # pasa la verificación de tipos
   user_a = get_user_name(UserId(42351))

   # falla la verificación de tipos; un int no es un UserId
   user_b = get_user_name(-1)

Se pueden realizar todas las operaciones de "int" en una variable de
tipo "UserId", pero el resultado siempre será de tipo "int". Esto
permite pasar un "UserId" allí donde se espere un "int", pero evitará
la creación accidental de un "UserId" de manera incorrecta:

   # 'output' es del tipo 'int', no 'UserId'
   output = UserId(23413) + UserId(54341)

Tenga en cuenta que estas validaciones solo las aplica el validador de
tipo estático. En tiempo de ejecución, la declaración "Derived =
NewType('Derived', Base)" hará que "Derived" sea una clase que retorna
inmediatamente cualquier parámetro que le pase. Eso significa que la
expresión "Derived(some_value)" no crea una nueva clase ni introduce
mucha sobrecarga más allá de la de una llamada de función regular.

Más concretamente, la expresión "some_value is Derived(some_value)"
será siempre verdadera en tiempo de ejecución.

No es válido crear un subtipo de "Derived":

   from typing import NewType

   UserId = NewType('UserId', int)

   # Falla en runtime y no pasa la verificación de tipos
   class AdminUserId(UserId): pass

Sin embargo, es posible crear un "NewType" basado en un "NewType"
'derivado':

   from typing import NewType

   UserId = NewType('UserId', int)

   ProUserId = NewType('ProUserId', UserId)

y la comprobación de tipo para "ProUserId" funcionará como se espera.

Véase **PEP 484** para más detalle.

Nota:

  Recuerde que el uso de alias de tipo implica que los dos tipos son
  *equivalentes* entre sí. Haciendo "type Alias = Original" provocará
  que el validador estático de tipos trate "Alias" como algo
  *exactamente equivalente* a "Original" en todos los casos. Esto es
  útil para cuando se quiera simplificar indicadores de tipo
  complejos.En cambio, "NewType" declara un tipo que es *subtipo* de
  otro. Haciendo "Derived = NewType('Derived', Original)" hará que el
  Validador estático de tipos trate "Derived" como una *subclase* de
  "Original", lo que implica que un valor de tipo "Original" no puede
  ser usado allí donde se espere un valor de tipo "Derived". Esto es
  útil para prevenir errores lógicos con un coste de ejecución mínimo.

Added in version 3.5.2.

Distinto en la versión 3.10: "NewType" es ahora una clase en lugar de
una función. Existe un costo de tiempo de ejecución adicional cuando
se llama a "NewType" a través de una función normal.

Distinto en la versión 3.11: El rendimiento al llamar "NewType" ha
sido restaurado a su nivel en Python 3.9.

## Anotaciones en objetos invocables

Las funciones (u otros objetos *callable*) se pueden anotar utilizando
"collections.abc.Callable" o el obsoleto "typing.Callable".
"Callable[[int], str]" significa una función que toma un único
parámetro de tipo "int" y devuelve un "str".

Por ejemplo:

   from collections.abc import Callable, Awaitable

   def feeder(get_next_item: Callable[[], str]) -> None:
       ...  # Body

   def async_query(on_success: Callable[[int], None],
                   on_error: Callable[[int, Exception], None]) -> None:
       ...  # Body

   async def on_update(value: str) -> None:
       ...  # Body

   callback: Callable[[str], Awaitable[None]] = on_update

The subscription syntax must always be used with exactly two values:
the argument list and the return type.  The argument list must be a
list of types, a "ParamSpec", "Concatenate", or an ellipsis ("...").
The return type must be a single type.

Si se proporciona una elipsis como lista de argumentos, indica que
sería aceptable un invocable con cualquier lista de parámetros
arbitraria:

   def concat(x: str, y: str) -> str:
       return x + y

   x: Callable[..., str]
   x = str     # OK
   x = concat  # Also OK

"Callable" no puede expresar firmas complejas, como funciones que
toman un número variádico de argumentos, overloaded functions o
funciones que tienen parámetros que solo contienen palabras clave. Sin
embargo, estas firmas se pueden expresar definiendo una clase
"Protocol" con un método "__call__()":

   from collections.abc import Iterable
   from typing import Protocol

   class Combiner(Protocol):
       def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]: ...

   def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
       for item in data:
           ...

   def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
       ...
   def bad_cb(*vals: bytes, maxitems: int | None) -> list[bytes]:
       ...

   batch_proc([], good_cb)  # OK
   batch_proc([], bad_cb)   # Error! El argumento 2 tiene un tipo incompatible debido a
                            # nombre y tipo diferentes en la devolución de llamada

Los invocables que toman otros invocables como argumentos pueden
indicar que sus tipos de parámetros dependen unos de otros utilizando
"ParamSpec". Además, si ese invocable agrega o elimina argumentos de
otros invocables, se puede utilizar el operador "Concatenate". Toman
la forma "Callable[ParamSpecVariable, ReturnType]" y
"Callable[Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable],
ReturnType]" respectivamente.

Distinto en la versión 3.10: "Callable" ahora es compatible con
"ParamSpec" y "Concatenate". Consulte **PEP 612** para obtener más
información.

Ver también:

  La documentación de "ParamSpec" y "Concatenate" proporciona ejemplos
  de uso en "Callable".

## Genéricos

Dado que la información de tipo sobre los objetos guardados en
contenedores no se puede inferir estáticamente de manera genérica,
muchas clases de contenedor en la biblioteca estándar admiten
suscripción para indicar los tipos esperados de elementos de
contenedor.

   from collections.abc import Mapping, Sequence

   class Employee: ...

   # Sequence[Employee] indica que todos los elementos de la secuencia
   # deben ser instancias de "Employee".
   # Mapping[str, str] indica que todas las claves y todos los valores de la asignación
   # deben ser cadenas.
   def notify_by_email(employees: Sequence[Employee],
                       overrides: Mapping[str, str]) -> None: ...

Funciones y clases genéricas pueden ser parametrizadas usando type
parameter syntax:

   from collections.abc import Sequence

   def first[T](l: Sequence[T]) -> T:  # La función es genérica sobre el TypeVar "T"
       return l[0]

O utilizando directamente la fábrica "TypeVar":

   from collections.abc import Sequence
   from typing import TypeVar

   U = TypeVar('U')                  # Declara variable tipo "U"

   def second(l: Sequence[U]) -> U:  # La función es genérica sobre  TypeVar "U"
       return l[1]

Distinto en la versión 3.12: El soporte sintáctico para genéricos es
nuevo en Python 3.12.

## Anotaciones en tuplas

En la mayoría de los contenedores de Python, el sistema de tipado
supone que todos los elementos del contenedor serán del mismo tipo.
Por ejemplo:

   from collections.abc import Mapping

   # El verificador de tipos inferirá que todos los elementos en ``x`` deben ser ints
   x: list[int] = []

   #Error del verificador de tipo: ``list`` solo acepta un único argumento de tipo:
   y: list[int, str] = [1, 'foo']

   # El verificador de tipos inferirá que todas las claves en ``z`` deben ser strings,
   # y que todos los valores en ``z`` deben ser strings o ints
   z: Mapping[str, str | int] = {}

"list" solo acepta un argumento de tipo, por lo que un validador de
tipos emitiría un error en la asignación "y" anterior. De manera
similar, "Mapping" solo acepta dos argumentos de tipo: el primero
indica el tipo de las claves y el segundo indica el tipo de los
valores.

Sin embargo, a diferencia de la mayoría de los demás contenedores de
Python, es común en el código idiomático de Python que las tuplas
tengan elementos que no sean todos del mismo tipo. Por este motivo,
las tuplas son un caso especial en el sistema de tipado de Python.
"tuple" acepta *cualquier número* de argumentos de tipo:

   # OK: ``x`` se asigna a una tupla de longitud 1 donde el único elemento es un int
   x: tuple[int] = (5,)

   # OK: ``y`` se asigna a una tupla de longitud 2;
   # el elemento 1 es un int, el elemento 2 es una cadena
   y: tuple[int, str] = (5, "foo")

   # Error: la anotación de tipo indica una tupla de longitud 1,
   # pero ``z`` se ha asignado a una tupla de longitud 3
   z: tuple[int] = (1, 2, 3)

To denote a tuple which could be of *any* length, and in which all
elements are of the same type "T", use the literal ellipsis "...":
"tuple[T, ...]". To denote an empty tuple, use "tuple[()]". Using
plain "tuple" as an annotation is equivalent to using "tuple[Any,
...]":

   x: tuple[int, ...] = (1, 2)
   # Estas reasignaciones están bien: ``tuple[int, ...]`` indica que x puede tener cualquier longitud
   x = (1, 2, 3)
   x = ()
   # Esta reasignación es un error: todos los elementos en ``x`` deben ser enteros
   x = ("foo", "bar")

   # ``y`` solo se puede asignar a una tupla vacía
   y: tuple[()] = ()

   z: tuple = ("foo", "bar")
   # Estas reasignaciones están bien: una ``tupla`` simple es equivalente a ``tuple[Any, ...]``
   z = (1, 2, 3)
   z = ()

## El tipo de objetos de clase

Una variable anotada con "C" puede aceptar un valor de tipo "C". Por
el contrario, una variable anotada con "type[C]" (o "typing.Type[C]"
en desuso) puede aceptar valores que sean clases en sí mismos;
específicamente, aceptará el *class object* de "C". Por ejemplo:

   a = 3         # Tiene tipo ``int``
   b = int       # Tiene tipo ``type[int]``
   c = type(a)   # Tambien tiene tipo ``type[int]``

Tenga en cuenta que "type[C]" es covariante:

   class User: ...
   class ProUser(User): ...
   class TeamUser(User): ...

   def make_new_user(user_class: type[User]) -> User:
       # ...
       return user_class()

   make_new_user(User)      # OK
   make_new_user(ProUser)   # También OK: ``type[ProUser]`` es un subtipo de ``type[User]``
   make_new_user(TeamUser)  # aún está bien
   make_new_user(User())    # Error: se espera ``type[User]`` pero se usó  ``User``
   make_new_user(int)       # Error: ``type[int]`` no es un subtipo de ``type[User]``

Los únicos parámetros legales para "type" son las clases, "Any",
variables de tipo y uniones de cualquiera de estos tipos. Por ejemplo:

   def new_non_team_user(user_class: type[BasicUser | ProUser]): ...

   new_non_team_user(BasicUser)  # OK
   new_non_team_user(ProUser)    # OK
   new_non_team_user(TeamUser)   # Error: ``type[TeamUser]`` no es un subtipo
                                 # de ``type[BasicUser | ProUser]``
   new_non_team_user(User)       # También un error

"type[Any]" es equivalente a "type", que es la raíz de la jerarquía de
metaclases de Python.

## Anotación de generadores y corrutinas

Se puede anotar un generador utilizando el tipo genérico
"Generator[YieldType, SendType, ReturnType]". Por ejemplo:

   def echo_round() -> Generator[int, float, str]:
       sent = yield 0
       while sent >= 0:
           sent = yield round(sent)
       return 'Done'

Tenga en cuenta que, a diferencia de muchas otras clases genéricas en
la biblioteca estándar, "SendType" de "Generator" se comporta de
manera contravariante, no covariante o invariante.

Los parámetros "SendType" y "ReturnType" tienen como valor
predeterminado "None":

   def infinite_stream(start: int) -> Generator[int]:
       while True:
           yield start
           start += 1

También es posible configurar estos tipos explícitamente:

   def infinite_stream(start: int) -> Generator[int, None, None]:
       while True:
           yield start
           start += 1

Los generadores simples que solo producen valores también se pueden
anotar como que tienen un tipo de retorno de "Iterable[YieldType]" o
"Iterator[YieldType]":

   def infinite_stream(start: int) -> Iterator[int]:
       while True:
           yield start
           start += 1

Los generadores asincrónicos se manejan de manera similar, pero no
espere un argumento de tipo "ReturnType" ("AsyncGenerator[YieldType,
SendType]"). El argumento "SendType" tiene como valor predeterminado
"None", por lo que las siguientes definiciones son equivalentes:

   async def infinite_stream(start: int) -> AsyncGenerator[int]:
       while True:
           yield start
           start = await increment(start)

   async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
       while True:
           yield start
           start = await increment(start)

Al igual que en el caso sincrónico, también están disponibles
"AsyncIterable[YieldType]" y "AsyncIterator[YieldType]":

   async def infinite_stream(start: int) -> AsyncIterator[int]:
       while True:
           yield start
           start = await increment(start)

Las corrutinas se pueden anotar utilizando "Coroutine[YieldType,
SendType, ReturnType]". Los argumentos genéricos corresponden a los de
"Generator", por ejemplo:

   from collections.abc import Coroutine
   c: Coroutine[list[str], str, int]  # Algunas corrutinas definidas en otro lugar
   x = c.send('hi')                   # El tipo inferido de 'x' es list[str]
   async def bar() -> None:
       y = await c                    # El tipo inferido de 'y' es int

## Tipos genéricos definidos por el usuario

Una clase definida por el usuario puede ser definida como una clase
genérica.

   from logging import Logger

   class LoggedVar[T]:
       def __init__(self, value: T, name: str, logger: Logger) -> None:
           self.name = name
           self.logger = logger
           self.value = value

       def set(self, new: T) -> None:
           self.log('Set ' + repr(self.value))
           self.value = new

       def get(self) -> T:
           self.log('Get ' + repr(self.value))
           return self.value

       def log(self, message: str) -> None:
           self.logger.info('%s: %s', self.name, message)

Esta sintaxis indica que la clase "LoggedVar" está parametrizada en
torno a un único type variable "T" . Esto también hace que "T" sea
válido como tipo dentro del cuerpo de la clase.

Las clases genéricas heredan implícitamente de "Generic". Para
compatibilidad con Python 3.11 y versiones anteriores, también es
posible heredar explícitamente de "Generic" para indicar una clase
genérica:

   from typing import TypeVar, Generic

   T = TypeVar('T')

   class LoggedVar(Generic[T]):
       ...

Las clases genéricas tienen métodos "__class_getitem__()", lo que
significa que se pueden parametrizar en tiempo de ejecución (por
ejemplo, "LoggedVar[int]" a continuación):

   from collections.abc import Iterable

   def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
       for var in vars:
           var.set(0)

Un tipo genérico puede tener un numero cualquiera de variables de
tipo. Se permiten todas las variaciones de "TypeVar" para ser usadas
como parámetros de un tipo genérico:

   from typing import TypeVar, Generic, Sequence

   class WeirdTrio[T, B: Sequence[bytes], S: (int, str)]:
       ...

   OldT = TypeVar('OldT', contravariant=True)
   OldB = TypeVar('OldB', bound=Sequence[bytes], covariant=True)
   OldS = TypeVar('OldS', int, str)

   class OldWeirdTrio(Generic[OldT, OldB, OldS]):
       ...

Cada argumento de variable de tipo de "Generic" debe ser distinto. Por
lo tanto, esto no es válido:

   from typing import TypeVar, Generic
   ...

   class Pair[M, M]:  # SyntaxError
       ...

   T = TypeVar('T')

   class Pair(Generic[T, T]):   # INVALID
       ...

Las clases genéricas también pueden heredar de otras clases:

   from collections.abc import Sized

   class LinkedList[T](Sized):
       ...

Al heredar de clases genéricas, algunos parámetros de tipo podrían ser
fijos:

   from collections.abc import Mapping

   class MyDict[T](Mapping[str, T]):
       ...

En este caso "MyDict" tiene un solo parámetro, "T".

El uso de una clase genérica sin especificar parámetros de tipo supone
"Any" para cada posición. En el siguiente ejemplo, "MyIterable" no es
genérico, sino que hereda implícitamente de "Iterable[Any]":

   from collections.abc import Iterable

   class MyIterable(Iterable): # Igual que Iterable[Any]
       ...

También se admiten alias de tipos genéricos definidos por el usuario.
Ejemplos:

   from collections.abc import Iterable

   type Response[S] = Iterable[S] | int

   # Return type here is same as Iterable[str] | int
   def response(query: str) -> Response[str]:
       ...

   type Vec[T] = Iterable[tuple[T, T]]

   def inproduct[T: (int, float, complex)](v: Vec[T]) -> T: # Same as Iterable[tuple[T, T]]
       return sum(x*y for x, y in v)

Para compatibilidad con versiones anteriores, también se pueden crear
alias de tipos genéricos mediante una asignación simple:

   from collections.abc import Iterable
   from typing import TypeVar

   S = TypeVar("S")
   Response = Iterable[S] | int

Distinto en la versión 3.7: "Generic" ya no posee una metaclase
personalizable.

Distinto en la versión 3.12: La compatibilidad sintáctica con
genéricos y alias de tipo es una novedad en la versión 3.12. Antes,
las clases genéricas debían heredar explícitamente de "Generic" o
contener una variable de tipo en una de sus bases.

User-defined generics for parameter expressions are also supported via
parameter specification variables in the form "[**P]".  The behavior
is consistent with type variables' described above as parameter
specification variables are treated by the "typing" module as a
specialized type variable.  The one exception to this is that a list
of types can be used to substitute a "ParamSpec":

   >>> class Z[T, **P]: ...  # T es un TypeVar; P es un ParamSpec
   ...
   >>> Z[int, [dict, float]]
   __main__.Z[int, [dict, float]]

También se pueden crear clases genéricas sobre "ParamSpec" utilizando
herencia explícita de "Generic". En este caso, no se utiliza "**":

   from typing import ParamSpec, Generic

   P = ParamSpec('P')

   class Z(Generic[P]):
       ...

Otra diferencia entre "TypeVar" y "ParamSpec" es que una variable
genérica con una sola especificación de parámetros aceptará listas de
parámetros en los formatos "X[[Type1, Type2, ...]]" y también
"X[Type1, Type2, ...]" por razones estéticas. Internamente, el último
se convierte al primero, por lo que los siguientes son equivalentes:

   >>> class X[**P]: ...
   ...
   >>> X[int, str]
   __main__.X[[int, str]]
   >>> X[[int, str]]
   __main__.X[[int, str]]

Tenga en cuenta que los genéricos con "ParamSpec" pueden no tener
"__parameters__" correctos después de la sustitución en algunos casos
porque están destinados principalmente a la verificación de tipos
estáticos.

Distinto en la versión 3.10: "Generic" ahora se puede parametrizar
sobre expresiones de parámetros. Consulte "ParamSpec" y **PEP 612**
para obtener más detalles.

A user-defined generic class can have ABCs as base classes without a
metaclass conflict. Generic metaclasses are not supported. The outcome
of parameterizing generics is cached, and most types in the "typing"
module are *hashable* and comparable for equality.

## El tipo "Any"

A special kind of type is "Any". A static type checker will treat
every type as assignable to "Any" and "Any" as assignable to every
type.

Esto significa que es posible realizar cualquier operación o llamada a
un método en un valor de tipo "Any" y asignarlo a cualquier variable:

   from typing import Any

   a: Any = None
   a = []          # OK
   a = 2           # OK

   s: str = ''
   s = a           # OK

   def foo(item: Any) -> int:
       # Pasa la verificación de tipos; 'item' puede ser de cualquier tipo,
       # y ese tipo puede tener el método 'bar'
       item.bar()
       ...

Nótese que no se realiza comprobación de tipo cuando se asigna un
valor de tipo "Any" a un tipo más preciso. Por ejemplo, el Validador
estático de tipos no reportó ningún error cuando se asignó "a" a "s",
aún cuando se declaró "s" como de tipo "str" y recibió un valor "int"
en tiempo de ejecución!

Además, todas las funciones sin un tipo de retorno o tipos en los
parámetros serán asignadas implícitamente a "Any" por defecto:

   def legacy_parser(text):
       ...
       return data

   # Un verificador de tipos estáticos tratará
   # lo anterior como si tuviera la misma firma que:
   def legacy_parser(text: Any) -> Any:
       ...
       return data

Este comportamiento permite que "Any" sea usado como una *vía de
escape* cuando es necesario mezclar código tipado estática y
dinámicamente.

Compárese el comportamiento de "Any" con el de "object". De manera
similar a "Any", todo tipo es un subtipo de "object". Sin embargo, en
oposición a "Any", lo contrario no es cierto: "object" *no* es un
subtipo de ningún otro tipo.

Esto implica que cuando el tipo de un valor es "object", un validador
de tipos rechazará prácticamente todas las operaciones con él, y al
asignarlo a una variable (o usarlo como valor de retorno) de un tipo
más preciso será un error de tipo. Por ejemplo:

   def hash_a(item: object) -> int:
       # Fails type checking; an object does not have a 'magic' method.
       item.magic()
       ...

   def hash_b(item: Any) -> int:
       # Passes type checking
       item.magic()
       ...

   # Passes type checking, since ints and strs are subclasses of object
   hash_a(42)
   hash_a("foo")

   # Passes type checking, since Any is assignable to all types
   hash_b(42)
   hash_b("foo")

Úsese "object" para indicar que un valor puede ser de cualquier tipo
de manera segura. Úsese "Any" para indicar que un valor es de tipado
dinámico.

## Subtipado nominal vs estructural

Inicialmente, el **PEP 484** definió el uso de *subtipado nominal*
para el sistema de tipado estático de Python. Esto implica que una
clase "A" será permitida allí donde se espere una clase "B" si y solo
si "A" es una subclase de "B".

Este requisito también se aplicaba anteriormente a clases base
abstractas (ABC), tales como "Iterable". El problema con esta
estrategia es que una clase debía de ser marcada explícitamente para
proporcionar esta funcionalidad, lo que resulta poco *pythónico*
(idiomático) y poco ajustado a lo que uno normalmente haría en un
código Python tipado dinámicamente. Por ejemplo, esto sí se ajusta al
**PEP 484**:

   from collections.abc import Sized, Iterable, Iterator

   class Bucket(Sized, Iterable[int]):
       ...
       def __len__(self) -> int: ...
       def __iter__(self) -> Iterator[int]: ...

**PEP 544** solves this problem by allowing users to write the above
code without explicit base classes in the class definition, allowing
"Bucket" to be implicitly considered a subtype of both "Sized" and
"Iterable[int]" by static type checkers. This is known as *structural
subtyping* (or static duck-typing):

   from collections.abc import Iterator, Iterable

   class Bucket:  # Nota: sin clases base
       ...
       def __len__(self) -> int: ...
       def __iter__(self) -> Iterator[int]: ...

   def collect(items: Iterable[int]) -> int: ...
   result = collect(Bucket())  # Pasa la verificación de tipos

Asimismo, creando subclases de la clase especial  "Protocol", el
usuario puede definir nuevos protocolos personalizados y beneficiarse
del tipado estructural (véanse los ejemplos de abajo).

## Contenido del módulo

El módulo "typing" define las siguientes clases, funciones y
decoradores.

### Primitivos especiales de tipado

#### Tipos especiales

Estos pueden ser usados como tipos en anotaciones. No soportan
suscripción usando "[]".

typing.Any

   Tipo especial que indica un tipo sin restricciones.

   * Every type is assignable to "Any".

   * "Any" is assignable to every type.

   Distinto en la versión 3.11: Ahora es posible utilizar "Any" como
   una clase base. Esto puede ser útil para evitar errores del
   validador de tipos con clases que pueden hacer uso del *duck
   typing* en cualquier punto, o que sean altamente dinámicas.

typing.AnyStr

   Una variables de tipo restringida.

   Definición:

      AnyStr = TypeVar('AnyStr', str, bytes)

   "AnyStr" está pensado para ser utilizado por funciones que pueden
   aceptar argumentos "str" o "bytes" pero que no puedan permitir que
   los dos se mezclen.

   Por ejemplo:

      def concat(a: AnyStr, b: AnyStr) -> AnyStr:
          return a + b

      concat("foo", "bar")    # OK, output tiene tipo 'str'
      concat(b"foo", b"bar")  # OK, output tiene tipo 'bytes'
      concat("foo", b"bar")   # Error, no se puede mezclar str y bytes

   Tenga en cuenta que, a pesar de su nombre, "AnyStr" no tiene nada
   que ver con el tipo "Any", ni significa “cualquier cadena de
   caracteres”. En particular, "AnyStr" y "str | bytes" son diferentes
   entre sí y tienen diferentes casos de uso:

      # Uso inválido de AnyStr:
      # La variable de tipo se usa solo una vez en la firma de la función,
      # por lo que el verificador de tipos no puede resolverla.
      def greet_bad(cond: bool) -> AnyStr:
          return "hi there!" if cond else b"greetings!"

      # La mejor manera de anotar esta función:
      def greet_proper(cond: bool) -> str | bytes:
          return "hi there!" if cond else b"greetings!"

   Deprecated since version 3.13, will be removed in version 3.18:
   Obsoleto en favor del nuevo type parameter syntax. Utilice "class
   A[T: (str, bytes)]: ..." en lugar de importar "AnyStr". Consulte
   **PEP 695** para obtener más detalles.En Python 3.16, "AnyStr" se
   eliminará de "typing.__all__" y se emitirán advertencias de desuso
   en tiempo de ejecución cuando se acceda a él o se importe desde
   "typing". "AnyStr" se eliminará de "typing" en Python 3.18.

typing.LiteralString

   Tipo especial que incluye sólo cadenas de caracteres literales.

   Cualquier cadena de caracteres literal es compatible con
   "LiteralString", al igual que cualquier otro "LiteralString". Sin
   embargo, un objeto cuyo tipo sea simplemente "str" no lo es. Una
   cadena de caracteres creada mediante la composición de objetos cuyo
   tipo sea "LiteralString" también es aceptable como "LiteralString".

   Por ejemplo:

      def run_query(sql: LiteralString) -> None:
          ...

      def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
          run_query("SELECT * FROM students")  # OK
          run_query(literal_string)  # OK
          run_query("SELECT * FROM " + literal_string)  # OK
          run_query(arbitrary_string)  # type checker error
          run_query(  # type checker error
              f"SELECT * FROM students WHERE name = {arbitrary_string}"
          )

   "LiteralString" es útil para API sensibles en las que cadenas de
   caracteres arbitrarias generadas por el usuario podrían generar
   problemas. Por ejemplo, los dos casos anteriores que generan
   errores de verificación de tipos podrían ser vulnerables a un
   ataque de inyección SQL.

   Véase **PEP 675** para más detalle.

   Added in version 3.11.

typing.Never
typing.NoReturn

   "Never" y "NoReturn" representan bottom type, un tipo que no tiene
   miembros.

   Se pueden utilizar para indicar que una función nunca retorna, como
   "sys.exit()":

      from typing import Never  # o NoReturn

      def stop() -> Never:
          raise RuntimeError('no way')

   O definir una función que nunca debe llamarse, ya que no hay
   argumentos válidos, como "assert_never()":

      from typing import Never  # o NoReturn

      def never_call_me(arg: Never) -> None:
          pass

      def int_or_str(arg: int | str) -> None:
          never_call_me(arg)  # error del verificador de tipos
          match arg:
              case int():
                  print("It's an int")
              case str():
                  print("It's a str")
              case _:
                  never_call_me(arg)  # OK, arg es del tipo Never (o NoReturn)

   "Never" y "NoReturn" tienen el mismo significado en el sistema de
   tipos y los verificadores de tipos estáticos los tratan a ambos de
   manera equivalente.

   Added in version 3.6.2: Se agregó "NoReturn".

   Added in version 3.11: Se agregó "Never".

typing.Self

   Tipo especial que representa la clase capturada actual.

   Por ejemplo:

      from typing import Self, reveal_type

      class Foo:
          def return_self(self) -> Self:
              ...
              return self

      class SubclassOfFoo(Foo): pass

      reveal_type(Foo().return_self())  # Revealed type is "Foo"
      reveal_type(SubclassOfFoo().return_self())  # Tipo revelado es "SubclassOfFoo"

   Esta anotación es semánticamente equivalente a lo siguiente, aunque
   de una manera más sucinta:

      from typing import TypeVar

      Self = TypeVar("Self", bound="Foo")

      class Foo:
          def return_self(self: Self) -> Self:
              ...
              return self

   En general, si algo devuelve "self", como en los ejemplos
   anteriores, se debe utilizar "Self" en la  anotación del retorno.
   Si "Foo.return_self" se anotó como que devuelve "”Foo”", entonces
   el validador de tipos inferiría que el objeto devuelto desde
   "SubclassOfFoo.return_self" es del tipo "Foo" en lugar de
   "SubclassOfFoo".

   Otros casos de uso comunes incluyen:

   * "classmethod" usados como constructores alternativos y retornan
     instancias del parámetro "cls".

   * Anotar un método "__enter__()" que retorna self.

   No debe utilizar "Self" como anotación de retorno si no se
   garantiza que el método devuelva una instancia de una subclase
   cuando la clase sea heredada:

      class Eggs:
          # Self would be an incorrect return annotation here,
          # as the object returned is always an instance of Eggs,
          # even in subclasses
          def returns_eggs(self) -> "Eggs":
              return Eggs()

   Véase **PEP 673** para más detalle.

   Added in version 3.11.

typing.TypeAlias

   Anotación especial para declarar explícitamente un alias de tipo.

   Por ejemplo:

      from typing import TypeAlias

      Factors: TypeAlias = list[int]

   "TypeAlias" es particularmente útil en versiones anteriores de
   Python para anotar alias que utilizan referencias para versiones
   posteriores, ya que puede ser difícil para los validadores de tipos
   distinguirlos de las asignaciones de variables normales:

      from typing import Generic, TypeAlias, TypeVar

      T = TypeVar("T")

      # "Box" aún no existe,
      # entonces tenemos que usar comillas para la referencia adelantada en Python <3.12.
      # Usando ``TypeAlias`` le dice al verificador de tipos que es una declaración de tipo alias,
      # no una asignacin de variable a un string.
      BoxOfStrings: TypeAlias = "Box[str]"

      class Box(Generic[T]):
          @classmethod
          def make_box_of_strings(cls) -> BoxOfStrings: ...

   Ver **PEP 613** para más detalle.

   Added in version 3.10.

   Obsoleto desde la versión 3.12: "TypeAlias" ha sido descontinuado
   en favor de la declaración "type", la cual crea instancias de
   "TypeAliasType" y que admite de forma nativa referencias de
   versiones posteriores de Python. Tenga en cuenta que, si bien
   "TypeAlias" y "TypeAliasType" tienen propósitos similares y tienen
   nombres similares, son distintos y el último no es el tipo del
   primero. La eliminación de "TypeAlias" no está prevista
   actualmente, pero se recomienda a los usuarios que migren a las
   declaraciones "type".

#### Formas especiales

Estos se pueden utilizar como tipos en anotaciones. Todos admiten la
suscripción mediante "[]", pero cada uno tiene una sintaxis única.

class typing.Union

   Tipo de unión; "Union[X, Y]" es equivalente a "X | Y" y significa X
   o Y.

   Para definir una unión, use p. ej. "Union[int, str]" o la
   abreviatura "int | str". Se recomienda el uso de la abreviatura.
   Detalles:

   * Los argumentos deben ser tipos y haber al menos uno.

   * Las uniones de uniones se simplifican (se aplanan), p. ej.:

        Union[Union[int, str], float] == Union[int, str, float]

     However, this does not apply to unions referenced through a type
     alias, to avoid forcing evaluation of the underlying
     "TypeAliasType":

        type A = Union[int, str]
        Union[A, float] != Union[int, str, float]

   * Las uniones con un solo argumento se eliminan, p. ej.:

        Union[int] == int  # El constructor de hecho retorna int

   * Argumentos repetidos se omiten, p. ej.:

        Union[int, str, int] == Union[int, str] == int | str

   * Cuando se comparan uniones, el orden de los argumentos se
     ignoran, p. ej.:

        Union[int, str] == Union[str, int]

   * No es posible crear una subclase o instanciar un "Union".

   * No es posible escribir "Union[X][Y]".

   Distinto en la versión 3.7: No elimina subclases explícitas de una
   unión en tiempo de ejecución.

   Distinto en la versión 3.10: Las uniones ahora se pueden escribir
   como "X | Y". Consulte union type expressions.

   Distinto en la versión 3.14: "types.UnionType" is now an alias for
   "Union", and both "Union[int, str]" and "int | str" create
   instances of the same class. To check whether an object is a
   "Union" at runtime, use "isinstance(obj, Union)". For compatibility
   with earlier versions of Python, use "get_origin(obj) is
   typing.Union or get_origin(obj) is types.UnionType".

typing.Optional

   "Optional[X]" es equivalente a "X | None" (o "Union[X, None]").

   Nótese que no es lo mismo que un argumento opcional, que es aquel
   que tiene un valor por defecto. Un argumento opcional con un valor
   por defecto no necesita el indicador "Optional" en su anotación de
   tipo simplemente por que sea opcional. Por ejemplo:

      def foo(arg: int = 0) -> None:
          ...

   Por otro lado, si se permite un valor "None", es apropiado el uso
   de "Optional", independientemente de que sea opcional o no. Por
   ejemplo:

      def foo(arg: Optional[int] = None) -> None:
          ...

   Distinto en la versión 3.10: Optional ahora se puede escribir como
   "X | None". Consulte union type expressions.

typing.Concatenate

   Forma especial para anotar funciones de orden superior.

   "Concatenate" can be used in conjunction with Callable and
   "ParamSpec" to annotate a higher-order callable which adds,
   removes, or transforms parameters of another callable.  Usage is in
   the form "Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable]".
   "Concatenate" is valid when used in Callable type hints and when
   instantiating user-defined generic classes with "ParamSpec"
   parameters. The last parameter to "Concatenate" must be a
   "ParamSpec" or ellipsis ("...").

   Por ejemplo, para anotar un decorador "with_lock" que proporciona
   un "threading.Lock" a la función decorada, "Concatenate" puede
   usarse para indicar que "with_lock" espera un invocable que toma un
   "Lock" como primer argumento y retorna un invocable con un tipo de
   firma diferente. En este caso, el "ParamSpec" indica que los tipos
   de parámetros de los invocables retornados dependen de los tipos de
   parámetros de los invocables que se pasan en

      from collections.abc import Callable
      from threading import Lock
      from typing import Concatenate

      # Utilice este bloqueo para garantizar que solo un hilo esté ejecutando una función
      # en cualquier momento.
      my_lock = Lock()

      def with_lock[**P, R](f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
          '''A type-safe decorator which provides a lock.'''
          def inner(*args: P.args, **kwargs: P.kwargs) -> R:
              # Proporcione el bloqueo como primer argumento.
              return f(my_lock, *args, **kwargs)
          return inner

      @with_lock
      def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
          '''Add a list of numbers together in a thread-safe manner.'''
          with lock:
              return sum(numbers)

      # No necesitamos pasar por la cerradura nosotros mismos gracias al decorador.
      sum_threadsafe([1.1, 2.2, 3.3])

   Added in version 3.10.

   Ver también:

     * **PEP 612** - Variables de especificación de parámetros (el PEP
       que introdujo "ParamSpec" y "Concatenate")

     * "ParamSpec"

     * Anotaciones en objetos invocables

typing.Literal

   Tipo especial que solo incluye cadenas literales.

   "Literal" se puede utilizar para indicar a los validadores de tipos
   que el objeto anotado tiene un valor equivalente a uno de los
   literales proporcionados.

   Por ejemplo:

      def validate_simple(data: Any) -> Literal[True]:  # siempre retorna True
          ...

      type Mode = Literal['r', 'rb', 'w', 'wb']
      def open_helper(file: str, mode: Mode) -> str:
          ...

      open_helper('/some/path', 'r')      # Pasa el verificador de tipos
      open_helper('/other/path', 'typo')  # Error en el verificador de tipos

   "Literal[...]" no puede ser derivado. En tiempo de ejecución, se
   permite un valor arbitrario como argumento de tipo de
   "Literal[...]", pero los validadores de tipos pueden imponer sus
   restricciones. Véase **PEP 585** para más detalles sobre tipos
   literales.

   Additional details:

   * The arguments must be literal values and there must be at least
     one.

   * Nested "Literal" types are flattened, e.g.:

        assert Literal[Literal[1, 2], 3] == Literal[1, 2, 3]

     However, this does not apply to "Literal" types referenced
     through a type alias, to avoid forcing evaluation of the
     underlying "TypeAliasType":

        type A = Literal[1, 2]
        assert Literal[A, 3] != Literal[1, 2, 3]

   * Argumentos repetidos se omiten, p. ej.:

        assert Literal[1, 2, 1] == Literal[1, 2]

   * When comparing literals, the argument order is ignored, e.g.:

        assert Literal[1, 2] == Literal[2, 1]

   * You cannot subclass or instantiate a "Literal".

   * You cannot write "Literal[X][Y]".

   Added in version 3.8.

   Distinto en la versión 3.9.1: "Literal" ahora elimina los
   parámetros duplicados. Las comparaciones de igualdad de los objetos
   "Literal" ya no dependen del orden. Los objetos "Literal" ahora
   lanzarán una excepción "TypeError" durante las comparaciones de
   igualdad si uno de sus parámetros no es *hashable*.

typing.ClassVar

   Construcción especial para tipado para marcar variables de clase.

   Tal y como introduce **PEP 526**, una anotación de variable rodeada
   por ClassVar indica que la intención de un atributo dado es ser
   usado como variable de clase y que no debería ser modificado en las
   instancias de esa misma clase. Uso:

      class Starship:
          stats: ClassVar[dict[str, int]] = {} # variable de clase
          damage: int = 10                     # variable de instancia

   "ClassVar" solo acepta tipos y no admite más niveles de subíndices.

   "ClassVar" is not a class itself, and cannot be used with
   "isinstance()" or "issubclass()". "ClassVar" does not change Python
   runtime behavior, but it can be used by static type checkers. For
   example, a type checker might flag the following code as an error:

      enterprise_d = Starship(3000)
      enterprise_d.stats = {} # Error, establece variable de clase en la instancia
      Starship.stats = {}     # Ésto está OK

   Added in version 3.5.3.

   Distinto en la versión 3.13: Ahora "ClassVar" se puede anidar en
   "Final" y viceversa.

typing.Final

   Construcción de tipado especial para indicar nombres finales a los
   validadores de tipos.

   Los nombres finales no se pueden reasignar en ningún ámbito. Los
   nombres finales declarados en ámbitos de clase no se pueden anular
   en subclases.

   Por ejemplo:

      MAX_SIZE: Final = 9000
      MAX_SIZE += 1  # Error reportado por un verificador de tipos

      class Connection:
          TIMEOUT: Final[int] = 10

      class FastConnector(Connection):
          TIMEOUT = 1  # Error reportado por un verificador de tipos

   No hay comprobación en tiempo de ejecución para estas propiedades.
   Véase **PEP 591** para más detalles.

   Added in version 3.8.

   Distinto en la versión 3.13: Ahora "Final" se puede anidar en
   "ClassVar" y viceversa.

typing.Required

   Construcción de tipado especial para marcar una clave "TypedDict"
   como requerida.

   Esto es útil principalmente para TypedDicts "total=False". Vea
   "TypedDict" y **PEP 655** para obtener más detalles.

   Added in version 3.11.

typing.NotRequired

   Construcción de tipado especial para marcar una clave "TypedDict"
   como potencialmente faltante.

   Véase "TypedDict" y **PEP 655** para más detalle.

   Added in version 3.11.

typing.ReadOnly

   Una construcción de tipificación especial para marcar un elemento
   de un "TypedDict" como de solo lectura.

   Por ejemplo:

      class Movie(TypedDict):
         title: ReadOnly[str]
         year: int

      def mutate_movie(m: Movie) -> None:
         m["year"] = 1999  # allowed
         m["title"] = "The Matrix"  # type checker error

   No hay ninguna comprobación en tiempo de ejecución para esta
   propiedad.

   Vea "TypedDict" y **PEP 705** para más detalle.

   Added in version 3.13.

typing.Annotated

   Forma de escritura especial para agregar metadatos específicos del
   contexto a una anotación.

   Agregue metadatos "x" a un tipo "T" determinado mediante la
   anotación "Annotated[T, x]". Los metadatos agregados mediante
   "Annotated" pueden usarse con herramientas de análisis estático o
   en tiempo de ejecución. En tiempo de ejecución, los metadatos se
   almacenan en un atributo "__metadata__".

   Si una biblioteca o herramienta encuentra una anotación
   "Annotated[T, x]" y no tiene una lógica especial para los
   metadatos, debe ignorar los metadatos y simplemente tratar la
   anotación como "T". Como tal, "Annotated" puede ser útil para el
   código que desea usar anotaciones para fines fuera del sistema de
   tipado estático de Python.

   Using "Annotated[T, x]" as an annotation still allows for static
   typechecking of "T", as type checkers will simply ignore the
   metadata "x". In this way, "Annotated" differs from the
   "@no_type_check" decorator, which can also be used for adding
   annotations outside the scope of the typing system, but completely
   disables typechecking for a function or class.

   La responsabilidad de interpretar los metadatos recae en la
   herramienta o biblioteca que encuentra una anotación "Annotated".
   Una herramienta o biblioteca que encuentra un tipo "Annotated"
   puede examinar los elementos de metadatos para determinar si son de
   interés (por ejemplo, utilizando "isinstance()").

   Annotated[<type>, <metadata>]

   A continuación se muestra un ejemplo de cómo podría utilizar
   "Annotated" para agregar metadatos a las anotaciones de tipo si
   estuviera realizando un análisis de rango:

      @dataclass
      class ValueRange:
          lo: int
          hi: int

      T1 = Annotated[int, ValueRange(-10, 5)]
      T2 = Annotated[T1, ValueRange(-20, 3)]

   The first argument to "Annotated" must be a valid type. Multiple
   metadata elements can be supplied as "Annotated" supports variadic
   arguments. The order of the metadata elements is preserved and
   matters for equality checks:

      @dataclass
      class ctype:
           kind: str

      a1 = Annotated[int, ValueRange(3, 10), ctype("char")]
      a2 = Annotated[int, ctype("char"), ValueRange(3, 10)]

      assert a1 != a2  # Order matters

   Depende de la herramienta que consume las anotaciones decidir si el
   cliente puede agregar varios elementos de metadatos a una anotación
   y cómo fusionar esas anotaciones.

   Los tipos anidados "Annotated" se aplanan. El orden de los
   elementos de metadatos comienza con la anotación más interna:

      assert Annotated[Annotated[int, ValueRange(3, 10)], ctype("char")] == Annotated[
          int, ValueRange(3, 10), ctype("char")
      ]

   However, this does not apply to "Annotated" types referenced
   through a type alias, to avoid forcing evaluation of the underlying
   "TypeAliasType":

      type From3To10[T] = Annotated[T, ValueRange(3, 10)]
      assert Annotated[From3To10[int], ctype("char")] != Annotated[
         int, ValueRange(3, 10), ctype("char")
      ]

   Los elementos de metadatos duplicados no se eliminan:

      assert Annotated[int, ValueRange(3, 10)] != Annotated[
          int, ValueRange(3, 10), ValueRange(3, 10)
      ]

   "Annotated" se puede utilizar con alias anidados y genéricos:

         @dataclass
         class MaxLen:
             value: int

         type Vec[T] = Annotated[list[tuple[T, T]], MaxLen(10)]

         # Cuando se utiliza en una anotación de tipo, un verificador de tipo tratará "V" de la misma manera que
         # ``Annotated[list[tuple[int, int]], MaxLen(10)]``:
         type V = Vec[int]

   No se puede utilizar "Annotated" con un "TypeVarTuple"
   descomprimido:

      type Variadic[*Ts] = Annotated[*Ts, Ann1] = Annotated[T1, T2, T3, ..., Ann1]  # NOT valid

   where "T1", "T2", ... are "TypeVars". This is invalid as only one
   type should be passed to Annotated.

   De forma predeterminada, "get_type_hints()" elimina los metadatos
   de las anotaciones. Pase "include_extras=True" para conservar los
   metadatos:

         >>> from typing import Annotated, get_type_hints
         >>> def func(x: Annotated[int, "metadata"]) -> None: pass
         ...
         >>> get_type_hints(func)
         {'x': <class 'int'>, 'return': <class 'NoneType'>}
         >>> get_type_hints(func, include_extras=True)
         {'x': typing.Annotated[int, 'metadata'], 'return': <class 'NoneType'>}

   En tiempo de ejecución, los metadatos asociados con un tipo
   "Annotated" se pueden recuperar a través del atributo
   "__metadata__":

         >>> from typing import Annotated
         >>> X = Annotated[int, "very", "important", "metadata"]
         >>> X
         typing.Annotated[int, 'very', 'important', 'metadata']
         >>> X.__metadata__
         ('very', 'important', 'metadata')

   If you want to retrieve the original type wrapped by "Annotated",
   use the "__origin__" attribute:

         >>> from typing import Annotated, get_origin
         >>> Password = Annotated[str, "secret"]
         >>> Password.__origin__
         <class 'str'>

   Tenga en cuenta que el uso de "get_origin()" devolverá el mismo
   "Annotated":

         >>> get_origin(Password)
         typing.Annotated

   Ver también:

     **PEP 593** - Anotaciones flexibles de funciones y variables
        El PEP introduce "Annotated" en la biblioteca estándar.

   Added in version 3.9.

typing.TypeIs

   Construcción de tipificación especial para marcar funciones de
   predicado de tipo definido por el usuario.

   "TypeIs" se puede utilizar para anotar el tipo de retorno de una
   función de predicado de tipo definida por el usuario. "TypeIs" solo
   acepta un único argumento de tipo. En tiempo de ejecución, las
   funciones marcadas de esta manera deben devolver un valor booleano
   y tomar al menos un argumento posicional.

   "TypeIs" tiene como objetivo beneficiar a *type narrowing*, una
   técnica utilizada por los verificadores de tipos estáticos para
   determinar un tipo más preciso de una expresión dentro del flujo de
   código de un programa. Por lo general, la restricción de tipos se
   realiza analizando el flujo de código condicional y aplicando la
   restricción a un bloque de código. La expresión condicional aquí a
   veces se denomina "predicado de tipo":

      def is_str(val: str | float):
          # "isinstance" predicado de tipo
          if isinstance(val, str):
              # Tipo de ``val`` se reduce a ``str``
              ...
          else:
              # De lo contrario, el tipo de ``val`` se limita a ``float``.
              ...

   A veces sería conveniente utilizar una función booleana definida
   por el usuario como predicado de tipo. Dicha función debería
   utilizar "TypeIs[...]" o "TypeGuard" como su tipo de retorno para
   alertar a los verificadores de tipos estáticos sobre esta
   intención. "TypeIs" suele tener un comportamiento más intuitivo que
   "TypeGuard", pero no se puede utilizar cuando los tipos de entrada
   y salida son incompatibles (por ejemplo, "list[object]" a
   "list[int]") o cuando la función no devuelve "True" para todas las
   instancias del tipo restringido.

   El uso de "-> TypeIs[NarrowedType]" le indica al verificador de
   tipo estático que para una función determinada:

   1. El valor de retorno es un booleano.

   2. Si el valor de retorno es "True", el tipo de su argumento es la
      intersección del tipo original del argumento y "NarrowedType".

   3. Si el valor de retorno es "False", el tipo de su argumento se
      limita para excluir "NarrowedType".

   Por ejemplo:

      from typing import assert_type, final, TypeIs

      class Parent: pass
      class Child(Parent): pass
      @final
      class Unrelated: pass

      def is_parent(val: object) -> TypeIs[Parent]:
          return isinstance(val, Parent)

      def run(arg: Child | Unrelated):
          if is_parent(arg):
              # El tipo de ``arg`` es reducido a la intersección
              # de ``Parent`` y ``Child``, lo cual es equivalente a
              # ``Child``.
              assert_type(arg, Child)
          else:
              # El tipo de  ``arg`` es reducido para excluir ``Parent``,
              # para que solo quede ``Unrelated``.
              assert_type(arg, Unrelated)

   El tipo dentro de "TypeIs" debe ser coherente con el tipo del
   argumento de la función; si no lo es, los comprobadores de tipos
   estáticos generarán un error. Una función "TypeIs" escrita
   incorrectamente puede provocar un comportamiento incorrecto en el
   sistema de tipos; es responsabilidad del usuario escribir dichas
   funciones de manera segura.

   Si una función "TypeIs" es un método de clase o instancia, entonces
   el tipo en "TypeIs" se asigna al tipo del segundo parámetro
   (después de "cls" o "self").

   En resumen, la forma "def foo(arg: TypeA) -> TypeIs[TypeB]: ...",
   significa que si "foo(arg)" devuelve "True", entonces "arg" es una
   instancia de "TypeB", y si devuelve "False", no es una instancia de
   "TypeB".

   "TypeIs" también funciona con variables de tipo. Para obtener más
   información, consulte **PEP 742** (Restringir tipos con "TypeIs").

   Added in version 3.13.

typing.TypeGuard

   Construcción de tipificación especial para marcar funciones de
   predicado de tipo definido por el usuario.

   Las funciones de predicado de tipo son funciones definidas por el
   usuario que indican si su argumento es una instancia de un tipo en
   particular. "TypeGuard" funciona de manera similar a "TypeIs", pero
   tiene efectos ligeramente diferentes en el comportamiento de
   verificación de tipo (ver a continuación).

   El uso de "-> TypeGuard" le dice al validador de tipo estático que
   para una función determinada:

   1. El valor de retorno es un booleano.

   2. Si el valor de retorno es "True", el tipo de su argumento es el
      tipo dentro de "TypeGuard".

   "TypeGuard" también funciona con variables de tipo. Véase **PEP
   647** para más detalles.

   Por ejemplo:

      def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
          '''Determines whether all objects in the list are strings'''
          return all(isinstance(x, str) for x in val)

      def func1(val: list[object]):
          if is_str_list(val):
              # El tipo de ``val`` es reducido a ``list[str]``.
              print(" ".join(val))
          else:
              # El tipo de ``val`` se mantiene como ``list[object]``.
              print("Not a list of strings!")

   "TypeIs" y "TypeGuard" se diferencian en los siguientes aspectos:

   * "TypeIs" requiere que el tipo restringido sea un subtipo del tipo
     de entrada, mientras que "TypeGuard" no lo requiere. La razón
     principal es permitir cosas como restringir "list[object]" a
     "list[str]", aunque este último no sea un subtipo del primero, ya
     que "list" es invariante.

   * Cuando una función "TypeGuard" devuelve "True", los verificadores
     de tipo limitan el tipo de la variable exactamente al tipo
     "TypeGuard". Cuando una función "TypeIs" devuelve "True", los
     verificadores de tipo pueden inferir un tipo más preciso
     combinando el tipo conocido previamente de la variable con el
     tipo "TypeIs". (Técnicamente, esto se conoce como un tipo de
     intersección).

   * Cuando una función "TypeGuard" devuelve "False", los
     verificadores de tipo no pueden limitar el tipo de la variable en
     absoluto. Cuando una función "TypeIs" devuelve "False", los
     verificadores de tipo pueden limitar el tipo de la variable para
     excluir el tipo "TypeIs".

   Added in version 3.10.

typing.Unpack

   Tipado para marcar conceptualmente un objeto como si hubiera sido
   desempaquetado.

   Por ejemplo, usar el operador de descompresión "*" en un type
   variable tuple es equivalente a usar "Unpack" para marcar la tupla
   de variable de tipo como descomprimida:

      Ts = TypeVarTuple('Ts')
      tup: tuple[*Ts]
      # Effectively does:
      tup: tuple[Unpack[Ts]]

   De hecho, "Unpack" se puede usar indistintamente con "*" en el
   contexto de los tipos "typing.TypeVarTuple" y "builtins.tuple". Es
   posible que veas que "Unpack" se usa explícitamente en versiones
   anteriores de Python, donde "*" no se podía usar en ciertos
   lugares:

      # En versiones anteriores de Python, TypeVarTuple y Unpack
      # se encuentran en el paquete de retroadaptación `typing_extensions`.
      from typing_extensions import TypeVarTuple, Unpack

      Ts = TypeVarTuple('Ts')
      tup: tuple[*Ts]         # Error de sintaxis en Python <= 3.10!
      tup: tuple[Unpack[Ts]]  # Equivalente semánticamente, y compatible con versiones anteriores

   "Unpack" también se puede usar junto con "typing.TypedDict" para
   tipear "**kwargs" en una firma de función:

      from typing import TypedDict, Unpack

      class Movie(TypedDict):
          name: str
          year: int

      # Esta función espera dos argumentos de palabras clave: `name` de tipo `str`
      # y `year` de tipo `int`.
      def foo(**kwargs: Unpack[Movie]): ...

   Consulte **PEP 692** para obtener más información sobre el uso de
   "Unpack" para tipear "**kwargs".

   Added in version 3.11.

#### Creación de tipos genéricos y alias de tipos

Las siguientes clases no se deben utilizar directamente como
anotaciones. Su finalidad es servir de bloques de construcción para
crear tipos genéricos y alias de tipos.

Estos objetos se pueden crear mediante una sintaxis especial (type
parameter lists y la declaración "type"). Para compatibilidad con
Python 3.11 y versiones anteriores, también se pueden crear sin la
sintaxis dedicada, como se documenta a continuación.

class typing.Generic

   Clase base abstracta para tipos genéricos.

   Un tipo genérico normalmente se declara agregando una lista de
   parámetros de tipo después del nombre de la clase:

      class Mapping[KT, VT]:
          def __getitem__(self, key: KT) -> VT:
              ...
              # Etc.

   Esta clase hereda implícitamente de "Generic". La semántica de
   tiempo de ejecución de esta sintaxis se analiza en la Referencia
   del lenguaje.

   Entonces, esta clase se puede usar como sigue:

      def lookup_name[X, Y](mapping: Mapping[X, Y], key: X, default: Y) -> Y:
          try:
              return mapping[key]
          except KeyError:
              return default

   Aquí los corchetes después del nombre de la función indican una
   función genérica.

   Para compatibilidad con versiones anteriores, las clases genéricas
   también se pueden declarar heredando explícitamente de "Generic".
   En este caso, los parámetros de tipo se deben declarar por
   separado:

      KT = TypeVar('KT')
      VT = TypeVar('VT')

      class Mapping(Generic[KT, VT]):
          def __getitem__(self, key: KT) -> VT:
              ...
              # Etc.

class typing.TypeVar(name, *constraints, bound=None, covariant=False, contravariant=False, infer_variance=False, default=typing.NoDefault)

   Variable de tipo.

   La forma preferida de construir una variable de tipo es a través de
   la sintaxis dedicada para funciones genéricas, clases genéricas y
   alias de tipo genérico:

      class Sequence[T]:  # T is a TypeVar
          ...

   This syntax can also be used to create bounded and constrained type
   variables:

      class StrSequence[S: str]:  # S is a TypeVar with a `str` upper bound;
          ...                     # we can say that S is "bounded by `str`"

      class StrOrBytesSequence[A: (str, bytes)]:  # A is a TypeVar constrained to str or bytes
          ...

   Sin embargo, si se desea, también se pueden construir manualmente
   variables de tipo reutilizables, de la siguiente manera:

      T = TypeVar('T')  # Puede ser cualquier cosa
      S = TypeVar('S', bound=str)  # Puede ser cualquier subtipo de str
      A = TypeVar('A', str, bytes)  # Tiene que ser exactamente str o bytes

   Las variables de tipo existen principalmente para el beneficio de
   los validadores de tipos estáticos. Sirven como parámetros para
   tipos genéricos, así como para definiciones de alias de tipo y
   funciones genéricas. Consulte "Generic" para obtener más
   información sobre tipos genéricos. Las funciones genéricas
   funcionan de la siguiente manera:

      def repeat[T](x: T, n: int) -> Sequence[T]:
          """Return a list containing n references to x."""
          return [x]*n

      def print_capitalized[S: str](x: S) -> S:
          """Print x capitalized, and return x."""
          print(x.capitalize())
          return x

      def concatenate[A: (str, bytes)](x: A, y: A) -> A:
          """Add two strings or bytes objects together."""
          return x + y

   Note that type variables can be *bounded*, *constrained*, or
   neither, but cannot be both bounded *and* constrained.

   La varianza de las variables de tipo es inferida por los
   validadores de tipo cuando se crean a través de la sintáxis de
   parámetros de tipo o cuando se pasa "infer_variance=True". Las
   variables de tipo creadas manualmente se pueden marcar
   explícitamente como covariantes o contravariantes al pasar
   "covariant=True" o "contravariant=True". De manera predeterminada,
   las variables de tipo creadas manualmente son invariantes. Consulte
   **PEP 484** y **PEP 695** para obtener más detalles.

   Bounded type variables and constrained type variables have
   different semantics in several important ways. Using a *bounded*
   type variable means that the "TypeVar" will be solved using the
   most specific type possible:

      x = print_capitalized('a string')
      reveal_type(x)  # el tipo revelado es str

      class StringSubclass(str):
          pass

      y = print_capitalized(StringSubclass('another string'))
      reveal_type(y)  # revealed type is StringSubclass

      z = print_capitalized(45)  # error: int no es un subtipo de str

   The upper bound of a type variable can be a concrete type, abstract
   type (ABC or Protocol), or even a union of types:

      # Puede ser cualquier cosa con un método __abs__
      def print_abs[T: SupportsAbs](arg: T) -> None:
          print("Absolute value:", abs(arg))

      U = TypeVar('U', bound=str|bytes)  # Puede ser cualquier subtipo de la unión str|bytes
      V = TypeVar('V', bound=SupportsAbs)  # Puede ser cualquier cosa con un método __abs__

   Sin embargo, usar una variable de tipo *constrained* significa que
   la "TypeVar" sólo podrá ser determinada como exactamente una de las
   restricciones dadas:

      a = concatenate('one', 'two')
      reveal_type(a)  # tipo revelado es str

      b = concatenate(StringSubclass('one'), StringSubclass('two'))
      reveal_type(b)  # tipo revelado es str, a pesar que se pasa StringSubclass

      c = concatenate('one', b'two')  # error: la variable de tipo 'A' puede ser str o bytes en una llamada a función, pero no ambas

   En tiempo de ejecución, "isinstance(x, T)" lanzará "TypeError".

   __name__

      El nombre de la variable de tipo.

   __covariant__

      Si la variable de tipo ha sido marcado explícitamente como
      covariante.

   __contravariant__

      Si la variable de tipo ha sido marcado explícitamente como
      covariante.

   __infer_variance__

      Si los validadores de tipo deben inferir la variación de la
      variable de tipo.

      Added in version 3.12.

   __bound__

      The upper bound of the type variable, if any.

      Distinto en la versión 3.12: Para las variables de tipo creadas
      a través de sintáxis de parámetros de tipo, el límite se evalúa
      solo cuando se accede al atributo, no cuando se crea la variable
      de tipo (consulte Evaluación perezosa).

   evaluate_bound()

      An *evaluate function* corresponding to the "__bound__"
      attribute. When called directly, this method supports only the
      "VALUE" format, which is equivalent to accessing the "__bound__"
      attribute directly, but the method object can be passed to
      "annotationlib.call_evaluate_function()" to evaluate the value
      in a different format.

      Added in version 3.14.

   __constraints__

      Una tupla que contiene las restricciones de la variable de tipo,
      si las hay.

      Distinto en la versión 3.12: Para las variables de tipo creadas
      a través de la sintáxis de parámetros de tipo, las restricciones
      se evalúan solo cuando se accede al atributo, no cuando se crea
      la variable de tipo (consulte Evaluación perezosa).

   evaluate_constraints()

      An *evaluate function* corresponding to the "__constraints__"
      attribute. When called directly, this method supports only the
      "VALUE" format, which is equivalent to accessing the
      "__constraints__" attribute directly, but the method object can
      be passed to "annotationlib.call_evaluate_function()" to
      evaluate the value in a different format.

      Added in version 3.14.

   __default__

      El valor predeterminado de la variable de tipo, o
      "typing.NoDefault" si no tiene valor predeterminado.

      Added in version 3.13.

   evaluate_default()

      An *evaluate function* corresponding to the "__default__"
      attribute. When called directly, this method supports only the
      "VALUE" format, which is equivalent to accessing the
      "__default__" attribute directly, but the method object can be
      passed to "annotationlib.call_evaluate_function()" to evaluate
      the value in a different format.

      Added in version 3.14.

   has_default()

      Devuelve si la variable de tipo tiene o no un valor
      predeterminado. Esto es equivalente a verificar si "__default__"
      no es el singleton "typing.NoDefault", excepto que no fuerza la
      evaluación del valor predeterminado lazily evaluated.

      Added in version 3.13.

   Distinto en la versión 3.12: Ahora es posible declarar variables de
   tipo utilizando la sintaxis de parámetros de tipo introducida por
   **PEP 695**. Se agregó el parámetro "infer_variance".

   Distinto en la versión 3.13: Se agregó soporte para valores
   predeterminados.

class typing.TypeVarTuple(name, *, default=typing.NoDefault)

   Tupla de variable de tipo. Forma especializada de type variable que
   habilita genéricos de *variadic*.

   Las tuplas de variables de tipo se pueden declarar en listas de
   parámetros de tipo usando un solo asterisco ("*") antes del nombre:

      def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
          return (*tup[1:], tup[0])

   O invocando explícitamente el constructor "TypeVarTuple":

      T = TypeVar("T")
      Ts = TypeVarTuple("Ts")

      def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
          return (*tup[1:], tup[0])

   Una variable de tipo normal permite parametrizar con un solo tipo.
   Una tupla de variables de tipo, en contraste, permite la
   parametrización con un número *arbitrario* de tipos, al actuar como
   un número *arbitrario* de variables de tipo envueltas en una tupla.
   Por ejemplo:

      # T está ligado a int, Ts está ligado a ()
      # El valor de retorno es (1,), que tiene tipo tuple[int]
      move_first_element_to_last(tup=(1,))

      # T está ligado a int, Ts está ligado a (str,)
      # El valor de retorno es ('spam', 1), que tiene tipo tuple[str, int]
      move_first_element_to_last(tup=(1, 'spam'))

      # T está ligado a int, Ts está ligado a (str, float)
      # El valor de retorno es ('spam', 3.0, 1), que tiene tipo tuple[str, float, int]
      move_first_element_to_last(tup=(1, 'spam', 3.0))

      # Esto falla al verificar el tipo (y falla en tiempo de ejecución)
      # porque tuple[()] no es compatible con tuple[T, *Ts]
      # (se requiere al menos un elemento)
      move_first_element_to_last(tup=())

   Nótese el uso del operador de desempaquetado "*" en "tuple[T,
   *Ts]". Conceptualmente, puede pensarse en "Ts" como una tupla de
   variables de tipo "(T1, T2, ...)". "tuple[T, *Ts]" se convertiría
   en "tuple[T, *(T1, T2, ...)]", lo que es equivalente a "tuple[T,
   T1, T2, ...]". (Nótese que en versiones más antiguas de Python,
   ésto puede verse escrito usando en cambio "Unpack", en la forma
   "Unpack[Ts]".)

   Las tuplas de variables de tipo *siempre* deben descomprimirse.
   Esto ayuda a distinguir las tuplas de variables de tipo, de las
   variables de tipo normales:

      x: Ts          # No válido
      x: tuple[Ts]   # No válido
      x: tuple[*Ts]  # La forma correcta de hacerlo

   Las tuplas de variables de tipo pueden ser utilizadas en los mismos
   contextos que las variables de tipo normales. Por ejemplo en
   definiciones de clases, argumentos y tipos de retorno:

      class Array[*Shape]:
          def __getitem__(self, key: tuple[*Shape]) -> float: ...
          def __abs__(self) -> "Array[*Shape]": ...
          def get_shape(self) -> tuple[*Shape]: ...

   Las tuplas de variables de tipo se pueden combinar sin problemas
   con variables de tipo normales:

      class Array[DType, *Shape]:  # Esto está bien
          pass

      class Array2[*Shape, DType]:  # Esto también está bien
          pass

      class Height: ...
      class Width: ...

      float_array_1d: Array[float, Height] = Array()     # Totalmente bien
      int_array_2d: Array[int, Height, Width] = Array()  # Sip, también está bien

   Sin embargo, nótese que en una determinada lista de argumentos de
   tipo o de parámetros de tipo puede haber como máximo una tupla de
   variables de tipo:

      x: tuple[*Ts, *Ts]            # Not valid
      class Array[*Shape, *Shape]:  # Not valid
          pass

   Finalmente, una tupla de variables de tipo desempaquetada puede ser
   utilizada como la anotación de tipo de "*args":

      def call_soon[*Ts](
          callback: Callable[[*Ts], None],
          *args: *Ts
      ) -> None:
          ...
          callback(*args)

   En contraste con las anotaciones no-desempaquetadas de "*args", por
   ej. "*args: int", que especificaría que *todos* los argumentos son
   "int" - "*args: *Ts" permite referenciar los tipos de los
   argumentos *individuales* en "*args". Aquí, ésto permite asegurarse
   de que los tipos de los "*args" que son pasados a "call_soon"
   calcen con los tipos de los argumentos (posicionales) de
   "callback".

   Véase **PEP 646** para obtener más detalles sobre las tuplas de
   variables de tipo.

   __name__

      El nombre de la tupla de variables de tipo.

   __default__

      El valor predeterminado de la variable de tipo tupla, o
      "typing.NoDefault" si no tiene valor predeterminado.

      Added in version 3.13.

   evaluate_default()

      An *evaluate function* corresponding to the "__default__"
      attribute. When called directly, this method supports only the
      "VALUE" format, which is equivalent to accessing the
      "__default__" attribute directly, but the method object can be
      passed to "annotationlib.call_evaluate_function()" to evaluate
      the value in a different format.

      Added in version 3.14.

   has_default()

      Devuelve si la variable de tipo tupla tiene o no un valor
      predeterminado. Esto es equivalente a verificar si "__default__"
      no es el singleton "typing.NoDefault", excepto que no fuerza la
      evaluación del valor predeterminado lazily evaluated.

      Added in version 3.13.

   Added in version 3.11.

   Distinto en la versión 3.12: Ahora es posible declarar tuplas de
   variables de tipo utilizando la sintaxis de parámetros de tipo
   introducida por **PEP 695**.

   Distinto en la versión 3.13: Se agregó soporte para valores
   predeterminados.

class typing.ParamSpec(name, *, bound=None, covariant=False, contravariant=False, infer_variance=False, default=typing.NoDefault)

   Variable de especificación de parámetros. Versión especializada de
   type variables.

   En las listas de parámetros de tipo, las especificaciones de
   parámetros se pueden declarar con dos asteriscos ("**"):

      type IntFunc[**P] = Callable[P, int]

   Para compatibilidad con Python 3.11 y versiones anteriores, los
   objetos "ParamSpec" también se pueden crear de la siguiente manera:

      P = ParamSpec('P')

   Las variables de especificación de parámetros existen
   principalmente para el beneficio de los validadores de tipo
   estático. Se utilizan para reenviar los tipos de parámetros de un
   invocable a otro invocable, un patrón que se encuentra comúnmente
   en funciones y decoradores de orden superior. Solo son válidos
   cuando se utilizan en "Concatenate", o como primer argumento de
   "Callable", o como parámetros para genéricos definidos por el
   usuario. Consulte "Generic" para obtener más información sobre
   tipos genéricos.

   Por ejemplo, para agregar un registro básico a una función, se
   puede crear un decorador "add_logging" para registrar llamadas a
   funciones. La variable de especificación de parámetros le dice al
   validador de tipo que el invocable pasado al decorador y el nuevo
   invocable retornado por él tienen parámetros de tipo
   interdependientes:

      from collections.abc import Callable
      import logging

      def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
          '''A type-safe decorator to add logging to a function.'''
          def inner(*args: P.args, **kwargs: P.kwargs) -> T:
              logging.info(f'{f.__name__} was called')
              return f(*args, **kwargs)
          return inner

      @add_logging
      def add_two(x: float, y: float) -> float:
          '''Add two numbers together.'''
          return x + y

   Without "ParamSpec", the simplest way to annotate this previously
   was to use a "TypeVar" with upper bound "Callable[..., Any]".
   However this causes two problems:

   1. El validador de tipo no puede verificar la función "inner"
      porque "*args" y "**kwargs" deben escribirse "Any".

   2. Es posible que se requiera "cast()" en el cuerpo del decorador
      "add_logging" al retornar la función "inner", o se debe indicar
      al validador de tipo estático que ignore el "return inner".

   args

   kwargs

      Dado que "ParamSpec" captura tanto parámetros posicionales como
      de palabras clave, "P.args" y "P.kwargs" se pueden utilizar para
      dividir un "ParamSpec" en sus componentes. "P.args" representa
      la tupla de parámetros posicionales en una llamada determinada y
      solo debe usarse para anotar "*args". "P.kwargs" representa la
      asignación de parámetros de palabras clave a sus valores en una
      llamada determinada y solo debe usarse para anotar "**kwargs".
      Ambos atributos requieren que el parámetro anotado esté dentro
      del alcance. En tiempo de ejecución, "P.args" y "P.kwargs" son
      instancias respectivamente de "ParamSpecArgs" y
      "ParamSpecKwargs".

   __name__

      El nombre de la especificación del parámetro.

   __default__

      El valor predeterminado de la especificación del parámetro, o
      "typing.NoDefault" si no tiene valor predeterminado.

      Added in version 3.13.

   evaluate_default()

      An *evaluate function* corresponding to the "__default__"
      attribute. When called directly, this method supports only the
      "VALUE" format, which is equivalent to accessing the
      "__default__" attribute directly, but the method object can be
      passed to "annotationlib.call_evaluate_function()" to evaluate
      the value in a different format.

      Added in version 3.14.

   has_default()

      Devuelve si la especificación del parámetro tiene o no un valor
      predeterminado. Esto es equivalente a verificar si "__default__"
      no es el singleton "typing.NoDefault", excepto que no fuerza la
      evaluación del valor predeterminado lazily evaluated.

      Added in version 3.13.

   Las variables de especificación de parámetros creadas con
   "covariant=True" o "contravariant=True" se pueden utilizar para
   declarar tipos genéricos covariantes o contravariantes. También se
   acepta el argumento "bound", similar a "TypeVar". Sin embargo, la
   semántica real de estas palabras clave aún no se ha decidido.

   Added in version 3.10.

   Distinto en la versión 3.12: Las especificaciones de parámetros
   ahora se pueden declarar utilizando la sintaxis de parámetros de
   tipo introducida por **PEP 695**.

   Distinto en la versión 3.13: Se agregó soporte para valores
   predeterminados.

   Nota:

     Solo las variables de especificación de parámetros definidas en
     el ámbito global pueden ser serializadas.

   Ver también:

     * **PEP 612** - Variables de especificación de parámetros (el PEP
       que introdujo "ParamSpec" y "Concatenate")

     * "Concatenate"

     * Anotaciones en objetos invocables

class typing.ParamSpecArgs
class typing.ParamSpecKwargs

   Argumentos y atributos de argumentos de palabras clave de un
   "ParamSpec". El atributo "P.args" de un "ParamSpec" es una
   instancia de "ParamSpecArgs" y "P.kwargs" es una instancia de
   "ParamSpecKwargs". Están pensados para la introspección en tiempo
   de ejecución y no tienen un significado especial para los
   validadores de tipo estático.

   Llamar a "get_origin()" en cualquiera de estos objetos retornará el
   "ParamSpec" original:

      >>> from typing import ParamSpec, get_origin
      >>> P = ParamSpec("P")
      >>> get_origin(P.args) is P
      True
      >>> get_origin(P.kwargs) is P
      True

   Added in version 3.10.

class typing.TypeAliasType(name, value, *, type_params=())

   El tipo de alias de tipo creado a través de la declaración "type".

   Por ejemplo:

      >>> type Alias = int
      >>> type(Alias)
      <class 'typing.TypeAliasType'>

   Added in version 3.12.

   __name__

      El nombre del alias de tipo:

         >>> type Alias = int
         >>> Alias.__name__
         'Alias'

   __module__

      The name of the module in which the type alias was defined:

         >>> type Alias = int
         >>> Alias.__module__
         '__main__'

   __type_params__

      Los parámetros de tipo del alias de tipo, o una tupla vacía si
      el alias no es genérico:

         >>> type ListOrSet[T] = list[T] | set[T]
         >>> ListOrSet.__type_params__
         (T,)
         >>> type NotGeneric = int
         >>> NotGeneric.__type_params__
         ()

   __value__

      El valor del alias de tipo. Se evalúa de forma diferida, por lo
      que los nombres utilizados en la definición del alias no se
      resuelven hasta que se accede al atributo "__value__":

         >>> type Mutually = Recursive
         >>> type Recursive = Mutually
         >>> Mutually
         Mutually
         >>> Recursive
         Recursive
         >>> Mutually.__value__
         Recursive
         >>> Recursive.__value__
         Mutually

   evaluate_value()

      An *evaluate function* corresponding to the "__value__"
      attribute. When called directly, this method supports only the
      "VALUE" format, which is equivalent to accessing the "__value__"
      attribute directly, but the method object can be passed to
      "annotationlib.call_evaluate_function()" to evaluate the value
      in a different format:

         >>> type Alias = undefined
         >>> Alias.__value__
         Traceback (most recent call last):
         ...
         NameError: name 'undefined' is not defined
         >>> from annotationlib import Format, call_evaluate_function
         >>> Alias.evaluate_value(Format.VALUE)
         Traceback (most recent call last):
         ...
         NameError: name 'undefined' is not defined
         >>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
         ForwardRef('undefined')

      Added in version 3.14.

   -[ Unpacking ]-

   Type aliases support star unpacking using the "*Alias" syntax. This
   is equivalent to using "Unpack[Alias]" directly:

      >>> type Alias = tuple[int, str]
      >>> type Unpacked = tuple[bool, *Alias]
      >>> Unpacked.__value__
      tuple[bool, typing.Unpack[Alias]]

   Added in version 3.14.

#### Otras directivas especiales

Estas funciones y clases no se deben utilizar directamente como
anotaciones. Su finalidad es servir de bloques de construcción para
crear y declarar tipos.

class typing.NamedTuple

   Versión para anotación de tipos de "collections.namedtuple()".

   Uso:

      class Employee(NamedTuple):
          name: str
          id: int

   Esto es equivalente a:

      Employee = collections.namedtuple('Employee', ['name', 'id'])

   Para proporcionar a un campo un valor por defecto se puede asignar
   en el cuerpo de la clase:

      class Employee(NamedTuple):
          name: str
          id: int = 3

      employee = Employee('Guido')
      assert employee.id == 3

   Los campos con un valor por defecto deben ir después de los campos
   sin valor por defecto.

   The types for each field name can be retrieved by calling
   "annotationlib.get_annotations()" on the resulting class. (The
   field names are in the "_fields" attribute and the default values
   are in the "_field_defaults" attribute, both of which are part of
   the "namedtuple()" API.)

   Las subclases de "NamedTuple" también pueden tener *docstrings* y
   métodos:

      class Employee(NamedTuple):
          """Represents an employee."""
          name: str
          id: int = 3

          def __repr__(self) -> str:
              return f'<Employee {self.name}, id={self.id}>'

   Las subclases de "NamedTuple" pueden ser genéricas:

      class Group[T](NamedTuple):
          key: T
          group: list[T]

   Uso retrocompatible:

      # Para crear un NamedTuple genérico en Python 3.11
      T = TypeVar("T")

      class Group(NamedTuple, Generic[T]):
          key: T
          group: list[T]

      # También se admite una sintaxis funcional
      Employee = NamedTuple('Employee', [('name', str), ('id', int)])

   Distinto en la versión 3.6: Soporte añadido para la sintaxis de
   anotación de variables propuesto en **PEP 526**.

   Distinto en la versión 3.6.1: Soporte añadido para valores por
   defecto, métodos y *docstrings*.

   Distinto en la versión 3.8: Los atributos "_field_types" y
   "__annotations__" son simples diccionarios en vez de instancias de
   "OrderedDict".

   Distinto en la versión 3.9: Se remueve el atributo "_field_types"
   en favor del atributo más estándar "__annotations__" que tiene la
   misma información.

   Distinto en la versión 3.9: "NamedTuple" is now a function rather
   than a class. It can still be used as a class base, as described
   above.

   Distinto en la versión 3.11: Se agrega soporte para *namedtuples*
   genéricas.

   Distinto en la versión 3.14: Using "super()" (and the "__class__"
   *closure variable*) in methods of "NamedTuple" subclasses is
   unsupported and causes a "TypeError".

   Deprecated since version 3.13, will be removed in version 3.15: La
   sintaxis de argumentos de palabras clave no documentada para crear
   clases NamedTuple ("NT = NamedTuple("NT", x=int)") está obsoleta y
   no se permitirá en la versión 3.15. En su lugar, utilice la
   sintaxis basada en clases o la sintaxis funcional.

   Deprecated since version 3.13, will be removed in version 3.15: Al
   utilizar la sintaxis funcional para crear una clase NamedTuple, no
   se permite pasar un valor al parámetro 'campos' ("NT =
   NamedTuple("NT")"). También se permite pasar "None" al parámetro
   'campos' ("NT = NamedTuple("NT", None)"). Ambos métodos no estarán
   permitidos en Python 3.15. Para crear una clase NamedTuple con 0
   campos, utilice "class NT(NamedTuple): pass" o "NT =
   NamedTuple("NT", [])".

class typing.NewType(name, tp)

   Clase auxiliar para crear tipos distintos con bajo consumo de
   recursos.

   A "NewType" is considered a distinct type by a type checker. At
   runtime, however, calling a "NewType" returns its argument
   unchanged.

   Uso:

      UserId = NewType('UserId', int)  # Declara el NewType "UserId"
      first_user = UserId(1)  # "UserId" retorna el argumento sin cambios en runtime

   __module__

      The name of the module in which the new type is defined.

   __name__

      El nombre del nuevo tipo.

   __supertype__

      El tipo en el que se basa el nuevo tipo.

   Added in version 3.5.2.

   Distinto en la versión 3.10: "NewType" es ahora una clase en lugar
   de una función.

class typing.Protocol(Generic)

   Clase base para clases de protocolo.

   Las clases de protocolo se definen así:

      class Proto(Protocol):
          def meth(self) -> int:
              ...

   Tales clases son usadas principalmente con validadores estáticos de
   tipos que detectan subtipado estructural (*duck-typing* estático),
   por ejemplo:

      class C:
          def meth(self) -> int:
              return 0

      def func(x: Proto) -> int:
          return x.meth()

      func(C())  # Pasa la verificación de tipos estática

   See **PEP 544** for more details. Protocol classes decorated with
   "@runtime_checkable" (described later) act as simple-minded runtime
   protocols that check only the presence of given attributes,
   ignoring their type signatures. Protocol classes without this
   decorator cannot be used as the second argument to "isinstance()"
   or "issubclass()".

   Las clases protocolo pueden ser genéricas, por ejemplo:

      class GenProto[T](Protocol):
          def meth(self) -> T:
              ...

   En el código que necesita ser compatible con Python 3.11 o
   anterior, los protocolos genéricos se pueden escribir de la
   siguiente manera:

      T = TypeVar("T")

      class GenProto(Protocol[T]):
          def meth(self) -> T:
              ...

   Added in version 3.8.

@typing.runtime_checkable

   Marca una clase protocolo como aplicable en tiempo de ejecución (lo
   convierte en un *runtime protocol*).

   Such a protocol can be used with "isinstance()" and "issubclass()".
   This allows a simple-minded structural check, very similar to "one-
   trick ponies" in "collections.abc" such as "Iterable".  For
   example:

      @runtime_checkable
      class Closable(Protocol):
          def close(self): ...

      assert isinstance(open('/some/file'), Closable)

      @runtime_checkable
      class Named(Protocol):
          name: str

      import threading
      assert isinstance(threading.Thread(name='Bob'), Named)

   This decorator raises "TypeError" when applied to a non-protocol
   class.

   Nota:

     "@runtime_checkable" will check only the presence of the required
     methods or attributes, not their type signatures or types. For
     example, "ssl.SSLObject" is a class, therefore it passes an
     "issubclass()" check against Callable. However, the
     "ssl.SSLObject.__init__" method exists only to raise a
     "TypeError" with a more informative message, therefore making it
     impossible to call (instantiate) "ssl.SSLObject".

   Nota:

     Una verificación "isinstance()" contra un protocolo comprobable
     en tiempo de ejecución puede ser sorprendentemente lenta en
     comparación con una verificación "isinstance()" contra una clase
     que no es de protocolo. Considere utilizar expresiones
     alternativas como llamadas "hasattr()" para comprobaciones
     estructurales en código sensible al rendimiento.

   Added in version 3.8.

   Distinto en la versión 3.12: La implementación interna de las
   comprobaciones de "isinstance()" con protocolos que se pueden
   comprobar en tiempo de ejecución ahora utiliza
   "inspect.getattr_static()" para buscar atributos (anteriormente, se
   utilizaba "hasattr()"). Como resultado, algunos objetos que solían
   considerarse instancias de un protocolo que se podía comprobar en
   tiempo de ejecución ya no se consideran instancias de ese protocolo
   en Python 3.12+, y viceversa. Es poco probable que la mayoría de
   los usuarios se vean afectados por este cambio.

   Distinto en la versión 3.12: The members of a runtime-checkable
   protocol are now considered "frozen" at runtime as soon as the
   class has been created. Monkey-patching attributes onto a runtime-
   checkable protocol will still work, but will have no impact on
   "isinstance()" checks comparing objects to the protocol. See What's
   new in Python 3.12 for more details.

class typing.TypedDict(dict)

   Special construct to add type hints to a dictionary. At runtime
   ""TypedDict" instances" are simply "dicts".

   "TypedDict" crea un tipo de diccionario que espera que todas sus
   instancias tenga un cierto conjunto de claves, donde cada clave
   está asociada con un valor de un tipo determinado. Esta exigencia
   no se comprueba en tiempo de ejecución y solo es aplicada por
   validadores de tipo. Uso:

      class Point2D(TypedDict):
          x: int
          y: int
          label: str

      a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
      b: Point2D = {'z': 3, 'label': 'bad'}           # Falla la verificación de tipos

      assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

   Una forma alternativa de crear un "TypedDict" es mediante la
   sintaxis de llamada de función. El segundo argumento debe ser un
   "dict" literal:

      Punto2D = TypedDict('Punto2D', {'x': int, 'y': int, 'etiqueta': str})

   This functional syntax allows defining keys which are not valid
   identifiers, for example because they are keywords or contain
   hyphens, or when key names must not be mangled like regular private
   names:

      # raises SyntaxError
      class Point2D(TypedDict):
          in: int  # 'in' is a keyword
          x-y: int  # name with hyphens

      class Definition(TypedDict):
          __schema: str  # mangled to `_Definition__schema`

      # OK, functional syntax
      Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
      Definition = TypedDict('Definition', {'__schema': str})  # not mangled

   De forma predeterminada, todas las llaves deben estar presentes en
   un "TypedDict". Es posible marcar llaves individuales como *no
   requeridas* utilizando "NotRequired":

      class Point2D(TypedDict):
          x: int
          y: int
          label: NotRequired[str]

      # Sintaxis alternativa
      Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})

   Esto significa que en un "TypedDict" que sea una instancia de
   "Point2D", será posible omitir la llave "label".

   Además, es posible marcar todas las llaves como no-requeridas por
   defecto, al especificar un valor de "False" en el argumento
   *total*:

      class Point2D(TypedDict, total=False):
          x: int
          y: int

      # Sintaxis alternativa
      Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)

   Esto significa que un "TypedDict" "Point2D" puede tener cualquiera
   de las llaves omitidas. Solo se espera que un validador de tipo
   admita un "False" literal o "True" como valor del argumento
   "total". "True" es el predeterminado y hace que todos los elementos
   definidos en el cuerpo de la clase sean obligatorios.

   Las llaves individuales de un "TypedDict" "total=False" pueden ser
   marcadas como requeridas utilizando "Required":

      class Point2D(TypedDict, total=False):
          x: Required[int]
          y: Required[int]
          label: str

      # Sintaxis alternativa
      Point2D = TypedDict('Point2D', {
          'x': Required[int],
          'y': Required[int],
          'label': str
      }, total=False)

   Es posible que un tipo "TypedDict" herede de uno o más tipos
   "TypedDict" usando la sintaxis de clase. Uso:

      class Point3D(Point2D):
          z: int

   "Point3D" tiene tres elementos: "x", "y" y "z". Lo que es
   equivalente a la siguiente definición:

      class Point3D(TypedDict):
          x: int
          y: int
          z: int

   Un "TypedDict" no puede heredar de una clase que no sea una
   subclase de "TypedDict", exceptuando "Generic". Por ejemplo:

      class X(TypedDict):
          x: int

      class Y(TypedDict):
          y: int

      class Z(object): pass  # Una clase  no-TypedDict

      class XY(X, Y): pass  # OK

      class XZ(X, Z): pass  # lanza TypeError

   Un "TypedDict" puede ser genérico:

      class Group[T](TypedDict):
          key: T
          group: list[T]

   Para crear un "TypedDict" genérico que sea compatible con Python
   3.11 o anterior, herede de "Generic" explícitamente:

      T = TypeVar("T")

      class Group(TypedDict, Generic[T]):
          key: T
          group: list[T]

   A "TypedDict" can be introspected via
   "annotationlib.get_annotations()" (see Prácticas recomendadas para
   las anotaciones for more information on annotations best practices)
   and the following attributes:

   __total__

      "Point2D.__total__" proporciona el valor del argumento "total".
      Ejemplo:

         >>> from typing import TypedDict
         >>> class Point2D(TypedDict): pass
         >>> Point2D.__total__
         True
         >>> class Point2D(TypedDict, total=False): pass
         >>> Point2D.__total__
         False
         >>> class Point3D(Point2D): pass
         >>> Point3D.__total__
         True

      Este atributo refleja el valor del argumento "total" de la clase
      "TypedDict" actual, no si la clase es semánticamente total. Por
      ejemplo, una "TypedDict" con "__total__" establecida en "True"
      puede tener claves marcadas con "NotRequired", o puede heredar
      de otra "TypedDict" con "total=False". Por lo tanto,
      generalmente es mejor usar "__required_keys__" y
      "__optional_keys__" para la introspección.

   __required_keys__

      Added in version 3.9.

   __optional_keys__

      "Point2D.__required_keys__" y "Point2D.__optional_keys__"
      retornan objetos de la clase "frozenset", que contienen las
      llaves requeridas y no requeridas, respectivamente.

      Las llaves marcadas con "Required" siempre aparecerán en
      "__required_keys__" y las llaves marcadas con "NotRequired"
      siempre aparecerán en "__optional_keys__".

      For backwards compatibility with Python 3.10 and below, it is
      also possible to use inheritance to declare both required and
      non-required keys in the same "TypedDict". This is done by
      declaring a "TypedDict" with one value for the "total" argument
      and then inheriting from it in another "TypedDict" with a
      different value for "total":

         >>> class Point2D(TypedDict, total=False):
         ...     x: int
         ...     y: int
         ...
         >>> class Point3D(Point2D):
         ...     z: int
         ...
         >>> Point3D.__required_keys__ == frozenset({'z'})
         True
         >>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
         True

      Added in version 3.9.

      Nota:

        Si se utiliza "from __future__ import annotations" o si las
        anotaciones se proporcionan como cadenas, las anotaciones no
        se evalúan cuando se define "TypedDict". Por lo tanto, la
        introspección en tiempo de ejecución de la que dependen
        "__required_keys__" y "__optional_keys__" puede no funcionar
        correctamente y los valores de los atributos pueden ser
        incorrectos.

   La compatibilidad con "ReadOnly" se refleja en los siguientes
   atributos:

   __readonly_keys__

      Un "frozenset" que contiene los nombres de todas las claves de
      solo lectura. Las claves son de solo lectura si llevan el
      calificador "ReadOnly".

      Added in version 3.13.

   __mutable_keys__

      Un "frozenset" que contiene los nombres de todas las claves
      mutables. Las claves son mutables si no llevan el calificador
      "ReadOnly".

      Added in version 3.13.

   See the TypedDict section in the typing documentation for more
   examples and detailed rules.

   Added in version 3.8.

   Distinto en la versión 3.9: "TypedDict" is now a function rather
   than a class. It can still be used as a class base, as described
   above.

   Distinto en la versión 3.11: Se agrega soporte para marcar llaves
   individuales como "Required" o "NotRequired". Véase **PEP 655**.

   Distinto en la versión 3.11: Se agrega soporte para "TypedDict"
   genéricos.

   Distinto en la versión 3.13: Se eliminó la compatibilidad con el
   método de argumento de palabra clave para crear "TypedDict"s.

   Distinto en la versión 3.13: Se agregó soporte para el calificador
   "ReadOnly".

   Deprecated since version 3.13, will be removed in version 3.15: Al
   utilizar la sintaxis funcional para crear una clase TypedDict, no
   se permite pasar un valor al parámetro 'campos' ("TD =
   TypedDict("TD")"). También se permite pasar "None" al parámetro
   'campos' ("TD = TypedDict("TD", None)"). Ambos métodos no estarán
   permitidos en Python 3.15. Para crear una clase TypedDict con 0
   campos, utilice "class TD(TypedDict): pass" o "TD = TypedDict("TD",
   {})".

### Protocolos

The following protocols are provided by the "typing" module. All are
decorated with "@runtime_checkable".

class typing.SupportsAbs

   A protocol with one abstract method "__abs__" that is covariant in
   its return type.

class typing.SupportsBytes

   A protocol with one abstract method "__bytes__".

class typing.SupportsComplex

   A protocol with one abstract method "__complex__".

class typing.SupportsFloat

   A protocol with one abstract method "__float__".

class typing.SupportsIndex

   A protocol with one abstract method "__index__".

   Added in version 3.8.

class typing.SupportsInt

   A protocol with one abstract method "__int__".

class typing.SupportsRound

   A protocol with one abstract method "__round__" that is covariant
   in its return type.

### ABCs and Protocols for working with I/O

class typing.IO[AnyStr]
class typing.TextIO
class typing.BinaryIO

   Generic class "IO[AnyStr]" and its subclasses "TextIO(IO[str])" and
   "BinaryIO(IO[bytes])" represent the types of I/O streams such as
   returned by "open()". Please note that these classes are not
   protocols, and their interface is fairly broad.

The protocols "io.Reader" and "io.Writer" offer a simpler alternative
for argument types, when only the "read()" or "write()" methods are
accessed, respectively:

   def read_and_write(reader: Reader[str], writer: Writer[bytes]):
       data = reader.read()
       writer.write(data.encode())

Also consider using "collections.abc.Iterable" for iterating over the
lines of an input stream:

   def read_config(stream: Iterable[str]):
       for line in stream:
           ...

### Funciones y decoradores

typing.cast(typ, val)

   Convertir un valor a un tipo.

   Esto retorna el valor sin modificar. Para el validador de tipos
   esto indica que el valor de retorno tiene el tipo señalado pero, de
   manera intencionada, no se comprobará en tiempo de ejecución (para
   maximizar la velocidad).

typing.assert_type(val, typ, /)

   Solicitar a un validador de tipos que confirme que *val* tiene
   *typ* por tipo inferido.

   En tiempo de ejecución esto no hace nada: devuelve el primer
   argumento sin cambios, sin verificaciones ni efectos secundarios,
   sin importar el tipo real del argumento.

   Cuando un validador de tipo estático encuentra una llamada a
   "assert_type()", emite un error si el valor no es del tipo
   especificado:

      def greet(name: str) -> None:
          assert_type(name, str)  # OK, tipo inferido de `name` es `str`
          assert_type(name, int)  # error del verificador de tipos

   Esta función es útil para asegurarse de que la comprensión que el
   validador de tipos tiene sobre un *script* está alineada con las
   intenciones de le desarrolladores:

      def complex_function(arg: object):
          # Haz alguna lógica compleja de reducción de tipo,
          # despues de la cual esperamos que el tipo inferido sea `int`
          ...
          # Probar si el verificador de tipos entiende correctamente nuestra función
          assert_type(arg, int)

   Added in version 3.11.

typing.assert_never(arg, /)

   Solicitar a un validador estático de tipos confirmar que una línea
   de código no es alcanzable.

   Por ejemplo:

      def int_or_str(arg: int | str) -> None:
          match arg:
              case int():
                  print("It's an int")
              case str():
                  print("It's a str")
              case _ as unreachable:
                  assert_never(unreachable)

   Aquí, las anotaciones permiten al validador de tipos inferir que el
   último caso nunca puede ejecutarse, porque "arg" es un "int" o un
   "str", y ambas opciones están cubiertas por los casos anteriores.

   Si un validador de tipos encuentra que una llamada a
   "assert_never()" es alcanzable, emitirá un error. Por ejemplo, si
   la anotación de tipo para "arg" fuese en cambio "int | str |
   float", el validador de tipos emitiría un error que indicaría que
   "unreachable" es de tipo "float". Para que una llamada a
   "assert_never" pase la verificación de tipos, el tipo inferido del
   argumento pasado debe ser el tipo inferior, "Never", y nada más.

   En tiempo de ejecución, ésto lanza una excepción cuando es llamado.

   Ver también:

     Unreachable Code and Exhaustiveness Checking has more information
     about exhaustiveness checking with static typing.

   Added in version 3.11.

typing.reveal_type(obj, /)

   Pídale a un verificador de tipos estáticos que revele el tipo
   inferido de una expresión.

   Cuando un verificador de tipos estáticos encuentra una llamada a
   esta función, emite un diagnóstico con el tipo inferido del
   argumento. Por ejemplo:

      x: int = 1
      reveal_type(x)  # Tipo revelado es "builtins.int"

   Ésto puede ser de utilidad cuando se desea *debuguear* cómo tu
   validador de tipos maneja una pieza particular de código.

   En tiempo de ejecución, esta función imprime el tipo de tiempo de
   ejecución de su argumento en "sys.stderr" y devuelve el argumento
   sin cambios (lo que permite que la llamada se use dentro de una
   expresión):

      x = reveal_type(1)  # imprime "Runtime type is int"
      print(x)  # prints "1"

   Tenga en cuenta que el tipo de tiempo de ejecución puede ser
   diferente (más o menos específico) del tipo inferido estáticamente
   por un verificador de tipos.

   La mayoría de los verificadores de tipos admiten "reveal_type()" en
   cualquier lugar, incluso si el nombre no se importa desde "typing".
   Sin embargo, importar el nombre desde "typing" permite que el
   código se ejecute sin errores de tiempo de ejecución y comunica la
   intención con mayor claridad.

   Added in version 3.11.

@typing.dataclass_transform(*, eq_default=True, order_default=False, kw_only_default=False, frozen_default=False, field_specifiers=(), **kwargs)

   Decorador para marcar un objeto como si proporcionara un
   comportamiento similar a "dataclass".

   "@dataclass_transform" may be used to decorate a class, metaclass,
   or a function that is itself a decorator. The presence of
   "@dataclass_transform()" tells a static type checker that the
   decorated object performs runtime "magic" that transforms a class
   in a similar way to "@dataclasses.dataclass".

   Ejemplo de uso con una función decoradora:

      @dataclass_transform()
      def create_model[T](cls: type[T]) -> type[T]:
          ...
          return cls

      @create_model
      class CustomerModel:
          id: int
          name: str

   En una clase base:

      @dataclass_transform()
      class ModelBase: ...

      class CustomerModel(ModelBase):
          id: int
          name: str

   En una metaclase:

      @dataclass_transform()
      class ModelMeta(type): ...

      class ModelBase(metaclass=ModelMeta): ...

      class CustomerModel(ModelBase):
          id: int
          name: str

   The "CustomerModel" classes defined above will be treated by type
   checkers similarly to classes created with
   "@dataclasses.dataclass". For example, type checkers will assume
   these classes have "__init__" methods that accept "id" and "name".

   The decorated class, metaclass, or function may accept the
   following bool arguments which type checkers will assume have the
   same effect as they would have on the "@dataclasses.dataclass"
   decorator: "init", "eq", "order", "unsafe_hash", "frozen",
   "match_args", "kw_only", and "slots". It must be possible for the
   value of these arguments ("True" or "False") to be statically
   evaluated.

   The arguments to the "@dataclass_transform" decorator can be used
   to customize the default behaviors of the decorated class,
   metaclass, or function:

   Parámetros:
      * **eq_default** (*bool*) -- Indica si se asume que el parámetro
        "eq" es "True" o "False" si el llamador lo omite. El valor
        predeterminado es "True".

      * **order_default** (*bool*) -- Indica si se asume que el
        parámetro "order" es "True" o "False" si el llamador lo omite.
        El valor predeterminado es "False".

      * **kw_only_default** (*bool*) -- Indica si se asume que el
        parámetro "kw_only" es "True" o "False" si el llamador lo
        omite. El valor predeterminado es "False".

      * **frozen_default** (*bool*) -- Indica si se asume que el
        parámetro "frozen" es "True" o "False" si el llamador lo
        omite. El valor predeterminado es "False". .. Agregado en la
        versión:: 3.12

      * **field_specifiers** (*tuple**[**Callable**[**...**,
        **Any**]**, **...**]*) -- Especifica una lista estática de
        clases o funciones admitidas que describen campos, parecido
        con "dataclasses.field()". El valor predeterminado es "()".

      * ****kwargs** (*Any*) -- Es posible pasar arbitrariamente otros
        argumentos nombrados para permitir posibles extensiones
        futuras.

   Los validadores de tipos reconocen los siguientes parámetros
   opcionales en los especificadores de campo:

   **Parámetros reconocidos para especificadores de campo**
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   +----------------------+----------------------------------------------------------------------------------+
   | Nombre del parámetro | Descripción                                                                      |
   |======================|==================================================================================|
   | "init"               | Indica si el campo debe incluirse en el método "__init__" sintetizado. Si no se  |
   |                      | especifica, el valor predeterminado de "init" es "True".                         |
   +----------------------+----------------------------------------------------------------------------------+
   | "default"            | Proporciona el valor predeterminado para el campo.                               |
   +----------------------+----------------------------------------------------------------------------------+
   | "default_factory"    | Proporciona una retrollamada en tiempo de ejecución que devuelve el valor        |
   |                      | predeterminado del campo. Si no se especifican "default" ni "default_factory",   |
   |                      | se supone que el campo no tiene un valor predeterminado y se le debe             |
   |                      | proporcionar un valor cuando se cree una instancia de la clase.                  |
   +----------------------+----------------------------------------------------------------------------------+
   | "factory"            | Un alias para el parámetro "default_factory" en los especificadores de campo.    |
   +----------------------+----------------------------------------------------------------------------------+
   | "kw_only"            | Indicates whether the field should be marked as keyword-only. If "True", the     |
   |                      | field will be keyword-only. If "False", it will not be keyword-only. If          |
   |                      | unspecified, the value of the "kw_only" parameter on the object decorated with   |
   |                      | "@dataclass_transform" will be used, or if that is unspecified, the value of     |
   |                      | "kw_only_default" on "@dataclass_transform" will be used.                        |
   +----------------------+----------------------------------------------------------------------------------+
   | "alias"              | Proporciona un nombre alternativo para el campo. Este nombre alternativo se      |
   |                      | utiliza en el método sintetizado "__init__".                                     |
   +----------------------+----------------------------------------------------------------------------------+

   En tiempo de ejecución, este decorador registra sus argumentos en
   el atributo "__dataclass_transform__" del objeto decorado. No tiene
   otro efecto en tiempo de ejecución.

   Véase **PEP 681** para más detalle.

   Added in version 3.11.

@typing.overload

   Decorador para crear funciones y métodos sobrecargados.

   El decorador "@overload" permite describir funciones y métodos que
   admiten múltiples combinaciones diferentes de tipos de argumentos.
   Una serie de definiciones decoradas con "@overload" debe ir seguida
   de exactamente una definición que no esté decorada con "@overload"
   (para la misma función o método).

   Las definiciones decoradas con "@overload" son solo para beneficio
   del validador de tipos, ya que serán sobrescritas por la definición
   no decorada con "@overload". Mientras tanto, la definición no
   decorada con "@overload" se usará en tiempo de ejecución, pero el
   validador de tipos debe ignorarla. En tiempo de ejecución, llamar a
   una función decorada con "@overload" directamente generará
   "NotImplementedError".

   Un ejemplo de sobrecarga que proporciona un tipo más preciso que el
   que se puede expresar mediante una unión o una variable de tipo:

      @overload
      def process(response: None) -> None:
          ...
      @overload
      def process(response: int) -> tuple[int, str]:
          ...
      @overload
      def process(response: bytes) -> str:
          ...
      def process(response):
          ...  # actual implementation goes here

   Véase **PEP 484** para más detalle y comparación con otras
   semánticas de tipado.

   Distinto en la versión 3.11: Ahora es posible introspectar en
   tiempo de ejecución las funciones sobrecargadas utilizando
   "get_overloads()".

typing.get_overloads(func)

   Return a sequence of "@overload"-decorated definitions for *func*.

   *func* is the function object for the implementation of the
   overloaded function. For example, given the definition of "process"
   in the documentation for "@overload", "get_overloads(process)" will
   return a sequence of three function objects for the three defined
   overloads. If called on a function with no overloads,
   "get_overloads()" returns an empty sequence.

   "get_overloads()" puede ser utilizada para introspectar en tiempo
   de ejecución una función sobrecargada.

   Added in version 3.11.

typing.clear_overloads()

   Borra todas las sobrecargas registradas en el registro interno.

   Esto se puede utilizar para recuperar la memoria utilizada por el
   registro.

   Added in version 3.11.

@typing.final

   Decorador para indicar métodos finales y clases finales.

   Decorar un método con "@final" indica a un validador de tipos que
   el método no se puede anular en una subclase. Decorar una clase con
   "@final" indica que no se puede subclasificar.

   Por ejemplo:

      class Base:
          @final
          def done(self) -> None:
              ...
      class Sub(Base):
          def done(self) -> None:  # Error informado por el verificador de tipos
              ...

      @final
      class Leaf:
          ...
      class Other(Leaf):  # Error informado por el verificador de tipos
          ...

   No hay comprobación en tiempo de ejecución para estas propiedades.
   Véase **PEP 591** para más detalles.

   Added in version 3.8.

   Distinto en la versión 3.11: El decorador intentará ahora
   establecer un atributo "__final__" como "True" en el objeto
   decorado. Por lo tanto, se puede utilizar una comprobación como "if
   getattr(obj, “__final__”, False)" en tiempo de ejecución para
   determinar si un objeto "obj" se ha marcado como final. Si el
   objeto decorado no admite la configuración de atributos, el
   decorador devuelve el objeto sin cambios sin lanzar una excepción.

@typing.no_type_check

   Un decorador para indicar que las anotaciones no deben ser
   comprobadas como indicadores de tipo.

   Esto funciona como un *decorator* (decorador) de clase o función.
   Con una clase, se aplica recursivamente a todos los métodos y
   clases definidos en esa clase (pero no a los métodos definidos en
   sus superclases o subclases). Los validadores de tipos ignorarán
   todas las anotaciones en una función o clase con este decorador.

   "@no_type_check" muta el objeto decorado en su lugar.

@typing.no_type_check_decorator

   Decorador para dar a otro decorador el efecto "no_type_check()".

   Esto hace que el decorador decorado añada el efecto de
   "no_type_check()" a la función decorada.

   Deprecated since version 3.13, will be removed in version 3.15:
   Ningún verificador de tipos agregó compatibilidad con
   "@no_type_check_decorator". Por lo tanto, está obsoleto y se
   eliminará en Python 3.15.

@typing.override

   Decorador para indicar que un método en una subclase está destinado
   a anular un método o atributo en una superclase.

   Los validadores de tipos deberían emitir un error si un método
   decorado con "@override" no anula nada. Esto ayuda a evitar errores
   que pueden ocurrir cuando se modifica una clase base sin un cambio
   equivalente en una clase secundaria.

   Por ejemplo:

      class Base:
          def log_status(self) -> None:
              ...

      class Sub(Base):
          @override
          def log_status(self) -> None:  # Okay: sobreescribe Base.log_status
              ...

          @override
          def done(self) -> None:  # Error reportado por el verificador de tipos
              ...

   No hay ninguna comprobación en tiempo de ejecución de esta
   propiedad.

   El decorador intentará establecer un atributo "__override__" en
   "True" en el objeto decorado. Por lo tanto, una comprobación como
   "if getattr(obj, “__override__”, False)" se puede utilizar en
   tiempo de ejecución para determinar si un objeto "obj" ha sido
   marcado como anulado. Si el objeto decorado no admite la
   configuración de atributos, el decorador devuelve el objeto sin
   cambios sin generar una excepción.

   Vea **PEP 681** para más información.

   Added in version 3.12.

@typing.type_check_only

   Decorador para marcar una clase o función como no disponible en
   tiempo de ejecución.

   Este decorador no está disponible en tiempo de ejecución. Existe
   principalmente para marcar clases que se definen en archivos *stub*
   para cuando una implementación retorna una instancia de una clase
   privada:

      @type_check_only
      class Response:  # privado o no disponible en tiempo de ejecución
          code: int
          def get_header(self, name: str) -> str: ...

      def fetch_response() -> Response: ...

   Nótese que no se recomienda retornar instancias de clases privadas.
   Normalmente es preferible convertirlas en clases públicas.

### Ayudas de introspección

typing.get_type_hints(obj, globalns=None, localns=None, include_extras=False, *, format=Format.VALUE)

   Return a dictionary containing type hints for a function, method,
   module, class object, or other callable object.

   This is often the same as "annotationlib.get_annotations()", but
   this function makes the following changes to the annotations
   dictionary:

   * Las referencias futuras codificadas como literales de cadena u
     objetos "ForwardRef" se manejan evaluándolas en el espacio de
     nombres *globalns*, *localns* y (cuando corresponda) el espacio
     de nombre type parameter *obj*. Si no se proporciona *globalns* o
     *localns*, los diccionarios de espacios de nombres apropiados se
     infieren de *obj*.

   * "None" se reemplaza por "types.NoneType".

   * If "@no_type_check" has been applied to *obj*, an empty
     dictionary is returned.

   * If *obj* is a class "C", the function returns a dictionary that
     merges annotations from "C"'s base classes with those on "C"
     directly. This is done by traversing "C.__mro__" and iteratively
     combining *annotations* of each base class. Annotations on
     classes appearing earlier in the *method resolution order* always
     take precedence over annotations on classes appearing later in
     the method resolution order.

   * The function recursively replaces all occurrences of
     "Annotated[T, ...]", "Required[T]", "NotRequired[T]", and
     "ReadOnly[T]" with "T", unless *include_extras* is set to "True"
     (see "Annotated" for more information).

   Prudencia:

     This function may execute arbitrary code contained in
     annotations. See Security implications of introspecting
     annotations for more information.

   Nota:

     If "Format.VALUE" is used and any forward references in the
     annotations of *obj* are not resolvable, a "NameError" exception
     is raised. For example, this can happen with names imported under
     "if TYPE_CHECKING". More generally, any kind of exception can be
     raised if an annotation contains invalid Python code.

   Nota:

     Calling "get_type_hints()" on an instance is not supported. To
     retrieve annotations for an instance, call "get_type_hints()" on
     the instance's class instead (for example,
     "get_type_hints(type(obj))").

   Distinto en la versión 3.9: Se agregó el parámetro "include_extras"
   como parte de **PEP 593**. Consulte la documentación en "Annotated"
   para obtener más información.

   Distinto en la versión 3.11: Anteriormente, se agregaba
   "Optional[t]" en las anotaciones de funciones o métodos si se
   establecía un valor por defecto igual a "None". Ahora la anotación
   es retornada sin cambios.

   Distinto en la versión 3.14: Added the "format" parameter. See the
   documentation on "annotationlib.get_annotations()" for more
   information.

   Distinto en la versión 3.14: Calling "get_type_hints()" on
   instances is no longer supported. Some instances were accepted in
   earlier versions as an undocumented implementation detail.

typing.get_origin(tp)

   Obtiene la versión sin suscripción de un tipo: para un objeto de
   tipado de la forma "X[Y, Z, ...]" devuelve "X".

   Si "X" es un alias de módulo de tipado para una clase incorporada o
   "collections", se normalizará a la clase original. Si "X" es una
   instancia de "ParamSpecArgs" o "ParamSpecKwargs", devuelve la
   "ParamSpec" subyacente. Devuelve "None" para objetos no soportados.

   Por ejemplo:

      assert get_origin(str) is None
      assert get_origin(Dict[str, int]) is dict
      assert get_origin(Union[int, str]) is Union
      assert get_origin(Annotated[str, "metadata"]) is Annotated
      P = ParamSpec('P')
      assert get_origin(P.args) is P
      assert get_origin(P.kwargs) is P

   Added in version 3.8.

typing.get_args(tp)

   Obtiene los argumentos de tipo con todas las sustituciones
   realizadas: para un objeto de tipo con la forma "X[Y, Z, ...]"
   devuelve "(Y, Z, ...)".

   Si "X" es una unión o "Literal" contenida en otro tipo genérico, el
   orden de "(Y, Z, ...)" puede ser diferente del orden de los
   argumentos originales "[Y, Z, ...]" debido al almacenamiento en
   caché de tipos. Devuelve "()" para objetos no soportados.

   Por ejemplo:

      assert get_args(int) == ()
      assert get_args(Dict[int, str]) == (int, str)
      assert get_args(Union[int, str]) == (int, str)

   Added in version 3.8.

typing.get_protocol_members(tp)

   Devuelve el conjunto de miembros definidos en un "Protocol".

      >>> from typing import Protocol, get_protocol_members
      >>> class P(Protocol):
      ...     def a(self) -> str: ...
      ...     b: int
      >>> get_protocol_members(P) == frozenset({'a', 'b'})
      True

   Genera "TypeError" para argumentos que no sean protocolos.

   Added in version 3.13.

typing.is_protocol(tp)

   Compruebe si un tipo es "TypedDict".

   Por ejemplo:

      class P(Protocol):
          def a(self) -> str: ...
          b: int

      assert is_protocol(P)
      assert not is_protocol(int)

   This function only returns true for "Protocol" classes, not for
   generic aliases of them:

      class GenericP[T](Protocol):
          def a(self) -> T: ...
          b: int

      assert not is_protocol(GenericP[int])

   Added in version 3.13.

typing.is_typeddict(tp)

   Compruebe si un tipo es "TypedDict".

   Por ejemplo:

      class Film(TypedDict):
          title: str
          year: int

      assert is_typeddict(Film)
      assert not is_typeddict(list | str)

      # TypedDict es una fábrica para crear diccionarios tipados,
      # no un diccionario tipado en si mismo
      assert not is_typeddict(TypedDict)

   This function only returns true for "TypedDict" classes, not for
   generic aliases of them:

      class GenericFilm[T](TypedDict):
          title: str
          year: T

      assert not is_typeddict(GenericFilm[int])

   Added in version 3.10.

class typing.ForwardRef

   Clase utilizada para la representación interna de tipado de cadenas
   de caracteres en referencias futuras.

   For example, "List["SomeClass"]" is implicitly transformed into
   "List[ForwardRef("SomeClass")]".  "ForwardRef" should not be
   instantiated by a user, but may be used by introspection tools.

   Nota:

     Los tipos genéricos de **PEP 585**, como "list["SomeClass"]", no
     se transformarán implícitamente en
     "list[ForwardRef("SomeClass")]" y, por lo tanto, no se resolverán
     automáticamente en "list[SomeClass]".

   Added in version 3.7.4.

   Distinto en la versión 3.14: This is now an alias for
   "annotationlib.ForwardRef". Several undocumented behaviors of this
   class have been changed; for example, after a "ForwardRef" has been
   evaluated, the evaluated value is no longer cached.

typing.evaluate_forward_ref(forward_ref, *, owner=None, globals=None, locals=None, type_params=None, format=annotationlib.Format.VALUE)

   Evaluate an "annotationlib.ForwardRef" as a *type hint*.

   This is similar to calling "annotationlib.ForwardRef.evaluate()",
   but unlike that method, "evaluate_forward_ref()" also recursively
   evaluates forward references nested within the type hint.

   See the documentation for "annotationlib.ForwardRef.evaluate()" for
   the meaning of the *owner*, *globals*, *locals*, *type_params*, and
   *format* parameters.

   Prudencia:

     This function may execute arbitrary code contained in
     annotations. See Security implications of introspecting
     annotations for more information.

   Added in version 3.14.

typing.NoDefault

   Un objeto centinela que se utiliza para indicar que un parámetro de
   tipo no tiene un valor predeterminado. Por ejemplo:

      >>> T = TypeVar("T")
      >>> T.__default__ is typing.NoDefault
      True
      >>> S = TypeVar("S", default=None)
      >>> S.__default__ is None
      True

   Added in version 3.13.

### Constantes

typing.TYPE_CHECKING

   A special constant that is assumed to be "True" by static type
   checkers. It's "False" at runtime.

   A module which is expensive to import, and which only contain types
   used for typing annotations, can be safely imported inside an "if
   TYPE_CHECKING:" block.  This prevents the module from actually
   being imported at runtime; annotations aren't eagerly evaluated
   (see **PEP 649**) so using undefined symbols in annotations is
   harmless--as long as you don't later examine them. Your static type
   analysis tool will set "TYPE_CHECKING" to "True" during static type
   analysis, which means the module will be imported and the types
   will be checked properly during such analysis.

   Uso:

      if TYPE_CHECKING:
          import expensive_mod

      def fun(arg: expensive_mod.SomeType) -> None:
          local_var: expensive_mod.AnotherType = other_fun()

   If you occasionally need to examine type annotations at runtime
   which may contain undefined symbols, use
   "annotationlib.get_annotations()" with a "format" parameter of
   "annotationlib.Format.STRING" or "annotationlib.Format.FORWARDREF"
   to safely retrieve the annotations without raising "NameError".

   Added in version 3.5.2.

### Alias obsoletos

This module defines several deprecated aliases to pre-existing
standard library classes. These were originally included in the
"typing" module in order to support parameterizing these generic
classes using "[]". However, the aliases became redundant in Python
3.9 when the corresponding pre-existing classes were enhanced to
support "[]" (see **PEP 585**).

Los tipos redundantes están obsoletos a partir de Python 3.9. Sin
embargo, si bien los alias pueden eliminarse en algún momento,
actualmente no se planea eliminarlos. Por lo tanto, el intérprete no
emite advertencias de obsolescencia para estos alias.

If at some point it is decided to remove these deprecated aliases, a
deprecation warning will be issued by the interpreter for at least two
releases prior to removal. The aliases are guaranteed to remain in the
"typing" module without deprecation warnings until at least Python
3.14.

Se recomienda a los validadores de tipos que marquen los usos de los
tipos obsoletos si el programa que están verificando apunta a una
versión mínima de Python 3.9 o más reciente.

#### Alias de tipos integrados

class typing.Dict(dict, MutableMapping[KT, VT])

   Alias obsoleto de "dict".

   Tenga en cuenta que para anotar argumentos, se prefiere utilizar un
   tipo de colección abstracto como "Mapping" en lugar de utilizar
   "dict" o "typing.Dict".

   Obsoleto desde la versión 3.9: "builtins.dict" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.List(list, MutableSequence[T])

   Alias obsoleto de "list".

   Tenga en cuenta que para anotar argumentos, se prefiere utilizar un
   tipo de colección abstracto como "Sequence" o "Iterable" en lugar
   de utilizar "list" o "typing.List".

   Obsoleto desde la versión 3.9: "builtins.list" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Set(set, MutableSet[T])

   Alias obsoleto de "builtins.set".

   Tenga en cuenta que para anotar argumentos, se prefiere utilizar un
   tipo de colección abstracto como "collections.abc.Set" en lugar de
   utilizar "set" o "typing.Set".

   Obsoleto desde la versión 3.9: "builtins.set" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.FrozenSet(frozenset, AbstractSet[T_co])

   Alias obsoleto de "builtins.frozenset".

   Obsoleto desde la versión 3.9: "builtins.frozenset" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

typing.Tuple

   Alias obsoleto de "tuple".

   "tuple" y "Tuple" son casos especiales en el sistema de tipos;
   consulte Anotaciones en tuplas para más detalles.

   Obsoleto desde la versión 3.9: "builtins.tuple" ahora soporta el
   uso de subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Type(Generic[CT_co])

   Alias obsoleto de "type".

   Vea El tipo de objetos de clase para obtener detalles sobre el uso
   de "type" o "typing.Type" en anotaciones de tipo.

   Added in version 3.5.2.

   Obsoleto desde la versión 3.9: "builtins.type" ahora soporta el uso
   de subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

#### Alias de tipos en "collections"

class typing.DefaultDict(collections.defaultdict, MutableMapping[KT, VT])

   Alias obsoleto de "collections.defaultdict".

   Added in version 3.5.2.

   Obsoleto desde la versión 3.9: "collections.defaultdict" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.OrderedDict(collections.OrderedDict, MutableMapping[KT, VT])

   Alias obsoleto de "collections.OrderedDict".

   Added in version 3.7.2.

   Obsoleto desde la versión 3.9: "collections.OrderedDict" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.ChainMap(collections.ChainMap, MutableMapping[KT, VT])

   Alias obsoleto de "collections.ChainMap".

   Added in version 3.6.1.

   Obsoleto desde la versión 3.9: "collections.ChainMap" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Counter(collections.Counter, Dict[T, int])

   Alias obsoleto de "collections.Counter".

   Added in version 3.6.1.

   Obsoleto desde la versión 3.9: "collections.Counter" ahora soporta
   subíndices ("[]")`. Véase **PEP 585** y Tipo Alias Genérico.

class typing.Deque(deque, MutableSequence[T])

   Alias obsoleto de "collections.deque".

   Added in version 3.6.1.

   Obsoleto desde la versión 3.9: "collections.deque" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

#### Alias ​​a otros tipos concretos

class typing.Pattern
class typing.Match

   Alias ​​obsoletos correspondientes a los tipos de retorno
   "re.compile()" y "re.match()".

   Estos tipos (y las funciones correspondientes) son genéricos sobre
   "AnyStr". "Pattern" se puede especializar como "Pattern[str]" o
   "Pattern[bytes]"; "Match" se puede especializar como "Match[str]" o
   "Match[bytes]".

   Obsoleto desde la versión 3.9: Las clases "Pattern" y "Match" de
   "re" ahora soportan "[]". Véase **PEP 585** y Tipo Alias Genérico.

class typing.Text

   Alias obsoleto para "str".

   Se indica "Text" para proporcionar compatibilidad con versiones de
   código posteriores a Python 2: en Python 2, "Text" es un alias para
   "unicode".

   Úsese "Text" para indicar que un valor debe contener una cadena de
   texto Unicode de manera que sea compatible con Python 2 y Python 3:

      def add_unicode_checkmark(text: Text) -> Text:
          return text + u' \u2713'

   Added in version 3.5.2.

   Obsoleto desde la versión 3.11: Python 2 ya no es compatible, y la
   mayoría de los validadores de tipos tampoco admiten la verificación
   de tipos de código Python 2. La eliminación del alias no está
   planeada actualmente, pero se recomienda a los usuarios utilizar
   "str" en lugar de "Text".

#### Alias de ABCs de contenedores en "collections.abc"

class typing.AbstractSet(Collection[T_co])

   Alias obsoleto de "collections.abc.Set".

   Obsoleto desde la versión 3.9: "collections.abc.Set" ahora soporta
   subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.ByteString(Sequence[int])

   Deprecated alias to "collections.abc.ByteString".

   Use "isinstance(obj, collections.abc.Buffer)" to test if "obj"
   implements the buffer protocol at runtime. For use in type
   annotations, either use "Buffer" or a union that explicitly
   specifies the types your code supports (e.g., "bytes | bytearray |
   memoryview").

   "ByteString" was originally intended to be an abstract class that
   would serve as a supertype of both "bytes" and "bytearray".
   However, since the ABC never had any methods, knowing that an
   object was an instance of "ByteString" never actually told you
   anything useful about the object. Other common buffer types such as
   "memoryview" were also never understood as subtypes of "ByteString"
   (either at runtime or by static type checkers).

   See **PEP 688** for more details.

   Deprecated since version 3.9, will be removed in version 3.17.

class typing.Collection(Sized, Iterable[T_co], Container[T_co])

   Alias obsoleto de "collections.abc.Collection".

   Added in version 3.6.

   Obsoleto desde la versión 3.9: "collections.abc.Collection" ahora
   soporta la sintaxis de subíndice ("[]"). Véase **PEP 585** y Tipo
   Alias Genérico.

class typing.Container(Generic[T_co])

   Alias obsoleto de "collections.abc.Container".

   Obsoleto desde la versión 3.9: "collections.abc.Container" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.ItemsView(MappingView, AbstractSet[tuple[KT_co, VT_co]])

   Alias obsoleto de "collections.abc.ItemsView".

   Obsoleto desde la versión 3.9: "collections.abc.ItemsView" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.KeysView(MappingView, AbstractSet[KT_co])

   Alias obsoleto de "collections.abc.KeysView".

   Obsoleto desde la versión 3.9: "collections.abc.KeysView" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Mapping(Collection[KT], Generic[KT, VT_co])

   Alias obsoleto de "collections.abc.Mapping".

   Obsoleto desde la versión 3.9: "collections.abc.Mapping" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.MappingView(Sized)

   Alias obsoleto de "collections.abc.MappingView".

   Obsoleto desde la versión 3.9: "collections.abc.MappingView" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.MutableMapping(Mapping[KT, VT])

   Alias obsoleto de "collections.abc.MutableMapping".

   Obsoleto desde la versión 3.9: "collections.abc.MutableMapping"
   ahora soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias
   Genérico.

class typing.MutableSequence(Sequence[T])

   Alias obsoleto de "collections.abc.MutableSequence".

   Obsoleto desde la versión 3.9: "collections.abc.MutableSequence"
   ahora soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias
   Genérico.

class typing.MutableSet(AbstractSet[T])

   Alias obsoleto de "collections.abc.MutableSet".

   Obsoleto desde la versión 3.9: "collections.abc.MutableSet" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Sequence(Reversible[T_co], Collection[T_co])

   Alias obsoleto de "collections.abc.Sequence".

   Obsoleto desde la versión 3.9: "collections.abc.Sequence" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.ValuesView(MappingView, Collection[_VT_co])

   Alias obsoleto de "collections.abc.ValuesView".

   Obsoleto desde la versión 3.9: "collections.abc.ValuesView" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

#### Alias para ABCs asíncronos en "collections.abc"

class typing.Coroutine(Awaitable[ReturnType], Generic[YieldType, SendType, ReturnType])

   Alias obsoleto de "collections.abc.Coroutine".

   Consulte Anotación de generadores y corrutinas para obtener
   detalles sobre el uso de "collections.abc.Coroutine" y
   "typing.Coroutine" en anotaciones de tipo.

   Added in version 3.5.3.

   Obsoleto desde la versión 3.9: "collections.abc.Coroutine" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.AsyncGenerator(AsyncIterator[YieldType], Generic[YieldType, SendType])

   Alias obsoleto de "collections.abc.AsyncGenerator".

   Consulte Anotación de generadores y corrutinas para obtener
   detalles sobre el uso de "collections.abc.AsyncGenerator" y
   "typing.AsyncGenerator" en anotaciones de tipo.

   Added in version 3.6.1.

   Obsoleto desde la versión 3.9: "collections.abc.AsycGenerator"
   ahora soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias
   Genérico.

   Distinto en la versión 3.13: El parámetro "SendType" ahora tiene un
   valor predeterminado.

class typing.AsyncIterable(Generic[T_co])

   Alias obsoleto de "collections.abc.AsyncIterable".

   Added in version 3.5.2.

   Obsoleto desde la versión 3.9: "collections.abc.AsyncIterable"
   ahora soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias
   Genérico.

class typing.AsyncIterator(AsyncIterable[T_co])

   Alias obsoleto de "collections.abc.AsyncIterator".

   Added in version 3.5.2.

   Obsoleto desde la versión 3.9: "collections.abc.AsyncIterator"
   ahora soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias
   Genérico.

class typing.Awaitable(Generic[T_co])

   Alias obsoleto de "collections.abc.Awaitable".

   Added in version 3.5.2.

   Obsoleto desde la versión 3.9: "collections.abc.Awaitable" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

#### Alias a otros ABCs en "collections.abc"

class typing.Iterable(Generic[T_co])

   Alias obsoleto de "collections.abc.Iterable".

   Obsoleto desde la versión 3.9: "collections.abc.Iterable" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Iterator(Iterable[T_co])

   Alias obsoleto de "collections.abc.Iterator".

   Obsoleto desde la versión 3.9: "collections.abc.Iterator" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

typing.Callable

   Alias obsoleto de "collections.abc.Callable".

   Vea Anotaciones en objetos invocables para información detallada de
   cómo usar "collections.abc.Callable" y "typing.Callable" en
   anotaciones de tipo.

   Obsoleto desde la versión 3.9: "collections.abc.Callable" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

   Distinto en la versión 3.10: "Callable" ahora es compatible con
   "ParamSpec" y "Concatenate". Consulte **PEP 612** para obtener más
   información.

class typing.Generator(Iterator[YieldType], Generic[YieldType, SendType, ReturnType])

   Alias obsoleto de "collections.abc.Generator".

   Consulte Anotación de generadores y corrutinas para obtener
   detalles sobre el uso de "collections.abc.Generator" y
   "typing.Generator" en anotaciones de tipo.

   Obsoleto desde la versión 3.9: "collections.abc.Generator" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

   Distinto en la versión 3.13: Valores por defecto para los tipos
   send y return fueron agregados.

class typing.Hashable

   Alias obsoleto de "collections.abc.Hashable".

   Obsoleto desde la versión 3.12: Use directamente
   "collections.abc.Hashable" en su lugar.

class typing.Reversible(Iterable[T_co])

   Alias obsoleto de "collections.abc.Reversible".

   Obsoleto desde la versión 3.9: "collections.abc.Reversible" ahora
   soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

class typing.Sized

   Alias obsoleto de "collections.abc.Sized".

   Obsoleto desde la versión 3.12: Use directamente
   "collections.abc.Sized" en su lugar.

#### Alias de ABCs "contextlib"

class typing.ContextManager(Generic[T_co, ExitT_co])

   Alias obsoleto de "contextlib.AbstractContextManager".

   El primer parámetro de tipo, "T_co", representa el tipo devuelto
   por el método "__enter__()". El segundo parámetro de tipo opcional,
   "ExitT_co", cuyo valor predeterminado es "bool | None", representa
   el tipo devuelto por el método "__exit__()".

   Added in version 3.5.4.

   Obsoleto desde la versión 3.9: "contextlib.AbstractContextManager"
   ahora soporta subíndices ("[]"). Véase **PEP 585** y Tipo Alias
   Genérico.

   Distinto en la versión 3.13: Se agregó el segundo parámetro de tipo
   opcional, "ExitT_co".

class typing.AsyncContextManager(Generic[T_co, AExitT_co])

   Alias obsoleto de "contextlib.AbstractAsyncContextManager".

   El primer parámetro de tipo, "T_co", representa el tipo devuelto
   por el método "__aenter__()". El segundo parámetro de tipo
   opcional, "AExitT_co", cuyo valor predeterminado es "bool | None",
   representa el tipo devuelto por el método "__aexit__()".

   Added in version 3.6.2.

   Obsoleto desde la versión 3.9:
   "contextlib.AbstractAsyncContextManager" ahora soporta subíndices
   ("[]"). Véase **PEP 585** y Tipo Alias Genérico.

   Distinto en la versión 3.13: Se agregó el segundo parámetro de tipo
   opcional, "AExitT_co".

## Línea de tiempo de obsolescencia de características principales

Algunas características de "typing" están obsoletas y podrán ser
removidas en versiones futuras de Python. Lo que sigue es una tabla
que resume las principales obsolescencias para su conveniencia. Ésto
está sujeto a cambio y no todas las obsolescencias están
representadas.

+---------------------------+---------------------------+---------------------------+---------------------------+
| Característica            | En desuso desde           | Eliminación proyectada    | PEP/issue                 |
|===========================|===========================|===========================|===========================|
| Versiones "typing" de     | 3.9                       | No decidido (ver Alias    | **PEP 585**               |
| colecciones estándares    |                           | obsoletos para más        |                           |
## |                           |                           | información)              |                           |

## | "typing.ByteString"       | 3.9                       | 3.17                      | gh-91896                  |

## | "typing.Text"             | 3.11                      | No decidido               | gh-92332                  |

| "typing.Hashable" y       | 3.12                      | No decidido               | gh-94309                  |
## | "typing.Sized"            |                           |                           |                           |

## | "typing.TypeAlias"        | 3.12                      | No decidido               | **PEP 695**               |

| "@typing.no_type_check_d  | 3.13                      | 3.15                      | gh-106309                 |
## | ecorator"                 |                           |                           |                           |

## | "typing.AnyStr"           | 3.13                      | 3.18                      | gh-105578                 |
