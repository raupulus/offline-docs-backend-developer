---
title: rnp_op_encrypt
description: Cifra un mensaje
source_url: https://www.php.net/manual/es/function.rnp-op-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-op-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72280
---

rnp_op_encrypt

Cifra un mensaje

## Descripción

```php
rnp_op_encrypt(RnpFFI $ffi, string $message, array $recipient_keys_fp, [array $options]): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`message`  
El mensaje a cifrar.

`recipient_keys_fp`  
Un array con las huellas de las claves del destinatario. Al menos una clave debe estar presente.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de dato | Descripción |
|----|----|----|
| `"compression_alg"` | string | Algoritmo de compresión. Las opciones `"compression_alg"` y `"compression_level"` deben estar ambas definidas para activar la compresión de los datos. |
| `"compression_level"` | integer | El nivel de compresión, de 0 a 9. 0 desactiva la compresión. |
| `"armor"` | boolean | Activa la salida ASCII armada. Desactivada por omisión. |
| `"add_signature"` | boolean | El mensaje cifrado será también firmado. |
| `"hash"` | string | Define el algoritmo de hash utilizado en el cálculo de la firma. La opción "add_signature" debe estar definida a `true`. |
| `"creation_time"` | integer | Define la hora de creación de la firma en segundos desde el 1 de enero de 1970 UTC. Por omisión, se utiliza la hora actual. |
| `"expiration_time"` | integer | Define el tiempo de expiración de la firma en segundos desde la hora de creación. El valor 0 se utiliza para marcar la firma como no expirante (valor por omisión). |
| `"password"` | string | Añade una contraseña utilizada para cifrar los datos. |
| `"cipher"` | string | Define el algoritmo de cifrado simétrico. Los valores posibles son "IDEA", "TRIPLEDES", "CAST5", "BLOWFISH", "AES128", "AES192", "AES256", "TWOFISH", "CAMELLIA128", "CAMELLIA192", "CAMELLIA256", "SM4". |
| `"aead"` | string | Define el algoritmo de modo AEAD. Los valores posibles son "None" para desactivar AEAD, "EAX", "OCB". |
| `"aead_bits"` | integer | Define la longitud del chunk para el modo AEAD en número de bits de tamaño de chunk. Debe estar comprendido entre 0 y 56. |
| `"flags"` | integer | Define indicadores de cifrado adicionales. Los indicadores soportados son: RNP_ENCRYPT_NOWRAP - no envolver los datos en un paquete de datos literales. Esto permitiría cifrar datos ya firmados. |
| `"file_name"` | string | Define el nombre de fichero almacenado internamente para los datos cifrados. El valor especial \_CONSOLE puede ser utilizado para marcar el mensaje como "para sus ojos solamente", es decir, que no debe ser almacenado en ningún lugar sino solo mostrado al destinatario. Por omisión, es una cadena vacía. |
| `"file_mtime"` | integer | Define la fecha de modificación del fichero de entrada en segundos desde el 1 de enero de 1970 UTC. |

## Valores devueltos

Los datos cifrados en caso de éxito o `false` si ocurre un error.
