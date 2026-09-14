---
title: date_create
description: Creación de un objeto DateTime
source_url: https://www.php.net/manual/es/function.date-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 71692b6f4
order: 10990
---

date_create

Creación de un objeto

DateTime

## Descripción

```php
date_create([string $datetime], [DateTimeZone $timezone]): DateTime
```php

Versión procedimental de DateTime::\_\_construct

A diferencia del constructor de `DateTime`, devolverá `false` en lugar de una excepción si la cadena `datetime` no es válida.

## Parámetros

Ver [DateTimeImmutable::\_\_construct](#datetimeimmutable.construct).

## Valores devueltos

Devuelve una nueva instancia DateTime o `false` si ocurre un error

## Véase también

DateTimeImmutable::\_\_construct

DateTimeImmutable::createFromFormat

DateTime::\_\_construct
