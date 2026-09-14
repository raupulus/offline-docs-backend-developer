---
title: DateTimeImmutable::createFromFormat
description: Analiza un string de tiempo según el formato especificado
source_url: https://www.php.net/manual/es/datetimeimmutable.createfromformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/createfromformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 10590
---

DateTimeImmutable::createFromFormat

date_create_immutable_from_format

Analiza un string de tiempo según el formato especificado

## Descripción

Estilo orientado a objetos

```php
public static DateTimeImmutable::createFromFormat(string $format, string $datetime, [DateTimeZone $timezone]): DateTimeImmutable
```php

Estilo procedimental

```php
date_create_immutable_from_format(string $format, string $datetime, [DateTimeZone $timezone]): DateTimeImmutable
```

Devuelve un nuevo objeto DateTimeImmutable representando la fecha y hora especificada por el string `datetime`, que tiene el formato indicado por `format`.

## Parámetros

`format`  
El formato en el cual se ha pasado el `string`. Consulta las opciones de formato a continuación. En la mayoría de los casos, pueden ser usadas las mismas letras que para la función `date`.

Todos los campos son inicializados con la fecha y hora actual. En el caso de que quieras restablecerlos a "cero" (Unix epoch, `01/01/1970 00:00:00 UTC`). Puedes hacerlo incluyendo el carácter `!` al principio de `format`, o `|` al final. Por favor, consulta la documentación de cada carácter a continuación para más información.

El formato es analizado de izquierda a derecha, lo que significa que en algunas situaciones el orden en el que los caracteres de formato están escritos afecta al resultado. En el caso de `z` (el día del año), es necesario que un año ya se haya analizado, por ejemplo mediante los caracteres `Y` o `y`.

Las letras de formato que se usan para analizar números permiten un amplio rango de valores, fuera de lo que sería el rango lógico. Por ejemplo, el `d` (día del mes) acepta valores en el rango de `00` a `99`. La única restricción es en la cantidad de dígitos. El mecanismo de desbordamiento del analizador de fecha/hora se usa cuando se dan valores fuera de rango. Los ejemplos a continuación muestran algo de este comportamiento.

Esto también significa que los datos analizados para una letra de formato son golosos, y leerán toda la cantidad de dígitos que su formato permite. Esto también puede significar que no hay suficientes caracteres en `datetime` para las letras de formato sucesivas. Un ejemplo en esta página también ilustra este problema.

