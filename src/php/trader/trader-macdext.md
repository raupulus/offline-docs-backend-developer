---
title: trader_macdext
description: MACD con tipo MA controlable
source_url: https://www.php.net/manual/es/function.trader-macdext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-macdext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95540
---

trader_macdext

MACD con tipo MA controlable

## Descripción

```php
trader_macdext(array $real, [int $fastPeriod], [int $fastMAType], [int $slowPeriod], [int $slowMAType], [int $signalPeriod], [int $signalMAType]): array
```php

## Parámetros

`real`  
Array de valores reales.

`fastPeriod`  
Número de período para el MA rápido. Intervalo válido: 2 a 100000.

`fastMAType`  
Tipo de media móvil para MA rápido. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

`slowPeriod`  
Número de período para el MA. Intervalo válido: 2 a 100000.

`slowMAType`  
Tipo de media móvil para MA lento. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

`signalPeriod`  
Suavizado de la línea de señal (número de período). Intervalo válido: 1 a 100000.

`signalMAType`  
Tipo de media móvil para la línea de señal. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
