---
title: LuaSandbox::getVersionInfo
description: Devuelve las versiones de LuaSandbox y Lua
source_url: https://www.php.net/manual/es/luasandbox.getversioninfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/getversioninfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43980
---

LuaSandbox::getVersionInfo

Devuelve las versiones de LuaSandbox y Lua

## Descripción

```php
public static LuaSandbox::getVersionInfo(): array
```php

Devuelve las versiones de LuaSandbox y Lua.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con dos claves:

| elemento | tipo | descripción |
|----|----|----|
| LuaSandbox | `string` | La versión de la extensión LuaSandbox. |
| Lua | `string` | El nombre y la versión de la biblioteca Lua, tal como se define por la macro LUA_RELEASE, por ejemplo, "Lua 5.1.5". |
