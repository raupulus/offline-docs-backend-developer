---
title: FFI::scope
description: Instancia un objeto FFI con las declaraciones C analizadas durante la
  precarga
source_url: https://www.php.net/manual/es/ffi.scope.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/scope.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23010
---

FFI::scope

Instancia un objeto FFI con las declaraciones C analizadas durante la precarga

## Descripción

```php
public static FFI::scope(string $name): FFI
```php

Instancia un objeto FFI con las declaraciones C analizadas durante la precarga.

El método FFI::scope puede ser llamado varias veces para el mismo ámbito. Varias referencias al mismo ámbito pueden ser cargadas al mismo tiempo.

## Parámetros

`name`  
El nombre del ámbito definido por una definición especial `FFI_SCOPE`.

## Valores devueltos

Devuelve el objeto `FFI` recién creado.

## Véase también

FFI::load
