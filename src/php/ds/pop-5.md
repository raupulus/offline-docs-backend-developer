---
title: Ds\Stack::pop
description: Elimina y devuelve el valor en la parte superior de la pila
source_url: https://www.php.net/manual/es/ds-stack.pop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/stack/pop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16150
---

Ds\Stack::pop

Elimina y devuelve el valor en la parte superior de la pila

## Descripción

```php
public Ds\Stack::pop(): mixed
```php

Elimina y devuelve el valor en la parte superior de la pila.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor eliminado que estaba en la parte superior de la pila.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Stack::pop`

```
<?php
$stack = new \Ds\Stack();

$stack->push("a");
$stack->push("b");
$stack->push("c");

var_dump($stack->pop());
var_dump($stack->pop());
var_dump($stack->pop());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "c"
    string(1) "b"
    string(1) "a"
