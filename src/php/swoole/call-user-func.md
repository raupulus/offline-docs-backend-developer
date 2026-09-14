---
title: Swoole\Coroutine::call_user_func
description: Llama a una función de retrollamada dada por el primer argumento
source_url: https://www.php.net/manual/es/swoole-coroutine.call-user-func.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/coroutine/call-user-func.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 91250
---

Swoole\Coroutine::call_user_func

Llama a una función de retrollamada dada por el primer argumento

## Descripción

```php
public static Swoole\Coroutine::call_user_func(callable $callback, mixed ...$args): mixed
```php

Llama al `callback` dado por el primer argumento y pasa los argumentos restantes como argumentos.

## Parámetros

`callback`  
El `callable` a llamar.

`args`  
Cero o más argumentos a pasar a la función de retrollamada.

## Valores devueltos
