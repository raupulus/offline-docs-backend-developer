---
title: La classe IntlCalendar
source_url: https://www.php.net/manual/es/class.intlcalendar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1f68eecaa
order: 40670
---

## Introducción

## Sinopsis de la clase

IntlCalendar

Constantes

public

const

int

IntlCalendar::FIELD_ERA

public

const

int

IntlCalendar::FIELD_YEAR

public

const

int

IntlCalendar::FIELD_MONTH

public

const

int

IntlCalendar::FIELD_WEEK_OF_YEAR

public

const

int

IntlCalendar::FIELD_WEEK_OF_MONTH

public

const

int

IntlCalendar::FIELD_DATE

public

const

int

IntlCalendar::FIELD_DAY_OF_YEAR

public

const

int

IntlCalendar::FIELD_DAY_OF_WEEK

public

const

int

IntlCalendar::FIELD_DAY_OF_WEEK_IN_MONTH

public

const

int

IntlCalendar::FIELD_AM_PM

public

const

int

IntlCalendar::FIELD_HOUR

public

const

int

IntlCalendar::FIELD_HOUR_OF_DAY

public

const

int

IntlCalendar::FIELD_MINUTE

public

const

int

IntlCalendar::FIELD_SECOND

public

const

int

IntlCalendar::FIELD_MILLISECOND

public

const

int

IntlCalendar::FIELD_ZONE_OFFSET

public

const

int

IntlCalendar::FIELD_DST_OFFSET

public

const

int

IntlCalendar::FIELD_YEAR_WOY

public

const

int

IntlCalendar::FIELD_DOW_LOCAL

public

const

int

IntlCalendar::FIELD_EXTENDED_YEAR

public

const

int

IntlCalendar::FIELD_JULIAN_DAY

public

const

int

IntlCalendar::FIELD_MILLISECONDS_IN_DAY

public

const

int

IntlCalendar::FIELD_IS_LEAP_MONTH

public

const

int

IntlCalendar::FIELD_FIELD_COUNT

public

const

int

IntlCalendar::FIELD_DAY_OF_MONTH

public

const

int

IntlCalendar::DOW_SUNDAY

public

const

int

IntlCalendar::DOW_MONDAY

public

const

int

IntlCalendar::DOW_TUESDAY

public

const

int

IntlCalendar::DOW_WEDNESDAY

public

const

int

IntlCalendar::DOW_THURSDAY

public

const

int

IntlCalendar::DOW_FRIDAY

public

const

int

IntlCalendar::DOW_SATURDAY

public

const

int

IntlCalendar::DOW_TYPE_WEEKDAY

public

const

int

IntlCalendar::DOW_TYPE_WEEKEND

public

const

int

IntlCalendar::DOW_TYPE_WEEKEND_OFFSET

public

const

int

IntlCalendar::DOW_TYPE_WEEKEND_CEASE

public

const

int

IntlCalendar::WALLTIME_FIRST

public

const

int

IntlCalendar::WALLTIME_LAST

public

const

int

IntlCalendar::WALLTIME_NEXT_VALID

Métodos

## Constantes predefinidas

`IntlCalendar::FIELD_ERA` `int`  
El campo de calendario que representa numéricamente una era, por ejemplo `1` para AD y `0` para BC en los calendarios gregoriano/juliano y `235` para la era Heisei (平成) en el calendario japonés. No todos los calendarios tienen más de una era.

`IntlCalendar::FIELD_YEAR` `int`  
El campo de calendario para el año. Esto no es único a través de las eras. Si el tipo de calendario tiene más de una era, generalmente el valor mínimo para este campo será `1`.

`IntlCalendar::FIELD_MONTH` `int`  
El campo de calendario para el mes. La secuencia de los meses comienza en cero, por lo que enero (aquí utilizado para significar el primer mes del calendario; esto puede tener otro nombre, como Muharram en el calendario islámico) está representado por `0`, febrero por `1`, …, diciembre por `11` y, para los calendarios que lo tienen, el 13º o mes bis por `12`.

