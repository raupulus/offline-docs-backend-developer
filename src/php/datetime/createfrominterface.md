---
title: DateTime::createFromInterface
description: RDevuelve un nuevo objeto DateTime que encapsula el objeto DateTimeInterface
  dado
source_url: https://www.php.net/manual/es/datetime.createfrominterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/createfrominterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10440
---

DateTime::createFromInterface

RDevuelve un nuevo objeto DateTime que encapsula el objeto DateTimeInterface dado

## Descripción

```php
public static DateTime::createFromInterface(DateTimeInterface $object): DateTime
```php

## Parámetros

`object`  
El objeto `DateTimeInterface` que necesita ser convertido a una versión mutable. Este objeto no se modifica, sino que en su lugar se crea un nuevo objeto `DateTime` que contiene la misma información de fecha, hora y zona horaria.

## Valores devueltos

Devuelve una nueva instancia de `DateTime`.

## Ejemplos

Creando un objeto fecha y hora mutable

```
<?php
$date = new DateTimeImmutable("2014-06-20 11:45 Europe/London");
$mutable = DateTime::createFromInterface($date);

$date = new DateTime("2014-06-20 11:45 Europe/London");
$also_mutable = DateTime::createFromInterface($date);

    
```php
