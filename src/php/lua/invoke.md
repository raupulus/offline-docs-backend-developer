---
title: LuaClosure::__invoke
description: Invoca el luaclosure
source_url: https://www.php.net/manual/es/luaclosure.invoke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lua/luaclosure/invoke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lua
translation_status: ready
translation_reviewed: false
translation_revision: 64ae8f745
order: 43840
---

LuaClosure::\_\_invoke

Invoca el luaclosure

## Descripción

```php
public LuaClosure::__invoke(mixed ...$args): void
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`args`  

## Valores devueltos

## Ejemplos

Ejemplo de `LuaClosure::__invoke`

```
<?php
$lua = new Lua();
$closure = $lua->eval(<<<CODE
    return (function ()
        print("hello world")
    end)
CODE
);

$lua->call($closure);
$closure();
?>

   
```php

El ejemplo anterior mostrará:

    hello worldhello world
