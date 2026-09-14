---
title: Ds\Map::isEmpty
description: Indica si el mapa está vacío
source_url: https://www.php.net/manual/es/ds-map.isempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/isempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e924f5b8
order: 14950
---

Ds\Map::isEmpty

Indica si el mapa está vacío

## Descripción

```php
public Ds\Map::isEmpty(): bool
```php

Indica si el mapa está vacío.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el mapa está vacío, de lo contrario `false`.

## Ejemplos

Ejemplo de `Ds\Map::isEmpty`

```
<?php
$a = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
$b = new \Ds\Map();

var_dump($a->isEmpty());
var_dump($b->isEmpty());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
