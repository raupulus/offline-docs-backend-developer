---
title: MongoDB\BSON\Binary::__construct
description: Construye un nuevo binario
source_url: https://www.php.net/manual/es/mongodb-bson-binary.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47340
---

MongoDB\BSON\Binary::\_\_construct

Construye un nuevo binario

## Descripción

```php
final public MongoDB\BSON\Binary::__construct(string $data, [int $type])
```php

## Parámetros

`data` (`string`)  
Los datos binarios.

`type` (`int`)  
Entero de 8 bits sin signo que indica el tipo de datos. Por omisión, el valor es `MongoDB\BSON\Binary::TYPE_GENERIC` si no se especifica.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

type

no es un entero sin signo de 8 bits.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

type

es

MongoDB\BSON\Binary::TYPE_UUID

o

MongoDB\BSON\Binary::TYPE_OLD_UUID

y

data

no tiene exactamente 16 bytes de longitud.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.15.0 | El parámetro `type` es ahora opcional y tiene el valor por omisión `MongoDB\BSON\Binary::TYPE_GENERIC` si no se especifica. |
| PECL mongodb 1.3.0 | `MongoDB\Driver\Exception\InvalidArgumentException` se lanza si `type` es `MongoDB\BSON\Binary::TYPE_UUID` o `MongoDB\BSON\Binary::TYPE_OLD_UUID` y `data` no tiene exactamente 16 bytes de longitud. |
| PECL mongodb 1.1.3 | `MongoDB\Driver\Exception\InvalidArgumentException` se lanza si `type` no es un entero sin signo de 8 bits. |

## Ejemplos

Ejemplo con `MongoDB\BSON\Binary::__construct`

```
<?php

$binary = new MongoDB\BSON\Binary('foo', MongoDB\BSON\Binary::TYPE_GENERIC);
var_dump($binary);

?>

   
```php

El ejemplo anterior mostrará:

    object(MongoDB\BSON\Binary)#1 (2) {
      ["data"]=>
      string(3) "foo"
      ["type"]=>
      int(0)
    }

## Véase también

Los tipos BSON
