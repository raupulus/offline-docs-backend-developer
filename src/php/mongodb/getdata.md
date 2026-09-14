---
title: MongoDB\BSON\Binary::getData
description: Devuelve los datos de Binary
source_url: https://www.php.net/manual/es/mongodb-bson-binary.getdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/getdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47360
---

MongoDB\BSON\Binary::getData

Devuelve los datos de Binary

## Descripción

```php
final public MongoDB\BSON\Binary::getData(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los datos de Binary.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\BSON\Binary::getData`

```
<?php

$binary = new MongoDB\BSON\Binary('foo', MongoDB\BSON\Binary::TYPE_GENERIC);
var_dump($binary->getData());

?>

   
```php

El ejemplo anterior mostrará:

    string(3) "foo"

## Véase también

Tipos BSON
