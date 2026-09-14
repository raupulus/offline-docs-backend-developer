---
title: ReflectionProperty::isDynamic
description: Verifica si la propiedad es una propiedad dinámica
source_url: https://www.php.net/manual/es/reflectionproperty.isdynamic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isdynamic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 969db61a5
order: 71640
---

ReflectionProperty::isDynamic

Verifica si la propiedad es una propiedad dinámica

## Descripción

```php
public ReflectionProperty::isDynamic(): bool
```php

Verifica si la propiedad ha sido declarada en tiempo de ejecución, o si la propiedad ha sido declarada en tiempo de compilación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la propiedad ha sido declarada en tiempo de ejecución, o `false` si ha sido creada en tiempo de compilación.

## Ejemplos

Ejemplo de ReflectionProperty::isDynamic

```
<?php

#[\AllowDynamicProperties]
class Foo {
    public $bar;
}

$o = new Foo();
$o->bar = 42;
$o->baz = 42;

$ro = new ReflectionObject($o);
var_dump($ro->getProperty('bar')->isDynamic());
var_dump($ro->getProperty('baz')->isDynamic());
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionProperty::getValue
