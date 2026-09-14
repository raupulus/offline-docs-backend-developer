---
title: ReflectionGenerator::getFunction
description: Obtiene el nombre de función del generador
source_url: https://www.php.net/manual/es/reflectiongenerator.getfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/getfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 812143d1d
order: 70850
---

ReflectionGenerator::getFunction

Obtiene el nombre de función del generador

## Descripción

```php
public ReflectionGenerator::getFunction(): ReflectionFunctionAbstract
```php

Permite obtener el nombre de función del generador devolviendo una clase derivada de `ReflectionFunctionAbstract`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una clase `ReflectionFunctionAbstract`. Esto será `ReflectionFunction` para las funciones, o `ReflectionMethod` para los métodos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | ReflectionGenerator::getFunction puede ser ahora llamado después de que el generador haya sido cerrado. |

## Ejemplos

Ejemplo con ReflectionGenerator::getFunction

```
<?php

function gen()
{
    yield 1;
}

$gen = gen();

$reflectionGen = new ReflectionGenerator($gen);

var_dump($reflectionGen->getFunction());

    
```php

Resultado del ejemplo anterior es similar a:

    object(ReflectionFunction)#3 (1) {
      ["name"]=>
      string(3) "gen"
    }

## Véase también

ReflectionGenerator::getThis, ReflectionGenerator::getTrace
