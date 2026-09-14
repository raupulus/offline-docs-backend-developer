---
title: Formatos soportados de tiempo y fechas
source_url: https://www.php.net/manual/es/datetime.formats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/formats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10930
---

## Formatos soportados de tiempo y fechas

Esta sección describe, en un formato de tipo BNF, todos los formatos diferentes que el analizador de `DateTimeImmutable`, `DateTime`, `date_create_immutable`, `date_create`, `date_parse`, y `strtotime` es capaz de comprender. Los formatos están agrupados por secciones. En la mayoría de los casos, los formatos de secciones diferentes, separados por caracteres de espacio en blanco, comas o puntos, pueden ser utilizados en la misma cadena fecha/hora. Para cada formato soportado, se dan uno o varios ejemplos así como una descripción del formato correspondiente. Los caracteres entre comillas simples para los formatos son insensibles a la mayúscula/minúscula (`'t'` podría escribirse `t` o `T`), los caracteres escritos entre comillas dobles, ellos, son sensibles a la mayúscula/minúscula (`"T"` y solo `T`).

Para formatear objetos `DateTimeImmutable` y `DateTime`, por favor refiérase a la documentación del método `DateTimeInterface::format`.

Un conjunto de reglas generales debería ser tenido en cuenta.

1.  El analizador, permite a cada unidad (año, mes, día, hora, minuto, segundo) el rango completo de valores. Para un año son solo 4 dígitos, para un mes es 0-12, para un día 0-31 y para la hora y los minutos es 0-59.

2.  60 es permitido para los segundos, ya que a veces cadenas de fechas con este segundo intercalar aparecen. Pero PHP implementa el tiempo Unix donde "60" no es un número de segundos válido y, por tanto, desborda.

3.  `strtotime` devuelve `false` si un número está fuera del rango, y `DateTimeImmutable::__construct` lanza una excepción.

4.  Si una cadena contiene una fecha, todos los elementos son puestos a 0.

5.  Todos los elementos de tiempo menos significativos son puestos a 0 si cualquier elemento de un tiempo está presente en la cadena dada.

6.  El analizador es tonto, y no efectúa verificación para hacerlo más rápido (y más genérico).

7.  Además de las reglas aplicables a los elementos temporales individuales, el analizador comprende también [formatos compuestos](#datetime.formats.compound) más específicos, tales como el análisis de timestamps Unix (`@1690388256`) y fechas semanales ISO (`2008-W28-3`).

8.  Hay una verificación adicional si una fecha inválida es proporcionada:

```php
    <?php
    $res = date_parse("2015-09-31");
    var_dump($res["warnings"]);

         
    ```

    El ejemplo anterior mostrará:

        array(1) {
          [11] =>
          string(27) "The parsed date was invalid"
        }

9.  Es ya posible manejar estos casos especiales, pero el uso de `DateTimeImmutable::createFromFormat` es requerido proporcionando el formato deseado.

```php
    <?php
    $res = DateTimeImmutable::createFromFormat("Y-m-d", "2015-09-34");
    var_dump($res);

         
    ```

    El ejemplo anterior mostrará:

        object(DateTimeImmutable)#1 (3) {
          ["date"] =>
          string(26) "2015-10-04 17:24:43.000000"
          ["timezone_type"] =>
          int(3)
          ["timezone"] =>
          string(13) "Europe/London"
        }

## Formatos para los tiempos (Time)

Esta página describe los diferentes formatos en una sintaxis de tipo BNF que los analizadores de `DateTimeImmutable`, `DateTime`, `date_create`, `date_create_immutable`, y `strtotime` comprenden.

Para formatear objetos `DateTimeImmutable` y `DateTime`, por favor refiérase a la documentación del método `DateTimeInterface::format`.

