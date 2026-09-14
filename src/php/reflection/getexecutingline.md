---
title: ReflectionFiber::getExecutingLine
description: Devuelve el número de línea del punto de ejecución actual
source_url: https://www.php.net/manual/es/reflectionfiber.getexecutingline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfiber/getexecutingline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: db22a7cfc
order: 70340
---

ReflectionFiber::getExecutingLine

Devuelve el número de línea del punto de ejecución actual

## Descripción

```php
public ReflectionFiber::getExecutingLine(): int
```php

Devuelve el número de línea del punto de ejecución actual de la `Fiber` reflejada. Si la fibra reflejada se utiliza fuera de una función definida por el usuario, `null` es devuelto. Si la fibra no ha sido iniciada o ha finalizado, se lanza una `Error`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de línea del punto de ejecución actual de la fibra.
