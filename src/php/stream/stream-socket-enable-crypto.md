---
title: stream_socket_enable_crypto
description: Activa o desactiva el cifrado para un socket ya conectado
source_url: https://www.php.net/manual/es/function.stream-socket-enable-crypto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-enable-crypto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: f39a3a7f3
order: 88140
---

stream_socket_enable_crypto

Activa o desactiva el cifrado para un socket ya conectado

## Descripción

```php
stream_socket_enable_crypto(resource $stream, bool $enable, [int $crypto_method], [resource $session_stream]): int
```php

Activa o desactiva el cifrado para un socket ya conectado.

Una vez definidos los parámetros de cifrado, este puede ser activado y desactivado dinámicamente pasando `true` o `false` en el argumento `enable`.

## Parámetros

`stream`  
El recurso de flujo.

`enable`  
Activa o desactiva el cifrado en el flujo.

`crypto_method`  
Configura el cifrado en el flujo. Los métodos válidos son

- `STREAM_CRYPTO_METHOD_SSLv2_CLIENT`

- `STREAM_CRYPTO_METHOD_SSLv3_CLIENT`

- `STREAM_CRYPTO_METHOD_SSLv23_CLIENT`

- `STREAM_CRYPTO_METHOD_ANY_CLIENT`

- `STREAM_CRYPTO_METHOD_TLS_CLIENT`

- `STREAM_CRYPTO_METHOD_TLSv1_0_CLIENT`

- `STREAM_CRYPTO_METHOD_TLSv1_1_CLIENT`

- `STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT`

- `STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT` (disponible a partir de PHP 7.4.0)

- `STREAM_CRYPTO_METHOD_SSLv2_SERVER`

- `STREAM_CRYPTO_METHOD_SSLv3_SERVER`

- `STREAM_CRYPTO_METHOD_SSLv23_SERVER`

- `STREAM_CRYPTO_METHOD_ANY_SERVER`

- `STREAM_CRYPTO_METHOD_TLS_SERVER`

- `STREAM_CRYPTO_METHOD_TLSv1_0_SERVER`

- `STREAM_CRYPTO_METHOD_TLSv1_1_SERVER`

- `STREAM_CRYPTO_METHOD_TLSv1_2_SERVER`

- `STREAM_CRYPTO_METHOD_TLSv1_3_SERVER` (disponible a partir de PHP 7.4.0)

Si se omite, la opción de contexto `crypto_method` en el contexto SSL del flujo será utilizada en su lugar.

`session_stream`  
Inicializa el flujo con la configuración proveniente del argumento `session_stream`.

## Valores devueltos

Retorna `true` en caso de éxito, `false` si la negociación falló o `0` si no hay suficientes datos y se debe intentar nuevamente (únicamente para sockets no bloqueantes).

## Historial de cambios

| Versión | Descripción                         |
|---------|-------------------------------------|
| 8.0.0   | `session_stream` ahora es nullable. |

## Ejemplos

Ejemplo con `stream_socket_enable_crypto`

```
<?php
$fp = stream_socket_client("tcp://myproto.example.com:31337", $errno, $errstr, 30);
if (!$fp) {
    die("Imposible conectar: $errstr ($errno)");
}

/* Activación del cifrado durante la identificación */
stream_socket_enable_crypto($fp, true, STREAM_CRYPTO_METHOD_SSLv23_CLIENT);
fwrite($fp, "USER god\r\n");
fwrite($fp, "PASS secret\r\n");

/* Desactivación del cifrado para el resto */
stream_socket_enable_crypto($fp, false);

while ($motd = fgets($fp)) {
    echo $motd;
}

fclose($fp);
?>

    
```php

Resultado del ejemplo anterior es similar a:

## Véase también

[???](#ref.openssl), [???](#transports)
