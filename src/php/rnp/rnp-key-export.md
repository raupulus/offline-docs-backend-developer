---
title: rnp_key_export
description: Exporta una clave
source_url: https://www.php.net/manual/es/function.rnp-key-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-key-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72200
---

rnp_key_export

Exporta una clave

## Descripción

```php
rnp_key_export(RnpFFI $ffi, string $key_fp, int $flags): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`key_fp`  
La huella de la clave.

`flags`  
Ver `RNP_KEY_EXPORT_*` constantes predefinidas (excepto `RNP_KEY_EXPORT_BASE64`).

## Valores devueltos

El paquete OpenPGP exportado de la clave (binario o ASCII-armored) en caso de éxito o `false` si ocurre un error.
