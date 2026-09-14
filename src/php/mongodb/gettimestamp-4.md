---
title: MongoDB\BSON\TimestampInterface::getTimestamp
description: Devuelve el componente de marca de tiempo de este TimestampInterface
source_url: https://www.php.net/manual/es/mongodb-bson-timestampinterface.gettimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/timestampinterface/gettimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48500
---

MongoDB\BSON\TimestampInterface::getTimestamp

Devuelve el componente de marca de tiempo de este TimestampInterface

## Descripción

```php
abstract public MongoDB\BSON\TimestampInterface::getTimestamp(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el componente de marca de tiempo de este TimestampInterface.

> [!WARNING]
> En sistemas de 32 bits este método puede devolver un número negativo. Aunque las partes de incremento y marca de tiempo del tipo de marca de tiempo BSON consisten en dos valores de 32 bits sin signo, PHP no puede representarlos en plataformas de 32 bits.

## Véase también

MongoDB\BSON\Timestamp::getTimestamp
