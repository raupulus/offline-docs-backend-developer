---
title: MongoDB\BSON\PackedArray::toPHP
description: Devuelve la representación PHP del array BSON
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.tophp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/tophp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48210
---

MongoDB\BSON\PackedArray::toPHP

Devuelve la representación PHP del array BSON

## Descripción

```php
final public MongoDB\BSON\PackedArray::toPHP([array $typeMap]): array
```php

## Parámetros

`typeMap` (`array`)  
[Configuración del mapa de tipos](#mongodb.persistence.typemaps).

## Valores devueltos

El valor decodificado en PHP.

> [!NOTE]
> Cuando se encuentra un valor codificado como un entero de 64 bits en el array BSON, el valor de retorno de este método será una instancia de `MongoDB\BSON\Int64`.

## Errores/Excepciones

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si una clase en el type map no puede ser instanciada o no implementa

MongoDB\BSON\Unserializable

.

## Véase también

MongoDB\BSON\toPHP

Tipos BSON
