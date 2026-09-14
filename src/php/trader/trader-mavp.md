---
title: trader_mavp
description: Media móvil con periodo variable
source_url: https://www.php.net/manual/es/function.trader-mavp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-mavp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95570
---

trader_mavp

Media móvil con periodo variable

## Descripción

```php
trader_mavp(array $real, array $periods, [int $minPeriod], [int $maxPeriod], [int $mAType]): array
```php

## Parámetros

`real`  
Array de valores reales.

`periods`  
Array de valores reales.

`minPeriod`  
Un valor inferior al mínimo será modificado a la período mínimo. Intervalo válido: 2 a 100000

`maxPeriod`  
Un valor superior al mínimo será modificado a la período máximo. Intervalo válido: 2 a 100000

`mAType`  
Tipo de media móvil. Una constante de la serie [TRADER_MA_TYPE\_\*](#trader.constants) debe ser utilizada.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
