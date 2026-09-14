---
title: MongoDB\BSON\Iterator::key
description: Devuelve la clave del elemento actual/corriente
source_url: https://www.php.net/manual/es/mongodb-bson-iterator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/iterator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47790
---

MongoDB\BSON\Iterator::key

Devuelve la clave del elemento actual/corriente

## Descripción

```php
public MongoDB\BSON\Iterator::key(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la clave del elemento actual/corriente. Durante la iteración de un documento BSON, la clave será siempre una `string`. Durante la iteración de un array BSON, la clave será un `int`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\LogicException

si el iterador no es válido.

## Véase también

Iterator::key
