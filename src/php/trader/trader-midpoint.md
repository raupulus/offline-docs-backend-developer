---
title: trader_midpoint
description: Punto medio sobre un periodo
source_url: https://www.php.net/manual/es/function.trader-midpoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-midpoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95620
---

trader_midpoint

Punto medio sobre un periodo

## Descripción

```php
trader_midpoint(array $real, [int $timePeriod]): array
```php

## Parámetros

`real`  
Array de valores reales.

`timePeriod`  
Número de período. Intervalo válido: 2 a 100000.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
