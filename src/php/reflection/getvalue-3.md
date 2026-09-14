---
title: ReflectionEnumUnitCase::getValue
description: Devuelve el objeto del caso de enumeración descrito por este objeto de
  reflexión
source_url: https://www.php.net/manual/es/reflectionenumunitcase.getvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionenumunitcase/getvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70120
---

ReflectionEnumUnitCase::getValue

Devuelve el objeto del caso de enumeración descrito por este objeto de reflexión

## Descripción

```php
public ReflectionEnumUnitCase::getValue(): UnitEnum
```php

Devuelve el objeto del caso de enumeración descrito por este objeto de reflexión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El caso de enumeración descrito por este objeto de reflexión.

## Ejemplos

Ejemplo de ReflectionEnum::getValue

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

$rCase = $rEnum->getCase('Diamonds');

var_dump($rCase->getValue());
?>

    
```php

El ejemplo anterior mostrará:

    enum(Suit::Diamonds)

## Véase también

[Enumeraciones](#language.enumerations)
