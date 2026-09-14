---
title: MongoDB\Driver\ReadConcern::bsonSerialize
description: Devuelve un objeto para la serialización BSON
source_url: https://www.php.net/manual/es/mongodb-driver-readconcern.bsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readconcern/bsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50810
---

MongoDB\Driver\ReadConcern::bsonSerialize

Devuelve un objeto para la serialización BSON

## Descripción

```php
final public MongoDB\Driver\ReadConcern::bsonSerialize(): stdClass
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto para la serialización del ReadConcern en BSON.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

`MongoDB\Driver\ReadConcern::bsonSerialize` con un read concern vacío

```
<?php

$rc = new MongoDB\Driver\ReadConcern;
var_dump($rc->bsonSerialize());

echo "\n", MongoDB\BSON\Document::fromPHP($rc)->toRelaxedExtendedJSON();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (0) {
    }

    { }

`MongoDB\Driver\ReadConcern::bsonSerialize` con un read concern local

```
<?php

$rc = new MongoDB\Driver\ReadConcern(MongoDB\Driver\ReadConcern::LOCAL);
var_dump($rc->bsonSerialize());

echo "\n", MongoDB\BSON\Document::fromPHP($rc)->toRelaxedExtendedJSON();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (1) {
      ["level"]=>
      string(5) "local"
    }

    { "level" : "local" }

## Véase también

MongoDB\BSON\Serializable::bsonSerialize

Referencia de Read Concern
