---
title: Ds\Map::__construct
description: Crear una nueva instancia
source_url: https://www.php.net/manual/es/ds-map.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 14850
---

Ds\Map::\_\_construct

Crear una nueva instancia

## Descripción

```php
public Ds\Map::__construct(mixed ...$values)
```php

Crear una nueva instancia, utilizando un objeto `traversable` o un `array` para los `values` iniciales.

## Parámetros

`values`  
Un objeto traversable o un `array` a utilizar para los valores iniciales.

## Ejemplos

Ejemplo de `Ds\Map::__construct`

```
<?php
$map = new \Ds\Map();
var_dump($map);

$map = new \Ds\Map(["a" => 1, "b" => 2, "c" => 3]);
var_dump($map);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Map)#1 (0) {
    }
    object(Ds\Map)#2 (3) {
      [0]=>
      object(Ds\Pair)#1 (2) {
        ["key"]=>
        string(1) "a"
        ["value"]=>
        int(1)
      }
      [1]=>
      object(Ds\Pair)#3 (2) {
        ["key"]=>
        string(1) "b"
        ["value"]=>
        int(2)
      }
      [2]=>
      object(Ds\Pair)#4 (2) {
        ["key"]=>
        string(1) "c"
        ["value"]=>
        int(3)
      }
    }
