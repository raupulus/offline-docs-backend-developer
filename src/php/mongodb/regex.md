---
title: La clase MongoDB\BSON\Regex
source_url: https://www.php.net/manual/es/class.mongodb-bson-regex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/regex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48320
---

## Introducción

Tipo BSON para un patrón de expresión regular y [flag](https://www.mongodb.com/docs/manual/reference/operator/query/regex/#op._S_options) opcional.

> [!NOTE]
> Este tipo BSON se utiliza principalmente durante la consulta de la base de datos. Alternativamente, el operador de consulta [\$regex](https://www.mongodb.com/docs/manual/reference/operator/query/regex) puede ser utilizado.

## Sinopsis de la clase

MongoDB\BSON\Regex

final

MongoDB\BSON\Regex

MongoDB\BSON\RegexInterface

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
| PECL mongodb 1.3.0  | Implementa MongoDB\BSON\RegexInterface.               |
| PECL mongodb 1.2.0  | Implementa Serializable y JsonSerializable.           |
