---
title: trader_apo
description: Oscilador de precio absoluto
source_url: https://www.php.net/manual/es/function.trader-apo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-apo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 94530
---

trader_apo

Oscilador de precio absoluto

## Descripción

```php
trader_apo(array $real, [int $fastPeriod], [int $slowPeriod], [int $mAType]): array
```php

## Parámetros

`real`  
Array de valores reales.

`fastPeriod`  
Número de período para el MA rápido. Intervalo válido: 2 a 100000.

`slowPeriod`  
Número de período para el MA. Intervalo válido: 2 a 100000.

`mAType`  
Tipo de media móvil. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
