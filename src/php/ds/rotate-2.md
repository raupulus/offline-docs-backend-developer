---
title: Ds\Sequence::rotate
description: Rota la secuencia un número dado de rotaciones
source_url: https://www.php.net/manual/es/ds-sequence.rotate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/rotate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 15680
---

Ds\Sequence::rotate

Rota la secuencia un número dado de rotaciones

## Descripción

```php
abstract public Ds\Sequence::rotate(int $rotations): void
```php

Rota la secuencia un cierto número de rotaciones, lo que equivale a llamar sucesivamente `$deque->push($deque->shift())` si el número de rotaciones es positivo, o `$deque->unshift($deque->pop())` si es negativo.

## Parámetros

`rotations`  
El número de veces que la secuencia debe ser rotada.

## Valores devueltos

No se retorna ningún valor.. La secuencia de la instancia actual será rotada.

## Ejemplos

Ejemplo de `Ds\Sequence::rotate`

```
<?php
$sequence = new \Ds\Vector(["a", "b", "c", "d"]);

$sequence->rotate(1);  // "a" es desplazado, luego empujado.
print_r($sequence);

$sequence->rotate(2);  // "b" y "c" son ambos desplazados, luego empujados.
print_r($sequence);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    (
        [0] => b
        [1] => c
        [2] => d
        [3] => a
    )
    Ds\Vector Object
    (
        [0] => d
        [1] => a
        [2] => b
        [3] => c
    )
