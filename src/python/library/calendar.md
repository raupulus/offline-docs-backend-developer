---
title: '"calendar" --- General calendar-related functions'
source_url: https://docs.python.org/es/3
source_path: library/calendar.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1890
---

# "calendar" --- General calendar-related functions

**Código fuente:** Lib/calendar.py

======================================================================

Este módulo te permite generar calendarios como el programa Unix
**cal**, y proporciona funciones útiles adicionales relacionadas con
el calendario. Por defecto, estos calendarios tienen el lunes como el
primer día de la semana, y el domingo como el último (la convención
europea). Use "setfirstweekday()" para establecer el primer día de la
semana en domingo (6) o en cualquier otro día de la semana. Los
parámetros que especifican fechas se indican como enteros. Para la
funcionalidad relacionada, consulta también los módulos "datetime" y
"time".

Las funciones y clases definidas en este módulo utilizan un calendario
idealizado, el calendario gregoriano actual extendido indefinidamente
en ambas direcciones. Esto coincide con la definición del calendario
"Gregoriano proléptico" en el libro "Calendrical Calculations" de
Dershowitz y Reingold, donde es el calendario base para todos los
cálculos. Los años cero y negativos se interpretan según lo prescrito
por la norma ISO 8601. El año 0 es 1 A. C., el año -1 es 2 a. C., y
así sucesivamente.

class calendar.Calendar(firstweekday=0)

   Crea un objeto "Calendar". *firstweekday* es un entero que
   especifica el primer día de la semana. "MONDAY" es "0" (por
   defecto), "SUNDAY" es "6".

   Un objeto "Calendar" proporciona varios métodos que se pueden
   utilizar para preparar los datos del calendario para dar formato.
   Esta clase no hace ningún formato en sí. Este es el trabajo de las
   subclases.

   "Calendar" instances have the following methods and attributes:

   firstweekday

      The first weekday as an integer (0--6).

      This property can also be set and read using "setfirstweekday()"
      and "getfirstweekday()" respectively.

   getfirstweekday()

      Return an "int" for the current first weekday (0--6).

      Identical to reading the "firstweekday" property.

   setfirstweekday(firstweekday)

      Set the first weekday to *firstweekday*, passed as an "int" (0--
      6).

      Identical to setting the "firstweekday" property.

   iterweekdays()

      Return an iterator for the weekday numbers that will be used for
      one week.  The first value from the iterator will be the same as
      the value of the "firstweekday" property.

   itermonthdates(year, month)

      Retorna un iterador para el mes *month* (1--12) en el año
      *year*. Este iterador retornará todos los días (como objetos
      "datetime.date") para el mes y todos los días antes del inicio
      del mes o después del final del mes que se requieren para
      obtener una semana completa.

   itermonthdays(year, month)

      Retorna un iterador para el mes *month* en el año *year* similar
      a "itermonthdates()", pero no restringido por el intervalo
      "datetime.date". Los días retornados serán simplemente el día de
      los números del mes. Para los días fuera del mes especificado,
      el número de día es "0".

   itermonthdays2(year, month)

      Return an iterator for the month *month* in the year *year*
      similar to "itermonthdates()", but not restricted by the
      "datetime.date" range. Days returned will be tuples consisting
      of a day of the month number and a weekday number.

   itermonthdays3(year, month)

      Retorna un iterador para el mes *month* del año *year* similar a
      "itermonthdates()", pero no restringido por el rango
      "datetime.date". Los días retornados serán tuplas que consisten
      en un año, un mes y un día del mes.

      Added in version 3.7.

   itermonthdays4(year, month)

      Retorna un iterador para el mes *month* del año *year* similar a
      "itermonthdates()", pero no restringido por el rango
      "datetime.date". Los días retornados serán tuplas que consisten
      en un año, un mes, un día del mes y un día de la semana.

      Added in version 3.7.

   monthdatescalendar(year, month)

      Retorna una lista de las semanas del mes *month* del año *year*
      como semanas completas. Las semanas son listas de siete objetos
      "datetime.date".

   monthdays2calendar(year, month)

      Retorna una lista de las semanas del mes *month* del año *year*
      como semanas completas. Las semanas son listas de siete tuplas
      de números de días y números de días de la semana.

   monthdayscalendar(year, month)

      Retorna una lista de las semanas del mes *month* del año *year*
      como semanas completas. Las semanas son listas de números de
      siete días.

   yeardatescalendar(year, width=3)

      Retorna los datos del año especificado listos para ser
      formateados. El valor de retorno es una lista de filas de mes.
      Cada fila de mes contiene hasta *width* meses (por defecto hasta
      3). Cada mes contiene entre 4 y 6 semanas y cada semana contiene
      1--7 días. Los días son objetos "datetime.date".

   yeardays2calendar(year, width=3)

      Retorna los datos del año especificado listos para ser
      formateados (similar a "yeardatescalendar()"). Las entradas en
      las listas de la semana son tuplas de números de días y números
      de días de la semana. Los números de los días fuera de este mes
      son cero.

   yeardayscalendar(year, width=3)

      Retorna los datos del año especificado listos para ser
      formateados (similar a "yeardatescalendar()"). Las entradas en
      las listas de la semana son números de día. Los números de día
      fuera de este mes son cero.

