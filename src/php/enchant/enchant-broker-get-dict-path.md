---
title: enchant_broker_get_dict_path
description: Obtiene la ruta del directorio para un backend proporcionado
source_url: https://www.php.net/manual/es/function.enchant-broker-get-dict-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-get-dict-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17370
---

enchant_broker_get_dict_path

Obtiene la ruta del directorio para un backend proporcionado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] enchant_broker_get_dict_path(EnchantBroker $broker, int $type): string
```php

Obtiene la ruta del directorio para un backend proporcionado.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

`type`  
El tipo de diccionarios, es decir, `ENCHANT_MYSPELL` o `ENCHANT_ISPELL`.

## Valores devueltos

Devuelve la ruta del directorio del diccionario en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido deprecada. |
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |

## Notas

> [!NOTE]
> Esta función solo está disponible si la extensión ha sido compilada con Enchant v1.

## Véase también

enchant_broker_set_dict_path
