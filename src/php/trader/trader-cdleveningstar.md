---
title: trader_cdleveningstar
description: Estrella de Atardecer
source_url: https://www.php.net/manual/es/function.trader-cdleveningstar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-cdleveningstar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 94840
---

trader_cdleveningstar

Estrella de Atardecer

## Descripción

```php
trader_cdleveningstar(array $open, array $high, array $low, array $close, [float $penetration]): array
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
