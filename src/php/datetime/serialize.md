---
title: DateTime::__serialize
description: Deserializa un DateTime
source_url: https://www.php.net/manual/es/datetime.serialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/serialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10800
---

DateTime::\_\_serialize

DateTimeImmutable::\_\_serialize

DateTimeInterface::\_\_serialize

Deserializa un DateTime

## Descripción

```php
public DateTime::__serialize(): array
```php

```php
public DateTimeImmutable::__serialize(): array
```

```php
public DateTimeInterface::__serialize(): array
```php

El gestor [\_\_serialize()](#object.serialize).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La representación serializada del objeto `DateTime`.

## Ejemplos

Ejemplo de `DateTime::serialize`

```
<?php
$date = new DateTime('2025-03-27');
var_dump(serialize($date));

   
```php

El ejemplo anterior mostrará:

    string(114) "O:8:"DateTime":3:{s:4:"date";s:26:"2025-03-27 00:00:00.000000";s:13:"timezone_type";i:3;s:8:"timezone";s:3:"UTC";}"

## Véase también

DateTime::\_\_unserialize
