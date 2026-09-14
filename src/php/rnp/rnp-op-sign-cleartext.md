---
title: rnp_op_sign_cleartext
description: Realiza una operación de firma sobre datos textuales, devuelve el mensaje
  firmado en claro
source_url: https://www.php.net/manual/es/function.rnp-op-sign-cleartext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-op-sign-cleartext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72300
---

rnp_op_sign_cleartext

Realiza una operación de firma sobre datos textuales, devuelve el mensaje firmado en claro

## Descripción

```php
rnp_op_sign_cleartext(RnpFFI $ffi, string $data, array $keys_fp, [array $options]): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`data`  
Los datos a firmar.

`keys_fp`  
El array con las huellas de las claves. Al menos una clave debe ser proporcionada. Las claves deben estar presentes en `ffi`.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de dato | Descripción |
|----|----|----|
| `"armor"` | boolean | Activa la salida ASCII armada. Desactivado por omisión. |
| `"hash"` | string | Define el algoritmo de hash utilizado durante el cálculo de la firma. |
| `"creation_time"` | integer | Define la hora de creación de la firma en segundos desde el 1 de enero de 1970 UTC. Por omisión, se utiliza la hora actual. |
| `"expiration_time"` | integer | Define el tiempo de expiración de la firma en segundos desde la hora de creación. El valor 0 se utiliza para marcar la firma como no expirada (valor por omisión). |

## Valores devueltos

El mensaje firmado en claro que contiene los datos fuente con encabezados adicionales y la firma ASCII-armored en caso de éxito o `false` si ocurre un error.
