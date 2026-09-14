---
title: enchant_dict_check
description: Verifica si una palabra está correctamente escrita
source_url: https://www.php.net/manual/es/function.enchant-dict-check.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-check.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17480
---

enchant_dict_check

Verifica si una palabra está correctamente escrita

## Descripción

```php
enchant_dict_check(EnchantDictionary $dictionary, string $word): bool
```php

Devuelve `true` si la palabra `word` está correctamente escrita, `false` en caso contrario.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`word`  
La palabra a verificar

## Valores devueltos

Devuelve `true` si la palabra está correctamente escrita, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |
