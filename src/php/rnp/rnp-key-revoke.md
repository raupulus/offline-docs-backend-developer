---
title: rnp_key_revoke
description: Elimina una clave o una subclave generando y añadiendo una firma de revocación
source_url: https://www.php.net/manual/es/function.rnp-key-revoke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-key-revoke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72230
---

rnp_key_revoke

Elimina una clave o una subclave generando y añadiendo una firma de revocación

## Descripción

```php
rnp_key_revoke(RnpFFI $ffi, string $key_fp, int $flags, [array $options]): bool
```php

Nota: es necesario llamar a `rnp_save_keys` para escribir los ficheros de claves actualizados.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`key_fp`  
La huella de la clave.

`flags`  
Actualmente debe ser 0.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de datos | Descripción |
|----|----|----|
| `"hash"` | string | Define el algoritmo de hash utilizado durante el cálculo de la firma. |
| `"code"` | string | El código de revocación de la clave. Los valores posibles son 'no', 'superseded', 'compromised', 'retired'. Si no se define, se utilizará el valor 'no' por omisión. |
| `"reason"` | string | Representación textual de la razón de la revocación. |

## Valores devueltos

Devuelve `true` en caso de éxito o `false` si ocurre un error.
