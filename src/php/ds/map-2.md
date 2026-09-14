---
title: Ds\Map::map
description: Devuelve el resultado de la aplicación de una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-map.map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15010
---

Ds\Map::map

Devuelve el resultado de la aplicación de una retrollamada a cada valor

## Descripción

```php
public Ds\Map::map(callable $callback): Ds\Map
```php

Devuelve el resultado de la aplicación de un `callback` a cada valor del mapa.

## Parámetros

`callback`  
```php
callback(mixed $key, mixed $value): mixed
```

Un `callable` a aplicar a cada valor del mapa.

La retrollamada debe devolver aquello a lo que la clave será mappada en el mapa resultante.

## Valores devueltos

El resultado de la aplicación de un `callback` a cada valor del mapa.

> [!NOTE]
> Las claves y los valores de la instancia actual no serán afectados.

## Ejemplos

Ejemplo de `Ds\Map::map`

```php
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

print_r($map->map(function($key, $value) { return $value * 2; }));
print_r($map);
?>

   
```

Resultado del ejemplo anterior es similar a:

    (
        [0] => Ds\Pair Object
            (
                [key] => a
                [value] => 2
            )

        [1] => Ds\Pair Object
            (
                [key] => b
                [value] => 4
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 6
            )

    )
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
