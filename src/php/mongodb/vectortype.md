---
title: La enumeración MongoDB\BSON\VectorType
source_url: https://www.php.net/manual/es/enum.mongodb-bson-vectortype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/vectortype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48700
---

## Introducción

La enumeración MongoDB\BSON\VectorType se utiliza para especificar el tipo de datos vectoriales almacenados en un `MongoDB\BSON\Binary` con subtipo `MongoDB\BSON\Binary::TYPE_VECTOR`.

## Sinopsis del enum

MongoDB\BSON\VectorType

Float32

Cada elemento en el vector es un valor de punto flotante de 32 bits.

Int8

Cada elemento en el vector es un valor entero de 8 bits.

PackedBit

Cada elemento en el vector es un valor de 1 bit. Al crear vectores de este tipo, puede pasar valores

bool

o valores

int

de 1 bit, es decir,

0

o

1

.