`IntlCalendar::FIELD_WEEK_OF_YEAR` `int`  
El campo de calendario para el número de la semana del año. Esto depende del día de la semana que se [considere como el inicio de la semana](#intlcalendar.getfirstdayofweek) y del [número mínimo de días en una semana](#intlcalendar.getminimaldaysinfirstweek).

`IntlCalendar::FIELD_WEEK_OF_MONTH` `int`  
El campo de calendario para el número de la semana del mes. Esto depende del día de la semana que se [considere como el inicio de la semana](#intlcalendar.getfirstdayofweek) y del [número mínimo de días en una semana](#intlcalendar.getminimaldaysinfirstweek).

`IntlCalendar::FIELD_DATE` `int`  
El campo de calendario para el día del mes. Idéntico a `IntlCalendar::FIELD_DAY_OF_MONTH`, que tiene un nombre más claro.

`IntlCalendar::FIELD_DAY_OF_YEAR` `int`  
El campo de calendario para el día del año. Para el calendario gregoriano, comienza en `1` y termina en `365` o `366`.

`IntlCalendar::FIELD_DAY_OF_WEEK` `int`  
El campo de calendario para el día de la semana. Sus valores comienzan en `1` (domingo, ver [`IntlCalendar::DOW_SUNDAY`](#intlcalendar.constants.dow-sunday) y las constantes siguientes) y el último valor válido es `7` (sábado).

`IntlCalendar::FIELD_DAY_OF_WEEK_IN_MONTH` `int`  
Dado un día de la semana (domingo, lunes, …), este campo de calendario asigna un ordinal a tal día de la semana en un mes específico. Por lo tanto, si el valor de este campo es `1` y el valor del día de la semana es `2` (lunes), entonces el día definido del mes es el primer lunes del mes; el valor máximo es `5`.

Además de esto, el valor `0` y los valores negativos también están permitidos. El valor `0` abarca los siete días que ocurren inmediatamente antes de los siete primeros días de un mes (que por lo tanto tienen un « día de la semana en el mes » con el valor `1`). Los valores negativos comienzan a contar desde el final del mes - `-1` apunta a la última ocurrencia de un día de la semana en un mes, `-2` a la penúltima, y así sucesivamente.

A diferencia de [`IntlCalendar::FIELD_WEEK_OF_MONTH`](#intlcalendar.constants.field-week-of-month) y [`IntlCalendar::FIELD_WEEK_OF_YEAR`](#intlcalendar.constants.field-week-of-year), este valor no depende de `IntlCalendar::getFirstDayOfWeek` o de `IntlCalendar::getMinimalDaysInFirstWeek`. El primer lunes es el primer lunes, incluso si se encuentra en una semana que pertenece al mes anterior.

`IntlCalendar::FIELD_AM_PM` `int`  
El campo de calendario que indica si una hora es antes del mediodía (valor `0`, AM) o después (`1`, PM). La medianoche es AM, el mediodía es PM.

`IntlCalendar::FIELD_HOUR` `int`  
El campo de calendario para la hora, sin especificar si es por la mañana o por la tarde. Los valores válidos son de `0` a `11`.

`IntlCalendar::FIELD_HOUR_OF_DAY` `int`  
El campo de calendario para la hora completa (24h) del día. Los valores válidos son de `0` a `23`.

`IntlCalendar::FIELD_MINUTE` `int`  
El campo de calendario para la componente minutos de la hora.

`IntlCalendar::FIELD_SECOND` `int`  
El campo de calendario para la componente segundos de la hora.

`IntlCalendar::FIELD_MILLISECOND` `int`  
El campo de calendario para la componente milisegundos de la hora.

`IntlCalendar::FIELD_ZONE_OFFSET` `int`  
El campo de calendario que indica el desplazamiento bruto del huso horario, en milisegundos. El desplazamiento bruto es el desplazamiento del huso horario, excluyendo cualquier desplazamiento debido al horario de verano.

`IntlCalendar::FIELD_DST_OFFSET` `int`  
El campo de calendario para el desplazamiento del horario de verano del huso horario del calendario, en milisegundos, si está activo para el huso horario

`IntlCalendar::FIELD_YEAR_WOY` `int`  
El campo de calendario que representa el año para los fines de la [semana del año](#intlcalendar.constants.field-week-of-year).

`IntlCalendar::FIELD_DOW_LOCAL` `int`  
El campo de calendario para el día localizado de la semana. Esto es un valor entre `1` y `7`, `1` siendo utilizado para el día de la semana que corresponde al valor devuelto por `IntlCalendar::getFirstDayOfWeek`.

`IntlCalendar::FIELD_EXTENDED_YEAR` `int`  
El campo de calendario para una representación numérica del año que es continua a través de las eras. Para el calendario gregoriano, el valor de este campo corresponde al de `IntlCalendar::FIELD_YEAR` para los años AD; un año BC `y` es representado por `-y + 1`.

`IntlCalendar::FIELD_JULIAN_DAY` `int`  
El campo de calendario para un número de días julianos modificado. Es diferente de un número convencional de días julianos en que sus transiciones ocurren a medianoche del huso horario local en lugar de a mediodía UTC. Identifica de manera única una fecha.

`IntlCalendar::FIELD_MILLISECONDS_IN_DAY` `int`  
El campo de calendario que engloba la información en `IntlCalendar::FIELD_HOUR_OF_DAY`, `IntlCalendar::FIELD_MINUTE`, `IntlCalendar::FIELD_SECOND` y `IntlCalendar::FIELD_MILLISECOND`. El rango es de `0` a `24 * 3600 * 1000 - 1`. Esto no es el número de milisegundos transcurridos en el día, ya que durante las transiciones DST tendrá discontinuidades análogas a las de la hora local.

`IntlCalendar::FIELD_IS_LEAP_MONTH` `int`  
El campo de calendario cuyo valor es `1` para indicar un mes bisiesto y `0` en caso contrario.

`IntlCalendar::FIELD_FIELD_COUNT` `int`  
El número total de campos.

`IntlCalendar::FIELD_DAY_OF_MONTH` `int`  
Un alias de [`IntlCalendar::FIELD_DATE`](#intlcalendar.constants.field-date).

`IntlCalendar::DOW_SUNDAY` `int`  
Domingo.

`IntlCalendar::DOW_MONDAY` `int`  
Lunes.

`IntlCalendar::DOW_TUESDAY` `int`  
Martes.

`IntlCalendar::DOW_WEDNESDAY` `int`  
Miércoles.

`IntlCalendar::DOW_THURSDAY` `int`  
Jueves.

`IntlCalendar::DOW_FRIDAY` `int`  
Viernes.

`IntlCalendar::DOW_SATURDAY` `int`  
Sábado.

`IntlCalendar::DOW_TYPE_WEEKDAY` `int`  
La salida de `IntlCalendar::getDayOfWeekType` indicando que un día de la semana pertenece a la semana.

`IntlCalendar::DOW_TYPE_WEEKEND` `int`  
La salida de `IntlCalendar::getDayOfWeekType` indicando que un día de la semana pertenece al fin de semana.

`IntlCalendar::DOW_TYPE_WEEKEND_OFFSET` `int`  
La salida de `IntlCalendar::getDayOfWeekType` indicando que el fin de semana comienza durante el día de la semana dado.

`IntlCalendar::DOW_TYPE_WEEKEND_CEASE` `int`  
La salida de `IntlCalendar::getDayOfWeekType` indicando que el fin de semana termina durante el día de la semana dado.

`IntlCalendar::WALLTIME_FIRST` `int`  
La salida de `IntlCalendar::getSkippedWallTimeOption` indicando que las horas murales en el rango saltado deberían referirse al mismo instante que las horas murales con una hora menos y de `IntlCalendar::getRepeatedWallTimeOption` indicando que las horas murales en el rango repetido deberían referirse al instante de la primera ocurrencia de esta hora murale.

`IntlCalendar::WALLTIME_LAST` `int`  
La salida de `IntlCalendar::getSkippedWallTimeOption` indicando que las horas murales en el rango saltado deberían referirse al mismo instante que las horas murales con una hora más y de `IntlCalendar::getRepeatedWallTimeOption` indicando que las horas murales en el rango repetido deberían referirse al instante de la segunda ocurrencia de esta hora murale.

`IntlCalendar::WALLTIME_NEXT_VALID` `int`  
La salida de `IntlCalendar::getRepeatedWallTimeOption` indicando que las horas murales en el rango repetido deberían referirse al instante cuando la transición del horario de verano llega (comienza).

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
