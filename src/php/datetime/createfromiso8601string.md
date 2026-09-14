---
title: DatePeriod::createFromISO8601String
description: Crea un nuevo objeto DatePeriod a partir de un string ISO8601
source_url: https://www.php.net/manual/es/dateperiod.createfromiso8601string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateperiod/createfromiso8601string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10330
---

DatePeriod::createFromISO8601String

Crea un nuevo objeto DatePeriod a partir de un string ISO8601

## Descripción

```php
public static DatePeriod::createFromISO8601String(string $specification, [int $options]): static
```php

Crea un nuevo objeto DatePeriod a partir de un string ISO8601, tal como se especifica con `specification`.

## Parámetros

`specification`  
Un subconjunto de la especificación [ISO 8601 de intervalos recurrentes](http://en.wikipedia.org/wiki/Iso8601#Repeating_intervals).

Un ejemplo de especificación de intervalo ISO 8601 aceptada es `R5/2008-03-01T13:00:00Z/P1Y2M10DT2H30M`, que especifica :

- 5 iteraciones (`R5/`)

- Comienza en `2008-03-01T13:00:00Z`.

- Cada iteración es un intervalo de 1 año, 2 meses, 10 días, 2 horas y 30 minutos (`/P1Y2M10DT2H30M`).

Los ejemplos de algunas funcionalidades de especificación de intervalo ISO 8601 que PHP no soporta son :

1.  cero ocurrencias (`R0/`)

2.  desplazamientos horarios distintos de UTC (`Z`), como `+02:00`.

`options`  
Un campo de bits que puede ser utilizado para controlar ciertos comportamientos con las fechas de inicio y fin.

Con `DatePeriod::EXCLUDE_START_DATE` se excluye la fecha de inicio del conjunto de fechas recurrentes en el período.

Con `DatePeriod::INCLUDE_END_DATE` se incluye la fecha de fin en el conjunto de fechas recurrentes en el período.

## Valores devueltos

Crea un nuevo objeto DatePeriod.

Los objetos `DatePeriod` creados con este método pueden ser utilizados como un iterador para generar un cierto número de objetos `DateTimeImmutable`.

## Errores/Excepciones

Lanza una `DateMalformedPeriodStringException` cuando la `specification` no puede ser analizada como un intervalo ISO 8601 válido.

## Ejemplos

Ejemplo de DatePeriod::createFromISO8601String

```
<?php
$iso = 'R4/2023-07-01T00:00:00Z/P7D';
$period = DatePeriod::createFromISO8601String($iso);

// Al iterar sobre el objeto DatePeriod, todas las
// fechas recurrentes en este período son mostradas.
foreach ($period as $date) {
    echo $date->format('Y-m-d'), "\n";
}

    
```php

El ejemplo anterior mostrará:

    2023-07-01
    2023-07-08
    2023-07-15
    2023-07-22
    2023-07-29
