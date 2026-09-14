---
title: LuaSandbox::loadBinary
description: Carga un fragmento binario precompilado en el entorno Lua
source_url: https://www.php.net/manual/es/luasandbox.loadbinary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/loadbinary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43990
---

LuaSandbox::loadBinary

Carga un fragmento binario precompilado en el entorno Lua

## Descripción

```php
public LuaSandbox::loadBinary(string $code, [string $chunkName]): LuaSandboxFunction
```php

Carga los datos generados por LuaSandboxFunction::dump.

## Parámetros

`code`  
Los datos de LuaSandboxFunction::dump.

`chunkName`  
El nombre del fragmento para la función cargada.

## Valores devueltos

Devuelve una `LuaSandboxFunction`.

## Véase también

LuaSandbox::loadString
