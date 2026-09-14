---
title: MongoDB\BSON\PackedArray::toCanonicalExtendedJSON
description: Devuelve la representación JSON extendida canónica del array BSON
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.tocanonicalextendedjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/tocanonicalextendedjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48200
---

MongoDB\BSON\PackedArray::toCanonicalExtendedJSON

Devuelve la representación JSON extendida canónica del array BSON

## Descripción

```php
final public MongoDB\BSON\PackedArray::toCanonicalExtendedJSON(): string
```php

Convierte el array BSON en su representación [JSON extendida canónica](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#canonical-extended-json-example). El formato canónico privilegia la fidelidad de los tipos en detrimento de la concisión de la salida y es el más adecuado para producir una salida que puede ser convertida en BSON sin pérdida de información de tipo (por ejemplo, los tipos numéricos permanecerán diferenciados).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string que contiene la representación [JSON extendida canónica](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#canonical-extended-json-example) del array BSON.

## Ejemplos

Ejemplo de MongoDB\BSON\PackedArray::toCanonicalExtendedJSON

```
    
<?php

$array = [
    'foo',
    123,
    4294967295,
    new MongoDB\BSON\ObjectId('56315a7c6118fd1b920270b1'),
];

$packedArray = MongoDB\BSON\PackedArray::fromPHP($array);
echo $packedArray->toCanonicalExtendedJSON(), "\n";

?>

   
```php

El ejemplo anterior mostrará:

        
    [ "foo", { "$numberInt" : "123" }, { "$numberLong" : "4294967295" }, { "$oid" : "56315a7c6118fd1b920270b1" } ]

## Véase también

MongoDB\BSON\PackedArray::fromJSON

MongoDB\BSON\PackedArray::toRelaxedExtendedJSON

MongoDB\BSON\toCanonicalExtendedJSON

Especificación del JSON extendido

Tipos BSON
