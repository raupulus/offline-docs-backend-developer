---
title: get_magic_quotes_gpc
description: Devuelve la configuración actual de la opción magic_quotes_gpc
source_url: https://www.php.net/manual/es/function.get-magic-quotes-gpc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-magic-quotes-gpc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 06313c3bb
order: 38910
---

get_magic_quotes_gpc

Devuelve la configuración actual de la opción magic_quotes_gpc

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
get_magic_quotes_gpc(): false
```php

Siempre devuelve `false`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Siempre devuelve `false`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |
| 7.4.0   | Esta función está obsoleta.     |

## Véase también

`addslashes`, `stripslashes`, `get_magic_quotes_runtime`, `ini_get`
