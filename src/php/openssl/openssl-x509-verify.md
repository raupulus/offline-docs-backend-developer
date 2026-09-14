---
title: openssl_x509_verify
description: Verifica la firma digital de un certificado x509 con respecto a una clave
  pública
source_url: https://www.php.net/manual/es/function.openssl-x509-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59640
---

openssl_x509_verify

Verifica la firma digital de un certificado x509 con respecto a una clave pública

## Descripción

```php
openssl_x509_verify(OpenSSLCertificate $certificate, OpenSSLAsymmetricKey $public_key): int
```php

La función `openssl_x509_verify` verifica que el certificado `certificate` ha sido firmado por la clave privada correspondiente a la clave pública `public_key`.

## Parámetros

`certificate`  
Ver los [parámetros clave/Certificados](#openssl.certparams) para una lista de valores válidos.

`public_key`  
`OpenSSLAsymmetricKey` - una clave, devuelta por la función `openssl_get_publickey`

`string` - una clave con formato PEM, por ejemplo, `-----BEGIN PUBLIC KEY----- MIIBCgK...`.

## Valores devueltos

Devuelve 1 si la firma es correcta, 0 si es incorrecta y -1 si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` acepta ahora una instancia de `OpenSSLCertificate`; anteriormente, un `resource` de tipo `OpenSSL X.509` era aceptado. |
| 8.0.0 | `public_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, un `resource` de tipo `OpenSSL key` o `OpenSSL X.509` era aceptado. |

## Ejemplos

Ejemplo con `openssl_x509_verify`

```
<?php
$hostname = "news.php.net";
$ssloptions = array(
    "capture_peer_cert" => true,
    "capture_peer_cert_chain" => true,
    "allow_self_signed"=> false,
    "CN_match" => $hostname,
    "verify_peer" => true,
    "SNI_enabled" => true,
    "SNI_server_name" => $hostname,
);

$ctx = stream_context_create( array("ssl" => $ssloptions) );
$result = stream_socket_client("ssl://$hostname:443", $errno, $errstr, 30, STREAM_CLIENT_CONNECT, $ctx);
$cont = stream_context_get_params($result);
$x509 = $cont["options"]["ssl"]["peer_certificate"];
$certparsed = openssl_x509_parse($x509);

foreach($cont["options"]["ssl"]["peer_certificate_chain"] as $chaincert)
{
    $chainparsed = openssl_x509_parse($chaincert);
    $chain_public_key = openssl_get_publickey($chaincert);
    $r = openssl_x509_verify($x509, $chain_public_key);
    if ($r==1)
    {
        echo $certparsed['subject']['CN'];
        echo " fue firmado digitalmente por ";
        echo $chainparsed['subject']['CN']."\n";
    }
}
?>

    
```php

## Véase también

`openssl_verify`, `openssl_get_publickey`
