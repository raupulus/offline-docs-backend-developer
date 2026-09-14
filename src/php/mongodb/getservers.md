---
title: MongoDB\Driver\Manager::getServers
description: Devolver los servidores a los que está conectado este gestor
source_url: https://www.php.net/manual/es/mongodb-driver-manager.getservers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/getservers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49820
---

MongoDB\Driver\Manager::getServers

Devolver los servidores a los que está conectado este gestor

## Descripción

```php
final public MongoDB\Driver\Manager::getServers(): array
```php

Devuelve un `array` de instancias `MongoDB\Driver\Server` a las que está conectado este gestor.

> [!NOTE]
> Dado que el controlador se conecta perezosamente a la base de datos, este método puede devolver un `array` vacío si se llama antes de ejecutar una operación en el `MongoDB\Driver\Manager`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` de instancias `MongoDB\Driver\Server` a las que está conectado este gestor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\Manager::getServers`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

/* El controlador se conecta al servidor de la base de datos de manera perezosa, por lo que Manager::getServers()
 * puede devolver inicialmente un array vacío. */
var_dump($manager->getServers());

$command = new MongoDB\Driver\Command(['ping' => 1]);
$manager->executeCommand('db', $command);

var_dump($manager->getServers());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(0) {
    }
    array(1) {
      [0]=>
      object(MongoDB\Driver\Server)#3 (10) {
        ["host"]=>
        string(9) "localhost"
        ["port"]=>
        int(27017)
        ["type"]=>
        int(1)
        ["is_primary"]=>
        bool(false)
        ["is_secondary"]=>
        bool(false)
        ["is_arbiter"]=>
        bool(false)
        ["is_hidden"]=>
        bool(false)
        ["is_passive"]=>
        bool(false)
        ["last_hello_response"]=>
        array(8) {
          ["isWritablePrimary"]=>
          bool(true)
          ["maxBsonObjectSize"]=>
          int(16777216)
          ["maxMessageSizeBytes"]=>
          int(48000000)
          ["maxWriteBatchSize"]=>
          int(1000)
          ["localTime"]=>
          object(MongoDB\BSON\UTCDateTime)#4 (1) {
            ["milliseconds"]=>
            int(1447267964517)
          }
          ["maxWireVersion"]=>
          int(3)
          ["minWireVersion"]=>
          int(0)
          ["ok"]=>
          float(1)
        }
        ["round_trip_time"]=>
        int(554)
      }
    }

## Véase también

MongoDB\Driver\Server

MongoDB\Driver\Manager::selectServer
