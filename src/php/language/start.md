---
title: Fiber::start
description: Inicia la ejecución de la fibra
source_url: https://www.php.net/manual/es/fiber.start.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/start.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3490
---

Fiber::start

Inicia la ejecución de la fibra

## Descripción

```php
public Fiber::start(mixed ...$args): mixed
```php

Una lista variádica de argumentos a proporcionar a la función utilizada durante la construcción de la fibra.

Si la fibra ya ha sido iniciada cuando se llama a este método, se emitirá un error `FiberError`.

## Parámetros

`args`  
Los argumentos a utilizar durante la invocación de la función dada al constructor de la fibra.

## Valores devueltos

El valor proporcionado a la primera llamada a Fiber::suspend o `null` si la fibra retorna. Si la fibra lanza una excepción antes de suspenderse, será emitida durante la llamada a este método.
