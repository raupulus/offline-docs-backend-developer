---
title: Ds\Map::reversed
description: Devuelve una copia invertida
source_url: https://www.php.net/manual/es/ds-map.reversed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/reversed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15090
---

Ds\Map::reversed

Devuelve una copia invertida

## Descripción

```php
public Ds\Map::reversed(): Ds\Map
```php

Devuelve una copia invertida del mapa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia invertida del mapa.

> [!NOTE]
> La instancia actual no se ve afectada.

## Ejemplos

Ejemplo de `Ds\Map::reversed`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

print_r($map->reversed());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => c
                [value] => 3
            )

        [1] => Ds\Pair Object
            (
                [key] => b
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => a
                [value] => 1
            )

    )
