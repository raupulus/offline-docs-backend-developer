---
title: '"time" --- Time access and conversions'
source_url: https://docs.python.org/es/3
source_path: library/time.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4150
---

# "time" --- Time access and conversions

======================================================================

Este módulo proporciona varias funciones relacionadas con el tiempo.
Para la funcionalidad relacionada, consulte también los módulos
"datetime" y "calendar".

Aunque este módulo siempre está disponible, no todas las funciones
están disponibles en todas las plataformas.  La mayoría de las
funciones definidas en este módulo llaman a funciones C de la
biblioteca de la plataforma con el mismo nombre.  A veces puede ser
útil consultar la documentación de la plataforma, ya que la semántica
de estas funciones varía entre plataformas.

Una explicación de algunas terminologías y convenciones está en orden.

* Una *epoch* es el punto en el cual el tiempo empieza, el valor
  retorno de la función "time.gmtime(0)". El cual es Enero, 1, 1970,
  00:00:00(UTC) en todas las plataformas.

* El término *seconds since the epoch* se refiere al número total de
  segundos transcurridos desde la época, excluyendo típicamente leap
  seconds . Los segundos intercalares se excluyen de este total en
  todas las plataformas compatibles con POSIX.

* The functions in this module may not handle dates and times before
  the epoch or far in the future.  The cut-off point in the future is
  determined by the C library; for 32-bit systems, it is typically in
  2038.

* La función "strptime()" puede analizar años de 2 dígitos cuando se
  le da el código de formato "%y". Cuando se analizan los años de 2
  dígitos, se convierten de acuerdo con los estándares POSIX e ISO C:
  los valores 69--99 se asignan a 1969--1999, y los valores 0--68 se
  asignan a 2000--2068.

* UTC is Coordinated Universal Time and superseded Greenwich Mean Time
  or GMT as the basis of international timekeeping. The acronym UTC is
  not a mistake but conforms to an earlier, language-agnostic naming
  scheme for time standards such as UT0, UT1, and UT2.

* El horario de verano es el horario de verano, un ajuste de la zona
  horaria por (generalmente) una hora durante parte del año. Las
  reglas DST son mágicas (determinadas por la ley local) y pueden
  cambiar de un año a otro. La biblioteca C tiene una tabla que
  contiene las reglas locales (a menudo se lee desde un archivo del
  sistema para flexibilidad) y es la única fuente de verdadera
  sabiduría en este sentido.

* La precisión de las diversas funciones en tiempo real puede ser
  inferior a la sugerida por las unidades en las que se expresa su
  valor o argumento. P.ej. En la mayoría de los sistemas Unix, el
  reloj "funciona" solo 50 o 100 veces por segundo.

* On the other hand, the precision of "time()" and "sleep()" is better
  than their Unix equivalents: times are expressed as floating-point
  numbers, "time()" returns the most accurate time available (using
  Unix "gettimeofday()" where available), and "sleep()" will accept a
  time with a nonzero fraction (Unix "select()" is used to implement
  this, where available).

* El valor de tiempo retornado por "gmtime()", "localtime()", y
  "strptime()", y aceptado por "asctime()", "mktime()" y "strftime()",
  es una secuencia de 9 enteros. Los valores de retorno de "gmtime()",
  "localtime()", y "strptime()" también ofrecen nombres de atributos
  para campos individuales.

  Ver "struct_time" para una descripción de estos objetos.

  Distinto en la versión 3.3: The "struct_time" type was extended to
  provide the "tm_gmtoff" and "tm_zone" attributes when platform
  supports corresponding "struct tm" members.

  Distinto en la versión 3.6: The "struct_time" attributes "tm_gmtoff"
  and "tm_zone" are now available on all platforms.

* Use las siguientes funciones para convertir entre representaciones
  de tiempo:

  +---------------------------+---------------------------+---------------------------+
  | Desde                     | A                         | Usar                      |
  |===========================|===========================|===========================|
  | segundos desde la época   | "struct_time" en UTC      | "gmtime()"                |
  +---------------------------+---------------------------+---------------------------+
  | segundos desde la época   | "struct_time" en hora     | "localtime()"             |
  |                           | local                     |                           |
  +---------------------------+---------------------------+---------------------------+
  | "struct_time" en UTC      | segundos desde la época   | "calendar.timegm()"       |
  +---------------------------+---------------------------+---------------------------+
  | "struct_time" en hora     | segundos desde la época   | "mktime()"                |
  | local                     |                           |                           |
  +---------------------------+---------------------------+---------------------------+

## Las Funciones

