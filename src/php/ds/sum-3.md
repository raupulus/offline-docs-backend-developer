---
title: Ds\Sequence::sum
description: Devuelve la suma de todos los valores de la secuencia
source_url: https://www.php.net/manual/es/ds-sequence.sum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/sum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: eb0bd932e
order: 15740
---

Ds\Sequence::sum

Devuelve la suma de todos los valores de la secuencia

## Descripción

```php
abstract public Ds\Sequence::sum(): int
```php

Devuelve la suma de todos los valores de la secuencia.

> [!NOTE]
> Los arrays y los objetos se consideran iguales a cero en el cálculo de la suma.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La suma de todos los valores de la secuencia como `float` o `int` dependiendo de los valores de la secuencia.

## Ejemplos

Ejemplo de `Ds\Sequence::sum` con un entero

```
<?php
$sequence = new \Ds\Vector([1, 2, 3]);
var_dump($sequence->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(6)

Ejemplo de `Ds\Sequence::sum` con un número de punto flotante

```
<?php
$sequence = new \Ds\Vector([1, 2.5, 3]);
var_dump($sequence->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    float(6.5)
