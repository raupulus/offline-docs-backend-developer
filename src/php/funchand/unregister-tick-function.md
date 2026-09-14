---
title: unregister_tick_function
description: Anula la función ejecutada en cada tick
source_url: https://www.php.net/manual/es/function.unregister-tick-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/unregister-tick-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: false
translation_revision: 1e40469ac
order: 24840
---

unregister_tick_function

Anula la función ejecutada en cada tick

## Descripción

```php
unregister_tick_function(callable $callback): void
```php

Anula la ejecución automática de `callback` en cada [tick](#control-structures.declare).

## Parámetros

`callback`  
La función a anular.

## Valores devueltos

No se retorna ningún valor.

## Véase también

`register_tick_function`
