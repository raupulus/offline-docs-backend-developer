---
title: ReflectionEnum::getCase
description: Devuelve un caso específico de una enumeración
source_url: https://www.php.net/manual/es/reflectionenum.getcase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenum/getcase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70020
---

ReflectionEnum::getCase

Devuelve un caso específico de una enumeración

## Descripción

```php
public ReflectionEnum::getCase(string $name): ReflectionEnumUnitCase
```php

Devuelve el objeto de reflexión para un caso específico de una enumeración por su nombre. Si el caso solicitado no está definido, se lanza una `ReflectionException`.

## Parámetros

`name`  
El nombre del caso a recuperar.

## Valores devueltos

Una instancia de `ReflectionEnumUnitCase` o `ReflectionEnumBackedCase`, según el caso.

## Ejemplos

Ejemplo de ReflectionEnum::getCase

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

$rCase = $rEnum->getCase('Clubs');

var_dump($rCase->getValue());
?>

    
```php

El ejemplo anterior mostrará:

    enum(Suit::Clubs)

## Véase también

[Enumeraciones](#language.enumerations), ReflectionEnum::getCases, ReflectionEnum::hasCase, ReflectionEnum::isBacked
