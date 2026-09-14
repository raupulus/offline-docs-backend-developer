---
title: ReflectionProperty::hasHook
description: Indica si la propiedad tiene un hook dado definido
source_url: https://www.php.net/manual/es/reflectionproperty.hashook.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/hashook.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 79c0572a5
order: 71590
---

ReflectionProperty::hasHook

Indica si la propiedad tiene un hook dado definido

## Descripción

```php
public ReflectionProperty::hasHook(PropertyHookType $type): bool
```php

Indica si la propiedad tiene un hook dado definido.

## Parámetros

`PropertyHookType`  
El tipo de hook a verificar.

## Valores devueltos

Devuelve `true` si el hook está definido en esta propiedad, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionProperty::hasHook

```
<?php
class Example
{
    public string $name { get => "Name here"; }
}

$rClass = new \ReflectionClass(Example::class);
$rProp = $rClass->getProperty('name');
var_dump($rProp->hasHook(PropertyHookType::Get));
var_dump($rProp->hasHook(PropertyHookType::Set));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

ReflectionMethod

PropertyHookType
