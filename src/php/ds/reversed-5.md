---
title: Ds\Vector::reversed
description: Devuelve una copia invertida
source_url: https://www.php.net/manual/es/ds-vector.reversed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/reversed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16420
---

Ds\Vector::reversed

Devuelve una copia invertida

## Descripción

```php
public Ds\Vector::reversed(): Ds\Vector
```php

Devuelve una copia invertida del vector.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia invertida del vector.

> [!NOTE]
> La instancia actual no se ve afectada.

## Ejemplos

Ejemplo de `Ds\Vector::reversed`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);

print_r($vector->reversed());
print_r($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => c
        [1] => b
        [2] => a
    )
    Ds\Vector Object
    (
        [0] => a
        [1] => b
        [2] => c
    )
