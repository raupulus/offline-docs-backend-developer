---
title: enchant_dict_add
description: Añadir una palabra a la lista personal de palabras
source_url: https://www.php.net/manual/es/function.enchant-dict-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-dict-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17470
---

enchant_dict_add

Añadir una palabra a la lista personal de palabras

## Descripción

```php
enchant_dict_add(EnchantDictionary $dictionary, string $word): void
```php

Añade una palabra a la lista personal de palabras del diccionario dado.

## Parámetros

`dictionary`  
Un diccionario Enchant devuelto por `enchant_broker_request_dict` o `enchant_broker_request_pwl_dict`.

`word`  
La palabra a añadir

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dictionary` ahora espera una instancia de `EnchantDictionary`; anteriormente, se esperaba un `resource`. |

## Ejemplos

Añadir una palabra a una PWL

```
<?php

$filename = './my_word_list.pwl';
$word = 'Supercalifragilisticexpialidocious';

$broker = enchant_broker_init();
$dict = enchant_broker_request_pwl_dict($broker, $filename);

enchant_dict_add($dict, $word);

?>

   
```php

## Véase también

enchant_broker_request_pwl_dict

enchant_broker_request_dict
