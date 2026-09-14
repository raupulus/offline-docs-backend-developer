---
title: openssl_public_encrypt
description: Cifra datos con una clave pública
source_url: https://www.php.net/manual/es/function.openssl-public-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-public-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 8108ac2a6
order: 59470
---

openssl_public_encrypt

Cifra datos con una clave pública

## Descripción

```php
#[\SensitiveParameter] openssl_public_encrypt(string $data, string $encrypted_data, OpenSSLAsymmetricKey $public_key, [int $padding], [string $digest_algo]): bool
```php

`openssl_public_encrypt` cifra los datos `data` con la clave pública `public_key` y almacena el resultado en `encrypted_data`. Los datos cifrados pueden ser descifrados con la función `openssl_private_decrypt`.

Esta función puede ser utilizada para cifrar un mensaje que podrá ser leído únicamente por el propietario de la clave privada. Puede ser igualmente utilizada para almacenar datos seguros en una base de datos.

## Parámetros

`data`  

`encrypted_data`  
Contendrá el resultado del cifrado.

`public_key`  
`public_key` debe ser la clave pública correspondiente a la clave privada que será utilizada para descifrar los datos.

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
| 8.0.0 | `public_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Véase también

`openssl_private_encrypt`, `openssl_private_decrypt`
