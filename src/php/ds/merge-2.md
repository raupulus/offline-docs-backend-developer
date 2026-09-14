---
title: Ds\Map::merge
description: Devuelve el resultado de la adición de todas las asociaciones dadas
source_url: https://www.php.net/manual/es/ds-map.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15020
---

Ds\Map::merge

Devuelve el resultado de la adición de todas las asociaciones dadas

## Descripción

```php
public Ds\Map::merge(mixed $values): Ds\Map
```php

Devuelve el resultado de la adición de todas las asociaciones de un objeto `traversable` dado o de un `array` con sus valores correspondientes, combinados con la instancia actual.

> [!NOTE]
> Los valores de la instancia actual serán sobrescritos por los proporcionados cuando las claves sean iguales.

## Parámetros

`values`  
Un objeto `traversable` o un `array`.

## Valores devueltos

El resultado de la asociación de todas las claves de un objeto `traversable` dado o de un `array` con sus valores correspondientes, combinados con la instancia actual.

> [!NOTE]
> La instancia actual no será afectada.

## Ejemplos

Ejemplo de `Ds\Map::merge`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

print_r($map->merge(["a" => 10, "e" => 50]));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => a
                [value] => 10
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

        [3] => Ds\Pair Object
            (
                [key] => e
                [value] => 50
            )

    )
