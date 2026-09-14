---
title: ReflectionType::allowsNull
description: Verifica si null es admitido
source_url: https://www.php.net/manual/es/reflectiontype.allowsnull.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiontype/allowsnull.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 6d2953348
order: 71880
---

ReflectionType::allowsNull

Verifica si null es admitido

## Descripción

```php
public ReflectionType::allowsNull(): bool
```php

Verifica si el argumento acepta `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si `null` es admitido, de lo contrario `false`

## Ejemplos

Ejemplo con ReflectionType::allowsNull

```
<?php
function someFunction(string $param, stdClass $param2 = null) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParams = $reflectionFunc->getParameters();

var_dump($reflectionParams[0]->getType()->allowsNull());
var_dump($reflectionParams[1]->getType()->allowsNull());

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionNamedType::isBuiltin, ReflectionType::\_\_toString, ReflectionParameter::getType
