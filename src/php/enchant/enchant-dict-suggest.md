---
title: enchant_dict_suggest
description: Sugerir ortografías para una palabra
source_url: https://www.php.net/manual/es/function.enchant-dict-suggest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-suggest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 17550
---

enchant_dict_suggest

Sugerir ortografías para una palabra

## Descripción

```php
enchant_dict_suggest(EnchantDictionary $dictionary, string $word): array
```php

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`word`  
Palabra para la que se generarán sugerencias.

## Valores devueltos

Devuelve un array de sugerencias si la palabra está mal escrita.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo de uso de `enchant_dict_suggest`

```
<?php
$tag = 'en_US';
$r = enchant_broker_init();
if (enchant_broker_dict_exists($r,$tag)) {
    $d = enchant_broker_request_dict($r, $tag);

    $wordcorrect = enchant_dict_check($d, "soong");
    if (!$wordcorrect) {
        $suggs = enchant_dict_suggest($d, "soong");
        echo "Sugerencias para 'soong':";
        print_r($suggs);
    }
}
?>

   
```php

## Véase también

enchant_dict_check

enchant_dict_quick_check
