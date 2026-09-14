---
title: ReflectionClass::getReflectionConstant
description: Obtiene un ReflectionClassConstant para una constante de una clase
source_url: https://www.php.net/manual/es/reflectionclass.getreflectionconstant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getreflectionconstant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c5402f665
order: 69280
---

ReflectionClass::getReflectionConstant

Obtiene un

ReflectionClassConstant

para una constante de una clase

## Descripción

```php
public ReflectionClass::getReflectionConstant(string $name): ReflectionClassConstant
```php

Obtiene un `ReflectionClassConstant` para una constante de clase.

## Parámetros

`name`  
El nombre de la constante de clase.

## Valores devueltos

Un `ReflectionClassConstant`, o `false` si ocurre un error.

## Véase también

ReflectionClass::getReflectionConstants, `ReflectionClassConstant`
