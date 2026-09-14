---
title: rnp_decrypt
description: Desencripta un mensaje PGP
source_url: https://www.php.net/manual/es/function.rnp-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72100
---

rnp_decrypt

Desencripta un mensaje PGP

## Descripción

```php
rnp_decrypt(RnpFFI $ffi, string $input): string
```php

Las claves privadas utilizadas para el desencriptado deben ser cargadas en el objeto FFI antes de llamar a esta función. Si se ha utilizado el cifrado por contraseña, el proveedor de contraseña debe ser definido llamando a `rnp_ffi_set_pass_provider`.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`input`  
El mensaje cifrado.

## Valores devueltos

El mensaje desencriptado en caso de éxito o `false` si ocurre un error.
