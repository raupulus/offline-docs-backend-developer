---
title: MongoDB\BSON\PackedArray::fromPHP
description: Construye una nueva instancia de array BSON a partir de datos PHP
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.fromphp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/fromphp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48120
---

MongoDB\BSON\PackedArray::fromPHP

Construye una nueva instancia de array BSON a partir de datos PHP

## Descripción

```php
final static public MongoDB\BSON\PackedArray::fromPHP(array $value): MongoDB\BSON\PackedArray
```php

## Parámetros

`value` (`array`)  
El array PHP a convertir en array BSON. El array debe ser una lista (es decir, tener claves numéricas secuenciales comenzando por `0`).

## Valores devueltos

Devuelve una nueva instancia de `MongoDB\BSON\PackedArray`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si el array dado no es una lista (por ejemplo, tiene secuencias numéricas comenzando por

0

).

## Véase también

Tipos BSON
