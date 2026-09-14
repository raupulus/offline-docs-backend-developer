---
title: ReflectionFunction::isDisabled
description: Verifica si una función está deshabilitada
source_url: https://www.php.net/manual/es/reflectionfunction.isdisabled.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunction/isdisabled.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 70440
---

ReflectionFunction::isDisabled

Verifica si una función está deshabilitada

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public ReflectionFunction::isDisabled(): bool
```php

Verifica si una función está deshabilitada, mediante la directiva [disable_functions](#ini.disable-functions).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la función está deshabilitada, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido deprecada, ya que no es posible construir un `ReflectionFunction` para funciones deshabilitadas. |

## Véase también

ReflectionFunctionAbstract::isUserDefined, [Directiva disable_functions](#ini.disable-functions)
