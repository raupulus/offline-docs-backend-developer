---
title: Ds\Map::reverse
description: Invierte el mapa en su lugar
source_url: https://www.php.net/manual/es/ds-map.reverse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/reverse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15080
---

Ds\Map::reverse

Invierte el mapa en su lugar

## Descripción

```php
public Ds\Map::reverse(): void
```php

Invierte el mapa en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Map::reverse`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$map->reverse();

print_r($map);
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
