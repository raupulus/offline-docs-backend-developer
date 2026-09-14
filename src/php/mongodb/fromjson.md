---
title: MongoDB\BSON\Document::fromJSON
description: Construye una nueva instancia de documento desde un string JSON
source_url: https://www.php.net/manual/es/mongodb-bson-document.fromjson.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/fromjson.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47590
---

MongoDB\BSON\Document::fromJSON

Construye una nueva instancia de documento desde un string JSON

## Descripción

```php
final static public MongoDB\BSON\Document::fromJSON(string $json): MongoDB\BSON\Document
```php

Convierte un string [JSON extendido](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/) a su representación BSON.

## Parámetros

`json` (`string`)  
El valor JSON a convertir.

## Valores devueltos

Retorna una nueva instancia de `MongoDB\BSON\Document`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza

MongoDB\Driver\Exception\UnexpectedValueException

si el valor JSON no puede ser convertido a un documento BSON (por ejemplo, debido a un error de sintaxis).

## Véase también

MongoDB\BSON\Document::fromPHP

MongoDB\BSON\Document::fromBSON

MongoDB JSON extendido

Tipo BSON