time.asctime([t])

   Convierta una tupla o "struct_time" que represente una hora
   retornada por "gmtime()" o "localtime()" en una cadena de la
   siguiente forma: "'Dom 20 de junio 23:21:05 1993'". El campo del
   día tiene dos caracteres de largo y se rellena con espacio si el
   día es un solo dígito, por ejemplo: "'Miercoles  9 de Julio
   04:26:40 1993'".

   Si no se proporciona *t*, se utiliza la hora actual retornada por
   "localtime()". La información regional no es utilizada por
   "asctime()".

   Nota:

     A diferencia de la función C del mismo nombre, "asctime()" no
     agrega una nueva línea final.

time.pthread_getcpuclockid(thread_id)

   Retorna el *clk_id* del reloj de tiempo de CPU específico del
   subproceso para el *thread_id* especificado.

   Utilice "threading.get_ident()" o el atributo "ident" de objetos
   "threading.Thread" para obtener un valor adecuado para *
   thread_id*.

   Advertencia:

     Pasar un * thread_id * no válido o caducado puede provocar un
     comportamiento indefinido, como un error de segmentación.

   Availability: Unix

   See the man page for *pthread_getcpuclockid(3)* for further
   information.

   Added in version 3.7.

time.clock_getres(clk_id)

   Retorna la resolución (precisión) del reloj especificado *clk_id*.
   Consulte Constantes de ID de reloj para obtener una lista de los
   valores aceptados para *clk_id*.

   Availability: Unix.

   Added in version 3.3.

time.clock_gettime(clk_id) -> float

   Retorna la hora del reloj especificado *clk_id*. Consulte
   Constantes de ID de reloj para obtener una lista de los valores
   aceptados para *clk_id*.

   Utilice "clock_gettime_ns()" para evitar la pérdida de precisión
   que causa el tipo "float".

   Availability: Unix.

   Added in version 3.3.

time.clock_gettime_ns(clk_id) -> int

   Similar a "clock_gettime()" pero retorna el tiempo en nanosegundos.

   Availability: Unix.

   Added in version 3.7.

time.clock_settime(clk_id, time: float)

   Establece la hora del reloj especificado *clk_id*. Actualmente,
   "CLOCK_REALTIME" es el único valor aceptado para *clk_id*.

   Utilice "clock_settime_ns()" para evitar la pérdida de precisión
   que causa el tipo "float".

   Availability: Unix, not Android, not iOS.

   Added in version 3.3.

time.clock_settime_ns(clk_id, time: int)

   Similar a "clock_settime()" pero establece el tiempo con
   nanosegundos.

   Availability: Unix, not Android, not iOS.

   Added in version 3.7.

time.ctime([secs])

   Convert a time expressed in seconds since the epoch to a string of
   a form: "'Sun Jun 20 23:21:05 1993'" representing local time. The
   day field is two characters long and is space padded if the day is
   a single digit, e.g.: "'Wed Jun  9 04:26:40 1993'".

   Si no se proporciona *secs* o "None", se utiliza la hora actual
   retornada por "time()". "ctime(secs)" es equivalente a
   "asctime(localtime(secs))". La información de configuración
   regional no la utiliza "ctime()".

time.get_clock_info(name)

   Obtenga información sobre el reloj especificado como un objeto de
   espacio de nombres. Los nombres de reloj admitidos y las funciones
   correspondientes para leer su valor son:

   * "'monotonic'": "time.monotonic()"

   * "'perf_counter'": "time.perf_counter()"

   * "'process_time'": "time.process_time()"

   * "'thread_time'": "time.thread_time()"

   * "'time'": "time.time()"

   El resultado tiene los siguientes atributos:

   * *adjustable*: "True" if the clock can be set to jump forward or
     backward in time, "False" otherwise. Does not refer to gradual
     NTP rate adjustments.

   * *implementation*: el nombre de la función C subyacente utilizada
     para obtener el valor del reloj. Consulte Constantes de ID de
     reloj para conocer los posibles valores.

   * *monotonic*: "True" si el reloj no puede retroceder, "False" de
     lo contrario

   * *resolution*: La resolución del reloj en segundos ("float")

   Added in version 3.3.

time.gmtime([secs])

   Convert a time expressed in seconds since the epoch to a
   "struct_time" in UTC in which the dst flag is always zero.  If
   *secs* is not provided or "None", the current time as returned by
   "time()" is used.  Fractions of a second are ignored.  See above
   for a description of the "struct_time" object. See
   "calendar.timegm()" for the inverse of this function.

time.localtime([secs])

   Como "gmtime()" pero se convierte a la hora local. Si no se
   proporciona *secs* o "None", se utiliza la hora actual retornada
   por "time()". El indicador *dst* se establece en "1" cuando DST se
   aplica al tiempo dado.

   "localtime()" podría lanzar un "OverflowError", si los valores de
   la marca de tiempo están fuera del rango soportado por las
   funciones "localtime()" o "gmtime()" de la plataforma C, y el
   "OSError" en las funciones "localtime()" o "gmtime()". Es común que
   este esté restringido para los años entre 1970 y 2038.

