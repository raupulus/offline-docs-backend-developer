---
title: trader_bbands
description: Bandas de Bollinger
source_url: https://www.php.net/manual/es/function.trader-bbands.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-bbands.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 94600
---

trader_bbands

Bandas de Bollinger

## Descripción

```php
trader_bbands(array $real, [int $timePeriod], [float $nbDevUp], [float $nbDevDn], [int $mAType]): array
```php

## Parámetros

`real`  
Array de valores reales.

`timePeriod`  
Número de período. Intervalo válido: 2 a 100000.

`nbDevUp`  
Multiplicador de desviación para la banda superior. Intervalo válido: [TRADER_REAL_MIN](#constant.trader-real-min) a [TRADER_REAL_MAX](#constant.trader-real-max).

`nbDevDn`  
Multiplicador de desviación para la banda inferior. Intervalo válido: [TRADER_REAL_MIN](#constant.trader-real-min) a [TRADER_REAL_MAX](#constant.trader-real-max).

`mAType`  
Tipo de media móvil. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
