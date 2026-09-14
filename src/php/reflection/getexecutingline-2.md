---
title: ReflectionGenerator::getExecutingLine
description: Obtiene la línea actualmente ejecutada del generador
source_url: https://www.php.net/manual/es/reflectiongenerator.getexecutingline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/getexecutingline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70840
---

ReflectionGenerator::getExecutingLine

Obtiene la línea actualmente ejecutada del generador

## Descripción

```php
public ReflectionGenerator::getExecutingLine(): int
```php

Obtiene la línea actualmente ejecutada del generador.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de línea de la declaración actualmente ejecutada en el generador.

## Ejemplos

Ejemplo con ReflectionGenerator::getExecutingLine

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

echo "Line: {$reflectionGen->getExecutingLine()}";

    
```php

Resultado del ejemplo anterior es similar a:

    Line: 7

## Véase también

ReflectionGenerator::getExecutingGenerator, ReflectionGenerator::getExecutingFile
