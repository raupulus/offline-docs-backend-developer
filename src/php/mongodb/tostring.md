---
title: MongoDB\BSON\Binary::__toString
description: Devuelve los datos de Binary
source_url: https://www.php.net/manual/es/mongodb-bson-binary.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47410
---

MongoDB\BSON\Binary::\_\_toString

Devuelve los datos de Binary

## Descripción

```php
final public MongoDB\BSON\Binary::__toString(): string
```php

Este método es un alias de: MongoDB\BSON\Binary::getData.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los datos de Binary.

## Ejemplos

Ejemplo con `MongoDB\BSON\Binary::__toString`

```
<?php

var_dump((string) new MongoDB\BSON\Binary('foo', MongoDB\BSON\Binary::TYPE_GENERIC));

?>

   
```php

El ejemplo anterior mostrará:

    string(3) "foo"

## Véase también

MongoDB\BSON\Binary::getData

Tipos BSON
