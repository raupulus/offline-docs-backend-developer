---
title: DateTimeImmutable::createFromMutable
description: Devuelve un nuevo objeto DateTimeImmutable que encapsula el objeto DateTime
  dado
source_url: https://www.php.net/manual/es/datetimeimmutable.createfrommutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/createfrommutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10610
---

DateTimeImmutable::createFromMutable

Devuelve un nuevo objeto DateTimeImmutable que encapsula el objeto DateTime dado

## Descripción

```php
public static DateTimeImmutable::createFromMutable(DateTime $object): static
```php

## Parámetros

`object`  
El objeto `DateTime` mutable para convertirlo en una versión immutable. Este objeto no se modifica, sino que en su lugar se crea un nuevo objeto `DateTimeImmutable` que contiene la misma información de fecha, hora y zona horaria.

## Valores devueltos

Devuelve una nueva instancia de `DateTimeImmutable`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El método ahora devuelve una instancia de la clase actualmente invocada. Anteriormente, creaba una nueva instancia de `DateTimeImmutable`. |

## Ejemplos

Creando un objeto de fecha y hora inmutable

```
<?php
$date = new DateTime("2014-06-20 11:45 Europe/London");
$immutable = DateTimeImmutable::createFromMutable( $date );

    
```php
