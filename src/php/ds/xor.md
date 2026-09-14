---
title: Ds\Map::xor
description: Crear un nuevo mapa utilizando las claves de la instancia actual o de
  otro mapa, pero no de ambos
source_url: https://www.php.net/manual/es/ds-map.xor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/xor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 15180
---

Ds\Map::xor

Crear un nuevo mapa utilizando las claves de la instancia actual o de otro mapa, pero no de ambos

## Descripción

```php
public Ds\Map::xor(Ds\Map $map): Ds\Map
```php

Crear un nuevo mapa que contiene las claves de la instancia actual así como de otro `map`, pero no de ambos.

`A ⊖ B = {x : x ∈ (A \ B) ∪ (B \ A)}`

## Parámetros

`map`  
El otro mapa.

## Valores devueltos

Un nuevo mapa que contiene las claves de la instancia actual así como de otro `map`, pero no de ambos.

## Véase también

[Diferencia simétrica](https://en.wikipedia.org/wiki/Symmetric_difference) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Map::xor`

```
<?php
$a = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$b = new \Ds\Map(["b" => 4, "c" => 5, "d" => 6]);

print_r($a->xor($b));
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
                [key] => d
                [value] => 6
            )

    )
