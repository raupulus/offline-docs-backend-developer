---
title: openssl_public_decrypt
description: Descifra datos con una clave pública
source_url: https://www.php.net/manual/es/function.openssl-public-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-public-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 7da0f9995
order: 59460
---

openssl_public_decrypt

Descifra datos con una clave pública

## Descripción

```php
#[\SensitiveParameter] openssl_public_decrypt(string $data, string $decrypted_data, OpenSSLAsymmetricKey $public_key, [int $padding]): bool
```php

`openssl_public_decrypt` descifra los datos `data` que han sido cifrados con la función `openssl_private_encrypt` y almacena el resultado en `decrypted_data`.

Puede utilizarse esta función para verificar si el mensaje ha sido escrito por el propietario de la clave privada.

## Parámetros

`data`  

`decrypted_data`  

`public_key`  
`public_key` debe ser la clave pública que ha sido utilizada para cifrar los datos.

`padding`  
`padding` puede ser `OPENSSL_PKCS1_PADDING` o `OPENSSL_NO_PADDING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `public_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509` . |

## Véase también

`openssl_private_encrypt`, `openssl_private_decrypt`
