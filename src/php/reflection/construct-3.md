---
title: ReflectionClassConstant::__construct
description: Construye una ReflectionClassConstant
source_url: https://www.php.net/manual/es/reflectionclassconstant.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclassconstant/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69700
---

ReflectionClassConstant::\_\_construct

Construye una ReflectionClassConstant

## Descripción

```php
public ReflectionClassConstant::__construct(object $class, string $constant)
```php

Construye un nuevo objeto `ReflectionClassConstant`.

## Parámetros

`class`  
Puede ser un `string` que contenga el nombre de la clase a reflejar, o un `object`.

`constant`  
El nombre de la constante de clase.

## Errores/Excepciones

Se lanza una `Exception` en caso de que la constante de clase proporcionada no exista.

## Véase también

[Constructors](#language.oop5.decon.constructor)
