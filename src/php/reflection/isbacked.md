---
title: ReflectionEnum::isBacked
description: Determina si una enumeración es una enumeración con valor base
source_url: https://www.php.net/manual/es/reflectionenum.isbacked.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenum/isbacked.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70050
---

ReflectionEnum::isBacked

Determina si una enumeración es una enumeración con valor base

## Descripción

```php
public ReflectionEnum::isBacked(): bool
```php

Una enumeración con valor base es una enumeración que tiene un equivalente escalar nativo, ya sea un `string` o un `int`. No todas las enumeraciones tienen valor base.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la enumeración tiene un soporte escalar, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionEnum::isBacked

```
<?php
enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

enum BackedSuit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

var_dump((new ReflectionEnum(Suit::class))->isBacked());
var_dump((new ReflectionEnum(BackedSuit::class))->isBacked());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

[Enumeraciones](#language.enumerations), ReflectionEnum::getBackingType
