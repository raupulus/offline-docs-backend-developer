---
title: openssl_pkey_export_to_file
description: Guarda una clave en formato ASCII en un fichero
source_url: https://www.php.net/manual/es/function.openssl-pkey-export-to-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-export-to-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: e50e79746
order: 59370
---

openssl_pkey_export_to_file

Guarda una clave en formato ASCII en un fichero

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_pkey_export_to_file(OpenSSLAsymmetricKey $key, string $output_filename, [string $passphrase], [array $options]): bool
```php

`openssl_pkey_export_to_file` guarda la clave en formato ASCII (PEM) `key` en el fichero `output_filename`.

> [!NOTE]
> Debe existir un archivo `openssl.cnf` válido e instalado para que esta función opere correctamente. Ver las notas encontradas en la [sección concerniente a la instalación](#openssl.installation) para más información.

## Parámetros

`key`  

`output_filename`  
Ruta del fichero de salida.

`passphrase`  
La clave puede estar eventualmente protegida por una `frase de contraseña`.

`options`  
`options` puede ser utilizado para ajustar el proceso de exportación especificando o reemplazando las opciones del archivo de configuración de OpenSSL. Véase `openssl_csr_new` para más información sobre `options`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
