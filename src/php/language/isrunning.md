---
title: Fiber::isRunning
description: Determina si la fibra está en ejecución
source_url: https://www.php.net/manual/es/fiber.isrunning.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/isrunning.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 3440
---

Fiber::isRunning

Determina si la fibra está en ejecución

## Descripción

```php
public Fiber::isRunning(): bool
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` solo si la fibra está en ejecución. Una fibra se considera en ejecución después de una llamada a Fiber::start, Fiber::resume, o Fiber::throw que aún no ha retornado. Devuelve `false` si la fibra no está en ejecución.
