---
title: ReflectionGenerator::getExecutingFile
description: Obtiene el nombre de fichero del generador actualmente ejecutado
source_url: https://www.php.net/manual/es/reflectiongenerator.getexecutingfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/getexecutingfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70820
---

ReflectionGenerator::getExecutingFile

Obtiene el nombre de fichero del generador actualmente ejecutado

## Descripción

```php
public ReflectionGenerator::getExecutingFile(): string
```php

Obtiene la ruta completa y el nombre de fichero del generador actualmente ejecutado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta completa y el nombre de fichero del generador actualmente ejecutado.

## Ejemplos

Ejemplo con ReflectionGenerator::getExecutingFile

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

echo "File: {$reflectionGen->getExecutingFile()}";

    
```php

Resultado del ejemplo anterior es similar a:

    File: /path/to/file/example.php

## Véase también

ReflectionGenerator::getExecutingLine, ReflectionGenerator::getExecutingGenerator
