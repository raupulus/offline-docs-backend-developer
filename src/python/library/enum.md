---
title: '"enum" --- Support for enumerations'
source_url: https://docs.python.org/es/3
source_path: library/enum.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2550
---

# "enum" --- Support for enumerations

Added in version 3.4.

**Código fuente:** Lib/enum.py

##### Important

Esta página contiene la información de referencia de la API. Para
obtener información sobre tutoriales y debates sobre temas más
avanzados, consulte

* Tutorial básico

* Tutorial avanzado

* Libro de recetas Enum

======================================================================

Una enumeración:

* es un conjunto de nombres simbólicos (miembros) vinculados a valores
  únicos

* can be iterated over to return its canonical (i.e. non-alias)
  members in definition order

* usa la sintaxis *call* para retornar miembros por valor

* usa la sintaxis *index* para retornar miembros por nombre

Las enumeraciones se crean mediante la sintaxis "class" o mediante la
sintaxis de llamadas a funciones:

   >>> from enum import Enum

   >>> # class syntax
   >>> class Color(Enum):
   ...     RED = 1
   ...     GREEN = 2
   ...     BLUE = 3

   >>> # functional syntax
   >>> Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

Aunque podemos usar la sintaxis "class" para crear enumeraciones, las
enumeraciones no son clases normales de Python. Ver ¿En qué se
diferencian las enumeraciones? para más detalles.

Nota:

  Nomenclatura

  * The class "Color" is an *enumeration* (or *enum*)

  * The attributes "Color.RED", "Color.GREEN", etc., are *enumeration
    members* (or *members*) and are functionally constants.

  * The enum members have *names* and *values* (the name of
    "Color.RED" is "RED", the value of "Color.BLUE" is "3", etc.)

======================================================================

## Module contents

   "EnumType"

      El "type" para Enum y sus subclases.

   "Enum"

      Clase base para crear constantes enumeradas.

   "IntEnum"

      Clase base para crear constantes enumeradas que también son
      subclases de "int". (Notes)

   "StrEnum"

      Clase base para crear constantes enumeradas que también son
      subclases de "str". (Notes)

   "Flag"

      Clase base para crear constantes enumeradas que se pueden
      combinar utilizando las operaciones *bitwise* sin perder su
      membresía "Flag".

   "IntFlag"

      Clase base para crear constantes enumeradas que se pueden
      combinar mediante los operadores bit a bit sin perder su
      pertenencia a "IntFlag". Los miembros "IntFlag" también son
      subclases de "int". (Notes)

   "ReprEnum"

      Usado por "IntEnum", "StrEnum" y "IntFlag" para mantener el
      "str()" del tipo mixto.

   "EnumCheck"

      Una enumeración con los valores "CONTINUOUS", "NAMED_FLAGS" y
      "UNIQUE", para usar con "verify()" para garantizar que una
      enumeración determinada cumpla varias restricciones.

   "FlagBoundary"

      Una enumeración con los valores "STRICT", "CONFORM", "EJECT" y
      "KEEP" que permite un control más detallado sobre cómo se tratan
      los valores no válidos en una enumeración.

   "EnumDict"

      A subclass of "dict" for use when subclassing "EnumType".

   "auto"

      Las instancias se reemplazan con un valor apropiado para los
      miembros de Enum. "StrEnum" usa de manera predeterminada la
      versión en minúsculas del nombre del miembro, mientras que otras
      enumeraciones tienen el valor predeterminado de 1 y aumentan a
      partir de ahí.

   "@~enum.property"

      Allows "Enum" members to have attributes without conflicting
      with member names.  The "value" and "name" attributes are
      implemented this way.

   "@unique"

      El decorador de clase Enum que garantiza que solo un nombre esté
      vinculado a cualquier valor.

   "@verify"

      Decorador de clase Enum que verifica las restricciones
      seleccionables por el usuario en una enumeración.

   "@member"

      Convierta a "obj" en miembro. Se puede utilizar como decorador.

   "@nonmember"

      No convierta a "obj" en miembro. Se puede utilizar como
      decorador.

   "@global_enum"

      Modify the "str()" and "repr()" of an enum to show its members
      as belonging to the module instead of its class, and export the
      enum members to the global namespace.

   "show_flag_values()"

      Retorna una lista de todos los enteros de potencia de dos
      contenidos en una bandera.

   "enum.bin()"

      Like built-in "bin()", except negative values are represented in
      two's complement, and the leading bit always indicates sign ("0"
      implies positive, "1" implies negative).

