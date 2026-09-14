---
title: ReflectionProperty::isFinal
description: Determina si la propiedad es final o no
source_url: https://www.php.net/manual/es/reflectionproperty.isfinal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isfinal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: a16ad380e
order: 71650
---

ReflectionProperty::isFinal

Determina si la propiedad es final o no

## Descripción

```php
public ReflectionProperty::isFinal(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve si la propiedad es [`final`](#language.oop5.final). Si la propiedad está marcada `private(set)`, entonces también será implícitamente `final`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la propiedad está explícitamente marcada `final`, o si es implícitamente `final` debido a ser `private(set)`. Devuelve `false` en caso contrario.

## Ejemplos

Ejemplo de ReflectionProperty::isFinal

```
<?php
class Example
{
    public string $name;

    final protected int $age;

    public private(set) string $job;
}

$rClass = new \ReflectionClass(Example::class);

var_dump($rClass->getProperty('name')->isFinal());
var_dump($rClass->getProperty('age')->isFinal());
var_dump($rClass->getProperty('job')->isFinal());
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    bool(true)

## Véase también

Elementos de clase

final

Visibilidad de propiedad asimétrica
