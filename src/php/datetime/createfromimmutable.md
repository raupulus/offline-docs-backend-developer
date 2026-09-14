---
title: DateTime::createFromImmutable
description: Devuelve una nueva instancia de DateTime encapsulando el objeto DateTimeImmutable
  dado
source_url: https://www.php.net/manual/es/datetime.createfromimmutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/createfromimmutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10430
---

DateTime::createFromImmutable

Devuelve una nueva instancia de DateTime encapsulando el objeto DateTimeImmutable dado

## Descripción

```php
public static DateTime::createFromImmutable(DateTimeImmutable $object): static
```php

## Parámetros

`object`  
El objeto `DateTimeImmutable` inmutable que necesita ser convertido a una versión mutable. Este objeto no es modificado, sino que en su lugar se crea una nueva instancia de `DateTime` que contiene la misma fecha, hora y zona horaria.

## Valores devueltos

Devuelve una nueva instancia de `DateTime`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El método ahora devuelve una instancia de la clase actualmente invocada. Anteriormente, creaba una nueva instancia de `DateTime`. |

## Ejemplos

Creando un objeto de fecha y hora mutable

```
<?php
$date = new DateTimeImmutable("2014-06-20 11:45 Europe/London");
$mutable = DateTime::createFromImmutable( $date );

    
```php
