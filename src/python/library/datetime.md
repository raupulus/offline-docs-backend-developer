---
title: '"datetime" --- Basic date and time types'
source_url: https://docs.python.org/es/3
source_path: library/datetime.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2260
---

# "datetime" --- Basic date and time types

**Código fuente:** Lib/datetime.py

======================================================================

The "datetime" module supplies classes for manipulating dates and
times.

Si bien la implementación permite operaciones aritméticas con fechas y
horas, su principal objetivo es poder extraer campos de forma
eficiente para su posterior manipulación o formateo.

Truco:

  Skip to the format codes.

Ver también:

  Módulo "calendar"
     Funciones generales relacionadas a *calendar*.

  Módulo "time"
     Acceso a tiempo y conversiones.

  Módulo "zoneinfo"
     Zonas horarias concretas que representan la base de datos de
     zonas horarias de la IANA.

  Paquete dateutil
     Biblioteca de terceros con zona horaria ampliada y soporte de
     análisis.

  Package DateType
     Third-party library that introduces distinct static types to for
     example, allow *static type checkers* to differentiate between
     naive and aware datetimes.

## Aware and naive objects

Date and time objects may be categorized as "aware" or "naive"
depending on whether or not they include time zone information.

Con suficiente conocimiento de los ajustes de tiempo políticos y
algorítmicos aplicables, como la zona horaria y la información del
horario de verano, un objeto **consciente** puede ubicarse en relación
con otros objetos conscientes. Un objeto consciente representa un
momento específico en el tiempo que no está abierto a interpretación.
[1]

A **naive** object does not contain enough information to
unambiguously locate itself relative to other date/time objects.
Whether a naive object represents Coordinated Universal Time (UTC),
local time, or time in some other time zone is purely up to the
program, just like it is up to the program whether a particular number
represents metres, miles, or mass. Naive objects are easy to
understand and to work with, at the cost of ignoring some aspects of
reality.

For applications requiring aware objects, "datetime" and "time"
objects have an optional time zone information attribute, "tzinfo",
that can be set to an instance of a subclass of the abstract "tzinfo"
class. These "tzinfo" objects capture information about the offset
from UTC time, the time zone name, and whether daylight saving time is
in effect.

Only one concrete "tzinfo" class, the "timezone" class, is supplied by
the "datetime" module. The "timezone" class can represent simple time
zones with fixed offsets from UTC, such as UTC itself or North
American EST and EDT time zones. Supporting time zones at deeper
levels of detail is up to the application. The rules for time
adjustment across the world are more political than rational, change
frequently, and there is no standard suitable for every application
aside from UTC.

## Constantes

The "datetime" module exports the following constants:

datetime.MINYEAR

   The smallest year number allowed in a "date" or "datetime" object.
   "MINYEAR" is 1.

datetime.MAXYEAR

   The largest year number allowed in a "date" or "datetime" object.
   "MAXYEAR" is 9999.

datetime.UTC

   Alias for the UTC time zone singleton "datetime.timezone.utc".

   Added in version 3.11.

## Available types

class datetime.date

   Una fecha naíf (*naive*) idealizada, suponiendo que el calendario
   gregoriano actual siempre estuvo, y siempre estará, vigente.
   Atributos: "year", "month", y "day".

class datetime.time

   Un tiempo idealizado, independiente de cualquier día en particular,
   suponiendo que cada día tenga exactamente 24* 60* 60 segundos.
   (Aquí no hay noción de "segundos intercalares".) Atributos: "hour",
   "minute", "second", "microsecond", y "tzinfo".

class datetime.datetime

   Una combinación de una fecha y una hora. Atributos: "year",
   "month", "day", "hour", "minute", "second", "microsecond" , y
   "tzinfo".

class datetime.timedelta

   A duration expressing the difference between two "datetime" or
   "date" instances to microsecond resolution.

class datetime.tzinfo

   Una clase base abstracta para objetos de información de zona
   horaria. Estos son utilizados por las clases "datetime" y "time"
   para proporcionar una noción personalizable de ajuste de hora (por
   ejemplo, para tener en cuenta la zona horaria y / o el horario de
   verano).

class datetime.timezone

   Una clase que implementa la clase de base abstracta "tzinfo" como
   un desplazamiento fijo desde el UTC.

   Added in version 3.2.

Los objetos de este tipo son inmutables.

Subclass relationships:

   [imagen: timedelta, tzinfo, time, and date inherit from object;
   timezone inherits from tzinfo; and datetime inherits from
   date.][imagen]

### Common properties

Las clases "date", "datetime", "time", y "timezone" comparten estas
características comunes:

* Los objetos de este tipo son inmutables.

* Objects of these types are *hashable*, meaning that they can be used
  as dictionary keys.

* Los objetos de este tipo admiten el *pickling* eficiente a través
  del módulo "pickle".

### Determining if an object is aware or naive

Los objetos del tipo "date" son siempre naíf (*naive*).

Un objeto de tipo "time" o "datetime" puede ser consciente (*aware*) o
naíf (*naive*).

A "datetime" object "d" is aware if both of the following hold:

1. "d.tzinfo" no es "None"

2. "d.tzinfo.utcoffset(d)" no retorna "None"

Otherwise, "d" is naive.

A "time" object "t" is aware if both of the following hold:

1. "t.tzinfo" no es "None"

2. "t.tzinfo.utcoffset(None)" no retorna "None".

Otherwise, "t" is naive.

La distinción entre los objetos consciente (*aware*) y naíf (*naive*)
no se aplica a "timedelta".

## "timedelta" objects

A "timedelta" object represents a duration, the difference between two
"datetime" or "date" instances.

class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

   All arguments are optional and default to 0. Arguments may be
   integers or floats, and may be positive or negative.

   Solo *days*, *seconds* y *microseconds* se almacenan internamente.
   Los argumentos se convierten a esas unidades:

   * Un milisegundo se convierte a 1000 microsegundos.

   * Un minuto se convierte a 60 segundos.

   * Una hora se convierte a 3600 segundos.

   * Una semana se convierte a 7 días.

   y los días, segundos y microsegundos se normalizan para que la
   representación sea única, con

   * "0 <= microsegundos < 1000000"

   * "0 <= segundos< 3600*24" (el número de segundos en un día)

   * "-999999999 <= days <= 999999999"

   El siguiente ejemplo ilustra cómo cualquier argumento además de
   *days*, *seconds* y *microseconds* se "fusionan" y normalizan en
   esos tres atributos resultantes:

      >>> import datetime as dt
      >>> delta = dt.timedelta(
      ...     days=50,
      ...     seconds=27,
      ...     microseconds=10,
      ...     milliseconds=29000,
      ...     minutes=5,
      ...     hours=8,
      ...     weeks=2
      ... )
      >>> # Only days, seconds, and microseconds remain
      >>> delta
      datetime.timedelta(days=64, seconds=29156, microseconds=10)

   Truco:

     "import datetime as dt" instead of "import datetime" or "from
     datetime import datetime" to avoid confusion between the module
     and the class. See How I Import Python’s datetime Module.

   Si algún argumento es flotante y hay microsegundos fraccionarios,
   los microsegundos fraccionarios que quedan de todos los argumentos
   se combinan y su suma se redondea al microsegundo más cercano
   utilizando el desempate de medio redondeo a par. Si ningún
   argumento es flotante, los procesos de conversión y normalización
   son exactos (no se pierde información).

   Si el valor normalizado de los días se encuentra fuera del rango
   indicado, se lanza "OverflowError".

   Tenga en cuenta que la normalización de los valores negativos puede
   ser sorprendente al principio. Por ejemplo:

      >>> import datetime as dt
      >>> d = dt.timedelta(microseconds=-1)
      >>> (d.days, d.seconds, d.microseconds)
      (-1, 86399, 999999)

   Since the string representation of "timedelta" objects can be
   confusing, use the following recipe to produce a more readable
   format:

      >>> def pretty_timedelta(td):
      ...     if td.days >= 0:
      ...         return str(td)
      ...     return f'-({-td!s})'
      ...
      >>> d = timedelta(hours=-1)
      >>> str(d)  # not human-friendly
      '-1 day, 23:00:00'
      >>> pretty_timedelta(d)
      '-(1:00:00)'

Atributos de clase:

timedelta.min

   El objeto más negativo en "timedelta", "timedelta(-999999999)".

timedelta.max

   El objeto más positivo de la "timedelta",
   "timedelta(days=999999999, hours=23, minutes=59, seconds=59,
   microseconds=999999)".

timedelta.resolution

   La diferencia más pequeña posible entre los objetos no iguales
   "timedelta" "timedelta(microseconds=1)".

Note that, because of normalization, "timedelta.max" is greater than
"-timedelta.min". "-timedelta.max" is not representable as a
"timedelta" object.

Atributos de instancia (solo lectura):

timedelta.days

   Between -999,999,999 and 999,999,999 inclusive.

timedelta.seconds

   Between 0 and 86,399 inclusive.

   Prudencia:

     It is a somewhat common bug for code to unintentionally use this
     attribute when it is actually intended to get a "total_seconds()"
     value instead:

        >>> import datetime as dt
        >>> duration = dt.timedelta(seconds=11235813)
        >>> duration.days, duration.seconds
        (130, 3813)
        >>> duration.total_seconds()
        11235813.0

timedelta.microseconds

   Between 0 and 999,999 inclusive.

Operaciones soportadas:

+----------------------------------+-------------------------------------------------+
| Operación                        | Resultado                                       |
|==================================|=================================================|
| "t1 = t2 + t3"                   | Sum of "t2" and "t3". Afterwards "t1 - t2 ==    |
## |                                  | t3" and "t1 - t3 == t2" are true. (1)           |

| "t1 = t2 - t3"                   | Difference of "t2"  and "t3". Afterwards "t1 == |
## |                                  | t2 - t3" and "t2 == t1 + t3" are true. (1)(6)   |

| "t1 = t2 * i o t1 = i * t2"      | Delta multiplied by an integer. Afterwards "t1  |
## |                                  | // i == t2" is true, provided "i != 0".         |

|                                  | In general, "t1  * i == t1 * (i-1) + t1" is     |
## |                                  | true. (1)                                       |

| "t1 = t2 * f o t1 = f * t2"      | Delta multiplicado por un número decimal. El    |
|                                  | resultado se redondea al múltiplo mas cercano   |
|                                  | de *timedelta.resolution* usando redondeo de    |
## |                                  | medio a par.                                    |

| "f = t2 / t3"                    | Division (3) of overall duration "t2" by        |
## |                                  | interval unit "t3". Returns a "float" object.   |

| "t1 = t2 / f o t1 = t2 / i"      | Delta dividido por un número decimal o un       |
|                                  | entero. El resultado se redondea al múltiplo    |
|                                  | más cercano de *timedelta.resolution* usando    |
## |                                  | redondeo de medio a par.                        |

| "t1 = t2 // i" o "t1 = t2 // t3" | El piso (*floor*) se calcula y el resto (si lo  |
|                                  | hay) se descarta. En el segundo caso, se        |
## |                                  | retorna un entero. (3)                          |

| "t1 = t2 % t3"                   | El resto se calcula como un objeto "timedelta". |
## |                                  | (3)                                             |

| "q, r = divmod(t1, t2)"          | Computes the quotient and the remainder: "q =   |
|                                  | t1 // t2" (3) and "r = t1 % t2". "q" is an      |
## |                                  | integer and "r" is a "timedelta" object.        |

| "+t1"                            | Retorna un objeto "timedelta" con el mismo      |
## |                                  | valor. (2)                                      |

| "-t1"                            | Equivalent to "timedelta(-t1.days, -t1.seconds, |
## |                                  | -t1.microseconds)", and to "t1 * -1". (1)(4)    |

| "abs(t)"                         | Equivalent to "+t" when "t.days >= 0", and to   |
## |                                  | "-t" when "t.days < 0". (2)                     |

| "str(t)"                         | Retorna una cadena de caracteres en la forma    |
|                                  | "[D day[s], ][H]H:MM:SS[.UUUUUU]", donde D es   |
## |                                  | negativo para negativo "t". (5)                 |

| "repr(t)"                        | Retorna una representación de cadena del objeto |
|                                  | "timedelta" como una llamada de constructor con |
## |                                  | valores de atributos canónicos.                 |

Notas:

1. Esto es exacto pero puede desbordarse.

2. Esto es exacto pero no puede desbordarse.

3. Division by zero raises "ZeroDivisionError".

4. "-timedelta.max" is not representable as a "timedelta" object.

5. Las representaciones de cadena de caracteres de los objetos
   "timedelta" se normalizan de manera similar a su representación
   interna. Esto conduce a resultados algo inusuales para *timedeltas*
   negativos. Por ejemplo:

      >>> timedelta(hours=-5)
      datetime.timedelta(days=-1, seconds=68400)
      >>> print(_)
      -1 day, 19:00:00

6. La expresión "t2 - t3" siempre será igual a la expresión "t2 +
   (-t3)" excepto cuando *t3* es igual a "timedelta.max"; en ese caso,
   el primero producirá un resultado mientras que el segundo se
   desbordará.

