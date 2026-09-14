---
title: Ds\Map::first
description: Devuelve la primera pareja del mapa
source_url: https://www.php.net/manual/es/ds-map.first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14900
---

Ds\Map::first

Devuelve la primera pareja del mapa

## Descripción

```php
public Ds\Map::first(): Ds\Pair
```php

Devuelve la primera pareja del mapa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La primera pareja del mapa.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Map::first`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
var_dump($map->first());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Pair)#2 (2) {
      ["key"]=>
      string(1) "a"
      ["value"]=>
      int(1)
    }