class calendar.TextCalendar(firstweekday=0)

   Esta clase puede ser usada para generar calendarios de texto
   simple.

   Las instancias de "TextCalendar" tienen los siguientes métodos:

   formatday(theday, weekday, width)

      Return a string representing a single day formatted with the
      given *width*. If *theday* is "0", return a string of spaces of
      the specified width, representing an empty day. The *weekday*
      parameter is unused.

   formatweek(theweek, w=0)

      Return a single week in a string with no newline. If *w* is
      provided, it specifies the width of the date columns, which are
      centered. Depends on the first weekday as specified in the
      constructor or set by the "setfirstweekday()" method.

   formatweekday(weekday, width)

      Return a string representing the name of a single weekday
      formatted to the specified *width*. The *weekday* parameter is
      an integer representing the day of the week, where "0" is Monday
      and "6" is Sunday.

   formatweekheader(width)

      Return a string containing the header row of weekday names,
      formatted with the given *width* for each column. The names
      depend on the locale settings and are padded to the specified
      width.

   formatmonth(theyear, themonth, w=0, l=0)

      Retorna el calendario de un mes en una cadena de varias líneas.
      Si se proporciona *w*, especifica el ancho de las columnas de
      fecha, que están centradas. Si se proporciona *l*, especifica el
      número de líneas que se utilizarán cada semana. Depende del
      primer día de la semana como se especifica en el constructor o
      se establece por el método "setfirstweekday()".

   formatmonthname(theyear, themonth, width=0, withyear=True)

      Return a string representing the month's name centered within
      the specified *width*. If *withyear* is "True", include the year
      in the output. The *theyear* and *themonth* parameters specify
      the year and month for the name to be formatted respectively.

   prmonth(theyear, themonth, w=0, l=0)

      Imprime el calendario de un mes como lo retorna "formatmonth()".

   formatyear(theyear, w=2, l=1, c=6, m=3)

      Retorna un calendario de *m* columnas para todo un año como una
      cadena de varias líneas. Los parámetros opcionales *w*, *l* y
      *c* son para el ancho de la columna de la fecha, las líneas por
      semana y el número de espacios entre las columnas del mes,
      respectivamente. Depende del primer día de la semana como se
      especifica en el constructor o se establece por el método
      "setfirstweekday()". El primer año para el que se puede generar
      un calendario depende de la plataforma.

   pryear(theyear, w=2, l=1, c=6, m=3)

      Imprime el calendario de un año entero como lo retorna
      "formatyear()".

