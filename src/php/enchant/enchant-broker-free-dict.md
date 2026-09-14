---
title: enchant_broker_free_dict
description: Libera un recurso de diccionario
source_url: https://www.php.net/manual/es/function.enchant-broker-free-dict.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-free-dict.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 17350
---

enchant_broker_free_dict

Libera un recurso de diccionario

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] enchant_broker_free_dict(EnchantDictionary $dictionary): bool
```php

Libera un diccionario. A partir de PHP 8.0.0, se recomienda destruir el objeto en lugar de llamar a esta función.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función está deprecada a favor de la desinicialización del objeto. |
| 8.0.0 | `dictionary` ahora espera una `EnchantDictionary`; anteriormente, se esperaba un `resource`. |

## Véase también

enchant_broker_request_dict

enchant_broker_request_pwl_dict
