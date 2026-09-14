---
title: MongoDB\BSON\Regex::getPattern
description: Devuelve la máscara del REGEX
source_url: https://www.php.net/manual/es/mongodb-bson-regex.getpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/regex/getpattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48290
---

MongoDB\BSON\Regex::getPattern

Devuelve la máscara del REGEX

## Descripción

```php
final public MongoDB\BSON\Regex::getPattern(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la máscara del REGEX.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `BSON\Regex::getPattern`

```
<?php

$regex = new MongoDB\BSON\Regex('regex', 'i');
var_dump($regex->getPattern());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(5) "regex"

## Véase también

Los tipos BSON
