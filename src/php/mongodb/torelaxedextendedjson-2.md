---
title: MongoDB\BSON\PackedArray::toRelaxedExtendedJSON
description: Devuelve la representación JSON extendida relajada del array BSON
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.torelaxedextendedjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/torelaxedextendedjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48220
---

MongoDB\BSON\PackedArray::toRelaxedExtendedJSON

Devuelve la representación JSON extendida relajada del array BSON

## Descripción

```php
final public MongoDB\BSON\PackedArray::toRelaxedExtendedJSON(): string
```php

Convierte el array BSON en su representación [JSON extendida relajada](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#relaxed-extended-json-example). El formato relajado prefiere el uso de los tipos primitivos JSON en detrimento de la fidelidad de los tipos y es el más adecuado para producir una salida que puede ser fácilmente consumida por APIs web y humanos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string que contiene la representación [JSON extendida relajada](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#relaxed-extended-json-example) del array BSON.

## Ejemplos

Ejemplo de MongoDB\BSON\PackedArray::toRelaxedExtendedJSON

```
    
<?php

$array = [
    'foo',
    123,
    4294967295,
    new MongoDB\BSON\ObjectId('56315a7c6118fd1b920270b1'),
];

$packedArray = MongoDB\BSON\PackedArray::fromPHP($array);
echo $packedArray->toRelaxedExtendedJSON(), "\n";

?>

   
```php

El ejemplo anterior mostrará:

        
    [ "foo", 123, 4294967295, { "$oid" : "56315a7c6118fd1b920270b1" } ]

## Véase también

MongoDB\BSON\PackedArray::fromJSON

MongoDB\BSON\PackedArray::toCanonicalExtendedJSON

MongoDB\BSON\toRelaxedExtendedJSON

Especificación del JSON extendido

Tipos BSON
