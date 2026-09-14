---
title: ReflectionGenerator::getExecutingGenerator
description: Obtiene el objeto Generator ejecutado
source_url: https://www.php.net/manual/es/reflectiongenerator.getexecutinggenerator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/getexecutinggenerator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70830
---

ReflectionGenerator::getExecutingGenerator

Obtiene el objeto

Generator

ejecutado

## Descripción

```php
public ReflectionGenerator::getExecutingGenerator(): Generator
```php

Obtiene el objeto `Generator` ejecutado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el objeto `Generator` actualmente ejecutado.

## Ejemplos

Ejemplo con ReflectionGenerator::getExecutingGenerator

```
<?php

class GenExample
{
    public function gen()
    {
        yield 1;
    }
}

$gen = (new GenExample)->gen();

$reflectionGen = new ReflectionGenerator($gen);

$gen2 = $reflectionGen->getExecutingGenerator();

var_dump($gen2 === $gen);
var_dump($gen2->current());

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    int(1);

## Véase también

ReflectionGenerator::getExecutingLine, ReflectionGenerator::getExecutingFile
