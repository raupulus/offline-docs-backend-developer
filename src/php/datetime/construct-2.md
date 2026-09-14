---
title: DatePeriod::__construct
description: Crea un nuevo objeto DatePeriod
source_url: https://www.php.net/manual/es/dateperiod.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 9eb962113
order: 10320
---

DatePeriod::\_\_construct

Crea un nuevo objeto DatePeriod

## Descripción

```php
public DatePeriod::__construct(DateTimeInterface $start, DateInterval $interval, int $recurrences, [int $options])
```php

```php
public DatePeriod::__construct(DateTimeInterface $start, DateInterval $interval, DateTimeInterface $end, [int $options])
```

> [!WARNING]
> La siguiente variante del constructor ha quedado obsoleta:
>
> ```php
public DatePeriod::__construct(string $isostr, [int $options])
```php
>
> Esta variante del constructor ha quedado obsoleta a partir de PHP 8.4.0, utiliza DatePeriod::createFromISO8601String en su lugar.

Crea un nuevo objeto DatePeriod.

Los objetos `DatePeriod` pueden ser utilizados como iterador para generar un cierto número de objetos `DateTimeImmutable` o `DateTime` a partir de una `start` fecha (fecha de inicio), un `interval`, y una `end` fecha (fecha de fin) o del número de `recurrences`.

La clase de los objetos devueltos es equivalente a la clase ancestro `DateTimeImmutable` o `DateTime` proporcionada por el objeto `start`.

## Parámetros

`start`  
La fecha de inicio del período. Incluida por omisión en el conjunto de resultados.

`interval`  
El intervalo entre las recurrencias del período.

`recurrences`  
El número de recurrencias. Debe ser mayor que `0`. El número de resultados devueltos es superior en una unidad, ya que la fecha de inicio está incluida en el conjunto de resultados por omisión.

`end`  
La fecha de fin del período. No incluida por omisión en el conjunto de resultados.

`isostr`  
Un subconjunto de la [ especificación ISO 8601 de la repetición del intervalo](http://en.wikipedia.org/wiki/Iso8601#Repeating_intervals).

Ejemplos de algunas funcionalidades de especificación de intervalo ISO 8601 que PHP no soporta:

1.  Las ocurrencias cero (`R0/`)

2.  Desplazamientos horarios distintos de UTC (`Z`), tales como `+02:00`.

`options`  
Un campo de bits que puede ser utilizado para controlar ciertos comportamientos con las fechas de inicio y fin.

Puede ser configurado a `DatePeriod::EXCLUDE_START_DATE` para excluir la fecha de inicio del conjunto de fechas de recursión en el período.

Puede ser configurado a `DatePeriod::INCLUDE_END_DATE` para incluir la fecha de fin del conjunto de fechas de recursión en el período.

## Errores/Excepciones

Lanza una excepción `DateMalformedPeriodStringException` cuando el argumento `isostr` no puede ser analizado como una cadena de período ISO 8601 válida. Anteriormente a PHP 8.3, esto era una Exception.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La firma que utiliza `isostr` ha quedado obsoleta, utiliza DatePeriod::createFromISO8601String en su lugar. |
| 8.3.0 | Ahora lanza una DateMalformedPeriodStringException en lugar de Exception. |
| 8.2.0 | Se ha añadido la constante `DatePeriod::INCLUDE_END_DATE`. |
| 7.2.19, 7.3.6, 7.4.0 | `recurrences` ahora debe ser mayor que `0`. |

## Ejemplos

Ejemplo con DatePeriod

```
<?php
$start = new DateTime('2012-07-01');
$interval = new DateInterval('P7D');
$end = new DateTime('2012-07-31');
$recurrences = 4;
$iso = 'R4/2012-07-01T00:00:00Z/P7D';

// Todas estas fechas son equivalentes.
$period = new DatePeriod($start, $interval, $recurrences);
$period = new DatePeriod($start, $interval, $end);
$period = new DatePeriod($iso);

// Al recorrer el objeto DatePeriod, todas las
// fechas de recursión para el período serán mostradas.
foreach ($period as $date) {
    echo $date->format('Y-m-d')."\n";
}

    
```php

El ejemplo anterior mostrará:

    Deprecated: Calling DatePeriod::__construct(string $isostr, int $options = 0) is deprecated, use DatePeriod::createFromISO8601String() instead in script on line 11
    2012-07-01
    2012-07-08
    2012-07-15
    2012-07-22
    2012-07-29

Ejemplo con DatePeriod y `DatePeriod::EXCLUDE_START_DATE`

```
<?php
$start = new DateTime('2012-07-01');
$interval = new DateInterval('P7D');
$end = new DateTime('2012-07-31');

$period = new DatePeriod($start, $interval, $end,
                         DatePeriod::EXCLUDE_START_DATE);

// Al recorrer el objeto DatePeriod,
// todas las fechas de recursión para el período son mostradas.
// Tenga en cuenta que, en este caso, 2012-07-01 no será mostrada.
foreach ($period as $date) {
    echo $date->format('Y-m-d')."\n";
}

    
```php

El ejemplo anterior mostrará:

    2012-07-08
    2012-07-15
    2012-07-22
    2012-07-29

DatePeriod mostrando todos los últimos jueves del mes durante un año

```
<?php
$begin = new DateTime('2021-12-31');
$end = new DateTime('2022-12-31 23:59:59');

$interval = DateInterval::createFromDateString('last thursday of next month');
$period = new DatePeriod($begin, $interval, $end, DatePeriod::EXCLUDE_START_DATE);

foreach ($period as $dt) {
    echo $dt->format('l Y-m-d'), "\n";
}

    
```php

El ejemplo anterior mostrará:

    Thursday 2022-01-27
    Thursday 2022-02-24
    Thursday 2022-03-31
    Thursday 2022-04-28
    Thursday 2022-05-26
    Thursday 2022-06-30
    Thursday 2022-07-28
    Thursday 2022-08-25
    Thursday 2022-09-29
    Thursday 2022-10-27
    Thursday 2022-11-24
    Thursday 2022-12-29

## Notas

Los números de repetición no vinculados especificados en la sección 4.5 "Intervalo de tiempo recurrente" de la norma ISO 8601 no son soportados, es decir, ni `"R/..."` como `isostr` ni `null` como `end` funcionaría.
