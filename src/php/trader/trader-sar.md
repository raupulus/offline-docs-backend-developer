---
title: trader_sar
description: Sistema parabólico
source_url: https://www.php.net/manual/es/function.trader-sar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-sar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 95820
---

trader_sar

Sistema parabólico

## Descripción

```php
trader_sar(array $high, array $low, [float $acceleration], [float $maximum]): array
```php

## Parámetros

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`acceleration`  
Factor de aceleración usado hasta el valor máximo. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`maximum`  
Valor máximo del factor de aceleración. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
