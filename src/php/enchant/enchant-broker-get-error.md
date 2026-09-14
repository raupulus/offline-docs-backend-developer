---
title: enchant_broker_get_error
description: Devuelve el último error de un sponsor
source_url: https://www.php.net/manual/es/function.enchant-broker-get-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-get-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17380
---

enchant_broker_get_error

Devuelve el último error de un sponsor

## Descripción

```php
enchant_broker_get_error(EnchantBroker $broker): string
```php

Devuelve el último error ocurrido para este sponsor.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

## Valores devueltos

Devuelve el mensaje si se ha encontrado un error, o `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |
