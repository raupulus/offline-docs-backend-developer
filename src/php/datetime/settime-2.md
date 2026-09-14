---
title: DateTimeImmutable::setTime
description: Establece la hora
source_url: https://www.php.net/manual/es/datetimeimmutable.settime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/settime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10690
---

DateTimeImmutable::setTime

Establece la hora

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::setTime() does not modify the object itself")] public DateTimeImmutable::setTime(int $hour, int $minute, [int $second], [int $microsecond]): DateTimeImmutable
```php

Devuelve un nuevo objeto DateTimeImmutable con la hora establecida a la hora dada.

## Parámetros

`hour`  
Hora de la hora.

`minute`  
Minuto de la hora.

`second`  
Segundo de la hora.

`microsecond`  
Microsegundo de la hora.

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El comportamiento con horas dobles existentes (durante la transición de DST de retroceso) cambió. Anteriormente, PHP elegiría la segunda ocurrencia (después de la transición de DST), en lugar de la primera ocurrencia (antes de la transición de DST). |
| 7.1.0 | Se ha añadido el parametro `microsecond`. |

## Ejemplos

Ejemplo de `DateTimeImmutable::setTime`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable('2001-01-01');

$newDate = $date->setTime(14, 55);
echo $newDate->format('Y-m-d H:i:s') . "\n";

$newDate = $date->setTime(14, 55, 24);
echo $newDate->format('Y-m-d H:i:s') . "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    2001-01-01 14:55:00
    2001-01-01 14:55:24

Valores que exceden los rangos se añaden a sus valores padres

```
<?php
$date = new DateTimeImmutable('2001-01-01');

$newDate = $date->setTime(14, 55, 24);
echo $newDate->format('Y-m-d H:i:s') . "\n";

$newDate = $date->setTime(14, 55, 65);
echo $newDate->format('Y-m-d H:i:s') . "\n";

$newDate = $date->setTime(14, 65, 24);
echo $newDate->format('Y-m-d H:i:s') . "\n";

$newDate = $date->setTime(25, 55, 24);
echo $newDate->format('Y-m-d H:i:s') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2001-01-01 14:55:24
    2001-01-01 14:56:05
    2001-01-01 15:05:24
    2001-01-02 01:55:24

## Véase también

DateTimeImmutable::setDate

DateTimeImmutable::setISODate
