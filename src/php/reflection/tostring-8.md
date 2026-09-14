---
title: ReflectionParameter::__toString
description: Obtiene una representación textual
source_url: https://www.php.net/manual/es/reflectionparameter.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ca840c9a6
order: 71410
---

ReflectionParameter::\_\_toString

Obtiene una representación textual

## Descripción

```php
public ReflectionParameter::__toString(): string
```php

Obtiene una representación textual del parámetro.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La cadena.

## Ejemplos

Ejemplo de ReflectionParameter::\_\_toString

```
<?php
echo new ReflectionParameter('substr', 0);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Parameter #0 [ <required> string $string ]

## Véase también

ReflectionFunction::\_\_toString, ReflectionMethod::\_\_toString, [\_\_toString()](#object.tostring)
