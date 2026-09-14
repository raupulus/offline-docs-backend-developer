---
title: ReflectionProperty::hasType
description: Verifica si la propiedad tiene un tipo
source_url: https://www.php.net/manual/es/reflectionproperty.hastype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/hastype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71610
---

ReflectionProperty::hasType

Verifica si la propiedad tiene un tipo

## Descripción

```php
public ReflectionProperty::hasType(): bool
```php

Verifica si la propiedad tiene un tipo asociado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si se especifica un tipo, `false` en caso contrario.

## Ejemplos

Ejemplo de ReflectionProperty::hasType

```
<?php
class User
{
    public string $name;
}

$rp = new ReflectionProperty('User', 'name');
var_dump($rp->hasType());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

ReflectionProperty::getType

ReflectionProperty::isInitialized
