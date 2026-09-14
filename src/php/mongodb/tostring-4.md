---
title: MongoDB\BSON\Decimal128::__toString
description: Devuelve la representación en forma de string de Decimal128
source_url: https://www.php.net/manual/es/mongodb-bson-decimal128.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/decimal128/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47530
---

MongoDB\BSON\Decimal128::\_\_toString

Devuelve la representación en forma de string de Decimal128

## Descripción

```php
final public MongoDB\BSON\Decimal128::__toString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación en forma de string de Decimal128.

## Ejemplos

Ejemplo con `MongoDB\BSON\Decimal128::__toString`

```
<?php

var_dump((string) new MongoDB\BSON\Decimal128(1234.5678));
var_dump((string) new MongoDB\BSON\Decimal128(NAN));
var_dump((string) new MongoDB\BSON\Decimal128(INF));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(9) "1234.5678"
    string(3) "NaN"
    string(8) "Infinity"

## Véase también

Formato de coma flotante Decimal128

Tipos BSON
