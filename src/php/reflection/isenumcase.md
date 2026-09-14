---
title: ReflectionClassConstant::isEnumCase
description: Verifica si la constante de clase es un caso de enumeración
source_url: https://www.php.net/manual/es/reflectionclassconstant.isenumcase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclassconstant/isenumcase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69810
---

ReflectionClassConstant::isEnumCase

Verifica si la constante de clase es un caso de enumeración

## Descripción

```php
public ReflectionClassConstant::isEnumCase(): bool
```php

Verifica si la constante de clase es un caso de [enumeración](#language.enumerations).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la constante de clase es una enumeración; de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionClassConstant::isEnumCase

Distingue entre los casos de enumeración y las constantes de clase regulares.

```
<?php
enum Status
{
    const BORING_CONSTANT = 'test';
    const ENUM_VALUE = Status::PUBLISHED;

    case DRAFT;
    case PUBLISHED;
    case ARCHIVED;
}

$reflection = new ReflectionEnum(Status::class);
foreach ($reflection->getReflectionConstants() as $constant) {
    echo "{$constant->name} is ",
        $constant->isEnumCase() ? "an enum case" : "a regular class constant",
        PHP_EOL;
}
?>

   
```php

El ejemplo anterior mostrará:

    BORING_CONSTANT is a regular class constant
    ENUM_VALUE is a regular class constant
    DRAFT is an enum case
    PUBLISHED is an enum case
    ARCHIVED is an enum case

## Véase también

ReflectionEnum
