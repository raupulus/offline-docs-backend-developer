---
title: ReflectionEnumBackedCase::getBackingValue
description: Devuelve el valor escalar de base de este caso de enumeración
source_url: https://www.php.net/manual/es/reflectionenumbackedcase.getbackingvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenumbackedcase/getbackingvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70080
---

ReflectionEnumBackedCase::getBackingValue

Devuelve el valor escalar de base de este caso de enumeración

## Descripción

```php
public ReflectionEnumBackedCase::getBackingValue(): int
```php

Se devuelve el valor escalar de base de este caso de enumeración.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor escalar de base de este caso de enumeración.

## Ejemplos

Ejemplo de ReflectionEnum::getBackingValue

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

$rCase = $rEnum->getCase('Spades');

var_dump($rCase->getBackingValue());
?>

    
```php

El ejemplo anterior mostrará:

    string(1) "S"

## Véase también

[Enumeraciones](#language.enumerations)
