---
title: openssl_pkcs7_encrypt
description: Cifra un mensaje S/MIME
source_url: https://www.php.net/manual/es/function.openssl-pkcs7-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs7-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 0773339dc
order: 59320
---

openssl_pkcs7_encrypt

Cifra un mensaje S/MIME

## Descripción

```php
openssl_pkcs7_encrypt(string $input_filename, string $output_filename, OpenSSLCertificate $certificate, array $headers, [int $flags], [int $cipher_algo]): bool
```php

`openssl_pkcs7_encrypt` toma el contenido del fichero `input_filename` y lo cifra utilizando un cifrado RC2 de 40 bits, de manera que el mensaje solo pueda ser leído por el poseedor de `certificate`.

## Parámetros

`input_filename`  

`output_filename`  

`certificate`  
Puede ser un certificado X.509 o un array de certificados X.509.

`headers`  
`headers` es un array de encabezados que serán añadidos al inicio del mensaje, una vez que los datos hayan sido cifrados.

`headers` puede ser un array asociativo, donde las claves son los nombres de los encabezados, o bien un array indexado donde cada línea contiene un encabezado completo.

`flags`  
`flags` puede ser utilizado para especificar opciones que afectarán al cifrado (ver las [constantes PKCS7](#openssl.pkcs7.flags)).

`cipher_algo`  
Una de las [constantes cipher](#openssl.ciphers).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El algoritmo de cifrado por omisión (`cipher_algo`) es ahora AES-128-CBC (`OPENSSL_CIPHER_AES_128_CBC`). Anteriormente, se utilizaba PKCS7/CMS (`OPENSSL_CIPHER_RC2_40`). |
| 8.0.0 | `certificate` acepta ahora una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |

## Ejemplos

Ejemplo con `openssl_pkcs7_encrypt`

```
<?php
// el mensaje que se desea cifrar y enviar a su agente secreto
// en misión, llamado "nighthawk". Tiene su certificado
// en el fichero "nighthawk.pem"
$data = <<<EOD
Nighthawk,

Top secret, solo para sus ojos !

El enemigo se acerca! Reúnase en el café a las 8:30,
para su pasaporte falso.

HQ
EOD;

// Carga de la clave
$key = file_get_contents("nighthawk.pem");

// Guardado del mensaje en un fichero
$fp = fopen("msg.txt", "w");
fwrite($fp, $data);
fclose($fp);

// Cifrado del mensaje
if (openssl_pkcs7_encrypt("msg.txt", "enc.txt", $key,
    array("To" => "nighthawk@example.com", // sintaxis en forma de clave
          "From: HQ <hq@example.com>", // sintaxis en forma de índice
          "Subject" => "Solo para sus ojos !"))) {
    // mensaje cifrado - envíelo !
    exec(ini_get("sendmail_path") . " < enc.txt");
}
?>

    
```php
