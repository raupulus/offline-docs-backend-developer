---
title: Ds\Set::map
description: Devuelve el resultado de la aplicación de una retrollamada a cada valor
source_url: https://www.php.net/manual/es/ds-set.map.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/map.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 54571648d
order: 15930
---

Ds\Set::map

Devuelve el resultado de la aplicación de una retrollamada a cada valor

## Descripción

```php
public Ds\Set::map(callable $callback): Ds\Set
```php

Devuelve el resultado de la aplicación de una `retrollamada` a cada valor del conjunto.

## Parámetros

`callback`  
La retrollamada a aplicar a cada valor del conjunto debe tener la siguiente firma:

```php
callback(mixed $value): mixed
```

## Valores devueltos

Devuelve un nuevo objeto `Ds\Set` donde cada valor es el resultado de la aplicación de la `retrollamada` a cada valor del conjunto.

## Ejemplos

Ejemplo de Ds\Set::map

```php
<?php
$set = new \Ds\Set([1, 2, 3]);

var_dump($set->map(function($value) { return $value * 2; }));
var_dump($set);
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#3 (3) {
      [0]=>
      int(2)
      [1]=>
      int(4)
      [2]=>
      int(6)
    }
    object(Ds\Set)#1 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
