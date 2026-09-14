---
title: enchant_dict_describe
description: Describe un diccionario individual
source_url: https://www.php.net/manual/es/function.enchant-dict-describe.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-describe.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17490
---

enchant_dict_describe

Describe un diccionario individual

## Descripción

```php
enchant_dict_describe(EnchantDictionary $dictionary): array
```php

Devuelve los detalles del diccionario.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |
| 8.0.0 | Antes de esta versión, la función devolvía `false` en caso de error. |

## Ejemplos

Ejemplo de `enchant_dict_describe`

Comprueba si existe un diccionario usando `enchant_broker_dict_exists` y muestra sus detalles.

```
<?php
$tag = 'en_US';
$broker = enchant_broker_init();
if (enchant_broker_dict_exists($broker, $tag)) {
    $dict = enchant_broker_request_dict($broker, $tag);
    $dict_details = enchant_dict_describe($dict);
    print_r($dict_details);
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [lang] => en_US
        [name] => aspell
        [desc] => Proveedor Aspell
        [file] => /usr/lib/enchant/libenchant_aspell.so
    )
