---
title: ReflectionClass::isInstantiable
description: Verifica si una clase es instanciable
source_url: https://www.php.net/manual/es/reflectionclass.isinstantiable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/isinstantiable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 84f256090
order: 69490
---

ReflectionClass::isInstantiable

Verifica si una clase es instanciable

## Descripción

```php
public ReflectionClass::isInstantiable(): bool
```php

Verifica si una clase es instanciable.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la clase es \*\*instanciable\*\* o `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::isInstantiable

```
<?php
class C { }

interface iface {
    function f1();
}

class ifaceImpl implements iface {
    function f1() {}
}

abstract class abstractClass {
    function f1() { }
    abstract function f2();
}

class D extends abstractClass {
    function f2() { }
}

trait T {
    function f1() {}
}

class privateConstructor {
    private function __construct() { }
}

$classes = array(
    "C",
    "iface",
    "ifaceImpl",
    "abstractClass",
    "D",
    "T",
    "privateConstructor",
);

foreach($classes as $class) {
    $reflectionClass = new ReflectionClass($class);
    echo "¿Es la clase $class instanciable? ";
    var_dump($reflectionClass->isInstantiable());
}

?>

    
```php

El ejemplo anterior mostrará:

    ¿Es C instanciable? bool(true)
    ¿Es iface instanciable? bool(false)
    ¿Es ifaceImpl instanciable? bool(true)
    ¿Es abstractClass instanciable? bool(false)
    ¿Es D instanciable? bool(true)
    ¿Es T instanciable? bool(false)
    ¿Es privateConstructor instanciable? bool(false)

## Véase también

ReflectionClass::isInstance
