---
title: MongoDB\BSON\UTCDateTime::toDateTime
description: Devuelve la representación DateTime de este UTCDateTime
source_url: https://www.php.net/manual/es/mongodb-bson-utcdatetime.todatetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/utcdatetime/todatetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48620
---

MongoDB\BSON\UTCDateTime::toDateTime

Devuelve la representación DateTime de este UTCDateTime

## Descripción

```php
final public MongoDB\BSON\UTCDateTime::toDateTime(): DateTime
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación `DateTime` de este UTCDateTime. El `DateTime` devuelto utilizará la zona horaria UTC.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\BSON\UTCDatetime::toDateTime`

```
<?php

$utcdatetime = new MongoDB\BSON\UTCDateTime(1416445411987);
$datetime = $utcdatetime->toDateTime();
var_dump($datetime->format('r'));
var_dump($datetime->format('U.u'));
var_dump($datetime->getTimezone());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(31) "Thu, 20 Nov 2014 01:03:31 +0000"
    string(17) "1416445411.987000"
    object(DateTimeZone)#3 (2) {
      ["timezone_type"]=>
      int(1)
      ["timezone"]=>
      string(6) "+00:00"
    }

## Véase también

MongoDB\BSON\UTCDateTime::toDateTimeImmutable

Tipos BSON: Fecha