Added in version 3.6: "Flag", "IntFlag", "auto"

Added in version 3.11: "StrEnum", "EnumCheck", "ReprEnum",
"FlagBoundary", "property", "member", "nonmember", "global_enum",
"show_flag_values"

Added in version 3.13: "EnumDict"

======================================================================

## Data types

class enum.EnumType

   *EnumType* es el *metaclass* para enumeraciones *enum*. Es posible
   subclasificar *EnumType*; consulte Subclassing EnumType para
   obtener más detalles.

   "EnumType" is responsible for setting the correct "__repr__()",
   "__str__()", "__format__()", and "__reduce__()" methods on the
   final *enum*, as well as creating the enum members, properly
   handling duplicates, providing iteration over the enum class, etc.

   Added in version 3.11: Before 3.11 "EnumType" was called
   "EnumMeta", which is still available as an alias.

   __call__(cls, value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

      Este método se llama de dos maneras diferentes:

      * para buscar un miembro existente:

           cls:
              La clase de enumeración que se llama.

           value:
              El valor a buscar.

      * to use the "cls" enum to create a new enum (only if the
        existing enum does not have any members):

           cls:
              La clase de enumeración que se llama.

           value:
              El nombre del nuevo Enum para crear.

           names:
              Los nombres/valores de los miembros para el nuevo Enum.

           module:
              El nombre del módulo en el que se crea el nuevo Enum.

           qualname:
              La ubicación real en el módulo donde se puede encontrar
              este Enum.

           type:
              Un tipo de mezcla para el nuevo Enum.

           start:
              The first integer value for the Enum (used by "auto").

           boundary:
              How to handle out-of-range values from bit operations
              ("Flag" only).

   __contains__(cls, member)

      Retorna "True" si el miembro pertenece a "cls":

         >>> some_var = Color.RED
         >>> some_var in Color
         True
         >>> Color.RED.value in Color
         True

      Distinto en la versión 3.12: Before Python 3.12, a "TypeError"
      is raised if a non-Enum-member is used in a containment check.

   __dir__(cls)

      Retorna "['__class__', '__doc__', '__members__', '__module__']"
      y los nombres de los miembros en *cls*:

         >>> dir(Color)
         ['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__']

   __getitem__(cls, name)

      Returns the Enum member in *cls* matching *name*, or raises a
      "KeyError":

         >>> Color['BLUE']
         <Color.BLUE: 3>

   __iter__(cls)

      Retorna cada miembro en *cls* en orden de definición:

         >>> list(Color)
         [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

   __len__(cls)

      Returns the number of members in *cls*:

         >>> len(Color)
         3

   __members__

      Returns a mapping of every enum name to its member, including
      aliases

   __reversed__(cls)

      Retorna cada miembro en *cls* en orden de definición inverso:

         >>> list(reversed(Color))
         [<Color.BLUE: 3>, <Color.GREEN: 2>, <Color.RED: 1>]

class enum.Enum

   *Enum* es la clase base para todas las enumeraciones *enum*.

   name

      El nombre utilizado para definir el miembro "Enum":

         >>> Color.BLUE.name
         'BLUE'

   value

      El valor dado al miembro "Enum":

         >>> Color.RED.value
         1

      Value of the member, can be set in "__new__()".

      Nota:

        Valores de miembros de EnumMember values can be anything:
        "int", "str", etc.  If the exact value is unimportant you may
        use "auto" instances and an appropriate value will be chosen
        for you.  See "auto" for the details.While mutable/unhashable
        values, such as "dict", "list" or a mutable "dataclass", can
        be used, they will have a quadratic performance impact during
        creation relative to the total number of mutable/unhashable
        values in the enum.

   _name_

      Name of the member.

   _value_

      Value of the member, can be set in "__new__()".

   _order_

      No longer used, kept for backward compatibility. (class
      attribute, removed during class creation).

      The "_order_" attribute can be provided to help keep Python 2 /
      Python 3 code in sync. It will be checked against the actual
      order of the enumeration and raise an error if the two do not
      match:

         >>> class Color(Enum):
         ...     _order_ = 'RED GREEN BLUE'
         ...     RED = 1
         ...     BLUE = 3
         ...     GREEN = 2
         ...
         Traceback (most recent call last):
         ...
         TypeError: member order does not match _order_:
            ['RED', 'BLUE', 'GREEN']
            ['RED', 'GREEN', 'BLUE']

      Nota:

        In Python 2 code the "_order_" attribute is necessary as
        definition order is lost before it can be recorded.

      Added in version 3.6.

   _ignore_

      "_ignore_" solo se usa durante la creación y se elimina de la
      enumeración una vez que se completa la creación.

      "_ignore_" es una lista de nombres que no se convertirán en
      miembros y cuyos nombres también se eliminarán de la enumeración
      completa. Consulte TimePeriod para ver un ejemplo.

      Added in version 3.7.

   __dir__(self)

      Retorna "['__class__', '__doc__', '__module__', 'name',
      'value']" y cualquier método público definido en
      *self.__class__*:

         >>> from enum import Enum
         >>> import datetime as dt
         >>> class Weekday(Enum):
         ...     MONDAY = 1
         ...     TUESDAY = 2
         ...     WEDNESDAY = 3
         ...     THURSDAY = 4
         ...     FRIDAY = 5
         ...     SATURDAY = 6
         ...     SUNDAY = 7
         ...     @classmethod
         ...     def today(cls):
         ...         print(f'today is {cls(dt.date.today().isoweekday()).name}')
         ...
         >>> dir(Weekday.SATURDAY)
         ['__class__', '__doc__', '__eq__', '__hash__', '__module__', 'name', 'today', 'value']

   _generate_next_value_(name, start, count, last_values)

         name:
            El nombre del miembro que se está definiendo (por ejemplo,
            'RED').

         start:
            El valor inicial de Enum; el valor predeterminado es 1.

         count:
            El número de miembros actualmente definidos, sin incluir
            este.

         last_values:
            Una lista de los valores anteriores.

      A *staticmethod* that is used to determine the next value
      returned by "auto".

      Nota:

        For standard "Enum" classes the next value chosen is the
        highest value seen incremented by one.For "Flag" classes the
        next value chosen will be the next highest power-of-two.

      This method may be overridden, e.g.:

         >>> from enum import auto, Enum
         >>> class PowersOfThree(Enum):
         ...     @staticmethod
         ...     def _generate_next_value_(name, start, count, last_values):
         ...         return 3 ** (count + 1)
         ...     FIRST = auto()
         ...     SECOND = auto()
         ...
         >>> PowersOfThree.SECOND.value
         9

      Added in version 3.6.

      Distinto en la versión 3.13: Prior versions would use the last
      seen value instead of the highest value.

   __init__(self, *args, **kwds)

      By default, does nothing.  If multiple values are given in the
      member assignment, those values become separate arguments to
      "__init__"; e.g.

      >>> from enum import Enum
      >>> class Weekday(Enum):
      ...     MONDAY = 1, 'Mon'

      "Weekday.__init__()" would be called as "Weekday.__init__(self,
      1, 'Mon')"

   __init_subclass__(cls, **kwds)

      Un *classmethod* que se usa para configurar más subclases
      subsiguientes. Por defecto, no hace nada.

   _missing_(cls, value)

      Un *classmethod* para buscar valores que no se encuentran en
      *cls*. De forma predeterminada, no hace nada, pero se puede
      anular para implementar un comportamiento de búsqueda
      personalizado:

         >>> from enum import auto, StrEnum
         >>> class Build(StrEnum):
         ...     DEBUG = auto()
         ...     OPTIMIZED = auto()
         ...     @classmethod
         ...     def _missing_(cls, value):
         ...         value = value.lower()
         ...         for member in cls:
         ...             if member.value == value:
         ...                 return member
         ...         return None
         ...
         >>> Build.DEBUG.value
         'debug'
         >>> Build('deBUG')
         <Build.DEBUG: 'debug'>

      Added in version 3.6.

   __new__(cls, *args, **kwds)

      By default, doesn't exist.  If specified, either in the enum
      class definition or in a mixin class (such as "int"), all values
      given in the member assignment will be passed; e.g.

      >>> from enum import Enum
      >>> class MyIntEnum(int, Enum):
      ...     TWENTYSIX = '1a', 16

      results in the call "int('1a', 16)" and a value of "26" for the
      member.

      Nota:

        When writing a custom "__new__", do not use "super().__new__"
        -- call the appropriate "__new__" instead.

   __repr__(self)

      Retorna la cadena utilizada para las llamadas *repr()*. De forma
      predeterminada, retorna el nombre *Enum*, el nombre del miembro
      y el valor, pero se puede anular:

         >>> from enum import auto, Enum
         >>> class OtherStyle(Enum):
         ...     ALTERNATE = auto()
         ...     OTHER = auto()
         ...     SOMETHING_ELSE = auto()
         ...     def __repr__(self):
         ...         cls_name = self.__class__.__name__
         ...         return f'{cls_name}.{self.name}'
         ...
         >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
         (OtherStyle.ALTERNATE, 'OtherStyle.ALTERNATE', 'OtherStyle.ALTERNATE')

   __str__(self)

      Retorna la cadena utilizada para las llamadas *str()*. De forma
      predeterminada, retorna el nombre *Enum* y el nombre del
      miembro, pero se puede anular:

         >>> from enum import auto, Enum
         >>> class OtherStyle(Enum):
         ...     ALTERNATE = auto()
         ...     OTHER = auto()
         ...     SOMETHING_ELSE = auto()
         ...     def __str__(self):
         ...         return f'{self.name}'
         ...
         >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
         (<OtherStyle.ALTERNATE: 1>, 'ALTERNATE', 'ALTERNATE')

   __format__(self)

      Returns the string used for *format()* and *f-string* calls.  By
      default, returns "__str__()" return value, but can be
      overridden:

         >>> from enum import auto, Enum
         >>> class OtherStyle(Enum):
         ...     ALTERNATE = auto()
         ...     OTHER = auto()
         ...     SOMETHING_ELSE = auto()
         ...     def __format__(self, spec):
         ...         return f'{self.name}'
         ...
         >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
         (<OtherStyle.ALTERNATE: 1>, 'OtherStyle.ALTERNATE', 'ALTERNATE')

   Nota:

     El uso de "auto" con "Enum" da como resultado números enteros de
     valor creciente, comenzando con "1".

   Distinto en la versión 3.12: Added Soporte de Dataclass

   _add_alias_()

      Adds a new name as an alias to an existing member:

         >>> Color.RED._add_alias_("ERROR")
         >>> Color.ERROR
         <Color.RED: 1>

      Raises a "NameError" if the name is already assigned to a
      different member.

      Added in version 3.13.

   _add_value_alias_()

      Adds a new value as an alias to an existing member:

         >>> Color.RED._add_value_alias_(42)
         >>> Color(42)
         <Color.RED: 1>

         Raises a "ValueError" if the value is already linked with a different member.
         See MultiValueEnum for an example.

      Added in version 3.13.

