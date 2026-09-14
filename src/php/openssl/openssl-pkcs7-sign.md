---
title: openssl_pkcs7_sign
description: Firma un mensaje S/MIME
source_url: https://www.php.net/manual/es/function.openssl-pkcs7-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs7-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59340
---

openssl_pkcs7_sign

Firma un mensaje S/MIME

## Descripción

```php
#[\SensitiveParameter] openssl_pkcs7_sign(string $input_filename, string $output_filename, OpenSSLCertificate $certificate, OpenSSLAsymmetricKey $private_key, array $headers, [int $flags], [string $untrusted_certificates_filename]): bool
```php

`openssl_pkcs7_sign` toma el contenido del fichero `input_filename` y lo firma utilizando el certificado y la clave privada contenidos en los argumentos `certificate` y `private_key`.

## Parámetros

`input_filename`  
El fichero de entrada que se tiene la intención de firmar digitalmente.

`output_filename`  
El fichero donde se escribirá la firma digital.

`certificate`  
El certificado X.509 utilizado para firmar digitalmente `input_filename`. Ver [parámetros Clave/Certificado](#openssl.certparams) para una lista de valores válidos.

`private_key`  
`private_key` es la clave privada correspondiente a `certificate`. Ver [parámetros Clave Pública/Privada](#openssl.certparams) para una lista de valores válidos.

`headers`  
`headers` es un array de encabezados que serán añadidos a los datos cifrados (ver la función `openssl_pkcs7_encrypt` para más detalles sobre el formato del parámetro).

`flags`  
`flags` puede ser utilizado para modificar la salida. Ver las [constantes PKCS7](#openssl.pkcs7.flags).

`untrusted_certificates_filename`  
`untrusted_certificates_filename` especifica el nombre del fichero que contiene un conjunto de certificados adicionales a incluir en la firma, los cuales podrán ayudar al destinatario a verificar los datos que se utilizan.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Ejemplos

Ejemplo con `openssl_pkcs7_sign`

```
<?php
// el mensaje que se quiere firmar, para que el destinatario esté seguro de que
// proviene de usted
$data = <<<EOD

Usted está autorizado a gastar 10 000€ en gastos de viaje.

El PDG
EOD;
// guardar el mensaje en un fichero
$fp = fopen("msg.txt", "w");
fwrite($fp, $data);
fclose($fp);
// cifrarlo
if (openssl_pkcs7_sign("msg.txt", "signed.txt", "file://mycert.pem",
    array("file://mycert.pem", "mypassphrase"),
    array("To" => "joes@example.com", // sintaxis con clave
          "From: HQ <ceo@example.com>", // sintaxis indexada
          "Subject" => "Eyes only")
    )) {
    // mensaje firmado - ¡envíelo!
    exec(ini_get("sendmail_path") . " < signed.txt");
}
?>

    
```php