Además de las operaciones enumeradas anteriormente, los objetos
"timedelta" admiten ciertas sumas y restas con objetos "date" y
"datetime" (ver más abajo).

Distinto en la versión 3.2: Floor division and true division of a
"timedelta" object by another "timedelta" object are now supported, as
are remainder operations and the "divmod()" function. True division
and multiplication of a "timedelta" object by a "float" object are now
supported.

"timedelta" objects support equality and order comparisons.

En contextos booleanos, un objeto "timedelta" se considera verdadero
si y solo si no es igual a "timedelta (0)".

Métodos de instancia:

timedelta.total_seconds()

   Return the total number of seconds contained in the duration.
   Equivalent to "td / timedelta(seconds=1)". For interval units other
   than seconds, use the division form directly (for example, "td /
   timedelta(microseconds=1)").

   Tenga en cuenta que para intervalos de tiempo muy largos (más de
   270 años en la mayoría de las plataformas) este método perderá
   precisión de microsegundos.

   Added in version 3.2.

### Examples of usage: "timedelta"

Ejemplos adicionales de normalización:

   >>> # Components of another_year add up to exactly 365 days
   >>> import datetime as dt
   >>> year = dt.timedelta(days=365)
   >>> another_year = dt.timedelta(weeks=40, days=84, hours=23,
   ...                             minutes=50, seconds=600)
   >>> year == another_year
   True
   >>> year.total_seconds()
   31536000.0

Ejemplos de "timedelta" aritmética:

   >>> import datetime as dt
   >>> year = dt.timedelta(days=365)
   >>> ten_years = 10 * year
   >>> ten_years
   datetime.timedelta(days=3650)
   >>> ten_years.days // 365
   10
   >>> nine_years = ten_years - year
   >>> nine_years
   datetime.timedelta(days=3285)
   >>> three_years = nine_years // 3
   >>> three_years, three_years.days // 365
   (datetime.timedelta(days=1095), 3)

## "date" objects

El objeto "date" representa una fecha (año, mes y día) en un
calendario idealizado, el calendario gregoriano actual se extiende
indefinidamente en ambas direcciones.

El 1 de enero del año 1 se llama día número 1, el 2 de enero del año 1
se llama día número 2, y así sucesivamente. [2]

class datetime.date(year, month, day)

   Todos los argumentos son obligatorios. Los argumentos deben ser
   enteros, en los siguientes rangos:

   * "MINYEAR <= year <= MAXYEAR"

   * "1 <= month <= 12"

   * "1 <= day <= number of days in the given month and year"

   Si se proporciona un argumento fuera de esos rangos, "ValueError"
   se genera.

Otros constructores, todos los métodos de clase:

classmethod date.today()

   Retorna la fecha local actual.

   Esto es equivalente a "date.fromtimestamp(time.time())".

classmethod date.fromtimestamp(timestamp)

   Return the local date corresponding to the POSIX *timestamp*, such
   as is returned by "time.time()".

   Esto puede generar "OverflowError", si la marca de tiempo está
   fuera del rango de valores admitidos por la plataforma *C*
   "localtime()", y "OSError" en "localtime()" falla . Es común que
   esto se restrinja a años desde 1970 hasta 2038. Tenga en cuenta que
   en los sistemas que no son POSIX que incluyen segundos bisiestos en
   su noción de marca de tiempo, los segundos bisiestos son ignorados
   por "fromtimestamp()".

   Distinto en la versión 3.3: Se genera "OverflowError" en lugar de
   "ValueError" si la marca de tiempo está fuera del rango de valores
   admitidos por la plataforma *C* "localtime()". Se genera "OSError"
   en lugar de "ValueError" cuando "localtime()", falla.

classmethod date.fromordinal(ordinal)

   Return the date corresponding to the proleptic Gregorian *ordinal*,
   where January 1 of year 1 has ordinal 1.

   "ValueError" is raised unless "1 <= ordinal <=
   date.max.toordinal()". For any date "d",
   "date.fromordinal(d.toordinal()) == d".

classmethod date.fromisoformat(date_string)

   Return a "date" corresponding to a *date_string* given in any valid
   ISO 8601 format, with the following exceptions:

   1. Reduced precision dates are not currently supported ("YYYY-MM",
      "YYYY").

   2. Extended date representations are not currently supported
      ("±YYYYYY-MM-DD").

   3. Ordinal dates are not currently supported ("YYYY-OOO").

   Ejemplos:

      >>> import datetime as dt
      >>> dt.date.fromisoformat('2019-12-04')
      datetime.date(2019, 12, 4)
      >>> dt.date.fromisoformat('20191204')
      datetime.date(2019, 12, 4)
      >>> dt.date.fromisoformat('2021-W01-1')
      datetime.date(2021, 1, 4)

   Added in version 3.7.

   Distinto en la versión 3.11: Anteriormente, este método solo
   admitía el formato "YYYY-MM-DD".

classmethod date.fromisocalendar(year, week, day)

   Return a "date" corresponding to the ISO calendar date specified by
   *year*, *week* and *day*. This is the inverse of the function
   "date.isocalendar()".

   Added in version 3.8.

classmethod date.strptime(date_string, format)

   Return a "date" corresponding to *date_string*, parsed according to
   *format*. This is equivalent to:

      date(*(time.strptime(date_string, format)[0:3]))

   "ValueError" is raised if the date_string and format can't be
   parsed by "time.strptime()" or if it returns a value which isn't a
   time tuple.  See also strftime() and strptime() behavior and
   "date.fromisoformat()".

   Nota:

     If *format* specifies a day of month without a year a
     "DeprecationWarning" is emitted.  This is to avoid a quadrennial
     leap year bug in code seeking to parse only a month and day as
     the default year used in absence of one in the format is not a
     leap year. Such *format* values may raise an error as of Python
     3.15.  The workaround is to always include a year in your
     *format*.  If parsing *date_string* values that do not have a
     year, explicitly add a year that is a leap year before parsing:

        >>> import datetime as dt
        >>> date_string = "02/29"
        >>> when = dt.date.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
        >>> when.strftime("%B %d")
        'February 29'

   Added in version 3.14.

Atributos de clase:

date.min

   La fecha representable más antigua, "date(MINYEAR, 1, 1)".

date.max

   La última fecha representable, "date(MAXYEAR, 12, 31)".

date.resolution

   La menor diferencia entre objetos de fecha no iguales,
   "timedelta(days=1)".

Atributos de instancia (solo lectura):

date.year

   Entre "MINYEAR" y "MAXYEAR" inclusive.

date.month

   Entre 1 y 12 inclusive.

date.day

   Entre 1 y el número de días en el mes dado del año dado.

Operaciones soportadas:

+---------------------------------+------------------------------------------------+
| Operación                       | Resultado                                      |
|=================================|================================================|
| "date2 = date1 + timedelta"     | "date2" will be "timedelta.days" days after    |
## |                                 | "date1". (1)                                   |

| "date2 = date1 - timedelta"     | Computes "date2" such that "date2 + timedelta  |
## |                                 | == date1". (2)                                 |

## | "timedelta = date1 - date2"     | (3)                                            |

| "date1 == date2" "date1 !=      | Equality comparison. (4)                       |
## | date2"                          |                                                |

| "date1 < date2" "date1 > date2" | Order comparison. (5)                          |
| "date1 <= date2" "date1 >=      |                                                |
## | date2"                          |                                                |

Notas:

1. *date2* se mueve hacia adelante en el tiempo si "timedelta.days >
   0", o hacia atrás si "timedelta.days < 0". Después "date2 - date1
   == timedelta. days". "timedelta.seconds" y "timedelta.microseconds"
   se ignoran. "OverflowError" se lanza si "date2.year" sería menor
   que "MINYEAR" o mayor que "MAXYEAR".

2. "timedelta.seconds" y "timedelta.microseconds" son ignorados.

3. This is exact, and cannot overflow. "timedelta.seconds" and
   "timedelta.microseconds" are 0, and "date2 + timedelta == date1"
   after.

4. "date" objects are equal if they represent the same date.

   "date" objects that are not also "datetime" instances are never
   equal to "datetime" objects, even if they represent the same date.

5. *date1* is considered less than *date2* when *date1* precedes
   *date2* in time. In other words, "date1 < date2" if and only if
   "date1.toordinal() < date2.toordinal()".

   Order comparison between a "date" object that is not also a
   "datetime" instance and a "datetime" object raises "TypeError".

Distinto en la versión 3.13: Comparison between "datetime" object and
an instance of the "date" subclass that is not a "datetime" subclass
no longer converts the latter to "date", ignoring the time part and
the time zone. The default behavior can be changed by overriding the
special comparison methods in subclasses.

En contextos booleanos, todos los objetos "date" se consideran
verdaderos.

Métodos de instancia:

date.replace(year=self.year, month=self.month, day=self.day)

   Return a new "date" object with the same values, but with specified
   parameters updated.

   Ejemplo:

      >>> import datetime as dt
      >>> d = dt.date(2002, 12, 31)
      >>> d.replace(day=26)
      datetime.date(2002, 12, 26)

   The generic function "copy.replace()" also supports "date" objects.

date.timetuple()

   Retorna una "time.struct_time" como la que retorna
   "time.localtime()".

   Las horas, minutos y segundos son 0, y el indicador DST es -1.

   "d.timetuple()" es equivalente a:

      time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1))

   where "yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1"
   is the day number within the current year starting with 1 for
   January 1st.

date.toordinal()

   Return the proleptic Gregorian ordinal of the date, where January 1
   of year 1 has ordinal 1. For any "date" object "d",
   "date.fromordinal(d.toordinal()) == d".

date.weekday()

   Retorna el día de la semana como un número entero, donde el lunes
   es 0 y el domingo es 6. Por ejemplo, "date(2002, 12, 4).weekday()
   == 2", un miércoles. Ver también "isoweekday()".

date.isoweekday()

   Retorna el día de la semana como un número entero, donde el lunes
   es 1 y el domingo es 7. Por ejemplo, "date(2002, 12,
   4).isoweekday() == 3", un miércoles. Ver también "weekday()",
   "isocalendar()".

date.isocalendar()

   Retorna un objeto *named tuple* con tres componentes: "year",
   "week" y "weekday".

   El calendario ISO es una variante amplia utilizada del calendario
   gregoriano. [3]

   El año ISO consta de 52 o 53 semanas completas, y donde una semana
   comienza un lunes y termina un domingo. La primera semana de un año
   ISO es la primera semana calendario (gregoriana) de un año que
   contiene un jueves. Esto se llama semana número 1, y el año ISO de
   ese jueves es el mismo que el año gregoriano.

   Por ejemplo, 2004 comienza en jueves, por lo que la primera semana
   del año ISO 2004 comienza el lunes 29 de diciembre de 2003 y
   termina el domingo 4 de enero de 2004

      >>> import datetime as dt
      >>> dt.date(2003, 12, 29).isocalendar()
      datetime.IsoCalendarDate(year=2004, week=1, weekday=1)
      >>> dt.date(2004, 1, 4).isocalendar()
      datetime.IsoCalendarDate(year=2004, week=1, weekday=7)

   Distinto en la versión 3.9: El resultado cambió de una tupla a un
   *named tuple*.

date.isoformat()

   Retorna una cadena de caracteres que representa la fecha en formato
   ISO 8601, "AAAA-MM-DD":

      >>> import datetime as dt
      >>> dt.date(2002, 12, 4).isoformat()
      '2002-12-04'

date.__str__()

   For a date "d", "str(d)" is equivalent to "d.isoformat()".

date.ctime()

   Retorna una cadena de caracteres que representa la fecha:

      >>> import datetime as dt
      >>> dt.date(2002, 12, 4).ctime()
      'Wed Dec  4 00:00:00 2002'

   "d.ctime()" es equivalente a:

      time.ctime(time.mktime(d.timetuple()))

   en plataformas donde la función nativa C "ctime()" (donde
   "time.ctime()" llama, pero que "date.ctime()" no se llama) se
   ajusta al estándar C.

date.strftime(format)

   Return a string representing the date, controlled by an explicit
   format string. Format codes referring to hours, minutes or seconds
   will see 0 values. See also strftime() and strptime() behavior and
   "date.isoformat()".

date.__format__(format)

   Same as "date.strftime()". This makes it possible to specify a
   format string for a "date" object in formatted string literals and
   when using "str.format()". See also strftime() and strptime()
   behavior and "date.isoformat()".

### Examples of usage: "date"

Ejemplo de contar días para un evento:

   >>> import time
   >>> import datetime as dt
   >>> today = dt.date.today()
   >>> today
   datetime.date(2007, 12, 5)
   >>> today == dt.date.fromtimestamp(time.time())
   True
   >>> my_birthday = dt.date(today.year, 6, 24)
   >>> if my_birthday < today:
   ...     my_birthday = my_birthday.replace(year=today.year + 1)
   ...
   >>> my_birthday
   datetime.date(2008, 6, 24)
   >>> time_to_birthday = abs(my_birthday - today)
   >>> time_to_birthday.days
   202