| Carácter `format` | Descripción | Ejemplo de valores analizables |
|----|----|----|
| *Día* | --- | --- |
| `d` y `j` | Día del mes, 2 dígitos con o sin ceros iniciales | `01` a `31` o `1` a `31`. (Se aceptan 2 dígitos numericos mayores que los días del mes, en cuyo caso harán que el mes se desborde. Por ejemplo usando 33 con enero, significará 2 de febrero) |
| `D` y `l` | Nombre del día de la semana como texto, en inglés | `Mon` hasta `Sun` o `Sunday` hasta `Saturday`. Si el nombre del día indicado es diferente al nombre del día que pertenece la fecha analizada (o predeterminada) es diferente, entonces se produce un desbordamiento a la *siguiente* fecha con el nombre de indicado. Vea los ejemplos a continuación para obtener una explicación. |
| `S` | Sufijo ordinal en inglés para el día del mes, 2 caracteres. Se ignora durante el procesamiento. | `st`, `nd`, `rd` o `th`. |
| `z` | Día del año (comenzando en 0); debe estar precedido por `Y` o `y`. | `0` hasta `365`. (son aceptados 3 dígitos numéricos mayores que 365, en cuyo caso harán que el año se desborde. Por ejemplo usando 366 con 2022, significa 2 de enero de 2023) |
| *Mes* | --- | --- |
| `F` y `M` | Nombre del mes, en inglés, como January o Sept | `January` hasta `December` o `Jan` hasta `Dec` |
| `m` y `n` | Representación numerica del mes, 2 dígitos con o sin ceros iniciales | `01` hasta `12` o `1` hasta `12`. (son aceptados 2 dígitos numéricos mayores que 12, en cuyo caso harán que el año se desborde. Por ejemplo usando 13 significa enero del siguiente año) |
| *Año* | --- | --- |
| `X` y `x` | Una representación completa del año, *hasta* 19 dígitos, opcionalmente con el prefijo `+` o `-` | Ejemplos: `0055`, `787`, `1999`, `-2003`, `+10191` |
| `Y` | Una representación completa del año, *hasta* 4 dígitos | Ejemplos: `25` (igual que `0025`), `787`, `1999`, `2003` |
| `y` | Una representación de dos dígitos de un año (que se asume que está en el rango 1970-2069, inclusive) | Ejemplos: `99` o `03` (que se interpretarán como `1999` y `2003`, respectivamente) |
| *Hora* | --- | --- |
| `a` y `A` | Ante meridiem y post meridiem | `am` or `pm` |
| `g` y `h` | Hora en formato 12 horas, 2 dígitos con o sin ceros iniciales | `1` hasta `12` o `01` hasta `12` (son aceptados 2 dígitos numéricos mayores que 12, en cuyo caso harán que el día se desborde. Por ejemplo usando `14` significa `02` en el siguiente periodo AM/PM) |
| `G` y `H` | Hora en formato 24 horas, 2 dígitos con o sin ceros iniciales | `0` hasta `23` o `00` hasta `23` (son aceptados 2 dígitos numéricos mayores que 24, en cuyo caso harán que el día se desborde. Por ejemplo usando `26` significa `02:00` en el siguiente día) |
| `i` | Minutos, con ceros iniciales | `00` a `59`. (son aceptados 2 dígitos numéricos mayores que 59, en cuyo caso harán que la hora se desborde. Por ejemplo usando `66` significa `06` en la siguiente hora) |
| `s` | Segundos, con ceros iniciales | `00` hastah `59` (son aceptados 2 dígitos numéricos mayores que 59, en cuyo caso harán que el minuto se desborde. Por ejemplo usando `90` significa `30` en el siguiente minuto) |
| `v` | Fracción en milisengundos (hasta 3 digitos) | Ejemplos: `12` (`0.12` segundos), `345` (`0.345` segundos) |
| `u` | Fracción en microsengundos (hasta 6 dígitos) | Ejemplos: `45` (`0.45` segundos), `654321` (`0.654321` segundos) |
| *Zona horaria* | --- | --- |
| `e`, `O`, `p`, `P` y `T` | Identificador de zona horaria, o diferencia a UTC en horas, o diferencia a UTC con dos puntos entre horas y minutos, o abreviatura de zona horaria | Ejemplos: `UTC`, `GMT`, `Atlantic/Azores` o `+0200` o `+02:00` o `EST`, `MDT` |
| *Fecha y hora completa* | --- | --- |
| `U` | Segundos desde Unix Epoch (1 de enero de 1970 00:00:00 GMT) | Ejemplo: `1292177455` |
| *Espacios en blanco y separadores* | --- | --- |
| `` (espacio) | Cero o más espacios, tabuladores, NBSP (U+A0) o NNBSP (U+202F) | Ejemplos: `"\t"` o `" "` |
| `#` | Uno de los siguientes símbolos de separación: `;`, `:`, `/`, `.`, `,`, `-`, `(` o `)` | Ejemplo: `/` |
| `;`, `:`, `/`, `.`, `,`, `-`, `(` o `)` | El carácter especificado | Ejemplo: `-` |
| `?` | Un byte aleatorio | Ejemplo: `^` (Tenga en cuenta que los caracteres UTF-8 es posible que necesite más de uno `?`. En este caso, usar `*` es probablemente lo que desea en su lugar) |
| `*` | Bytes aleatorios hasta el siguiente separador o dígito | Ejemplo: `*` en `Y-*-d` con la cadena `2009-aWord-08` coincidirá con `aWord` |
| `!` | Restablece todos los campos (año, mes, día, hora, minuto, segundo, fracción e información de zona horaria) a valores similares a cero (`0` para hora, minuto, segundo y fracción, `1` para mes y día, `1970` para año y la zona horaria predeterminada) | Sin `!`, todos los campos se establecerán a la fecha y hora actual. |
| `|` | Restablece todos los campos (año, mes, día, hora, minuto, segundo, fracción e información de zona horaria) a valores similares a cero si no han sido analizados todavía. | `Y-m-d|` establecerá el año, mes y día a la información encontrada en la cadena a analizar, y establecerá la hora, minuto y segundo a `0`. |
| `+` | Si este especificador de formato está presente, los datos adicionales en la cadena no causarán un error, sino una advertencia en su lugar | Usa DateTimeImmutable::getLastErrors para averiguar si había datos adicionales. |

Los siguientes caracteres son reconocidos en la cadena del parámetro `format`

