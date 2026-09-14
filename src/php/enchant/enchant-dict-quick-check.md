---
title: enchant_dict_quick_check
description: Verifica si la palabra está correctamente escrita y proporciona sugerencias
source_url: https://www.php.net/manual/es/function.enchant-dict-quick-check.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-quick-check.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17530
---

enchant_dict_quick_check

Verifica si la palabra está correctamente escrita y proporciona sugerencias

## Descripción

```php
enchant_dict_quick_check(EnchantDictionary $dictionary, string $word, [array $suggestions]): bool
```php

Devuelve `true` si la palabra está correctamente escrita, `false` si la variable de sugerencias es proporcionada, y la llena con las sugerencias posibles.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`word`  
La palabra a verificar

`suggestions`  
Si la palabra no está correctamente escrita, esta variable contendrá un array de sugerencias.

## Valores devueltos

Devuelve `true` si la palabra está correctamente escrita, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `enchant_dict_quick_check`

```
<?php
$tag = 'en_US';
$r = enchant_broker_init();

if (enchant_broker_dict_exists($r,$tag)) {
    $d = enchant_broker_request_dict($r, $tag);
    enchant_dict_quick_check($d, 'soong', $suggs);
    print_r($suggs);
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => song
        [1] => snog
        [2] => soon
        [3] => Sang
        [4] => Sung
        [5] => sang
        [6] => sung
        [7] => sponge
        [8] => spongy
        [9] => snag
        [10] => snug
        [11] => sonic
        [12] => sing
        [13] => songs
        [14] => Son
        [15] => Sonja
        [16] => Synge
        [17] => son
        [18] => Sejong
        [19] => sarong
        [20] => sooner
        [21] => Sony
        [22] => sown
        [23] => scone
        [24] => song's
    )

## Véase también

enchant_dict_check

enchant_dict_suggest
