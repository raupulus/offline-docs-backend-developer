---
title: Ds\Map::sort
description: Ordena el mapa en el lugar por valor
source_url: https://www.php.net/manual/es/ds-map.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 2226ad08f
order: 15120
---

Ds\Map::sort

Ordena el mapa en el lugar por valor

## Descripción

```php
public Ds\Map::sort([callable $comparator]): void
```php

Ordena el mapa en el lugar por valor, utilizando una función `comparator` opcional.

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

Ejemplo de `Ds\Map::sort`

```php
<?php
$map = new \Ds\Map(["a" => 2, "b" => 3, "c" => 1]);
$map->sort();

print_r($map);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => c
                [value] => 1
            )

        [1] => Ds\Pair Object
            (
                [key] => a
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => b
                [value] => 3
            )

    )

Ejemplo de `Ds\Map::sort` utilizando un comparador

```php
<?php
$map = new \Ds\Map(["a" => 2, "b" => 3, "c" => 1]);

$map->sort(function($a, $b) {
    return $b <=> $a;
});

print_r($map);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => b
                [value] => 3
            )

        [1] => Ds\Pair Object
            (
                [key] => a
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 1
            )

    )
