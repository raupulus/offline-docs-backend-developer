---
title: BackedEnum::from
description: Convierte un escalar en una instancia de enum
source_url: https://www.php.net/manual/es/backedenum.from.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/backedenum/from.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 9c74079f1
order: 3000
---

BackedEnum::from

Convierte un escalar en una instancia de enum

## Descripción

```php
public static BackedEnum::from(int $value): static
```php

El método from traduce un `string` o un `int` en un caso Enum correspondiente, si existe. Si no hay un caso correspondiente definido, lanzará un error `ValueError`.

## Parámetros

`value`  
El valor escalar a hacer coincidir con un caso de enumeración.

## Valores devueltos

Una instancia de caso de esta enumeración.

## Ejemplos

Uso básico

El siguiente ejemplo ilustra la forma en que se devuelven los casos de enumeración.

```
<?php
enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

$h = Suit::from('H');

var_dump($h);

$b = Suit::from('B');
?>

   
```php

El ejemplo anterior mostrará:

    enum(Suit::Hearts)

    Fatal error: Uncaught ValueError: "B" is not a valid backing value for enum "Suit" in /file.php:15

## Véase también

UnitEnum::cases, BackedEnum::tryFrom
