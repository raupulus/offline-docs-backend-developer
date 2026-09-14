---
title: MongoDB\BSON\Document::getIterator
description: Devuelve un iterador para el documento BSON
source_url: https://www.php.net/manual/es/mongodb-bson-document.getiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/getiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47620
---

MongoDB\BSON\Document::getIterator

Devuelve un iterador para el documento BSON

## Descripción

```php
final public MongoDB\BSON\Document::getIterator(): MongoDB\BSON\Iterator
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una instancia de `MongoDB\BSON\Iterator` que puede ser utilizada para iterar sobre todas las claves del documento.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\UnexpectedValueException

si el iterador BSON no puede ser inicializado.

## Véase también

Tipos BSON
