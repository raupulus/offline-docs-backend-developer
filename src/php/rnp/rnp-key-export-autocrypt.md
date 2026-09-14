---
title: rnp_key_export_autocrypt
description: 'Exporta la clave mínima para la funcionalidad autocrypt (solo 5 paquetes:
  clave, uid, firma, subclave de cifrado, firma)'
source_url: https://www.php.net/manual/es/function.rnp-key-export-autocrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-key-export-autocrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72180
---

rnp_key_export_autocrypt

Exporta la clave mínima para la funcionalidad autocrypt (solo 5 paquetes: clave, uid, firma, subclave de cifrado, firma)

## Descripción

```php
rnp_key_export_autocrypt(RnpFFI $ffi, string $key_fp, string $subkey_fp, string $uid, int $flags): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`key_fp`  
La huella de la clave primaria.

`subkey_fp`  
La subclave a exportar. Puede ser una string vacía para elegir la primera subclave apropiada.

`uid`  
El identificador del usuario a exportar. Puede ser una string vacía si la clave exportada solo tiene un identificador.

`flags`  
Solo `RNP_KEY_EXPORT_BASE64` es actualmente soportado. Activarlo exportará los datos de la clave codificados en base64 en lugar de binario.

## Valores devueltos

Los paquetes OpenPGP de la clave exportada en caso de éxito o `false` si ocurre un error.
