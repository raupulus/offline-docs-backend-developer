---
title: openssl_pkey_export
description: Almacena una representación exportable de la clave en una cadena de caracteres
source_url: https://www.php.net/manual/es/function.openssl-pkey-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59380
---

openssl_pkey_export

Almacena una representación exportable de la clave en una cadena de caracteres

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_pkey_export(OpenSSLAsymmetricKey $key, string $output, [string $passphrase], [array $options]): bool
```php

`openssl_pkey_export` exporta la clave `key` en formato de cadena PEM, y la almacena en la variable `output` (que se pasa por referencia).

> [!NOTE]
> Debe existir un archivo `openssl.cnf` válido e instalado para que esta función opere correctamente. Ver las notas encontradas en la [sección concerniente a la instalación](#openssl.installation) para más información.

## Parámetros

`key`  

`output`  

`passphrase`  
La clave puede estar protegida por la contraseña `passphrase`.

`options`  
`options` puede ser utilizado para ajustar el proceso de exportación especificando o reemplazando las opciones del archivo de configuración de OpenSSL. Consulte `openssl_csr_new` para más información sobre `options`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
