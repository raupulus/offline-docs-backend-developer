---
title: openssl_verify
description: Verifica una firma
source_url: https://www.php.net/manual/es/function.openssl-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 59550
---

openssl_verify

Verifica una firma

## Descripción

```php
openssl_verify(string $data, string $signature, OpenSSLAsymmetricKey $public_key, [string $algorithm], [int $padding]): int
```php

`openssl_verify` verifica que la firma `signature` es correcta para los datos `data`, y con la clave pública `public_key`. Esta clave debe ser la clave pública correspondiente a la clave privada utilizada durante la firma.

## Parámetros

`data`  
La cadena de datos utilizada para generar la firma

`signature`  
Una cadena binaria bruta, generada por la función `openssl_sign` o similar

`public_key`  
`OpenSSLAsymmetricKey` - una clave, retornada por la función `openssl_get_publickey`

`string` - una clave en formato PEM, por ejemplo: `-----BEGIN PUBLIC KEY----- MIIBCgK...`.

`algorithm`  
`int` - una de las [firmas de algoritmos](#openssl.signature-algos).

`string` - una cadena válida retornada por la función `openssl_get_md_methods`, por ejemplo: "sha1WithRSAEncryption" o "sha512". Algoritmo por omisión: "OPENSSL_ALGO_SHA1".

`padding`  
Relleno RSA PSS a utilizar.

## Valores devueltos

Retorna 1 si la firma es correcta, 0 si es incorrecta y -1 o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se ha añadido el parámetro opcional `padding`. |
| 8.0.0 | `public_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Ejemplos

Ejemplo con `openssl_verify`

```
<?php
// Se asume que $data y $signature contienen los datos a firmar y
// la firma.

// Lectura de la clave pública desde el certificado
$pubkeyid = openssl_pkey_get_public("file://src/openssl-0.9.6/demos/sign/cert.pem");

// indica si la firma es correcta
$ok = openssl_verify($data, $signature, $pubkeyid);
if ($ok == 1) {
    echo "Firma válida";
} elseif ($ok == 0) {
    echo "Firma errónea";
} else {
    echo "Error de verificación de la firma";
}
// libera las claves de la memoria
openssl_free_key($pubkeyid);
?>

    
```php

Ejemplo con `openssl_verify`

```
<?php
//Datos que se desean firmar
$data = 'my data';

//Crea una nueva clave privada y pública
$private_key_res = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));
$details = openssl_pkey_get_details($private_key_res);
$public_key_res = openssl_pkey_get_public($details['key']);

//Crea una firma
openssl_sign($data, $signature, $private_key_res, "sha256WithRSAEncryption");

//Verifica la firma
$ok = openssl_verify($data, $signature, $public_key_res, OPENSSL_ALGO_SHA256);
if ($ok == 1) {
    echo "válida";
} elseif ($ok == 0) {
    echo "inválida";
} else {
    echo "error: ".openssl_error_string();
}
?>

    
```php

## Véase también

`openssl_sign`
