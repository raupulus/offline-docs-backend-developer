---
title: MongoDB\BSON\PackedArray::fromJSON
description: Construye una nueva instancia de array BSON a partir de un string JSON
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.fromjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/fromjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48110
---

MongoDB\BSON\PackedArray::fromJSON

Construye una nueva instancia de array BSON a partir de un string JSON

## Descripción

```php
final static public MongoDB\BSON\PackedArray::fromJSON(string $json): MongoDB\BSON\PackedArray
```php

Convierte un string [JSON extendido](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/) en su representación BSON.

## Parámetros

`json` (`string`)  
El valor JSON a convertir.

## Valores devueltos

Devuelve una nueva instancia de `MongoDB\BSON\PackedArray`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\UnexpectedValueException

si el valor JSON no puede ser convertido en un array BSON (por ejemplo, debido a un error de sintaxis).

## Ejemplos

Ejemplo de MongoDB\BSON\PackedArray::fromJSON

```
    
<?php

$json = '[ "foo", { "$numberInt" : "123" }, { "$numberLong" : "4294967295" }, { "$oid" : "56315a7c6118fd1b920270b1" } ]';
$packedArray = MongoDB\BSON\PackedArray::fromJSON($json);
var_dump($packedArray);

?>

   
```php

El ejemplo anterior mostrará:

        
    object(MongoDB\BSON\PackedArray)#1 (2) {
      ["data"]=>
      string(68) "MQAAAAIwAAQAAABmb28AEDEAewAAABIyAP////8AAAAABzMAVjFafGEY/RuSAnCxAA=="
      ["value"]=>
      array(4) {
        [0]=>
        string(3) "foo"
        [1]=>
        int(123)
        [2]=>
        int(4294967295)
        [3]=>
        object(MongoDB\BSON\ObjectId)#2 (1) {
          ["oid"]=>
          string(24) "56315a7c6118fd1b920270b1"
        }
      }
    }

## Véase también

MongoDB\BSON\PackedArray::fromPHP

Json extendido de MongoDB

Tipos BSON
