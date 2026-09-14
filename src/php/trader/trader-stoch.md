---
title: trader_stoch
description: Estocástico
source_url: https://www.php.net/manual/es/function.trader-stoch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-stoch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95910
---

trader_stoch

Estocástico

## Descripción

```php
trader_stoch(array $high, array $low, array $close, [int $fastK_Period], [int $slowK_Period], [int $slowK_MAType], [int $slowD_Period], [int $slowD_MAType]): array
```php

## Parámetros

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`close`  
Precio cerrado, array de valores reales.

`fastK_Period`  
Período de tiempo para construir la línea Fast-K. Intervalo válido: 1 a 100000.

`slowK_Period`  
Suavizado para realizar la línea Slow-K. Intervalo válido: 1 a 100000, habitualmente definido a 3.

`slowK_MAType`  
Tipo de media móvil para Slow-K. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

`slowD_Period`  
Suavizado para realizar la línea Slow-D. Intervalo válido: 1 a 100000.

`slowD_MAType`  
Tipo de media móvil para Slow-D. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
