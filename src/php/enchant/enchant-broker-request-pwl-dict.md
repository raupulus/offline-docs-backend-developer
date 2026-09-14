---
title: enchant_broker_request_pwl_dict
description: Crea un diccionario utilizando un archivo PWL
source_url: https://www.php.net/manual/es/function.enchant-broker-request-pwl-dict.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-request-pwl-dict.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 17420
---

enchant_broker_request_pwl_dict

Crea un diccionario utilizando un archivo PWL

## Descripción

```php
enchant_broker_request_pwl_dict(EnchantBroker $broker, string $filename): EnchantDictionary
```php

Crea un diccionario utilizando un archivo PWL. Un archivo PWL es un archivo de palabras personales que contiene una palabra por línea.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

`filename`  
Ruta de acceso al archivo PWL. Si el archivo no existe, se creará uno nuevo, si es posible.

## Valores devueltos

Devuelve un recurso de diccionario en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `EnchantDictionary` ; anteriormente se devolvía una `resource`. |

## Véase también

enchant_dict_describe

enchant_broker_dict_exists

enchant_broker_free_dict
