---
title: rnp_import_keys
description: Importa claves desde una string PHP hacia el llavero de claves y devuelve
  un JSON describiendo las claves nuevas o actualizadas
source_url: https://www.php.net/manual/es/function.rnp-import-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-import-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72160
---

rnp_import_keys

Importa claves desde una string PHP hacia el llavero de claves y devuelve un JSON describiendo las claves nuevas o actualizadas

## Descripción

```php
rnp_import_keys(RnpFFI $ffi, string $input, int $flags): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`input`  
Los paquetes OpenPGP que contienen la o las claves a cargar. Puede ser binario o ASCII armored.

`flags`  
Ver las constantes predefinidas `RNP_LOAD_SAVE_*`.

## Valores devueltos

Una string JSON con la información sobre las claves nuevas y actualizadas en caso de éxito o `false` si ocurre un error.
