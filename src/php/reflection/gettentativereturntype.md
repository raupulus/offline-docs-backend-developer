---
title: ReflectionFunctionAbstract::getTentativeReturnType
description: Devuelve el tipo de retorno provisional asociado con esta función
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.gettentativereturntype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/gettentativereturntype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70670
---

ReflectionFunctionAbstract::getTentativeReturnType

Devuelve el tipo de retorno provisional asociado con esta función

## Descripción

```php
public ReflectionFunctionAbstract::getTentativeReturnType(): ReflectionType
```php

Devuelve el tipo de retorno provisional asociado con esta función.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `ReflectionType` si se especifica un tipo de retorno provisional, de lo contrario `null`.

## Ejemplos

Ejemplo de ReflectionFunctionAbstract::getTentativeReturnType

```
<?php

$method = new ReflectionMethod(\ArrayAccess::class, 'offsetGet');
var_dump($method->getTentativeReturnType());

    
```php

Resultado del ejemplo anterior es similar a:

    object(ReflectionNamedType)#2 (0) {
    }

## Véase también

ReflectionFunctionAbstract::getReturnType, ReflectionFunctionAbstract::hasTentativeReturnType, [Compatibilidad de los tipos de retorno con las clases internas](#language.oop5.inheritance.internal-classes)
