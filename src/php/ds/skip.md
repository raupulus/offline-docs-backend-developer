---
title: Ds\Map::skip
description: Devuelve el par a un índice de posición dado
source_url: https://www.php.net/manual/es/ds-map.skip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/skip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15100
---

Ds\Map::skip

Devuelve el par a un índice de posición dado

## Descripción

```php
public Ds\Map::skip(int $position): Ds\Pair
```php

Devuelve el par a un índice dado basado en cero `position`.

## Parámetros

`position`  
El índice de posición basado en cero a devolver.

## Valores devueltos

Devuelve el `Ds\Pair` a la `position` dada.

## Errores/Excepciones

`OutOfRangeException` si la posición no es válida.

## Ejemplos

Ejemplo de `Ds\Map::skip`

```
<?php
$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);

var_dump($map->skip(1));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Pair)#2 (2) {
      ["key"]=>
      string(1) "b"
      ["value"]=>
      int(2)
    }
