---
title: ReflectionMethod::hasPrototype
description: Indica si el método tiene un prototipo
source_url: https://www.php.net/manual/es/reflectionmethod.hasprototype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/hasprototype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70990
---

ReflectionMethod::hasPrototype

Indica si el método tiene un prototipo

## Descripción

```php
public ReflectionMethod::hasPrototype(): bool
```php

Indica si el método tiene un prototipo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el método tiene un prototipo, de lo contrario `false`.

## Ejemplos

Ejemplo con ReflectionMethod::hasPrototype

```
<?php

class Hello
{
    public function sayHelloTo($name)
    {
        return 'Hello '.$name;
    }
}

class HelloWorld extends Hello
{
    public function sayHelloTo($name)
    {
        return 'Hello world: '.$name;
    }
}
$reflectionMethod = new ReflectionMethod('HelloWorld', 'sayHelloTo');
var_dump($reflectionMethod->hasPrototype());
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

ReflectionMethod::getPrototype
