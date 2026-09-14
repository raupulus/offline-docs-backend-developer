---
title: openssl_cms_sign
description: Firma un fichero
source_url: https://www.php.net/manual/es/function.openssl-cms-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cms-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: 5bc68add3
order: 59040
---

openssl_cms_sign

Firma un fichero

## Descripción

```php
#[\SensitiveParameter] openssl_cms_sign(string $input_filename, string $output_filename, OpenSSLCertificate $certificate, OpenSSLAsymmetricKey $private_key, array $headers, [int $flags], [int $encoding], [string $untrusted_certificates_filename]): bool
```php

Esta función firma un fichero con un certificado X.509 y una clave.

## Parámetros

`input_filename`  
El nombre del fichero a firmar.

`output_filename`  
El nombre del fichero para depositar los resultados.

`certificate`  
El certificado de firma. Véase [Parámetros de clave/certificado](#openssl.certparams) para una lista de valores válidos.

`private_key`  
La clave asociada al `certificate`. Véase [Parámetros de clave/certificado](#openssl.certparams) para una lista de valores válidos.

`headers`  
Un array de encabezados a incluir en la salida S/MIME.

`flags`  
Los flag a pasar a `cms_sign`.

`encoding`  
La codificación del fichero de salida. Una de las constantes `OPENSSL_ENCODING_SMIME`, `OPENSSL_ENCODING_DER` o `OPENSSL_ENCODING_PEM`.

`untrusted_certificates_filename`  
Los certificados intermedios a incluir en la firma.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `openssl_cms_sign`

```
<?php

openssl_cms_sign('input.txt', 'output.txt', 'file://cert.pem', 'file://privkey.pem', null, OPENSSL_CMS_BINARY, OPENSSL_ENCODING_DER, 'chain.pem');
?>

    
```php
