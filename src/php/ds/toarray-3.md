---
title: Ds\Map::toArray
description: Convierte el mapa en un array
source_url: https://www.php.net/manual/es/ds-map.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 15150
---

Ds\Map::toArray

Convierte el mapa en un

array

## Descripción

```php
public Ds\Map::toArray(): array
```php

Convierte el mapa en un `array`.

> [!CAUTION]
> Los mapas con claves no escalares no pueden ser convertidos en `array`.

> [!CAUTION]
> Un `array` tratará todas las claves numéricas como enteros, por ejemplo `"1"` y `1` como claves en el mapa resultará solo en `1` siendo incluido en el array.

> [!NOTE]
> La conversión en `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` conteniendo todos los valores en el mismo orden que el mapa.

## Ejemplos

Ejemplo de `Ds\Map::toArray`

```
<?php
$map = new \Ds\Map([
    "a" => 1,
    "b" => 2,
    "c" => 3,
]);

var_dump($map->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["a"]=>
      int(1)
      ["b"]=>
      int(2)
      ["c"]=>
      int(3)
    }
