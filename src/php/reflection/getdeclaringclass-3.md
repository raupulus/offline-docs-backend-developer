---
title: ReflectionParameter::getDeclaringClass
description: Obtiene la clase declarante
source_url: https://www.php.net/manual/es/reflectionparameter.getdeclaringclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/getdeclaringclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71250
---

ReflectionParameter::getDeclaringClass

Obtiene la clase declarante

## Descripción

```php
public ReflectionParameter::getDeclaringClass(): ReflectionClass
```php

Obtiene la clase declarante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionClass` o `null` si se llama sobre una función.

## Ejemplos

Obtención de la clase que declaró el método

```
<?php
class Foo
{
    public function bar(\DateTime $datetime)
    {
    }
}

class Baz extends Foo
{
}

$param = new \ReflectionParameter(['Baz', 'bar'], 0);

var_dump($param->getDeclaringClass());

    
```php

El ejemplo anterior mostrará:

    object(ReflectionClass)#2 (1) {
      ["name"]=>
      string(3) "Foo"
    }

## Véase también

ReflectionParameter::getClass
