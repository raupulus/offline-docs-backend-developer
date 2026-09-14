---
title: La clase DatePeriod
source_url: https://www.php.net/manual/es/class.dateperiod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: ee1ce6a0e
order: 10380
---

## Introducción

Representa un período de fechas.

Un período de fechas permite iterar a través de un conjunto de fechas y horas, ocurriendo a intervalos regulares, durante un período determinado.

## Sinopsis de la clase

DatePeriod

implements

IteratorAggregate

Constantes

public

const

int

DatePeriod::EXCLUDE_START_DATE

public

const

int

DatePeriod::INCLUDE_END_DATE

Propiedades

public

readonly

DateTimeInterface

null

start

public

readonly

DateTimeInterface

null

current

public

readonly

DateTimeInterface

null

end

public

readonly

DateInterval

null

interval

public

readonly

int

recurrences

public

readonly

bool

include_start_date

public

readonly

bool

include_end_date

Métodos

## Constantes predefinidas

`DatePeriod::EXCLUDE_START_DATE` `int`  
Excluye la fecha de inicio, utilizada por `DatePeriod::__construct`.

`DatePeriod::INCLUDE_END_DATE` `int`  
Incluye la fecha de fin, utilizada por `DatePeriod::__construct`.

## Propiedades

`recurrences`  
La cantidad mínima de instancias devueltas por el iterador.

Si el número de recurrencias ha sido explícitamente pasado mediante el argumento `$recurrences` en el constructor de la instancia `DatePeriod`, entonces esta propiedad contiene ese valor, *más* uno si la fecha de inicio no ha sido desactivada por `DatePeriod::EXCLUDE_START_DATE`, *más* uno si la fecha de fin ha sido activada por `DatePeriod::INCLUDE_END_DATE`.

Si el número de recurrencias no ha sido explícitamente pasado, entonces esta propiedad contiene el número mínimo de instancias devueltas. Esto sería `0`, *más* uno si la fecha de inicio no ha sido desactivada por `DatePeriod::EXCLUDE_START_DATE`, *más* uno si la fecha de fin ha sido activada por `DatePeriod::INCLUDE_END_DATE`.

```php
<?php
$start = new DateTime('2018-12-31 00:00:00');
$end   = new DateTime('2021-12-31 00:00:00');
$interval = new DateInterval('P1M');
$recurrences = 5;

// recurrencias explícitamente definidas por el constructor
$period = new DatePeriod($start, $interval, $recurrences, DatePeriod::EXCLUDE_START_DATE);
echo $period->recurrences, "\n";

$period = new DatePeriod($start, $interval, $recurrences);
echo $period->recurrences, "\n";

$period = new DatePeriod($start, $interval, $recurrences, DatePeriod::INCLUDE_END_DATE);
echo $period->recurrences, "\n";

// recurrencias no definidas en el constructor
$period = new DatePeriod($start, $interval, $end);
echo $period->recurrences, "\n";

$period = new DatePeriod($start, $interval, $end, DatePeriod::EXCLUDE_START_DATE);
echo $period->recurrences, "\n";

         
```

El ejemplo anterior mostrará:

```php
5
6
7
1
0

         
```

Ver también DatePeriod::getRecurrences.

`include_end_date`  
Incluye o no la fecha de fin en el conjunto de fechas recurrentes.

`include_start_date`  
Si se debe incluir la fecha de inicio en el conjunto de fechas recurrentes o no.

`start`  
La fecha de inicio del período.

`current`  
Durante la iteración, esto contendrá la fecha del día en el período.

`end`  
La fecha de fin del período.

`interval`  
Una especificación de intervalo repetitivo ISO 8601.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 8.2.0 | La constante `DatePeriod::INCLUDE_END_DATE` y la propiedad include_end_date han sido añadidas. |
| 8.0.0 | La clase `DatePeriod` ahora implementa IteratorAggregate. Anteriormente, solo Traversable era implementada. |
