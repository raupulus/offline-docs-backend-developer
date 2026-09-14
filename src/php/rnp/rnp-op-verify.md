---
title: rnp_op_verify
description: Verifica las firmas integradas o en claro
source_url: https://www.php.net/manual/es/function.rnp-op-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-op-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72340
---

rnp_op_verify

Verifica las firmas integradas o en claro

## Descripción

```php
rnp_op_verify(RnpFFI $ffi, string $data): array
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`data`  
Los datos firmados.

## Valores devueltos

Un array asociativo con información sobre los resultados de la verificación o `false` si ocurre un error.

| Clave | Tipo de datos | Descripción |
|----|----|----|
| `"verification_status"` | string | Resultados de la verificación global, ya sea la cadena "Success" o un mensaje de error apropiado. El resultado "Success" se define cuando al menos una firma es válida y se verifica con éxito. El resultado de la verificación individual para cada firma puede ser verificado en el array "signatures". |
| `"file_name"` | string | El nombre del fichero. |
| `"file_mtime"` | integer | Hora de modificación del fichero. |
| `"mode"` | string | Modo de protección de los datos (cifrado) utilizado en el mensaje procesado. Los valores actualmente definidos son "none", "cfb", "cfb-mdc", "aead-ocb", "aead-eax". |
| `"cipher"` | string | Cifrado simétrico utilizado para el cifrado de los datos. |
| `"valid_integrity"` | boolean | `true` si la protección de la integridad del mensaje ha sido utilizada (es decir, MDC o AEAD) y ha sido validada con éxito. |
| `"signatures"` | array | Un array asociativo que describe cada firma encontrada. Ver la descripción a continuación. |

El subarray "signatures".

| Clave | Tipo de datos | Descripción |
|----|----|----|
| "verification_status" | string | Estado de verificación de la firma, ya sea la cadena "Success" o un mensaje de error apropiado. |
| "creation_time" | integer | Hora de creación de la firma en segundos desde el 1 de enero de 1970 UTC. |
| "expiration_time" | integer | El tiempo de expiración de la firma en segundos desde el tiempo de creación o 0 si la firma no expira nunca. |
| "hash" | string | Algoritmo de hash utilizado para calcular la firma. |
| "signing_key" | string | La huella de la clave utilizada para firmar. Puede ser "Not found" si la clave pública correspondiente no está cargada en el objeto FFI. |
| "signature_type" | string | El tipo de firma. Los valores actualmente definidos son "binary", "text", "standalone", "certification (generic)", "certification (persona)", "certification (casual)", "certification (positive)", "subkey binding", "primary key binding", "direct", "key revocation", "subkey revocation", "certification revocation", "timestamp", "uknown: 0..255". |
