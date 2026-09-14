---
title: Parámetros de claves/certificados
source_url: https://www.php.net/manual/es/openssl.certparams.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/certparams.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 58960
---

## Parámetros de claves/certificados

Un gran número de funciones OpenSSL requieren una clave o un certificado como parámetros. Los métodos siguientes pueden ser utilizados para obtenerlos:

- Certificados

  1.  Una instancia de `OpenSSLCertificate` (o anterior a PHP 8.0.0, un `resource` de tipo `OpenSSL X.509`) devuelta por `openssl_x509_read`

  2.  Una cadena con el formato `file://path/to/cert.pem`; El fichero identificado debe contener un certificado, codificado en formato PEM.

  3.  Una cadena que contiene el contenido de un certificado, codificado en formato PEM, puede comenzar por `-----BEGIN CERTIFICATE-----`.

- Solicitudes de firma de certificados (Certificate Signing Requests, abreviado CSRs)

  1.  Una instancia de `OpenSSLCertificateSigningRequest` (o anterior a PHP 8.0.0, un `resource` de tipo `OpenSSL X.509 CSR`) devuelta por `openssl_csr_new`

  2.  Una `string` con el formato `file://path/to/csr.pem`; el fichero nombrado debe contener un CSR codificado en formato PEM.

  3.  Una `string` que contiene el contenido de un CSR, codificado en formato PEM, puede comenzar por `-----BEGIN CERTIFICATE REQUEST-----`.

- Claves públicas/privadas

  1.  Una instancia de `OpenSSLAsymmetricKey` (o anterior a PHP 8.0.0, un `resource` de tipo `OpenSSL key`) devuelta por `openssl_csr_new`

  2.  Para las claves públicas únicamente: una instancia de `OpenSSLCertificate` (o anterior a PHP 8.0.0, un `resource` de tipo `OpenSSL X.509`)

  3.  Una cadena con el formato: `file://path/to/file.pem`. El fichero debe contener una clave privada, o un certificado, codificado en formato PEM (puede contener ambos).

  4.  Una `string` que contiene el contenido de un certificado/clave, codificado en formato PEM, puede comenzar por `-----BEGIN PUBLIC KEY-----`.

  5.  Para las claves privadas, también puede utilizarse la sintaxis `array($key, $passphrase)`, donde `$key` representa una clave especificada por un fichero o una representación textual como se ha citado anteriormente, y `$passphrase` representa una cadena que contiene la frase de contraseña de esta clave privada.