Más ejemplos de trabajo con "date":

   >>> import datetime as dt
   >>> d = dt.date.fromordinal(730920) # 730920th day after 1. 1. 0001
   >>> d
   datetime.date(2002, 3, 11)

   >>> # Methods related to formatting string output
   >>> d.isoformat()
   '2002-03-11'
   >>> d.strftime("%d/%m/%y")
   '11/03/02'
   >>> d.strftime("%A %d. %B %Y")
   'Monday 11. March 2002'
   >>> d.ctime()
   'Mon Mar 11 00:00:00 2002'
   >>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
   'The day is 11, the month is March.'

   >>> # Methods for extracting 'components' under different calendars
   >>> t = d.timetuple()
   >>> for i in t:
   ...     print(i)
   2002                # year
   3                   # month
   11                  # day
   0
   0
   0
   0                   # weekday (0 = Monday)
   70                  # 70th day in the year
   -1
   >>> ic = d.isocalendar()
   >>> for i in ic:
   ...     print(i)
   2002                # ISO year
   11                  # ISO week number
   1                   # ISO day number ( 1 = Monday )

   >>> # A date object is immutable; all operations produce a new object
   >>> d.replace(year=2005)
   datetime.date(2005, 3, 11)

## "datetime" objects

El objeto "datetime" es un único objeto que contiene toda la
información de un objeto "date" y un objeto "time".

Like a "date" object, "datetime" assumes the current Gregorian
calendar extended in both directions; like a "time" object, "datetime"
assumes there are exactly 3600*24 seconds in every day.

Constructor:

class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

   Se requieren los argumentos *year*, *month* y *day*. *tzinfo* puede
   ser "None", o una instancia de una subclase "tzinfo". Los
   argumentos restantes deben ser enteros en los siguientes rangos:

   * "MINYEAR <= year <= MAXYEAR",

   * "1 <= month <= 12",

   * "1 <= day <= number of days in the given month and year",

   * "0 <= hour < 24",

   * "0 <= minute < 60",

   * "0 <= second < 60",

   * "0 <= microsecond < 1000000",

   * "fold in [0, 1]".

   Si se proporciona un argumento fuera de esos rangos, "ValueError"
   se genera.

   Distinto en la versión 3.6: Added the *fold* parameter.

Otros constructores, todos los métodos de clase:

classmethod datetime.today()

   Return the current local date and time, with "tzinfo" "None".

   Equivalente a:

      datetime.fromtimestamp(time.time())

   Ver también "now()", "fromtimestamp()".

   Este método es funciona como "now()", pero sin un parámetro "tz".

classmethod datetime.now(tz=None)

   Retorna la fecha y hora local actual.

   Si el argumento opcional *tz* es "None" o no se especifica, es como
   "today()", pero, si es posible, proporciona más precisión de la que
   se puede obtener al pasar por "time.time()" marca de tiempo (por
   ejemplo, esto puede ser posible en plataformas que suministran la
   función C "gettimeofday()").

   Si *tz* no es "None", debe ser una instancia de una subclase
   "tzinfo", y la fecha y hora actuales se convierten en la zona
   horaria de *tz*.

   Esta función es preferible a "today()" y "utcnow()".

   Nota:

     Subsequent calls to "datetime.now()" may return the same instant
     depending on the precision of the underlying clock.

classmethod datetime.utcnow()

   Retorna la fecha y hora UTC actual, con "tzinfo" "None".

   Esto es como "now()", pero retorna la fecha y hora UTC actual, como
   un objeto naíf (*naive*): "datetime". Se puede obtener una fecha y
   hora UTC actual consciente (*aware*) llamando a "datetime.now
   (timezone.utc)". Ver también "now()".

   Advertencia:

     Debido a que los objetos naífs (*naive*) de "datetime" son
     tratados por muchos métodos de "datetime" como horas locales, se
     prefiere usar fechas y horas conscientes(*aware*) para
     representar las horas en UTC. Como tal, la forma recomendada de
     crear un objeto que represente la hora actual en UTC es llamando
     a "datetime.now(timezone.utc)".

   Obsoleto desde la versión 3.12: Use "datetime.now()" with "UTC"
   instead.

classmethod datetime.fromtimestamp(timestamp, tz=None)

   Retorna la fecha y hora local correspondiente a la marca de tiempo
   POSIX, tal como la retorna "time.time()". Si el argumento opcional
   *tz* es "None" o no se especifica, la marca de tiempo se convierte
   a la fecha y hora local de la plataforma, y el objeto retornado
   "datetime" es naíf (*naive*).

   Si *tz* no es "None", debe ser una instancia de una subclase
   "tzinfo", y la fecha y hora actuales se convierten en la zona
   horaria de *tz*.

   "fromtimestamp()" puede aumentar "OverflowError", si la marca de
   tiempo está fuera del rango de valores admitidos por la plataforma
   *C* "localtime()" o "gmtime()", y "OSError" en "localtime()" o
   "gmtime()" falla. Es común que esto se restrinja a los años 1970 a
   2038. Tenga en cuenta que en los sistemas que no son POSIX que
   incluyen segundos bisiestos en su noción de marca de tiempo, los
   segundos bisiestos son ignorados por "fromtimestamp()", y luego es
   posible tener dos marcas de tiempo que difieren en un segundo que
   producen objetos idénticos "datetime". Se prefiere este método
   sobre "utcfromtimestamp()".

   Distinto en la versión 3.3: Se genera "OverflowError" en lugar de
   "ValueError" si la marca de tiempo está fuera del rango de valores
   admitidos por la plataforma *C* "localtime()" o "gmtime()". genera
   "OSError" en lugar de la función "ValueError" en "localtime()" o
   error "gmtime()".

   Distinto en la versión 3.6: "fromtimestamp()" puede retornar
   instancias con "fold" establecido en 1.

classmethod datetime.utcfromtimestamp(timestamp)

   Retorna el UTC "datetime" correspondiente a la marca de tiempo
   POSIX, con "tzinfo" "None". (El objeto resultante es naíf
   (*naive*).)

   Esto puede generar "OverflowError", si la marca de tiempo está
   fuera del rango de valores admitidos por la plataforma C
   "gmtime()", y error en "OSError" en "gmtime()". Es común que esto
   se restrinja a los años entre1970 a 2038.

   Para conocer un objeto "datetime", llama a "fromtimestamp()":

      datetime.fromtimestamp(timestamp, timezone.utc)

   En las plataformas compatibles con POSIX, es equivalente a la
   siguiente expresión:

      datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp)

   excepto que la última fórmula siempre admite el rango de años
   completo: entre "MINYEAR" y "MAXYEAR" inclusive.

   Advertencia:

     Debido a que los objetos naíf (*naive*) de "datetime" son
     tratados por muchos métodos de "datetime" como horas locales, se
     prefiere usar fechas y horas conscientes para representar las
     horas en UTC. Como tal, la forma recomendada de crear un objeto
     que represente una marca de tiempo específica en UTC es llamando
     a "datetime.fromtimestamp(timestamp, tz=timezone.utc)".

   Distinto en la versión 3.3: Se genera "OverflowError" en lugar de
   "ValueError" si la marca de tiempo está fuera del rango de valores
   admitidos por la plataforma *C* "gmtime()". genera "OSError" en
   lugar de "ValueError" en el error de "gmtime()".

   Distinto en la versión 3.15: Accepts any real number as
   *timestamp*, not only integer or float.

   Obsoleto desde la versión 3.12: Use "datetime.fromtimestamp()" with
   "UTC" instead.

classmethod datetime.fromordinal(ordinal)

   Se genera "datetime" correspondiente al ordinal del proléptico
   gregoriano, donde el 1 de enero del año 1 tiene ordinal 1.
   "ValueError" se genera a menos que "1 <= ordinal <=
   datetime.max.toordinal()". La hora, minuto, segundo y microsegundo
   del resultado son todos 0, y "tzinfo" es "None".

classmethod datetime.combine(date, time, tzinfo=time.tzinfo)

   Return a new "datetime" object whose date components are equal to
   the given "date" object's, and whose time components are equal to
   the given "time" object's. If the *tzinfo* argument is provided,
   its value is used to set the "tzinfo" attribute of the result,
   otherwise the "tzinfo" attribute of the *time* argument is used.
   If the *date* argument is a "datetime" object, its time components
   and "tzinfo" attributes are ignored.

   For any "datetime" object "d", "d == datetime.combine(d.date(),
   d.time(), d.tzinfo)".

   Distinto en la versión 3.6: Se agregó el argumento *tzinfo*.

classmethod datetime.fromisoformat(date_string)

   Devuelve un "datetime" correspondiente a un *date_string* en
   cualquier formato ISO 8601 válido, con las siguientes excepciones:

   1. Las compensaciones de zona horaria pueden tener fracciones de
      segundo.

   2. El separador "T" se puede reemplazar por cualquier carácter
      Unicode único.

   3. No se admiten fracciones de horas y minutos.

   4. Reduced precision dates are not currently supported ("YYYY-MM",
      "YYYY").

   5. Extended date representations are not currently supported
      ("±YYYYYY-MM-DD").

   6. Ordinal dates are not currently supported ("YYYY-OOO").

   Ejemplos:

      >>> import datetime as dt
      >>> dt.datetime.fromisoformat('2011-11-04')
      datetime.datetime(2011, 11, 4, 0, 0)
      >>> dt.datetime.fromisoformat('20111104')
      datetime.datetime(2011, 11, 4, 0, 0)
      >>> dt.datetime.fromisoformat('2011-11-04T00:05:23')
      datetime.datetime(2011, 11, 4, 0, 5, 23)
      >>> dt.datetime.fromisoformat('2011-11-04T00:05:23Z')
      datetime.datetime(2011, 11, 4, 0, 5, 23, tzinfo=datetime.timezone.utc)
      >>> dt.datetime.fromisoformat('20111104T000523')
      datetime.datetime(2011, 11, 4, 0, 5, 23)
      >>> dt.datetime.fromisoformat('2011-W01-2T00:05:23.283')
      datetime.datetime(2011, 1, 4, 0, 5, 23, 283000)
      >>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283')
      datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
      >>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
      datetime.datetime(2011, 11, 4, 0, 5, 23, 283000, tzinfo=datetime.timezone.utc)
      >>> dt.datetime.fromisoformat('2011-11-04T00:05:23+04:00')
      datetime.datetime(2011, 11, 4, 0, 5, 23,
          tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))

   Added in version 3.7.

   Distinto en la versión 3.11: Previously, this method only supported
   formats that could be emitted by "date.isoformat()" or
   "datetime.isoformat()".

classmethod datetime.fromisocalendar(year, week, day)

   Return a "datetime" corresponding to the ISO calendar date
   specified by *year*, *week* and *day*. The non-date components of
   the datetime are populated with their normal default values. This
   is the inverse of the function "datetime.isocalendar()".

   Added in version 3.8.

classmethod datetime.strptime(date_string, format)

   Retorna "datetime" correspondiente a *date_string*, analizado según
   *format*.

   If *format* does not contain microseconds or time zone information,
   this is equivalent to:

      datetime(*(time.strptime(date_string, format)[0:6]))

   "ValueError" is raised if the date_string and format can't be
   parsed by "time.strptime()" or if it returns a value which isn't a
   time tuple.  See also strftime() and strptime() behavior and
   "datetime.fromisoformat()".

   Distinto en la versión 3.13: If *format* specifies a day of month
   without a year a "DeprecationWarning" is now emitted.  This is to
   avoid a quadrennial leap year bug in code seeking to parse only a
   month and day as the default year used in absence of one in the
   format is not a leap year. Such *format* values may raise an error
   as of Python 3.15.  The workaround is to always include a year in
   your *format*.  If parsing *date_string* values that do not have a
   year, explicitly add a year that is a leap year before parsing:

      >>> import datetime as dt
      >>> date_string = "02/29"
      >>> when = dt.datetime.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
      >>> when.strftime("%B %d")
      'February 29'

Atributos de clase:

datetime.min

   La primera fecha representable "datetime", "datetime(MINYEAR, 1, 1,
   tzinfo=None)".

datetime.max

   La última fecha representable "datetime", "datetime(MAXYEAR, 12,
   31, 23, 59, 59, 999999, tzinfo=None)".

datetime.resolution

   La diferencia más pequeña posible entre objetos no iguales
   "datetime", "timedelta(microseconds=1)".

Atributos de instancia (solo lectura):

datetime.year

   Entre "MINYEAR" y "MAXYEAR" inclusive.

datetime.month

   Entre 1 y 12 inclusive.

datetime.day

   Entre 1 y el número de días en el mes dado del año dado.

datetime.hour

   En "range(24)".

datetime.minute

   En "range(60)".

datetime.second

   En "range(60)".

datetime.microsecond

   En "range(1000000)".

datetime.tzinfo

   El objeto pasó como argumento *tzinfo* al constructor "datetime", o
   "None" si no se pasó ninguno.

