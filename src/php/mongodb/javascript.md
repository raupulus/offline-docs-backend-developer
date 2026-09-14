---
title: La clase MongoDB\BSON\Javascript
source_url: https://www.php.net/manual/es/class.mongodb-bson-javascript.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/javascript.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47890
---

## Introducción

Tipo BSON para el código JavaScript. Un documento de ámbito opcional puede ser especificado que mapea los identificadores a los valores y define el ámbito en el cual el código debe ser evaluado por el servidor.

> [!NOTE]
> Este tipo BSON es principalmente utilizado durante la ejecución de comandos de base de datos que toman una función JavaScript como argumento, tal como [mapReduce](https://www.mongodb.com/docs/manual/reference/command/mapReduce/).

## Sinopsis de la clase

MongoDB\BSON\Javascript

final

MongoDB\BSON\Javascript

MongoDB\BSON\JavascriptInterface

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
| PECL mongodb 1.3.0  | Implementa MongoDB\BSON\JavascriptInterface.          |
| PECL mongodb 1.2.0  | Implementa Serializable y JsonSerializable.           |
