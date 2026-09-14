---
title: enchant_dict_is_added
description: Si la palabra existe o no en esta sesión de ortografía
source_url: https://www.php.net/manual/es/function.enchant-dict-is-added.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-is-added.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17510
---

enchant_dict_is_added

Si la palabra existe o no en esta sesión de ortografía

## Descripción

```php
enchant_dict_is_added(EnchantDictionary $dictionary, string $word): bool
```php

Informa si la palabra ya existe o no en la sesión actual.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`word`  
La palabra a buscar

## Valores devueltos

Devuelve `true` si la palabra existe o `false`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |

## Véase también

enchant_dict_add_to_session
