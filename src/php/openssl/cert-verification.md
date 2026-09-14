---
title: Verificación de certificados
source_url: https://www.php.net/manual/es/openssl.cert.verification.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/cert-verification.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: 9e8ce329f
order: 58950
---

## Verificación de certificados

Cuando se llama a una función que va a verificar una firma o un certificado, el argumento `ca_info` debe ser un array que contenga los nombres de un directorio y un fichero que indiquen los emisores de confianza. Si se especifica un directorio, debe ser correcto, ya que `openssl` lo utilizará.
