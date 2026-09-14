---
title: MongoDB\BSON\Timestamp::getIncrement
description: Devuelve el componente de incremento de este Timestamp
source_url: https://www.php.net/manual/es/mongodb-bson-timestamp.getincrement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/timestamp/getincrement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 48440
---

MongoDB\BSON\Timestamp::getIncrement

Devuelve el componente de incremento de este Timestamp

## Descripción

```php
final public MongoDB\BSON\Timestamp::getIncrement(): int
```php

El componente de incremento de un Timestamp son sus 32 bits menos significativos, que denotan el ordinal de incremento para operaciones dentro de un mismo segundo. Este valor se lee como un entero sin signo de 32 bits con orden de bytes big-endian.

> [!NOTE]
> Dado que el tipo integer de PHP es con signo, algunos de los valores devueltos por este método pueden aparecer como enteros negativos en plataformas de 32 bits. El formateador `"%u"` de `sprintf` se puede utilizar para obtener una representación en forma de string del valor decimal sin signo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de incremento de este Timestamp.

> [!WARNING]
> En sistemas de 32 bits este método puede devolver un número negativo. Aunque las partes de incremento y marca de tiempo del tipo BSON timestamp consisten en dos valores sin signo de 32 bits, PHP no puede representarlos en plataformas de 32 bits.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

Tipos BSON: Marcas de tiempo
