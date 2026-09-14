---
title: MongoDB\Driver\ReadPreference::bsonSerialize
description: Devuelve un objeto para la serialización BSON
source_url: https://www.php.net/manual/es/mongodb-driver-readpreference.bsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference/bsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50860
---

MongoDB\Driver\ReadPreference::bsonSerialize

Devuelve un objeto para la serialización BSON

## Descripción

```php
final public MongoDB\Driver\ReadPreference::bsonSerialize(): stdClass
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto para la serialización de la ReadPreference en BSON.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

`MongoDB\Driver\ReadPreference::bsonSerialize` con una preferencia de lectura primaria

```
<?php

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::PRIMARY);
var_dump($rp->bsonSerialize());

echo "\n", MongoDB\BSON\Document::fromPHP($rp)->toRelaxedExtendedJSON();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (1) {
      ["mode"]=>
      string(7) "primary"
    }

    { "mode" : "primary" }

`MongoDB\Driver\ReadPreference::bsonSerialize` con una preferencia de lectura secundaria

```
<?php

$rp = new MongoDB\Driver\ReadPreference(
    MongoDB\Driver\ReadPreference::SECONDARY,
    [
        ['dc' => 'ny'],
        ['dc' => 'sf', 'use' => 'reporting'],
        []
    ]
);
var_dump($rp->bsonSerialize());

echo "\n", MongoDB\BSON\toJSON(MongoDB\BSON\fromPHP($rp));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (2) {
      ["mode"]=>
      string(9) "secondary"
      ["tags"]=>
      array(3) {
        [0]=>
        object(stdClass)#1 (1) {
          ["dc"]=>
          string(2) "ny"
        }
        [1]=>
        object(stdClass)#5 (2) {
          ["dc"]=>
          string(2) "sf"
          ["use"]=>
          string(9) "reporting"
        }
        [2]=>
        object(stdClass)#4 (0) {
        }
      }
    }

    { "mode" : "secondary", "tags" : [ { "dc" : "ny" }, { "dc" : "sf", "use" : "reporting" }, {  } ] }

`MongoDB\Driver\ReadPreference::bsonSerialize` con una preferencia de lectura secundaria y un tiempo máximo de retraso

```
<?php

$rp = new MongoDB\Driver\ReadPreference(
    MongoDB\Driver\ReadPreference::SECONDARY,
    null,
    ['maxStalenessSeconds' => 120]
);
var_dump($rp->bsonSerialize());

echo "\n", MongoDB\BSON\Document::fromPHP($rp)->toRelaxedExtendedJSON();

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#2 (2) {
      ["mode"]=>
      string(9) "secondary"
      ["maxStalenessSeconds"]=>
      int(120)
    }

    { "mode" : "secondary", "maxStalenessSeconds" : 120 }

## Véase también

MongoDB\BSON\Serializable::bsonSerialize

Referencia de Read Preference
