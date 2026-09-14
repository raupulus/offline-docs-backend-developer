---
title: openssl_pkey_get_public
description: Extrae una clave pública de un certificado y la prepara
source_url: https://www.php.net/manual/es/function.openssl-pkey-get-public.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-get-public.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59420
---

openssl_pkey_get_public

Extrae una clave pública de un certificado y la prepara

## Descripción

```php
openssl_pkey_get_public(OpenSSLAsymmetricKey $public_key): OpenSSLAsymmetricKey
```php

`openssl_pkey_get_public` extrae la clave pública del certificado `public_key` y la prepara para ser utilizada por otras funciones.

## Parámetros

`public_key`  
`public_key` puede tener uno de los siguientes valores:

1.  Una instancia de `OpenSSLAsymmetricKey`.

2.  Una cadena en el formato `file://path/to/file.pem`. El fichero designado debe contener una clave pública o un certificado en formato PEM (eventualmente ambos).

3.  Una clave pública en formato PEM.

## Valores devueltos

Devuelve una instancia de `OpenSSLAsymmetricKey` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `OpenSSLAsymmetricKey`; anteriormente se devolvía un `resource` de tipo `OpenSSL key`. |
| 8.0.0 | `public_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
