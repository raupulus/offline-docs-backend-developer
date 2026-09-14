---
title: Ds\Map::filter
description: Crear un nuevo mapa utilizando un callable para determinar qué pares
  incluir
source_url: https://www.php.net/manual/es/ds-map.filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14890
---

Ds\Map::filter

Crear un nuevo mapa utilizando un

callable

para determinar qué pares incluir

## Descripción

```php
public Ds\Map::filter([callable $callback]): Ds\Map
```php

Crear un nuevo mapa utilizando un `callable` para determinar qué pares incluir.

## Parámetros

`callback`  
```php
callback(mixed $key, mixed $value): bool
```

Un `callable` opcional que devuelve `true` si el par debe ser incluido, `false` en caso contrario.

Si no se proporciona ninguna función de retrollamada, solo se incluirán los valores que sean `true` (ver [conversión en booléen](#language.types.boolean.casting)).

## Valores devueltos

Un nuevo mapa que contiene todos los pares para los cuales el `callback` ha devuelto `true`, o todas las claves que se convierten en `true` si no se proporciona un `callback`.

## Ejemplos

Ejemplo de `Ds\Map::filter` utilizando una función de retrollamada

```php
<?php
$map = new \Ds\Map(["a", "b", "c", "d", "e"]);

var_dump($map->filter(function($key, $value) {
    return $key % 2 == 0;
}));
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Map)#3 (3) {
      [0]=>
      object(Ds\Pair)#2 (2) {
        ["key"]=>
        int(0)
        ["value"]=>
        string(1) "a"
      }
      [1]=>
      object(Ds\Pair)#4 (2) {
        ["key"]=>
        int(2)
        ["value"]=>
        string(1) "c"
      }
      [2]=>
      object(Ds\Pair)#5 (2) {
        ["key"]=>
        int(4)
        ["value"]=>
        string(1) "e"
      }
    }

Ejemplo de `Ds\Map::filter` sin función de retrollamada

```php
<?php
$map = new \Ds\Map(["a" => 0, "b" => 1, "c" => true, "d" => false]);

var_dump($map->filter());
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Map)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      string(1) "a"
      [2]=>
      bool(true)
    }