class enum.IntEnum

   *IntEnum* is the same as "Enum", but its members are also integers
   and can be used anywhere that an integer can be used.  If any
   integer operation is performed with an *IntEnum* member, the
   resulting value loses its enumeration status.

   >>> from enum import IntEnum
   >>> class Number(IntEnum):
   ...     ONE = 1
   ...     TWO = 2
   ...     THREE = 3
   ...
   >>> Number.THREE
   <Number.THREE: 3>
   >>> Number.ONE + Number.TWO
   3
   >>> Number.THREE + 5
   8
   >>> Number.THREE == 3
   True

   Nota:

     El uso de "auto" con "IntEnum" da como resultado números enteros
     de valor creciente, comenzando con "1".

   Distinto en la versión 3.11: "__str__()" is now "int.__str__()" to
   better support the *replacement of existing constants* use-case.
   "__format__()" was already "int.__format__()" for that same reason.

class enum.StrEnum

   *StrEnum* is the same as "Enum", but its members are also strings
   and can be used in most of the same places that a string can be
   used. The result of any string operation performed on or with a
   *StrEnum* member is not part of the enumeration.

   >>> from enum import StrEnum, auto
   >>> class Color(StrEnum):
   ...     RED = 'r'
   ...     GREEN = 'g'
   ...     BLUE = 'b'
   ...     UNKNOWN = auto()
   ...
   >>> Color.RED
   <Color.RED: 'r'>
   >>> Color.UNKNOWN
   <Color.UNKNOWN: 'unknown'>
   >>> str(Color.UNKNOWN)
   'unknown'

   Nota:

     There are places in the stdlib that check for an exact "str"
     instead of a "str" subclass (i.e. "type(unknown) == str" instead
     of "isinstance(unknown, str)"), and in those locations you will
     need to use "str(MyStrEnum.MY_MEMBER)".

   Nota:

     El uso de "auto" con "StrEnum" da como resultado el nombre de
     miembro en minúsculas como valor.

   Nota:

     "__str__()" is "str.__str__()" to better support the *replacement
     of existing constants* use-case.  "__format__()" is likewise
     "str.__format__()" for that same reason.

   Added in version 3.11.

