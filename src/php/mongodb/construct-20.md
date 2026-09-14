---
title: MongoDB\Driver\Command::__construct
description: Crea un nuevo Command
source_url: https://www.php.net/manual/es/mongodb-driver-command.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/command/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49220
---

MongoDB\Driver\Command::\_\_construct

Crea un nuevo Command

## Descripción

```php
final public MongoDB\Driver\Command::__construct(array $documento, [array $opcionesComando])
```php

Construye un nuevo `MongoDB\Driver\Command`, que es un objeto de valor inmutable que representa un comando de base de datos. El comando puede entonces ser ejecutado con MongoDB\Driver\Manager::executeCommand.

El documento de comando completo, que incluye el nombre del comando y sus opciones, debe ser expresado en el parámetro `documento`. El parámetro `opcionesComando` solo se utiliza para especificar opciones relacionadas con la ejecución del comando y el `MongoDB\Driver\Cursor` resultante.

## Parámetros

`documento`  
El documento de comando completo, que será enviado al servidor.

`opcionesComando`  
> [!NOTE]
> No utilice este parámetro para especificar opciones descritas en la referencia del comando en el manual de MongoDB. Este parámetro solo debe ser utilizado para las opciones listadas explícitamente a continuación.

| Opción | Tipo | Descripción |
|----|----|----|
| maxAwaitTimeMS | `int` | Entero positivo que denota el límite de tiempo en milisegundos para que el servidor bloquee una operación getMore si no hay datos disponibles. Esta opción solo debe ser utilizada en conjunto con comandos que devuelven un cursor rastreable (p. ej. [Streams de Cambios](https://www.mongodb.com/docs/manual/changeStreams/)). |

opcionesComando

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.4.0 | Se añadió un segundo argumento `opcionesComando`, que soporta la opción `"maxAwaitTimeMS"`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\Command::__construct`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$command = new MongoDB\Driver\Command(array("buildinfo" => 1));

try {
    $cursor = $manager->executeCommand("admin", $command);
    $response = $cursor->toArray()[0];
} catch(MongoDB\Driver\Exception $e) {
    echo $e->getMessage(), "\n";
    exit;
}
var_dump($response);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(13) {
      ["version"]=>
      string(14) "2.8.0-rc2-pre-"
      ["gitVersion"]=>
      string(62) "b743d7158f7642f4da6b7eac8320374b3b88dc2e modules: subscription"
      ["OpenSSLVersion"]=>
      string(25) "OpenSSL 1.0.1f 6 Jan 2014"
      ["sysInfo"]=>
      string(104) "Linux infant 3.16.0-24-generic #32-Ubuntu SMP Tue Oct 28 13:07:32 UTC 2014 x86_64 BOOST_LIB_VERSION=1_49"
      ["loaderFlags"]=>
      string(91) "-fPIC -pthread -Wl,-z,now -rdynamic -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,-E"
      ["compilerFlags"]=>
      string(301) "-Wnon-virtual-dtor -Woverloaded-virtual -std=c++11 -fPIC -fno-strict-aliasing -ggdb -pthread -Wall -Wsign-compare -Wno-unknown-pragmas -Winvalid-pch -pipe -Werror -O3 -Wno-unused-local-typedefs -Wno-unused-function -Wno-deprecated-declarations -Wno-unused-but-set-variable -fno-builtin-memcmp -std=c99"
      ["allocator"]=>
      string(8) "tcmalloc"
      ["versionArray"]=>
      array(4) {
        [0]=>
        int(2)
        [1]=>
        int(8)
        [2]=>
        int(0)
        [3]=>
        int(-8)
      }
      ["javascriptEngine"]=>
      string(2) "V8"
      ["bits"]=>
      int(64)
      ["debug"]=>
      bool(false)
      ["maxBsonObjectSize"]=>
      int(16777216)
      ["ok"]=>
      float(1)
    }

Ejemplo de `MongoDB\Driver\Command::__construct`

Los comandos pueden aceptar opciones también, como parte de la estructura normal que se crea para enviar al servidor. Por ejemplo, la opción `maxTimeMS` puede ser pasada con la mayoría de comandos para restringir la cantidad de tiempo que un comando específico puede ejecutarse en el servidor.

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$command = new MongoDB\Driver\Command(
    array(
        "distinct" => "beer",
        "key" => "beer_name",
        "maxTimeMS" => 10,
    )
);

try {
    $cursor = $manager->executeCommand("beerdb", $command);
    $response = $cursor->toArray()[0];
} catch(MongoDB\Driver\Exception\Exception $e) {
    echo $e->getMessage(), "\n";
    exit;
}
var_dump($response);

?>

   
```php

Resultado del ejemplo anterior es similar a:

        la operación excedió el límite de tiempo

## Véase también

MongoDB\Driver\Manager::executeCommand

MongoDB\Driver\Cursor
