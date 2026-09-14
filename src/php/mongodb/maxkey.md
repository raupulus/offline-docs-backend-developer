---
title: La clase MongoDB\BSON\MaxKey
source_url: https://www.php.net/manual/es/class.mongodb-bson-maxkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/maxkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47960
---

## Introducción

Tipo BSON especial que compara el valor más grande posible de todos los otros valores de elementos BSON posibles.

> [!NOTE]
> Se trata de un tipo interno de MongoDB utilizado para la indexación y la desfragmentación.

## Sinopsis de la clase

MongoDB\BSON\MaxKey

final

MongoDB\BSON\MaxKey

MongoDB\BSON\MaxKeyInterface

MongoDB\BSON\Type

JsonSerializable

Métodos

## Historial de cambios

| Versión            | Descripción                                           |
|--------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0 | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.3.0 | Implementa MongoDB\BSON\MaxKeyInterface.              |
| PECL mongodb 1.2.0 | Implementa Serializable y JsonSerializable.           |
