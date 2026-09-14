---
title: openssl_pkcs12_export
description: Exporta un certificado compatible PKCS#12 a una variable
source_url: https://www.php.net/manual/es/function.openssl-pkcs12-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs12-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59290
---

openssl_pkcs12_export

Exporta un certificado compatible

PKCS

\#12 a una variable

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_pkcs12_export(OpenSSLCertificate $certificate, string $output, OpenSSLAsymmetricKey $private_key, string $passphrase, [array $options]): bool
```php

`openssl_pkcs12_export` almacena un certificado `certificate` en una cadena denominada `output` en un formato PKCS#12.

## Parámetros

`certificate`  
Ver los [parámetros clave/Certificados](#openssl.certparams) para una lista de valores válidos.

`output`  
En caso de éxito, esta variable contendrá el PKCS#12.

`private_key`  
Clave privada del archivo PKCS#12. Consulte [Parámetros de claves pública/privada](#openssl.certparams) para obtener la lista de valores válidos.

`passphrase`  
Contraseña de cifrado para desbloquear el archivo PKCS#12.

`options`  
Array opcional, las otras claves serán ignoradas.

| Clave | Descripción |
|----|----|
| `"extracerts"` | Array de certificados adicionales o de un certificado único a incluir en el archivo PKCS#12. |
| `"friendly_name"` | cadena a utilizar para el certificado y la clave proporcionados |

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
