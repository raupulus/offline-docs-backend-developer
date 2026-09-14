---
title: enchant_dict_get_error
description: Devuelve el último error de la sesión actual
source_url: https://www.php.net/manual/es/function.enchant-dict-get-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-get-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: true
translation_revision: a6b55f8de
order: 17500
---

enchant_dict_get_error

Devuelve el último error de la sesión actual

## Descripción

```php
enchant_dict_get_error(EnchantDictionary $dictionary): string
```php

Devuelve el último error de la sesión actual.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

## Valores devueltos

Devuelve el mensaje de error en forma de string, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |
