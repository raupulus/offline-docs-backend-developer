---
title: rnp_load_keys
description: Carga las claves a partir de un string PHP
source_url: https://www.php.net/manual/es/function.rnp-load-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-load-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72260
---

rnp_load_keys

Carga las claves a partir de un string PHP

## Descripción

```php
rnp_load_keys(RnpFFI $ffi, string $format, string $input, int $flags): bool
```php

Se debe tener en cuenta que para G10, la entrada debe ser un directorio (que ya debe existir).

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`format`  
El formato de clave para los datos (GPG, KBX, G10).

`input`  
Los paquetes OpenPGP que contienen la o las claves a cargar. Puede ser binario o ASCII armored.

`flags`  
Ver la descripción de los flags `RNP_LOAD_SAVE_*`.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` si ocurre un error
