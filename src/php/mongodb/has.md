---
title: MongoDB\BSON\Document::has
description: Indica si una clave está presente en el documento
source_url: https://www.php.net/manual/es/mongodb-bson-document.has.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/has.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47630
---

MongoDB\BSON\Document::has

Indica si una clave está presente en el documento

## Descripción

```php
final public MongoDB\BSON\Document::has(string $key): bool
```php

## Parámetros

`key` (`string`)  
La clave a buscar en el documento.

## Valores devueltos

Devuelve `true` si la clave está presente en el documento, de lo contrario `false`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\BSON\Document::get

Tipos BSON
