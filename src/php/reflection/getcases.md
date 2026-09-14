---
title: ReflectionEnum::getCases
description: Devuelve la lista de todos los casos de una enumeración
source_url: https://www.php.net/manual/es/reflectionenum.getcases.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenum/getcases.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70030
---

ReflectionEnum::getCases

Devuelve la lista de todos los casos de una enumeración

## Descripción

```php
public ReflectionEnum::getCases(): array
```php

Una enumeración puede contener cero o varios casos. Este método recupera todos los casos definidos, en orden léxico (es decir, el orden en que aparecen en el código fuente).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos de reflexión de enumeración, uno por cada caso de la enumeración. Para una enumeración unitaria, serán todas instancias de `ReflectionEnumUnitCase`. Para una enumeración con valor base, serán todas instancias de `ReflectionEnumBackedCase`.

## Ejemplos

Ejemplo de ReflectionEnum::getCases

```
<?php
enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

$rEnum = new ReflectionEnum(Suit::class);

$cases = $rEnum->getCases();

foreach ($cases as $rCase) {
    var_dump($rCase->getValue());
}
?>

    
```php

El ejemplo anterior mostrará:

    enum(Suit::Hearts)
    enum(Suit::Diamonds)
    enum(Suit::Clubs)
    enum(Suit::Spades)

## Véase también

[Enumeraciones](#language.enumerations), ReflectionEnum::getCase, ReflectionEnum::isBacked
