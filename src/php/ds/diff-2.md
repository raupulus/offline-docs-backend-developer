---
title: Ds\Set::diff
description: Crear un nuevo conjunto utilizando valores que no están en otra secuencia
source_url: https://www.php.net/manual/es/ds-set.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 15840
---

Ds\Set::diff

Crear un nuevo conjunto utilizando valores que no están en otra secuencia

## Descripción

```php
public Ds\Set::diff(Ds\Set $set): Ds\Set
```php

Crear un nuevo conjunto utilizando valores que no están en otra secuencia.

`A \ B = {x ∈ A | x ∉ B}`

## Parámetros

`set`  
El conjunto que contiene los valores a excluir.

## Valores devueltos

Un nuevo conjunto que contiene todos los valores que no estaban en el otro `set`.

## Véase también

[Complemento](https://en.wikipedia.org/wiki/Complement_(set_theory)) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Set::diff`

```
<?php
$a = new \Ds\Set([1, 2, 3]);
$b = new \Ds\Set([3, 4, 5]);

var_dump($a->diff($b));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#3 (2) {
      [0]=>
      int(1)
      [1]=>
      int(2)
    }
