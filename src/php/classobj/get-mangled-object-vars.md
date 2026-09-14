---
title: get_mangled_object_vars
description: Devuelve un array de propiedades del objeto manipulado
source_url: https://www.php.net/manual/es/function.get-mangled-object-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-mangled-object-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_reviewed: false
translation_revision: d332b5ae7
order: 6840
---

get_mangled_object_vars

Devuelve un array de propiedades del objeto manipulado

## Descripción

```php
get_mangled_object_vars(object $object): array
```php

Devuelve un `array` cuyos elementos son las propiedades del `object`. Las claves son los nombres de las variables miembro, con algunas excepciones notables: las variables privadas tienen el nombre de la clase precedido del nombre de la variable, y las variables protegidas están precedidas de un `*`. Estos valores precedidos tienen bytes `NUL` a ambos lados. Las [propiedades tipadas](#language.oop5.properties.typed-properties) no inicializadas son rechazadas silenciosamente.

## Parámetros

`object`  
Una instancia de objeto.

## Valores devueltos

Devuelve un `array` que contiene todas las propiedades de `object`, independientemente de su visibilidad.

## Ejemplos

Ejemplo de `get_mangled_object_vars`

```
<?php

class A
{
    public $public = 1;

    protected $protected = 2;

    private $private = 3;
}

class B extends A
{
    private $private = 4;
}

$object = new B;
$object->dynamic = 5;
$object->{'6'} = 6;

var_dump(get_mangled_object_vars($object));

class AO extends ArrayObject
{
    private $private = 1;
}

$arrayObject = new AO(['x' => 'y']);
$arrayObject->dynamic = 2;

var_dump(get_mangled_object_vars($arrayObject));

    
```php

El ejemplo anterior mostrará:

    array(6) {
      ["Bprivate"]=>
      int(4)
      ["public"]=>
      int(1)
      ["*protected"]=>
      int(2)
      ["Aprivate"]=>
      int(3)
      ["dynamic"]=>
      int(5)
      [6]=>
      int(6)
    }
    array(2) {
      ["AOprivate"]=>
      int(1)
      ["dynamic"]=>
      int(2)
    }

## Véase también

`get_class_vars`, `get_object_vars`
