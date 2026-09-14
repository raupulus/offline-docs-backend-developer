---
title: DateTime::__unserialize
description: Deserializar un DateTime
source_url: https://www.php.net/manual/es/datetime.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 10810
---

DateTime::\_\_unserialize

DateTimeImmutable::\_\_unserialize

DateTimeInterface::\_\_unserialize

Deserializar un DateTime

## Descripción

```php
public DateTime::__unserialize(array $data): void
```php

```php
public DateTimeImmutable::__unserialize(array $data): void
```

```php
public DateTimeInterface::__unserialize(array $data): void
```php

El gestor [\_\_unserialize()](#object.unserialize).

## Parámetros

`data`  
El `DateTime` serializado.

## Valores devueltos

El objeto `DateTime`.

## Ejemplos

Ejemplo de `DateTime::unserialize`

```
<?php
$serializedDate = 'O:8:"DateTime":3:{s:4:"date";s:26:"2025-03-27 00:00:00.000000";s:13:"timezone_type";i:3;s:8:"timezone";s:3:"UTC";}';
var_dump(unserialize($serializedDate));

   
```php

El ejemplo anterior mostrará:

    object(DateTime)#1 (3) {
      ["date"]=>
      string(26) "2025-03-27 00:00:00.000000"
      ["timezone_type"]=>
      int(3)
      ["timezone"]=>
      string(3) "UTC"
    }

## Véase también

DateTime::\_\_serialize
