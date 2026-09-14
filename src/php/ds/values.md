---
title: Ds\Map::values
description: Devuelve una secuencia de los valores del mapa
source_url: https://www.php.net/manual/es/ds-map.values.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/values.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 0a116512a
order: 15170
---

Ds\Map::values

Devuelve una secuencia de los valores del mapa

## Descripción

```php
public Ds\Map::values(): Ds\Sequence
```php

Devuelve una secuencia que contiene todos los valores del mapa, en el mismo orden.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una `Ds\Sequence` que contiene todos los valores del mapa.

## Ejemplos

Ejemplo de `Ds\Map::values`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
var_dump($map->values());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
