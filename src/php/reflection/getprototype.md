---
title: ReflectionMethod::getPrototype
description: Obtiene el prototipo del método (si existe)
source_url: https://www.php.net/manual/es/reflectionmethod.getprototype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/getprototype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70980
---

ReflectionMethod::getPrototype

Obtiene el prototipo del método (si existe)

## Descripción

```php
public ReflectionMethod::getPrototype(): ReflectionMethod
```php

Devuelve el prototipo del método.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionMethod` instancia del método.

## Errores/Excepciones

Se lanzará una excepción `ReflectionException` si el método no posee un prototipo.

## Ejemplos

Ejemplo con ReflectionMethod::getPrototype

```
<?php
class Hello {

    public function sayHelloTo($name) {
        return 'Hello ' . $name;
    }

}
class HelloWorld extends Hello {

    public function sayHelloTo($name) {
        return 'Hello world: ' . $name;
    }

}

$reflectionMethod = new ReflectionMethod('HelloWorld', 'sayHelloTo');
var_dump($reflectionMethod->getPrototype());
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionMethod)#2 (2) {
      ["name"]=>
      string(10) "sayHelloTo"
      ["class"]=>
      string(5) "Hello"
    }

## Véase también

ReflectionMethod::getModifiers, ReflectionMethod::hasPrototype
