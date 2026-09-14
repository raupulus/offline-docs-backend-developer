---
title: MongoDB\BSON\Document::offsetSet
description: Implementación de ArrayAccess
source_url: https://www.php.net/manual/es/mongodb-bson-document.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47660
---

MongoDB\BSON\Document::offsetSet

Implementación de

ArrayAccess

## Descripción

```php
final public MongoDB\BSON\Document::offsetSet(mixed $key, mixed $value): void
```php

Cambia el valor en la `key` especificada por `value`.

## Parámetros

`key`  
El índice a definir.

`value`  
El nuevo valor para la `key`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Siempre lanza una

MongoDB\Driver\Exception\LogicException

.
