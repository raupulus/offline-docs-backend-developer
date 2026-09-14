---
title: La clase MongoDB\Driver\Command
source_url: https://www.php.net/manual/es/class.mongodb-driver-command.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/command.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49230
---

## Introducción

La clase `MongoDB\Driver\Command` es un objeto valor que representa un comando de base de datos.

Para proporcionar “asistentes de comandos” el objeto `MongoDB\Driver\Command` debe estar compuesto.

## Sinopsis de la clase

MongoDB\Driver\Command

final

MongoDB\Driver\Command

Métodos

## Ejemplos

Composición de `MongoDB\Driver\Command` para proporcionar un asistente para crear colecciones

```php
<?php
class CreateCollection {
    protected $cmd = array();

    function __construct($collectionName) {
        $this->cmd["create"] = (string) $collectionName;
    }
    function setCappedCollection($maxBytes, $maxDocuments = false) {
        $this->cmd["capped"] = true;
        $this->cmd["size"]   = (int) $maxBytes;

        if ($maxDocuments) {
            $this->cmd["max"] = (int) $maxDocuments;
        }
    }
    function usePowerOf2Sizes($bool) {
        if ($bool) {
            $this->cmd["flags"] = 1;
        } else {
            $this->cmd["flags"] = 0;
        }
    }
    function setFlags($flags) {
        $this->cmd["flags"] = (int) $flags;
    }
    function getCommand() {
        return new MongoDB\Driver\Command($this->cmd);
    }
    function getCollectionName() {
        return $this->cmd["create"];
    }
}

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

$createCollection = new CreateCollection("cappedCollection");
$createCollection->setCappedCollection(64 * 1024);

try {
    $command = $createCollection->getCommand();
    $cursor = $manager->executeCommand("databaseName", $command);
    $response = $cursor->toArray()[0];
    var_dump($response);

    $collstats = ["collstats" => $createCollection->getCollectionName()];
    $cursor = $manager->executeCommand("databaseName", new MongoDB\Driver\Command($collstats));
    $response = $cursor->toArray()[0];
    var_dump($response);
} catch(MongoDB\Driver\Exception $e) {
    echo $e->getMessage(), "\n";
    exit;
}

?>

    
```

El ejemplo anterior mostrará:

```php
object(MongoDB\Driver\Command)#3 (1) {
  ["command"]=>
  array(3) {
    ["create"]=>
    string(16) "cappedCollection"
    ["capped"]=>
    bool(true)
    ["size"]=>
    int(65536)
  }
}
array(1) {
  ["ok"]=>
  float(1)
}
array(16) {
  ["ns"]=>
  string(29) "databaseName.cappedCollection"
  ["count"]=>
  int(0)
  ["size"]=>
  int(0)
  ["numExtents"]=>
  int(1)
  ["storageSize"]=>
  int(65536)
  ["nindexes"]=>
  int(1)
  ["lastExtentSize"]=>
  float(65536)
  ["paddingFactor"]=>
  float(1)
  ["paddingFactorNote"]=>
  string(101) "paddingFactor is unused and unmaintained in 2.8. It remains hard coded to 1.0 for compatibility only."
  ["userFlags"]=>
  int(0)
  ["capped"]=>
  bool(true)
  ["max"]=>
  int(9223372036854775807)
  ["maxSize"]=>
  int(65536)
  ["totalIndexSize"]=>
  int(8176)
  ["indexSizes"]=>
  object(stdClass)#4 (1) {
    ["_id_"]=>
    int(8176)
  }
  ["ok"]=>
  float(1)
}

   
```
