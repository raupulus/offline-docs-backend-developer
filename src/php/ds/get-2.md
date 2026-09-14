---
title: Ds\Map::get
description: Devuelve el valor para una clave dada
source_url: https://www.php.net/manual/es/ds-map.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 14910
---

Ds\Map::get

Devuelve el valor para una clave dada

## Descripción

```php
public Ds\Map::get(mixed $key, [mixed $default]): mixed
```php

Devuelve el valor para una clave dada, o un valor por defecto opcional si la clave no ha podido ser encontrada.

> [!NOTE]
> Las claves de tipo `object` son soportadas. Si un objeto implementa `Ds\Hashable`, la igualdad será determinada por la función `equals` del objeto. Si un objeto no implementa `Ds\Hashable`, los objetos deben ser referencias a la misma instancia para ser considerados iguales.

> [!NOTE]
> Asimismo, se puede utilizar la sintaxis de array para acceder a los valores por clave, por ejemplo `$map["clé"]`.

> [!CAUTION]
> Atención al uso de la sintaxis de array. Las claves escalares serán coercionadas a enteros por el motor. Por ejemplo, `$map["1"]` intentará acceder a `int(1)`, mientras que `$map->get("1")` buscará correctamente la clave de string.
>
> Ver [array](#language.types.array).

## Parámetros

`key`  
La clave a buscar.

`default`  
El valor por defecto opcional, devuelto si la clave no ha podido ser encontrada.

## Valores devueltos

El valor mapeado a la `clave` dada, o el `valor por defecto` si se proporciona y la clave no ha podido ser encontrada en el mapa.

## Errores/Excepciones

`OutOfBoundsException` si la clave no ha podido ser encontrada y ningún valor por defecto ha sido proporcionado.

## Ejemplos

Ejemplo de `Ds\Map::get`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

var_dump($map->get("a"));       // 1
var_dump($map->get("d", 10));   // 10 (usar por defecto)
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1)
    int(10)

Ejemplo de `Ds\Map::get` utilizando la sintaxis de array

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

var_dump($map["a"]); // 1
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1)
