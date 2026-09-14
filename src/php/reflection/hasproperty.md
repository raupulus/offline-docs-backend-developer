---
title: ReflectionClass::hasProperty
description: Verifica si una propiedad está definida
source_url: https://www.php.net/manual/es/reflectionclass.hasproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/hasproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69390
---

ReflectionClass::hasProperty

Verifica si una propiedad está definida

## Descripción

```php
public ReflectionClass::hasProperty(string $name): bool
```php

Verifica si la propiedad especificada está definida.

## Parámetros

`name`  
El nombre de la propiedad a verificar.

## Valores devueltos

`true` si la propiedad está definida, `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::hasProperty

```
<?php
class Foo {
    public    $p1;
    protected $p2;
    private   $p3;

}

$obj = new ReflectionObject(new Foo());

var_dump($obj->hasProperty("p1"));
var_dump($obj->hasProperty("p2"));
var_dump($obj->hasProperty("p3"));
var_dump($obj->hasProperty("p4"));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(true)
    bool(false)

## Véase también

ReflectionClass::hasConstant, ReflectionClass::hasMethod
