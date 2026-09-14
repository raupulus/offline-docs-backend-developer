---
title: MongoDB\Driver\WriteConcern::bsonSerialize
description: Devuelve un objeto para la serialización BSON
source_url: https://www.php.net/manual/es/mongodb-driver-writeconcern.bsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcern/bsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51460
---

MongoDB\Driver\WriteConcern::bsonSerialize

Devuelve un objeto para la serialización BSON

## Descripción

```php
final public MongoDB\Driver\WriteConcern::bsonSerialize(): stdClass
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto para la serialización del WriteConcern en BSON.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

`MongoDB\Driver\WriteConcern::bsonSerialize` con el write concern majority

```
<?php

$wc = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY);
var_dump($wc->bsonSerialize());

echo "\n", MongoDB\BSON\Document::fromPHP($wc)->toRelaxedExtendedJSON();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (1) {
      ["w"]=>
      string(8) "majority"
    }

    { "w" : "majority" }

`MongoDB\Driver\WriteConcern::bsonSerialize` con el wtimeout y el journal

```
<?php

$wc = new MongoDB\Driver\WriteConcern(2, 1000, true);
var_dump($wc->bsonSerialize());

echo "\n", MongoDB\BSON\Document::fromPHP($wc)->toRelaxedExtendedJSON();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (3) {
      ["w"]=>
      int(2)
      ["j"]=>
      bool(true)
      ["wtimeout"]=>
      int(1000)
    }

    { "w" : 2, "j" : true, "wtimeout" : 1000 }

## Véase también

MongoDB\BSON\Serializable::bsonSerialize

Referencia de Write Concern
