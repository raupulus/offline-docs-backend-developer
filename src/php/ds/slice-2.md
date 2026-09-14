---
title: Ds\Map::slice
description: Devuelve un subconjunto del mapa definido por un índice de inicio y una
  longitud
source_url: https://www.php.net/manual/es/ds-map.slice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/slice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15110
---

Ds\Map::slice

Devuelve un subconjunto del mapa definido por un índice de inicio y una longitud

## Descripción

```php
public Ds\Map::slice(int $index, [int $length]): Ds\Map
```php

Devuelve un subconjunto del mapa definido por un `index` de inicio y una longitud `length`.

## Parámetros

`index`  
El índice desde el cual comienza el rango.

Si es positivo, el rango comenzará en este índice en el mapa. Si es negativo, el rango comenzará a esta distancia del final.

`length`  
Si se da una longitud y es positiva, el mapa resultante tendrá hasta tantas parejas. Si se da una longitud y es negativa, el rango terminará a tantas parejas del final. Si la longitud provoca un desbordamiento, solo las parejas hasta el final del mapa serán incluidas. Si no se proporciona una longitud, el mapa resultante contendrá todas las parejas entre el índice y el final del mapa.

## Valores devueltos

Un subconjunto del mapa definido por un índice de inicio y una longitud.

## Ejemplos

Ejemplo de `Ds\Map::slice`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3, "d" => 4, "e" => 5]);

// Slice desde 2 en adelante
print_r($map->slice(2)->toArray());

// Slice desde 1, con una longitud de 3
print_r($map->slice(1, 3)->toArray());

// Slice desde 1 en adelante
print_r($map->slice(1)->toArray());

// Slice desde 2 desde el final en adelante
print_r($map->slice(-2)->toArray());

// Slice desde 1 hasta 1 desde el final
print_r($map->slice(1, -1)->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [c] => 3
        [d] => 4
        [e] => 5
    )
    Array
    (
        [b] => 2
        [c] => 3
        [d] => 4
    )
    Array
    (
        [b] => 2
        [c] => 3
        [d] => 4
        [e] => 5
    )
    Array
    (
        [d] => 4
        [e] => 5
    )
    Array
    (
        [b] => 2
        [c] => 3
        [d] => 4
    )
