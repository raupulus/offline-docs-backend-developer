---
title: DateTimeInterface::getMicrosecond
description: Obtiene la parte de microsegundos de la marca de tiempo Unix
source_url: https://www.php.net/manual/es/datetimeinterface.getmicrosecond.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/getmicrosecond.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 726154e3c
order: 10760
---

DateTimeInterface::getMicrosecond

DateTimeImmutable::getMicrosecond

DateTime::getMicrosecond

Obtiene la parte de microsegundos de la marca de tiempo Unix

## Descripción

```php
public DateTimeInterface::getMicrosecond(): int
```php

```php
public DateTimeImmutable::getMicrosecond(): int
```

```php
public DateTime::getMicrosecond(): int
```php

Obtiene la parte de microsegundos de la marca de tiempo Unix.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la parte de microsegundos de la marca de tiempo Unix que representa la fecha.

## Ejemplos

Ejemplo de DateTimeInterface::getMicrosecond

```
<?php
$date = new DateTimeImmutable('2024-01-01 12:34:56.789123');
var_dump($date->format('u'));
var_dump($date->getMicrosecond());
?>

   
```php

El ejemplo anterior mostrará:

    string(6) "789123"
    int(789123)

## Véase también

DateTimeInterface::getTimestamp

DateTimeInterface::format