time.mktime(t)

   This is the inverse function of "localtime()".  Its argument is the
   "struct_time" or full 9-tuple (since the dst flag is needed; use
   "-1" as the dst flag if it is unknown) which expresses the time in
   *local* time, not UTC.  It returns a floating-point number, for
   compatibility with "time()". If the input value cannot be
   represented as a valid time, either "OverflowError" or "ValueError"
   will be raised (which depends on whether the invalid value is
   caught by Python or the underlying C libraries). The earliest date
   for which it can generate a time is platform-dependent.

time.monotonic() -> float

   Retorna el valor (en segundos fraccionarios) de un reloj monótono,
   es decir, un reloj que no puede retroceder. El reloj no se ve
   afectado por las actualizaciones del reloj del sistema. El punto de
   referencia del valor retornado no está definido, de modo que sólo
   la diferencia entre los resultados de dos llamadas es válida.

   Clock:

   * On Windows, call "QueryPerformanceCounter()" and
     "QueryPerformanceFrequency()".

   * On macOS, call "mach_absolute_time()" and "mach_timebase_info()".

   * On HP-UX, call "gethrtime()".

   * Call "clock_gettime(CLOCK_HIGHRES)" if available.

   * Otherwise, call "clock_gettime(CLOCK_MONOTONIC)".

   Utilice "monotonic_ns()" para evitar la pérdida de precisión que
   causa el tipo "float".

   Added in version 3.3.

   Distinto en la versión 3.5: The function is now always available
   and the clock is now the same for all processes.

   Distinto en la versión 3.10: On macOS, the clock is now the same
   for all processes.

time.monotonic_ns() -> int

   Similar a "monotonic()", pero el tiempo de retorno es en
   nanosegundos.

   Added in version 3.7.

time.perf_counter() -> float

   Return the value (in fractional seconds) of a performance counter,
   i.e. a clock with the highest available resolution to measure a
   short duration.  It does include time elapsed during sleep. The
   clock is the same for all processes. The reference point of the
   returned value is undefined, so that only the difference between
   the results of two calls is valid.

   **Detalles de implementación de CPython:** On CPython, use the same
   clock as "time.monotonic()" and is a monotonic clock, i.e. a clock
   that cannot go backwards.

   Utilice la función "perf_counter_ns()" para evitar la pérdida de
   precisión que causa el tipo "float".

   Added in version 3.3.

   Distinto en la versión 3.10: On Windows, the clock is now the same
   for all processes.

   Distinto en la versión 3.13: Use the same clock as
   "time.monotonic()".

time.perf_counter_ns() -> int

   Similar a "perf_counter()", pero el tiempo de retorno es en
   nanosegundos.

   Added in version 3.7.

time.process_time() -> float

   Retorna el valor (en fracciones de segundo) de la suma del sistema
   y el tiempo de CPU del usuario del proceso actual. No incluye el
   tiempo transcurrido durante el sleep. Es todo el proceso por
   definición. El punto de referencia del valor retornado no está
   definido, de modo que sólo la diferencia entre los resultados de
   dos llamadas es válida.

   Utilice "process_time_ns()" para evitar la pérdida de precisión que
   causa el tipo "float".

   Added in version 3.3.

time.process_time_ns() -> int

   Similar a "process_time()" pero retorna el tiempo en nanosegundos.

   Added in version 3.7.

time.sleep(secs)

   Suspend execution of the calling thread for the given number of
   seconds. The argument may be a floating-point number to indicate a
   more precise sleep time.

   Si el sleep es interrumpido por una señal y ninguna excepción fue
   lanzada por el gestor de señales, este sleep es reiniciado con un
   tiempo límite recalculado.

   El tiempo de suspensión podría ser mayor al requerido por un monto
   arbitrario, a raíz de la programación de otra actividad del
   sistema.

   -[ Windows implementation ]-

   On Windows, if *secs* is zero, the thread relinquishes the
   remainder of its time slice to any other thread that is ready to
   run. If there are no other threads ready to run, the function
   returns immediately, and the thread continues execution.  On
   Windows 10 and newer the implementation uses a high-resolution
   timer which provides resolution of 100 nanoseconds. If *secs* is
   zero, "Sleep(0)" is used.

   -[ Unix implementation ]-

   * Si está disponible, use "clock_nanosleep()" (resolución: 1
     nanosegundo);

   * O use "nanosleep()" si está disponible (resolución: 1
     nanosegundo);

   * O use "select()" (resolución: 1 microsegundo).

   Nota:

     To emulate a "no-op", use "pass" instead of "time.sleep(0)".To
     voluntarily relinquish the CPU, specify a real-time scheduling
     policy and use "os.sched_yield()" instead.

   Raises an auditing event "time.sleep" with argument "secs".

   Distinto en la versión 3.5: La función ahora duerme al menos *
   segundos * incluso si el sleep es interrumpido por una señal,
   excepto si el manejador de la señal genera una excepción (ver **PEP
   475** para la justificación).

   Distinto en la versión 3.11: On Unix, the "clock_nanosleep()" and
   "nanosleep()" functions are now used if available. On Windows, a
   waitable timer is now used.

   Distinto en la versión 3.13: Raises an auditing event.

time.strftime(format[, t])

   Convierta una tupla o "struct_time" que represente un tiempo
   retornado por "gmtime()" o "localtime()" en una cadena como se
   especifica mediante el argumento *format*. Si no se proporciona
   *t*, se utiliza la hora actual retornada por "localtime()".
   *format* debe ser una cadena. Se lanza un "ValueError" si algún
   campo en *t* está fuera del rango permitido.

   0 es un argumento legal para cualquier posición en la tupla de
   tiempo; si normalmente es ilegal, el valor se fuerza a uno
   correcto.

   Las siguientes directivas se pueden incrustar en la cadena
   *format*. Se muestran sin el ancho de campo opcional y la
   especificación de precisión, y se reemplazan por los caracteres
   indicados en el resultado "strftime()":

   +-------------+--------------------------------------------------+---------+
   | Directiva   | Significado                                      | Notas   |
   |=============|==================================================|=========|
   | "%a"        | Nombre abreviado del día local de la localidad.  |         |
   +-------------+--------------------------------------------------+---------+
   | "%A"        | Nombre completo del día laborable de Localidad.  |         |
   +-------------+--------------------------------------------------+---------+
   | "%b"        | Nombre abreviado del mes de la localidad.        |         |
   +-------------+--------------------------------------------------+---------+
   | "%B"        | Nombre completo del mes de la localidad.         |         |
   +-------------+--------------------------------------------------+---------+
   | "%c"        | Representación apropiada de fecha y hora de la   |         |
   |             | localidad.                                       |         |
   +-------------+--------------------------------------------------+---------+
   | "%d"        | Día del mes como número decimal [01,31].         |         |
   +-------------+--------------------------------------------------+---------+
   | "%f"        | Microseconds as a decimal number                 | (1)     |
   |             | [000000,999999].                                 |         |
   +-------------+--------------------------------------------------+---------+
   | "%H"        | Hora (reloj de 24 horas) como un número decimal  |         |
   |             | [00,23].                                         |         |
   +-------------+--------------------------------------------------+---------+
   | "%I"        | Hora (reloj de 12 horas) como un número decimal  |         |
   |             | [01,12].                                         |         |
   +-------------+--------------------------------------------------+---------+
   | "%j"        | Día del año como número decimal [001,366].       |         |
   +-------------+--------------------------------------------------+---------+
   | "%m"        | Mes como un número decimal [01,12].              |         |
   +-------------+--------------------------------------------------+---------+
   | "%M"        | Minuto como un número decimal [00,59].           |         |
   +-------------+--------------------------------------------------+---------+
   | "%p"        | El equivalente de la configuración regional de   | (2)     |
   |             | AM o PM.                                         |         |
   +-------------+--------------------------------------------------+---------+
   | "%S"        | Segunda como un número decimal [00,61].          | (3)     |
   +-------------+--------------------------------------------------+---------+
   | "%U"        | Número de semana del año (domingo como primer    | (4)     |
   |             | día de la semana) como número decimal [00,53].   |         |
   |             | Todos los días en un nuevo año anterior al       |         |
   |             | primer domingo se consideran en la semana 0.     |         |
   +-------------+--------------------------------------------------+---------+
   | "%u"        | Day of the week (Monday is 1; Sunday is 7) as a  |         |
   |             | decimal number [1, 7].                           |         |
   +-------------+--------------------------------------------------+---------+
   | "%w"        | Día de la semana como un número decimal [0       |         |
   |             | (domingo), 6].                                   |         |
   +-------------+--------------------------------------------------+---------+
   | "%W"        | Número de semana del año (lunes como primer día  | (4)     |
   |             | de la semana) como número decimal [00,53]. Todos |         |
   |             | los días en un nuevo año anterior al primer      |         |
   |             | lunes se consideran en la semana 0.              |         |
   +-------------+--------------------------------------------------+---------+
   | "%x"        | Representación de fecha apropiada de la          |         |
   |             | localidad.                                       |         |
   +-------------+--------------------------------------------------+---------+
   | "%X"        | Representación del tiempo apropiado de la        |         |
   |             | localidad.                                       |         |
   +-------------+--------------------------------------------------+---------+
   | "%y"        | Año sin siglo como número decimal [00,99].       |         |
   +-------------+--------------------------------------------------+---------+
   | "%Y"        | Año con siglo como número decimal.               |         |
   +-------------+--------------------------------------------------+---------+
   | "%z"        | Time zone offset indicating a positive or        |         |
   |             | negative time difference from UTC/GMT of the     |         |
   |             | form +HHMM or -HHMM, where H represents decimal  |         |
   |             | hour digits and M represents decimal minute      |         |
   |             | digits [-23:59, +23:59]. [1]                     |         |
   +-------------+--------------------------------------------------+---------+
   | "%Z"        | Time zone name (no characters if no time zone    |         |
   |             | exists). Deprecated. [1]                         |         |
   +-------------+--------------------------------------------------+---------+
   | "%G"        | ISO 8601 year (similar to "%Y" but follows the   |         |
   |             | rules for the ISO 8601 calendar year). The year  |         |
   |             | starts with the week that contains the first     |         |
   |             | Thursday of the calendar year.                   |         |
   +-------------+--------------------------------------------------+---------+
   | "%V"        | ISO 8601 week number (as a decimal number        |         |
   |             | [01,53]). The first week of the year is the one  |         |
   |             | that contains the first Thursday of the year.    |         |
   |             | Weeks start on Monday.                           |         |
   +-------------+--------------------------------------------------+---------+
   | "%%"        | Un carácter literal "'%'".                       |         |
   +-------------+--------------------------------------------------+---------+

   Notas:

   1. The "%f" format directive only applies to "strptime()", not to
      "strftime()". However, see also "datetime.datetime.strptime()"
      and "datetime.datetime.strftime()" where the "%f" format
      directive applies to microseconds.

   2. Cuando se usa con la función "strptime()", la directiva "%p"
      solo afecta el campo de hora de salida si se usa la directiva
      "%I" para analizar la hora.

   3. El rango realmente es "0" a "61"; el valor "60" es válido en las
      marcas de tiempo que representan segundos intercalares y el
      valor "61" es compatible por razones históricas.

   4. Cuando se usa con la función "strptime()", "%U" y "%W" solo se
      usan en los cálculos cuando se especifica el día de la semana y
      el año.

   Here is an example, a format for dates compatible with that
   specified  in the **RFC 5322** Internet email standard.  [1]

      >>> from time import gmtime, strftime
      >>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
      'Thu, 28 Jun 2001 14:17:15 +0000'

   Es posible que se admitan directivas adicionales en ciertas
   plataformas, pero solo las que se enumeran aquí tienen un
   significado estandarizado por ANSI C. Para ver el conjunto completo
   de códigos de formato admitidos en su plataforma, consulte la
   documentación de *strftime(3)*.

   En algunas plataformas, una especificación de precisión y ancho de
   campo opcional puede seguir inmediatamente el "'%'" inicial de una
   directiva en el siguiente orden; Esto tampoco es portátil. El ancho
   del campo es normalmente 2 excepto "%j" donde es 3.

