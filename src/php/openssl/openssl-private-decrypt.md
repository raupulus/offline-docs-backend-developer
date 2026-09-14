---
title: openssl_private_decrypt
description: Descifra datos con una clave privada
source_url: https://www.php.net/manual/es/function.openssl-private-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-private-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 8108ac2a6
order: 59440
---

openssl_private_decrypt

Descifra datos con una clave privada

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_private_decrypt(string $data, string $decrypted_data, OpenSSLAsymmetricKey $private_key, [int $padding], [string $digest_algo]): bool
```php

`openssl_private_decrypt` descifra `data` que ha sido cifrada previamente con `openssl_public_encrypt`, y almacena el resultado en la variable `decrypted_data`.

Esta función puede ser utilizada, por ejemplo, para descifrar datos que solo deben ser accesibles para el usuario.

## Parámetros

`data`  

`decrypted_data`  

`private_key`  
`private_key` debe ser la clave privada utilizada para cifrar los datos.

`padding`  
`padding` puede ser `OPENSSL_PKCS1_PADDING`, `OPENSSL_SSLV23_PADDING`, `OPENSSL_PKCS1_OAEP_PADDING` o `OPENSSL_NO_PADDING`.

`digest_algo`  
El algoritmo de resumen para el relleno OAEP, o `null` para utilizar el algoritmo por omisión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se ha añadido el parámetro opcional `digest_algo`. |
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Véase también

`openssl_public_encrypt`, `openssl_public_decrypt`
