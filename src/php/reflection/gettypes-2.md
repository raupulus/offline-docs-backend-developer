---
title: ReflectionUnionType::getTypes
description: Devuelve los tipos incluidos en la unión
source_url: https://www.php.net/manual/es/reflectionuniontype.gettypes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionuniontype/gettypes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 71910
---

ReflectionUnionType::getTypes

Devuelve los tipos incluidos en la unión

## Descripción

```php
public ReflectionUnionType::getTypes(): array
```php

Devuelve la reflexión de los tipos incluidos en la unión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos `ReflectionType`.

## Ejemplos

Ejemplo de ReflectionUnionType::getTypes

```
<?php
function someFunction(int|float $number) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParam = $reflectionFunc->getParameters()[0];

var_dump($reflectionParam->getType()->getTypes());

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
        [0] =>
        class ReflectionNamedType#4(0) {
        }
        [1] =>
        class ReflectionNamedType#5(0) {
        }
    }

## Véase también

ReflectionType::allowsNull, ReflectionParameter::getType
