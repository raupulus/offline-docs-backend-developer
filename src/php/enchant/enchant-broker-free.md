---
title: enchant_broker_free
description: Libera los recursos del patrocinador así como sus diccionarios
source_url: https://www.php.net/manual/es/function.enchant-broker-free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17360
---

enchant_broker_free

Libera los recursos del patrocinador así como sus diccionarios

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] enchant_broker_free(EnchantBroker $broker): bool
```php

Libera un patrocinador así como todos sus diccionarios. A partir de PHP 8.0.0, se recomienda destruir el objeto en lugar de llamar a esta función.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido deprecada en favor de la desinicialización del objeto. |
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |

## Véase también

enchant_broker_init