time.strptime(string[, format])

   Analiza una cadena que representa un tiempo de acuerdo con un
   formato. El valor de retorno es a "struct_time" como lo retorna
   "gmtime()" o "localtime()".

   El parámetro *format* utiliza las mismas directivas que las
   utilizadas por "strftime()"; el valor predeterminado es ""%a %b %d
   %H:%M:%S %Y"" que coincide con el formato retornado por "ctime()".
   Si *string* no se puede analizar de acuerdo con *format*, o si
   tiene un exceso de datos después del análisis, se lanza un
   "ValueError". Los valores predeterminados utilizados para completar
   los datos faltantes cuando no se pueden inferir valores más
   precisos son "(1900, 1, 1, 0, 0, 0, 0, 1, -1)". Tanto *string* como
   *format* deben ser strings.

   Por ejemplo:

   >>> import time
   >>> time.strptime("30 Nov 00", "%d %b %y")
   time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                    tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

   La compatibilidad con la directiva "%Z" se basa en los valores
   contenidos en "tzname" y en si "daylight" es verdadero. Debido a
   esto, es específico de la plataforma, excepto para reconocer UTC y
   GMT que siempre se conocen (y se consideran zonas horarias que no
   son de horario de verano).

   Solo se admiten las directivas especificadas en la documentación.
   Debido a que "strftime()" se implementa por plataforma, a veces
   puede ofrecer más directivas que las enumeradas. Pero "strptime()"
   es independiente de cualquier plataforma y, por lo tanto, no
   necesariamente admite todas las directivas disponibles que no están
   documentadas como compatibles.

