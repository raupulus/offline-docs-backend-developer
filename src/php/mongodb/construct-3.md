---
title: MongoDB\BSON\Decimal128::__construct
description: Construye un nuevo Decimal128
source_url: https://www.php.net/manual/es/mongodb-bson-decimal128.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/decimal128/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47510
---

MongoDB\BSON\Decimal128::\_\_construct

Construye un nuevo Decimal128

## Descripción

```php
final public MongoDB\BSON\Decimal128::__construct(string $value)
```php

> [!NOTE]
> `MongoDB\BSON\Decimal128` solo es compatible con MongoDB 3.4+. Si se intenta utilizar el tipo BSON con una versión antigua de MongoDB, se emitirá un error.

## Parámetros

`value` (`string`)  
Una cadena decimal

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza

MongoDB\Driver\Exception\InvalidArgumentException

si

value

no es una cadena decimal válida.

## Ejemplos

Ejemplo con `MongoDB\BSON\Decimal128::__construct`

```
<?php

var_dump(new MongoDB\BSON\Decimal128(1234.5678));
var_dump(new MongoDB\BSON\Decimal128(NAN));
var_dump(new MongoDB\BSON\Decimal128(INF));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\Decimal128)#1 (1) {
      ["dec"]=>
      string(9) "1234.5678"
    }
    object(MongoDB\BSON\Decimal128)#1 (1) {
      ["dec"]=>
      string(3) "NaN"
    }
    object(MongoDB\BSON\Decimal128)#1 (1) {
      ["dec"]=>
      string(8) "Infinity"
    }

## Véase también

Formato de coma flotante Decimal128

Tipos BSON
