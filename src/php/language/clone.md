---
title: Error::__clone
description: Clonar el error
source_url: https://www.php.net/manual/es/error.clone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/clone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3150
---

Error::\_\_clone

Clonar el error

## Descripción

```php
private Error::__clone(): void
```php

Un error no se pueden clonar, por lo que este método resulta en un error fatal.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Los errores *no* son clonabes.

## Historial de cambios

| Versión | Descripción                      |
|---------|----------------------------------|
| 8.1.0   | Error::\_\_clone ya no es final. |