| Descripción | Formatos | Ejemplos |
|----|----|----|
| `frac` | . \[0-9\]+ | ".21342", ".85" |
| `hh` | "0"?\[1-9\] \| "1"\[0-2\] | "04", "7", "12" |
| `HH` | \[01\]\[0-9\] \| "2"\[0-4\] | "04", "07", "19" |
| `meridiem` | \[AaPp\] .? \[Mm\] .? \[\0\t \] | "A.m.", "pM", "am." |
| `MM` | \[0-5\]\[0-9\] | "00", "12", "59" |
| `II` | \[0-5\]\[0-9\] | "00", "12", "59" |
| `espacio` | \[ \t\] |  |
| `tz` | "("? \[A-Za-z\]{1,6} ")"? \| \[A-Z\]\[a-z\]+(\[\_/\]\[A-Z\]\[a-z\]+)+ | "CEST", "Europe/Amsterdam", "America/Indiana/Knox" |
| `tzcorrection` | "GMT"? \[+-\] `hh` ":"? `MM`? | "+0400", "GMT-07:00", "-07:00" |

Símbolos utilizados

| Descripción | Formato | Ejemplos |
|----|----|----|
| Horas solas, con meridiem | `hh` `espacio`? `meridiem` | "4 am", "5PM" |
| Horas y minutos, con meridiem | `hh` \[.:\] `MM` `espacio`? `meridiem` | "4:08 am", "7:19P.M." |
| Horas, minutos y segundos con meridiem | `hh` \[.:\] `MM` \[.:\] `II` `espacio`? `meridiem` | "4:08:37 am", "7:19:19P.M." |
| MS SQL (Horas, minutos, segundos y fracción con meridiem) | `hh` ":" `MM` ":" `II` \[.:\] \[0-9\]+ `meridiem` | "4:08:39:12313am" |

Notación de 12 horas

| Descripción | Formato | Ejemplos |
|----|----|----|
| Horas y minutos | 't'? `HH` \[.:\] `MM` | "04:08", "19.19", "T23:43" |
| Horas y minutos, sin dos puntos | 't'? `HH` `MM` | "0408", "t1919", "T2343" |
| Horas, minutos y segundos | 't'? `HH` \[.:\] `MM` \[.:\] `II` | "04.08.37", "t19:19:19" |
| Horas, minutos y segundos, sin dos puntos | 't'? `HH` `MM` `II` | "040837", "T191919" |
| Horas, minutos, segundos y zona horaria | 't'? `HH` \[.:\] `MM` \[.:\] `II` `espacio`? ( `tzcorrection` \| `tz` ) | "040837CEST", "T191919-0700" |
| Horas, minutos, segundos y fracción | 't'? `HH` \[.:\] `MM` \[.:\] `II` `frac` | "04.08.37.81412", "19:19:19.532453" |
| Información de zona horaria | `tz` \| `tzcorrection` | "CEST", "Europe/Amsterdam", "+0430", "GMT-06:00" |

Notación de 24 horas

## Formatos de fechas

Esta página describe los diferentes formatos en una sintaxis de tipo BNF que los analizadores de `DateTimeImmutable`, `DateTime`, `date_create`, `date_create_immutable`, y `strtotime` comprenden.

Para formatear objetos `DateTimeImmutable` y `DateTime`, por favor refiérase a la documentación del método `DateTimeInterface::format`.

| Descripción | Formato | Ejemplos |
|----|----|----|
| `sufijo de días` | "st" \| "nd" \| "rd" \| "th" |  |
| `dd` | (\[0-2\]?\[0-9\] \| "3"\[01\]) `daysuf`? | "7th", "22nd", "31" |
| `DD` | "0" \[0-9\] \| \[1-2\]\[0-9\] \| "3" \[01\] | "07", "31" |
| `m` | 'january' \| 'february' \| 'march' \| 'april' \| 'may' \| 'june' \| 'july' \| 'august' \| 'september' \| 'october' \| 'november' \| 'december' \| 'jan' \| 'feb' \| 'mar' \| 'apr' \| 'may' \| 'jun' \| 'jul' \| 'aug' \| 'sep' \| 'sept' \| 'oct' \| 'nov' \| 'dec' \| "I" \| "II" \| "III" \| "IV" \| "V" \| "VI" \| "VII" \| "VIII" \| "IX" \| "X" \| "XI" \| "XII" |  |
| `M` | 'jan' \| 'feb' \| 'mar' \| 'apr' \| 'may' \| 'jun' \| 'jul' \| 'aug' \| 'sep' \| 'sept' \| 'oct' \| 'nov' \| 'dec' |  |
| `mm` | "0"? \[0-9\] \| "1"\[0-2\] | "0", "04", "7", "12" |
| `MM` | "0" \[0-9\] \| "1"\[0-2\] | "00", "04", "07", "12" |
| `y` | \[0-9\]{1,4} | "00", "78", "08", "8", "2008" |
| `yy` | \[0-9\]{2} | "00", "08", "78" |
| `YY` | \[0-9\]{4} | "2000", "2008", "1978" |
| `YYY` | \[0-9\]{5,19} | "81412", "20192" |

