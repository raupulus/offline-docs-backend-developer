---
title: ReflectionFunctionAbstract::hasReturnType
description: Verifica si la función tiene un tipo de retorno definido
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.hasreturntype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/hasreturntype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c3485c8f1
order: 70680
---

ReflectionFunctionAbstract::hasReturnType

Verifica si la función tiene un tipo de retorno definido

## Descripción

```php
public ReflectionFunctionAbstract::hasReturnType(): bool
```php

Verifica si la función tiene un tipo de retorno definido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si la función tiene un tipo de retorno definido, de lo contrario `false`.

## Ejemplos

Ejemplo con ReflectionFunctionAbstract::hasReturnType

```
<?php

function to_int($param): int
{
    return (int) $param;
}

$reflection1 = new ReflectionFunction('to_int');
var_dump($reflection1->hasReturnType());

    
```php

El ejemplo anterior mostrará:

    bool(true)

Uso con funciones integradas

```
<?php

$reflection2 = new ReflectionFunction('array_merge');

var_dump($reflection2->hasReturnType());

    
```php

El ejemplo anterior mostrará:

    bool(false)

## Véase también

ReflectionFunctionAbstract::getReturnType
