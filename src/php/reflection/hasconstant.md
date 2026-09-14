---
title: ReflectionClass::hasConstant
description: Verifica si una constante está definida
source_url: https://www.php.net/manual/es/reflectionclass.hasconstant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/hasconstant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69370
---

ReflectionClass::hasConstant

Verifica si una constante está definida

## Descripción

```php
public ReflectionClass::hasConstant(string $name): bool
```php

Verifica si una constante específica está definida en una clase.

## Parámetros

`name`  
Nombre de la constante a verificar.

## Valores devueltos

`true` si la constante está definida, `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::hasConstant

```
<?php
class Foo {
    const c1 = 1;
}

$class = new ReflectionClass("Foo");

var_dump($class->hasConstant("c1"));
var_dump($class->hasConstant("c2"));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)

## Véase también

ReflectionClass::hasMethod, ReflectionClass::hasProperty
