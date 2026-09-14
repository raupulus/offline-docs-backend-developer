---
title: Ds\Map::last
description: Devuelve el último par del mapa
source_url: https://www.php.net/manual/es/ds-map.last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15000
---

Ds\Map::last

Devuelve el último par del mapa

## Descripción

```php
public Ds\Map::last(): Ds\Pair
```php

Devuelve el último par del mapa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el último par del mapa.

## Errores/Excepciones

`UnderflowException` si está vacío.

## Ejemplos

Ejemplo de `Ds\Map::last`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
var_dump($map->last());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Pair)#2 (2) {
      ["key"]=>
      string(1) "c"
      ["value"]=>
      int(3)
    }
