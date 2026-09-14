---
title: Throwable::getCode
description: Obtener el código de la excepción
source_url: https://www.php.net/manual/es/throwable.getcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/throwable/getcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3960
---

Throwable::getCode

Obtener el código de la excepción

## Descripción

```php
public Throwable::getCode(): int
```php

Devuelve el código de error asociado al objeto lanzado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código de la excepción como un `int` en `Exception`, aunque posiblemente como otro tipo en los descendientes de `Exception` (por ejemplo, como `string` en `PDOException`).

## Véase también

Exception::getCode
