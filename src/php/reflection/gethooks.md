---
title: ReflectionProperty::getHooks
description: Devuelve un array de todos los hooks en esta propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.gethooks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/gethooks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: a16ad380e
order: 71510
---

ReflectionProperty::getHooks

Devuelve un array de todos los hooks en esta propiedad

## Descripción

```php
public ReflectionProperty::getHooks(): array
```php

Devuelve una lista de todos los hooks en esta propiedad.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos `ReflectionMethod` indexados por el hook al que corresponden. Por ejemplo, una propiedad con hooks `get` y `set` devolverá un array de 2 elementos con claves de string `get` y `set`, cada una es un objeto `ReflectionMethod`. El orden en que se devuelven es explícitamente indefinido. Si no hay hooks definidos, se devuelve un array vacío.

## Ejemplos

Ejemplo de ReflectionProperty::getHooks

```
<?php
class Example
{
    public string $name { get => "Name here"; }

    public int $count;
}

$rClass = new \ReflectionClass(Example::class);

$rProp = $rClass->getProperty('name');
var_dump($rProp->getHooks());

$rProp = $rClass->getProperty('count');
var_dump($rProp->getHooks());
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["get"]=>
      object(ReflectionMethod)#3 (2) {
        ["name"]=>
        string(10) "$name::get"
        ["class"]=>
        string(7) "Example"
      }
    }
    array(0) {
    }

## Véase también

ReflectionMethod

ReflectionProperty::hasHooks
