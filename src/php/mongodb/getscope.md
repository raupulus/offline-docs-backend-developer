---
title: MongoDB\BSON\Javascript::getScope
description: Devuelve el documento de ámbito de Javascript
source_url: https://www.php.net/manual/es/mongodb-bson-javascript.getscope.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/javascript/getscope.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47860
---

MongoDB\BSON\Javascript::getScope

Devuelve el documento de ámbito de Javascript

## Descripción

```php
final public MongoDB\BSON\Javascript::getScope(): object
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el documento de ámbito de Javascript, o `null` si no tiene ámbito.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\BSON\Javascript::getScope`

```
<?php

$js = new MongoDB\BSON\Javascript('function foo(bar) { return bar; }');
var_dump($js->getScope());

$js = new MongoDB\BSON\Javascript('function foo() { return foo; }', ['foo' => 42]);
var_dump($js->getScope());

?>

   
```php

El ejemplo anterior mostrará:

    NULL
    object(stdClass)#1 (1) {
      ["foo"]=>
      int(42)
    }

## Véase también

Tipos BSON
