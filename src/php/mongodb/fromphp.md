---
title: MongoDB\BSON\Document::fromPHP
description: Construye una nueva instancia de documento a partir de datos PHP
source_url: https://www.php.net/manual/es/mongodb-bson-document.fromphp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/fromphp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47600
---

MongoDB\BSON\Document::fromPHP

Construye una nueva instancia de documento a partir de datos PHP

## Descripción

```php
final static public MongoDB\BSON\Document::fromPHP(object $value): MongoDB\BSON\Document
```php

## Parámetros

`value` (`objectarray`)  
Un objeto PHP o un array que contiene el documento. Cuando se pasa un array con claves numéricas, los valores numéricos se convierten en strings y se utilizan como claves del documento.

## Valores devueltos

Devuelve una nueva instancia de `MongoDB\BSON\Document`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\BSON\Document::fromBSON

MongoDB\BSON\Document::fromJSON

Tipos BSON
