---
title: enchant_broker_request_dict
description: Crear un nuevo diccionario usando una etiqueta
source_url: https://www.php.net/manual/es/function.enchant-broker-request-dict.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-request-dict.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17410
---

enchant_broker_request_dict

Crear un nuevo diccionario usando una etiqueta

## Descripción

```php
enchant_broker_request_dict(EnchantBroker $broker, string $tag): EnchantDictionary
```php

crea un nuevo diccionario usando una etiqueta, la etiqueta de idioma no vacía que desea solicitar para un diccionario ("en_US", "de_DE", ...)

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

`tag`  
Una etiqueta que describe la configuración local, por ejemplo en_US, de_DE

## Valores devueltos

Devuelve un recurso de diccionario en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `EnchantDictionary`; anteriormente, se devolvía un `resource`. |

## Ejemplos

Un ejemplo de `enchant_broker_request_dict`

Comprueba si existe un diccionario usando `enchant_broker_dict_exists` y solicítalo.

```
<?php
$tag = 'en_US';
$broker = enchant_broker_init();
if (enchant_broker_dict_exists($broker,$tag)) {
    $dict = enchant_broker_request_dict($broker, $tag);
    var_dump($dict);
}
?>

   
```php

## Véase también

enchant_dict_describe

enchant_broker_dict_exists

enchant_broker_free_dict
