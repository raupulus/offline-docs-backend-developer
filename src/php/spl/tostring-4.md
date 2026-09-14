---
title: SplFileObject::__toString
description: Retorna la línea actual como un string
source_url: https://www.php.net/manual/es/splfileobject.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 823dc72e7
order: 84620
---

SplFileObject::\_\_toString

Retorna la línea actual como un string

## Descripción

```php
public SplFileObject::__toString(): string
```php

Este método retorna la línea actual como un string.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna la línea actual como un string.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.14, 8.2.1 | Cambiada de un alias de SplFileObject::fgets a una implementación de SplFileObject::current que retorna un string CSV cuando la opción `SplFileObject::READ_CSV` está definida. |
| 7.2.19, 7.3.6 | Modificada de un alias de SplFileObject::current a un alias de SplFileObject::fgets. |
