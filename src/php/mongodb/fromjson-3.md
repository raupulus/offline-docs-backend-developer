---
title: MongoDB\BSON\fromJSON
description: Devuelve la representación BSON de un valor JSON
source_url: https://www.php.net/manual/es/function.mongodb.bson-fromjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/bson/fromjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48750
---

MongoDB\BSON\fromJSON

Devuelve la representación BSON de un valor JSON

> [!WARNING]
> Esta función ha sido *DEPRECADA* a partir de la versión 1.20.0 de la extensión y fue eliminada en la versión 2.0. Las aplicaciones deben usar MongoDB\BSON\Document::fromJSON en su lugar.

## Descripción

```php
MongoDB\BSON\fromJSON(string $json): string
```php

Convierte una cadena de [JSON extendido](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/) a su representación BSON.

## Parámetros

`json` (`string`)  
Valor JSON que se desea convertir.

## Valores devueltos

El documento BSON serializado como una cadena binaria.

## Errores/Excepciones

Lanza

MongoDB\Driver\Exception\UnexpectedValueException

si el valor JSON no puede convertirse a BSON (por ejemplo, debido a un error de sintaxis).

## Historial de cambios

| Versión            | Descripción                     |
|--------------------|---------------------------------|
| PECL mongodb 2.0.0 | Esta función ha sido eliminada. |

## Ejemplos

Ejemplo de `MongoDB\BSON\fromJSON`

```
<?php

$json = '{ "_id": { "$oid": "563143b280d2387c91807965" } }';
$bson = MongoDB\BSON\fromJSON($json);
$value = MongoDB\BSON\toPHP($bson);
var_dump($value);

?>

   
```php

El ejemplo anterior mostrará:

    object(stdClass)#2 (1) {
      ["_id"]=>
      object(MongoDB\BSON\ObjectId)#1 (1) {
        ["oid"]=>
        string(24) "563143b280d2387c91807965"
      }
    }

## Véase también

MongoDB\BSON\Document::fromJSON

MongoDB\BSON\toJSON

JSON Extendido de MongoDB

BSON de MongoDB
