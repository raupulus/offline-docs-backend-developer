---
title: Ds\Map::sum
description: Devuelve la suma de todos los valores del mapa
source_url: https://www.php.net/manual/es/ds-map.sum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/sum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: eb0bd932e
order: 15140
---

Ds\Map::sum

Devuelve la suma de todos los valores del mapa

## Descripción

```php
public Ds\Map::sum(): int
```php

Devuelve la suma de todos los valores del mapa.

> [!NOTE]
> Los arrays y los objetos se consideran iguales a cero en el cálculo de la suma.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La suma de todos los valores del mapa como `float` o `int` dependiendo de los valores del mapa.

## Ejemplos

Ejemplo de `Ds\Map::sum` con enteros

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
var_dump($map->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(6)

Ejemplo de `Ds\Map::sum` con números de punto flotante

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2.5, "c" => 3]);
var_dump($map->sum());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    float(6.5)