class calendar.HTMLCalendar(firstweekday=0)

   Esta clase puede utilizarse para generar calendarios HTML.

   Las instancias de "HTMLCalendar" tienen los siguientes métodos:

   formatmonth(theyear, themonth, withyear=True)

      Retorna el calendario de un mes como una tabla HTML. Si
      *withyear* es verdadero, el año será incluido en el encabezado,
      de lo contrario sólo se usará el nombre del mes.

   formatyear(theyear, width=3)

      Retorna el calendario de un año como una tabla HTML. *width*
      (por defecto a 3) especifica el número de meses por fila.

   formatyearpage(theyear, width=3, css='calendar.css', encoding=None)

      Retorna el calendario de un año como una página HTML completa.
      *width* (por defecto a 3) especifica el número de meses por
      fila. *css* es el nombre de la hoja de estilo en cascada que se
      debe usar. "None" puede ser pasada si no se debe usar una hoja
      de estilo. *encoding* especifica la codificación a ser usada
      para la salida (por defecto a la codificación por defecto del
      sistema).

   formatmonthname(theyear, themonth, withyear=True)

      Return a month name as an HTML table row. If *withyear* is true
      the year will be included in the row, otherwise just the month
      name will be used.

   "HTMLCalendar" tiene los siguientes atributos que puedes
   sobrescribir para personalizar las clases CSS utilizadas por el
   calendario:

   cssclasses

      Una lista de clases CSS utilizadas para cada día de la semana.
      La lista de clases predeterminada es:

         cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

      se pueden añadir más estilos para cada día:

         cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]

      Ten en cuenta que la longitud de esta lista debe ser de siete
      elementos.

   cssclass_noday

      La clase CSS para un día de la semana que ocurre en el mes
      anterior o siguiente.

      Added in version 3.7.

   cssclasses_weekday_head

      Una lista de clases CSS utilizadas para los nombres de los días
      de la semana en la fila del encabezado. El valor por defecto es
      el mismo que "cssclasses".

      Added in version 3.7.

   cssclass_month_head

      La clase de CSS del mes (usada por "formatmonthname()"). El
      valor por defecto es ""month"".

      Added in version 3.7.

   cssclass_month

      La clase de CSS para la tabla de todo el mes (usada por
      "formatmonth()"). El valor por defecto es ""month"".

      Added in version 3.7.

   cssclass_year

      La clase de CSS para la tabla de tablas de todo el año (usada
      por "formatyear()"). El valor por defecto es ""year"".

      Added in version 3.7.

   cssclass_year_head

      La clase de CSS para el encabezado de la tabla para todo el año
      (usado por "formatyear()"). El valor por defecto es ""year"".

      Added in version 3.7.

   Nótese que aunque la denominación de los atributos de clase
   descritos anteriormente es singular (por ejemplo, "cssclass_month"
   "cssclass_noday"), uno puede reemplazar la clase CSS única con una
   lista de clases CSS separadas por espacios, por ejemplo:

      "text-bold text-red"

   Aquí hay un ejemplo de cómo "HTMLCalendar" puede ser personalizado:

      class CustomHTMLCal(calendar.HTMLCalendar):
          cssclasses = [style + " text-nowrap" for style in
                        calendar.HTMLCalendar.cssclasses]
          cssclass_month_head = "text-center month-head"
          cssclass_month = "text-center month"
          cssclass_year = "text-italic lead"

class calendar.LocaleTextCalendar(firstweekday=0, locale=None)

   Esta subclase de "TextCalendar" se le puede pasar un nombre de
   configuración regional en el constructor y retornará los nombres de
   los meses y días de la semana en la configuración regional
   especificada.

class calendar.LocaleHTMLCalendar(firstweekday=0, locale=None)

   Esta subclase de "HTMLCalendar" se le puede pasar un nombre de
   configuración regional en el constructor y retornará los nombres de
   los meses y días de la semana en la configuración regional
   especificada.

Nota:

  The constructor, "formatweekday()" and "formatmonthname()" methods
  of these two classes temporarily change the "LC_TIME" locale to the
  given *locale*. Because the current locale is a process-wide
  setting, they are not thread-safe.

Para los calendarios de texto simples este módulo proporciona las
siguientes funciones.

calendar.setfirstweekday(firstweekday)

   Establece el día de la semana (el "0" es el lunes, el "6" es el
   domingo) para empezar cada semana. Los valores "MONDAY", "TUESDAY",
   "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", y "SUNDAY" se
   proporcionan por conveniencia. Por ejemplo, para fijar el primer
   día de la semana en domingo:

      import calendar
      calendar.setfirstweekday(calendar.SUNDAY)

