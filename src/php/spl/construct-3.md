---
title: ArrayObject::__construct
description: Construye un nuevo objeto array
source_url: https://www.php.net/manual/es/arrayobject.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 81370
---

ArrayObject::\_\_construct

Construye un nuevo objeto array

## Descripción

```php
public ArrayObject::__construct([array $array], [int $flags], [string $iteratorClass])
```php

Construye un nuevo objeto array.

## Parámetros

`array`  
El parámetro `array` acepta un `array` o un `object`.

`flags`  
Opción de control del comportamiento del objeto `ArrayObject`. Ver el método ArrayObject::setFlags.

`iteratorClass`  
Especifica la clase que será utilizada para las iteraciones del objeto `ArrayObject`. La clase debe ser un subtipo de la clase `ArrayIterator`.

## Ejemplos

Ejemplo con `ArrayObject::__construct`

```
<?php

$array = [
    '1' => 'one',
    '2' => 'two',
    '3' => 'three'
     ];

$arrayobject = new ArrayObject($array);

var_dump($arrayobject);

?>

   
```php

El ejemplo anterior mostrará:

    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(3) {
        [1]=>
        string(3) "one"
        [2]=>
        string(3) "two"
        [3]=>
        string(5) "three"
      }
    }

## Véase también

ArrayObject::setflags
