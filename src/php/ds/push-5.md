---
title: Ds\Stack::push
description: Añade valores a la pila
source_url: https://www.php.net/manual/es/ds-stack.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/stack/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 16160
---

Ds\Stack::push

Añade valores a la pila

## Descripción

```php
public Ds\Stack::push(mixed ...$values): void
```php

Añade los `values` a la pila.

## Parámetros

`values`  
Los valores a añadir a la pila.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Stack::push`

```
<?php
$stack = new \Ds\Stack();

$stack->push("a");
$stack->push("b");
$stack->push("c", "d");
$stack->push(...["e", "f"]);

print_r($stack);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Stack Object
    (
        [0] => a
        [1] => b
        [2] => c
        [3] => d
        [4] => e
        [5] => f
    )
