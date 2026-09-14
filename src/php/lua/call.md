---
title: Lua::call
description: Llama funciones de Lua
source_url: https://www.php.net/manual/es/lua.call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lua/lua/call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lua
translation_status: ready
translation_revision: 64ae8f745
order: 43770
---

Lua::call

Lua::\_\_call

Llama funciones de Lua

## Descripción

```php
public Lua::call(callable $lua_func, [array $args], [int $use_self]): mixed
```php

```php
public Lua::__call(callable $lua_func, [array $args], [int $use_self]): mixed
```

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`lua_func`  
Nombre de la función en Lua

`args`  
Argumentos pasados a la función de Lua

`use_self`  
Cuando se debe usar `self`

## Valores devueltos

Devuelve el resultado de la función llamada, `null` si los argumentos son inválidos o `false` en caso de error.

## Ejemplos

Ejemplo de la función `Lua::call`

```php
<?php
$lua = new Lua();
$lua->eval(<<<CODE
  function dummy(foo, bar)
    print(foo, ",", bar)
  end
CODE
);
$lua->call("dummy", array("Lua", "geiliable\n"));
var_dump($lua->call(array("table", "concat"), array(array(1=>1, 2=>2, 3=>3), "-")));
?>

   
```

Resultado del ejemplo anterior es similar a:

    Lua,geiliable
    string(5) "1-2-3"

## Véase también

Lua::\_\_call
