---
title: rnp_key_export_revocation
description: Genera y exporta una firma de revocación de clave primaria
source_url: https://www.php.net/manual/es/function.rnp-key-export-revocation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-key-export-revocation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72190
---

rnp_key_export_revocation

Genera y exporta una firma de revocación de clave primaria

## Descripción

```php
rnp_key_export_revocation(RnpFFI $ffi, string $key_fp, int $flags, [array $options]): string
```php

Notas: para revocar una clave, será necesario importar esta firma en el llavero de claves o utilizar la función `rnp_key_revoke`.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`key_fp`  
La huella de la clave primaria a revocar.

`flags`  
`RNP_KEY_EXPORT_ARMORED` o 0.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de datos | Descripción |
|----|----|----|
| `"hash"` | string | Define el algoritmo de hash utilizado en el cálculo de la firma. |
| `"code"` | string | Código de razón de la revocación. Valores posibles: 'no', 'superseded', 'compromised', 'retired'. Si no se define, se utilizará el valor 'no' por omisión. |
| `"reason"` | string | Representación textual de la razón de la revocación. |

## Valores devueltos

Revocación exportada en caso de éxito o `false` si ocurre un error.
