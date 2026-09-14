---
title: LuaSandbox::callFunction
description: Llama a una función en una variable global Lua
source_url: https://www.php.net/manual/es/luasandbox.callfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/callfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43910
---

LuaSandbox::callFunction

Llama a una función en una variable global Lua

## Descripción

```php
public LuaSandbox::callFunction(string $name, mixed ...$args): array
```php

Llama a una función en una variable global Lua.

Si el nombre contiene caracteres ".", la función se localiza a través de accesos recursivos a la tabla, como si el nombre fuera una expresión Lua.

Si la variable no existe, o no es una función, se devolverá false y se emitirá un aviso.

Para más información sobre la llamada de funciones Lua y los valores de retorno, ver LuaSandboxFunction::call.

## Parámetros

`name`  
Nombre de la variable Lua.

`args`  
Argumentos de la función.

## Valores devueltos

Devuelve un `array` de los valores devueltos por la función Lua, que puede estar vacío, o `false` si ocurre un error.

## Ejemplos

Llamada a una función Lua

```
<?php

// crear un nuevo LuaSandbox
$sandbox = new LuaSandbox();

// Llamar a la función Lua string.match
$captures = $sandbox->callFunction( 'string.match', $string, $pattern );

?>

   
```php
