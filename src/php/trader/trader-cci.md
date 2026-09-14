---
title: trader_cci
description: Índice de Canal de Comodidad
source_url: https://www.php.net/manual/es/function.trader-cci.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-cci.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 94630
---

trader_cci

Índice de Canal de Comodidad

## Descripción

```php
trader_cci(array $high, array $low, array $close, [int $timePeriod]): array
```php

## Parámetros

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`close`  
Precio cerrado, array de valores reales.

`timePeriod`  
Número de período. Intervalo válido: 2 a 100000.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
