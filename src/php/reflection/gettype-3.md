---
title: ReflectionProperty::getType
description: Obtiene el tipo de una propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71560
---

ReflectionProperty::getType

Obtiene el tipo de una propiedad

## Descripción

```php
public ReflectionProperty::getType(): ReflectionType
```php

Obtiene el tipo asociado a una propiedad.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una `ReflectionType` si la propiedad tiene un tipo, y `null` en caso contrario.

## Ejemplos

Ejemplo de ReflectionProperty::getType

```
<?php
class User
{
    public string $name;
}

$rp = new ReflectionProperty('User', 'name');
echo $rp->getType()->getName();
?>

   
```php

El ejemplo anterior mostrará:

    string

## Véase también

ReflectionProperty::hasType

ReflectionProperty::isInitialized
