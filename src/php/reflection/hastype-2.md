---
title: ReflectionParameter::hasType
description: Verifica si un parámetro tiene un tipo
source_url: https://www.php.net/manual/es/reflectionparameter.hastype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/hastype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71320
---

ReflectionParameter::hasType

Verifica si un parámetro tiene un tipo

## Descripción

```php
public ReflectionParameter::hasType(): bool
```php

Verifica si el parámetro tiene un tipo asociado con este.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si se especifica un tipo, `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionParameter::hasType

```
<?php
function someFunction(string $param, $param2 = null) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParams = $reflectionFunc->getParameters();

var_dump($reflectionParams[0]->hasType());
var_dump($reflectionParams[1]->hasType());

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)

## Véase también

ReflectionParameter::getType
