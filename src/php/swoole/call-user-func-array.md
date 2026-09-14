---
title: Swoole\Coroutine::call_user_func_array
description: Llama a una función de retrollamada con un array de argumentos
source_url: https://www.php.net/manual/es/swoole-coroutine.call-user-func-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/coroutine/call-user-func-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 322606e4f
order: 91240
---

Swoole\Coroutine::call_user_func_array

Llama a una función de retrollamada con un array de argumentos

## Descripción

```php
public static Swoole\Coroutine::call_user_func_array(callable $callback, array $param_array): mixed
```php

Llama a la función de retrollamada dada por el primer argumento con los argumentos en param_array.

## Parámetros

`callback`  
El `callable` a llamar.

`param_array`  
Cero o más argumentos en el array a pasar a la función de retrollamada.

## Valores devueltos
