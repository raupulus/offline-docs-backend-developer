---
title: ReflectionFunctionAbstract::getClosureScopeClass
description: Devuelve la clase correspondiente al contexto interno de una función
  anónima
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.getclosurescopeclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/getclosurescopeclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 348789add
order: 70500
---

ReflectionFunctionAbstract::getClosureScopeClass

Devuelve la clase correspondiente al contexto interno de una función anónima

## Descripción

```php
public ReflectionFunctionAbstract::getClosureScopeClass(): ReflectionClass
```php

Devuelve la clase en forma de `ReflectionClass` que corresponde al contexto interno de la `Closure`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una `ReflectionClass` correspondiente a la clase cuyo contexto se utiliza dentro de la `Closure`. Si la función no es una función anónima o si tiene un contexto global, `null` es devuelto en su lugar.

## Véase también

ReflectionFunctionAbstract::getClosureCalledClass

ReflectionFunctionAbstract::getClosureThis
