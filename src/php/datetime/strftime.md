---
title: strftime
description: Formatea una fecha/hora local con la configuración local
source_url: https://www.php.net/manual/es/function.strftime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/strftime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11320
---

strftime

Formatea una fecha/hora local con la configuración local

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Se recomienda evitar su uso.

Las alternativas a esta función incluyen:

date

IntlDateFormatter::format

## Descripción

```php
#[\Deprecated] strftime(string $format, [int $timestamp]): string
```php

Formatea una fecha y/o una hora según la localización local. Los nombres de los meses, de los días de la semana pero también de otras cadenas dependientes de la localización, respetarán la localización actual definida por la función `setlocale`.

> [!WARNING]
> Es posible que no todos los especificadores de conversión sean compatibles con su biblioteca C, en cuyo caso no serán compatibles con `strftime` de PHP. Además, no todas las plataformas admiten marcas de tiempo negativas, por lo que su rango de fechas puede estar limitado a fechas no anteriores a la época Unix. Esto significa que `%e`, `%T`, `%R` y `%D` (y puede que otros) y las fechas anteriores al `1 de Enero de 1970` no funcionarán bajo Windows, en algunas distribuciones de Linux, y algunos otros sistemas operativos. Para Windows, una lista completa de las opciones de conversión está disponible en el [sitio de MSDN](http://msdn.microsoft.com/en-us/library/fe06s4ak.aspx). Utilice en su lugar el método IntlDateFormatter::format.

## Parámetros

`format`  
| `format` | Descripción | Ejemplo de valores devueltos |
|----|----|----|
| *Día* | --- | --- |
| `%a` | Nombre abreviado del día de la semana | De `Sun` a `Sat` |
| `%A` | Nombre completo del día de la semana | De `Sunday` a `Saturday` |
| `%d` | Día del mes en formato numérico, con 2 dígitos (con el cero inicial) | De `01` a `31` |
| `%e` | Día del mes, con un espacio precediendo al primer dígito. La implementación de Windows es diferente, véase más abajo para más información. | De `1` a `31` |
| `%j` | Día del año, con 3 dígitos con cero inicial | `001` a `366` |
| `%u` | Representación ISO-8601 del día de la semana | De `1` (para Lunes) a `7` (para Domingo) |
| `%w` | Representación numérica del día de la semana | De `0` (para Domingo) a `6` (para Sábado) |
| *Semana* | --- | --- |
| `%U` | Número de la semana del año dado, comenzando por el primer Lunes como primera semana | `13` (para la 13ª semana completa del año) |
| `%V` | Número de la semana del año, siguiendo la norma ISO-8601:1988, comenzando como primera semana, la semana del año que contiene al menos 4 días, y donde Lunes es el inicio de la semana | De `01` a `53` (donde 53 cuenta como semana de solapamiento) |
| `%W` | Una representación numérica de la semana del año, comenzando por el primer Lunes de la primera semana | `46` (para la 46ª semana de la semana comenzando por un Lunes) |
| *Mes* | --- | --- |
| `%b` | Nombre del mes, abreviado, según la localización | De `Jan` a `Dec` |
| `%B` | Nombre completo del mes, según la localización | De `January` a `December` |
| `%h` | Nombre del mes abreviado, según la localización (alias de %b) | De `Jan` a `Dec` |
| `%m` | Mes, con 2 dígitos | De `01` (para Enero) a `12` (para Diciembre) |
| *Año* | --- | --- |
| `%C` | Representación, con 2 dígitos, del siglo (año dividido por 100, reducido a un entero) | `19` para el siglo 20 |
| `%g` | Representación, con 2 dígitos, del año, compatible con los estándares ISO-8601:1988 (véase %V) | Ejemplo: `09` para la semana del 6 de enero de 2009 |
| `%G` | La versión completa de 4 dígitos de %g | Ejemplo: `2009` para la semana del 3 de enero de 2009 |
| `%y` | El año, con 2 dígitos | Ejemplo: `09` para 2009, `79` para 1979 |
| `%Y` | El año, con 4 dígitos | Ejemplo: `2038` |
| *Hora* | --- | --- |
| `%H` | La hora, con 2 dígitos, en formato 24 horas | De `00` a `23` |
| `%k` | La hora en formato 24 horas, con un espacio precediendo a un solo dígito | De `0` a `23` |
| `%I` | Hora, con 2 dígitos, en formato 12 horas | De `01` a `12` |
| `%l` ('L' minúscula) | Hora, en formato 12 horas, con un espacio precediendo a un solo dígito | De `1` a `12` |
| `%M` | Minuto, con 2 dígitos | De `00` a `59` |
| `%p` | 'AM' o 'PM', en mayúsculas, basado en la hora proporcionada | Ejemplo: `AM` para 00:31, `PM` para 22:23. El resultado exacto depende del sistema operativo, y pueden devolver también variantes en minúsculas, o variantes con puntos (como `a.m.`). |
| `%P` | 'am' o 'pm', en minúsculas, basado en la hora proporcionada | Ejemplo: `am` para 00:31, `pm` para 22:23. No soportado por todos los sistemas operativos. |
| `%r` | Idéntico a "%I:%M:%S %p" | Ejemplo: `09:34:17 PM` para 21:34:17 |
| `%R` | Idéntico a "`%H:%M`" | Ejemplo: `00:35` para 12:35 AM, `16:44` para 4:44 PM |
| `%S` | Segundo, con 2 dígitos | De `00` a `59` |
| `%T` | Idéntico a "`%H:%M:%S`" | Ejemplo: `21:34:17` para 09:34:17 PM |
| `%X` | Representación de la hora, basada en la localización, sin la fecha | Ejemplo: `03:59:16` o `15:59:16` |
| `%z` | El desplazamiento horario. No implementado tal como se describe en Windows. Ver más abajo para más información. | Ejemplo: `-0500` para la hora del este de EE.UU. |
| `%Z` | La abreviación del desplazamiento horario. No implementado tal como se describe en Windows. Ver más abajo para más información. | Ejemplo: `EST` para la hora del este |
| *Hora y fecha* | --- | --- |
| `%c` | Fecha y hora preferidas, basadas en la localización | Ejemplo: `Tue Feb 5 00:45:10 2009` para el 5 de febrero de 2009 a las 12:45:10 AM |
| `%D` | Idéntico a "`%m/%d/%y`" | Ejemplo: `02/05/09` para el 5 de febrero de 2009 |
| `%F` | Idéntico a "`%Y-%m-%d`" (usado habitualmente por las bases de datos) | Ejemplo: `2009-02-05` para el 5 de febrero de 2009 |
| `%s` | Timestamp de la época Unix (idéntico a la función `time`) | Ejemplo: `305815200` para el 10 de septiembre de 1979 08:40:00 AM |
| `%x` | Representación preferida de la fecha, basada en la localización, sin la hora | Ejemplo: `02/05/09` para el 5 de febrero de 2009 |
| *Varios* | --- | --- |
| `%n` | Una nueva línea ("\n") | --- |
| `%t` | Una tabulación ("\t") | --- |
| `%%` | El carácter de porcentaje ("`%`") | --- |

Los siguientes caracteres son reconocidos en el argumento `format`

> [!WARNING]
> A diferencia de la norma `ISO-9899:1999`, Sun Solaris comienza con el Domingo a 1. También, el formato `%u` no funcionará tal como se describe en este manual.

> [!WARNING]
> *Solo Windows:*
>
> El modificador `%e` no es soportado bajo Windows. Para calcular el valor, el modificador `%#d` puede ser utilizado en su lugar. El ejemplo de abajo ilustra la manera de escribir un código multiplataforma.
>
> Los modificadores `%z` y `%Z` devuelven ambos el nombre de la zona horaria en lugar del desplazamiento o de la abreviación.

> [!WARNING]
> *Solo macOS y musl:* El modificador `%P` no es soportado por la implementación de esta función bajo macOS.

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

## Valores devueltos

Devuelve una `string` formateada según el argumento `format` dado, utilizando el argumento `timestamp` o la fecha local actual si no se proporciona ningún timestamp. Los nombres de los meses, de los días de la semana pero también de otras cadenas dependientes de la localización, respetarán la localización actual definida por la función `setlocale`. La función devuelve `false` si `format` está vacío, contiene especificadores de conversión no soportados, o si la longitud de la cadena devuelta sería mayor que `4095`.

## Errores/Excepciones

Cada llamada a una función de fecha/hora generará un diagnóstico de tipo `E_WARNING` si la zona horaria no es válida. Ver también `date_default_timezone_set`

Dado que la salida depende de la biblioteca C subyacente, algunos especificadores de conversión no son soportados. Bajo Windows, el hecho de proporcionar un especificador de conversión desconocido devolverá 5 mensajes de nivel `E_WARNING` y devolverá `false` al final. Bajo otros sistemas operativos, no recibirá ningún mensaje de nivel `E_WARNING` y la salida contendrá los especificadores no convertidos.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Ejemplos

Este ejemplo solo funcionará si tiene las localizaciones respectivas instaladas en su sistema.

Ejemplo con `strftime`

```
<?php
setlocale(LC_TIME, "C");
echo strftime("%A");
setlocale(LC_TIME, "fi_FI");
echo strftime(" in Finnish is %A,");
setlocale(LC_TIME, "fr_FR");
echo strftime(" in French %A and");
setlocale(LC_TIME, "de_DE");
echo strftime(" in German %A.\n");

    
```php

Ejemplo en formato de fecha ISO 8601:1988

```
<?php
/*     Diciembre 2002 / Enero 2003
ISOWk  L   M   X   J   V   S   D
----- ----------------------------
51     16  17  18  19  20  21  22
52     23  24  25  26  27  28  29
1      30  31   1   2   3   4   5
2       6   7   8   9  10  11  12
3      13  14  15  16  17  18  19   */

// Muestra: 12/28/2002 - %V,%G,%Y = 52,2002,2002
echo "12/28/2002 - %V,%G,%Y = " . strftime("%V,%G,%Y", strtotime("12/28/2002")) . "\n";

// Muestra: 12/30/2002 - %V,%G,%Y = 1,2003,2002
echo "12/30/2002 - %V,%G,%Y = " . strftime("%V,%G,%Y", strtotime("12/30/2002")) . "\n";

// Muestra: 1/3/2003 - %V,%G,%Y = 1,2003,2003
echo "1/3/2003 - %V,%G,%Y = " . strftime("%V,%G,%Y",strtotime("1/3/2003")) . "\n";

// Muestra: 1/10/2003 - %V,%G,%Y = 2,2003,2003
echo "1/10/2003 - %V,%G,%Y = " . strftime("%V,%G,%Y",strtotime("1/10/2003")) . "\n";

/*     Diciembre 2004 / Enero 2005
ISOWk  L   M   X   J   V   S   D
----- ----------------------------
51     13  14  15  16  17  18  19
52     20  21  22  23  24  25  26
53     27  28  29  30  31   1   2
1       3   4   5   6   7   8   9
2      10  11  12  13  14  15  16   */

// Muestra: 12/23/2004 - %V,%G,%Y = 52,2004,2004
echo "12/23/2004 - %V,%G,%Y = " . strftime("%V,%G,%Y",strtotime("12/23/2004")) . "\n";

// Muestra: 12/31/2004 - %V,%G,%Y = 53,2004,2004
echo "12/31/2004 - %V,%G,%Y = " . strftime("%V,%G,%Y",strtotime("12/31/2004")) . "\n";

// Muestra: 1/2/2005 - %V,%G,%Y = 53,2004,2005
echo "1/2/2005 - %V,%G,%Y = " . strftime("%V,%G,%Y",strtotime("1/2/2005")) . "\n";

// Muestra: 1/3/2005 - %V,%G,%Y = 1,2005,2005
echo "1/3/2005 - %V,%G,%Y = " . strftime("%V,%G,%Y",strtotime("1/3/2005")) . "\n";

    
```php

`%e` funcionando en toda plataforma

```
<?php

// 1 de Enero: resultados en: '%e%1%' (%%, e, %%, %e, %%)
$format = '%%e%%%e%%';

// Verifica bajo Windows, para encontrar y reemplazar el modificador %e
// correctamente
if (strtoupper(substr(PHP_OS, 0, 3)) == 'WIN') {
    $format = preg_replace('#(?<!%)((?:%%)*)%e#', '\1%#d', $format);
}

echo strftime($format);

    
```php

Muestra todos los formatos conocidos o no

```
<?php

// Describe los formatos
$strftimeFormats = array(
    'A' => 'Una representación textual completa del día',
    'B' => 'Nombre del mes completo, basado en la localización',
    'C' => 'Representación con 2 dígitos del año (año, dividido por 100, truncado a entero)',
    'D' => 'Idéntico a "%m/%d/%y"',
    'E' => '',
    'F' => 'Idéntico a "%Y-%m-%d"',
    'G' => 'La versión completa, con 4 dígitos de %g',
    'H' => 'Una representación con 2 dígitos de la hora en formato 24-horas',
    'I' => 'Una representación con 2 dígitos de la hora en formato 12-horas',
    'J' => '',
    'K' => '',
    'L' => '',
    'M' => 'Una representación con 2 dígitos de los minutos',
    'N' => '',
    'O' => '',
    'P' => '"am" o "pm" (en minúsculas) basado en la hora actual',
    'Q' => '',
    'R' => 'Idéntico a "%H:%M"',
    'S' => 'Una representación con 2 dígitos de los segundos',
    'T' => 'Idéntico a "%H:%M:%S"',
    'U' => 'Número de la semana para el año actual, comenzando por el primer Domingo como primera semana',
    'V'  => 'Número ISO-8601:1988 de la semana del año actual, comenzando por la primera semana del año con al menos 4 días de semana, con el Lunes como inicio de semana',
    'W' => 'Una representación numérica de la semana del año, comenzando por el primer Lunes como primera semana',
    'X' => 'Representación preferida para la hora, basada en la localización, sin la fecha',
    'Y' => 'Una representación con 4 dígitos del año',
    'Z' => 'La abreviación del desplazamiento horario, no proporcionada por %z (depende del sistema operativo)',
    'a' => 'La abreviación de la representación textual del día',
    'b' => 'La abreviación del nombre del mes, basada en la localización',
    'c' => 'Timestamp preferido basado en la localización',
    'd' => 'Día del mes con 2 dígitos (con el cero inicial)',
    'e' => 'Día del mes, con un espacio precediendo a un solo dígito',
    'f' => '',
    'g' => 'Una representación con 2 dígitos del año en formato ISO-8601:1988 (ver %V)',
    'h' => 'Abreviación del nombre del mes, basada en la localización (alias de %b)',
    'i' => '',
    'j' => 'Día del año, con 3 dígitos con cero inicial',
    'k' => 'Hora, en formato 24-horas, con un espacio precediendo a un solo dígito',
    'l' => 'Hora, en formato 12-horas, con un espacio precediendo a un solo dígito',
    'm' => 'Una representación del mes con 2 dígitos',
    'n' => 'Un carácter de nueva línea ("\n")',
    'o' => '',
    'p' => '"AM" o "PM" (en mayúsculas) basado en la hora actual',
    'q' => '',
    'r' => 'Idéntico a "%I:%M:%S %p"',
    's' => 'Timestamp respecto a la época Unix',
    't' => 'Un carácter de tabulación ("\t")',
    'u' => 'Representación numérica del día de la semana en formato ISO-8601',
    'v' => '',
    'w' => 'Representación numérica del día de la semana',
    'x' => 'Representación preferida de la fecha, basada en la localización, sin la hora',
    'y' => 'Representación del año con 2 dígitos',
    'z' => 'O bien el desplazamiento horario desde UTC o su abreviación (según el sistema operativo)',
    '%' => 'Un carácter porcentaje ("%")',
);

// Resultados
$strftimeValues = array();

// Evalúa los formatos suprimiendo los errores
foreach ($strftimeFormats as $format => $description) {
    if (false !== ($value = @strftime("%{$format}"))) {
        $strftimeValues[$format] = $value;
    }
}

// Encuentra el valor más largo
$maxValueLength = 2 + max(array_map('strlen', $strftimeValues));

// Muestra todos los formatos conocidos
foreach ($strftimeValues as $format => $value) {
    echo "Formato conocido: '{$format}' = ", str_pad("'{$value}'", $maxValueLength), " ( {$strftimeFormats[$format]} )\n";
}

// Muestra todos los formatos no conocidos
foreach (array_diff_key($strftimeFormats, $strftimeValues) as $format => $description) {
    echo "Formato desconocido: '{$format}'   ", str_pad(' ', $maxValueLength), ($description ? " ( {$description} )" : ''), "\n";
}

    
```php

Resultado del ejemplo anterior es similar a:

    Formato conocido: 'A' = 'Friday'            ( Una representación textual completa del día )
    Formato conocido: 'B' = 'December'          ( Nombre del mes completo, basado en la localización )
    Formato conocido: 'H' = '11'                ( Una representación con 2 dígitos de la hora en formato 24-horas )
    Formato conocido: 'I' = '11'                ( Una representación con 2 dígitos de la hora en formato 12-horas )
    Formato conocido: 'M' = '24'                ( Una representación con 2 dígitos de los minutos )
    Formato conocido: 'S' = '44'                ( Una representación con 2 dígitos de los segundos )
    Formato conocido: 'U' = '48'                ( Número de la semana para el año actual, comenzando por el primer Domingo como primera semana )
    Formato conocido: 'W' = '48'                ( Una representación numérica de la semana del año, comenzando por el primer Lunes como primera semana )
    Formato conocido: 'X' = '11:24:44'          ( Representación preferida para la hora, basada en la localización, sin la fecha )
    Formato conocido: 'Y' = '2010'              ( Una representación con 4 dígitos del año )
    Formato conocido: 'Z' = 'GMT Standard Time' ( La abreviación del desplazamiento horario, no proporcionada por %z (depende del sistema operativo) )
    Formato conocido: 'a' = 'Fri'               ( La abreviación de la representación textual del día )
    Formato conocido: 'b' = 'Dec'               ( La abreviación del nombre del mes, basada en la localización )
    Formato conocido: 'c' = '12/03/10 11:24:44' ( Timestamp preferido basado en la localización )
    Formato conocido: 'd' = '03'                ( Día del mes con 2 dígitos (con el cero inicial) )
    Formato conocido: 'j' = '337'               ( Día del año, con 3 dígitos con cero inicial )
    Formato conocido: 'm' = '12'                ( Una representación del mes con 2 dígitos )
    Formato conocido: 'p' = 'AM'                ( "AM" o "PM" (en mayúsculas) basado en la hora actual )
    Formato conocido: 'w' = '5'                 ( Representación numérica del día de la semana )
    Formato conocido: 'x' = '12/03/10'          ( Representación preferida de la fecha, basada en la localización, sin la hora )
    Formato conocido: 'y' = '10'                ( Representación del año con 2 dígitos )
    Formato conocido: 'z' = 'GMT Standard Time' ( O bien el desplazamiento horario desde UTC o su abreviación (según el sistema operativo) )
    Formato conocido: '%' = '%'                 ( Un carácter porcentaje ("%") )
    Formato desconocido: 'C'                       ( Representación con 2 dígitos del año (año, dividido por 100, truncado a entero) )
    Formato desconocido: 'D'                       ( Idéntico a "%m/%d/%y" )
    Formato desconocido: 'E'
    Formato desconocido: 'F'                       ( Idéntico a "%Y-%m-%d" )
    Formato desconocido: 'G'                       ( La versión completa, con 4 dígitos de %g )
    Formato desconocido: 'J'
    Formato desconocido: 'K'
    Formato desconocido: 'L'
    Formato desconocido: 'N'
    Formato desconocido: 'O'
    Formato desconocido: 'P'                       ( "am" o "pm" (en minúsculas) basado en la hora actual )
    Formato desconocido: 'Q'
    Formato desconocido: 'R'                       ( Idéntico a "%H:%M" )
    Formato desconocido: 'T'                       ( Idéntico a "%H:%M:%S" )
    Formato desconocido: 'V'                       ( Número ISO-8601:1988 de la semana del año actual, comenzando por la primera semana del año con al menos 4 días de semana, con el Lunes como inicio de semana )
    Formato desconocido: 'e'                       ( Día del mes, con un espacio precediendo a un solo dígito )
    Formato desconocido: 'f'
    Formato desconocido: 'g'                       ( Una representación con 2 dígitos del año en formato ISO-8601:1988 (ver %V) )
    Formato desconocido: 'h'                       ( Abreviación del nombre del mes, basada en la localización (alias de %b) )
    Formato desconocido: 'i'
    Formato desconocido: 'k'                       ( Hora, en formato 24-horas, con un espacio precediendo a un solo dígito )
    Formato desconocido: 'l'                       ( Hora, en formato 12-horas, con un espacio precediendo a un solo dígito )
    Formato desconocido: 'n'                       ( Un carácter de nueva línea ("\n") )
    Formato desconocido: 'o'
    Formato desconocido: 'q'
    Formato desconocido: 'r'                       ( Idéntico a "%I:%M:%S %p" )
    Formato desconocido: 's'                       ( Timestamp respecto a la época Unix )
    Formato desconocido: 't'                       ( Un carácter de tabulación ("\t") )
    Formato desconocido: 'u'                       ( Representación numérica del día de la semana en formato ISO-8601 )
    Formato desconocido: 'v'

## Notas

> [!NOTE]
> `%G` y `%V`, que están basadas en la semana `ISO 8601:1988`, pueden conducir a resultados inesperados (aunque correctos) si el sistema de numeración no es conocido. Ver el ejemplo `%V` de esta página.

## Véase también

IntlDateFormatter::format, DateTimeInterface::format, [Herramienta de formato strftime() en línea](http://strftime.net/), `setlocale`, `mktime`, `strptime`, `gmstrftime`, [grupo de especificaciones de `strftime`](http://www.opengroup.org/onlinepubs/007908799/xsh/strftime.html)
