---
title: Ds\Map::apply
description: Actualiza todos los valores aplicando una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-map.apply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/apply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14820
---

Ds\Map::apply

Actualiza todos los valores aplicando una retrollamada a cada valor

## Descripción

```php
public Ds\Map::apply(callable $callback): void
```php

Actualiza todos los valores aplicando una `callback` a cada valor del mapa.

## Parámetros

`callback`  
```php
callback(mixed $key, mixed $value): mixed
```

Un `callable` a aplicar a cada valor del mapa.

La retrollamada debe devolver lo que el valor debe ser reemplazado por.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Map::apply`

```php
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$map->apply(function($key, $value) { return $value * 2; });

print_r($map);
?>

   
```

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
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