datetime.fold

   In "[0, 1]". Used to disambiguate wall times during a repeated
   interval. (A repeated interval occurs when clocks are rolled back
   at the end of daylight saving time or when the UTC offset for the
   current zone is decreased for political reasons.) The values 0 and
   1 represent, respectively, the earlier and later of the two moments
   with the same wall time representation.

   Added in version 3.6.

Operaciones soportadas:

+-----------------------------------------+----------------------------------+
| Operación                               | Resultado                        |
|=========================================|==================================|
## | "datetime2 = datetime1 + timedelta"     | (1)                              |

## | "datetime2 = datetime1 - timedelta"     | (2)                              |

## | "timedelta = datetime1 - datetime2"     | (3)                              |

| "datetime1 == datetime2" "datetime1 !=  | Equality comparison. (4)         |
## | datetime2"                              |                                  |

| "datetime1 < datetime2" "datetime1 >    | Order comparison. (5)            |
| datetime2" "datetime1 <= datetime2"     |                                  |
## | "datetime1 >= datetime2"                |                                  |

1. "datetime2" is a duration of "timedelta" removed from "datetime1",
   moving forward in time if "timedelta.days > 0", or backward if
   "timedelta.days < 0". The result has the same "tzinfo" attribute as
   the input datetime, and "datetime2 - datetime1 == timedelta" after.
   "OverflowError" is raised if "datetime2.year" would be smaller than
   "MINYEAR" or larger than "MAXYEAR". Note that no time zone
   adjustments are done even if the input is an aware object.

2. Computes the "datetime2" such that "datetime2 + timedelta ==
   datetime1". As for addition, the result has the same "tzinfo"
   attribute as the input datetime, and no time zone adjustments are
   done even if the input is aware.

3. Subtraction of a "datetime" from a "datetime" is defined only if
   both operands are naive, or if both are aware. If one is aware and
   the other is naive, "TypeError" is raised.

   If both are naive, or both are aware and have the same "tzinfo"
   attribute, the "tzinfo" attributes are ignored, and the result is a
   "timedelta" object "t" such that "datetime2 + t == datetime1". No
   time zone adjustments are done in this case.

   If both are aware and have different "tzinfo" attributes, "a-b"
   acts as if "a" and "b" were first converted to naive UTC datetimes.
   The result is "(a.replace(tzinfo=None) - a.utcoffset()) -
   (b.replace(tzinfo=None) - b.utcoffset())" except that the
   implementation never overflows.

4. "datetime" objects are equal if they represent the same date and
   time, taking into account the time zone.

   Naive and aware "datetime" objects are never equal.

   If both comparands are aware, and have the same "tzinfo" attribute,
   the "tzinfo" and "fold" attributes are ignored and the base
   datetimes are compared. If both comparands are aware and have
   different "tzinfo" attributes, the comparison acts as comparands
   were first converted to UTC datetimes except that the
   implementation never overflows. "datetime" instances in a repeated
   interval are never equal to "datetime" instances in other time
   zone.

5. *datetime1* is considered less than *datetime2* when *datetime1*
   precedes *datetime2* in time, taking into account the time zone.

   Order comparison between naive and aware "datetime" objects raises
   "TypeError".

   If both comparands are aware, and have the same "tzinfo" attribute,
   the "tzinfo" and "fold" attributes are ignored and the base
   datetimes are compared. If both comparands are aware and have
   different "tzinfo" attributes, the comparison acts as comparands
   were first converted to UTC datetimes except that the
   implementation never overflows.

Distinto en la versión 3.3: Las comparaciones de igualdad entre las
instancias conscientes (*aware*) y naíf (*naive*) "datetime" no
generan "TypeError".

Distinto en la versión 3.13: Comparison between "datetime" object and
an instance of the "date" subclass that is not a "datetime" subclass
no longer converts the latter to "date", ignoring the time part and
the time zone. The default behavior can be changed by overriding the
special comparison methods in subclasses.

Métodos de instancia:

datetime.date()

   Retorna el objeto "date" con el mismo año, mes y día.

datetime.time()

   Retorna el objeto "time" con la misma hora, minuto, segundo,
   microsegundo y doblado(*fold*). "tzinfo" es "None". Ver también
   método "timetz()".

   Distinto en la versión 3.6: El valor de plegado (*fold value*) se
   copia en el objeto "time" retornado.

datetime.timetz()

   Retorna el objeto "time" con los mismos atributos de hora, minuto,
   segundo, microsegundo, pliegue y *tzinfo*. Ver también método
   "time()".

   Distinto en la versión 3.6: El valor de plegado (*fold value*) se
   copia en el objeto "time" retornado.

datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

   Return a new "datetime" object with the same attributes, but with
   specified parameters updated. Note that "tzinfo=None" can be
   specified to create a naive datetime from an aware datetime with no
   conversion of date and time data.

   "datetime" objects are also supported by generic function
   "copy.replace()".

   Distinto en la versión 3.6: Added the *fold* parameter.

datetime.astimezone(tz=None)

   Retorna un objeto "datetime" con el atributo nuevo "tzinfo" *tz*,
   ajustando los datos de fecha y hora para que el resultado sea la
   misma hora UTC que *self*, pero en hora local *tz*.

   If provided, *tz* must be an instance of a "tzinfo" subclass, and
   its "utcoffset()" and "dst()" methods must not return "None". If
   *self* is naive, it is presumed to represent time in the system
   time zone.

   If called without arguments (or with "tz=None") the system local
   time zone is assumed for the target time zone. The ".tzinfo"
   attribute of the converted datetime instance will be set to an
   instance of "timezone" with the zone name and offset obtained from
   the OS.

   If "self.tzinfo" is *tz*, "self.astimezone(tz)" is equal to *self*:
   no adjustment of date or time data is performed. Else the result is
   local time in the time zone *tz*, representing the same UTC time as
   *self*:  after "astz = dt.astimezone(tz)", "astz -
   astz.utcoffset()" will have the same date and time data as "dt -
   dt.utcoffset()".

   If you merely want to attach a "timezone" object *tz* to a datetime
   *dt* without adjustment of date and time data, use
   "dt.replace(tzinfo=tz)". If you merely want to remove the
   "timezone" object from an aware datetime *dt* without conversion of
   date and time data, use "dt.replace(tzinfo=None)".

   Tenga en cuenta que el método predeterminado "tzinfo.fromutc()" se
   puede reemplazar en una subclase "tzinfo" para afectar el resultado
   retornado por "astimezone()". "astimezone()" ignora los casos de
   error, actúa como:

      def astimezone(self, tz):
          if self.tzinfo is tz:
              return self
          # Convert self to UTC, and attach the new timezone object.
          utc = (self - self.utcoffset()).replace(tzinfo=tz)
          # Convert from UTC to tz's local time.
          return tz.fromutc(utc)

   Distinto en la versión 3.3: *tz* ahora puede ser omitido.

   Distinto en la versión 3.6: El método "astimezone()" ahora se puede
   invocar en instancias naíf (*naive*) que se supone representan la
   hora local del sistema.

datetime.utcoffset()

   Si "tzinfo" es "None", retorna "None", de lo contrario retorna
   "self.tzinfo.utcoffset (self)", y genera una excepción si este
   último no retorna "None" o un objeto "timedelta" con magnitud
   inferior a un día.

   Distinto en la versión 3.7: El desfase UTC no está restringido a un
   número entero de minutos.

datetime.dst()

   Si "tzinfo" es "None", retorna "None", de lo contrario retorna
   "self.tzinfo.utcoffset (self)", y genera una excepción si este
   último no retorna "None" o un objeto "timedelta" con magnitud
   inferior a un día.

   Distinto en la versión 3.7: El desfase DST no está restringido a un
   número entero de minutos.

datetime.tzname()

   Si "tzinfo" es "None", retorna "None", de lo contrario retorna
   "self.tzinfo.tzname(self)", genera una excepción si este último no
   retorna "None" o un objeto de cadena de caracteres,

datetime.timetuple()

   Retorna una "time.struct_time" como la que retorna
   "time.localtime()".

   "d.timetuple()" es equivalente a:

      time.struct_time((d.year, d.month, d.day,
                        d.hour, d.minute, d.second,
                        d.weekday(), yday, dst))

   where "yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1"
   is the day number within the current year starting with 1 for
   January 1st. The "tm_isdst" flag of the result is set according to
   the "dst()" method: "tzinfo" is "None" or "dst()" returns "None",
   "tm_isdst" is set to "-1"; else if "dst()" returns a non-zero
   value, "tm_isdst" is set to 1; else "tm_isdst" is set to 0.

datetime.utctimetuple()

   If "datetime" instance "d" is naive, this is the same as
   "d.timetuple()" except that "tm_isdst" is forced to 0 regardless of
   what "d.dst()" returns. DST is never in effect for a UTC time.

   If "d" is aware, "d" is normalized to UTC time, by subtracting
   "d.utcoffset()", and a "time.struct_time" for the normalized time
   is returned. "tm_isdst" is forced to 0. Note that an
   "OverflowError" may be raised if "d.year" was "MINYEAR" or
   "MAXYEAR" and UTC adjustment spills over a year boundary.

   Advertencia:

     Because naive "datetime" objects are treated by many "datetime"
     methods as local times, it is preferred to use aware datetimes to
     represent times in UTC; as a result, using
     "datetime.utctimetuple()" may give misleading results. If you
     have a naive "datetime" representing UTC, use
     "datetime.replace(tzinfo=timezone.utc)" to make it aware, at
     which point you can use "datetime.timetuple()".

datetime.toordinal()

   Retorna el ordinal gregoriano proléptico de la fecha. Lo mismo que
   "self.date().toordinal()".

datetime.timestamp()

   Retorna la marca de tiempo (*timestamp*) POSIX correspondiente a la
   instancia "datetime". El valor de retorno es "float" similar al
   retornado por "time.time()".

   Naive "datetime" instances are assumed to represent local time and
   this method relies on the platform C "mktime()" function to perform
   the conversion. Since "datetime" supports wider range of values
   than "mktime()" on many platforms, this method may raise
   "OverflowError" or "OSError" for times far in the past or far in
   the future.

   Para las instancias de "datetime", el valor de retorno se calcula
   como:

      (dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()

   Nota:

     There is no method to obtain the POSIX timestamp directly from a
     naive "datetime" instance representing UTC time. If your
     application uses this convention and your system time zone is not
     set to UTC, you can obtain the POSIX timestamp by supplying
     "tzinfo=timezone.utc":

        timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

     o calculando la marca de tiempo (*timestamp*) directamente:

        timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)

   Added in version 3.3.

   Distinto en la versión 3.6: El método "timestamp()" utiliza el
   atributo "fold" para desambiguar los tiempos durante un intervalo
   repetido.

datetime.weekday()

   Retorna el día de la semana como un entero, donde el lunes es 0 y
   el domingo es 6. Lo mismo que "self.date().weekday()". Ver también
   "isoweekday()".

datetime.isoweekday()

   Retorna el día de la semana como un número entero, donde el lunes
   es 1 y el domingo es 7. Lo mismo que "self.date().isoweekday()".
   Ver también "weekday()", "isocalendar()".

datetime.isocalendar()

   Retorna una  *named tuple* con tres componentes: "year", "week", y
   "weekday". Lo mismo que "self.date().isocalendar()".

datetime.isoformat(sep='T', timespec='auto')

   Retorna una cadena de caracteres representando la fecha y la hora
   en formato ISO 8601:

   * "YYYY-MM-DDTHH:MM:SS.ffffff", si "microsecond" no es 0

   * "YYYY-MM-DDTHH:MM:SS", si "microsecond" es 0

   Si "utcoffset()" no retorna "None", se agrega una cadena de
   caracteres dando el desplazamiento UTC:

   * "YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]", si
     "microsecond" no es 0

   * "YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]]", si "microsecond" es 0

   Ejemplos:

      >>> import datetime as dt
      >>> dt.datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()
      '2019-05-18T15:17:08.132263'
      >>> dt.datetime(2019, 5, 18, 15, 17, tzinfo=dt.timezone.utc).isoformat()
      '2019-05-18T15:17:00+00:00'

   El argumento opcional *sep* (default "’T’") es un separador de un
   carácter, ubicado entre las porciones de fecha y hora del
   resultado. Por ejemplo:

      >>> import datetime as dt
      >>> class TZ(dt.tzinfo):
      ...     """A time zone with an arbitrary, constant -06:39 offset."""
      ...     def utcoffset(self, when):
      ...         return dt.timedelta(hours=-6, minutes=-39)
      ...
      >>> dt.datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
      '2002-12-25 00:00:00-06:39'
      >>> dt.datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat()
      '2009-11-27T00:00:00.000100-06:39'

   El argumento opcional *timespec* especifica el número de
   componentes adicionales del tiempo a incluir (el valor
   predeterminado es "‘auto’"). Puede ser uno de los siguientes:

   * "’auto’": Igual que "’seconds’" si "microsecond" es 0, igual que
     "’microseconds’" de lo contrario.

   * "’hours’": incluye el "hour" en el formato de dos dígitos "HH".

   * "’minutes’": Incluye "hour" y "minute" en formato "HH:MM".

   * "’seconds’": Incluye "hour", "minute", y "second" en formato
     "HH:MM:SS".

   * "’milliseconds’": Incluye tiempo completo, pero trunca la segunda
     parte fraccionaria a milisegundos. Formato "HH:MM:SS.sss".

   * "’microseconds’": Incluye tiempo completo en formato
     "HH:MM:SS.ffffff".

   Nota:

     Los componentes de tiempo excluidos están truncados, no
     redondeados.

   "ValueError" lanzará un argumento inválido *timespec*:

      >>> import datetime as dt
      >>> dt.datetime.now().isoformat(timespec='minutes')
      '2002-12-25T00:00'
      >>> my_datetime = dt.datetime(2015, 1, 1, 12, 30, 59, 0)
      >>> my_datetime.isoformat(timespec='microseconds')
      '2015-01-01T12:30:59.000000'

   Distinto en la versión 3.6: Added the *timespec* parameter.

