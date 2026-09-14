---
title: trader_macdfix
description: Convergencia/divergencia fija 12/26 de la media móvil
source_url: https://www.php.net/manual/es/function.trader-macdfix.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-macdfix.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 95550
---

trader_macdfix

Convergencia/divergencia fija 12/26 de la media móvil

## Descripción

```php
trader_macdfix(array $real, [int $signalPeriod]): array
```php

## Parámetros

`real`  
Array de valores reales.

`signalPeriod`  
Suavizado de la línea de señal (número de período). Intervalo válido: 1 a 100000.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de error.
