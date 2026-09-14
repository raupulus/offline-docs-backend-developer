---
title: trader_sarext
description: Sistema parabólico - Extendido
source_url: https://www.php.net/manual/es/function.trader-sarext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-sarext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 95830
---

trader_sarext

Sistema parabólico - Extendido

## Descripción

```php
trader_sarext(array $high, array $low, [float $startValue], [float $offsetOnReverse], [float $accelerationInitLong], [float $accelerationLong], [float $accelerationMaxLong], [float $accelerationInitShort], [float $accelerationShort], [float $accelerationMaxShort]): array
```php

## Parámetros

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`startValue`  
Valor inicial y dirección. 0 para Auto, \>0 para Long, \<0 para Short. Rango válido de [TRADER_REAL_MIN](#constant.trader-real-min) hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`offsetOnReverse`  
Índice de porcentaje añadido/eliminado a la parada inicial sobre el reverso short/long reversal. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`accelerationInitLong`  
Valor inicial del factor de aceleración para la dirección Long. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`accelerationLong`  
Factor de acelereción para la dirección Long. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`accelerationMaxLong`  
Valor máximo del factor de aceleración para la dirección Long. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`accelerationInitShort`  
Valor inicial del factor de aceleración para la dirección Short. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`accelerationShort`  
Factor de aceleración para la dirección Short. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

`accelerationMaxShort`  
Valor máximo del factor de aceleración para la dirección Short. Rango válido de 0 hasta [TRADER_REAL_MAX](#constant.trader-real-max).

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
