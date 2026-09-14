---
title: Ds\Map::hasKey
description: Determina si el mapa contiene una clave dada
source_url: https://www.php.net/manual/es/ds-map.haskey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/haskey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 14920
---

Ds\Map::hasKey

Determina si el mapa contiene una clave dada

## Descripción

```php
public Ds\Map::hasKey(mixed $key): bool
```php

Determina si el mapa contiene una clave dada.

## Parámetros

`key`  
La clave a buscar.

## Valores devueltos

Devuelve `true` si la clave ha sido encontrada, de lo contrario `false`.

## Ejemplos

`Ds\Map::hasKey` example

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

var_dump($map->hasKey("a")); // true
var_dump($map->hasKey("e")); // false
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)
