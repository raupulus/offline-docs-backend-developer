---
title: trader_cdlmorningstar
description: Lucero del Alba
source_url: https://www.php.net/manual/es/function.trader-cdlmorningstar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-cdlmorningstar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 95070
---

trader_cdlmorningstar

Lucero del Alba

## Descripción

```php
trader_cdlmorningstar(array $open, array $high, array $low, array $close, [float $penetration]): array
```php

## Parámetros

`open`  
Precio abierto, array de valores reales.

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`close`  
Precio cerrado, array de valores reales.

`penetration`  
Porcentaje de penetración de una vela en otra vela.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
