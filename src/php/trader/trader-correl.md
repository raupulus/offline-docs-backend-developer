---
title: trader_correl
description: Coeficiente de correlación de Pearson (r)
source_url: https://www.php.net/manual/es/function.trader-correl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-correl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95270
---

trader_correl

Coeficiente de correlación de Pearson (r)

## Descripción

```php
trader_correl(array $real0, array $real1, [int $timePeriod]): array
```php

## Parámetros

`real0`  
Array de valores reales.

`real1`  
Array de valores reales.

`timePeriod`  
Número de período. Intervalo válido: 2 a 100000.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