datetime.__str__()

   For a "datetime" instance "d", "str(d)" is equivalent to
   "d.isoformat(' ')".

datetime.ctime()

   Retorna una cadena de caracteres que representa la fecha y la hora:

      >>> import datetime as dt
      >>> dt.datetime(2002, 12, 4, 20, 30, 40).ctime()
      'Wed Dec  4 20:30:40 2002'

   La cadena de salida *no* incluirá información de zona horaria,
   independientemente de si la entrada es consciente (*aware*) o naíf
   (*naive*).

   "d.ctime()" es equivalente a:

      time.ctime(time.mktime(d.timetuple()))

   en plataformas donde la función nativa C "ctime()" (que
   "time.ctime()" invoca, pero que "datetime.ctime()" no invoca) se
   ajusta al estándar *C*.

datetime.strftime(format)

   Return a string representing the date and time, controlled by an
   explicit format string. See also strftime() and strptime() behavior
   and "datetime.isoformat()".

datetime.__format__(format)

   Same as "datetime.strftime()". This makes it possible to specify a
   format string for a "datetime" object in formatted string literals
   and when using "str.format()". See also strftime() and strptime()
   behavior and "datetime.isoformat()".

### Examples of usage: "datetime"

Examples of working with "datetime" objects:

   >>> import datetime as dt

   >>> # Using datetime.combine()
   >>> d = dt.date(2005, 7, 14)
   >>> t = dt.time(12, 30)
   >>> dt.datetime.combine(d, t)
   datetime.datetime(2005, 7, 14, 12, 30)

   >>> # Using datetime.now()
   >>> dt.datetime.now()
   datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
   >>> dt.datetime.now(dt.timezone.utc)
   datetime.datetime(2007, 12, 6, 15, 29, 43, 79060, tzinfo=datetime.timezone.utc)

   >>> # Using datetime.strptime()
   >>> my_datetime = dt.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
   >>> my_datetime
   datetime.datetime(2006, 11, 21, 16, 30)

   >>> # Using datetime.timetuple() to get tuple of all attributes
   >>> tt = my_datetime.timetuple()
   >>> for it in tt:
   ...     print(it)
   ...
   2006    # year
   11      # month
   21      # day
   16      # hour
   30      # minute
   0       # second
   1       # weekday (0 = Monday)
   325     # number of days since 1st January
   -1      # dst - method tzinfo.dst() returned None

   >>> # Date in ISO format
   >>> ic = my_datetime.isocalendar()
   >>> for it in ic:
   ...     print(it)
   ...
   2006    # ISO year
   47      # ISO week
   2       # ISO weekday

   >>> # Formatting a datetime
   >>> my_datetime.strftime("%A, %d. %B %Y %I:%M%p")
   'Tuesday, 21. November 2006 04:30PM'
   >>> 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(my_datetime, "day", "month", "time")
   'The day is 21, the month is November, the time is 04:30PM.'

El siguiente ejemplo define una subclase "tzinfo" que captura la
información de zona horaria de *Kabul*, Afganistán, que utilizó +4 UTC
hasta 1945 y +4:30 UTC a partir de entonces:

   import datetime as dt

   class KabulTz(dt.tzinfo):
       # Kabul used +4 until 1945, when they moved to +4:30
       UTC_MOVE_DATE = dt.datetime(1944, 12, 31, 20, tzinfo=dt.timezone.utc)

       def utcoffset(self, when):
           if when.year < 1945:
               return dt.timedelta(hours=4)
           elif (1945, 1, 1, 0, 0) <= when.timetuple()[:5] < (1945, 1, 1, 0, 30):
               # An ambiguous ("imaginary") half-hour range representing
               # a 'fold' in time due to the shift from +4 to +4:30.
               # If when falls in the imaginary range, use fold to decide how
               # to resolve. See PEP 495.
               return dt.timedelta(hours=4, minutes=(30 if when.fold else 0))
           else:
               return dt.timedelta(hours=4, minutes=30)

       def fromutc(self, when):
           # Follow same validations as in datetime.tzinfo
           if not isinstance(when, dt.datetime):
               raise TypeError("fromutc() requires a datetime argument")
           if when.tzinfo is not self:
               raise ValueError("when.tzinfo is not self")

           # A custom implementation is required for fromutc as
           # the input to this function is a datetime with utc values
           # but with a tzinfo set to self.
           # See datetime.astimezone or fromtimestamp.
           if when.replace(tzinfo=dt.timezone.utc) >= self.UTC_MOVE_DATE:
               return when + dt.timedelta(hours=4, minutes=30)
           else:
               return when + dt.timedelta(hours=4)

       def dst(self, when):
           # Kabul does not observe daylight saving time.
           return dt.timedelta(0)

       def tzname(self, when):
           if when >= self.UTC_MOVE_DATE:
               return "+04:30"
           return "+04"

Uso de "KabulTz" desde arriba

   >>> tz1 = KabulTz()

   >>> # Datetime before the change
   >>> dt1 = dt.datetime(1900, 11, 21, 16, 30, tzinfo=tz1)
   >>> print(dt1.utcoffset())
   4:00:00

   >>> # Datetime after the change
   >>> dt2 = dt.datetime(2006, 6, 14, 13, 0, tzinfo=tz1)
   >>> print(dt2.utcoffset())
   4:30:00

   >>> # Convert datetime to another time zone
   >>> dt3 = dt2.astimezone(dt.timezone.utc)
   >>> dt3
   datetime.datetime(2006, 6, 14, 8, 30, tzinfo=datetime.timezone.utc)
   >>> dt2
   datetime.datetime(2006, 6, 14, 13, 0, tzinfo=KabulTz())
   >>> dt2 == dt3
   True

## "time" objects

A "time" object represents a (local) time of day, independent of any
particular day, and subject to adjustment via a "tzinfo" object.

class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

   Todos los argumentos son opcionales. *tzinfo* puede ser "None", o
   una instancia de una subclase "tzinfo". Los argumentos restantes
   deben ser enteros en los siguientes rangos:

   * "0 <= hour < 24",

   * "0 <= minute < 60",

   * "0 <= second < 60",

   * "0 <= microsecond < 1000000",

   * "fold in [0, 1]".

   If an argument outside those ranges is given, "ValueError" is
   raised. All default to 0 except *tzinfo*, which defaults to "None".

Atributos de clase:

time.min

   El primero representable "time",``time (0, 0, 0, 0)``.

time.max

   El último representable "time", "time(23, 59, 59, 999999)".

time.resolution

   La diferencia más pequeña posible entre los objetos no iguales
   "time", "timedelta(microseconds=1)", aunque tenga en cuenta que la
   aritmética en objetos "time" no es compatible.

Atributos de instancia (solo lectura):

time.hour

   En "range(24)".

time.minute

   En "range(60)".

time.second

   En "range(60)".

time.microsecond

   En "range(1000000)".

time.tzinfo

   El objeto pasado como argumento *tzinfo* al constructor de la clase
   "time" , o "None" si no se pasó ninguno.

time.fold

   In "[0, 1]". Used to disambiguate wall times during a repeated
   interval. (A repeated interval occurs when clocks are rolled back
   at the end of daylight saving time or when the UTC offset for the
   current zone is decreased for political reasons.) The values 0 and
   1 represent, respectively, the earlier and later of the two moments
   with the same wall time representation.

   Added in version 3.6.

"time" objects support equality and order comparisons, where "a" is
considered less than "b" when "a" precedes "b" in time.

Naive and aware "time" objects are never equal. Order comparison
between naive and aware "time" objects raises "TypeError".

If both comparands are aware, and have the same "tzinfo" attribute,
the "tzinfo" and "fold" attributes are ignored and the base times are
compared. If both comparands are aware and have different "tzinfo"
attributes, the comparands are first adjusted by subtracting their UTC
offsets (obtained from "self.utcoffset()").

Distinto en la versión 3.3: Equality comparisons between aware and
naive "time" instances don't raise "TypeError".

En contextos booleanos, un objeto "time" siempre se considera
verdadero.

Distinto en la versión 3.5: Before Python 3.5, a "time" object was
considered to be false if it represented midnight in UTC. This
behavior was considered obscure and error-prone and has been removed
in Python 3.5. See bpo-13936 for more information.

Other constructors:

classmethod time.fromisoformat(time_string)

   Devuelve un "time" correspondiente a un *time_string* en cualquier
   formato ISO 8601 válido, con las siguientes excepciones:

   1. Las compensaciones de zona horaria pueden tener fracciones de
      segundo.

   2. No se requiere el "T" inicial, que normalmente se requiere en
      los casos en que puede haber ambigüedad entre una fecha y una
      hora.

   3. Las fracciones de segundo pueden tener cualquier número de
      dígitos (cualquier número más allá de 6 será truncado).

   4. No se admiten fracciones de horas y minutos.

   Examples:

      >>> import datetime as dt
      >>> dt.time.fromisoformat('04:23:01')
      datetime.time(4, 23, 1)
      >>> dt.time.fromisoformat('T04:23:01')
      datetime.time(4, 23, 1)
      >>> dt.time.fromisoformat('T042301')
      datetime.time(4, 23, 1)
      >>> dt.time.fromisoformat('04:23:01.000384')
      datetime.time(4, 23, 1, 384)
      >>> dt.time.fromisoformat('04:23:01,000384')
      datetime.time(4, 23, 1, 384)
      >>> dt.time.fromisoformat('04:23:01+04:00')
      datetime.time(4, 23, 1, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))
      >>> dt.time.fromisoformat('04:23:01Z')
      datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)
      >>> dt.time.fromisoformat('04:23:01+00:00')
      datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)

   Added in version 3.7.

   Distinto en la versión 3.11: Previously, this method only supported
   formats that could be emitted by "time.isoformat()".

classmethod time.strptime(date_string, format)

   Return a "time" corresponding to *date_string*, parsed according to
   *format*.

   If *format* does not contain microseconds or timezone information,
   this is equivalent to:

      time(*(time.strptime(date_string, format)[3:6]))

   "ValueError" is raised if the *date_string* and *format* cannot be
   parsed by "time.strptime()" or if it returns a value which is not a
   time tuple.  See also strftime() and strptime() behavior and
   "time.fromisoformat()".

   Added in version 3.14.

Métodos de instancia:

time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

   Return a new "time" with the same values, but with specified
   parameters updated. Note that "tzinfo=None" can be specified to
   create a naive "time" from an aware "time", without conversion of
   the time data.

   "time" objects are also supported by generic function
   "copy.replace()".

   Distinto en la versión 3.6: Added the *fold* parameter.

time.isoformat(timespec='auto')

   Retorna una cadena que representa la hora en formato ISO 8601, una
   de:

   * "HH:MM:SS.ffffff", si "microsecond" no es 0

   * "HH:MM:SS", si "microsecond" es 0

   * "HH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]", si "utcoffset()" no
     retorna "None"

   * "HH:MM:SS+HH:MM[:SS[.ffffff]]", si "microsecond" es 0 y
     "utcoffset()" no retorna "None"

   El argumento opcional *timespec* especifica el número de
   componentes adicionales del tiempo a incluir (el valor
   predeterminado es "‘auto’"). Puede ser uno de los siguientes:

   * "’auto’": Igual que "’seconds’" si "microsecond" es 0, igual que
     "’microseconds’" de lo contrario.

   * "’hours’": incluye el "hour" en el formato de dos dígitos "HH".

   * "’minutes’": Incluye "hour" y "minute" en formato "HH:MM".

   * "’seconds’": Incluye "hour", "minute", y "second" en formato
     "HH:MM:SS".

   * "’milliseconds’": Incluye tiempo completo, pero trunca la segunda
     parte fraccionaria a milisegundos. Formato "HH:MM:SS.sss".

   * "’microseconds’": Incluye tiempo completo en formato
     "HH:MM:SS.ffffff".

   Nota:

     Los componentes de tiempo excluidos están truncados, no
     redondeados.

   "ValueError" lanzará un argumento inválido *timespec*.

   Ejemplo:

      >>> import datetime as dt
      >>> dt.time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')
      '12:34'
      >>> my_time = dt.time(hour=12, minute=34, second=56, microsecond=0)
      >>> my_time.isoformat(timespec='microseconds')
      '12:34:56.000000'
      >>> my_time.isoformat(timespec='auto')
      '12:34:56'

   Distinto en la versión 3.6: Added the *timespec* parameter.

