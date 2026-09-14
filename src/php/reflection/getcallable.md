---
title: ReflectionFiber::getCallable
description: Devuelve el callable utilizado para crear la Fibra
source_url: https://www.php.net/manual/es/reflectionfiber.getcallable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfiber/getcallable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70320
---

ReflectionFiber::getCallable

Devuelve el callable utilizado para crear la Fibra

## Descripción

```php
public ReflectionFiber::getCallable(): callable
```php

Devuelve el callable utilizado para crear la `Fiber`. Si la `Fiber` ha sido terminada, se lanza una `Error`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El callable utilizado para crear la `Fiber`.
