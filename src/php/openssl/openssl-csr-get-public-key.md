---
title: openssl_csr_get_public_key
description: Devuelve la clave pública de un CSR
source_url: https://www.php.net/manual/es/function.openssl-csr-get-public-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-csr-get-public-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59080
---

openssl_csr_get_public_key

Devuelve la clave pública de un

CSR

## Descripción

```php
openssl_csr_get_public_key(OpenSSLCertificateSigningRequest $csr, [bool $short_names]): OpenSSLAsymmetricKey
```php

`openssl_csr_get_public_key` extrae la clave pública de la `csr` y la prepara para su utilización por otras funciones.

## Parámetros

`csr`  
Ver los [parámetros CSR](#openssl.certparams) para obtener una lista de los valores válidos.

`short_names`  
> [!WARNING]
> Este parámetro es ignorado

## Valores devueltos

Devuelve una `OpenSSLAsymmetricKey` en caso de éxito, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `OpenSSLAsymmetricKey` ; anteriormente se devolvía un `resource` de tipo `OpenSSL key`. |
| 8.0.0 | `csr` acepta ahora una instancia de `OpenSSLCertificateSigningRequest` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |

## Ejemplos

Ejemplo de openssl_csr_get_public_key()

```
<?php
$subject = array(
    "commonName" => "example.com",
);
$private_key = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));
$csr = openssl_csr_new($subject, $private_key, array('digest_alg' => 'sha256') );
$public_key = openssl_csr_get_public_key($csr);
$info = openssl_pkey_get_details($public_key);
echo $info['key'];
?>

    
```php

## Véase también

`openssl_csr_get_subject`, `openssl_csr_new`, `openssl_pkey_get_details`, `openssl_pkey_export_to_file`, `openssl_pkey_export`
