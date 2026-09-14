---
title: date_create_immutable
description: Crea un nuevo objeto DateTimeImmutable
source_url: https://www.php.net/manual/es/function.date-create-immutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-create-immutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: true
translation_revision: 71692b6f4
order: 10980
---

date_create_immutable

Crea un nuevo objeto

DateTimeImmutable

## Descripción

```php
date_create_immutable([string $datetime], [DateTimeZone $timezone]): DateTimeImmutable
```php

Versión procedimental de DateTimeImmutable::\_\_construct.

A diferencia del constructor de `DateTimeImmutable`, esta función devolverá `false` en lugar de una excepción si la cadena `datetime` proporcionada no es válida.

## Parámetros

Ver [DateTimeImmutable::\_\_construct](#datetimeimmutable.construct).

## Valores devueltos

Devuelve una nueva instancia DateTimeImmutable o `false` si ocurre un error

## Véase también

DateTimeImmutable::createFromFormat
