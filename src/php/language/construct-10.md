---
title: Fiber::__construct
description: Crea una nueva instancia de Fibra
source_url: https://www.php.net/manual/es/fiber.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3410
---

Fiber::\_\_construct

Crea una nueva instancia de Fibra

## Descripción

```php
public Fiber::__construct(callable $callback)
```php

## Parámetros

`callback`  
El `callable` a invocar al iniciar la fibra. Los argumentos dados a Fiber::start serán proporcionados como argumentos a la función dada.
