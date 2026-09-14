---
title: openssl_cms_verify
description: Verifica una firma CMS
source_url: https://www.php.net/manual/es/function.openssl-cms-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cms-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: 96263b140
order: 59050
---

openssl_cms_verify

Verifica una firma CMS

## Descripción

```php
openssl_cms_verify(string $input_filename, [int $flags], [string $certificates], [array $ca_info], [string $untrusted_certificates_filename], [string $content], [string $pk7], [string $sigfile], [int $encoding]): bool
```php

Esta función verifica una firma CMS, ya sea adjunta o desprendida, con la codificación especificada.

## Parámetros

`input_filename`  
El fichero de entrada.

`flags`  
Los flag a pasar a `cms_verify`.

`certificates`  
Un fichero con el certificado del firmante y eventualmente certificados intermedios.

`ca_info`  
Un array que contiene certificados de autoridad auto-firmados.

`untrusted_certificates_filename`  
Un fichero que contiene certificados intermedios adicionales.

`content`  
Un fichero que apunta al contenido cuando las firmas están desprendidas.

`pk7`  

`sigfile`  
Un fichero para guardar la firma.

`encoding`  
La codificación del fichero de entrada. Una de las constantes `OPENSSL_ENCODING_SMIME`, `OPENSSL_ENCODING_DER` o `OPENSSL_ENCODING_PEM`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
