---
title: enchant_broker_describe
description: Enumera los proveedores Enchant
source_url: https://www.php.net/manual/es/function.enchant-broker-describe.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-describe.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17330
---

enchant_broker_describe

Enumera los proveedores Enchant

## Descripción

```php
enchant_broker_describe(EnchantBroker $broker): array
```php

Enumera los proveedores Enchant y muestra algunas informaciones sobre ellos. Las mismas informaciones son proporcionadas mediante la función `phpinfo`.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

## Valores devueltos

Devuelve un `array` de los proveedores Enchant disponibles con sus detalles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |
| 8.0.0 | Anterior a esta versión, esta función devolvía `false` en caso de error. |

## Ejemplos

Lista las interfaces proporcionadas por un patrocinador dado

```
<?php
$r = enchant_broker_init();
$bprovides = enchant_broker_describe($r);
echo "El patrocinador actual proporciona las siguientes interfaces :\n";
print_r($bprovides);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    El patrocinador actual proporciona las siguientes interfaces :
    Array
    (
        [0] => Array
            (
                [name] => aspell
                [desc] => Aspell Provider
                [file] => /usr/lib/enchant/libenchant_aspell.so
            )

        [1] => Array
            (
                [name] => hspell
                [desc] => Hspell Provider
                [file] => /usr/lib/enchant/libenchant_hspell.so
            )

        [2] => Array
            (
                [name] => ispell
                [desc] => Ispell Provider
                [file] => /usr/lib/enchant/libenchant_ispell.so
            )

        [3] => Array
            (
                [name] => myspell
                [desc] => Myspell Provider
                [file] => /usr/lib/enchant/libenchant_myspell.so
            )

    )
