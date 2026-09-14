---
title: Ds\Vector::clear
description: Elimina todos los valores
source_url: https://www.php.net/manual/es/ds-vector.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16210
---

Ds\Vector::clear

Elimina todos los valores

## Descripción

```php
public Ds\Vector::clear(): void
```php

Elimina todos los valores del vector.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Vector::clear`

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);
print_r($vector);

$vector->clear();
print_r($vector);
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
    )
