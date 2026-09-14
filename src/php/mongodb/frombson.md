---
title: MongoDB\BSON\Document::fromBSON
description: Construye una nueva instancia de documento a partir de un string BSON
source_url: https://www.php.net/manual/es/mongodb-bson-document.frombson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/frombson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47580
---

MongoDB\BSON\Document::fromBSON

Construye una nueva instancia de documento a partir de un string BSON

## Descripción

```php
final static public MongoDB\BSON\Document::fromBSON(string $bson): MongoDB\BSON\Document
```php

## Parámetros

`bson` (`string`)  
Un string que contiene un documento en formato BSON.

## Valores devueltos

Devuelve una nueva instancia de `MongoDB\BSON\Document`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\UnexpectedValueException

si

bson

es un string inválido o contiene más de un documento

## Véase también

MongoDB\BSON\Document::fromPHP

MongoDB\BSON\Document::fromJSON

BSON Types
