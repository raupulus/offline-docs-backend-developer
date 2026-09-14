---
title: ReflectionProperty::isPromoted
description: Verifica si la propiedad está promovida
source_url: https://www.php.net/manual/es/reflectionproperty.ispromoted.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/ispromoted.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71700
---

ReflectionProperty::isPromoted

Verifica si la propiedad está promovida

## Descripción

```php
public ReflectionProperty::isPromoted(): bool
```php

Verifica si la propiedad está [promovida](#language.oop5.decon.constructor.promotion)

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la propiedad está promovida, `false` en caso contrario.

## Ejemplos

Ejemplo de ReflectionProperty::isPromoted

```
<?php
class Foo {
    public $baz;

    public function __construct(public $bar) {}
}

$o = new Foo(42);
$o->baz = 42;

$ro = new ReflectionObject($o);
var_dump($ro->getProperty('bar')->isPromoted());
var_dump($ro->getProperty('baz')->isPromoted());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

ReflectionProperty::isDefault, ReflectionProperty::isInitialized, ReflectionProperty::getValue
