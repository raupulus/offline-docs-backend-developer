---
title: openssl_pkcs7_verify
description: Verifica la firma de un mensaje S/MIME
source_url: https://www.php.net/manual/es/function.openssl-pkcs7-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs7-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59350
---

openssl_pkcs7_verify

Verifica la firma de un mensaje S/MIME

## Descripción

```php
openssl_pkcs7_verify(string $input_filename, int $flags, [string $signers_certificates_filename], [array $ca_info], [string $untrusted_certificates_filename], [string $content], [string $output_filename]): bool
```php

`openssl_pkcs7_verify` lee el mensaje S/MIME contenido en el fichero `filename` y examina la firma digital.

## Parámetros

`input_filename`  
Ruta hacia el mensaje.

`flags`  
`flags` sirve para modificar la forma en que se verifica la firma. Consulte las [constantes PKCS7](#openssl.pkcs7.flags). Por omisión, el valor es: PKCS7_DETACHED.

`signers_certificates_filename`  
Si el parámetro `signers_certificates_filename` es especificado, debe ser una cadena que contenga el nombre de un fichero que contiene el certificado del firmante, en formato PEM.

`ca_info`  
Si el parámetro `ca_info` es especificado, debe contener la información sobre los certificados de confianza de terceros utilizados durante la verificación. Consulte [verificación de certificados](#openssl.cert.verification) para más detalles.

`untrusted_certificates_filename`  
Si el parámetro `untrusted_certificates_filename` es especificado, debe representar el nombre de un fichero que contiene un conjunto de certificados utilizados como certificados de poca confianza.

`content`  
Puede especificarse un nombre de fichero con el parámetro `content` que puede ser rellenado con los datos verificados, pero sin las informaciones de firma.

`output_filename`  

## Valores devueltos

Devuelve `true` si la firma es verificada, y `false` en caso contrario (el mensaje ha sido modificado, o bien el certificado de firma es inválido) o -1 si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `signers_certificates_filename`, `untrusted_certificates_filename`, `content` y `output_filename` ahora son nullable. |
| 7.2.0 | Se ha añadido el parámetro `output_filename`. |

## Notas

> [!NOTE]
> Tal como se especifica en la RFC 2045, las líneas no deben ser más largas que 76 caracteres en el parámetro `input_filename`.
