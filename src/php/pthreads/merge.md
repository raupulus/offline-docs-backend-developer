---
title: Threaded::merge
description: Manipulación
source_url: https://www.php.net/manual/es/threaded.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/threaded/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66830
---

Threaded::merge

Manipulación

## Descripción

```php
public Threaded::merge(mixed $from, [bool $overwrite]): bool
```php

Fusiona los datos en el objeto actual

## Parámetros

`from`  
Los datos a fusionar

`overwrite`  
Sobrescribe las claves existentes; por omisión vale `true`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Fusiona el objeto thread en la tabla de propiedades

```
<?php
$array = [];

while (count($array) < 10)
    $array[] = count($array);

$stdClass = new stdClass();
$stdClass->foo = "foo";
$stdClass->bar = "bar";
$stdClass->baz = "baz";

$safe = new Threaded();
$safe->merge($array);

$safe->foo = "bar";
$safe->merge($stdClass, false);

var_dump($safe);
?>

   
```php

El ejemplo anterior mostrará:

    object(Threaded)#2 (13) {
      ["0"]=>
      int(0)
      ["1"]=>
      int(1)
      ["2"]=>
      int(2)
      ["3"]=>
      int(3)
      ["4"]=>
      int(4)
      ["5"]=>
      int(5)
      ["6"]=>
      int(6)
      ["7"]=>
      int(7)
      ["8"]=>
      int(8)
      ["9"]=>
      int(9)
      ["foo"]=>
      string(3) "bar"
      ["bar"]=>
      string(3) "bar"
      ["baz"]=>
      string(3) "baz"
    }
