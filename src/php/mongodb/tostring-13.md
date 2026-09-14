---
title: MongoDB\BSON\Regex::__toString
description: Devuelve el string que representa esta REGEX
source_url: https://www.php.net/manual/es/mongodb-bson-regex.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/regex/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48310
---

MongoDB\BSON\Regex::\_\_toString

Devuelve el string que representa esta REGEX

## Descripción

```php
final public MongoDB\BSON\Regex::__toString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el string que representa esta REGEX.

## Ejemplos

Ejemplo con `BSON\Regex::__toString`

```
<?php

$regex = new MongoDB\BSON\Regex('regex', 'i');
var_dump((string) $regex);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(8) "/regex/i"

## Véase también

Los tipos BSON
