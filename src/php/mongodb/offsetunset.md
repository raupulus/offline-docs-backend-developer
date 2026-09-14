---
title: MongoDB\BSON\Document::offsetUnset
description: Implementación de ArrayAccess
source_url: https://www.php.net/manual/es/mongodb-bson-document.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47670
---

MongoDB\BSON\Document::offsetUnset

Implementación de

ArrayAccess

## Descripción

```php
final public MongoDB\BSON\Document::offsetUnset(mixed $key): void
```php

Elimina el valor en el índice especificado.

## Parámetros

`key`  
El índice a eliminar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Siempre lanza una

MongoDB\Driver\Exception\LogicException

.
