---
title: trader_ultosc
description: Oscilador final
source_url: https://www.php.net/manual/es/function.trader-ultosc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-ultosc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 96050
---

trader_ultosc

Oscilador final

## Descripción

```php
trader_ultosc(array $high, array $low, array $close, [int $timePeriod1], [int $timePeriod2], [int $timePeriod3]): array
```php

## Parámetros

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`close`  
Precio cerrado, array de valores reales.

`timePeriod1`  
Número de barras para el primer periodo. Rango válido de 1 hasta 100000.

`timePeriod2`  
Número de barras para el segundo periodo. Rango válido de 1 hasta 100000.

`timePeriod3`  
Número de barras para el tercer periodo. Rango válido de 1 hasta 100000.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
