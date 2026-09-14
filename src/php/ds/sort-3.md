---
title: Ds\Sequence::sort
description: Ordena la secuencia en su lugar
source_url: https://www.php.net/manual/es/ds-sequence.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/sequence/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 2226ad08f
order: 15720
---

Ds\Sequence::sort

Ordena la secuencia en su lugar

## Descripción

```php
abstract public Ds\Sequence::sort([callable $comparator]): void
```php

Ordena la secuencia en su lugar, utilizando una función de comparación opcional `comparator`.

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

Ejemplo de `Ds\Sequence::sort`

```php
<?php
$sequence = new \Ds\Vector([4, 5, 1, 3, 2]);
$sequence->sort();

print_r($sequence);
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

Ejemplo de `Ds\Sequence::sort` utilizando un comparador

```php
<?php
$sequence = new \Ds\Vector([4, 5, 1, 3, 2]);

$sequence->sort(function($a, $b) {
    return $b <=> $a;
});

print_r($sequence);
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
