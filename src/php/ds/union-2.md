---
title: Ds\Set::union
description: Crear un nuevo conjunto utilizando los valores de la instancia actual
  y de otro conjunto
source_url: https://www.php.net/manual/es/ds-set.union.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/union.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 16040
---

Ds\Set::union

Crear un nuevo conjunto utilizando los valores de la instancia actual y de otro conjunto

## Descripción

```php
public Ds\Set::union(Ds\Set $set): Ds\Set
```php

Crear un nuevo conjunto que contiene los valores de la instancia actual así como los valores de otro `set`.

`A ∪ B = {x: x ∈ A ∨ x ∈ B}`

## Parámetros

`set`  
El otro conjunto, a combinar con la instancia actual.

## Valores devueltos

Un nuevo conjunto que contiene todos los valores de la instancia actual así como de otro `set`.

## Véase también

[Unión](https://en.wikipedia.org/wiki/Union_(set_theory)) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Set::union`

```
<?php
$a = new \Ds\Set([1, 2, 3]);
$b = new \Ds\Set([3, 4, 5]);

var_dump($a->union($b));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#3 (5) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
      [3]=>
      int(4)
      [4]=>
      int(5)
    }