class time.struct_time

   El tipo de secuencia de valores de tiempo retornado por "gmtime()",
   "localtime()", y "strptime()". Es un objeto con una interfaz *named
   tuple*: se puede acceder a los valores por índice y por nombre de
   atributo. Los siguientes valores están presentes:

   +-----------------------------------+-----------------------------------+-----------------------------------+
   | Índice                            | Atributo                          | Valores                           |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 0                                 | tm_year                           | (por ejemplo, 1993)               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 1                                 | tm_mon                            | rango [1, 12]                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 2                                 | tm_mday                           | rango [1, 31]                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 3                                 | tm_hour                           | rango [0, 23]                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 4                                 | tm_min                            | rango [0, 59]                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 5                                 | tm_sec                            | range [0, 61]; see Note (2) in    |
   |                                   |                                   | "strftime()"                      |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 6                                 | tm_wday                           | range [0, 6]; Monday is 0         |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 7                                 | tm_yday                           | rango [1, 366]                    |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 8                                 | tm_isdst                          | 0, 1 ó -1; ver abajo              |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | N/A                               | tm_zone                           | abreviatura del nombre de la zona |
   |                                   |                                   | horaria                           |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | N/A                               | tm_gmtoff                         | desplazamiento al este de UTC en  |
   |                                   |                                   | segundos                          |
   +-----------------------------------+-----------------------------------+-----------------------------------+

   Tenga en cuenta que, a diferencia de la estructura C, el valor del
   mes es un rango de [1, 12], no [0, 11].

   En llamadas a "mktime()", "tm_isdst" puede establecerse en 1 cuando
   el horario de verano está vigente y 0 cuando no lo está. Un valor
   de -1 indica que esto no se conoce y, por lo general, se completará
   el estado correcto.

   Cuando una tupla con una longitud incorrecta se pasa a una función
   que espera a "struct_time", o que tiene elementos del tipo
   incorrecto, se lanza un "TypeError".

time.time() -> float

   Return the time in seconds since the epoch as a floating-point
   number. The handling of leap seconds is platform dependent. On
   Windows and most Unix systems, the leap seconds are not counted
   towards the time in seconds since the epoch. This is commonly
   referred to as Unix time.

   Note that even though the time is always returned as a floating-
   point number, not all systems provide time with a better precision
   than 1 second. While this function normally returns non-decreasing
   values, it can return a lower value than a previous call if the
   system clock has been set back between the two calls.

   El número retornado por "time()" se puede convertir a un formato de
   hora más común (es decir, año, mes, día, hora, etc.) en UTC
   pasándolo a función "gmtime()" o en hora local pasándola a la
   función "localtime()". En ambos casos se retorna un objeto
   "struct_time", desde el cual se puede acceder a los componentes de
   la fecha del calendario como atributos.

   Clock:

   * On Windows, call "GetSystemTimePreciseAsFileTime()".

   * Call "clock_gettime(CLOCK_REALTIME)" if available.

   * Otherwise, call "gettimeofday()".

   Utilice "time_ns()" para evitar la pérdida de precisión que causa
   el tipo "float".

Distinto en la versión 3.13: On Windows, calls
"GetSystemTimePreciseAsFileTime()" instead of
"GetSystemTimeAsFileTime()".

time.time_ns() -> int

   Similar a "time()" pero retorna el tiempo como un número entero de
   nanosegundos desde la época.

   Added in version 3.7.

time.thread_time() -> float

   Retorna el valor (en fracciones de segundo) de la suma del sistema
   y el tiempo de CPU del usuario del subproceso actual. No incluye el
   tiempo transcurrido durante el sleep. Es específico del hilo por
   definición. El punto de referencia del valor retornado no está
   definido, de modo que sólo la diferencia entre los resultados de
   dos llamadas en el mismo hilo es válida.

   Utilice "thread_time_ns()" para evitar la pérdida de precisión que
   causa el tipo "float".

   Availability: Linux, Unix, Windows.

   Sistemas Unix que soporten "CLOCK_THREAD_CPUTIME_ID".

   Added in version 3.7.

time.thread_time_ns() -> int

   Similar a "thread_time()" pero retorna el tiempo en nanosegundos.

   Added in version 3.7.

