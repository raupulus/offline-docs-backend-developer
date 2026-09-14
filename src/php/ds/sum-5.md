---
title: Ds\Vector::sum
description: Devuelve la suma de todos los valores del vector
source_url: https://www.php.net/manual/es/ds-vector.sum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/sum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: eb0bd932e
order: 16490
---

Ds\Vector::sum

Devuelve la suma de todos los valores del vector

## Descripción

```php
public Ds\Vector::sum(): int
```php

Devuelve la suma de todos los valores del vector.

> [!NOTE]
> Los arrays y los objetos se consideran iguales a cero durante el cálculo de la suma.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La suma de todos los valores del vector como `float` o `int` dependiendo de los valores del vector.

## Ejemplos

Ejemplo de `Ds\Vector::sum` con un entero

```
<?php
$vector = new \Ds\Vector([1, 2, 3]);
var_dump($vector->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(6)

Ejemplo de `Ds\Vector::sum` con un número de punto flotante

```
<?php
$vector = new \Ds\Vector([1, 2.5, 3]);
var_dump($vector->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    float(6.5)
