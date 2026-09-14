---
title: Ds\Map::diff
description: Crear un nuevo map utilizando claves que no están en otro map
source_url: https://www.php.net/manual/es/ds-map.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 14880
---

Ds\Map::diff

Crear un nuevo map utilizando claves que no están en otro map

## Descripción

```php
public Ds\Map::diff(Ds\Map $map): Ds\Map
```php

Devuelve el resultado de la eliminación de todas las claves de la instancia actual que están presentes en un `map` dado.

`A \ B = {x ∈ A | x ∉ B}`

## Parámetros

`map`  
El map que contiene las claves a excluir del map resultante.

## Valores devueltos

El resultado de la eliminación de todas las claves de la instancia actual que están presentes en un `map` dado.

## Véase también

[Complemento](https://en.wikipedia.org/wiki/Complement_(set_theory)) en Wikipedia

## Ejemplos

Ejemplo de `Ds\Map::diff`

```
<?php
$a = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$b = new \Ds\Map(["b" => 4, "c" => 5, "d" => 6]);

var_dump($a->diff($b));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Map)#3 (1) {
      [0]=>
      object(Ds\Pair)#4 (2) {
        ["key"]=>
        string(1) "a"
        ["value"]=>
        int(1)
      }
    }
