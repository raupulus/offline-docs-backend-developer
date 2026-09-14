---
title: Throwable::getTrace
description: Obtener la traza de la pila
source_url: https://www.php.net/manual/es/throwable.gettrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/throwable/gettrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 4010
---

Throwable::getTrace

Obtener la traza de la pila

## Descripción

```php
public Throwable::getTrace(): array
```php

Devuelve la traza de la pila como un `array`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la traza de la pila como un `array` con el mismo formato que en `debug_backtrace`.

## Véase también

Exception::getTrace
