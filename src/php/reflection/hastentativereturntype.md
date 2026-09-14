---
title: ReflectionFunctionAbstract::hasTentativeReturnType
description: Indica si la función tiene un tipo de retorno provisional
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.hastentativereturntype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/hastentativereturntype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70690
---

ReflectionFunctionAbstract::hasTentativeReturnType

Indica si la función tiene un tipo de retorno provisional

## Descripción

```php
public ReflectionFunctionAbstract::hasTentativeReturnType(): bool
```php

Indica si la función tiene un tipo de retorno provisional.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la función tiene un tipo de retorno provisional, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionFunctionAbstract::hasTentativeReturnType

```
<?php

$method = new ReflectionMethod(\ArrayAccess::class, 'offsetGet');
var_dump($method->hasTentativeReturnType());

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

ReflectionFunctionAbstract::getTentativeReturnType, ReflectionFunctionAbstract::hasReturnType, [Compatibilidad de los tipos de retorno con las clases internas](#language.oop5.inheritance.internal-classes)
