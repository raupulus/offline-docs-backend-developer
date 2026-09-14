---
title: MongoDB\Driver\CursorInterface::setTypeMap
description: Establece un mapa de tipos para usar en la deserialización BSON
source_url: https://www.php.net/manual/es/mongodb-driver-cursorinterface.settypemap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorinterface/settypemap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49420
---

MongoDB\Driver\CursorInterface::setTypeMap

Establece un mapa de tipos para usar en la deserialización BSON

## Descripción

```php
abstract public MongoDB\Driver\CursorInterface::setTypeMap(array $typemap): void
```php

Establece la [configuración del mapa de tipos](#mongodb.persistence.typemaps) que se usará al deserializar los resultados BSON en valores PHP.

## Parámetros

`typeMap` (`array`)  
[Configuración del mapa de tipos](#mongodb.persistence.typemaps).

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Cursor::setTypeMap
