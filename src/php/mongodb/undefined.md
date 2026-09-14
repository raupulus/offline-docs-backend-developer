---
title: La clase MongoDB\BSON\Undefined
source_url: https://www.php.net/manual/es/class.mongodb-bson-undefined.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/undefined.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48570
---

## Introducción

Tipo BSON para el tipo "Undefined" (Indefinido). Este tipo BSON está deprecado, y esta clase no puede ser instanciada. Será creada a partir de un tipo BSON undefined al convertir BSON a PHP, y también puede ser convertido de vuelta a BSON al almacenar documentos en la base de datos.

## Sinopsis de la clase

MongoDB\BSON\Undefined

final

MongoDB\BSON\Undefined

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
