---
title: ReflectionProperty::isDefault
description: Verifica si la propiedad es la predeterminada
source_url: https://www.php.net/manual/es/reflectionproperty.isdefault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isdefault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 969db61a5
order: 71630
---

ReflectionProperty::isDefault

Verifica si la propiedad es la predeterminada

## Descripción

```php
public ReflectionProperty::isDefault(): bool
```php

Verifica si la propiedad fue declarada durante la compilación o si la propiedad fue declarada dinámicamente durante la ejecución.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la propiedad fue declarada durante la compilación o `false` si fue declarada durante la ejecución.

## Ejemplos

Ejemplo con ReflectionClass::isDefault

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
var_dump($ro->getProperty('bar')->isDefault());
var_dump($ro->getProperty('baz')->isDefault());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

ReflectionProperty::getValue
