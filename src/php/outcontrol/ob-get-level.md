---
title: ob_get_level
description: Devuelve el número de niveles de anidación del sistema de temporización
  de salida
source_url: https://www.php.net/manual/es/function.ob-get-level.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-get-level.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: af7044e82
order: 59820
---

ob_get_level

Devuelve el número de niveles de anidación del sistema de temporización de salida

## Descripción

```php
ob_get_level(): int
```php

Devuelve el número de niveles de anidación del sistema de temporización de salida.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de niveles de anidación del sistema de temporización de salida, y cero si no está activo.

> [!CAUTION]
> El valor para los niveles idénticos entre `ob_get_level` y `ob_get_status` difiere en uno. Para `ob_get_level`, el primer nivel es `1`. Mientras que para `ob_get_status`, el primer nivel es `0`.

## Véase también

`ob_start`, `ob_get_status`, `ob_get_contents`
