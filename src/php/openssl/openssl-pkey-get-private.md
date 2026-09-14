---
title: openssl_pkey_get_private
description: Lee una clave privada
source_url: https://www.php.net/manual/es/function.openssl-pkey-get-private.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-get-private.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59410
---

openssl_pkey_get_private

Lee una clave privada

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_pkey_get_private(OpenSSLAsymmetricKey $private_key, [string $passphrase]): OpenSSLAsymmetricKey
```php

`openssl_pkey_get_private` analiza la clave `private_key` y la prepara para ser utilizada por otras funciones.

## Parámetros

`private_key`  
`private_key` puede ser uno de los siguientes valores:

1.  una cadena en el formato `file://path/to/file.pem`. El fichero así designado debe contener una clave privada o un certificado en formato PEM (eventualmente ambos).

2.  Una clave privada en formato PEM.

`passphrase`  
El parámetro opcional `passphrase` debe ser utilizado si la clave especificada está cifrada (protegida por una contraseña).

## Valores devueltos

Devuelve una instancia de `OpenSSLAsymmetricKey` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `OpenSSLAsymmetricKey`; anteriormente se devolvía un `resource` de tipo `OpenSSL key`. |
| 8.0.0 | `private_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
| 8.0.0 | `passphrase` es ahora nullable. |
