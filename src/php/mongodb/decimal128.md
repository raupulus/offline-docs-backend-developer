---
title: La clase MongoDB\BSON\Decimal128
source_url: https://www.php.net/manual/es/class.mongodb-bson-decimal128.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/decimal128.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47540
---

## Introducción

Tipo BSON para el [formato de coma flotante Decimal128](https://en.wikipedia.org/wiki/Decimal128_floating-point_format), que soporta números con hasta 34 dígitos decimales (i.e. dígitos significativos) y un rango de exponentes de −6143 a +6144.

A diferencia del tipo BSON double (i.e. `float` en PHP), que solo almacena una aproximación de los valores decimales, el tipo de datos decimal almacena el valor exacto. Por ejemplo, `MongoDB\BSON\Decimal128('9.99')` tiene un valor preciso de 9.99 mientras que un double 9.99 tendría un valor aproximado de 9.9900000000000002131628….

> [!NOTE]
> `MongoDB\BSON\Decimal128` solo es compatible con MongoDB 3.4+. Si se intenta utilizar el tipo BSON con una versión antigua de MongoDB, se emitirá un error.

## Sinopsis de la clase

MongoDB\BSON\Decimal128

final

MongoDB\BSON\Decimal128

MongoDB\BSON\Decimal128Interface

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
| PECL mongodb 1.3.0  | Implementa MongoDB\BSON\Decimal128Interface.          |
| PECL mongodb 1.2.0  | Implementa Serializable y JsonSerializable.           |
