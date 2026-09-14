---
title: Exception::__clone
description: Clona la excepción
source_url: https://www.php.net/manual/es/exception.clone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/clone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 35c16b154
order: 3290
---

Exception::\_\_clone

Clona la excepción

## Descripción

```php
private Exception::__clone(): void
```php

`Exception`s no se pueden clonar, y el intento de hacerlo lanzará un `Error`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Las Excepciones *no* se pueden clonar.

## Historial de cambios

| Versión | Descripción                      |
|---------|----------------------------------|
| 8.1.0   | Error::\_\_clone ya no es final. |