Símbolos utilizados

| Descripción | Ejemplos |
|----|----|
| ATOM | "2022-06-02T16:58:35+00:00" |
| COOKIE | "Thursday, 02-Jun-2022 16:58:35 UTC" |
| ISO8601 | "2022-06-02T16:58:35+0000" |
| [RFC 822](https://datatracker.ietf.org/doc/html/rfc822) | "Thu, 02 Jun 22 16:58:35 +0000" |
| [RFC 850](https://datatracker.ietf.org/doc/html/rfc850) | "Thursday, 02-Jun-22 16:58:35 UTC" |
| [RFC 1036](https://datatracker.ietf.org/doc/html/rfc1036) | "Thu, 02 Jun 22 16:58:35 +0000" |
| [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123) | "Thu, 02 Jun 2022 16:58:35 +0000" |
| [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) | "Thu, 02 Jun 2022 16:58:35 +0000" |
| [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) | "2022-06-02T16:58:35+00:00" |
| [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) Extended | "2022-06-02T16:58:35.698+00:00" |
| [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231) | "Thu, 02 Jun 2022 16:58:35 GMT" |
| RSS | "Thu, 02 Jun 2022 16:58:35 +0000" |
| W3C | "2022-06-02T16:58:35+00:00" |

Formatos estándar

| Descripción | Formato | Ejemplos |
|----|----|----|
| Mes americano y día | `mm` "/" `dd` | "5/12", "10/27" |
| Mes americano, día y año | `mm` "/" `dd` "/" `y` | "12/22/78", "1/17/2006", "1/17/6" |
| Año de cuatro dígitos, mes y día con slashes | `YY` "/" `mm` "/" `dd` | "2008/6/30", "1978/12/22" |
| Año de cuatro dígitos y mes (GNU) | `YY` "-" `mm` | "2008-6", "2008-06", "1978-12" |
| Año, mes y día con guiones | `y` "-" `mm` "-" `dd` | "2008-6-30", "78-12-22", "8-6-21" |
| Día, mes y año de dos dígitos, con puntos, tabulaciones o guiones | `dd` \[.\t-\] `mm` \[.-\] `YY` | "30-6-2008", "22.12.1978" |
| Día, mes y año de dos dígitos, con puntos o tabulaciones | `dd` \[.\t\] `mm` "." `yy` | "30.6.08", "22\t12.78" |
| Día, mes textual y año | `dd` (\[ \t.-\])\* `m` (\[ \t.-\])\* `y` | "30-June 2008", "22DEC78", "14 III 1879" |
| Mes textual y año de cuatro dígitos (el día será el 1) | `m` (\[ \t.-\])\* `YY` | "June 2008", "DEC1978", "March 1879" |
| Año de cuatro dígitos y mes textual (el día será el 1) | `YY` (\[ \t.-\])\* `m` | "2008 June", "1978-XII", "1879.MArCH" |
| Mes textual, día y año | `m` (\[ .\t-\])\* `dd` \[,.stndrh\t \]+ `y` | "July 1st, 2008", "April 17, 1790", "May.9,78" |
| Mes textual y día | `m` (\[ .\t-\])\* `dd` \[,.stndrh\t \]\* | "July 1st,", "Apr 17", "May.9" |
| Día y mes textual | `dd` (\[ .\t-\])\* `m` | "1 July", "17 Apr", "9.May" |
| Mes abreviado, día y año | `M` "-" `DD` "-" `y` | "May-09-78", "Apr-17-1790" |
| Año, mes abreviado y día | `y` "-" `M` "-" `DD` | "78-Dec-22", "1814-MAY-17" |
| Año (y solo el año) | `YY` | "1978", "2008" |
| Año (desarrollado, 5-19 dígitos con signo) | \[+-\] `YYY` | "-81120", "+20192" |
| Mes textual (y solo el mes) | `m` | "March", "jun", "DEC" |

Notaciones localizadas

| Descripción | Formato | Ejemplos |
|----|----|----|
| Año, mes y día de ocho dígitos | `YY` `MM` `DD` | "15810726", "19780417", "18140517" |
| Año de cuatro dígitos, mes y día con slashes | `YY` "/" `MM` "/" `DD` | "2008/06/30", "1978/12/22" |
| Año de dos dígitos, mes y día con guiones | `yy` "-" `MM` "-" `DD` | "08-06-30", "78-12-22" |
| Año de cuatro dígitos con signo opcional, mes y día | \[+-\]? `YY` "-" `MM` "-" `DD` | "-0002-07-26", "+1978-04-17", "1814-05-17" |
| Año de cinco dígitos con signo, mes y día requeridos | \[+-\] `YYY` "-" `MM` "-" `DD` | "-81120-02-26", "+20192-04-17" |

Notaciones ISO8601

> [!NOTE]
> Para los formatos `y` y `yy`, los años antes de 100 son considerados de una manera especial cuando los símbolos `y` o `yy` son utilizados. Si el año está entre 0 (inclusivo) y 69 (inclusivo), 2000 será añadido. Si el año está entre 70 (inclusivo) y 99 (inclusivo) entonces 1900 será añadido. Esto significa que "00-01-01" es interpretado como "2000-01-01".

> [!NOTE]
> El formato "Día, mes y año de dos dígitos con tabulaciones o puntos" (`dd` \[.\t\] `mm` "." `yy`) solo funciona para valores de año de 61 (inclusivo) a 99 (inclusivo) - fuera de estos límites, el *formato de tiempo* "`HH` \[.:\] `MM` \[.:\] `SS`" tiene una precedencia más fuerte y prima.

> [!NOTE]
> El formato "Año (y solo el año)" solo funciona de manera fiable si una cadena de tiempo ya ha sido encontrada. De lo contrario, si el año de cuatro dígitos coincide con `HH` `MM`, estos dos elementos de fecha son definidos en su lugar.
>
> Para analizar de manera coherente solo un año, utilice `DateTimeImmutable::createFromFormat` con el especificador `Y`.

> [!CAUTION]
> Es posible añadir o restar un préstamo para los formatos `dd` y `DD`. El día 0 significa el último día del mes anterior, los préstamos positivos contarán el mes siguiente. Así, "2008-08-00" es equivalente a "2008-07-31" y "2008-06-31" es equivalente a "2008-07-01" (junio solo tiene 30 días).
>
> Es de notar que el rango de día está limitado a 0-31 como indicado por la expresión regular anterior. Así, "2008-06-32" no es una cadena de fecha válida, por ejemplo.
>
> También es posible jugar con los préstamos de los formatos `mm` y `MM` gracias al valor 0. Un valor de mes de 0 significa Diciembre del año anterior. Por ejemplo "2008-00-22" es equivalente a "2007-12-22".
>
> Si combina las dos nociones anteriores y utiliza un préstamo negativo en el día y el mes, entonces ocurre esto: "2008-00-00" es convertido primero hacia "2007-12-00" luego hacia "2007-11-30". Esto también ocurre con la cadena "0000-00-00" que es entonces transformada hacia "-0001-11-30" (el año -1 en el calendario ISO 8601, que es 2 BC en el calendario Gregoriano).

## Formatos compuestos

Esta página describe los diferentes formatos en una sintaxis de tipo BNF que los analizadores de `DateTimeImmutable`, `DateTime`, `date_create`, `date_create_immutable`, y `strtotime` comprenden.

Para formatear objetos `DateTimeImmutable` y `DateTime`, por favor refiérase a la documentación del método `DateTimeInterface::format`.

| Descripción | Formatos | Ejemplos |
|----|----|----|
| `DD` | "0" \[0-9\] \| \[1-2\]\[0-9\] \| "3" \[01\] | "02", "12", "31" |
| `doy` | "00"\[1-9\] \| "0"\[1-9\]\[0-9\] \| \[1-2\]\[0-9\]\[0-9\] \| "3"\[0-5\]\[0-9\] \| "36"\[0-6\] | "001", "012", "180", "350", "366" |
| `frac` | . \[0-9\]+ | ".21342", ".85" |
| `hh` | "0"?\[1-9\] \| "1"\[0-2\] | "04", "7", "12" |
| `HH` | \[01\]\[0-9\] \| "2"\[0-4\] | "04", "07", "19" |
| `meridiem` | \[AaPp\] .? \[Mm\] .? \[\0\t \] | "A.m.", "pM", "am." |
| `ii` | \[0-5\]?\[0-9\] | "04", "8", "59" |
| `II` | \[0-5\]\[0-9\] | "04", "08", "59" |
| `M` | 'jan' \| 'feb' \| 'mar' \| 'apr' \| 'may' \| 'jun' \| 'jul' \| 'aug' \| 'sep' \| 'sept' \| 'oct' \| 'nov' \| 'dec' |  |
| `MM` | \[0-1\]\[0-9\] | "00", "12" |
| `espacio` | \[ \t\] |  |
| `ss` | (\[0-5\]?\[0-9\])\|60 | "04", "8", "59", "60" (segundo intercalar) |
| `SS` | \[0-5\]\[0-9\] | "04", "08", "59" |
| `W` | "0"\[1-9\] \| \[1-4\]\[0-9\] \| "5"\[0-3\] | "05", "17", "53" |
| `tzcorrection` | "GMT"? \[+-\] `hh` ":"? `II`? | "+0400", "GMT-07:00", "-07:00" |
| `YY` | \[0-9\]{4} | "2000", "2008", "1978" |

Símbolos utilizados

| Descripción | Formato | Ejemplos |
|----|----|----|
| Formato de log común | `dd` "/" `M` "/" `YY` : `HH` ":" `II` ":" `SS` `espacio` `tzcorrection` | "10/Oct/2000:13:55:36 -0700" |
| EXIF | `YY` ":" `MM` ":" `DD` " " `HH` ":" `II` ":" `SS` | "2008:08:07 18:11:31" |
| Año ISO con semana ISO | `YY` "-"? "W" `W` | "2008W27", "2008-W28" |
| Año ISO con semana ISO y día | `YY` "-"? "W" `W` "-"? \[0-7\] | "2008W273", "2008-W28-3" |
| MySQL | `YY` "-" `MM` "-" `DD` " " `HH` ":" `II` ":" `SS` | "2008-08-07 18:11:31" |
| PostgreSQL: Año con día del año | `YY` "."? `doy` | "2008.197", "2008197" |
| SOAP | `YY` "-" `MM` "-" `DD` "T" `HH` ":" `II` ":" `SS` `frac` `tzcorrection`? | "2008-07-01T22:35:17.02", "2008-07-01T22:35:17.03+08:00" |
| Timestamp Unix | "@" "-"? \[0-9\]+ | "@1215282385" |
| Timestamp Unix con microsegundos | "@" "-"? \[0-9\]+ "." \[0-9\]{0,6} | "@1607974647.503686" |
| XMLRPC | `YY` `MM` `DD` "T" `hh` ":" `II` ":" `SS` | "20080701T22:38:07", "20080701T9:38:07" |
| XMLRPC (Compacto) | `YY` `MM` `DD` 't' `hh` `II` `SS` | "20080701t223807", "20080701T093807" |
| WDDX | `YY` "-" `mm` "-" `dd` "T" `hh` ":" `ii` ":" `ss` | "2008-7-1T9:3:37" |

Notaciones localizadas

> [!NOTE]
> El "W" en los formatos "Año ISO con semana ISO" y "Año ISO con semana ISO y día" es sensible a la mayúscula/minúscula; solo puede utilizarse la mayúscula "W".
>
> El "T" en los formatos SOAP, XMRPC y WDDX es sensible a la mayúscula/minúscula; utilice siempre la mayúscula "T".
>
> El formato timestamp Unix define la zona horaria a UTC.

## Formatos relativos

Esta página describe los diferentes formatos en una sintaxis de tipo BNF que los analizadores de `DateTimeImmutable`, `DateTime`, `date_create`, `date_create_immutable`, y `strtotime` comprenden.

Para formatear objetos `DateTimeImmutable` y `DateTime`, por favor refiérase a la documentación del método `DateTimeInterface::format`.

| Descripción | Formato |
|----|----|
| `dayname` | 'sunday' \| 'monday' \| 'tuesday' \| 'wednesday' \| 'thursday' \| 'friday' \| 'saturday' \| 'sun' \| 'mon' \| 'tue' \| 'wed' \| 'thu' \| 'fri' \| 'sat' |
| `daytext` | 'weekday' \| 'weekdays' |
| `number` | \[+-\]?\[0-9\]+ |
| `ordinal` | 'first' \| 'second' \| 'third' \| 'fourth' \| 'fifth' \| 'sixth' \| 'seventh' \| 'eighth' \| 'ninth' \| 'tenth' \| 'eleventh' \| 'twelfth' \| 'next' \| 'last' \| 'previous' \| 'this' |
| `reltext` | 'next' \| 'last' \| 'previous' \| 'this' |
| `espacio` | \[ \t\]+ |
| `unit` | 'ms' \| 'µs' \| (( 'msec' \| 'millisecond' \| 'µsec' \| 'microsecond' \| 'usec' \| 'sec' \| 'second' \| 'min' \| 'minute' \| 'hour' \| 'day' \| 'fortnight' \| 'forthnight' \| 'month' \| 'year') 's'?) \| 'weeks' \| `daytext` |

Símbolos utilizados

| Formato | Descripción | Ejemplos |
|----|----|----|
| 'yesterday' | Medianoche de ayer | "yesterday 14:00" |
| 'midnight' | El tiempo es puesto a 00:00:00 |  |
| 'today' | El tiempo es puesto a 00:00:00 |  |
| 'now' | Ahora |  |
| 'noon' | El tiempo es puesto a 12:00:00 | "yesterday noon" |
| 'tomorrow' | Medianoche de mañana |  |
| 'back of' `hour` | 15 minutos antes de la hora especificada | "back of 7pm", "back of 15" |
| 'front of' `hour` | 15 minutos después de la hora especificada | "front of 5am", "front of 23" |
| 'first day of'? | Asigna el día del primer día del mes actual. Generalmente es preferible utilizar esta expresión con el nombre del mes que sigue, ya que solo se refiere al mes actual. | "first day of January 2008" |
| 'last day of'? | Asigna el día del último día del mes actual. Generalmente es preferible utilizar esta expresión con el nombre del mes que sigue, ya que solo se refiere al mes actual. | "last day of next month" |
| `ordinal` `espacio` `dayname` `espacio` 'of' | Calcula el `x`-ésimo día de la semana del mes actual. | "first sat of July 2008" |
| 'last' `espacio` `dayname` `espacio` 'of' | Calcula el *último* día de la semana del mes actual. | "last sat of July 2008" |
| `number` `espacio`? (`unit` \| 'week') | Maneja tiempos relativos cuyo valor es numerado. | "+5 weeks", "12 day", "-7 weekdays" |
| (`ordinal` \| `reltext`) `espacio` `unit` | Maneja elementos temporales relativos cuyo valor es textual. `last` y `previous` son equivalentes a `-1`, `this` a 0, y `next` a `+1`. | "fifth day", "second month", "last day", "previous year" |
| 'ago' | Utiliza en el pasado cualquier descripción de tiempo relativo ('hace'). | "2 days ago", "8 days ago 14:00", "2 months 5 days ago", "2 months ago 5 days", "2 days ago" |
| `dayname` | Se mueve hacia el próximo día indicado.(Ver [nota](#datetime.formats.relative.dayname-note)) | "Monday" |
| `reltext` `espacio` 'week' | Maneja el formato especial "weekday + last/this/next week". | "Monday next week" |

Notaciones basadas en el día

> [!NOTE]
> Las expresiones relativas son siempre tratadas *después* de las expresiones no relativas. Esto hace que "+1 week july 2008" y "july 2008 +1 week" sean equivalentes.
>
> "yesterday", "midnight", "today", "noon" y "tomorrow" son excepciones a esta regla. Note que "tomorrow 11:00" y "11:00 tomorrow" son diferentes. Si la fecha de hoy es "July 23rd, 2008", la primera expresión da "2008-07-24 11:00" mientras que la segunda dará "2008-07-24 00:00". La razón es que estas cinco expresiones influyen directamente en la fecha actual.
>
> Las palabras clave como "first day of" dependen del contexto en el cual la cadena de formato relativo es utilizada. Si se utiliza con un método estático o una función, el referente es el timestamp actual del sistema. Sin embargo, si se utiliza en `DateTime::modify` o `DateTimeImmutable::modify`, el referente es el objeto sobre el cual el método `modify()` es llamado.

> [!NOTE]
> Note las observaciones que siguen cuando el día de la semana actual es el mismo que el día de la semana utilizado en la cadena fecha/hora. El día de la semana actual podría haber sido recalculado con respecto a las partes no relativas de la cadena fecha/hora.
>
> 1.  "`dayname`" no avanza *hacia* otro día. (Ejemplo: "Wed July 23rd, 2008" significa "2008-07-23").
>
> 2.  "`number` `dayname`" no avanza *hacia* otro día. (Ejemplo: "1 wednesday july 23rd, 2008" significa "2008-07-23").
>
> 3.  "`number` week `dayname`" añadirá primero el número de semanas, pero no avanzará *hacia* otro día. En este caso "`number` week" y "`dayname`" son dos bloques distintos. (Ejemplo: "+1 week wednesday july 23rd, 2008" significa "2008-07-30").
>
> 4.  "`ordinal` `dayname`" *avanza* hacia otro día. (Ejemplo: "first wednesday july 23rd, 2008" significa "2008-07-30").
>
> 5.  "`number` week `ordinal` `dayname`" añadirá primero el número de semanas y luego *avanzará* hacia otro día. En este caso, "`number` week" y "`ordinal` `dayname`" son dos bloques distintos. (Ejemplo: "+1 week first wednesday july 23rd, 2008" significa "2008-08-06").
>
> 6.  "`ordinal` `dayname` 'of' " no avanza *hacia* otro día. (Ejemplo: "first wednesday of july 23rd, 2008" significa "2008-07-02" ya que la frase con 'of' resetea el día del mes hacia '1' y el '23' será ignorado).
>
> Note también que el "of" en "`ordinal` `espacio` `dayname` `espacio` 'of' " y "'last' `espacio` `dayname` `espacio` 'of' " hace algo especial.
>
> 1.  Asigna el día del mes a 1.
>
> 2.  "`ordinal` `dayname` 'of' " no avanza *hacia* otro día. (Ejemplo: "first tuesday of july 2008" significa "2008-07-01").
>
> 3.  "`ordinal` `dayname` " *avanza* hacia otro día. (Ejemplo: "first tuesday july 2008" significa "2008-07-08", ver también el punto número 4 de la lista anterior).
>
> 4.  "'last' `dayname` 'of' " toma el último `dayname` del mes actual. (Ejemplo: "last wed of july 2008" significa "2008-07-30")
>
> 5.  "'last' `dayname`" toma el último `dayname` a partir del día actual. (Ejemplo: "last wed july 2008" significa "2008-06-25"; "july 2008" asigna primero la fecha actual a "2008-07-01" y luego "last wed" retrocede al último miércoles que es el "2008-06-25").

> [!NOTE]
> Los valores relativos de los meses calculados se basan en el número de días de los meses que se utilizan. Por ejemplo, "+2 month 2011-11-30", dará como resultado la fecha "2012-01-30". Esto se debe a que el mes de noviembre tiene 30 días, y que el mes de diciembre tiene 31, lo que suma un total de 61 días.

> [!NOTE]
> `number` es un número *entero*; si un número decimal es dado, el punto (o la coma) será probablemente interpretado como un delimitador. Por ejemplo, `'+1.5 hours'` será analizado como `'+1 5 hours'`, y no como `'+1 hour +30 minutes'`.

### Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `number` ahora acepta un signo más seguido de un signo menos, por ejemplo `+-2`, y otras combinaciones de varios signos. |
| 8.2.0 | `number` ya no acepta un signo más seguido de un signo menos, ejemplo `+-2`. |
| 7.0.8 | Las semanas siempre comienzan el lunes. Antes, el domingo también era considerado para comenzar una semana. |
