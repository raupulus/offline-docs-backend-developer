---
title: Ds\Map::union
description: Crear un nuevo mapa utilizando los valores de la instancia actual y de
  otro mapa
source_url: https://www.php.net/manual/es/ds-map.union.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/union.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 15160
---

Ds\Map::union

Crear un nuevo mapa utilizando los valores de la instancia actual y de otro mapa

## Descripción

```php
public Ds\Map::union(Ds\Map $map): Ds\Map
```php

Crear un nuevo mapa que contiene los pares de la instancia actual así como los pares de otro `map`.

`A ∪ B = {x: x ∈ A ∨ x ∈ B}`

> [!NOTE]
> Los valores de la instancia actual serán sobrescritos por aquellos proporcionados cuando las claves sean iguales.

## Parámetros

`map`  
El otro mapa, a combinar con la instancia actual.

## Valores devueltos

Un nuevo mapa que contiene todos los pares de la instancia actual así como de otro `map`.

## Véase también

[Unión](https://en.wikipedia.org/wiki/Union_(set_theory)) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Map::union`

```
<?php
$a = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$b = new \Ds\Map(["b" => 3, "c" => 4, "d" => 5]);

print_r($a->union($b));
?>

   
```php

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
                [value] => 3
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 4
            )

        [3] => Ds\Pair Object
            (
                [key] => d
                [value] => 5
            )

    )
