---
title: ReflectionProperty::getHook
description: Devuelve un objeto de reflexión para un hook dado
source_url: https://www.php.net/manual/es/reflectionproperty.gethook.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/gethook.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 366a10b13
order: 71500
---

ReflectionProperty::getHook

Devuelve un objeto de reflexión para un hook dado

## Descripción

```php
public ReflectionProperty::getHook(PropertyHookType $type): ReflectionMethod
```php

Devuelve la reflexión del hook de la propiedad, si está definido.

## Parámetros

`PropertyHookType`  
El tipo de hook a solicitar.

## Valores devueltos

Si el hook solicitado está definido, se devuelve una instancia de `ReflectionMethod`. De lo contrario, el método devolverá `null`

## Ejemplos

Ejemplo de ReflectionProperty::getHook

```
<?php
class Example
{
    public string $name { get => "Name here"; }
}

$rClass = new \ReflectionClass(Example::class);
$rProp = $rClass->getProperty('name');
var_dump($rProp->getHook(PropertyHookType::Get));
var_dump($rProp->getHook(PropertyHookType::Set));
?>

   
```php

El ejemplo anterior mostrará:

    object(ReflectionMethod)#4 (2) {
      ["name"]=>
      string(10) "$name::get"
      ["class"]=>
      string(7) "Example"
    }
    NULL

## Véase también

ReflectionMethod

PropertyHookType
