---
title: openssl_cms_decrypt
description: Descifra un mensaje CMS
source_url: https://www.php.net/manual/es/function.openssl-cms-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cms-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: 5bc68add3
order: 59010
---

openssl_cms_decrypt

Descifra un mensaje CMS

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_cms_decrypt(string $input_filename, string $output_filename, OpenSSLCertificate $certificate, [OpenSSLAsymmetricKey $private_key], [int $encoding]): bool
```php

Descifra un mensaje CMS.

## Parámetros

`input_filename`  
El nombre de un fichero que contiene contenido cifrado.

`output_filename`  
El nombre del fichero para depositar el contenido descifrado.

`certificate`  
El nombre del fichero que contiene un certificado del destinatario.

`private_key`  
El nombre del fichero que contiene una clave PKCS#8.

`encoding`  
La codificación del fichero de entrada. Una de las constantes `OPENSSL_ENCODING_SMIME`, `OPENSSL_ENCODING_DER` o `OPENSSL_ENCODING_PEM`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
