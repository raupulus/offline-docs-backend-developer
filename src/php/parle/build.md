---
title: Parle\Lexer::build
description: Finaliza el conjunto de reglas del lexer
source_url: https://www.php.net/manual/es/parle-lexer.build.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/lexer/build.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 6add79a3e
order: 60410
---

Parle\Lexer::build

Finaliza el conjunto de reglas del lexer

## Descripción

```php
public Parle\Lexer::build(): void
```php

Las reglas, previamente añadidas con Parle\Lexer::push, son finalizadas. Esta llamada de método debe realizarse después de que todas las reglas necesarias hayan sido añadidas. El conjunto de reglas se vuelve de solo lectura. El análisis léxico puede comenzar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
