---
title: Ds\Deque::rotate
description: Rota el deque un cierto número de rotaciones
source_url: https://www.php.net/manual/es/ds-deque.rotate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/deque/rotate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 14700
---

Ds\Deque::rotate

Rota el deque un cierto número de rotaciones

## Descripción

```php
public Ds\Deque::rotate(int $rotations): void
```php

Rota el deque un cierto número de rotaciones, lo que equivale a llamar sucesivamente `$deque->push($deque->shift())` si el número de rotaciones es positivo, o `$deque->unshift($deque->pop())` si es negativo.

## Parámetros

`rotations`  
El número de veces que el deque debe ser rotado.

## Valores devueltos

No se retorna ningún valor.. El deque de la instancia actual será rotado.

## Ejemplos

Ejemplo de `Ds\Deque::rotate`

```
<?php
$deque = new \Ds\Deque(["a", "b", "c", "d"]);

$deque->rotate(1);  // "a" es desplazado, luego empujado.
print_r($deque);

$deque->rotate(2);  // "b" y "c" son ambos desplazados, luego empujados.
print_r($deque);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    (
        [0] => b
        [1] => c
        [2] => d
        [3] => a
    )
    Ds\Deque Object
    (
        [0] => d
        [1] => a
        [2] => b
        [3] => c
    )
