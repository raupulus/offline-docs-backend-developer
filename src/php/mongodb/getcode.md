---
title: MongoDB\BSON\Javascript::getCode
description: Devuelve el código Javascript
source_url: https://www.php.net/manual/es/mongodb-bson-javascript.getcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/javascript/getcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47850
---

MongoDB\BSON\Javascript::getCode

Devuelve el código Javascript

## Descripción

```php
final public MongoDB\BSON\Javascript::getCode(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código Javascript.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\BSON\Javascript::getCode`

```
<?php

$js = new MongoDB\BSON\Javascript('function foo(bar) { return bar; }');
var_dump($js->getCode());

?>

   
```php

El ejemplo anterior mostrará:

    string(33) "function foo(bar) { return bar; }"

## Véase también

Tipos BSON
