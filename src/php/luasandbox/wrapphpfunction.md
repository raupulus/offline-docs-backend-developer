---
title: LuaSandbox::wrapPhpFunction
description: Envuelve una función PHP en una LuaSandboxFunction
source_url: https://www.php.net/manual/es/luasandbox.wrapphpfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/wrapphpfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44060
---

LuaSandbox::wrapPhpFunction

Envuelve una función PHP en una

LuaSandboxFunction

## Descripción

```php
public LuaSandbox::wrapPhpFunction(callable $function): LuaSandboxFunction
```php

Envuelve una función PHP en una `LuaSandboxFunction`, de modo que pueda ser pasada a Lua como una función anónima.

La función debe devolver un array de valores (que puede estar vacío), o `null` que es equivalente a devolver el array vacío.

Las excepciones serán lanzadas como errores en Lua, sin embargo, solo las excepciones `LuaSandboxRuntimeError` pueden ser capturadas dentro de Lua con `pcall()` o `xpcall()`.

Para más información sobre la llamada de funciones Lua y los valores de retorno, ver LuaSandboxFunction::call.

## Parámetros

`function`  
La función de retrollamada a envolver.

## Valores devueltos

Devuelve un `LuaSandboxFunction`.

## Véase también

LuaSandbox::loadString

LuaSandbox::registerLibrary
