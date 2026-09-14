---
title: MongoDB\BSON\Iterator::current
description: Devuelve el elemento actual/corriente
source_url: https://www.php.net/manual/es/mongodb-bson-iterator.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/iterator/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47780
---

MongoDB\BSON\Iterator::current

Devuelve el elemento actual/corriente

## Descripción

```php
public MongoDB\BSON\Iterator::current(): mixed
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el valor del elemento actual/corriente.

> [!NOTE]
> Cuando un valor es codificado como un integer de 64 bits en la estructura BSON es encontrado, el valor de retorno de este método será una instancia de `MongoDB\BSON\Int64`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\LogicException

si el iterador no es válido.

## Véase también

Iterator::current
