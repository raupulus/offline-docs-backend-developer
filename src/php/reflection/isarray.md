---
title: ReflectionParameter::isArray
description: Verifica si el parámetro espera un array
source_url: https://www.php.net/manual/es/reflectionparameter.isarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/isarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 71330
---

ReflectionParameter::isArray

Verifica si el parámetro espera un array

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

Ver el ejemplo a continuación para un método alternativo para obtener esta información.

## Descripción

```php
#[\Deprecated] public ReflectionParameter::isArray(): bool
```php

Verifica si el parámetro espera un array.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si el parámetro espera un array, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido deprecada en favor del método ReflectionParameter::getType. |

## Ejemplos

Equivalente en PHP 8.0.0

A partir de PHP 8.0.0, el siguiente código indica si un tipo soporta arrays, incluyendo aquellos que forman parte de una unión.

```
<?php
function declaresArray(ReflectionParameter $reflectionParameter): bool
{
    $reflectionType = $reflectionParameter->getType();

    if (!$reflectionType) return false;

    $types = $reflectionType instanceof ReflectionUnionType
        ? $reflectionType->getTypes()
        : [$reflectionType];

   return in_array('array', array_map(fn(ReflectionNamedType $t) => $t->getName(), $types));
}
?>

    
```php

## Véase también

ReflectionParameter::isOptional
