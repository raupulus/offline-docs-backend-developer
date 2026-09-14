---
title: property_exists
description: Verifica si un objeto o una clase posee una propiedad
source_url: https://www.php.net/manual/es/function.property-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/property-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: a4fb7f593
order: 6910
---

property_exists

Verifica si un objeto o una clase posee una propiedad

## Descripción

```php
property_exists(object $object_or_class, string $property): bool
```php

Esta función verifica si la propiedad `property` existe en la clase especificada.

> [!NOTE]
> `property_exists` devuelve `true` incluso si la propiedad tiene un valor `null`, a diferencia de la función `isset`.

## Parámetros

`object_or_class`  
El nombre de la clase o un objeto de la clase a probar

`property`  
El nombre de la propiedad

## Valores devueltos

Devuelve `true` si la propiedad existe, `false` si no existe.

## Ejemplos

Ejemplo con `property_exists`

```
<?php

class myClass {
    public $mine;
    private $xpto;
    static protected $test;

    static function test() {
        var_dump(property_exists('myClass', 'xpto')); //true
    }
}

var_dump(property_exists('myClass', 'mine'));   //true
var_dump(property_exists(new myClass, 'mine')); //true
var_dump(property_exists('myClass', 'xpto'));   //true
var_dump(property_exists('myClass', 'bar'));    //false
var_dump(property_exists('myClass', 'test'));   //true
myClass::test();

?>

    
```php

## Notas

> [!NOTE]
> El uso de esta función utilizará todos los [autoloaders](#language.oop5.autoload) registrados si la clase no es conocida aún.

> [!NOTE]
> La función `property_exists` no puede detectar las propiedades que son accesibles utilizando el método mágico [`__get`](#language.oop5.overloading.members).

## Véase también

`method_exists`
