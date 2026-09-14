---
title: mktime
description: Obtener la marca de tiempo Unix de una fecha
source_url: https://www.php.net/manual/es/function.mktime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/mktime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 11310
---

mktime

Obtener la marca de tiempo Unix de una fecha

## Descripción

```php
mktime(int $hour, [int $minute], [int $second], [int $month], [int $day], [int $year]): int
```php

Devuelve la marca de tiempo Unix correspondiente a los argumentos dados. Esta marca de tiempo es un entero que contiene el número de segundos entre la Época Unix (1 de Enero del 1970 00:00:00 GMT) y el instante especificado.

Cualquier parámetro opcional omitido o a `null` se establecerá al valor actual según la fecha y hora locales.

> [!WARNING]
> Tenga en cuenta que el orden de los argumentos es extraño: `month`, `day`, `year`, y no en el orden más natural de `year`, `month`, `day`.

Llamar a `mktime` sin argumentos no está soportado, y devolverá un `ArgumentCountError`. Puede usar `time` para obtener la marca de tiempo actual.

## Parámetros

`hour`  
El número de la hora relativa al inicio del día determinado por `month`, `day` y `year`. Los valores negativos referencian la hora antes de la media noche del día en cuestión. Los valores mayores que 23 referencian la hora apropiada en el/los día/s siguiente/s.

`minute`  
El número de los minutos relativos al inicio de `hour`. Los valores negativos referencian el minuto en la hora previa. Los valores mayores que 59 referencian el minuto apropiado en la/s hora/s siguiente/s.

`second`  
El número de segundos relativos al inicio de `minute`. Los valores negativos referencian el segundo en el minuto previo. Los valores mayores que 59 referencian el segundo apropiado en el/los minuto/s siguiente/s.

`month`  
El número del mes relativo al final del año previo. Los valores de 1 a 12 referencian los meses del calendario normal del año en cuestión. Los valores menores que 1 (incluyendo valores negativos) referencian los meses del año previo en orden inverso, por lo que 0 es Diciembre, -1 es Noviembre, etc. Los valores mayores que 12 referencian el mes apropiado en el/los año/s siguiente/s.

`day`  
El número del día relativo al final del mes previo. Los valores del 1 al 28, 29, 30 o 31 (dependiendo del mes) referencian los días normales del mes relevante. Los valores menores que 1 (incluyendo valores negativos) referencian los días del mes previo por lo que 0 es el último día del mes previo, -1 es el día anterior a ese, etc. Los valores mayores que el número de días del mes relevante referencian el día apropiado en el/los mes/es siguiente/s.

`year`  
El número del año, puede ser un valor de dos o cuatro dígitos, con valores entre 0-69 mapeados a 2000-2069 y 70-100 a 1970-2000. En sistemas donde time_t es un entero con signo de 32 bits, como es lo más normal hoy en día, el rango válido para `year` es entre 1901 y 2038. Sin embargo, antes de PHP 5.1.0 este rango estaba limitado desde 1970 a 2038 en algunos sistemas (p.ej. Windows).

## Valores devueltos

`mktime` devuelve la marca de tiempo Unix de los argumentos dados, o `false` si la marca de tiempo no cabe en un entero PHP.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `hour` ya no es opcional. Si necesita una marca de tiempo unix, utilice `time`. |
| 8.0.0 | `minute`, `second`, `month`, `day` y `year` ahora pueden ser nulos. |

## Ejemplos

Ejemplo básico de `mktime`

```
<?php
// Establece la zona horaria a utilizar.
date_default_timezone_set('UTC');

// Imprime: 1 de julio de 2000 cae en sábado
echo "1 de julio de 2000 cae en " . date("l", mktime(0, 0, 0, 7, 1, 2000)) . "\n";

// Imprime algo como: 2006-04-05T01:02:03+00:00
echo date('c', mktime(1, 2, 3, 4, 5, 2006)) . "\n";

    
```php

Resultado del ejemplo anterior es similar a:

    1 de julio de 2000 cae en Saturday
    2006-04-05T01:02:03+00:00

Ejemplo `mktime`

`mktime` es útil para hacer cálculos con fechas y validaciones, ya que calculará automáticamente los valores correctos para entradas fuera de rango. Por ejemplo, cada una de las siguientes líneas devuelve la cadena: "Jan-01-1998".

```
<?php
date_default_timezone_set('America/New_York');

echo date("c", mktime(0, 0, 0, 12, 32, 1997)) . "\n";
echo date("c", mktime(0, 0, 0, 13, 1, 1997)) . "\n";
echo date("c", mktime(0, 0, 0, 1, 1, 1998)) . "\n";
echo date("c", mktime(0, 0, 0, 1, 1, 98)) . "\n";

    
```php

Resultado del ejemplo anterior es similar a:

    1998-01-01T00:00:00-05:00
    1998-01-01T00:00:00-05:00
    1998-01-01T00:00:00-05:00
    1998-01-01T00:00:00-05:00

Usando mktime para buscar fechas relativas

```
<?php
date_default_timezone_set('Asia/Tokyo');

$tomorrow  = mktime(0, 0, 0, date("m")  , date("d")+1, date("Y"));
print date('c', $tomorrow) . "\n";

$lastmonth = mktime(0, 0, 0, date("m")-1, date("d"),   date("Y"));
print date('c', $lastmonth) . "\n";

$nextyear  = mktime(0, 0, 0, date("m"),   date("d"),   date("Y")+1) . "\n";
print date('c', $nextyear) . "\n";

    
```php

Resultado del ejemplo anterior es similar a:

    2025-09-30T00:00:00+09:00
    2025-08-29T00:00:00+09:00
    2026-09-29T00:00:00+09:00

> [!NOTE]
> Esto puede ser más fiable que simplemente sumar o restar el número de segundos de un día o mes a una marca de tiempo debido al horario de verano.

El último día del mes

El último día de cualquier mes dado se puede expresar como el día "0" del mes siguiente, no el día -1. Los dos ejemplos siguientes producirán la cadena "El último día en Feb 2000 es: 29".

```
<?php

$lastday = mktime(0, 0, 0, 3, 0, 2000);
echo 'El último día en Feb 2000 es: ', date('d', $lastday) . "\n";

$lastday = mktime(0, 0, 0, 4, -31, 2000);
echo 'El último día en Feb 2000 es: ', date('d', $lastday) . "\n";

    
```php

El ejemplo anterior mostrará:

    El último día en Feb 2000 es: 29
    El último día en Feb 2000 es: 29

## Véase también

La clase `DateTimeImmutable`, `checkdate`, `gmmktime`, `date`, `time`
