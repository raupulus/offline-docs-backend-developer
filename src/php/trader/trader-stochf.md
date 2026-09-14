---
title: trader_stochf
description: Estocástico rápido
source_url: https://www.php.net/manual/es/function.trader-stochf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-stochf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95920
---

trader_stochf

Estocástico rápido

## Descripción

```php
trader_stochf(array $high, array $low, array $close, [int $fastK_Period], [int $fastD_Period], [int $fastD_MAType]): array
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

`fastD_Period`  
Suavizado para realizar la línea Fast-D. Intervalo válido: 1 a 100000, habitualmente definido a 3.

`fastD_MAType`  
Tipo de media móvil para Fast-D. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
