---
title: trader_t3
description: Media móvil exponencial triple (T3)
source_url: https://www.php.net/manual/es/function.trader-t3.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-t3.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95960
---

trader_t3

Media móvil exponencial triple (T3)

## Descripción

```php
trader_t3(array $real, [int $timePeriod], [float $vFactor]): array
```php

## Parámetros

`real`  
Array de valores reales.

`timePeriod`  
Número de período. Intervalo válido: 2 a 100000.

`vFactor`  
Factor de volumen. Intervalo válido: 1 a 0.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
