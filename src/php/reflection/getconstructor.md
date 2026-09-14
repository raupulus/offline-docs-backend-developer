---
title: ReflectionClass::getConstructor
description: Obtiene el constructor de una clase
source_url: https://www.php.net/manual/es/reflectionclass.getconstructor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getconstructor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69100
---

ReflectionClass::getConstructor

Obtiene el constructor de una clase

## Descripción

```php
public ReflectionClass::getConstructor(): ReflectionMethod
```php

Obtiene el constructor de una clase.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionMethod` que refleja el constructor de la clase, o `null` si la clase no tiene constructor.

## Ejemplos

Uso simple de ReflectionClass::getConstructor

```
<?php
$class = new ReflectionClass('ReflectionClass');
$constructor = $class->getConstructor();
var_dump($constructor);
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionMethod)#2 (2) {
      ["name"]=>
      string(11) "__construct"
      ["class"]=>
      string(15) "ReflectionClass"
    }

## Véase también

ReflectionClass::getName
