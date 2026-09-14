---
title: UnitEnum::cases
description: Genera una lista de casos sobre una enumeración
source_url: https://www.php.net/manual/es/unitenum.cases.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/unitenum/cases.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 4b06b2d5c
order: 4080
---

UnitEnum::cases

Genera una lista de casos sobre una enumeración

## Descripción

```php
public static UnitEnum::cases(): array
```php

Este método devuelve un array de todos los casos de una enumeración, en el orden de su declaración.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de todos los casos definidos de esta enumeración, en el orden de la declaración.

## Ejemplos

Uso básico

El siguiente ejemplo ilustra la forma en que los casos de enumeración son devueltos.

```
<?php
enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

var_dump(Suit::cases());

   
```php

El ejemplo anterior mostrará:

    array(4) {
      [0]=>
      enum(Suit::Hearts)
      [1]=>
      enum(Suit::Diamonds)
      [2]=>
      enum(Suit::Clubs)
      [3]=>
      enum(Suit::Spades)
    }