class enum.Flag

   "Flag" is the same as "Enum", but its members support the bitwise
   operators "&" (*AND*), "|" (*OR*), "^" (*XOR*), and "~" (*INVERT*);
   the results of those operations are (aliases of) members of the
   enumeration.

   __contains__(self, value)

      Retorna *True* si el valor está en sí mismo:

         >>> from enum import Flag, auto
         >>> class Color(Flag):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> purple = Color.RED | Color.BLUE
         >>> white = Color.RED | Color.GREEN | Color.BLUE
         >>> Color.GREEN in purple
         False
         >>> Color.GREEN in white
         True
         >>> purple in white
         True
         >>> white in purple
         False

   __iter__(self)

      Returns all contained non-alias members:

         >>> list(Color.RED)
         [<Color.RED: 1>]
         >>> list(purple)
         [<Color.RED: 1>, <Color.BLUE: 4>]

      Added in version 3.11.

   __len__(self)

      Retorna el número de miembros en la bandera:

         >>> len(Color.GREEN)
         1
         >>> len(white)
         3

      Added in version 3.11.

   __bool__(self)

      Retorna *True* si hay algún miembro en la bandera, *False* de lo
      contrario:

         >>> bool(Color.GREEN)
         True
         >>> bool(white)
         True
         >>> black = Color(0)
         >>> bool(black)
         False

   __or__(self, other)

      Retorna la bandera actual binaria o con otra:

         >>> Color.RED | Color.GREEN
         <Color.RED|GREEN: 3>

   __and__(self, other)

      Retorna el binario de la bandera actual y se combina con otro:

         >>> purple & white
         <Color.RED|BLUE: 5>
         >>> purple & Color.GREEN
         <Color: 0>

   __xor__(self, other)

      Retorna la bandera actual binaria xor'ed con otra:

         >>> purple ^ white
         <Color.GREEN: 2>
         >>> purple ^ Color.GREEN
         <Color.RED|GREEN|BLUE: 7>

   __invert__(self)

      Returns all the flags in *type(self)* that are not in *self*:

         >>> ~white
         <Color: 0>
         >>> ~purple
         <Color.GREEN: 2>
         >>> ~Color.RED
         <Color.GREEN|BLUE: 6>

   _numeric_repr_()

      Función utilizada para dar formato a los valores numéricos
      restantes sin nombre. El valor predeterminado es la repr del
      valor; las opciones comunes son "hex()" y "oct()".

   Nota:

     El uso de "auto" con "Flag" da como resultado números enteros que
     son potencias de dos, comenzando con "1".

   Distinto en la versión 3.11: The *repr()* of zero-valued flags has
   changed.  It is now:

   >>> Color(0)
   <Color: 0>

