---
title: rnp_import_signatures
description: Importa firmas autónomas en el llavero de claves y devuelve un JSON que
  describe las claves actualizadas
source_url: https://www.php.net/manual/es/function.rnp-import-signatures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-import-signatures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72170
---

rnp_import_signatures

Importa firmas autónomas en el llavero de claves y devuelve un JSON que describe las claves actualizadas

## Descripción

```php
rnp_import_signatures(RnpFFI $ffi, string $input, int $flags): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`input`  
Los paquetes OpenPGP que contienen las firmas a importar. Puede ser binario o ASCII armado.

`flags`  
Actualmente debe ser 0.

## Valores devueltos

La cadena JSON con información sobre las claves actualizadas en caso de éxito o `false` si ocurre un error.
