---
title: trader_set_unstable_period
description: Establece el periodo inestable
source_url: https://www.php.net/manual/es/function.trader-set-unstable-period.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/trader/functions/trader-set-unstable-period.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: trader
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 95850
---

trader_set_unstable_period

Establece el periodo inestable

## Descripción

```php
trader_set_unstable_period(int $functionId, int $timePeriod): void
```php

Factor de periodos inestables de influencia para funciones, las cuales son sensibles a él. Se puede encontrar más información sobre periodos inestables en la página de la documentación de la API [TA-Lib](https://ta-lib.org/api/?h=unstable#Unstable+Period).

## Parámetros

`functionId`  
El ID de la función para la cual debería establecerse el factor. Se pueden usar la serie de constantes [TRADER_FUNC_UNST\_\*](#trader.constants) para afectar a la función correspondiente.

`timePeriod`  
El valor de periodo inestable.

## Valores devueltos

No se retorna ningún valor.
