---
title: register_tick_function
description: Registra una función ejecutada en cada tick
source_url: https://www.php.net/manual/es/function.register-tick-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/register-tick-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: true
translation_revision: 689cf3b5a
order: 24830
---

register_tick_function

Registra una función ejecutada en cada tick

## Descripción

```php
register_tick_function(callable $callback, mixed ...$args): bool
```php

`register_tick_function` registra la función `callback` para ser ejecutada cada vez que ocurre un [tick](#control-structures.declare.ticks).

## Parámetros

`callback`  
La función a registrar.

`args`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `register_tick_function`

```
<?php
declare(ticks=1);

function my_tick_function($param) {
    echo "Función de retorno tick llamada con el parámetro: $param\n";
}

register_tick_function('my_tick_function', true);
?>

    
```php

## Véase también

[declare](#control-structures.declare), `unregister_tick_function`
