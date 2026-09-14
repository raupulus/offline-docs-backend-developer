---
title: ReflectionMethod::__toString
description: Devuelve una representación textual del método
source_url: https://www.php.net/manual/es/reflectionmethod.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71100
---

ReflectionMethod::\_\_toString

Devuelve una representación textual del método

## Descripción

```php
public ReflectionMethod::__toString(): string
```php

Obtiene una representación textual del método.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una representación textual de este objeto `ReflectionMethod`.

## Ejemplos

ReflectionMethod::\_\_toString ejemplo

```
<?php
class HelloWorld {

    public function sayHelloTo($name) {
        return 'Hello ' . $name;
    }

}

$reflectionMethod = new ReflectionMethod(new HelloWorld(), 'sayHelloTo');
echo $reflectionMethod;
?>

    
```php

El ejemplo anterior mostrará:

    Method [ <user> método público sayHelloTo ] {
      @@ /var/www/examples/reflection.php 16 - 18

      - Parámetros [1] {
        Parámetro #0 [ <required> $name ]
      }
    }

## Véase también

ReflectionMethod::export, [\_\_toString()](#object.tostring)
