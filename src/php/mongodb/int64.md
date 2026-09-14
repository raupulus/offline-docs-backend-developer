---
title: La clase MongoDB\BSON\Int64
source_url: https://www.php.net/manual/es/class.mongodb-bson-int64.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/int64.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47760
---

## Introducción

Tipo BSON para un entero de 64 bits. Al decodificar BSON en datos PHP, esta clase se utiliza cuando un entero de 64 bits no puede ser representado como un entero PHP en plataformas de 32 bits. Estos objetos soportan los operadores [aritméticos](#language.operators.arithmetic), [a nivel de bits](#language.operators.bitwise), y [comparación](#language.operators.comparison) sobrecargados.

Al trabajar con datos BSON sin tratar a través de las clases `MongoDB\BSON\Document`, `MongoDB\BSON\PackedArray`, y `MongoDB\BSON\Iterator`, cualquier entero de 64 bits será devuelto como una instancia de esta clase, independientemente de la plataforma y de la posibilidad de representar el valor como un entero PHP. Esto garantiza que los valores pueden ser recorridos sin cambiar el tipo.

Al codificar BSON, los objetos de esta clase serán convertidos en un tipo entero 64 bits, incluso cuando el valor podría caber en un entero de 32 bits. Esto permite almacenar explícitamente valores como enteros de 64 bits en BSON.

## Sinopsis de la clase

MongoDB\BSON\Int64

final

MongoDB\BSON\Int64

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.16.0 | Esta clase puede ahora ser instanciada en todas las plataformas. Se añade soporte para los operadores aritméticos, a nivel de bits, y de comparación sobrecargados. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+. |
