---
title: La clase MongoDB\Driver\ServerApi
source_url: https://www.php.net/manual/es/class.mongodb-driver-serverapi.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverapi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51170
---

## Introducción

## Sinopsis de la clase

MongoDB\Driver\ServerApi

final

MongoDB\Driver\ServerApi

MongoDB\BSON\Serializable

Serializable

Constantes

const

string

MongoDB\Driver\ServerAPI::V1

"1"

Métodos

## Constantes predefinidas

`MongoDB\Driver\ServerApi::V1`  
Versión 1 de la API del servidor.

## Ejemplos

Declarar una versión de API en un gestor

```php
<?php

use MongoDB\Driver\Manager;
use MongoDB\Driver\ServerApi;

$v1 = new ServerApi(ServerApi::v1);
$manager = new Manager('mongodb://localhost:27017', [], ['serverApi' => $v1]);

$command = new MongoDB\Driver\Command(['buildInfo' => 1]);

try {
    $cursor = $manager->executeCommand('admin', $command);
} catch(MongoDB\Driver\Exception $e) {
    echo $e->getMessage(), "\n";
    exit;
}

/* El comando buildInfo devuelve un único documento de resultado, por lo que
 * necesitamos acceder al primer resultado en el cursor. */
$buildInfo = $cursor->toArray()[0];

echo $buildInfo->version, "\n";

?>

    
```

El ejemplo anterior mostrará:

    4.9.0-alpha7-49-gb968ca0

Declarar una versión estricta de API en un gestor

El siguiente ejemplo establece la `strict` flag, que indica al servidor que rechace cualquier comando que no forme parte de la versión de API declarada. Esto genera un error al ejecutar el comando buildInfo.

```php
<?php

use MongoDB\Driver\Manager;
use MongoDB\Driver\ServerApi;

$v1 = new ServerApi(ServerApi::v1, true);
$manager = new Manager('mongodb://localhost:27017', [], ['serverApi' => $v1]);

$command = new MongoDB\Driver\Command(['buildInfo' => 1]);

try {
    $cursor = $manager->executeCommand('admin', $command);
} catch(MongoDB\Driver\Exception $e) {
    echo $e->getMessage(), "\n";
    exit;
}

/* El comando buildInfo devuelve un único documento de resultado, por lo que
 * necesitamos acceder al primer resultado en el cursor. */
$buildInfo = $cursor->toArray()[0];

echo $buildInfo->version, "\n";

?>

    
```

El ejemplo anterior mostrará:

    Provided apiStrict:true, but the command buildInfo is not in API Version 1
