---
title: ReflectionClass::hasMethod
description: Verifica si un método está definido
source_url: https://www.php.net/manual/es/reflectionclass.hasmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/hasmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69380
---

ReflectionClass::hasMethod

Verifica si un método está definido

## Descripción

```php
public ReflectionClass::hasMethod(string $name): bool
```php

Verifica si un método específico está definido en una clase.

## Parámetros

`name`  
Nombre del método a verificar.

## Valores devueltos

`true` si el método está definido, `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::hasMethod

```
<?php
Class C {
    public function publicFoo() {
        return true;
    }

    protected function protectedFoo() {
        return true;
    }

    private function privateFoo() {
        return true;
    }

    static function staticFoo() {
        return true;
    }
}

$rc = new ReflectionClass("C");

var_dump($rc->hasMethod('publicFoo'));

var_dump($rc->hasMethod('protectedFoo'));

var_dump($rc->hasMethod('privateFoo'));

var_dump($rc->hasMethod('staticFoo'));

// C no debería tener el método bar
var_dump($rc->hasMethod('bar'));

// Los nombres de los métodos no son sensibles a mayúsculas/minúsculas
var_dump($rc->hasMethod('PUBLICfOO'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(true)
    bool(true)
    bool(true)
    bool(false)
    bool(true)

## Véase también

ReflectionClass::hasConstant, ReflectionClass::hasProperty
