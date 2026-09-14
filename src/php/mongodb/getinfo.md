---
title: MongoDB\Driver\Server::getInfo
description: Devuelve un array de información que describe este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.getinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/getinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51030
---

MongoDB\Driver\Server::getInfo

Devuelve un array de información que describe este servidor

## Descripción

```php
final public MongoDB\Driver\Server::getInfo(): array
```php

Devuelve un array de información que describe el servidor. Este array se deriva de la respuesta más reciente a la comando [hello](https://www.mongodb.com/docs/manual/reference/command/hello/) obtenida por la [supervisión del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md).

> [!NOTE]
> Cuando el controlador está conectado a un balanceador de carga, este método devuelve la respuesta al comando [hello](https://www.mongodb.com/docs/manual/reference/command/hello/) del servidor de respaldo durante el apretón de manos inicial de la conexión. Esto contrasta con otros métodos (por ejemplo, `MongoDB\Driver\Server::getType`), que devolverán información sobre el balanceador de carga mismo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de información que describe este servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\Server::getInfo`

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017/');

$rp = new MongoDB\Driver\ReadPreference('primary');
$server = $manager->selectServer($rp);

var_dump($server->getInfo());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(23) {
      ["helloOk"]=>
      bool(true)
      ["topologyVersion"]=>
      array(2) {
        ["processId"]=>
        object(MongoDB\BSON\ObjectId)#4 (1) {
          ["oid"]=>
          string(24) "617b6d696a3a89d2f77e6df0"
        }
        ["counter"]=>
        int(6)
      }
      ["hosts"]=>
      array(1) {
        [0]=>
        string(15) "localhost:27017"
      }
      ["setName"]=>
      string(3) "rs0"
      ["setVersion"]=>
      int(1)
      ["ismaster"]=>
      bool(true)
      ["secondary"]=>
      bool(false)
      ["primary"]=>
      string(15) "localhost:27017"
      ["me"]=>
      string(15) "localhost:27017"
      ["electionId"]=>
      object(MongoDB\BSON\ObjectId)#5 (1) {
        ["oid"]=>
        string(24) "7fffffff0000000000000001"
      }
      ["lastWrite"]=>
      array(4) {
        ["opTime"]=>
        array(2) {
          ["ts"]=>
          object(MongoDB\BSON\Timestamp)#6 (2) {
            ["increment"]=>
            string(1) "1"
            ["timestamp"]=>
            string(10) "1635478989"
          }
          ["t"]=>
          int(1)
        }
        ["lastWriteDate"]=>
        object(MongoDB\BSON\UTCDateTime)#7 (1) {
          ["milliseconds"]=>
          string(13) "1635478989000"
        }
        ["majorityOpTime"]=>
        array(2) {
          ["ts"]=>
          object(MongoDB\BSON\Timestamp)#8 (2) {
            ["increment"]=>
            string(1) "1"
            ["timestamp"]=>
            string(10) "1635478989"
          }
          ["t"]=>
          int(1)
        }
        ["majorityWriteDate"]=>
        object(MongoDB\BSON\UTCDateTime)#9 (1) {
          ["milliseconds"]=>
          string(13) "1635478989000"
        }
      }
      ["maxBsonObjectSize"]=>
      int(16777216)
      ["maxMessageSizeBytes"]=>
      int(48000000)
      ["maxWriteBatchSize"]=>
      int(100000)
      ["localTime"]=>
      object(MongoDB\BSON\UTCDateTime)#10 (1) {
        ["milliseconds"]=>
        string(13) "1635478992136"
      }
      ["logicalSessionTimeoutMinutes"]=>
      int(30)
      ["connectionId"]=>
      int(3)
      ["minWireVersion"]=>
      int(0)
      ["maxWireVersion"]=>
      int(13)
      ["readOnly"]=>
      bool(false)
      ["ok"]=>
      float(1)
      ["$clusterTime"]=>
      array(2) {
        ["clusterTime"]=>
        object(MongoDB\BSON\Timestamp)#11 (2) {
          ["increment"]=>
          string(1) "1"
          ["timestamp"]=>
          string(10) "1635478989"
        }
        ["signature"]=>
        array(2) {
          ["hash"]=>
          object(MongoDB\BSON\Binary)#12 (2) {
            ["data"]=>
            string(20) ""
            ["type"]=>
            int(0)
          }
          ["keyId"]=>
          int(0)
        }
      }
      ["operationTime"]=>
      object(MongoDB\BSON\Timestamp)#13 (2) {
        ["increment"]=>
        string(1) "1"
        ["timestamp"]=>
        string(10) "1635478989"
      }
    }

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.11.0 | Cuando el controlador está conectado a un balanceador de carga, este método devuelve la respuesta al comando `hello` del servidor de respaldo a partir del apretón de manos de conexión inicial. |

## Véase también

MongoDB\Driver\ServerDescription::getHelloResponse

Comando

hello

en el manual de MongoDB

Especificación de la detección y supervisión de servidores
