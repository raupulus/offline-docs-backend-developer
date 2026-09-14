---
title: BackedEnum::tryFrom
description: Asocia un escalar a una instancia de enum o a null
source_url: https://www.php.net/manual/es/backedenum.tryfrom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/backedenum/tryfrom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 9c74079f1
order: 3010
---

BackedEnum::tryFrom

Asocia un escalar a una instancia de enum o a null

## Descripción

```php
public static BackedEnum::tryFrom(int $value): static
```php

El método tryFrom traduce un `string` o un `int` en el caso Enum correspondiente, si existe. Si no hay un caso correspondiente definido, devolverá null.

## Parámetros

`value`  
El valor escalar a hacer corresponder con un caso de enumeración.

## Valores devueltos

Una instancia de caso de esta enumeración, o `null` si no se ha encontrado.

## Ejemplos

Uso básico

El siguiente ejemplo ilustra la manera en que los casos de enumeración son devueltos.

```
<?php
enum Suit: string
{
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';
}

$h = Suit::tryFrom('H');

var_dump($h);

$b = Suit::tryFrom('B') ?? Suit::Spades;

var_dump($b);
?>

   
```php

El ejemplo anterior mostrará:

    enum(Suit::Hearts)
    enum(Suit::Spades)

## Véase también

UnitEnum::cases, BackedEnum::from
