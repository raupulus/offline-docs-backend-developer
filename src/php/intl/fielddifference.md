---
title: IntlCalendar::fieldDifference
description: Calcula la diferencia entre el tiempo dado y el tiempo del objeto
source_url: https://www.php.net/manual/es/intlcalendar.fielddifference.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/fielddifference.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40260
---

IntlCalendar::fieldDifference

Calcula la diferencia entre el tiempo dado y el tiempo del objeto

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::fieldDifference(float $timestamp, int $field): int
```php

Estilo procedimental

```php
intlcal_field_difference(IntlCalendar $calendar, float $timestamp, int $field): int
```

Devuelve la diferencia entre el tiempo dado y el tiempo de este objeto, respetando la cantidad especificada por el argumento `field`.

Este método está previsto para ser llamado sucesivamente, primero con el campo de interés más significativo, luego con el campo menos significativo. Al final, como efecto secundario, el valor del calendario para el campo especificado será avanzado por la duración devuelta.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`timestamp`  
El tiempo utilizado para la comparación con la cantidad representada por el campo `field`. Para que el resultado sea positivo, el tiempo proporcionado en este argumento debe estar en el futuro con respecto al tiempo del objeto del método.

`field`  
El campo que representa la cantidad a comparar.

## Valores devueltos

Devuelve una diferencia (con signo) de tiempo, utilizando la unidad asociada con el campo especificado o `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlCalendar::fieldDifference`

```php
<?php
ini_set('date.timezone', 'Europe/Lisbon');
ini_set('intl.default_locale', 'fr_FR');

$cal1 = IntlCalendar::fromDateTime('2012-02-29 09:00:11');
$cal2 = IntlCalendar::fromDateTime('2013-03-01 09:19:29');
$time = $cal2->getTime();

echo "Tiempo, antes de la operación: ", IntlDateFormatter::formatObject($cal1), "\n";

printf(
    "La diferencia de tiempo es de %d año(s), %d mes(es), "
  . "%d día(s), %d hora(s) y %d minuto(s)\n",
    $cal1->fieldDifference($time, IntlCalendar::FIELD_YEAR),
    $cal1->fieldDifference($time, IntlCalendar::FIELD_MONTH),
    $cal1->fieldDifference($time, IntlCalendar::FIELD_DAY_OF_MONTH),
    $cal1->fieldDifference($time, IntlCalendar::FIELD_HOUR_OF_DAY),
    $cal1->fieldDifference($time, IntlCalendar::FIELD_MINUTE)
);

// ahora, el tiempo objetivo ha sido avanzado, excepto para los segundos,
// para los cuales no medimos la diferencia
echo "Tiempo, después de la operación: ", IntlDateFormatter::formatObject($cal1), "\n";

    
```

El ejemplo anterior mostrará:

    Tiempo, antes de la operación: 29 feb. 2012 09:00:11
    La diferencia de tiempo es de 1 año(s), 0 mes(es), 1 día(s), 0 hora(s) y 19 minuto(s)
    Tiempo, después de la operación: 1 mar. 2013 09:19:11
