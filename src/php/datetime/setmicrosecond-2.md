---
title: DateTimeImmutable::setMicrosecond
description: Establece la parte de microsegundos de la hora
source_url: https://www.php.net/manual/es/datetimeimmutable.setmicrosecond.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/setmicrosecond.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 726154e3c
order: 10680
---

DateTimeImmutable::setMicrosecond

Establece la parte de microsegundos de la hora

## Descripción

```php
#[\NoDiscard(message: "as DateTimeImmutable::setMicrosecond() does not modify the object itself")] public DateTimeImmutable::setMicrosecond(int $microsecond): static
```php

Devuelve un nuevo objeto `DateTimeImmutable` construido a partir del antiguo, con la parte de microsegundos modificada.

## Parámetros

`microsecond`  
El valor de microsegundos a establecer (de `0` a `999999`).

## Valores devueltos

Retorna un nuevo objeto `DateTimeImmutable` con los datos modificados.

## Errores/Excepciones

Si `microsecond` está fuera del rango \[`0`, `999999`\], se lanza una DateRangeError.

## Ejemplos

Ejemplo de DateTimeImmutable::setMicrosecond

```
<?php
$date = DateTimeImmutable::createFromTimestamp(123.456789);
echo $date->format('Y-m-d H:i:s.u') . PHP_EOL;
$date = $date->setMicrosecond(987654);
echo $date->format('Y-m-d H:i:s.u') . PHP_EOL;
?>

   
```php

El ejemplo anterior mostrará:

    1970-01-01 00:02:03.456789
    1970-01-01 00:02:03.987654

## Véase también

DateTimeInterface::getMicrosecond
