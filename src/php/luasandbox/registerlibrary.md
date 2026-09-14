---
title: LuaSandbox::registerLibrary
description: Registra un conjunto de funciones PHP como una biblioteca Lua
source_url: https://www.php.net/manual/es/luasandbox.registerlibrary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/registerlibrary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44020
---

LuaSandbox::registerLibrary

Registra un conjunto de funciones PHP como una biblioteca Lua

## Descripción

```php
public LuaSandbox::registerLibrary(string $libname, array $functions): void
```php

Registra un conjunto de funciones PHP como una biblioteca Lua, de modo que Lua pueda llamar al código PHP correspondiente.

Para más información sobre la llamada de funciones Lua y los valores de retorno, ver LuaSandboxFunction::call.

## Parámetros

`libname`  
El nombre de la biblioteca. En el estado Lua, la variable global de este nombre se definirá en la tabla de funciones. Si la tabla ya existe, las nuevas funciones se añadirán a ella.

`functions`  
Un `array`, donde cada clave es un nombre de función, y cada valor es un `callable` PHP correspondiente.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Registro de funciones PHP para ser llamadas desde Lua

```
<?php

// crear un nuevo LuaSandbox
$sandbox = new LuaSandbox();

// Registrar algunas funciones en el entorno Lua

function frobnosticate( $v ) {
    return [ $v + 42 ];
}

$sandbox->registerLibrary( 'php', [
    'frobnosticate' => 'frobnosticate',
    'output' => function ( $string ) {
        echo "$string\n";
    },
    'error' => function () {
        throw new LuaSandboxRuntimeError( "Something is wrong" );
    }
] );

?>

   
```php

## Véase también

LuaSandbox::loadString

LuaSandbox::wrapPhpFunction
