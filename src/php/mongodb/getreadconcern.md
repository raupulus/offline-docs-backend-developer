---
title: MongoDB\Driver\Manager::getReadConcern
description: Devuelve el ReadConcern para el Manager
source_url: https://www.php.net/manual/es/mongodb-driver-manager.getreadconcern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/getreadconcern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49800
---

MongoDB\Driver\Manager::getReadConcern

Devuelve el ReadConcern para el Manager

## Descripción

```php
final public MongoDB\Driver\Manager::getReadConcern(): MongoDB\Driver\ReadConcern
```php

Devuelve el `MongoDB\Driver\ReadConcern` para el Manager, que se deriva de sus opciones URI. Es el ReadConcern por omisión para las peticiones y comandos ejecutados en el Manager.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El `MongoDB\Driver\ReadConcern` para el Manager.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo `MongoDB\Driver\Manager::getReadConcern`

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
var_dump($manager->getReadConcern());

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017/?readConcernLevel=local');
var_dump($manager->getReadConcern());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\ReadConcern)#2 (0) {
    }
    object(MongoDB\Driver\ReadConcern)#1 (1) {
      ["level"]=>
      string(5) "local"
    }

## Véase también

MongoDB\Driver\ReadConcern

MongoDB\Driver\Manager::\_\_construct
