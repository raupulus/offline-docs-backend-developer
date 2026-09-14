---
title: trader_get_unstable_period
description: Obtiene el periodo inestable
source_url: https://www.php.net/manual/es/function.trader-get-unstable-period.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-get-unstable-period.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: ad2e71299
order: 95380
---

trader_get_unstable_period

Obtiene el periodo inestable

## Descripción

```php
trader_get_unstable_period(int $functionId): int
```php

Obtiene el factor de periodo inestable para una función en particular.

## Parámetros

`functionId`  
El ID de la función por la que leer el factor. Se debería usar la serie de constantes [TRADER_FUNC_UNST\_\*](#trader.constants).

## Valores devueltos

Devuelve el factor del periodo inestable para la función correspondiente.
