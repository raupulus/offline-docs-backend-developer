---
title: LuaSandbox::loadString
description: Carga código Lua en el entorno Lua
source_url: https://www.php.net/manual/es/luasandbox.loadstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/loadstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44000
---

LuaSandbox::loadString

Carga código Lua en el entorno Lua

## Descripción

```php
public LuaSandbox::loadString(string $code, [string $chunkName]): LuaSandboxFunction
```php

Carga código Lua en el entorno Lua.

Esto es equivalente a la función `loadstring()` de Lua estándar.

## Parámetros

`code`  
El código Lua.

`chunkName`  
El nombre del fragmento cargado, para su uso en los rastros de error.

## Valores devueltos

Devuelve una `LuaSandboxFunction` que, al ejecutarse, ejecutará el `$code` pasado.

## Ejemplos

Carga de código en Lua

```
<?php

// Crear un nuevo LuaSandbox
$sandbox = new LuaSandbox();

// Carga el código
$function = $sandbox->loadString(
<<<CODE
    return "Hello, world"
CODE
);

// Ejecuta el código cargado
var_dump( $function->call() );

?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      string(12) "Hello, world"
    }

## Véase también

LuaSandbox::registerLibrary

LuaSandbox::wrapPhpFunction
