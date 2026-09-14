---
title: Ds\Map::keys
description: Devuelve un conjunto de las claves del mapa
source_url: https://www.php.net/manual/es/ds-map.keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14970
---

Ds\Map::keys

Devuelve un conjunto de las claves del mapa

## Descripción

```php
public Ds\Map::keys(): Ds\Set
```php

Devuelve un conjunto que contiene todas las claves del mapa, en el mismo orden.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un conjunto `Ds\Set` que contiene todas las claves del mapa.

## Ejemplos

Ejemplo de `Ds\Map::keys`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
var_dump($map->keys());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#2 (3) {
      [0]=>
      string(1) "a"
      [1]=>
      string(1) "b"
      [2]=>
      string(1) "c"
    }