calendar.firstweekday()

   Retorna la configuración actual para el día de la semana para
   empezar cada semana.

calendar.isleap(year)

   Retorna "True" si *year* es un año bisiesto, si no "False".

calendar.leapdays(y1, y2)

   Retorna el número de años bisiestos en el rango de *y1* a *y2*
   (exclusivo), donde *y1* y *y2* son años.

   Esta función opera para rangos que abarcan un cambio de siglo.

calendar.weekday(year, month, day)

   Retorna el día de la semana ("0" es lunes) para *year*
   ("1970"--...), *month* ("1"--"12"), *day* ("1"--"31").

calendar.weekheader(width)

   Return a header containing abbreviated weekday names. *width*
   specifies the width in characters for one weekday.

calendar.monthrange(year, month)

   Returns weekday of first day of the month and number of days in
   month, for the specified *year* and *month*.

calendar.monthcalendar(year, month)

   Retorna una matriz que representa el calendario de un mes. Cada
   fila representa una semana; los días fuera del mes se representan
   con ceros. Cada semana comienza con el lunes a menos que lo
   establezca "setfirstweekday()".

calendar.prmonth(theyear, themonth, w=0, l=0)

   Imprime el calendario de un mes según lo retorna "month()".

calendar.month(theyear, themonth, w=0, l=0)

   Returns a month's calendar in a multi-line string using the
   "formatmonth()" of the "TextCalendar" class.

calendar.prcal(theyear, w=0, l=0, c=6, m=3)

   Imprime el calendario de todo un año como lo retorna "calendar()".

calendar.calendar(theyear, w=2, l=1, c=6, m=3)

   Returns a 3-column calendar for an entire year as a multi-line
   string using the "formatyear()" of the "TextCalendar" class.

calendar.timegm(tuple)

   An unrelated but handy function that takes a time tuple such as
   returned by the "gmtime()" function in the "time" module, and
   returns the corresponding Unix timestamp value, assuming an epoch
   of 1970, and the POSIX encoding.  In fact, "time.gmtime()" and
   "timegm()" are each other's inverse.

The "calendar" module exports the following data attributes:

calendar.day_name

   A sequence that represents the days of the week in the current
   locale, where Monday is day number 0.

   >>> import calendar
   >>> list(calendar.day_name)
   ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

calendar.day_abbr

   A sequence that represents the abbreviated days of the week in the
   current locale, where Mon is day number 0.

   >>> import calendar
   >>> list(calendar.day_abbr)
   ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

calendar.MONDAY
calendar.TUESDAY
calendar.WEDNESDAY
calendar.THURSDAY
calendar.FRIDAY
calendar.SATURDAY
calendar.SUNDAY

   Alias para los días de la semana, donde "MONDAY" es "0" y "SUNDAY"
   es "6".

   Added in version 3.12.

class calendar.Day

   Enumeración que define los días de la semana como constantes
   enteras. Los miembros de esta enumeración se exportan al alcance
   del módulo como "MONDAY" hasta "SUNDAY".

   Added in version 3.12.

calendar.month_name

   A sequence that represents the months of the year in the current
   locale.  This follows normal convention of January being month
   number 1, so it has a length of 13 and "month_name[0]" is the empty
   string.

   >>> import calendar
   >>> list(calendar.month_name)
   ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

calendar.month_abbr

   A sequence that represents the abbreviated months of the year in
   the current locale.  This follows normal convention of January
   being month number 1, so it has a length of 13 and  "month_abbr[0]"
   is the empty string.

   >>> import calendar
   >>> list(calendar.month_abbr)
   ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

calendar.JANUARY
calendar.FEBRUARY
calendar.MARCH
calendar.APRIL
calendar.MAY
calendar.JUNE
calendar.JULY
calendar.AUGUST
calendar.SEPTEMBER
calendar.OCTOBER
calendar.NOVEMBER
calendar.DECEMBER

   Alias para los meses del año, donde "JANUARY" es "1" y "DECEMBER"
   es "12".

   Added in version 3.12.

class calendar.Month

   Enumeración que define los meses del año como constantes enteras.
   Los miembros de esta enumeración se exportan al alcance del módulo
   como "JANUARY" hasta "DECEMBER".

   Added in version 3.12.