Los caracteres no reconocidos en el string de formato causarán que el análisis falle y un mensaje de error se añadirá a la estructura devuelta. Puedes consultar los mensajes de error con DateTimeImmutable::getLastErrors.

Para incluir caracteres literales en `format`, debes escaparlos con una barra invertida (`\`).

Si `format` no contiene el carácter `!`, entonces las partes de la fecha/hora que no están especificadas en `format` se establecerán a la fecha actual del sistema.

Si `format` contiene el carácter `!`, entonces las partes de la fecha/hora generadas que no están especificadas en `format`, así como los valores a la izquierda del `!`, se establecerán a los valores correspondientes de Unix epoch.

Si cualquier carácter de tiempo es analizado, entonces todos los demás campos relacionados con el tiempo se establecerán a "0", a menos que también se analicen.

Unix epoch es 01/01/1970 00:00:00 UTC.

`datetime`  
String representando la fecha y hora.

`timezone`  
Una instancia de `DateTimeZone` representando la zona horaria deseada.

Si se omite `timezone` o pasado `null` y `datetime` no contiene zona horaria, se usará la zona horaria actual.

> [!NOTE]
> El parámetro `timezone` y la zona horaria actual son ignorados cuando el parámetro `datetime` contiene un timestamp UNIX (por ejemplo, `946684800`) o especifica una zona horaria (por ejemplo, `2010-01-28T15:00:00+02:00`).

## Valores devueltos

Devuelve una nueva instancia de DateTimeImmutable o `false` si ocurre un error.

## Errores/Excepciones

Este método lanza ValueError cuando `datetime` contiene bytes nulos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.9 | El especificador `` (espacio) ahora también soporta los caracteres NBSP (U+A0) y NNBSP (U+202F). |
| 8.2.0 | Se ha añadido los especificadores de `format` `X` y `x`. |
| 8.0.21, 8.1.8, 8.2.0 | Ahora se lanza ValueError cuando se pasan bytes nulos a `datetime`, lo que anteriormente se ignoraba silenciosamente. |
| 7.3.0 | Se ha añadido el especificador de `format` `v`. |

## Ejemplos

Ejemplo de `DateTimeImmutable::createFromFormat`

Estilo orientado a objetos

```php
<?php
$date = DateTimeImmutable::createFromFormat('j-M-Y', '15-Feb-2009');
echo $date->format('Y-m-d');

   
```

Usando constantes predefinidas con `DateTimeImmutable::createFromFormat`

Estilo orientado a objetos

```php
<?php
$date = DateTimeImmutable::createFromFormat(
    DateTimeInterface::ISO8601,
    '2004-02-12T15:19:21+00:00'
);
echo $date->format('c e') . "\n";

$date = DateTimeImmutable::createFromFormat(
    DateTimeInterface::RFC3339_EXTENDED,
    '2013-10-14T09:00:00.000+02:00'
);
echo $date->format('c e') . "\n";

   
```

Las [constantes de formato](#datetimeinterface.constants.types) usadas en este ejemplo consisten en una cadena de caracteres para [formatear](#datetime.format) un objeto `DateTimeImmutable`. En la mayoría de los casos, estas letras coinciden con los mismos elementos de información de fecha/hora que los definidos en los [parámetros](#datetimeimmutable.createfromformat.parameters) de la sección anterior, pero tienden a ser más permisivos.

Complejidades de `DateTimeImmutable::createFromFormat`

```php
<?php
echo 'Hora actual: ' . date('Y-m-d H:i:s') . "\n";

$format = 'Y-m-d';
$date = DateTimeImmutable::createFromFormat($format, '2009-02-15');
echo "Formato: $format; " . $date->format('Y-m-d H:i:s') . "\n";

$format = 'Y-m-d H:i:s';
$date = DateTimeImmutable::createFromFormat($format, '2009-02-15 15:16:17');
echo "Formato: $format; " . $date->format('Y-m-d H:i:s') . "\n";

$format = 'Y-m-!d H:i:s';
$date = DateTimeImmutable::createFromFormat($format, '2009-02-15 15:16:17');
echo "Formato: $format; " . $date->format('Y-m-d H:i:s') . "\n";

$format = '!d';
$date = DateTimeImmutable::createFromFormat($format, '15');
echo "Formato: $format; " . $date->format('Y-m-d H:i:s') . "\n";

$format = 'i';
$date = DateTimeImmutable::createFromFormat($format, '15');
echo "Formato: $format; " . $date->format('Y-m-d H:i:s') . "\n";

   
```

Resultado del ejemplo anterior es similar a:

    Hora actual: 2022-06-02 15:50:46
    Formato: Y-m-d; 2009-02-15 15:50:46
    Formato: Y-m-d H:i:s; 2009-02-15 15:16:17
    Formato: Y-m-!d H:i:s; 1970-01-15 15:16:17
    Formato: !d; 1970-01-15 00:00:00
    Formato: i; 2022-06-02 00:15:00

Cadenas de formato con caracteres literales

```php
<?php
echo DateTimeImmutable::createFromFormat('H\h i\m s\s','23h 15m 03s')->format('H:i:s');

   
```

Resultado del ejemplo anterior es similar a:

    23:15:03

Comportamiento de desbordamiento

```php
<?php
echo DateTimeImmutable::createFromFormat('Y-m-d H:i:s', '2021-17-35 16:60:97')->format(DateTimeImmutable::RFC2822);

   
```

Resultado del ejemplo anterior es similar a:

    Sat, 04 Jun 2022 17:01:37 +0000

       

Aunque el resultado parece extraño, es correcto, ya que ocurren los siguientes desbordamientos:

1.  `97` segundos se desbordan a `1` minuto, dejando `37` segundos.

2.  `61` minutos se desbordan a `1` hora, dejando `1` minuto.

3.  `35` días se debordan a `1` mes, dejando `4` días. La cantidad de días que quedan depende del mes, ya que no todos los meses tienen la misma cantidad de días.

4.  `18` meses se desbordan a `1` año, dejando `6` meses.

Comportamiento de desbordamiento de nombres de días de la semana

```php
<?php
$d = DateTime::createFromFormat(DateTimeInterface::RFC1123, 'Mon, 3 Aug 2020 25:00:00 +0000');
echo $d->format(DateTime::RFC1123), "\n";

   
```

Resultado del ejemplo anterior es similar a:

    Mon, 10 Aug 2020 01:00:00 +0000

       

Aunque el resultado parece extraño, es correcto, ya que ocurren los siguientes desbordamientos:

1.  `3 Aug 2020 25:00:00` se desborda a `(Tue) 4 Aug 2020 01:00`.

2.  Se aplica `Mon`, el cual avanza la fecha a `Mon, 10 Aug 2020 01:00:00`. La explicación de palabras clave relativas como `Mon` se explica en la sección de [formatos relativos](#datetime.formats.relative).

Para detectar desbordamientos en fechas, puedes usar DateTimeImmutable::getLastErrors, el cual incluirá una advertencia si ocurrió un desbordamiento.

Detección de fechas desbordadas

```php
<?php
$d = DateTimeImmutable::createFromFormat('Y-m-d H:i:s', '2021-17-35 16:60:97');
echo $d->format(DateTimeImmutable::RFC2822), "\n\n";

var_dump(DateTimeImmutable::getLastErrors());

   
```

Resultado del ejemplo anterior es similar a:

    Sat, 04 Jun 2022 17:01:37 +0000

    array(4) {
      'warning_count' =>
      int(2)
      'warnings' =>
      array(1) {
        [19] =>
        string(27) "The parsed date was invalid"
      }
      'error_count' =>
      int(0)
      'errors' =>
      array(0) {
      }
    }

Comportamiento de análisis goloso

```php
<?php
print_r(date_parse_from_format('Gis', '60101'));

   
```

Resultado del ejemplo anterior es similar a:

    Array
    (
        [year] =>
        [month] =>
        [day] =>
        [hour] => 60
        [minute] => 10
        [second] => 0
        [fraction] => 0
        [warning_count] => 1
        [warnings] => Array
            (
                [5] => The parsed time was invalid
            )

        [error_count] => 1
        [errors] => Array
            (
                [4] => A two digit second could not be found
            )

        [is_localtime] =>
    )

       

El formato `G` es para analizar horas en formato de 24 horas, con o sin cero inicial. Esto requiere analizar 1 o 2 dígitos. Debido a que hay dos dígitos siguientes, lo lee ávidamente como `60`.

Los siguientes caracteres de formato `i` y `s` requieren ambos dos dígitos. Esto significa que se pasa `10` como minutos (`i`), y que luego no quedan suficientes dígitos para analizar como segundos (`s`).

El array `errors` indica este problema.

Adicionalmente, una hora de `60` está fuera del rango `0`-`24`, lo que hace que el array `warnings` incluya una advertencia de que la hora es incorrecta.

## Véase también

DateTimeImmutable::\_\_construct

DateTimeImmutable::getLastErrors

checkdate

strptime
