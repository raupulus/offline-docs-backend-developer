---
title: rnp_list_keys
description: Enumera todas las claves presentes en un llavero de claves por tipo de
  identificador especificado
source_url: https://www.php.net/manual/es/function.rnp-list-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-list-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72240
---

rnp_list_keys

Enumera todas las claves presentes en un llavero de claves por tipo de identificador especificado

## Descripción

```php
rnp_list_keys(RnpFFI $ffi, string $identifier_type): array
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`identifier_type`  
La clave de tipo de identificador ("userid", "keyid", "grip", "fingerprint").

## Valores devueltos

Un array asociativo donde la clave es un string de identificador y el valor es una huella de clave PGP o `false` si ocurre un error.
