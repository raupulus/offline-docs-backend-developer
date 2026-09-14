---
title: rnp_locate_key
description: Búsqueda de la clave
source_url: https://www.php.net/manual/es/function.rnp-locate-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-locate-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72270
---

rnp_locate_key

Búsqueda de la clave

## Descripción

```php
rnp_locate_key(RnpFFI $ffi, string $identifier_type, string $identifier): string
```php

Nota: los identificadores válidos se verifican durante la búsqueda por identificador.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`identifier_type`  
Cadena de tipo de identificador: "userid", "keyid", "fingerprint", "grip".

`identifier`  
El identificador del usuario OpenPGP (nombre y correo electrónico) para el tipo "userid", cadena hexadecimal que representa el identificador de clave, la huella digital o el grip de clave correspondiente.

## Valores devueltos

Devuelve la huella digital hexadecimal de la clave encontrada en caso de éxito o `false` si ocurre un error.
