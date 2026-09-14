---
title: openssl_sign
description: Firma los datos
source_url: https://www.php.net/manual/es/function.openssl-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 59500
---

openssl_sign

Firma los datos

## Descripción

```php
#[\SensitiveParameter] openssl_sign(string $data, string $signature, OpenSSLAsymmetricKey $private_key, [string $algorithm], [int $padding]): bool
```php

`openssl_sign` calcula la firma de los datos `data` generando una firma digital criptográfica utilizando la clave privada asociada con el parámetro `private_key`. Tenga en cuenta que los datos en sí no son cifrados.

## Parámetros

`data`  
La cadena de datos que se desea firmar.

`signature`  
Si la llamada a la función tiene éxito, la firma será devuelta en el parámetro `signature`.

`private_key`  
`OpenSSLAsymmetricKey` - una clave, devuelta por la función `openssl_get_privatekey`

`string` - una clave en formato PEM.

`algorithm`  
`int` - uno de los [algoritmos de firma](#openssl.signature-algos).

`string` - una cadena válida devuelta por la función `openssl_get_md_methods`, por ejemplo: "sha256WithRSAEncryption" o "sha384".

`padding`  
Relleno RSA PSS a utilizar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se ha añadido el parámetro opcional `padding`. |
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Ejemplos

Ejemplo con `openssl_sign`

```
<?php
// Se asume que $data contiene los datos a firmar

// lectura de la clave pública para cada destinatario
$pkeyid = openssl_pkey_get_private("file://src/openssl-0.9.6/demos/sign/key.pem");

// cálculo de la firma
openssl_sign($data, $signature, $pkeyid);

// libera las claves de la memoria
openssl_free_key($pkeyid);
?>

    
```php

Ejemplo con `openssl_sign`

```
<?php
//datos que se desean firmar
$data = 'my data';

//Crea una nueva clave privada y pública
$new_key_pair = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));
openssl_pkey_export($new_key_pair, $private_key_pem);

$details = openssl_pkey_get_details($new_key_pair);
$public_key_pem = $details['key'];

//Creación de la firma
openssl_sign($data, $signature, $private_key_pem, OPENSSL_ALGO_SHA256);

//Guardado para uso posterior
file_put_contents('private_key.pem', $private_key_pem);
file_put_contents('public_key.pem', $public_key_pem);
file_put_contents('signature.dat', $signature);

//Verificación de la firma
$r = openssl_verify($data, $signature, $public_key_pem, "sha256WithRSAEncryption");
var_dump($r);
?>

    
```php

## Véase también

`openssl_verify`
