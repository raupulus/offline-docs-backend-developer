---
title: La clase MongoDB\BSON\DBPointer
source_url: https://www.php.net/manual/es/class.mongodb-bson-dbpointer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/dbpointer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47500
---

## Introducción

El tipo BSON para el tipo "DBPointer". Este tipo BSON está deprecado, y esta clase no puede ser instanciada. Será creada a partir de un tipo BSON DBPointer durante la conversión BSON a PHP, y puede también ser convertida en BSON durante el almacenamiento de documentos en la base de datos.

## Sinopsis de la clase

MongoDB\BSON\DBPointer

final

MongoDB\BSON\DBPointer

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
