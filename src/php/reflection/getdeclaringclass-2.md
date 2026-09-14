---
title: ReflectionMethod::getDeclaringClass
description: Obtiene la declaración de la clase del método reflejado
source_url: https://www.php.net/manual/es/reflectionmethod.getdeclaringclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/getdeclaringclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70960
---

ReflectionMethod::getDeclaringClass

Obtiene la declaración de la clase del método reflejado

## Descripción

```php
public ReflectionMethod::getDeclaringClass(): ReflectionClass
```php

Obtiene la declaración de la clase del método reflejado

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionClass` que representa la clase a la que pertenece el método reflejado.

## Ejemplos

Ejemplo para ReflectionMethod::getDeclaringClass

```
<?php
class HelloWorld {

    protected function sayHelloTo($name) {
        return 'Hello ' . $name;
    }

}

$reflectionMethod = new ReflectionMethod(new HelloWorld(), 'sayHelloTo');
var_dump($reflectionMethod->getDeclaringClass());
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionClass)#2 (1) {
      ["name"]=>
      string(10) "HelloWorld"
    }

## Véase también

ReflectionMethod::isAbstract
