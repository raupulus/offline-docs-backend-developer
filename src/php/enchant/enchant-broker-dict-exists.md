---
title: enchant_broker_dict_exists
description: Verifica si un diccionario existe
source_url: https://www.php.net/manual/es/function.enchant-broker-dict-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-dict-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 17340
---

enchant_broker_dict_exists

Verifica si un diccionario existe

## Descripción

```php
enchant_broker_dict_exists(EnchantBroker $broker, string $tag): bool
```php

Verifica si un diccionario existe.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

`tag`  
lenguaje, en un formato como us_US, ch_DE, etc.

## Valores devueltos

Devuelve `true` si el lenguaje existe, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `enchant_broker_dict_exists`

```
<?php
$tag = 'en_US';
$r = enchant_broker_init();
if (enchant_broker_dict_exists($r,$tag)) {
    echo "Diccionario " . $tag . " encontrado.\n";
}
?>

   
```php

## Véase también

enchant_broker_describe
