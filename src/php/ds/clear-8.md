---
title: Ds\Stack::clear
description: Elimina todos los valores
source_url: https://www.php.net/manual/es/ds-stack.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/stack/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16080
---

Ds\Stack::clear

Elimina todos los valores

## Descripción

```php
public Ds\Stack::clear(): void
```php

Elimina todos los valores de la pila.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Stack::clear`

```
<?php
$stack = new \Ds\Stack([1, 2, 3]);
print_r($stack);

$stack->clear();
print_r($stack);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Stack Object
    (
        [0] => 3
        [1] => 2
        [2] => 1
    )
    Ds\Stack Object
    (
    )