time.tzset()

   Restablezca las reglas de conversión de tiempo utilizadas por las
   rutinas de la biblioteca. La variable de entorno "TZ" especifica
   cómo se hace esto. También establecerá las variables "tzname" (de
   variable de entorno "TZ"), "timezone" (segundos que no son DST al
   oeste de UTC), "altzone" (segundos DST al oeste de UTC ) y
   "daylight" (a 0 si esta zona horaria no tiene ninguna regla de
   horario de verano, o a cero si hay un horario pasado, presente o
   futuro cuando se aplica el horario de verano).

   Availability: Unix.

   Nota:

     Aunque en muchos casos, cambiar la variable de entorno "TZ" puede
     afectar la salida de funciones como "localtime()" sin llamar a
     "tzset()", no se debe confiar en este comportamiento.La variable
     de entorno "TZ" no debe contener espacios en blanco.

   El formato estándar de la variable de entorno "TZ" es (espacio en
   blanco agregado para mayor claridad):

      std offset [dst [offset [,start[/time], end[/time]]]]

   Donde están los componentes:

   "std" y  "dst"
      Tres o más caracteres alfanuméricos que dan las abreviaturas de
      zona horaria. Estos se propagarán en time.tzname

   "offset"
      El desplazamiento tiene la forma: "± hh[:mm[:ss]]". Esto indica
      el valor agregado de la hora local para llegar a UTC. Si está
      precedido por un '-', la zona horaria está al este del primer
      meridiano; de lo contrario, es oeste. Si no hay desplazamiento
      después de dst, se supone que el horario de verano es una hora
      antes del horario estándar.

   "start[/time], end[/time]"
      Indica cuándo cambiar hacia y desde DST. El formato de las
      fechas de inicio y finalización es uno de los siguientes:

      "J*n*"
         El día juliano * n * (1 <= * n * <= 365). Los días bisiestos
         no se cuentan, por lo que en todos los años el 28 de febrero
         es el día 59 y el 1 de marzo es el día 60.

      "*n*"
         El día juliano basado en cero (0 <= * n * <= 365). Los días
         bisiestos se cuentan y es posible referirse al 29 de febrero.

      "M*m*.*n*.*d*"
         El  día d (0 <= *d* <= 6) de la semana *n* del mes *m* del
         año (1 <= *n* <= 5, 1 <= *m* <= 12, donde la semana 5
         significa "el último *d* día del mes *m*", que puede ocurrir
         en la cuarta o quinta semana). La semana 1 es la primera
         semana en la que ocurre el día *d*. El día cero es un
         domingo.

      "time" tiene el mismo formato que "offset", excepto que no se
      permite ningún signo inicial ('-' o '+'). El valor
      predeterminado, si no se da el tiempo, es 02:00:00.

      >>> os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
      >>> time.tzset()
      >>> time.strftime('%X %x %Z')
      '02:07:36 05/08/03 EDT'
      >>> os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
      >>> time.tzset()
      >>> time.strftime('%X %x %Z')
      '16:08:12 05/08/03 AEST'

   En muchos sistemas Unix (incluidos *BSD, Linux, Solaris y Darwin),
   es más conveniente utilizar la base de datos *zoneinfo*
   (*tzfile(5)*) del sistema para especificar las reglas de zona
   horaria. Para hacer esto, configure la variable de entorno "TZ" en
   la ruta del archivo de datos de zona horaria requerida, en relación
   con la raíz de la base de datos de zona horaria 'zoneinfo' de los
   sistemas, generalmente ubicada en "/usr/share/zoneinfo" . Por
   ejemplo, "'US/Eastern'", "'Australia/Melbourne'", "'Egypt'" o
   "'Europe/Amsterdam'".

      >>> os.environ['TZ'] = 'US/Eastern'
      >>> time.tzset()
      >>> time.tzname
      ('EST', 'EDT')
      >>> os.environ['TZ'] = 'Egypt'
      >>> time.tzset()
      >>> time.tzname
      ('EET', 'EEST')

## Constantes de ID de reloj

Estas constantes se utilizan como parámetros para "clock_getres()" y
"clock_gettime()".

time.CLOCK_BOOTTIME

   Idéntico a "CLOCK_MONOTONIC", excepto que también incluye cualquier
   momento en que el sistema esté suspendido.

   Esto permite que las aplicaciones obtengan un reloj monótono con
   suspensión sin tener que lidiar con las complicaciones de
   "CLOCK_REALTIME", que puede tener discontinuidades si se cambia la
   hora usando "settimeofday()" o similar.

   Availability: Linux >= 2.6.39.

   Added in version 3.7.

time.CLOCK_HIGHRES

   El sistema operativo Solaris tiene un temporizador "CLOCK_HIGHRES"
   que intenta utilizar una fuente de hardware óptima y puede brindar
   una resolución cercana a los nanosegundos. "CLOCK_HIGHRES" es el
   reloj de alta resolución no ajustable.

   Availability: Solaris.

   Added in version 3.3.

time.CLOCK_MONOTONIC

   Reloj que no se puede configurar y representa el tiempo monótono
   desde algún punto de partida no especificado.

   Availability: Unix.

   Added in version 3.3.

