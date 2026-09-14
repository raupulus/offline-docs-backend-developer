---
title: ArrayObject::exchangeArray
description: Sustituye un array por otro
source_url: https://www.php.net/manual/es/arrayobject.exchangearray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/exchangearray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81390
---

ArrayObject::exchangeArray

Sustituye un array por otro

## Descripción

```php
public ArrayObject::exchangeArray(array $array): array
```php

Sustituye el `array` actual por otro `array` o un `object`.

## Parámetros

`array`  
El nuevo `array` o `object` a utilizar.

## Valores devueltos

Devuelve el antiguo `array`.

## Ejemplos

Ejemplo con `ArrayObject::exchangeArray`

```
<?php
// Arrays de frutas
$fruits = array("limones" => 1, "naranjas" => 4, "plátanos" => 5, "manzanas" => 10);
// Array de ciudades en Europa
$locations = array('Ámsterdam', 'París', 'Londres');

$fruitsArrayObject = new ArrayObject($fruits);

// Intercambio de frutas por ciudades
$old = $fruitsArrayObject->exchangeArray($locations);
var_dump($old);
var_dump($fruitsArrayObject);

?>

    
```php

El ejemplo anterior mostrará:

    array(4) {
      ["limones"]=>
      int(1)
      ["naranjas"]=>
      int(4)
      ["plátanos"]=>
      int(5)
      ["manzanas"]=>
      int(10)
    }
    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(3) {
        [0]=>
        string(9) "Ámsterdam"
        [1]=>
        string(5) "París"
        [2]=>
        string(7) "Londres"
      }
    }
