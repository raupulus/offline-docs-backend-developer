---
title: Ds\Vector::sort
description: Ordena el vector en su lugar
source_url: https://www.php.net/manual/es/ds-vector.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 2226ad08f
order: 16470
---

Ds\Vector::sort

Ordena el vector en su lugar

## Descripción

```php
public Ds\Vector::sort([callable $comparator]): void
```php

Ordena el vector en su lugar, utilizando una función `comparator` opcional.

## Parámetros

`comparator`  
La función de comparación debe retornar un entero menor que, igual a, o mayor que 0 si el primer argumento es considerado, respectivamente, menor que, igual a, o mayor que el segundo.

```php
callback(mixed $a, mixed $b): int
```

> [!CAUTION]
> Devolver valores *no enteros* (como `float`) desde la función de comparación resultará en una conversión interna del valor de retorno de la retrollamada a `int`. Así, valores como `0.99` y `0.1` serán convertidos ambos al valor entero `0`, por lo que se compararán como iguales.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Vector::sort`

```php
<?php
$vector = new \Ds\Vector([4, 5, 1, 3, 2]);
$vector->sort();

print_r($vector);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
        [4] => 5
    )

Ejemplo de `Ds\Vector::sort` utilizando un comparador

```php
<?php
$vector = new \Ds\Vector([4, 5, 1, 3, 2]);

$vector->sort(function($a, $b) {
    return $b <=> $a;
});

print_r($vector);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => 5
        [1] => 4
        [2] => 3
        [3] => 2
        [4] => 1
    )
