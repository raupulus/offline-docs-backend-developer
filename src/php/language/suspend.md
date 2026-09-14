---
title: Fiber::suspend
description: Suspende la ejecución de la fibra actual
source_url: https://www.php.net/manual/es/fiber.suspend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/suspend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3500
---

Fiber::suspend

Suspende la ejecución de la fibra actual

## Descripción

```php
public static Fiber::suspend([mixed $value]): mixed
```php

Suspende la ejecución de la fibra actual. El valor proporcionado a este método será devuelto por la llamada a Fiber::start, Fiber::resume, o Fiber::throw que hizo cambiar la ejecución a la fibra actual.

Cuando la fibra se reanuda, este método devuelve el valor proporcionado a Fiber::resume. Si la fibra se reanuda utilizando Fiber::throw, la excepción dada a este método será emitida al llamar a este método.

Si este método es llamado desde fuera de una fibra, una `FiberError` será emitida.

## Parámetros

`value`  
El valor a devolver de la llamada a Fiber::start, Fiber::resume, o Fiber::throw que hizo cambiar la ejecución a la fibra actual.

## Valores devueltos

El valor proporcionado a Fiber::resume.
