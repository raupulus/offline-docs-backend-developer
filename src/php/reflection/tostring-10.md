---
title: ReflectionType::__toString
description: Conversión a string
source_url: https://www.php.net/manual/es/reflectiontype.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiontype/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: a02e0daac
order: 71890
---

ReflectionType::\_\_toString

Conversión a string

## Descripción

```php
public ReflectionType::__toString(): string
```php

Se recupera el nombre del tipo del argumento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Se devuelve el tipo del argumento.

## Historial de cambios

| Versión | Descripción                                                    |
|---------|----------------------------------------------------------------|
| 8.0.0   | ReflectionType::\_\_toString ha sido marcado como no obsoleto. |
| 7.1.0   | ReflectionType::\_\_toString ha sido marcado como obsoleto.    |

## Ejemplos

Ejemplo con ReflectionType::\_\_toString

```
<?php
function someFunction(string $param) {}

$reflectionFunc = new ReflectionFunction('someFunction');
$reflectionParam = $reflectionFunc->getParameters()[0];

echo $reflectionParam->getType();

    
```php

Resultado del ejemplo anterior es similar a:

    string

## Véase también

ReflectionNamedType::getName, ReflectionNamedType::isBuiltin, ReflectionType::allowsNull, ReflectionUnionType::getTypes, ReflectionParameter::getType
