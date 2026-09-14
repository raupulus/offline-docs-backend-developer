---
title: DateTimeImmutable::createFromInterface
description: Devuelve un nuevo objeto DateTimeImmutable que encapsula el objeto DateTimeInterface
  dado
source_url: https://www.php.net/manual/es/datetimeimmutable.createfrominterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/createfrominterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10600
---

DateTimeImmutable::createFromInterface

Devuelve un nuevo objeto DateTimeImmutable que encapsula el objeto DateTimeInterface dado

## Descripción

```php
public static DateTimeImmutable::createFromInterface(DateTimeInterface $object): DateTimeImmutable
```php

## Parámetros

`object`  
El objeto `DateTimeInterface` que necesita ser convertido en una versión immutable. Este objeto no se modifica, sino que en su lugar se crea un nuevo objeto `DateTimeImmutable` que contiene la misma información de fecha, hora y zona horaria.

## Valores devueltos

Devuelve una nueva instancia de `DateTimeImmutable`.

## Ejemplos

Creando un objeto fecha y hora inmutable

```
<?php
$date = new DateTime("2014-06-20 11:45 Europe/London");
$immutable = DateTimeImmutable::createFromInterface($date);

$date = new DateTimeImmutable("2014-06-20 11:45 Europe/London");
$also_immutable = DateTimeImmutable::createFromInterface($date);

    
```php
