---
title: FFI::type
description: Crea un objeto FFI\CType a partir de una declaración C
source_url: https://www.php.net/manual/es/ffi.type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23040
---

FFI::type

Crea un objeto FFI\CType a partir de una declaración C

## Descripción

```php
public FFI::type(string $type): FFI\CType
```php

Esta función crea y devuelve un objeto `FFI\CType` para el `string` dado que contiene una declaración de tipo C. Cualquier tipo declarado para la instancia está permitido.

## Parámetros

`type`  
Una declaración C válida como `string`.

## Valores devueltos

Devuelve el objeto `FFI\CType` recién creado, o `null` en caso de fallo.

## Historial de cambios

| Versión | Descripción                                           |
|---------|-------------------------------------------------------|
| 8.3.0   | La llamada estática de FFI::type está ahora obsoleta. |
