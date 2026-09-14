---
title: Ds\Map::hasValue
description: Determina si el mapa contiene un valor dado
source_url: https://www.php.net/manual/es/ds-map.hasvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/hasvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 14930
---

Ds\Map::hasValue

Determina si el mapa contiene un valor dado

## Descripción

```php
public Ds\Map::hasValue(mixed $value): bool
```php

Determina si el mapa contiene un valor dado.

## Parámetros

`value`  
El valor a buscar.

## Valores devueltos

Devuelve `true` si el valor ha sido encontrado, de lo contrario `false`.

## Ejemplos

Ejemplo de `Ds\Map::hasValue`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

var_dump($map->hasValue(1)); // true
var_dump($map->hasValue(4)); // false
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)
