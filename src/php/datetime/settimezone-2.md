---
title: DateTimeImmutable::setTimezone
description: Establece la zona horaria
source_url: https://www.php.net/manual/es/datetimeimmutable.settimezone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/settimezone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10710
---

DateTimeImmutable::setTimezone

Establece la zona horaria

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::setTimezone() does not modify the object itself")] public DateTimeImmutable::setTimezone(DateTimeZone $timezone): DateTimeImmutable
```php

Devuelve un nuevo objeto DateTimeImmutable con una nueva zona horaria establecida.

## Parámetros

`timezone`  
Un objeto `DateTimeZone` que representa la zona horaria deseada.

## Valores devueltos

Devuelve un nuevo objeto `DateTimeImmutable` modificado para encadenar métodos. El instante subyacente no se modifica al llamar a este método.

## Ejemplos

Ejemplo de `DateTimeImmutable::setTimeZone`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable('2000-01-01', new DateTimeZone('Pacific/Nauru'));
echo $date->format('Y-m-d H:i:sP') . "\n";

$newDate = $date->setTimezone(new DateTimeZone('Pacific/Chatham'));
echo $newDate->format('Y-m-d H:i:sP') . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    2000-01-01 00:00:00+12:00
    2000-01-01 01:45:00+13:45

## Véase también

DateTimeImmutable::getTimezone

DateTimeZone::\_\_construct
