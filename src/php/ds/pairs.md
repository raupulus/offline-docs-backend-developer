---
title: Ds\Map::pairs
description: Devuelve una secuencia que contiene todas las parejas del mapa
source_url: https://www.php.net/manual/es/ds-map.pairs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/pairs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 15030
---

Ds\Map::pairs

Devuelve una secuencia que contiene todas las parejas del mapa

## Descripción

```php
public Ds\Map::pairs(): Ds\Sequence
```php

Devuelve una `Ds\Sequence` que contiene todas las parejas del mapa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`Ds\Sequence` que contiene todas las parejas del mapa.

## Ejemplos

Ejemplo de `Ds\Map::pairs`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

var_dump($map->pairs());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#8 (3) {
      [0]=>
      object(Ds\Pair)#5 (2) {
        ["key"]=>
        string(1) "a"
        ["value"]=>
        int(1)
      }
      [1]=>
      object(Ds\Pair)#6 (2) {
        ["key"]=>
        string(1) "b"
        ["value"]=>
        int(2)
      }
      [2]=>
      object(Ds\Pair)#7 (2) {
        ["key"]=>
        string(1) "c"
        ["value"]=>
        int(3)
      }
    }
