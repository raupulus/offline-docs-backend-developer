---
title: rnp_op_sign
description: Realiza una operación de firma sobre datos binarios, devuelve la o las
  firmas integradas
source_url: https://www.php.net/manual/es/function.rnp-op-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-op-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72320
---

rnp_op_sign

Realiza una operación de firma sobre datos binarios, devuelve la o las firmas integradas

## Descripción

```php
rnp_op_sign(RnpFFI $ffi, string $data, array $keys_fp, [array $options]): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`data`  
Datos a firmar.

`keys_fp`  
Un array con las huellas de las claves. Al menos una clave debe ser proporcionada. Las claves deben estar presentes en `ffi`.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de datos | Descripción |
|----|----|----|
| `"compression_alg"` | string | Algoritmo de compresión. Las opciones `"compression_alg"` y `"compression_level"` deben ser ambas definidas para activar la compresión de datos. |
| `"compression_level"` | integer | Nivel de compresión, 0-9. 0 desactiva la compresión. |
| `"armor"` | boolean | Activa la salida ASCII armada. Desactivado por omisión. |
| `"hash"` | string | Define el algoritmo de hash utilizado en el cálculo de la firma. |
| `"creation_time"` | integer | Define la hora de creación de la firma en segundos desde el 1 de enero de 1970 UTC. Por omisión, se utiliza la hora actual. |
| `"expiration_time"` | integer | Define el tiempo de expiración de la firma en segundos desde la hora de creación. El valor 0 se utiliza para marcar la firma como no expirante (valor por omisión). |
| `"file_name"` | string | Define el nombre del fichero de entrada. El valor especial \_CONSOLE puede ser utilizado para marcar el mensaje como 'para sus ojos solamente', es decir, que no debe ser almacenado en ningún lugar sino solo mostrado al destinatario. Por omisión, es una cadena vacía. |
| `"file_mtime"` | integer | Define la fecha de modificación del fichero de entrada en segundos desde el 1 de enero de 1970 UTC. |

## Valores devueltos

Los datos firmados con la(s) firma(s) integrada en caso de éxito o `false` si ocurre un error.
