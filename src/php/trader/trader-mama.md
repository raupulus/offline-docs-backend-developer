---
title: trader_mama
description: Media móvil adaptativa MESA
source_url: https://www.php.net/manual/es/function.trader-mama.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-mama.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 95560
---

trader_mama

Media móvil adaptativa MESA

## Descripción

```php
trader_mama(array $real, [float $fastLimit], [float $slowLimit]): array
```php

## Parámetros

`real`  
Array de valores reales.

`fastLimit`  
Límite superior del algoritmo adaptativo. Intervalo válido: 0.01 a 0.99.

`slowLimit`  
Límite inferior del algoritmo adaptativo. Intervalo válido: 0.01 a 0.99.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
