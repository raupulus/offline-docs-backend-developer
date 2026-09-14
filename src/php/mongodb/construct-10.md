---
title: MongoDB\BSON\ObjectId::__construct
description: Construye un nuevo ObjectId
source_url: https://www.php.net/manual/es/mongodb-bson-objectid.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/objectid/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48020
---

MongoDB\BSON\ObjectId::\_\_construct

Construye un nuevo ObjectId

## Descripción

```php
final public MongoDB\BSON\ObjectId::__construct([string $id])
```php

## Parámetros

`id` (`string`)  
Una cadena hexadecimal de 24 caracteres. Si no se proporciona, la extensión generará un ObjectId.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

id

no es una cadena hexadecimal de 24 caracteres.

## Ejemplos

Ejemplo con `MongoDB\BSON\ObjectId::__construct`

```
<?php

var_dump(new MongoDB\BSON\ObjectId());

var_dump(new MongoDB\BSON\ObjectId('000000000000000000000001'));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\ObjectId)#1 (1) {
      ["oid"]=>
      string(24) "56732d3dda14d81214634921"
    }
    object(MongoDB\BSON\ObjectId)#1 (1) {
      ["oid"]=>
      string(24) "000000000000000000000001"
    }

## Véase también

La referencia ObjectId

El tipo BSON : ObjectId