time.__str__()

   For a time "t", "str(t)" is equivalent to "t.isoformat()".

time.strftime(format)

   Return a string representing the time, controlled by an explicit
   format string.  See also strftime() and strptime() behavior and
   "time.isoformat()".

time.__format__(format)

   Same as "time.strftime()". This makes it possible to specify a
   format string for a "time" object in formatted string literals and
   when using "str.format()". See also strftime() and strptime()
   behavior and "time.isoformat()".

time.utcoffset()

   Si "tzinfo" es "None", retorna "None", sino retorna
   "self.tzinfo.utcoffset(None)", y genera una excepción si este
   último no retorna "None" o un objeto de "timedelta" con magnitud
   inferior a un día.

   Distinto en la versión 3.7: El desfase UTC no está restringido a un
   número entero de minutos.

time.dst()

   Si "tzinfo" es "None", retorna "None", sino retorna
   "self.tzinfo.utcoffset(None)", y genera una excepción si este
   último no retorna "None", o un objeto de "timedelta" con magnitud
   inferior a un día.

   Distinto en la versión 3.7: El desfase DST no está restringido a un
   número entero de minutos.

time.tzname()

   Si "tzinfo" es "None", retorna "None", sino retorna
   "self.tzinfo.tzname(None)", o genera una excepción si este último
   no retorna "None" o un objeto de cadena.

### Examples of usage: "time"

Ejemplos de trabajo con el objeto "time":

   >>> import datetime as dt
   >>> class TZ1(dt.tzinfo):
   ...     def utcoffset(self, when):
   ...         return dt.timedelta(hours=1)
   ...     def dst(self, when):
   ...         return dt.timedelta(0)
   ...     def tzname(self, when):
   ...         return "+01:00"
   ...     def  __repr__(self):
   ...         return f"{self.__class__.__name__}()"
   ...
   >>> t = dt.time(12, 10, 30, tzinfo=TZ1())
   >>> t
   datetime.time(12, 10, 30, tzinfo=TZ1())
   >>> t.isoformat()
   '12:10:30+01:00'
   >>> t.dst()
   datetime.timedelta(0)
   >>> t.tzname()
   '+01:00'
   >>> t.strftime("%H:%M:%S %Z")
   '12:10:30 +01:00'
   >>> 'The {} is {:%H:%M}.'.format("time", t)
   'The time is 12:10.'

## "tzinfo" objects

class datetime.tzinfo

   This is an *abstract base class*, meaning that this class should
   not be instantiated directly.  Define a subclass of "tzinfo" to
   capture information about a particular time zone.

   An instance of (a concrete subclass of) "tzinfo" can be passed to
   the constructors for "datetime" and "time" objects. The latter
   objects view their attributes as being in local time, and the
   "tzinfo" object supports methods revealing offset of local time
   from UTC, the name of the time zone, and DST offset, all relative
   to a date or time object passed to them.

   You need to derive a concrete subclass, and (at least) supply
   implementations of the standard "tzinfo" methods needed by the
   "datetime" methods you use. The "datetime" module provides
   "timezone", a simple concrete subclass of "tzinfo" which can
   represent time zones with fixed offset from UTC such as UTC itself
   or North American EST and EDT.

   Special requirement for pickling:  A "tzinfo" subclass must have an
   "__init__()" method that can be called with no arguments, otherwise
   it can be pickled but possibly not unpickled again. This is a
   technical requirement that may be relaxed in the future.

   A concrete subclass of "tzinfo" may need to implement the following
   methods. Exactly which methods are needed depends on the uses made
   of aware "datetime" objects. If in doubt, simply implement all of
   them.

tzinfo.utcoffset(dt)

   Retorna el desplazamiento de la hora local desde UTC, como un
   objeto "timedelta" que es positivo al este de UTC. Si la hora local
   es al oeste de UTC, esto debería ser negativo.

   Esto representa el desplazamiento *total* de UTC; por ejemplo, si
   un objeto "tzinfo" representa ajustes de zona horaria y DST,
   "utcoffset()" debería retornar su suma. Si no se conoce el
   desplazamiento UTC, retorna "None" . De lo contrario, el valor
   detonado debe ser un objeto de "timedelta" estrictamente entre
   "-timedelta(hours = 24)" y "timedelta (hours = 24)" (la magnitud
   del desplazamiento debe ser inferior a un día) La mayoría de las
   implementaciones de "utcoffset()" probablemente se parecerán a una
   de estas dos:

      return CONSTANT                 # fixed-offset class
      return CONSTANT + self.dst(dt)  # daylight-aware class

   Si "utcoffset()" no retorna "None", "dst()" no debería retornar
   "None" tampoco.

   La implementación por defecto de "utcoffset()" genera
   "NotImplementedError".

   Distinto en la versión 3.7: El desfase UTC no está restringido a un
   número entero de minutos.

tzinfo.dst(dt)

   Retorna el ajuste del horario de verano (DST), como un objeto de
   "timedelta" o "None" si no se conoce la información de DST.

   Return "timedelta(0)" if DST is not in effect. If DST is in effect,
   return the offset as a "timedelta" object (see "utcoffset()" for
   details). Note that DST offset, if applicable, has already been
   added to the UTC offset returned by "utcoffset()", so there's no
   need to consult "dst()" unless you're interested in obtaining DST
   info separately. For example, "datetime.timetuple()" calls its
   "tzinfo" attribute's "dst()" method to determine how the "tm_isdst"
   flag should be set, and "tzinfo.fromutc()" calls "dst()" to account
   for DST changes when crossing time zones.

   Una instancia *tz* de una subclase "tzinfo" que modela los horarios
   estándar y diurnos debe ser coherente en este sentido:

   "tz.utcoffset(dt) - tz.dst(dt)"

   must return the same result for every "datetime" *dt* with
   "dt.tzinfo == tz". For sane "tzinfo" subclasses, this expression
   yields the time zone's "standard offset", which should not depend
   on the date or the time, but only on geographic location. The
   implementation of "datetime.astimezone()" relies on this, but
   cannot detect violations; it's the programmer's responsibility to
   ensure it. If a "tzinfo" subclass cannot guarantee this, it may be
   able to override the default implementation of "tzinfo.fromutc()"
   to work correctly with "astimezone()" regardless.

   La mayoría de las implementaciones de "dst()" probablemente se
   parecerán a una de estas dos:

      import datetime as dt

      def dst(self, when):
          # a fixed-offset class:  doesn't account for DST
          return dt.timedelta(0)

   o:

      import datetime as dt

      def dst(self, when):
          # Code to set dston and dstoff to the time zone's DST
          # transition times based on the input when.year, and expressed
          # in standard local time.

          if dston <= when.replace(tzinfo=None) < dstoff:
              return dt.timedelta(hours=1)
          else:
              return dt.timedelta(0)

   La implementación predeterminada de "dst()" genera
   "NotImplementedError".

   Distinto en la versión 3.7: El desfase DST no está restringido a un
   número entero de minutos.

tzinfo.tzname(dt)

   Return the time zone name corresponding to the "datetime" object
   *dt*, as a string. Nothing about string names is defined by the
   "datetime" module, and there's no requirement that it mean anything
   in particular. For example, ""GMT"", ""UTC"", ""-500"", ""-5:00"",
   ""EDT"", ""US/Eastern"", ""America/New York"" are all valid
   replies. Return "None" if a string name isn't known. Note that this
   is a method rather than a fixed string primarily because some
   "tzinfo" subclasses will wish to return different names depending
   on the specific value of *dt* passed, especially if the "tzinfo"
   class is accounting for daylight time.

   La implementación predeterminada de "tzname()" genera
   "NotImplementedError".

These methods are called by a "datetime" or "time" object, in response
to their methods of the same names. A "datetime" object passes itself
as the argument, and a "time" object passes "None" as the argument. A
"tzinfo" subclass's methods should therefore be prepared to accept a
*dt* argument of "None", or of class "datetime".

Cuando se pasa "None", corresponde al diseñador de la clase decidir la
mejor respuesta. Por ejemplo, retornar "None" es apropiado si la clase
desea decir que los objetos de tiempo no participan en los protocolos
"tzinfo". Puede ser más útil que "utcoffset(None)" retorne el
desplazamiento UTC estándar, ya que no existe otra convención para
descubrir el desplazamiento estándar.

When a "datetime" object is passed in response to a "datetime" method,
"dt.tzinfo" is the same object as *self*. "tzinfo" methods can rely on
this, unless user code calls "tzinfo" methods directly. The intent is
that the "tzinfo" methods interpret *dt* as being in local time, and
not need worry about objects in other time zones.

Hay un método más "tzinfo" que una subclase puede desear anular:

tzinfo.fromutc(dt)

   This is called from the default "datetime.astimezone()"
   implementation. When called from that, "dt.tzinfo" is *self*, and
   *dt*'s date and time data are to be viewed as expressing a UTC
   time. The purpose of "fromutc()" is to adjust the date and time
   data, returning an equivalent datetime in *self*'s local time.

   Most "tzinfo" subclasses should be able to inherit the default
   "fromutc()" implementation without problems. It's strong enough to
   handle fixed-offset time zones, and time zones accounting for both
   standard and daylight time, and the latter even if the DST
   transition times differ in different years. An example of a time
   zone the default "fromutc()" implementation may not handle
   correctly in all cases is one where the standard offset (from UTC)
   depends on the specific date and time passed, which can happen for
   political reasons. The default implementations of "astimezone()"
   and "fromutc()" may not produce the result you want if the result
   is one of the hours straddling the moment the standard offset
   changes.

   Código de omisión para casos de error, el valor predeterminado
   "fromutc()" la implementación actúa como

      import datetime as dt

      def fromutc(self, when):
          # raise ValueError error if when.tzinfo is not self
          dtoff = when.utcoffset()
          dtdst = when.dst()
          # raise ValueError if dtoff is None or dtdst is None
          delta = dtoff - dtdst  # this is self's standard offset
          if delta:
              when += delta   # convert to standard local time
              dtdst = when.dst()
              # raise ValueError if dtdst is None
          if dtdst:
              return when + dtdst
          else:
              return when

