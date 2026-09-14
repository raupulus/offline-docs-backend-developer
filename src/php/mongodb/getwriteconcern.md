---
title: MongoDB\Driver\Manager::getWriteConcern
description: Devuelve el WriteConcern para el Manager
source_url: https://www.php.net/manual/es/mongodb-driver-manager.getwriteconcern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/getwriteconcern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49830
---

MongoDB\Driver\Manager::getWriteConcern

Devuelve el WriteConcern para el Manager

## Descripción

```php
final public MongoDB\Driver\Manager::getWriteConcern(): MongoDB\Driver\WriteConcern
```php

Devuelve el `MongoDB\Driver\WriteConcern` para el Manager, que se deriva de sus opciones URI. Es el WriteConcern por omisión para las escrituras y comandos ejecutados en el Manager.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El `MongoDB\Driver\WriteConcern` para el Manager.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\Manager::getWriteConcern`

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
var_dump($manager->getWriteConcern());

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017/?w=majority&wtimeoutMS=2000');
var_dump($manager->getWriteConcern());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\WriteConcern)#2 (0) {
    }
    object(MongoDB\Driver\WriteConcern)#1 (2) {
      ["w"]=>
      string(8) "majority"
      ["wtimeout"]=>
      int(2000)
    }

## Véase también

MongoDB\Driver\WriteConcern

MongoDB\Driver\Manager::\_\_construct
