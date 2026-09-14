---
title: MongoDB\BSON\UTCDateTime::__toString
description: Devuelve la representación en forma de string de este UTCDateTime
source_url: https://www.php.net/manual/es/mongodb-bson-utcdatetime.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/utcdatetime/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48640
---

MongoDB\BSON\UTCDateTime::\_\_toString

Devuelve la representación en forma de string de este UTCDateTime

## Descripción

```php
final public MongoDB\BSON\UTCDateTime::__toString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación en forma de string de este UTCDateTime.

## Ejemplos

Ejemplo de `MongoDB\BSON\UTCDateTime::__toString`

```
<?php

$utcdatetime = new MongoDB\BSON\UTCDateTime(1416445411987);
var_dump((string) $utcdatetime);

?>

   
```php

El ejemplo anterior mostrará:

    string(13) "1416445411987"

## Véase también

Tipos BSON: Fecha