En el siguiente archivo "tzinfo_examples.py" hay algunos ejemplos de
clases "tzinfo":

   import datetime as dt

   # A class capturing the platform's idea of local time.
   # (May result in wrong values on historical times in
   #  timezones where UTC offset and/or the DST rules had
   #  changed in the past.)
   import time

   ZERO = dt.timedelta(0)
   HOUR = dt.timedelta(hours=1)
   SECOND = dt.timedelta(seconds=1)

   STDOFFSET = dt.timedelta(seconds=-time.timezone)
   if time.daylight:
       DSTOFFSET = dt.timedelta(seconds=-time.altzone)
   else:
       DSTOFFSET = STDOFFSET

   DSTDIFF = DSTOFFSET - STDOFFSET

   class LocalTimezone(dt.tzinfo):

       def fromutc(self, when):
           assert when.tzinfo is self
           stamp = (when - dt.datetime(1970, 1, 1, tzinfo=self)) // SECOND
           args = time.localtime(stamp)[:6]
           dst_diff = DSTDIFF // SECOND
           # Detect fold
           fold = (args == time.localtime(stamp - dst_diff))
           return dt.datetime(*args, microsecond=when.microsecond,
                              tzinfo=self, fold=fold)

       def utcoffset(self, when):
           if self._isdst(when):
               return DSTOFFSET
           else:
               return STDOFFSET

       def dst(self, when):
           if self._isdst(when):
               return DSTDIFF
           else:
               return ZERO

       def tzname(self, when):
           return time.tzname[self._isdst(when)]

       def _isdst(self, when):
           tt = (when.year, when.month, when.day,
                 when.hour, when.minute, when.second,
                 when.weekday(), 0, 0)
           stamp = time.mktime(tt)
           tt = time.localtime(stamp)
           return tt.tm_isdst > 0

   Local = LocalTimezone()

   # A complete implementation of current DST rules for major US time zones.

   def first_sunday_on_or_after(when):
       days_to_go = 6 - when.weekday()
       if days_to_go:
           when += dt.timedelta(days_to_go)
       return when

   # US DST Rules
   #
   # This is a simplified (i.e., wrong for a few cases) set of rules for US
   # DST start and end times. For a complete and up-to-date set of DST rules
   # and timezone definitions, visit the Olson Database (or try pytz):
   # http://www.twinsun.com/tz/tz-link.htm
   # https://sourceforge.net/projects/pytz/ (might not be up-to-date)
   #
   # In the US, since 2007, DST starts at 2am (standard time) on the second
   # Sunday in March, which is the first Sunday on or after Mar 8.
   DSTSTART_2007 = dt.datetime(1, 3, 8, 2)
   # and ends at 2am (DST time) on the first Sunday of Nov.
   DSTEND_2007 = dt.datetime(1, 11, 1, 2)
   # From 1987 to 2006, DST used to start at 2am (standard time) on the first
   # Sunday in April and to end at 2am (DST time) on the last
   # Sunday of October, which is the first Sunday on or after Oct 25.
   DSTSTART_1987_2006 = dt.datetime(1, 4, 1, 2)
   DSTEND_1987_2006 = dt.datetime(1, 10, 25, 2)
   # From 1967 to 1986, DST used to start at 2am (standard time) on the last
   # Sunday in April (the one on or after April 24) and to end at 2am (DST time)
   # on the last Sunday of October, which is the first Sunday
   # on or after Oct 25.
   DSTSTART_1967_1986 = dt.datetime(1, 4, 24, 2)
   DSTEND_1967_1986 = DSTEND_1987_2006

   def us_dst_range(year):
       # Find start and end times for US DST. For years before 1967, return
       # start = end for no DST.
       if 2006 < year:
           dststart, dstend = DSTSTART_2007, DSTEND_2007
       elif 1986 < year < 2007:
           dststart, dstend = DSTSTART_1987_2006, DSTEND_1987_2006
       elif 1966 < year < 1987:
           dststart, dstend = DSTSTART_1967_1986, DSTEND_1967_1986
       else:
           return (dt.datetime(year, 1, 1), ) * 2

       start = first_sunday_on_or_after(dststart.replace(year=year))
       end = first_sunday_on_or_after(dstend.replace(year=year))
       return start, end

   class USTimeZone(dt.tzinfo):

       def __init__(self, hours, reprname, stdname, dstname):
           self.stdoffset = dt.timedelta(hours=hours)
           self.reprname = reprname
           self.stdname = stdname
           self.dstname = dstname

       def __repr__(self):
           return self.reprname

       def tzname(self, when):
           if self.dst(when):
               return self.dstname
           else:
               return self.stdname

       def utcoffset(self, when):
           return self.stdoffset + self.dst(when)

       def dst(self, when):
           if when is None or when.tzinfo is None:
               # An exception may be sensible here, in one or both cases.
               # It depends on how you want to treat them.  The default
               # fromutc() implementation (called by the default astimezone()
               # implementation) passes a datetime with when.tzinfo is self.
               return ZERO
           assert when.tzinfo is self
           start, end = us_dst_range(when.year)
           # Can't compare naive to aware objects, so strip the timezone from
           # when first.
           when = when.replace(tzinfo=None)
           if start + HOUR <= when < end - HOUR:
               # DST is in effect.
               return HOUR
           if end - HOUR <= when < end:
               # Fold (an ambiguous hour): use when.fold to disambiguate.
               return ZERO if when.fold else HOUR
           if start <= when < start + HOUR:
               # Gap (a non-existent hour): reverse the fold rule.
               return HOUR if when.fold else ZERO
           # DST is off.
           return ZERO

       def fromutc(self, when):
           assert when.tzinfo is self
           start, end = us_dst_range(when.year)
           start = start.replace(tzinfo=self)
           end = end.replace(tzinfo=self)
           std_time = when + self.stdoffset
           dst_time = std_time + HOUR
           if end <= dst_time < end + HOUR:
               # Repeated hour
               return std_time.replace(fold=1)
           if std_time < start or dst_time >= end:
               # Standard time
               return std_time
           if start <= std_time < end - HOUR:
               # Daylight saving time
               return dst_time

   Eastern  = USTimeZone(-5, "Eastern",  "EST", "EDT")
   Central  = USTimeZone(-6, "Central",  "CST", "CDT")
   Mountain = USTimeZone(-7, "Mountain", "MST", "MDT")
   Pacific  = USTimeZone(-8, "Pacific",  "PST", "PDT")

Tenga en cuenta que hay sutilezas inevitables dos veces al año en una
subclase "tzinfo" que representa tanto el horario estándar como el
horario de verano, en los puntos de transición DST. Para mayor
concreción, considere *US Eastern* (UTC -0500), donde EDT comienza el
minuto después de 1:59 (EST) el segundo domingo de marzo y termina el
minuto después de 1:59 (EDT) el primer domingo de noviembre

     UTC   3:MM  4:MM  5:MM  6:MM  7:MM  8:MM
     EST  22:MM 23:MM  0:MM  1:MM  2:MM  3:MM
     EDT  23:MM  0:MM  1:MM  2:MM  3:MM  4:MM

   start  22:MM 23:MM  0:MM  1:MM  3:MM  4:MM

     end  23:MM  0:MM  1:MM  1:MM  2:MM  3:MM

Cuando comienza el horario de verano (la línea de "inicio"),tiempo
real transcurrido (*wall time*) salta de 1:59 a 3:00. Un tiempo de
pared de la forma 2: MM realmente no tiene sentido ese día, por lo que
"astimezone (Eastern)" no entregará un resultado con "hour == 2" el
día en que comienza el horario de verano. Por ejemplo, en la
transición de primavera de 2016, obtenemos

   >>> import datetime as dt
   >>> from tzinfo_examples import HOUR, Eastern
   >>> u0 = dt.datetime(2016, 3, 13, 5, tzinfo=dt.timezone.utc)
   >>> for i in range(4):
   ...     u = u0 + i*HOUR
   ...     t = u.astimezone(Eastern)
   ...     print(u.time(), 'UTC =', t.time(), t.tzname())
   ...
   05:00:00 UTC = 00:00:00 EST
   06:00:00 UTC = 01:00:00 EST
   07:00:00 UTC = 03:00:00 EDT
   08:00:00 UTC = 04:00:00 EDT

When DST ends (the "end" line), there's a potentially worse problem:
there's an hour that can't be spelled unambiguously in local wall
time: the last hour of daylight time. In Eastern, that's times of the
form 5:MM UTC on the day daylight time ends. The local wall clock
leaps from 1:59 (daylight time) back to 1:00 (standard time) again.
Local times of the form 1:MM are ambiguous. "astimezone()" mimics the
local clock's behavior by mapping two adjacent UTC hours into the same
local hour then. In the Eastern example, UTC times of the form 5:MM
and 6:MM both map to 1:MM when converted to Eastern, but earlier times
have the "fold" attribute set to 0 and the later times have it set to
1. For example, at the Fall back transition of 2016, we get:

   >>> import datetime as dt
   >>> from tzinfo_examples import HOUR, Eastern
   >>> u0 = dt.datetime(2016, 11, 6, 4, tzinfo=dt.timezone.utc)
   >>> for i in range(4):
   ...     u = u0 + i*HOUR
   ...     t = u.astimezone(Eastern)
   ...     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
   ...
   04:00:00 UTC = 00:00:00 EDT 0
   05:00:00 UTC = 01:00:00 EDT 0
   06:00:00 UTC = 01:00:00 EST 1
   07:00:00 UTC = 02:00:00 EST 0

Note that the "datetime" instances that differ only by the value of
the "fold" attribute are considered equal in comparisons.

Applications that can't bear wall-time ambiguities should explicitly
check the value of the "fold" attribute or avoid using hybrid "tzinfo"
subclasses; there are no ambiguities when using "timezone", or any
other fixed-offset "tzinfo" subclass (such as a class representing
only EST (fixed offset -5 hours), or only EDT (fixed offset -4
hours)).

Ver también:

     "zoneinfo"
        The "datetime" module has a basic "timezone" class (for
        handling arbitrary fixed offsets from UTC) and its
        "timezone.utc" attribute (a UTC "timezone" instance).

        "zoneinfo" brings the *IANA time zone database* (also known as
        the Olson database) to Python, and its usage is recommended.

  IANA time zone database
     La base de datos de zonas horarias (a menudo llamada *tz, tzdata
     o zoneinfo*) contiene código y datos que representan el historial
     de la hora local de muchos lugares representativos de todo el
     mundo. Se actualiza periódicamente para reflejar los cambios
     realizados por los cuerpos políticos en los límites de la zona
     horaria, las compensaciones UTC y las reglas de horario de
     verano.

## "timezone" objects

The "timezone" class is a subclass of "tzinfo", each instance of which
represents a time zone defined by a fixed offset from UTC.

Objects of this class cannot be used to represent time zone
information in the locations where different offsets are used in
different days of the year or where historical changes have been made
to civil time.

class datetime.timezone(offset, name=None)

   El argumento *offset* debe especificarse como un objeto de
   "timedelta" que representa la diferencia entre la hora local y UTC.
   Debe estar estrictamente entre "-timedelta(horas = 24)" y
   "timedelta(horas = 24)", de lo contrario "ValueError" se genera.

   El argumento *name* es opcional. Si se especifica, debe ser una
   cadena de caracteres que se utilizará como el valor retornado por
   el método "datetime.tzname()".

   Added in version 3.2.

   Distinto en la versión 3.7: El desfase UTC no está restringido a un
   número entero de minutos.

timezone.utcoffset(dt)

   Retorna el valor fijo especificado cuando se construye la instancia
   "timezone".

   El argumento *dt* se ignora. El valor de retorno es una instancia
   de "timedelta" igual a la diferencia entre la hora local y UTC.

   Distinto en la versión 3.7: El desfase UTC no está restringido a un
   número entero de minutos.

timezone.tzname(dt)

   Retorna el valor fijo especificado cuando se construye la instancia
   "timezone".

   Si no se proporciona *name* en el constructor, el nombre retornado
   por "tzname(dt)" se genera a partir del valor del "offset" de la
   siguiente manera. Si *offset* es "timedelta (0)", el nombre es
   "UTC", de lo contrario es una cadena en el formato "UTC±HH:MM",
   donde ± es el signo de "offset", HH y MM son dos dígitos de
   "offset.hours" y "offset.minutes" respectivamente.

   Distinto en la versión 3.6: El nombre generado a partir de
   "offset=timedelta(0)" ahora es simplemente "'UTC'", no
   "'UTC+00:00'".

timezone.dst(dt)

   Siempre retorna "None".

timezone.fromutc(dt)

   Retorna "dt + offset". El argumento *dt* debe ser una instancia
   consciente (*aware*) "datetime", con "tzinfo" establecido en
   "self".

Atributos de clase:

timezone.utc

   The UTC time zone, "timezone(timedelta(0))".

## "strftime()" and "strptime()" behavior

"date", "datetime", y "time" los objetos admiten un método
"strftime(format)", para crear una cadena que represente el tiempo
bajo el control de una cadena de caracteres de formato explícito.

Conversely, the "date.strptime()", "datetime.strptime()" and
"time.strptime()" class methods create an object from a string
representing the time and a corresponding format string.

The table below provides a high-level comparison of "strftime()"
versus "strptime()":

+------------------+----------------------------------------------------------+--------------------------------------------------------------+
|                  | "strftime"                                               | "strptime"                                                   |
|==================|==========================================================|==============================================================|
| Uso              | Convierte objetos en una cadena de caracteres de acuerdo | Parse a string into an object given a corresponding format   |
## |                  | con un formato dado                                      |                                                              |

## | Tipo de método   | Método de instancia                                      | Método de clase                                              |

## | Firma            | "strftime(format)"                                       | "strptime(date_string, format)"                              |

### "strftime()" and "strptime()" format codes

These methods accept format codes that can be used to parse and format
dates:

   >>> import datetime as dt
   >>> dt.datetime.strptime('31/01/22 23:59:59.999999',
   ...                      '%d/%m/%y %H:%M:%S.%f')
   datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
   >>> _.strftime('%a %d %b %Y, %I:%M%p')
   'Mon 31 Jan 2022, 11:59PM'

La siguiente es una lista de todos los códigos de formato que requiere
el estándar 1989 C, y estos funcionan en todas las plataformas con una
implementación estándar C.

+-------------+----------------------------------+--------------------------+---------+
| Directiva   | Significado                      | Ejemplo                  | Notas   |
|=============|==================================|==========================|=========|
| "%a"        | Día de la semana como nombre     | *Sun, Mon, …, Sat        | (1)     |
|             | abreviado según la configuración | (en_US)*; *So, Mo, …, Sa |         |
## |             | regional.                        | (de_DE)*                 |         |

| "%A"        | Día de la semana como nombre     | *Sunday, Monday, …,      | (1)     |
|             | completo de la localidad.        | Saturday (en_US)*;       |         |
|             |                                  | *Sonntag, Montag, …,     |         |
## |             |                                  | Samstag (de_DE)*         |         |

| "%w"        | Día de la semana como un número  | 0, 1, …, 6               |         |
|             | decimal, donde 0 es domingo y 6  |                          |         |
## |             | es sábado.                       |                          |         |

| "%d"        | Día del mes como un número       | 01, 02, …, 31            | (9)     |
## |             | decimal rellenado con ceros.     |                          |         |

| "%b"        | Mes como nombre abreviado según  | *Jan, Feb, …, Dec        | (1)     |
|             | la configuración regional.       | (en_US)*; *Jan, Feb, …,  |         |
## |             |                                  | Dez (de_DE)*             |         |

| "%B"        | Mes como nombre completo según   | *January, February, …,   | (1)     |
|             | la configuración regional.       | December (en_US)*;       |         |
|             |                                  | *Januar, Februar, …,     |         |
## |             |                                  | Dezember (de_DE)*        |         |

