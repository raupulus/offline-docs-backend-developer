---
title: Ds\Pair::copy
description: Devuelve una copia superficial del par
source_url: https://www.php.net/manual/es/ds-pair.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/pair/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15210
---

Ds\Pair::copy

Devuelve una copia superficial del par

## Descripción

```php
public Ds\Pair::copy(): Ds\Pair
```php

Devuelve una copia superficial del par.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial del par.

## Ejemplos

Ejemplo de `Ds\Pair::copy`

```
<?php
$a = new \Ds\Pair("a", 1);
$b = $a->copy();

$a->key = "x";

print_r($a);
print_r($b);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Pair Object
    (
        [key] => x
        [value] => 1
    )
    Ds\Pair Object
    (
        [key] => a
        [value] => 1
    )
