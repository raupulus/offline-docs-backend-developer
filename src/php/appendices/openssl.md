---
title: Cambios para OpenSSL en PHP 5.6.x
source_url: https://www.php.net/manual/es/migration56.openssl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration56/openssl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: ee1ce6a0e
order: 230
---

## Cambios para OpenSSL en PHP 5.6.x

## Las envolturas de flujo ahora verifican de forma predeterminada los certificados de par y los nombres de host al usar SSL/TLS

Todos los flujos cifrados de cliente activan ahora la verificación de pares de forma predeterminada. De forma predeterminada, esto utilizará el paquete de CA predeterminado de OpenSSL para verificar el certificado de par. Para la mayoría de los usuarios, esto no debería causar problemas al comunicarse con servidores que tengan certificados SSL válidos, ya que la mayoría de los distribuidores configuran OpenSSL para usar las rutas de CA predeterminadas.

El paquete de CA predeterminado se puede sobrescribir a nivel global utilizando las opciones de configuración openssl.cafile o openssl.capath, o para cada solicitud utilizando las opciones de contexto [`cafile`](#context.ssl.cafile) o [`capath`](#context.ssl.capath) .

Aunque en general no se recomienda, es posible desactivar la verificación del certificado de par para una solicitud estableciendo la opción de contexto [`verify_peer`](#context.ssl.verify-peer) a `false`, y desactivar la validación del nombre del par configurando la opción de contexto [`verify_peer_name`](#context.ssl.verify-peer-name) a `false`.

## Huellas digitales de certificado

Se ha añadido soporte para extraer y verificar las huellas digitales de los certificados. `openssl_x509_fingerprint` se ha añadido para extraer una huella digital de un certificado X.509 y se han añadido dos [opciones de contexto](#context.ssl) de flujo SSL: `capture_peer_cert` para capturar el certificado X.509 del par y `peer_fingerprint` para asegurar que el certificado del par coincida con la huella digital dada.

## Cifrados por defecto actualizados

Los cifrados predeterminados utilizados por PHP se han actualizado a una lista más segura basada en las [recomendaciones de cifrado de Mozilla](https://wiki.mozilla.org/Security/Server_Side_TLS#Recommended_Ciphersuite), con dos exclusiones adicionales: cifrados Diffie-Hellman anónimos y RC4.

Esta lista es accesible a través de la nueva constante `OPENSSL_DEFAULT_STREAM_CIPHERS` y puede ser reemplazada (como en versiones anteriores de PHP) definiendo la opción de contexto [`ciphers`](#context.ssl.ciphers).

## Compresión desactivada por defecto

La compresión SSL/TLS se ha desactivado de forma predeterminada para mitigar el ataque CRIME. PHP 5.4.13 añadió una opción de contexto [`disable_compression`](#context.ssl.disable-compression) para permitir desactivar la compresión; ahora está establecida en `true` (es decir, la compresión está desactivada) de forma predeterminada.

## Permitir que los servidores prefieran su propio orden de cifrado

Se ha añadido la opción de contexto SSL `honor_cipher_order` para permitir que los servidores de flujos cifrados mitiguen las vulnerabilidades de BEAST prefiriendo los cifrados del servidor sobre los del cliente.

## Acceder al protocolo negociado y al cifrado

Ahora se puede acceder al protocolo y cifrado negociados para un flujo cifrado a través de `stream_get_meta_data` o `stream_context_get_options` cuando la opción de contexto SSL `capture_session_meta` está establecida en `true`.

```php
<?php
$ctx = stream_context_create(['ssl' => [
    'capture_session_meta' => TRUE
]]);

$html = file_get_contents('https://google.com/', FALSE, $ctx);
$meta = stream_context_get_options($ctx)['ssl']['session_meta'];
var_dump($meta);
?>

   
```

El ejemplo anterior mostrará:

    array(4) {
      ["protocol"]=>
      string(5) "TLSv1"
      ["cipher_name"]=>
      string(20) "ECDHE-RSA-AES128-SHA"
      ["cipher_bits"]=>
      int(128)
      ["cipher_version"]=>
      string(11) "TLSv1/SSLv3"
    }

## Nuevas opciones para la confidencialidad persistente en servidores de flujos cifrados

Los flujos cifrados de cliente ya admiten la confidencialidad persistente, dado que por lo general esta es controlada por el servidor. Los flujos cifrados de servidor en PHP que utilizan certificados compatibles con la confidencialidad persistente no requieren realizar ninguna acción adicional para habilitar PFS; sin embargo, se han añadido varias opciones de contexto SSL nuevas para permitir un control mucho más granular sobre PFS y manejar los problemas de compatibilidad que puedan surgir.

`ecdh_curve`  
Esta opción permite seleccionar una curva específica para usar con los cifrados ECDH. Si no se especifica, se usará `prime256v1`.

`dh_param`  
Ruta a un archivo que contiene parámetros para el intercambio de claves Diffie-Hellman, como el creado por el siguiente comando:

```php
openssl dhparam -out /path/to/my/certs/dh-2048.pem 2048

     
```

`single_dh_use`  
Si se establece en `true`, se creará un nuevo par de claves al usar los parámetros Diffie-Hellman, mejorando así la confidencialidad persistente.

`single_ecdh_use`  
Si se establece en `true`, siempre se generará un nuevo par de claves al negociar las suites de cifrado ECDH. Esto mejora la confidencialidad persistente.

## Selección de la versión SSL/TLS

Ahora es posible seleccionar versiones específicas de SSL y TLS a través de la opción de contexto SSL `crypto_method` o especificando un transporte concreto al crear una envoltura de flujo (por ejemplo, llamando a `stream_socket_client` o `stream_socket_server`).

La opción de contexto SSL `crypto_method` acepta una máscara de bits enumerando los protocolos que están permitidos, como lo hace el `crypto_type` de `stream_socket_enable_crypto`.

Protocolo(s)

Bandera cliente

Bandera servidor

Transporte

Cualquier versión TLS o SSL

STREAM_CRYPTO_METHOD_ANY_CLIENT

STREAM_CRYPTO_METHOD_ANY_SERVER

ssl://

Cualquier versión TLS

STREAM_CRYPTO_METHOD_TLS_CLIENT

STREAM_CRYPTO_METHOD_TLS_SERVER

tls://

TLS 1.0

STREAM_CRYPTO_METHOD_TLSv1_0_CLIENT

STREAM_CRYPTO_METHOD_TLSv1_0_SERVER

tlsv1.0://

TLS 1.1

STREAM_CRYPTO_METHOD_TLSv1_1_CLIENT

STREAM_CRYPTO_METHOD_TLSv1_1_SERVER

tlsv1.1://

TLS 1.2

STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT

STREAM_CRYPTO_METHOD_TLSv1_2_SERVER

tlsv1.2://

SSL 3

STREAM_CRYPTO_METHOD_SSLv3_CLIENT

STREAM_CRYPTO_METHOD_SSLv3_SERVER

sslv3://

```php
<?php

// Requiriendo TLS 1.0 o mejor al usar file_get_contents():
$ctx = stream_context_create([
    'ssl' => [
        'crypto_method' => STREAM_CRYPTO_METHOD_TLS_CLIENT,
    ],
]);
$html = file_get_contents('https://google.com/', false, $ctx);

// Requiriendo TLS 1.1 o 1.2:
$ctx = stream_context_create([
    'ssl' => [
        'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_1_CLIENT |
                           STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT,
    ],
]);
$html = file_get_contents('https://google.com/', false, $ctx);

// Conexión usando el transporte de socket tlsv1.2://.
$sock = stream_socket_client('tlsv1.2://google.com:443/');

?>

   
```

## Adición de `openssl_get_cert_locations`

Se ha añadido la función `openssl_get_cert_locations`, la cual devuelve las ubicaciones predeterminadas en las que PHP buscará los paquetes de CA.

```php
<?php
var_dump(openssl_get_cert_locations());
?>

   
```

El ejemplo anterior mostrará:

    array(8) {
      ["default_cert_file"]=>
      string(21) "/etc/pki/tls/cert.pem"
      ["default_cert_file_env"]=>
      string(13) "SSL_CERT_FILE"
      ["default_cert_dir"]=>
      string(18) "/etc/pki/tls/certs"
      ["default_cert_dir_env"]=>
      string(12) "SSL_CERT_DIR"
      ["default_private_dir"]=>
      string(20) "/etc/pki/tls/private"
      ["default_default_cert_area"]=>
      string(12) "/etc/pki/tls"
      ["ini_cafile"]=>
      string(0) ""
      ["ini_capath"]=>
      string(0) ""
    }

## Soporte SPKI

Se ha añadido compatibilidad para generar, extraer y verificar claves públicas y desafíos firmados (SPKAC). Las funciones `openssl_spki_new`, `openssl_spki_verify`, `openssl_spki_export_challenge` y `openssl_spki_export` se han añadido para crear, verificar y exportar tanto la clave pública en formato PEM como el desafío asociados a un SPKAC generado a partir de un elemento `KeyGen` de HTML5.

`openssl_spki_new`  
Genera un nuevo SPKAC usando la clave privada, `string` de desafío y el algoritmo de hashing.

```php
<?php
$pkey = openssl_pkey_new();
openssl_pkey_export($pkey, 'secret passphrase');

$spkac = openssl_spki_new($pkey, 'challenge string');
?>

      
```

El ejemplo anterior mostrará:

    SPKAC=MIIBXjCByDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA3L0IfUijj7+A8CPC8EmhcdNoe5fUAog7OrBdhn7EkxFButUp40P7+LiYiygYG1TmoI/a5EgsLU3s9twEz3hmgY9mYIqb/rb+SF8qlD/K6KVyUORC7Wlz1Df4L8O3DuRGzx6/+3jIW6cPBpfgH1sVuYS1vDBsP/gMMIxwTsKJ4P0CAwEAARYkYjViMzYxMTktNjY5YS00ZDljLWEyYzctMGZjNGFhMjVlMmE2MA0GCSqGSIb3DQEBAwUAA4GBAF7hu0ifzmjonhAak2FhhBRsKFDzXdKIkrWxVNe8e0bZzMrWOxFM/rqBgeH3/gtOUDRS5Fnzyq425UsTYbjfiKzxGeCYCQJb1KJ2V5Ij/mIJHZr53WYEXHQTNMGR8RPm7IxwVXVSHIgAfXsXZ9IXNbFbcaLRiSTr9/N4U+MXUWL7

`openssl_spki_verify`  
Verifica el SPKAC proporcionado.

```php
<?php
$pkey = openssl_pkey_new();
openssl_pkey_export($pkey, 'secret passphrase');

$spkac = openssl_spki_new($pkey, 'challenge string');
var_dump(openssl_spki_verify($spkac));
?>

      
```

`openssl_spki_export_challenge`  
Exporta el desafío asociado al SPKAC proporcionado.

```php
<?php
$pkey = openssl_pkey_new();
openssl_pkey_export($pkey, 'secret passphrase');

$spkac = openssl_spki_new($pkey, 'challenge string');
$challenge = openssl_spki_export_challenge($spkac);
echo $challenge;
?>

      
```

El ejemplo anterior mostrará:

    challenge string

`openssl_spki_export`  
Exporta la clave pública RSA en formato PEM del SPKAC.

```php
<?php
$pkey = openssl_pkey_new();
openssl_pkey_export($pkey, 'secret passphrase');

$spkac = openssl_spki_new($pkey, 'challenge string');
echo openssl_spki_export($spkac);
?>

      
```

El ejemplo anterior mostrará:

    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcvQh9SKOPv4DwI8LwSaFx02h7
    l9QCiDs6sF2GfsSTEUG61SnjQ/v4uJiLKBgbVOagj9rkSCwtTez23ATPeGaBj2Zg
    ipv+tv5IXyqUP8ropXJQ5ELtbXPUN/gvw7cO5EbPHr/7eMhbpw8Gl+AfWxW5hLW8
    MGw/+AwwjHBOwong/QIDAQAB
    -----END PUBLIC KEY-----
