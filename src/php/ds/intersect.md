---
title: Ds\Map::intersect
description: Crear un nuevo mapa intersectando las claves con otro mapa
source_url: https://www.php.net/manual/es/ds-map.intersect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/intersect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 14940
---

Ds\Map::intersect

Crear un nuevo mapa intersectando las claves con otro mapa

## Descripción

```php
public Ds\Map::intersect(Ds\Map $map): Ds\Map
```php

Crear un nuevo mapa que contiene las parejas de la instancia actual cuyas claves están también presentes en el `map` dado. En otras palabras, devuelve una copia de la instancia actual con todas las claves eliminadas que no están también en el otro `map`.

`A ∩ B = {x : x ∈ A ∧ x ∈ B}`

> [!NOTE]
> Los valores de la instancia actual serán conservados.

## Parámetros

`map`  
El otro mapa, que contiene las claves a intersectar.

## Valores devueltos

La intersección de las claves de la instancia actual y de otro `map`.

## Véase también

[Intersección](https://en.wikipedia.org/wiki/Intersection_(set_theory)) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Map::intersect`

```
<?php
$a = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$b = new \Ds\Map(["b" => 4, "c" => 5, "d" => 6]);

var_dump($a->intersect($b));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Map)#3 (2) {
      [0]=>
      object(Ds\Pair)#4 (2) {
        ["key"]=>
        string(1) "b"
        ["value"]=>
        int(2)
      }
      [1]=>
      object(Ds\Pair)#5 (2) {
        ["key"]=>
        string(1) "c"
        ["value"]=>
        int(3)
      }
    }
