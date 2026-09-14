---
title: MongoDB\BSON\ObjectId::__toString
description: Devuelve la representación hexadecimal de este ObjectId
source_url: https://www.php.net/manual/es/mongodb-bson-objectid.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/objectid/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 48050
---

MongoDB\BSON\ObjectId::\_\_toString

Devuelve la representación hexadecimal de este ObjectId

## Descripción

```php
final public MongoDB\BSON\ObjectId::__toString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación hexadecimal de este ObjectId.

## Ejemplos

Ejemplo con `MongoDB\BSON\ObjectId::__toString`

```
<?php

var_dump((string) new MongoDB\BSON\ObjectId());
var_dump((string) new MongoDB\BSON\ObjectId('000000000000000000000001'));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(24) "56731b49da14d8747d701211"
    string(24) "000000000000000000000001"

## Véase también

La referencia ObjectId

El tipo BSON : ObjectId
