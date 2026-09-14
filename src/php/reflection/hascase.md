---
title: ReflectionEnum::hasCase
description: Verifica un caso en una enumeración
source_url: https://www.php.net/manual/es/reflectionenum.hascase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenum/hascase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70040
---

ReflectionEnum::hasCase

Verifica un caso en una enumeración

## Descripción

```php
public ReflectionEnum::hasCase(string $name): bool
```php

Determina si un caso dado está definido en una enumeración.

## Parámetros

`name`  
El caso a verificar.

## Valores devueltos

`true` si el caso está definido, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionEnum::hasCase

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

var_dump($rEnum->hasCase('Hearts'));
var_dump($rEnum->hasCase('Horseshoes'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

[Enumeraciones](#language.enumerations), ReflectionEnum::getCase, ReflectionEnum::getCases
