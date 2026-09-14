---
title: rnp_save_keys_to_path
description: Guarda las claves en la ruta especificada
source_url: https://www.php.net/manual/es/function.rnp-save-keys-to-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-save-keys-to-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72350
---

rnp_save_keys_to_path

Guarda las claves en la ruta especificada

## Descripción

```php
rnp_save_keys_to_path(RnpFFI $ffi, string $format, string $output_path, int $flags): bool
```php

Guarda las claves presentes en el objeto FFI (cargadas o generadas) en el fichero o directorio especificado.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`format`  
El formato de clave para los datos (GPG, KBX, G10).

`output_path`  
La ruta del fichero o directorio donde las claves deben ser guardadas.

`flags`  
Ver la descripción de los flags `RNP_LOAD_SAVE_*`.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` si ocurre un error.
