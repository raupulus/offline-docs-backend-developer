---
title: rnp_key_get_info
description: Devuelve información sobre la clave
source_url: https://www.php.net/manual/es/function.rnp-key-get-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-key-get-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72210
---

rnp_key_get_info

Devuelve información sobre la clave

## Descripción

```php
rnp_key_get_info(RnpFFI $ffi, string $key_fp): array
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`key_fp`  
La huella de la clave.

## Valores devueltos

Un array asociativo con información sobre la clave o `false` si ocurre un error.

| Clave | Tipo de datos | Descripción |
|----|----|----|
| `"is_primary"` | boolean | `true` si esta clave es la clave primaria. |
| `"is_sub"` | boolean | `true` si esta clave es una subclave. |
| `"is_valid"` | boolean | `true` si la clave pública es válida. Esto incluye las verificaciones de auto-firmas, las fechas de expiración, las revocaciones, etc. |
| `"is_revoked"` | boolean | `true` si esta clave está revocada. |
| `"is_superseded"` | boolean | `true` si esta clave está obsoleta. Presente solo si la clave está revocada. |
| `"is_compromised"` | boolean | `true` si esta clave está comprometida. Presente solo si la clave está revocada. |
| `"is_retired"` | boolean | `true` si esta clave está retirada. Presente solo si la clave está revocada. |
| `"is_expired"` | boolean | `true` si esta clave está expirada. |
| `"have_secret"` | boolean | `true` si esta clave tiene una parte secreta. |
| `"is_locked"` | boolean | `true` si esta clave está actualmente bloqueada. Presente solo para claves secretas. |
| `"is_protected"` | boolean | `true` si esta clave está protegida. Presente solo para claves secretas. Una clave protegida es una clave que está cifrada y puede ser almacenada de manera segura en memoria y bloqueada/desbloqueada según sea necesario. |
| `"have_public"` | boolean | `true` si esta clave tiene una parte pública. En general, todas las claves tienen una parte pública. |
| `"valid_till"` | integer | El timestamp hasta el cual la clave puede ser considerada válida. Nota: esto tendrá en cuenta no solo la expiración de la clave, sino también las revocaciones. Para la subclave primaria, el tiempo de validez de la clave pública también será verificado. |
| `"bits"` | integer | El número de bits en la clave. Para las claves basadas en EC, esto contendrá el tamaño de la curva. |
| `"alg"` | string | El algoritmo de nombre de clave. |
| `"subkeys"` | array | Un array indexado que contiene información sobre las subclaves. Puede estar vacío si la clave primaria no tiene subclaves. |
| `"uids"` | array | Un array indexado que contiene información sobre los identificadores de usuario. Puede estar vacío si la clave primaria no tiene identificadores de usuario. |
