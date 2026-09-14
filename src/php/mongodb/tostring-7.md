---
title: MongoDB\BSON\Int64::__toString
description: Devuelve la representación en forma de string de Int64
source_url: https://www.php.net/manual/es/mongodb-bson-int64.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/int64/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47750
---

MongoDB\BSON\Int64::\_\_toString

Devuelve la representación en forma de string de Int64

## Descripción

```php
final public MongoDB\BSON\Int64::__toString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación en forma de string de Int64.

## Ejemplos

Ejemplo con `MongoDB\BSON\Int64::__toString`

```
<?php

$int64 = new MongoDB\BSON\Int64('9223372036854775807');

var_dump((string) $int64);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(19) "9223372036854775807"

## Véase también

Tipos BSON
