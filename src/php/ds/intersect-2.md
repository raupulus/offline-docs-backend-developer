---
title: Ds\Set::intersect
description: Crear un nuevo conjunto utilizando valores comunes con otra secuencia
source_url: https://www.php.net/manual/es/ds-set.intersect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/intersect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 15880
---

Ds\Set::intersect

Crear un nuevo conjunto utilizando valores comunes con otra secuencia

## Descripción

```php
public Ds\Set::intersect(Ds\Set $set): Ds\Set
```php

Crear un nuevo conjunto utilizando valores comunes con otro `set`. En otras palabras, devuelve una copia de la instancia actual con todos los valores eliminados que no están en el otro `set`.

`A ∩ B = {x : x ∈ A ∧ x ∈ B}`

## Parámetros

`set`  
La otra secuencia.

## Valores devueltos

La intersección de la instancia actual y otro `set`.

## Véase también

[Intersección](https://en.wikipedia.org/wiki/Intersection_(set_theory)) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Set::intersect`

```
<?php
$a = new \Ds\Set([1, 2, 3]);
$b = new \Ds\Set([3, 4, 5]);

var_dump($a->intersect($b));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#3 (1) {
      [0]=>
      int(3)
    }
