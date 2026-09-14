---
title: openssl_pkcs12_export_to_file
description: Exporta un certificado compatible con PKCS#12
source_url: https://www.php.net/manual/es/function.openssl-pkcs12-export-to-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs12-export-to-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59280
---

openssl_pkcs12_export_to_file

Exporta un certificado compatible con

PKCS

\#12

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_pkcs12_export_to_file(OpenSSLCertificate $certificate, string $output_filename, OpenSSLAsymmetricKey $private_key, string $passphrase, [array $options]): bool
```php

`openssl_pkcs12_export_to_file` almacena un certificado `certificate` en un fichero denominado `output_filename` en un formato de fichero PKCS#12.

## Parámetros

`certificate`  
Ver los [parámetros clave/Certificados](#openssl.certparams) para una lista de valores válidos.

`output_filename`  
Ruta de acceso al fichero de salida.

`private_key`  
Clave privada del fichero PKCS#12. Ver [parámetros Clave/Certificado](#openssl.certparams) para una lista de valores válidos.

`passphrase`  
Contraseña de cifrado para desbloquear el fichero PKCS#12.

`options`  
Array opcional, las demás claves serán ignoradas.

| Clave | Descripción |
|----|----|
| `"extracerts"` | array de certificados adicionales o un certificado único a incluir en el fichero PKCS#12. |
| `"friendly_name"` | `string` a utilizar para el certificado y la clave proporcionados |

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
