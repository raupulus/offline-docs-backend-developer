---
title: openssl_pkcs7_read
description: Exporta el fichero PKCS7 a un array de certificados PEM
source_url: https://www.php.net/manual/es/function.openssl-pkcs7-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs7-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59330
---

openssl_pkcs7_read

Exporta el fichero PKCS7 a un array de certificados

PEM

## Descripción

```php
openssl_pkcs7_read(string $data, array $certificates): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`data`  
El string de datos que debe ser analizado (en formato p7b).

`certificates`  
Un array de certificados PEM desde los datos de entrada p7b.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Obtener un array PEM desde un fichero P7B

```
<?php

$file = 'certs.p7b';

$f = file_get_contents($file);
$p7 = array();
$r = openssl_pkcs7_read($f, $p7);

if ($r === false) {
    printf("ERROR: %s no es un fichero p7b válido".PHP_EOL, $file);
        for($e = openssl_error_string(), $i = 0; $e; $e = openssl_error_string(), $i++)
            printf("SSL l%d: %s".PHP_EOL, $i, $e);
    exit(1);
}

print_r($p7);
?>

    
```php

## Véase también

`openssl_csr_sign`
