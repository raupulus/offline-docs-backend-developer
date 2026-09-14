---
title: ReflectionProperty::hasDefaultValue
description: Verifica si la propiedad tiene un valor por omisión
source_url: https://www.php.net/manual/es/reflectionproperty.hasdefaultvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/hasdefaultvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71580
---

ReflectionProperty::hasDefaultValue

Verifica si la propiedad tiene un valor por omisión

## Descripción

```php
public ReflectionProperty::hasDefaultValue(): bool
```php

Verifica si la propiedad ha sido declarada con un valor por omisión, incluyendo un valor por omisión implícito `null`. Retorna `false` para las propiedades tipadas sin valor por omisión (o las propiedades dinámicas).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Si la propiedad tiene un valor por omisión (incluyendo `null`), `true` es retornado; si la propiedad es tipada sin valor por omisión declarado o es una propiedad dinámica, `false` es retornado.

## Ejemplos

Ejemplo de ReflectionProperty::hasDefaultValue

```
<?php
class Foo {
    public $bar;
    public ?int $baz;
    public ?int $foo = null;
    public int $boing;

    public function __construct()
    {
        $this->ping = '';
    }
}

$ro = new ReflectionObject(new Foo());
var_dump($ro->getProperty('bar')->hasDefaultValue());
var_dump($ro->getProperty('baz')->hasDefaultValue());
var_dump($ro->getProperty('foo')->hasDefaultValue());
var_dump($ro->getProperty('boing')->hasDefaultValue());
var_dump($ro->getProperty('ping')->hasDefaultValue()); // Propiedad dinámica
var_dump($ro->getProperty('pong')->hasDefaultValue()); // Propiedad no definida
?>

 
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(true)
    bool(false)
    bool(false)

    Fatal error: Uncaught ReflectionException: Property Foo::$pong does not exist in example.php

## Véase también

ReflectionProperty::getDefaultValue
