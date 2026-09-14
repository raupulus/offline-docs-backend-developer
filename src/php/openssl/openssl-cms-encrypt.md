---
title: openssl_cms_encrypt
description: Cifra un mensaje CMS
source_url: https://www.php.net/manual/es/function.openssl-cms-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cms-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: aa120f36c
order: 59020
---

openssl_cms_encrypt

Cifra un mensaje CMS

## Descripción

```php
openssl_cms_encrypt(string $input_filename, string $output_filename, OpenSSLCertificate $certificate, array $headers, [int $flags], [int $encoding], [string $cipher_algo]): bool
```php

Esta función cifra el contenido para uno o varios destinatarios, basado en los certificados que se le pasan.

## Parámetros

`input_filename`  
El fichero a cifrar.

`output_filename`  
El fichero de salida.

`certificate`  
Los destinatarios a cifrar.

`headers`  
Las cabeceras a incluir al utilizar S/MIME.

`flags`  
Los flag a pasar a CMS_sign.

`encoding`  
Una codificación de salida. Una de las constantes `OPENSSL_ENCODING_SMIME`, `OPENSSL_ENCODING_DER` o `OPENSSL_ENCODING_PEM`.

`cipher_algo`  
El cifrado a utilizar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `cipher_algo` es ahora de tipo `int` o `string`. Anteriormente, era de tipo `int`. |
| 8.1.0 | El algoritmo de cifrado por omisión (`cipher_algo`) es ahora AES-128-CBC (`OPENSSL_CIPHER_AES_128_CBC`). Anteriormente, se utilizaba PKCS7/CMS (`OPENSSL_CIPHER_RC2_40`). |
