---
title: MongoDB\BSON\Document::offsetGet
description: Devuelve el valor de una clave en un documento
source_url: https://www.php.net/manual/es/mongodb-bson-document.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47650
---

MongoDB\BSON\Document::offsetGet

Devuelve el valor de una clave en un documento

## Descripción

```php
final public MongoDB\BSON\Document::offsetGet(mixed $key): mixed
```php

## Parámetros

`key`  
La clave a recuperar en el documento.

## Valores devueltos

Devuelve el valor asociado a la clave dada. Si la clave no está presente en el documento, se lanza una excepción.

> [!NOTE]
> Cuando se encuentra un valor codificado como un entero de 64 bits en el documento BSON, el valor de retorno de este método será una instancia de `MongoDB\BSON\Int64`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\RuntimeException

si la clave no está presente en el documento.

## Véase también

ArrayAccess::offsetGet, MongoDB\BSON\Document::get