class enum.IntFlag

   "IntFlag" is the same as "Flag", but its members are also integers
   and can be used anywhere that an integer can be used.

   >>> from enum import IntFlag, auto
   >>> class Color(IntFlag):
   ...     RED = auto()
   ...     GREEN = auto()
   ...     BLUE = auto()
   ...
   >>> Color.RED & 2
   <Color: 0>
   >>> Color.RED | 2
   <Color.RED|GREEN: 3>

   Si se realiza alguna operación con enteros con un miembro
   *IntFlag*, el resultado no es un *IntFlag*:

      >>> Color.RED + 2
      3

   If a "Flag" operation is performed with an *IntFlag* member and:

   * el resultado es un *IntFlag* válido: se retorna un *IntFlag*

   * the result is not a valid *IntFlag*: the result depends on the
     "FlagBoundary" setting

   The "repr()" of unnamed zero-valued flags has changed.  It is now:

      >>> Color(0)
      <Color: 0>

   Nota:

     El uso de "auto" con "IntFlag" da como resultado números enteros
     que son potencias de dos, comenzando con "1".

   Distinto en la versión 3.11: "__str__()" is now "int.__str__()" to
   better support the *replacement of existing constants* use-case.
   "__format__()" was already "int.__format__()" for that same
   reason.Inversion of an "IntFlag" now returns a positive value that
   is the union of all flags not in the given flag, rather than a
   negative value. This matches the existing "Flag" behavior.

