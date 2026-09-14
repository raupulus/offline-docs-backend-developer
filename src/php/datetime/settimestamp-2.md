---
title: DateTimeImmutable::setTimestamp
description: Establece la fecha y hora basadas en una marca de tiempo Unix (Unix timestamp)
source_url: https://www.php.net/manual/es/datetimeimmutable.settimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/settimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 726154e3c
order: 10700
---

DateTimeImmutable::setTimestamp

Establece la fecha y hora basadas en una marca de tiempo Unix (Unix timestamp)

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::setTimestamp() does not modify the object itself")] public DateTimeImmutable::setTimestamp(int $timestamp): DateTimeImmutable
```php

Devuelve un nuevo objeto `DateTimeImmutable` construido a partir del antiguo, con la fecha y hora establecidas basadas en una marca de tiempo Unix.

## Parámetros

`timestamp`  
Una marca de tiempo Unix representando la fecha. Establecer marcas de tiempo fuera del rango de `int` es posible usando DateTimeImmutable::modify con el formato `@`.

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Ejemplos

Ejemplo de `DateTimeImmutable::setTimestamp`

Estilo orientado a objetos

```
<?php
$date = new DateTimeImmutable();
echo $date->format('U = Y-m-d H:i:s') . "\n";

$newDate = $date->setTimestamp(1171502725);
echo $newDate->format('U = Y-m-d H:i:s') . "\n";

   
```php

Resultado del ejemplo anterior es similar a:

    1272508903 = 2010-04-28 22:41:43
    1171502725 = 2007-02-14 20:25:25

## Véase también

DateTimeImmutable::getTimestamp

DateTimeImmutable::setMicrosecond
