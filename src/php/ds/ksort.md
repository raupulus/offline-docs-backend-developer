---
title: Ds\Map::ksort
description: Ordena el mapa en el lugar por clave
source_url: https://www.php.net/manual/es/ds-map.ksort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/ksort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 14980
---

Ds\Map::ksort

Ordena el mapa en el lugar por clave

## Descripción

```php
public Ds\Map::ksort([callable $comparator]): void
```php

Ordena el mapa en el lugar por clave, utilizando una función `comparator` opcional.

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

Ejemplo de `Ds\Map::ksort`

```php
<?php
$map = new \Ds\Map(["b" => 2, "c" => 3, "a" => 1]);
$map->ksort();

print_r($map);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => a
                [value] => 1
            )

        [1] => Ds\Pair Object
            (
                [key] => b
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 3
            )

    )

Ejemplo de `Ds\Map::ksort` utilizando un comparador

```php
<?php
$map = new \Ds\Map([1 => "x", 2 => "y", 0 => "z"]);

// Reverse
$map->ksort(function($a, $b) {
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
                [key] => 2
                [value] => y
            )

        [1] => Ds\Pair Object
            (
                [key] => 1
                [value] => x
            )

        [2] => Ds\Pair Object
            (
                [key] => 0
                [value] => z
            )

    )
