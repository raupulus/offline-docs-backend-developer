---
title: ReflectionFunctionAbstract::getClosureThis
description: Devuelve el objeto que corresponde a $this dentro de una closure
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.getclosurethis.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/getclosurethis.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 348789add
order: 70510
---

ReflectionFunctionAbstract::getClosureThis

Devuelve el objeto que corresponde a \$this dentro de una closure

## Descripción

```php
public ReflectionFunctionAbstract::getClosureThis(): object
```php

Si la función es una closure no estática, recupera el objeto vinculado a `$this` dentro de la closure.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la instancia de objeto representada por `$this` dentro de la `Closure`. Si la función no es una closure o si no tiene un `$this`, `null` es devuelto en su lugar.

## Véase también

ReflectionFunctionAbstract::getClosureCalledClass

ReflectionFunctionAbstract::getClosureScopeClass
