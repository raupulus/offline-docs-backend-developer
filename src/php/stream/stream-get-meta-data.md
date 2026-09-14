---
title: stream_get_meta_data
description: Lee los encabezados y metadatos de los flujos
source_url: https://www.php.net/manual/es/function.stream-get-meta-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-get-meta-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: cf3707c0f
order: 87980
---

stream_get_meta_data

Lee los encabezados y metadatos de los flujos

## Descripción

```php
stream_get_meta_data(resource $stream): array
```php

Devuelve la información disponible sobre el flujo `stream`.

## Parámetros

`stream`  
El flujo puede ser cualquier flujo creado por las funciones `fopen`, `fsockopen`, `pfsockopen` y `stream_socket_client`.

## Valores devueltos

El array resultante puede contener los siguientes elementos:

- `timed_out` (`bool`) : `true` si el flujo ha alcanzado el tiempo límite de espera de datos durante la última llamada a las funciones `fread` y `fgets`.

- `blocked` (`bool`) : `true` si el flujo está en modo bloqueante. Véase también `stream_set_blocking`.

- `eof` (`bool`) : `true` si el flujo ha alcanzado el final del fichero. Tenga en cuenta que para los sockets, este valor puede ser `true` incluso si `unread_bytes` no es nulo. Para determinar si quedan datos por leer, utilice en su lugar la función `feof`.

- `unread_bytes` (`int`) : el número de bytes actualmente colocados en el búfer interno de PHP.

  > [!NOTE]
  > No se debería utilizar este valor en un script.

- `stream_type` (`string`) : un nombre que describe la implementación subyacente del flujo.

- `wrapper_type` (`string`) : un nombre que describe el gestor de protocolo para este flujo. Véase [???](#wrappers) para más información sobre los gestores.

- `wrapper_data` (mixed) : datos específicos del gestor asociados a este flujo. Véase [???](#wrappers) para más información sobre los gestores y sus datos.

- `mode` (`string`) : el tipo de acceso requerido para este flujo (véase la tabla 1 de la referencia de la función [`fopen`](#function.fopen)).

- `seekable` (`bool`) : si se puede buscar en el flujo actual.

- `uri` (`string`) : la URI/nombre de fichero asociado a este flujo.

- `crypto` (`array`) - los metadatos de la conexión TLS para este flujo. (Nota: Solo se proporciona cuando el recurso de flujo utiliza TLS).

## Ejemplos

Ejemplo de `stream_get_meta_data` utilizando `fopen` con http

```
<?php
$url = 'http://www.example.com/';

if (!$fp = fopen($url, 'r')) {
    trigger_error("No se puede abrir la URL ($url)", E_USER_ERROR);
}

$meta = stream_get_meta_data($fp);

var_dump($meta);

fclose($fp);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(10) {
      'timed_out' =>
      bool(false)
      'blocked' =>
      bool(true)
      'eof' =>
      bool(false)
      'wrapper_data' =>
      array(13) {
        [0] =>
        string(15) "HTTP/1.1 200 OK"
        [1] =>
        string(11) "Age: 244629"
        [2] =>
        string(29) "Cache-Control: max-age=604800"
        [3] =>
        string(38) "Content-Type: text/html; charset=UTF-8"
        [4] =>
        string(35) "Date: Sat, 20 Nov 2021 18:17:57 GMT"
        [5] =>
        string(24) "Etag: "3147526947+ident""
        [6] =>
        string(38) "Expires: Sat, 27 Nov 2021 18:17:57 GMT"
        [7] =>
        string(44) "Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT"
        [8] =>
        string(22) "Server: ECS (chb/0286)"
        [9] =>
        string(21) "Vary: Accept-Encoding"
        [10] =>
        string(12) "X-Cache: HIT"
        [11] =>
        string(20) "Content-Length: 1256"
        [12] =>
        string(17) "Connection: close"
      }
      'wrapper_type' =>
      string(4) "http"
      'stream_type' =>
      string(14) "tcp_socket/ssl"
      'mode' =>
      string(1) "r"
      'unread_bytes' =>
      int(1256)
      'seekable' =>
      bool(false)
      'uri' =>
      string(23) "http://www.example.com/"
    }

Ejemplo de `stream_get_meta_data` utilizando `stream_socket_client` con https

```
     
<?php
$streamContext = stream_context_create(
    [
        'ssl' => [
            'capture_peer_cert' => true,
            'capture_peer_cert_chain' => true,
            'disable_compression' => true,
        ],
    ]
);

$client = stream_socket_client(
    'ssl://www.example.com:443',
    $errorNumber,
    $errorDescription,
    40,
    STREAM_CLIENT_CONNECT,
    $streamContext
);

$meta = stream_get_meta_data($client);

var_dump($meta);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(8) {
      'crypto' =>
      array(4) {
        'protocol' =>
        string(7) "TLSv1.3"
        'cipher_name' =>
        string(22) "TLS_AES_256_GCM_SHA384"
        'cipher_bits' =>
        int(256)
        'cipher_version' =>
        string(7) "TLSv1.3"
      }
      'timed_out' =>
      bool(false)
      'blocked' =>
      bool(true)
      'eof' =>
      bool(false)
      'stream_type' =>
      string(14) "tcp_socket/ssl"
      'mode' =>
      string(2) "r+"
      'unread_bytes' =>
      int(0)
      'seekable' =>
      bool(false)
    }

## Notas

> [!NOTE]
> Esta función no funciona en los sockets creados con [la extensión socket](#ref.sockets).

## Véase también

`get_headers`, [\$http_response_header](#reserved.variables.httpresponseheader)
