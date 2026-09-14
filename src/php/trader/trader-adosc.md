---
title: trader_adosc
description: Oscilador A/D Chaikin
source_url: https://www.php.net/manual/es/function.trader-adosc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-adosc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 94500
---

trader_adosc

Oscilador A/D Chaikin

## Descripción

```php
trader_adosc(array $high, array $low, array $close, array $volume, [int $fastPeriod], [int $slowPeriod]): array
```php

## Parámetros

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`close`  
Precio cerrado, array de valores reales.

`volume`  
Volumen intercambiado, array de valores reales.

`fastPeriod`  
Número de período para el MA rápido. Intervalo válido: 2 a 100000.

`slowPeriod`  
Número de período para el MA. Intervalo válido: 2 a 100000.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
