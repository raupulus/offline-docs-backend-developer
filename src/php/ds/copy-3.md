---
title: Ds\Map::copy
description: Devuelve una copia superficial del mapa
source_url: https://www.php.net/manual/es/ds-map.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14860
---

Ds\Map::copy

Devuelve una copia superficial del mapa

## Descripción

```php
public Ds\Map::copy(): Ds\Map
```php

Devuelve una copia superficial del mapa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia superficial del mapa.

## Ejemplos

Ejemplo de `Ds\Map::copy`

```
<?php
$map = new \Ds\Map([
    "a" => 1,
    "b" => 2,
    "c" => 3,
]);

print_r($map->copy());
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
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 3
            )

    )
