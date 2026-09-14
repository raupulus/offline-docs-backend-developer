---
title: ReflectionParameter::getClass
description: Obtiene un objeto ReflectionClass para el parámetro que se está reflejando
  o null
source_url: https://www.php.net/manual/es/reflectionparameter.getclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/getclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 71240
---

ReflectionParameter::getClass

Obtiene un objeto

ReflectionClass

para el parámetro que se está reflejando o

null

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public ReflectionParameter::getClass(): ReflectionClass
```php

Obtiene un objeto `ReflectionClass` para el parámetro que se está reflejando o `null`.

A partir de PHP 8.0.0 esta función está obsoleta y no se recomienda. En su lugar, debe utilizarse ReflectionParameter::getType para obtener la `ReflectionType` de este parámetro y luego interrogar este objeto para determinar el tipo del parámetro.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionClass`, o `null` si no se declara ningún tipo, o el tipo declarado no es una clase o interfaz.

## Ejemplos

Ejemplo de uso de la clase `ReflectionParameter`

```
<?php
function foo(Exception $a) { }

$functionReflection = new ReflectionFunction('foo');
$parameters = $functionReflection->getParameters();
$aParameter = $parameters[0];

echo $aParameter->getClass()->name;
?>

    
```php

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ha sido deprecada en favor de ReflectionParameter::getType. |

## Véase también

ReflectionParameter::getDeclaringClass
