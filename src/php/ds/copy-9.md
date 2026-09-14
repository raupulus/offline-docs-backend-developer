---
title: Ds\Vector::copy
description: Devuelve una copia superficial del vector
source_url: https://www.php.net/manual/es/ds-vector.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16240
---

Ds\Vector::copy

Devuelve una copia superficial del vector

## Descripción

```php
public Ds\Vector::copy(): Ds\Vector
```php

Devuelve una copia superficial del vector.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial del vector.

## Ejemplos

Ejemplo de `Ds\Vector::copy`

```
<?php
$a = new \Ds\Vector([1, 2, 3]);
$b = $a->copy();

// Cambiar la copia no afecta al original
$b->push(4);

print_r($a);
print_r($b);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
    )
    Ds\Vector Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
    )