class enum.ReprEnum

   "ReprEnum" uses the "repr()" of "Enum", but the "str()" of the
   mixed-in data type:

   * "int.__str__()" para "IntEnum" y "IntFlag"

   * "str.__str__()" para "StrEnum"

   Inherit from "ReprEnum" to keep the "str()" / "format()" of the
   mixed-in data type instead of using the "Enum"-default "str()".

   Added in version 3.11.

class enum.EnumCheck

   *EnumCheck* contiene las opciones utilizadas por el decorador
   "verify()" para garantizar diversas restricciones; las
   restricciones fallidas dan como resultado un "ValueError".

   UNIQUE

      Asegúrese de que cada valor tenga un solo nombre:

         >>> from enum import Enum, verify, UNIQUE
         >>> @verify(UNIQUE)
         ... class Color(Enum):
         ...     RED = 1
         ...     GREEN = 2
         ...     BLUE = 3
         ...     CRIMSON = 1
         Traceback (most recent call last):
         ...
         ValueError: aliases found in <enum 'Color'>: CRIMSON -> RED

   CONTINUOUS

      Asegúrese de que no falten valores entre el miembro de menor
      valor y el miembro de mayor valor:

         >>> from enum import Enum, verify, CONTINUOUS
         >>> @verify(CONTINUOUS)
         ... class Color(Enum):
         ...     RED = 1
         ...     GREEN = 2
         ...     BLUE = 5
         Traceback (most recent call last):
         ...
         ValueError: invalid enum 'Color': missing values 3, 4

   NAMED_FLAGS

      Ensure that any flag groups/masks contain only named flags --
      useful when values are specified instead of being generated by
      "auto()":

         >>> from enum import Flag, verify, NAMED_FLAGS
         >>> @verify(NAMED_FLAGS)
         ... class Color(Flag):
         ...     RED = 1
         ...     GREEN = 2
         ...     BLUE = 4
         ...     WHITE = 15
         ...     NEON = 31
         Traceback (most recent call last):
         ...
         ValueError: invalid Flag 'Color': aliases WHITE and NEON are missing combined values of 0x18 [use enum.show_flag_values(value) for details]

   Nota:

     CONTINUOUS y NAMED_FLAGS están diseñados para funcionar con
     miembros con valores enteros.

   Added in version 3.11.

