---
title: MongoDB\BSON\Timestamp::__toString
description: Devuelve la representación en string de este Timestamp
source_url: https://www.php.net/manual/es/mongodb-bson-timestamp.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/timestamp/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48470
---

MongoDB\BSON\Timestamp::\_\_toString

Devuelve la representación en string de este Timestamp

## Descripción

```php
final public MongoDB\BSON\Timestamp::__toString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación en string de este Timestamp.

## Ejemplos

Ejemplo de `MongoDB\BSON\Timestamp::__toString`

```
<?php

$timestamp = new MongoDB\BSON\Timestamp(1234, 5678);
var_dump((string) $timestamp);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "[1234:5678]"

## Véase también

Tipos BSON: Timestamps
