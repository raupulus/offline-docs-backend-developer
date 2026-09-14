---
title: trader_stddev
description: Desviación estándar
source_url: https://www.php.net/manual/es/function.trader-stddev.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-stddev.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95900
---

trader_stddev

Desviación estándar

## Descripción

```php
trader_stddev(array $real, [int $timePeriod], [float $nbDev]): array
```php

## Parámetros

`real`  
Array de valores reales.

`timePeriod`  
Número de período. Intervalo válido: 2 a 100000.

`nbDev`  

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