class enum.FlagBoundary

   "FlagBoundary" controls how out-of-range values are handled in
   "Flag" and its subclasses.

   STRICT

      Out-of-range values cause a "ValueError" to be raised. This is
      the default for "Flag":

         >>> from enum import Flag, STRICT, auto
         >>> class StrictFlag(Flag, boundary=STRICT):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> StrictFlag(2**2 + 2**4)
         Traceback (most recent call last):
         ...
         ValueError: <flag 'StrictFlag'> invalid value 20
             given 0b0 10100
           allowed 0b0 00111

   CONFORM

      Out-of-range values have invalid values removed, leaving a valid
      "Flag" value:

         >>> from enum import Flag, CONFORM, auto
         >>> class ConformFlag(Flag, boundary=CONFORM):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> ConformFlag(2**2 + 2**4)
         <ConformFlag.BLUE: 4>

   EJECT

      Out-of-range values lose their "Flag" membership and revert to
      "int".

      >>> from enum import Flag, EJECT, auto
      >>> class EjectFlag(Flag, boundary=EJECT):
      ...     RED = auto()
      ...     GREEN = auto()
      ...     BLUE = auto()
      ...
      >>> EjectFlag(2**2 + 2**4)
      20

   KEEP

      Out-of-range values are kept, and the "Flag" membership is kept.
      This is the default for "IntFlag":

         >>> from enum import Flag, KEEP, auto
         >>> class KeepFlag(Flag, boundary=KEEP):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> KeepFlag(2**2 + 2**4)
         <KeepFlag.BLUE|16: 20>

   Added in version 3.11.

class enum.EnumDict

   *EnumDict* is a subclass of "dict" that is used as the namespace
   for defining enum classes (see Preparando el espacio de nombres de
   la clase). It is exposed to allow subclasses of "EnumType" with
   advanced behavior like having multiple values per member. It should
   be called with the name of the enum class being created, otherwise
   private names and internal classes will not be handled correctly.

   Note that only the "MutableMapping" interface ("__setitem__()" and
   "update()") is overridden. It may be possible to bypass the checks
   using other "dict" operations like "|=".

   member_names

      A list of member names.

   Added in version 3.13.

======================================================================

### Nombres soportados "__dunder__"

"__members__" is a read-only ordered mapping of "member_name":"member"
items.  It is only available on the class.

"__new__()", if specified, must create and return the enum members; it
is also a very good idea to set the member's "_value_" appropriately.
Once all the members are created it is no longer used.

### Nombres "_sunder_" compatibles

* "_name_" -- name of the member

* "_value_" -- value of the member; can be set in "__new__"

* "_missing_()" -- a lookup function used when a value is not found;
  may be overridden

* "_ignore_" -- a list of names, either as a "list" or a "str", that
  will not be transformed into members, and will be removed from the
  final class

* "_order_" -- no longer used, kept for backward compatibility (class
  attribute, removed during class creation)

* "_generate_next_value_()" -- used to get an appropriate value for an
  enum member; may be overridden

* "_add_alias_()" -- adds a new name as an alias to an existing
  member.

* "_add_value_alias_()" -- adds a new value as an alias to an existing
  member.

* While "_sunder_" names are generally reserved for the further
  development of the "Enum" class and can not be used, some are
  explicitly allowed:

  * "_repr_*" (e.g. "_repr_html_"), as used in IPython's rich display

Added in version 3.6: "_missing_", "_order_", "_generate_next_value_"

Added in version 3.7: "_ignore_"

Added in version 3.13: "_add_alias_", "_add_value_alias_", "_repr_*"

======================================================================

## Utilities and decorators

