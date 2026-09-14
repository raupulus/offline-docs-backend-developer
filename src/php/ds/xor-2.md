---
title: Ds\Set::xor
description: Crear un nuevo conjunto utilizando los valores de la instancia actual
  o de otro conjunto, pero no de ambos
source_url: https://www.php.net/manual/es/ds-set.xor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/xor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 16050
---

Ds\Set::xor

Crear un nuevo conjunto utilizando los valores de la instancia actual o de otro conjunto, pero no de ambos

## Descripción

```php
public Ds\Set::xor(Ds\Set $set): Ds\Set
```php

Crear un nuevo conjunto que contiene los valores de la instancia actual o de otro `set`,

`A ⊖ B = {x : x ∈ (A \ B) ∪ (B \ A)}`

## Parámetros

`set`  
El otro conjunto.

## Valores devueltos

Un nuevo conjunto que contiene los valores de la instancia actual o de otro `set`, pero no de ambos.

## Véase también

[Diferencia simétrica](https://en.wikipedia.org/wiki/Symmetric_difference) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Set::xor`

```
<?php
$a = new \Ds\Set([1, 2, 3]);
$b = new \Ds\Set([3, 4, 5]);

var_dump($a->xor($b));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#3 (4) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(4)
      [3]=>
      int(5)
    }
