---
title: La clase MongoDB\BSON\Symbol
source_url: https://www.php.net/manual/es/class.mongodb-bson-symbol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/symbol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48420
---

## Introducción

Tipo BSON para el tipo "Symbol". Este tipo BSON está deprecado, y esta clase no puede ser instanciada. Será creada a partir de un tipo BSON symbol al convertir BSON a PHP, y también puede ser convertida de vuelta a BSON al almacenar documentos en la base de datos.

## Sinopsis de la clase

MongoDB\BSON\Symbol

final

MongoDB\BSON\Symbol

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
