---
title: Ds\Map::putAll
description: Asocia todas las parejas clave-valor de un objeto traversable o de un
  array
source_url: https://www.php.net/manual/es/ds-map.putall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/putAll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15050
---

Ds\Map::putAll

Asocia todas las parejas clave-valor de un objeto traversable o de un array

## Descripción

```php
public Ds\Map::putAll(mixed $pairs): void
```php

Asocia todas las `pairs` clave-valor de un objeto `traversable` o de un `array`.

> [!NOTE]
> Las claves de tipo `object` son soportadas. Si un objeto implementa `Ds\Hashable`, la igualdad será determinada por la función `equals` del objeto. Si un objeto no implementa `Ds\Hashable`, los objetos deben ser referencias a la misma instancia para ser considerados iguales.

## Parámetros

`pairs`  
Un objeto `traversable` o `array`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Map::putAll`

```
<?php
$map = new \Ds\Map();

$map->putAll([
    "a" => 1,
    "b" => 2,
    "c" => 3,
]);

print_r($map);
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
