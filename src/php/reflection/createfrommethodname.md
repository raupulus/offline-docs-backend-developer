---
title: ReflectionMethod::createFromMethodName
description: Crear una nueva ReflectionMethod
source_url: https://www.php.net/manual/es/reflectionmethod.createfrommethodname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/createfrommethodname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 5b5736079
order: 70930
---

ReflectionMethod::createFromMethodName

Crear una nueva ReflectionMethod

## Descripción

```php
public static ReflectionMethod::createFromMethodName(string $method): static
```php

Crear una nueva `ReflectionMethod`.

## Parámetros

`method`  
Nombre de la clase y del método delimitados por `::`.

## Valores devueltos

Devuelve una nueva `ReflectionMethod` en caso de éxito.

## Errores/Excepciones

Se lanza una `ReflectionException` si el método dado no existe.

## Ejemplos

Ejemplo con ReflectionMethod::createFromMethodName

```
<?php

class Foo {
    public function bar() {

    }
}

$methodInfo = ReflectionMethod::createFromMethodName("Foo::bar");
var_dump($methodInfo);
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionMethod)#1 (2) {
      ["name"]=>
      string(3) "bar"
      ["class"]=>
      string(3) "Foo"
    }
