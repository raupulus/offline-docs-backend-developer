---
title: MongoDB\BSON\Int64::__construct
description: Construye un nuevo Int64
source_url: https://www.php.net/manual/es/mongodb-bson-int64.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/int64/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47730
---

MongoDB\BSON\Int64::\_\_construct

Construye un nuevo Int64

## Descripción

```php
final public MongoDB\BSON\Int64::__construct(int $value)
```php

Crea una nueva instancia de `MongoDB\BSON\Int64` para el valor entero dado.

## Parámetros

`value` (`intstring`)  
El valor a asignar a la instancia de `Int64`. Este valor puede ser proporcionado como `int` o `string`, siendo este último requerido en plataformas de 32 bits para representar valores de 64 bits.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.16.0 | Este método se hizo público para soportar la creación de instancias Int64 durante la manipulación de BSON sin tratar. |

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si el string

value

no puede ser analizado como un entero de 64 bits.

## Véase también

Tipos BSON
