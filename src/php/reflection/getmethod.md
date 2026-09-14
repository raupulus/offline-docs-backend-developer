---
title: ReflectionClass::getMethod
description: Obtiene un ReflectionMethod para un método de clase
source_url: https://www.php.net/manual/es/reflectionclass.getmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69200
---

ReflectionClass::getMethod

Obtiene un

ReflectionMethod

para un método de clase

## Descripción

```php
public ReflectionClass::getMethod(string $name): ReflectionMethod
```php

Obtiene un `ReflectionMethod` para un método de clase.

## Parámetros

`name`  
El nombre del método a reflejar.

## Valores devueltos

Un objeto `ReflectionMethod`.

## Errores/Excepciones

Una excepción `ReflectionException` si el método no existe.

## Ejemplos

Uso simple de ReflectionClass::getMethod

```
<?php
$class = new ReflectionClass('ReflectionClass');
$method = $class->getMethod('getMethod');
var_dump($method);
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionMethod)#2 (2) {
      ["name"]=>
      string(9) "getMethod"
      ["class"]=>
      string(15) "ReflectionClass"
    }

## Véase también

ReflectionClass::getMethods