class enum.auto

   *auto* can be used in place of a value.  If used, the *Enum*
   machinery will call an "Enum"'s "_generate_next_value_()" to get an
   appropriate value. For "Enum" and "IntEnum" that appropriate value
   will be the last value plus one; for "Flag" and "IntFlag" it will
   be the first power-of-two greater than the highest value; for
   "StrEnum" it will be the lower-cased version of the member's name.
   Care must be taken if mixing *auto()* with manually specified
   values.

   *auto* instances are only resolved when at the top level of an
   assignment, either by itself or as part of a tuple:

   * "FIRST = auto()" will work (auto() is replaced with "1");

   * "SECOND = auto(), -2" will work (auto is replaced with "2", so
     "2, -2" is used to create the "SECOND" enum member;

   * "THREE = [auto(), -3]" will *not* work ("[<auto instance>, -3]"
     is used to create the "THREE" enum member)

   Distinto en la versión 3.11.1: In prior versions, "auto()" had to
   be the only thing on the assignment line to work properly.

   "_generate_next_value_" se puede anular para personalizar los
   valores utilizados por *auto*.

   Nota:

     in 3.13 the default "_generate_next_value_" will always return
     the highest member value incremented by 1, and will fail if any
     member is an incompatible type.

@enum.property

   A decorator similar to the built-in "@property", but specifically
   for enumerations.  It allows member attributes to have the same
   names as members themselves.

   Nota:

     el *property* y el miembro deben definirse en clases separadas;
     por ejemplo, los atributos *value* y *name* se definen en la
     clase *Enum* y las subclases *Enum* pueden definir miembros con
     los nombres "value" y "name".

   Added in version 3.11.

@enum.unique

   A "class" decorator specifically for enumerations.  It searches an
   enumeration's "__members__", gathering any aliases it finds; if any
   are found "ValueError" is raised with the details:

      >>> from enum import Enum, unique
      >>> @unique
      ... class Mistake(Enum):
      ...     ONE = 1
      ...     TWO = 2
      ...     THREE = 3
      ...     FOUR = 3
      ...
      Traceback (most recent call last):
      ...
      ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

@enum.verify

   Un decorador "class" específicamente para enumeraciones. Los
   miembros de "EnumCheck" se utilizan para especificar qué
   restricciones deben verificarse en la enumeración decorada.

   Added in version 3.11.

@enum.member

   Un decorador para usar en enumeraciones: su objetivo se convertirá
   en miembro.

   Added in version 3.11.

@enum.nonmember

   Un decorador para usar en enumeraciones: su destino no se
   convertirá en miembro.

   Added in version 3.11.

@enum.global_enum

   Un decorador para cambiar el "str()" y "repr()" de una enumeración
   para mostrar sus miembros como pertenecientes al módulo en lugar de
   a su clase. Solo debe usarse cuando los miembros de la enumeración
   se exportan al espacio de nombres global del módulo (consulte
   "re.RegexFlag" para ver un ejemplo).

   Added in version 3.11.

enum.show_flag_values(value)

   Retorna una lista de todos los enteros de potencia de dos
   contenidos en un indicador *value*.

   Added in version 3.11.

enum.bin(num, max_bits=None)

   Like built-in "bin()", except negative values are represented in
   two's complement, and the leading bit always indicates sign ("0"
   implies positive, "1" implies negative).

   >>> import enum
   >>> enum.bin(10)
   '0b0 1010'
   >>> enum.bin(~10)   # ~10 is -11
   '0b1 0101'

   Added in version 3.11.

======================================================================

## Notas

"IntEnum", "StrEnum" y "IntFlag"

   Estos tres tipos de enumeración están diseñados para ser reemplazos
   directos de los valores existentes basados ​​en cadenas y enteros;
   como tales, tienen limitaciones adicionales:

   * "__str__" usa el valor y no el nombre del miembro de enumeración

   * "__format__", debido a que usa "__str__", también usará el valor
     del miembro de enumeración en lugar de su nombre

   Si no necesita/quiere esas limitaciones, puede crear su propia
   clase base mezclando el tipo "int" o "str" usted mismo:

      >>> from enum import Enum
      >>> class MyIntEnum(int, Enum):
      ...     pass

   o puede reasignar el "str()" apropiado, etc., en su enumeración:

      >>> from enum import Enum, IntEnum
      >>> class MyIntEnum(IntEnum):
      ...     __str__ = Enum.__str__
