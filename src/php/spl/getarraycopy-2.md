---
title: ArrayObject::getArrayCopy
description: Crea una copia del objeto ArrayObject
source_url: https://www.php.net/manual/es/arrayobject.getarraycopy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/getarraycopy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81400
---

ArrayObject::getArrayCopy

Crea una copia del objeto

ArrayObject

## Descripción

```php
public ArrayObject::getArrayCopy(): array
```php

Exporta el objeto `ArrayObject` a un array.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una copia del `array`. Cuando el objeto `ArrayObject` es un objeto, el array devuelto contiene las propiedades de dicho objeto.

## Ejemplos

Ejemplo con `ArrayObject::getArrayCopy`

```
<?php
// Lista de frutas
$fruits = array("limones" => 1, "naranjas" => 4, "plátanos" => 5, "manzanas" => 10);

$fruitsArrayObject = new ArrayObject($fruits);
$fruitsArrayObject['peras'] = 4;

// Crea una copia de los arrays
$copy = $fruitsArrayObject->getArrayCopy();
var_dump($copy);

?>

    
```php

El ejemplo anterior mostrará:

    array(5) {
      ["limones"]=>
      int(1)
      ["naranjas"]=>
      int(4)
      ["plátanos"]=>
      int(5)
      ["manzanas"]=>
      int(10)
      ["peras"]=>
      int(4)
    }
