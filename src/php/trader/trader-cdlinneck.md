---
title: trader_cdlinneck
description: Patrón Formación en el cuello
source_url: https://www.php.net/manual/es/function.trader-cdlinneck.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-cdlinneck.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 94960
---

trader_cdlinneck

Patrón Formación en el cuello

## Descripción

```php
trader_cdlinneck(array $open, array $high, array $low, array $close): array
```php

## Parámetros

`open`  
Precio abierto, array de valores reales.

`high`  
Precio alto, array de valores reales.

`low`  
Precio bajo, array de valores reales.

`close`  
Precio cerrado, array de valores reales.

## Valores devueltos

Devuelve un array con los datos calculados o false en caso de fallo.
