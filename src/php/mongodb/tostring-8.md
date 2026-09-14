---
title: MongoDB\BSON\Javascript::__toString
description: Devuelve el código Javascript
source_url: https://www.php.net/manual/es/mongodb-bson-javascript.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/javascript/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47880
---

MongoDB\BSON\Javascript::\_\_toString

Devuelve el código Javascript

## Descripción

```php
final public MongoDB\BSON\Javascript::__toString(): string
```php

Este método es un alias de: MongoDB\BSON\Javascript::getCode.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código Javascript.

## Ejemplos

Ejemplo con `MongoDB\BSON\Javascript::__toString`

```
<?php

var_dump((string) new MongoDB\BSON\Javascript('function foo(bar) { return bar; }'));

?>

   
```php

El ejemplo anterior mostrará:

    string(33) "function foo(bar) { return bar; }"

## Véase también

MongoDB\BSON\Javascript::getCode

Tipos BSON
