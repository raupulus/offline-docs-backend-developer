---
title: ReflectionClassConstant::isDeprecated
description: Verifica la deprecación
source_url: https://www.php.net/manual/es/reflectionclassconstant.isdeprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclassconstant/isdeprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 7de265dc4
order: 69800
---

ReflectionClassConstant::isDeprecated

Verifica la deprecación

## Descripción

```php
public ReflectionClassConstant::isDeprecated(): bool
```php

Verifica si la constante de clase está deprecada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si está deprecada, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionClassConstant::isDeprecated

```
<?php
class Basket {
    #[\Deprecated(message: 'use Basket::APPLE instead')]
    public const APLE = 'apple';

    public const APPLE = 'apple';
}
$classConstant = new ReflectionClassConstant('Basket', 'APLE');
var_dump($classConstant->isDeprecated());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

Deprecated

ReflectionClassConstant::getDocComment
