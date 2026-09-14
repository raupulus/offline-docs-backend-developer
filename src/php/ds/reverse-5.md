---
title: Ds\Vector::reverse
description: Invertir el vector en su lugar
source_url: https://www.php.net/manual/es/ds-vector.reverse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/reverse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16410
---

Ds\Vector::reverse

Invertir el vector en su lugar

## Descripción

```php
public Ds\Vector::reverse(): void
```php

Invierte el vector en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Vector::reverse`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c"]);
$vector->reverse();

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
