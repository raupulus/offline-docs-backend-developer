---
title: Ds\Deque::sum
description: Devuelve la suma de todos los valores del deque
source_url: https://www.php.net/manual/es/ds-deque.sum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/sum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: eb0bd932e
order: 14760
---

Ds\Deque::sum

Devuelve la suma de todos los valores del deque

## Descripción

```php
public Ds\Deque::sum(): int
```php

Devuelve la suma de todos los valores del deque.

> [!NOTE]
> Los arrays y los objetos se consideran iguales a cero durante el cálculo de la suma.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La suma de todos los valores del deque como `float` o `int` dependiendo de los valores del deque.

## Ejemplos

Ejemplo de `Ds\Deque::sum` con un entero

```
<?php
$deque = new \Ds\Deque([1, 2, 3]);
var_dump($deque->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(6)

Ejemplo de `Ds\Deque::sum` con un número de punto flotante

```
<?php
$deque = new \Ds\Deque([1, 2.5, 3]);
var_dump($deque->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    float(6.5)
