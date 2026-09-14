---
title: openssl_x509_checkpurpose
description: Verifica el uso de un certificado
source_url: https://www.php.net/manual/es/function.openssl-x509-checkpurpose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-checkpurpose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59570
---

openssl_x509_checkpurpose

Verifica el uso de un certificado

## Descripción

```php
openssl_x509_checkpurpose(OpenSSLCertificate $certificate, int $purpose, [array $ca_info], [string $untrusted_certificates_file]): bool
```php

`openssl_x509_checkpurpose` examina el certificado especificado por `certificate`, para ver si puede ser utilizado para una operación particular `purpose`.

## Parámetros

`certificate`  
El certificado examinado.

`purpose`  
| Constante | Descripción |
|----|----|
| X509_PURPOSE_SSL_CLIENT | ¿Puede el certificado ser utilizado con el cliente de una conexión SSL? |
| X509_PURPOSE_SSL_SERVER | ¿Puede el certificado ser utilizado con el servidor de una conexión SSL? |
| X509_PURPOSE_NS_SSL_SERVER | ¿Puede el certificado ser utilizado con un servidor Netscape de una conexión SSL? |
| X509_PURPOSE_SMIME_SIGN | ¿Puede el certificado ser utilizado para firmar correos en el estándar S/MIME? |
| X509_PURPOSE_SMIME_ENCRYPT | ¿Puede el certificado ser utilizado para cifrar un correo en formato S/MIME? |
| X509_PURPOSE_CRL_SIGN | ¿Puede el certificado ser utilizado para cifrar una lista de revocación de certificados? (CRL)? |
| X509_PURPOSE_ANY | ¿Puede el certificado ser utilizado para cualquiera de estos casos? |

Uso de `openssl_x509_checkpurpose`

Estas opciones no son campos de bits: solo puede pasarse una a la vez.

`ca_info`  
`ca_info` debe ser un array de directorios/ficheros de CA de confianza como se describe en la [Verificación de certificados](#openssl.cert.verification).

`untrusted_certificates_file`  
Si se especifica, es el nombre de un fichero en formato PEM que contiene los certificados que podrán ayudar durante la verificación del certificado, aunque se les deba otorgar una confianza limitada.

## Valores devueltos

Retorna `true` si el certificado puede ser utilizado para un propósito particular, `false` si no puede serlo, o -1 si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
| 8.0.0 | `untrusted_certificates_file` ahora es nullable. |
