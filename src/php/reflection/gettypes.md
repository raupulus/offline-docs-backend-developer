---
title: ReflectionIntersectionType::getTypes
description: Devuelve los tipos incluidos en el tipo de intersección
source_url: https://www.php.net/manual/es/reflectionintersectiontype.gettypes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionintersectiontype/gettypes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70900
---

ReflectionIntersectionType::getTypes

Devuelve los tipos incluidos en el tipo de intersección

## Descripción

```php
public ReflectionIntersectionType::getTypes(): array
```php

Devuelve los tipos incluidos en el tipo de intersección.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos `ReflectionType`.

## Ejemplos

Ejemplo de ReflectionIntersectionType::getTypes

```
<?php

function someFunction(Iterator&Countable $value) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParam = $reflectionFunc->getParameters()[0];

var_dump($reflectionParam->getType()->getTypes());
?>

    
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
