---
title: enchant_dict_add_to_session
description: Añade una palabra a la sesión actual
source_url: https://www.php.net/manual/es/function.enchant-dict-add-to-session.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-add-to-session.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17460
---

enchant_dict_add_to_session

Añade una palabra a la sesión actual

## Descripción

```php
enchant_dict_add_to_session(EnchantDictionary $dictionary, string $word): void
```php

Añade la palabra `word` al diccionario proporcionado. Solo será añadida para la sesión actual.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`word`  
La palabra a añadir

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |

## Véase también

enchant_broker_request_dict
