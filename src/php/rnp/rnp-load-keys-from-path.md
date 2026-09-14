---
title: rnp_load_keys_from_path
description: Carga claves a partir de la ruta especificada
source_url: https://www.php.net/manual/es/function.rnp-load-keys-from-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-load-keys-from-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72250
---

rnp_load_keys_from_path

Carga claves a partir de la ruta especificada

## Descripción

```php
rnp_load_keys_from_path(RnpFFI $ffi, string $format, string $input_path, int $flags): bool
```php

Es importante señalar que para G10, la entrada debe ser un directorio (que ya debe existir).

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`format`  
El formato de clave para los datos (GPG, KBX, G10).

`input_path`  
El fichero o directorio que contiene las claves.

`flags`  
Ver la descripción de los flags `RNP_LOAD_SAVE_*`.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` si ocurre un error.
