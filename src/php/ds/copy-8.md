---
title: Ds\Stack::copy
description: Devuelve una copia superficial de la pila
source_url: https://www.php.net/manual/es/ds-stack.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/stack/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16100
---

Ds\Stack::copy

Devuelve una copia superficial de la pila

## Descripción

```php
public Ds\Stack::copy(): Ds\Stack
```php

Devuelve una copia superficial de la pila.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial de la pila.

## Ejemplos

Ejemplo de `Ds\Stack::copy`

```
<?php
$a = new \Ds\Stack([1, 2, 3]);
$b = $a->copy();

// Cambiar la copia no afecta al original
$b->push(4);

print_r($a);
print_r($b);
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
        [0] => 4
        [1] => 3
        [2] => 2
        [3] => 1
    )
