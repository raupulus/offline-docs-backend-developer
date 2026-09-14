---
title: rnp_key_remove
description: Elimina una clave de los llaveros
source_url: https://www.php.net/manual/es/function.rnp-key-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-key-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72220
---

rnp_key_remove

Elimina una clave de los llaveros

## Descripción

```php
rnp_key_remove(RnpFFI $ffi, string $key_fp, int $flags): bool
```php

Nota: es necesario llamar a `rnp_save_keys` para escribir los llaveros actualizados.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`key_fp`  
La huella de la clave.

`flags`  
Ver `RNP_KEY_REMOVE_*` constantes predefinidas. El flag `RNP_KEY_REMOVE_SUBKEYS` solo funcionará para la clave principal y eliminará también todas sus subclaves.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` si ocurre un error.
