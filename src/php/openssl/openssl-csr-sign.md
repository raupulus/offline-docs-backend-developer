---
title: openssl_csr_sign
description: Firma un CSR con otro certificado (o consigo mismo) y genera un certificado
source_url: https://www.php.net/manual/es/function.openssl-csr-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-csr-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 6338117af
order: 59110
---

openssl_csr_sign

Firma un

CSR

con otro certificado (o consigo mismo) y genera un certificado

## Descripción

```php
#[\SensitiveParameter] openssl_csr_sign(OpenSSLCertificateSigningRequest $csr, OpenSSLCertificate $ca_certificate, OpenSSLAsymmetricKey $private_key, int $days, [array $options], [int $serial], [string $serial_hex]): OpenSSLCertificate
```php

`openssl_csr_sign` genera un certificado x509 desde el CSR proporcionado.

> [!NOTE]
> Debe existir un archivo `openssl.cnf` válido e instalado para que esta función opere correctamente. Ver las notas encontradas en la [sección concerniente a la instalación](#openssl.installation) para más información.

## Parámetros

`csr`  
Un CSR generado previamente por `openssl_csr_new`. Sin embargo, esto también puede ser la ruta hacia un CSR codificado en formato PEM si se especifica con `file://path/to/csr` o una cadena exportada generada por `openssl_csr_export`.

`ca_certificate`  
El certificado generado será firmado por el certificado `ca_certificate`. Si `ca_certificate` es `null`, el certificado generado será autosignado.

`private_key`  
`private_key` es la clave privada que corresponde al certificado `ca_certificate`.

`days`  
`days` especifica la duración para la cual el certificado es válido, en número de días.

`options`  
Se pueden ajustar las opciones de firma CSR con `options`. Consulte la función `openssl_csr_new` para obtener más información sobre `options`.

`serial`  
Un número de serie opcional para el certificado emitido. Si no se especifica, tendrá un valor de 0.

`serial_hex`  
Una cadena hexadecimal opcional que representa el número de serie del certificado emitido. Si se define, tiene prioridad sobre el valor del parámetro `serial`. Si no se especifica o se define como `null`, se utiliza el valor del parámetro `serial` en su lugar.

## Valores devueltos

Devuelve una instancia de `OpenSSLCertificate` en caso de éxito, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se ha añadido el parámetro `serial_hex`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `OpenSSLCertificate` ; anteriormente se devolvía un `resource` de tipo `OpenSSL X.509`. |
| 8.0.0 | `csr` ahora acepta una instancia de `OpenSSLCertificateSigningRequest` ; anteriormente se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |
| 8.0.0 | `ca_certificate` ahora acepta una instancia de `OpenSSLCertificate` ; anteriormente se aceptaba un `resource` de tipo `OpenSSL X.509`. |
| 8.0.0 | `ca_certificate` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |

## Ejemplos

Ejemplo con `openssl_csr_sign` - firmar una CSR (cómo ser su propia Autoridad de Certificación)

```
<?php
// Supongamos que este script está configurado para recibir CSR que han
// sido pegados en un campo textarea desde otra página
$csrdata = $_POST["CSR"];

// Vamos a firmar la solicitud con nuestro propio certificado, como
// "autoridad de certificación". Puede utilizarse cualquier certificado para firmar otro,
// pero el proceso es inútil a menos que el certificado de firma tenga la confianza de los usuarios
// que utilizarán el nuevo certificado firmado.

// Necesitamos nuestro certificado y la clave privada
$cacert = "file://path/to/ca.crt";
$privkey = array("file://path/to/ca.key", "la_clave_secreta_de_su_certificado");

$usercert = openssl_csr_sign($csrdata, $cacert, $privkey, 365, array('digest_alg'=>'sha256') );

// Mostramos ahora el certificado generado, de forma que el usuario
// pueda copiarlo/pegarlo en su configuración local (como un
// archivo que contiene los certificados de su servidor SSL)
openssl_x509_export($usercert, $certout);
echo $certout;

// Muestra todos los errores ocurridos
while (($e = openssl_error_string()) !== false) {
    echo $e . "\n";
}
?>

    
```php
