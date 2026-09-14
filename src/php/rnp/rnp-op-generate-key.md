---
title: rnp_op_generate_key
description: Genera una clave
source_url: https://www.php.net/manual/es/function.rnp-op-generate-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-op-generate-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72290
---

rnp_op_generate_key

Genera una clave

## Descripción

```php
rnp_op_generate_key(RnpFFI $ffi, string $userid, string $key_alg, [string $sub_alg], [array $options]): string
```php

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`userid`  
El identificador del usuario PGP - texto que debe representar el nombre y la dirección de correo electrónico del titular de la clave.

`key_alg`  
La clave del algoritmo (es decir, 'RSA', 'DSA', etc).

`sub_alg`  
El algoritmo de subclave. Si no está definido, la subclave no será generada.

`options`  
Un array asociativo con opciones.

| Clave | Tipo de datos | Descripción |
|----|----|----|
| `"bits"` | integer | El tamaño de la clave principal en bits. Aplicable únicamente a las claves RSA, DSA y El-Gamal. |
| `"hash"` | string | Algoritmo de hash utilizado en la firma de la clave o la firma de ligadura de subclave. |
| `"dsa_qbits"` | integer | Define el tamaño de un parámetro `q` para la clave DSA. Nota: se definirá un valor predeterminado adecuado, según el número de bits de la clave. Sin embargo, puede ser reemplazado si es necesario. |
| `"curve"` | string | Define la curva utilizada para la clave ECC. Nota: esto se aplica únicamente a las claves ECDSA, ECDH y SM2. |
| `"request_password"` | boolean | Activa la solicitud de contraseña a través del proveedor de contraseñas. Esta contraseña será utilizada para el cifrado de la clave. La función de retrollamada del proveedor de contraseñas debe ser definida previamente llamando a `rnp_ffi_set_pass_provider`. Nota: este parámetro será ignorado si la contraseña ha sido definida a través de `"password"` |
| `"password"` | string | Define la contraseña utilizada para cifrar los datos de la clave secreta. |
| `"expiration"` | integer | Define el tiempo de expiración de la clave principal y la subclave en segundos. |
| `"sub_bits"` | integer | El tamaño de la subclave en bits. Aplicable únicamente a las claves RSA, DSA y El-Gamal. |
| `"sub_hash"` | string | Algoritmo de hash utilizado en la firma de la subclave o la firma de ligadura de subclave. |
| `"sub_curve"` | string | Define la curva utilizada para la subclave ECC. Nota: esto se aplica únicamente a las claves ECDSA, ECDH y SM2. |

## Valores devueltos

La huella de la clave principal generada o `false` si ocurre un error. Esta huella puede ser utilizada más tarde para referenciar la clave en las operaciones de firma y cifrado. Los datos de la clave se almacenan en el contexto de memoria FFI y pueden ser guardados utilizando `rnp_save_keys` o `rnp_save_keys_to_path`.
