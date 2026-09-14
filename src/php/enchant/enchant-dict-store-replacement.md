---
title: enchant_dict_store_replacement
description: Añade una ortografía para una palabra
source_url: https://www.php.net/manual/es/function.enchant-dict-store-replacement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-store-replacement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: true
translation_revision: 330a38c4d
order: 17540
---

enchant_dict_store_replacement

Añade una ortografía para una palabra

## Descripción

```php
enchant_dict_store_replacement(EnchantDictionary $dictionary, string $misspelled, string $correct): void
```php

Añade una ortografía para `misspelled` utilizando `correct`. Tenga en cuenta que si se reemplaza @mis por @cor, entonces es probable que las futuras ocurrencias de @mis sean reemplazadas por @cor. Así, @cor será añadido a la lista de sugerencias.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`misspelled`  
La palabra a tratar

`correct`  
La palabra correcta

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |
