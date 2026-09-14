---
title: openssl_get_cert_locations
description: Obtener las ubicaciones de certificados disponibles
source_url: https://www.php.net/manual/es/function.openssl-get-cert-locations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-get-cert-locations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: dd421bc26
order: 59180
---

openssl_get_cert_locations

Obtener las ubicaciones de certificados disponibles

## Descripción

```php
openssl_get_cert_locations(): array
```php

`openssl_get_cert_locations` devuelve un array con información sobre la ubicaciones de certificados disponibles donde buscar certificados SSL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con las ubicaciones de certificados disponibles.

## Ejemplos

Ejemplo de `openssl_get_cert_locations`

```
<?php
var_dump(openssl_get_cert_locations());
?>

    
```php

El ejemplo anterior mostrará:

    array(8) {
      ["default_cert_file"]=>
      string(21) "/usr/lib/ssl/cert.pem"
      ["default_cert_file_env"]=>
      string(13) "SSL_CERT_FILE"
      ["default_cert_dir"]=>
      string(18) "/usr/lib/ssl/certs"
      ["default_cert_dir_env"]=>
      string(12) "SSL_CERT_DIR"
      ["default_private_dir"]=>
      string(20) "/usr/lib/ssl/private"
      ["default_default_cert_area"]=>
      string(12) "/usr/lib/ssl"
      ["ini_cafile"]=>
      string(0) ""
      ["ini_capath"]=>
      string(0) ""
    }
