---
title: openssl_private_encrypt
description: Cifra datos con una clave privada
source_url: https://www.php.net/manual/es/function.openssl-private-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-private-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 7da0f9995
order: 59450
---

openssl_private_encrypt

Cifra datos con una clave privada

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_private_encrypt(string $data, string $encrypted_data, OpenSSLAsymmetricKey $private_key, [int $padding]): bool
```php

`openssl_private_encrypt` cifra los datos `data` con la clave privada `private_key` y almacena el resultado en `encrypted_data`. Los datos cifrados pueden ser descifrados con la función `openssl_public_decrypt`.

Esta función puede ser utilizada para firmar los datos (o sus cifrados) para demostrar que no han sido escritos por otra persona.

## Parámetros

`data`  

`encrypted_data`  

`private_key`  
`private_key` debe ser la clave privada correspondiente a la clave pública que será utilizada para descifrar los datos.

`padding`  
El parámetro `padding` puede ser `OPENSSL_PKCS1_PADDING` o `OPENSSL_NO_PADDING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `private_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Véase también

`openssl_public_encrypt`, `openssl_public_decrypt`