| "%m"        | Mes como un número decimal       | 01, 02, …, 12            | (9)     |
## |             | rellenado con ceros.             |                          |         |

| "%y"        | Año sin siglo como un número     | 00, 01, …, 99            | (9)     |
## |             | decimal rellenado con ceros.     |                          |         |

| "%Y"        | Año con siglo como número        | 0001, 0002, …, 2013,     | (2)     |
## |             | decimal.                         | 2014, …, 9998, 9999      |         |

| "%H"        | Hora (reloj de 24 horas) como un | 00, 01, …, 23            | (9)     |
|             | número decimal rellenado con     |                          |         |
## |             | ceros.                           |                          |         |

| "%I"        | Hora (reloj de 12 horas) como un | 01, 02, …, 12            | (9)     |
|             | número decimal rellenado con     |                          |         |
## |             | ceros.                           |                          |         |

| "%p"        | El equivalente de la             | AM, PM (en_US); am, pm   | (1),    |
|             | configuración regional de AM o   | (de_DE)                  | (3)     |
## |             | PM.                              |                          |         |

| "%M"        | Minuto como un número decimal    | 00, 01, …, 59            | (9)     |
## |             | rellenado con ceros.             |                          |         |

| "%S"        | Segundo como un número decimal   | 00, 01, …, 59            | (4),    |
## |             | rellenado con ceros.             |                          | (9)     |

| "%f"        | Microsegundo como número         | 000000, 000001, …,       | (5)     |
|             | decimal, con ceros hasta 6       | 999999                   |         |
## |             | dígitos.                         |                          |         |

| "%z"        | Desplazamiento (*offset*) UTC en | (vacío), +0000, -0400,   | (6)     |
|             | la forma "±HHMM[SS[.ffffff]]"    | +1030, +063415,          |         |
|             | (cadena de caracteres vacía si   | -030712.345216           |         |
## |             | el objeto es naíf (*naive*)).    |                          |         |

| "%Z"        | Nombre de zona horaria (cadena   | (vacío), UTC, GMT        | (6)     |
|             | de caracteres vacía si el objeto |                          |         |
## |             | es naíf (*naive*)).              |                          |         |

| "%j"        | Día del año como un número       | 001, 002, …, 366         | (9)     |
## |             | decimal rellenado con ceros.     |                          |         |

| "%U"        | Número de semana del año         | 00, 01, …, 53            | (7),    |
|             | (domingo como primer día de la   |                          | (9)     |
|             | semana) como un número decimal   |                          |         |
|             | con ceros. Todos los días de un  |                          |         |
|             | nuevo año que preceden al primer |                          |         |
|             | domingo se consideran en la      |                          |         |
## |             | semana 0.                        |                          |         |

| "%W"        | Número de semana del año (lunes  | 00, 01, …, 53            | (7),    |
|             | como primer día de la semana)    |                          | (9)     |
|             | como un número decimal con       |                          |         |
|             | ceros. Todos los días de un      |                          |         |
|             | nuevo año que preceden al primer |                          |         |
|             | lunes se consideran en la semana |                          |         |
## |             | 0.                               |                          |         |

| "%c"        | Representación apropiada de      | *Tue Aug 16 21:30:00     | (1)     |
|             | fecha y hora de la configuración | 1988 (en_US)*; *Di 16    |         |
|             | regional.                        | Aug 21:30:00 1988        |         |
## |             |                                  | (de_DE)*                 |         |

| "%x"        | Representación de fecha          | 08/16/88 (*None*);       | (1)     |
|             | apropiada de la configuración    | 08/16/1988 (en_US);      |         |
## |             | regional.                        | 16.08.1988 (de_DE)       |         |

| "%X"        | Representación de la hora        | 21:30:00 (en_US);        | (1)     |
|             | apropiada de la configuración    | 21:30:00 (de_DE)         |         |
## |             | regional.                        |                          |         |

## | "%%"        | Un carácter literal "’%’".       | %                        |         |

Se incluyen varias directivas adicionales no requeridas por el
estándar C89 por conveniencia. Todos estos parámetros corresponden a
valores de fecha ISO 8601.

+-------------+----------------------------------+--------------------------+---------+
| Directiva   | Significado                      | Ejemplo                  | Notas   |
|=============|==================================|==========================|=========|
| "%G"        | ISO 8601 año con siglo que       | 0001, 0002, …, 2013,     | (8)     |
|             | representa el año que contiene   | 2014, …, 9998, 9999      |         |
|             | la mayor parte de la semana ISO  |                          |         |
## |             | ("%V").                          |                          |         |

| "%u"        | ISO 8601 día de la semana como   | 1, 2, …, 7               |         |
|             | un número decimal donde 1 es     |                          |         |
## |             | lunes.                           |                          |         |

| "%V"        | ISO 8601 semana como un número   | 01, 02, …, 53            | (8),    |
|             | decimal con lunes como primer    |                          | (9)     |
|             | día de la semana. La semana 01   |                          |         |
|             | es la semana que contiene el 4   |                          |         |
## |             | de enero.                        |                          |         |

| "%:z"       | UTC offset in the form           | (empty), +00:00, -04:00, | (6)     |
|             | "±HH:MM[:SS[.ffffff]]" (empty    | +10:30, +06:34:15,       |         |
## |             | string if the object is naive).  | -03:07:12.345216         |         |

These may not be available on all platforms when used with the
"strftime()" method. The ISO 8601 year and ISO 8601 week directives
are not interchangeable with the year and week number directives
above. Calling "strptime()" with incomplete or ambiguous ISO 8601
directives will raise a "ValueError".

The full set of format codes supported varies across platforms,
because Python calls the platform C library's "strftime()" function,
and platform variations are common. To see the full set of format
codes supported on your platform, consult the *strftime(3)*
documentation. There are also differences between platforms in
handling of unsupported format specifiers.

Added in version 3.6: "%G", "%u" y "%V" fueron añadidos.

Added in version 3.12: "%:z" was added.

### Technical detail

Broadly speaking, "d.strftime(fmt)" acts like the "time" module's
"time.strftime(fmt, d.timetuple())" although not all objects support a
"timetuple()" method.

For the "datetime.strptime()" and "date.strptime()" class methods, the
default value is "1900-01-01T00:00:00.000": any components not
specified in the format string will be pulled from the default value.

Nota:

  Format strings without separators can be ambiguous for parsing. For
  example, with "%Y%m%d", the string "2026111" may be parsed either as
  "2026-11-01" or as "2026-01-11". Use separators to ensure the input
  is parsed as intended.

Nota:

  When used to parse partial dates lacking a year,
  "datetime.strptime()" and "date.strptime()" will raise when
  encountering February 29 because the default year of 1900 is *not* a
  leap year.  Always add a default leap year to partial date strings
  before parsing.

   >>> import datetime as dt
   >>> value = "2/29"
   >>> dt.datetime.strptime(value, "%m/%d")
   Traceback (most recent call last):
   ...
   ValueError: day 29 must be in range 1..28 for month 2 in year 1900
   >>> dt.datetime.strptime(f"1904 {value}", "%Y %m/%d")
   datetime.datetime(1904, 2, 29, 0, 0)

Usar "datetime.strptime(date_string, format)" es equivalente a:

   datetime(*(time.strptime(date_string, format)[0:6]))

except when the format includes sub-second components or time zone
offset information, which are supported in "datetime.strptime" but are
discarded by "time.strptime".

For "time" objects, the format codes for year, month, and day should
not be used, as "time" objects have no such values. If they're used
anyway, 1900 is substituted for the year, and 1 for the month and day.

For "date" objects, the format codes for hours, minutes, seconds, and
microseconds should not be used, as "date" objects have no such
values. If they're used anyway, 0 is substituted for them.

Por la misma razón, el manejo de cadenas de formato que contienen
puntos de código Unicode que no se pueden representar en el conjunto
de caracteres del entorno local actual también depende de la
plataforma. En algunas plataformas, estos puntos de código se
conservan intactos en la salida, mientras que en otros "strftime"
puede generar "UnicodeError" o retornar una cadena vacía.

Notas:

1. Because the format depends on the current locale, care should be
   taken when making assumptions about the output value. Field
   orderings will vary (for example, "month/day/year" versus
   "day/month/year"), and the output may contain non-ASCII characters.

2. The "strptime()" method can parse years in the full [1, 9999]
   range, but years < 1000 must be zero-filled to 4-digit width.

   Distinto en la versión 3.2: In previous versions, "strftime()"
   method was restricted to years >= 1900.

   Distinto en la versión 3.3: In version 3.2, "strftime()" method was
   restricted to years >= 1000.

3. When used with the "strptime()" method, the "%p" directive only
   affects the output hour field if the "%I" directive is used to
   parse the hour.

4. Unlike the "time" module, the "datetime" module does not support
   leap seconds.

5. When used with the "strptime()" method, the "%f" directive accepts
   from one to six digits and zero pads on the right. "%f" is an
   extension to the set of format characters in the C standard (but
   implemented separately in datetime objects, and therefore always
   available).

6. For a naive object, the "%z", "%:z" and "%Z" format codes are
   replaced by empty strings.

   Para un objeto consciente (*aware*)

   "%z"
      "utcoffset()" is transformed into a string of the form
      "±HHMM[SS[.ffffff]]", where "HH" is a 2-digit string giving the
      number of UTC offset hours, "MM" is a 2-digit string giving the
      number of UTC offset minutes, "SS" is a 2-digit string giving
      the number of UTC offset seconds and "ffffff" is a 6-digit
      string giving the number of UTC offset microseconds. The
      "ffffff" part is omitted when the offset is a whole number of
      seconds and both the "ffffff" and the "SS" part is omitted when
      the offset is a whole number of minutes. For example, if
      "utcoffset()" returns "timedelta(hours=-3, minutes=-30)", "%z"
      is replaced with the string "'-0330'".

   Distinto en la versión 3.7: El desfase UTC no está restringido a un
   número entero de minutos.

   Distinto en la versión 3.7: When the "%z" directive is provided to
   the  "strptime()" method, the UTC offsets can have a colon as a
   separator between hours, minutes and seconds. For example,
   "'+01:00:00'" will be parsed as an offset of one hour. In addition,
   providing "'Z'" is identical to "'+00:00'".

   "%:z"
      Behaves exactly as "%z", but has a colon separator added between
      hours, minutes and seconds.

   "%Z"
      In "strftime()", "%Z" is replaced by an empty string if
      "tzname()" returns "None"; otherwise "%Z" is replaced by the
      returned value, which must be a string.

      "strptime()" only accepts certain values for "%Z":

      1. cualquier valor en "time.tzname" para la configuración
         regional de su máquina

      2. los valores codificados de forma rígida "UTC" y "GMT"

      Entonces, alguien que viva en Japón puede tener "JST", "UTC" y
      "GMT" como valores válidos, pero probablemente no "EST". Lanzará
      "ValueError" para valores no válidos.

   Distinto en la versión 3.2: When the "%z" directive is provided to
   the "strptime()" method, an aware "datetime" object will be
   produced. The "tzinfo" of the result will be set to a "timezone"
   instance.

7. When used with the "strptime()" method, "%U" and "%W" are only used
   in calculations when the day of the week and the calendar year
   ("%Y") are specified.

8. Similar to "%U" and "%W", "%V" is only used in calculations when
   the day of the week and the ISO year ("%G") are specified in a
   "strptime()" format string. Also note that "%G" and "%Y" are not
   interchangeable.

9. When used with the "strptime()" method, the leading zero is
   optional for  formats "%d", "%m", "%H", "%I", "%M", "%S", "%j",
   "%U", "%W", and "%V". Format "%y" does require a leading zero.

10. When parsing a month and day using "strptime()", always include a
    year in the format.  If the value you need to parse lacks a year,
    append an explicit dummy leap year.  Otherwise your code will
    raise an exception when it encounters leap day because the default
    year used by the parser (1900) is not a leap year.  Users run into
    that bug every leap year.

       >>> month_day = "02/29"
       >>> dt.datetime.strptime(f"{month_day};1984", "%m/%d;%Y")  # No leap year bug.
       datetime.datetime(1984, 2, 29, 0, 0)

    Deprecated since version 3.13, will be removed in version 3.15:
    "strptime()" calls using a format string containing a day of month
    without a year now emit a "DeprecationWarning". In 3.15 or later
    we may change this into an error or change the default year to a
    leap year. See gh-70647.

-[ Pie de notas ]-

[1] If, that is, we ignore the effects of relativity.

[2] Esto coincide con la definición del calendario "proléptico
    gregoriano" en el libro de *Dershowitz y Reingold* *Cálculos
    calendáricos*, donde es el calendario base para todos los
    cálculos. Consulte el libro sobre algoritmos para convertir entre
    ordinales gregorianos prolépticos y muchos otros sistemas de
    calendario.

[3] Consulte guide to the mathematics of the ISO 8601 calendar de R.
    H. van Gent para obtener una buena explicación.
