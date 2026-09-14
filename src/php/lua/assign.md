---
title: Lua::assign
description: Asigna una variable de PHP a Lua
source_url: https://www.php.net/manual/es/lua.assign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lua/lua/assign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lua
translation_status: ready
translation_reviewed: false
translation_revision: 64ae8f745
order: 43760
---

Lua::assign

Asigna una variable de PHP a Lua

## Descripción

```php
public Lua::assign(string $name, string $value): mixed
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`name`  

`value`  

## Valores devueltos

Devuelve `$this` o `null` en caso de error.

## Ejemplos

Ejemplo de `Lua::assign`

```
<?php
$lua = new Lua();
$lua->assign("php_var", array(1=>1, 2, 3)); //índice de la tabla empieza en 1
$lua->eval(<<<CODE
    print(php_var);
CODE
);
?>

   
```php

El ejemplo anterior mostrará:

    Array
     (
         [1] => 1
         [2] => 2
         [3] => 3
     )
