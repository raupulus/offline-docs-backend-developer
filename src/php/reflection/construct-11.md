---
title: ReflectionGenerator::__construct
description: Construye un objeto ReflectionGenerator
source_url: https://www.php.net/manual/es/reflectiongenerator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70810
---

ReflectionGenerator::\_\_construct

Construye un objeto ReflectionGenerator

## Descripción

```php
public ReflectionGenerator::__construct(Generator $generator)
```php

Construye un objeto `ReflectionGenerator`.

## Parámetros

`generator`  
Un objeto generator.

## Ejemplos

Ejemplo con ReflectionGenerator::\_\_construct

```
<?php

function gen()
{
    yield 1;
}

$gen = gen();

$reflectionGen = new ReflectionGenerator($gen);

echo <<< output
{$reflectionGen->getFunction()->name}
Line: {$reflectionGen->getExecutingLine()}
File: {$reflectionGen->getExecutingFile()}
output;

    
```php

Resultado del ejemplo anterior es similar a:

    gen
    Line: 5
    File: /path/to/file/example.php

## Véase también

ReflectionGenerator::getFunction, ReflectionGenerator::getExecutingLine, ReflectionGenerator::getExecutingFile
