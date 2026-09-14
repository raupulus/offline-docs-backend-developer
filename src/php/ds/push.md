---
title: Ds\Deque::push
description: Añade valores al final del deque
source_url: https://www.php.net/manual/es/ds-deque.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 14650
---

Ds\Deque::push

Añade valores al final del deque

## Descripción

```php
public Ds\Deque::push(mixed ...$values): void
```php

Añade los valores al final del deque.

## Parámetros

`values`  
Los valores a añadir.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Deque::push`

```
<?php
$deque = new \Ds\Deque();

$deque->push("a");
$deque->push("b");
$deque->push("c", "d");
$deque->push(...["e", "f"]);

print_r($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Deque Object
    (
        [0] => a
        [1] => b
        [2] => c
        [3] => d
        [4] => e
        [5] => f
    )
