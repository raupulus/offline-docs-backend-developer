---
title: Ds\Vector::rotate
description: Rota el vector un cierto número de rotaciones
source_url: https://www.php.net/manual/es/ds-vector.rotate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/rotate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 16430
---

Ds\Vector::rotate

Rota el vector un cierto número de rotaciones

## Descripción

```php
public Ds\Vector::rotate(int $rotations): void
```php

Rota el vector un cierto número de rotaciones, lo que equivale a llamar sucesivamente `$vector->push($vector->shift())` si el número de rotaciones es positivo, o `$vector->unshift($vector->pop())` si es negativo.

## Parámetros

`rotations`  
El número de veces que el vector debe ser rotado.

## Valores devueltos

No se retorna ningún valor.. El vector de la instancia actual será rotado.

## Ejemplos

Ejemplo de `Ds\Vector::rotate`

```
<?php
$vector = new \Ds\Vector(["a", "b", "c", "d"]);

$vector->rotate(1);  // "a" es desplazado, luego empujado.
print_r($vector);

$vector->rotate(2);  // ambos son desplazados, luego empujados.
print_r($vector);
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
