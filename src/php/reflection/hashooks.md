---
title: ReflectionProperty::hasHooks
description: Indica si la propiedad tiene hooks definidos
source_url: https://www.php.net/manual/es/reflectionproperty.hashooks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/hashooks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: a16ad380e
order: 71600
---

ReflectionProperty::hasHooks

Indica si la propiedad tiene hooks definidos

## Descripción

```php
public ReflectionProperty::hasHooks(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Indica si la propiedad tiene hooks definidos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la propiedad tiene al menos un hook definido, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionProperty::hasHooks

```
<?php
class Example
{
    public string $name { get => "Name here"; }

    public string $none;
}

$rClass = new \ReflectionClass(Example::class);
var_dump($rClass->getProperty('name')->hasHooks());
var_dump($rClass->getProperty('none')->hasHooks());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Notas

> [!NOTE]
> Este método es equivalente a verificar ReflectionProperty::getHooks con un array vacío.

## Véase también

ReflectionProperty::getHooks
