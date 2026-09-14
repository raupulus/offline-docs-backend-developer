---
title: MongoDB\BSON\Binary::getType
description: Devuelve el tipo de Binary
source_url: https://www.php.net/manual/es/mongodb-bson-binary.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47370
---

MongoDB\BSON\Binary::getType

Devuelve el tipo de Binary

## Descripción

```php
final public MongoDB\BSON\Binary::getType(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tipo de Binary.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\BSON\Binary::getType`

```
<?php

$binary = new MongoDB\BSON\Binary('foo', MongoDB\BSON\Binary::TYPE_GENERIC);
var_dump($binary->getType());

?>

   
```php

El ejemplo anterior mostrará:

    int(0)

## Véase también

Tipos BSON
