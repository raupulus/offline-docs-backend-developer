---
title: Lua::eval
description: Evalúa una cadena de texto como código Lua
source_url: https://www.php.net/manual/es/lua.eval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/lua/lua/eval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: lua
translation_status: ready
translation_revision: 64ae8f745
order: 43790
---

Lua::eval

Evalúa una cadena de texto como código Lua

## Descripción

```php
public Lua::eval(string $statements): mixed
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`statements`  

## Valores devueltos

Devuelve el resultado del código evaluado, `null` si los parámetros son inválidos o `false` en caseo de error.

## Ejemplos

Ejemplo de la función `Lua::eval`

```
<?php
    $lua = new Lua();
    $lua->eval(<<<CODE
     print(2);
CODE
);
?>

   
```php

El ejemplo anterior mostrará:

    2