The "calendar" module defines the following exceptions:

exception calendar.IllegalMonthError(month)

   A subclass of "ValueError" and "IndexError", raised when the given
   month number is outside of the range 1-12 (inclusive).

   Distinto en la versión 3.12: "IllegalMonthError" is now also a
   subclass of "ValueError". New code should avoid catching
   "IndexError".

   month

      El número del mes no válido.

exception calendar.IllegalWeekdayError(weekday)

   Una subclase de "ValueError", que se lanza cuando el número del día
   de la semana proporcionado está fuera del rango 0-6 (inclusive).

   weekday

      El número de día de la semana laborable no válido.

Ver también:

  Módulo "datetime"
     Interfaz orientada a objetos para fechas y horas con una
     funcionalidad similar a la del módulo "time".

  Módulo "time"
     Funciones de bajo nivel relacionadas con el tiempo.

## Command-line usage

Added in version 2.5.

The "calendar" module can be executed as a script from the command
line to interactively print a calendar.

   python -m calendar [-h] [-L LOCALE] [-e ENCODING] [-t {text,html}]
                      [-w WIDTH] [-l LINES] [-s SPACING] [-m MONTHS] [-c CSS]
                      [-f FIRST_WEEKDAY] [year] [month]

Por ejemplo, para imprimir un calendario para el año 2000:

   $ python -m calendar 2000
                                     2000

         January                   February                   March
   Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1  2          1  2  3  4  5  6             1  2  3  4  5
    3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
   10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
   17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
   24 25 26 27 28 29 30      28 29                     27 28 29 30 31
   31

          April                      May                       June
   Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1  2       1  2  3  4  5  6  7                1  2  3  4
    3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
   10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
   17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
   24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

           July                     August                  September
   Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1  2          1  2  3  4  5  6                   1  2  3
    3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
   10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
   17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
   24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
   31

         October                   November                  December
   Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                      1             1  2  3  4  5                   1  2  3
    2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
    9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
   16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
   23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
   30 31

Se aceptan las siguientes opciones:

--help, -h

   Muestra el mensaje de ayuda y salida.

--locale LOCALE, -L LOCALE

   La configuración regional que se utiliza para los nombres de meses
   y días de la semana. El valor predeterminado es inglés.

--encoding ENCODING, -e ENCODING

   La codificación que se utiliza para la salida. Se necesita "--
   encoding" si "--locale" está configurada.

--type {text,html}, -t {text,html}

   Imprime el calendario en la terminal como texto o como un documento
   HTML.

--first-weekday FIRST_WEEKDAY, -f FIRST_WEEKDAY

   The weekday to start each week. Must be a number between 0 (Monday)
   and 6 (Sunday). Defaults to 0.

   Added in version 3.13.

year

   The year to print the calendar for. Defaults to the current year.

month

   El mes de "year" especificado para imprimir el calendario. Debe ser
   un número entre 1 y 12 y sólo se puede usar en modo texto. El valor
   predeterminado es imprimir un calendario para el año completo.

*Opciones de modo texto:*

--width WIDTH, -w WIDTH

   El ancho de la columna de fecha en las columnas terminales. La
   fecha se imprime centrada en la columna. Cualquier valor inferior a
   2 se ignora. El valor predeterminado es 2.

--lines LINES, -l LINES

   El número de líneas para cada semana en filas terminales. La fecha
   se imprime alineada en la parte superior. Cualquier valor inferior
   a 1 se ignora. El valor predeterminado es 1.

--spacing SPACING, -s SPACING

   El espacio entre meses en columnas. Cualquier valor inferior a 2 se
   ignora. El valor predeterminado es 6.

--months MONTHS, -m MONTHS

   El número de meses se imprimen por fila. El valor predeterminado es
   3.

Distinto en la versión 3.14: By default, today's date is highlighted
in color and can be controlled using environment variables.

*Opciones de modo HTML:*

--css CSS, -c CSS

   La ruta de una hoja de estilos CSS que se utiliza para el
   calendario. Esta debe ser relativa al HTML generado, o un HTTP
   absoluto o una URL "file:///".
