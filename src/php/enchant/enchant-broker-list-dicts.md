---
title: enchant_broker_list_dicts
description: Devuelve una lista de todos los diccionarios disponibles
source_url: https://www.php.net/manual/es/function.enchant-broker-list-dicts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-list-dicts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17400
---

enchant_broker_list_dicts

Devuelve una lista de todos los diccionarios disponibles

## Descripción

```php
enchant_broker_list_dicts(EnchantBroker $broker): array
```php

Devuelve una lista de todos los diccionarios disponibles junto con sus detalles.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

## Valores devueltos

Devuelve un `array` de diccionarios disponibles con sus detalles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |
| 8.0.0 | Antes de esta versión, la función devolvía `false` en caso de error. |

## Ejemplos

Lista todos los diccionarios disponibles para un sponsor

```
<?php
$r = enchant_broker_init();
$dicts = enchant_broker_list_dicts($r);
print_r($dicts);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [lang_tag] => de
                [provider_name] => aspell
                [provider_desc] => Aspell Provider
                [provider_file] => /usr/lib/enchant/libenchant_aspell.so
            )

        [1] => Array
            (
                [lang_tag] => de_DE
                [provider_name] => aspell
                [provider_desc] => Aspell Provider
                [provider_file] => /usr/lib/enchant/libenchant_aspell.so
            )

        [3] => Array
            (
                [lang_tag] => en
                [provider_name] => aspell
                [provider_desc] => Aspell Provider
                [provider_file] => /usr/lib/enchant/libenchant_aspell.so
            )

        [4] => Array
            (
                [lang_tag] => en_GB
                [provider_name] => aspell
                [provider_desc] => Aspell Provider
                [provider_file] => /usr/lib/enchant/libenchant_aspell.so
            )

        [5] => Array
            (
                [lang_tag] => en_US
                [provider_name] => aspell
                [provider_desc] => Aspell Provider
                [provider_file] => /usr/lib/enchant/libenchant_aspell.so
            )

        [6] => Array
            (
                [lang_tag] => hi_IN
                [provider_name] => myspell
                [provider_desc] => Myspell Provider
                [provider_file] => /usr/lib/enchant/libenchant_myspell.so
            )

    )

## Véase también

enchant_broker_describe
