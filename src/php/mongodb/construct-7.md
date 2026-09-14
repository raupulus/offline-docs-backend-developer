---
title: MongoDB\BSON\Javascript::__construct
description: Construye un nuevo objeto Javascript
source_url: https://www.php.net/manual/es/mongodb-bson-javascript.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/javascript/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47840
---

MongoDB\BSON\Javascript::\_\_construct

Construye un nuevo objeto Javascript

## Descripción

```php
final public MongoDB\BSON\Javascript::__construct(string $code, [array $scope])
```php

## Parámetros

`code` (`string`)  
El código Javascript.

`scope` (`arrayobject`)  
El ámbito del Javascript.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza

MongoDB\Driver\Exception\InvalidArgumentException

si

code

contiene un byte nulo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.2.0 | `MongoDB\Driver\Exception\InvalidArgumentException` se lanza si `code` contiene un byte nulo. Anteriormente, los valores eran truncados en el primer byte nulo. |

## Ejemplos

`MongoDB\BSON\Javascript::__construct` example

```
<?php

$code = new MongoDB\BSON\Javascript('function() { return 1; }');
var_dump($code);

$codews = new MongoDB\BSON\Javascript('function() { return foo; }', ['foo' => 'bar']);
var_dump($codews);

?>

   
```php

El ejemplo anterior mostrará:

    object(MongoDB\BSON\Javascript)#1 (2) {
      ["javascript"]=>
      string(24) "function() { return 1; }"
      ["scope"]=>
      object(stdClass)#2 (0) {
      }
    }
    object(MongoDB\BSON\Javascript)#2 (2) {
      ["javascript"]=>
      string(26) "function() { return foo; }"
      ["scope"]=>
      object(stdClass)#1 (1) {
        ["foo"]=>
        string(3) "bar"
      }
    }

## Véase también

Los tipos BSON
