---
title: ReflectionNamedType::isBuiltin
description: Verifica si es un tipo integrado
source_url: https://www.php.net/manual/es/reflectionnamedtype.isbuiltin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionnamedtype/isbuiltin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 6d2953348
order: 71130
---

ReflectionNamedType::isBuiltin

Verifica si es un tipo integrado

## Descripción

```php
public ReflectionNamedType::isBuiltin(): bool
```php

Verifica si el tipo es un tipo integrado en PHP. Un tipo integrado es todo tipo que no es una clase, interfaz o trait.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si es un tipo integrado en PHP, de lo contrario `false`

## Ejemplos

Ejemplo con ReflectionNamedType::isBuiltin

```
<?php
class SomeClass {}

function someFunction(string $param, SomeClass $param2, stdClass $param3) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParams = $reflectionFunc->getParameters();

var_dump($reflectionParams[0]->getType()->isBuiltin());
var_dump($reflectionParams[1]->getType()->isBuiltin());
var_dump($reflectionParams[2]->getType()->isBuiltin());

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(false)

Se observa que el método ReflectionNamedType::isBuiltin no distingue entre clases internas y de usuario. Para realizar esta distinción, debe utilizarse el método ReflectionClass::isInternal sobre el nombre de clase devuelto.

## Véase también

ReflectionType::allowsNull, ReflectionType::\_\_toString, ReflectionClass::isInternal, ReflectionParameter::getType
