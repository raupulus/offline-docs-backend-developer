---
title: ReflectionExtension::__toString
description: Obtiene una representación textual
source_url: https://www.php.net/manual/es/reflectionextension.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70290
---

ReflectionExtension::\_\_toString

Obtiene una representación textual

## Descripción

```php
public ReflectionExtension::__toString(): string
```php

Exporta una extensión reflejada y devuelve el resultado en forma de `string`. Este método es idéntico a ReflectionExtension::export con `return` definido como `true`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la extensión reflejada en forma de string, de la misma manera que ReflectionExtension::export.

## Véase también

ReflectionExtension::\_\_construct, ReflectionExtension::export, [\_\_toString()](#object.tostring)
