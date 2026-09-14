---
title: ReflectionProperty::getSettableType
description: Devuelve el tipo de argumento de un hook setter
source_url: https://www.php.net/manual/es/reflectionproperty.getsettabletype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/getsettabletype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 79c0572a5
order: 71550
---

ReflectionProperty::getSettableType

Devuelve el tipo de argumento de un hook setter

## Descripción

```php
public ReflectionProperty::getSettableType(): ReflectionType
```php

Devuelve el tipo de argumento de un hook `set`. Si no se define ningún hook `set`, se comporta de manera idéntica a ReflectionProperty::getType.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Este método devuelve una instancia de

ReflectionType

que corresponde al tipo definible para la propiedad.

Si existe un hook

set

que define un tipo explícito, este será devuelto.

Si el hook no especifica un tipo, o si no existe, se devolverá el tipo de la propiedad, de manera idéntica a

ReflectionProperty::getType

. Este valor puede ser

null

si la propiedad no está tipada.

Si la propiedad es virtual y no tiene hook

set

, se devolverá una instancia de

ReflectionType

para

never

.

## Ejemplos

Ejemplo de ReflectionProperty::getSettableType

```
<?php

class Example
{
    public string $basic {
        set => strtolower($value);
    }

    public string $wider {
        set(string|Stringable $value) => (string) $value;
    }

    public string $virtual {
        get => 'Do not change this';
    }

    public $untyped = 'silly';
}

$rClass = new \ReflectionClass(Example::class);

var_dump($rClass->getProperty('basic')->getSettableType());
var_dump($rClass->getProperty('wider')->getSettableType());
var_dump($rClass->getProperty('virtual')->getSettableType());
var_dump($rClass->getProperty('untyped')->getSettableType());

?>

   
```php

El ejemplo anterior mostrará:

    object(ReflectionNamedType)#3 (0) {
    }
    object(ReflectionUnionType)#2 (0) {
    }
    object(ReflectionNamedType)#3 (0) {
    }
    NULL

## Véase también

ReflectionProperty::getType
