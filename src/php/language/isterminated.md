---
title: Fiber::isTerminated
description: Determina si la fibra ha terminado
source_url: https://www.php.net/manual/es/fiber.isterminated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/isterminated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3470
---

Fiber::isTerminated

Determina si la fibra ha terminado

## Descripción

```php
public Fiber::isTerminated(): bool
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` solo después de que la fibra haya terminado, ya sea devolviendo o lanzando una excepción; de lo contrario, se devuelve `false`.
