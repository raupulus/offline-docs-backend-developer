---
title: ReflectionEnum::getBackingType
description: Devuelve el tipo base de una enumeración, si está presente
source_url: https://www.php.net/manual/es/reflectionenum.getbackingtype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenum/getbackingtype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 911fe79de
order: 70010
---

ReflectionEnum::getBackingType

Devuelve el tipo base de una enumeración, si está presente

## Descripción

```php
public ReflectionEnum::getBackingType(): ReflectionNamedType
```php

Si la enumeración es una enumeración con valor base, este método devolverá una instancia de `ReflectionType` para el tipo base de la enumeración. Si no es una enumeración con valor base, devolverá `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una instancia de `ReflectionNamedType`, o `null` si la enumeración no tiene tipo base.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El valor de retorno ahora es declarado como `?ReflectionNamedType`. Anteriormente, `?ReflectionType` era declarado. |

## Ejemplos

Ejemplo de ReflectionEnum::getBackingType

```
<?php
enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

$rEnum = new ReflectionEnum(Suit::class);

$rBackingType = $rEnum->getBackingType();

var_dump((string) $rBackingType);
?>

    
```php

El ejemplo anterior mostrará:

    string(6) "string"

## Véase también

[Enumeraciones](#language.enumerations), ReflectionEnum::isBacked