time.CLOCK_MONOTONIC_RAW

   Similar a "CLOCK_MONOTONIC", pero proporciona acceso a un tiempo
   sin procesar basado en hardware que no está sujeto a ajustes NTP.

   Availability: Linux >= 2.6.28, macOS >= 10.12.

   Added in version 3.3.

time.CLOCK_MONOTONIC_RAW_APPROX

   Similar to "CLOCK_MONOTONIC_RAW", but reads a value cached by the
   system at context switch and hence has less accuracy.

   Availability: macOS >= 10.12.

   Added in version 3.13.

time.CLOCK_PROCESS_CPUTIME_ID

   Temporizador por proceso de alta resolución desde la CPU.

   Availability: Unix.

   Added in version 3.3.

time.CLOCK_PROF

   Temporizador por proceso de alta resolución desde la CPU.

   Availability: FreeBSD, NetBSD >= 7, OpenBSD.

   Added in version 3.7.

time.CLOCK_TAI

   International Atomic Time

   El sistema debe contar con una tabla de segundos intercalares para
   que éste dé la respuesta correcta. Software PTP o NTP puede
   mantener una tabla de segundos intercalares.

   Availability: Linux.

   Added in version 3.9.

time.CLOCK_THREAD_CPUTIME_ID

   Reloj de tiempo de CPU específico de subproceso.

   Availability: Unix.

   Added in version 3.3.

time.CLOCK_UPTIME

   Tiempo cuyo valor absoluto es el tiempo que el sistema ha estado
   funcionando y no suspendido, proporcionando una medición precisa
   del tiempo de actividad, tanto absoluta como de intervalo.

   Availability: FreeBSD, OpenBSD >= 5.5.

   Added in version 3.7.

time.CLOCK_UPTIME_RAW

   Reloj que se incrementa monótonamente, rastreando el tiempo desde
   un punto arbitrario, no afectado por los ajustes de frecuencia o
   tiempo y no incrementado mientras el sistema está dormido.

   Availability: macOS >= 10.12.

   Added in version 3.8.

time.CLOCK_UPTIME_RAW_APPROX

   Like "CLOCK_UPTIME_RAW", but the value is cached by the system at
   context switches and therefore has less accuracy.

   Availability: macOS >= 10.12.

   Added in version 3.13.

La siguiente constante es el único parámetro que se puede enviar a
"clock_settime()".

time.CLOCK_REALTIME

   Real-time clock.  Setting this clock requires appropriate
   privileges. The clock is the same for all processes.

   Availability: Unix.

   Added in version 3.3.

## Constantes de zona horaria

time.altzone

   El desplazamiento de la zona horaria de horario de verano local, en
   segundos al oeste de UTC, si se define uno. Esto es negativo si la
   zona horaria local del horario de verano está al este de UTC (como
   en Europa occidental, incluido el Reino Unido). Solo use esto si la
   "daylight" no es cero. Vea la nota abajo.

time.daylight

   No es cero si se define una zona horaria DST. Vea la nota abajo.

time.timezone

   El desplazamiento de la zona horaria local (no DST), en segundos al
   oeste de UTC (negativo en la mayoría de Europa occidental, positivo
   en los EE. UU., Cero en el Reino Unido). Vea la nota abajo.

time.tzname

   Una tupla de dos cadenas: la primera es el nombre de la zona
   horaria local no DST, la segunda es el nombre de la zona horaria
   local DST. Si no se define la zona horaria DST, la segunda cadena
   no debe usarse. Vea la nota abajo.

Nota:

  For the above Timezone constants ("altzone", "daylight", "timezone",
  and "tzname"), the value is determined by the timezone rules in
  effect at module load time or the last time "tzset()" is called and
  may be incorrect for times in the past.  It is recommended to use
  the "tm_gmtoff" and "tm_zone" results from "localtime()" to obtain
  timezone information.

Ver también:

  Modulo "datetime"
     Más interfaz orientada a objetos para fechas y horas.

  Modulo "locale"
     Servicios de internacionalización. La configuración regional
     afecta la interpretación de muchos especificadores de formato en
     "strftime()" y "strptime()".

  Modulo "calendar"
     Funciones generales relacionadas con el calendario. "timegm()" es
     el inverso de "gmtime()" de este módulo.

-[ Notas al pie ]-

[1] The use of "%Z" is now deprecated, but the "%z" escape that
    expands to the preferred hour/minute offset is not supported by
    all ANSI C libraries. Also, a strict reading of the original 1982
    **RFC 822** standard calls for a two-digit year ("%y" rather than
    "%Y"), but practice moved to 4-digit years long before the year
    2000.  After that, **RFC 822** became obsolete and the 4-digit
    year has been first recommended by **RFC 1123** and then mandated
    by **RFC 2822**, with **RFC 5322** continuing this requirement.
