---
title: ReflectionClass::getLazyInitializer
description: Devuelve el inicializador perezoso
source_url: https://www.php.net/manual/es/reflectionclass.getlazyinitializer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getlazyinitializer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c0fa5077c
order: 69190
---

ReflectionClass::getLazyInitializer

Devuelve el inicializador perezoso

## Descripción

```php
public ReflectionClass::getLazyInitializer(object $object): callable
```php

Devuelve el inicializador perezoso o la fábrica asociada a `object`.

## Parámetros

`object`  
El objeto a partir del cual obtener el inicializador.

## Valores devueltos

Devuelve el inicializador si el objeto es un objeto perezoso no inicializado, `null` en caso contrario.

## Véase también

Objetos perezosos

ReflectionClass::newLazyGhost
