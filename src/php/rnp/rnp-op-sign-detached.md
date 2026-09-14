---
title: rnp_op_sign_detached
description: Realiza una operación de firma, devuelve la firma desvinculada
source_url: https://www.php.net/manual/es/function.rnp-op-sign-detached.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-op-sign-detached.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72310
---

rnp_op_sign_detached

Realiza una operación de firma, devuelve la firma desvinculada

## Descripción

```php
rnp_op_sign_detached(RnpFFI $ffi, string $data, array $keys_fp, [array $options]): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`data`  
Los datos a firmar.

`keys_fp`  
Un array con las huellas de las claves. Al menos una clave debe ser proporcionada. Las claves deben estar presentes en `ffi`.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de dato | Descripción |
|----|----|----|
| `"armor"` | boolean | Activa la salida ASCII-armored. Desactivado por omisión. |
| `"hash"` | string | Define el algoritmo de hash utilizado durante el cálculo de la firma. |
| `"creation_time"` | integer | Define la hora de creación de la firma en segundos desde el 1 de enero de 1970 UTC. Por omisión, se utiliza la hora actual. |
| `"expiration_time"` | integer | Define el tiempo de expiración de la firma en segundos desde la hora de creación. El valor 0 se utiliza para marcar la firma como no expirada (valor por omisión). |

## Valores devueltos

Los datos de firma(s) desvinculados en caso de éxito o `false` si ocurre un error.
