---
title: MongoDB\BSON\Document::offsetExists
description: Indica si una clave está presente en el documento
source_url: https://www.php.net/manual/es/mongodb-bson-document.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47640
---

MongoDB\BSON\Document::offsetExists

Indica si una clave está presente en el documento

## Descripción

```php
final public MongoDB\BSON\Document::offsetExists(mixed $key): bool
```php

## Parámetros

`key`  
La clave a buscar en el documento.

## Valores devueltos

Devuelve `true` si la clave está presente en el documento, de lo contrario `false`.

## Véase también

ArrayAccess::offsetExists, MongoDB\BSON\Document::has
