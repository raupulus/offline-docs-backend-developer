---
title: ReflectionGenerator::getThis
description: Obtiene el valor de $this del generador
source_url: https://www.php.net/manual/es/reflectiongenerator.getthis.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/getthis.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70860
---

ReflectionGenerator::getThis

Obtiene el valor de

\$this

del generador

## Descripción

```php
public ReflectionGenerator::getThis(): object
```php

Obtiene el valor de `$this` del generador al que tiene acceso.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el valor de `$this`, o `null` si el generador no ha sido creado en un contexto de clase.

## Ejemplos

Ejemplo con ReflectionGenerator::getThis

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

var_dump($reflectionGen->getThis());

    
```php

Resultado del ejemplo anterior es similar a:

    object(GenExample)#3 (0) {
    }

## Véase también

ReflectionGenerator::getFunction, ReflectionGenerator::getTrace
