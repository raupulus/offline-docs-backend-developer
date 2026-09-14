---
title: stream_socket_shutdown
description: Detiene una conexión full-duplex
source_url: https://www.php.net/manual/es/function.stream-socket-shutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-shutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 88200
---

stream_socket_shutdown

Detiene una conexión full-duplex

## Descripción

```php
stream_socket_shutdown(resource $stream, int $mode): bool
```php

Detiene (parcialmente o no) una conexión full-duplex.

> [!NOTE]
> El o los buffers asociados pueden o no ser vaciados.

## Parámetros

`stream`  
Un flujo abierto (abierto con la función `stream_socket_client`, por ejemplo)

`mode`  
Una de las constantes siguientes: `STREAM_SHUT_RD` (desactiva las recepciones futuras), `STREAM_SHUT_WR` (desactiva las transmisiones futuras) o `STREAM_SHUT_RDWR` (desactiva las recepciones o las transmisiones futuras).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_socket_shutdown`

```
<?php

$server = stream_socket_server('tcp://127.0.0.1:1337');
$client = stream_socket_client('tcp://127.0.0.1:1337');

var_dump(fputs($client, "Hola"));

stream_socket_shutdown($client, STREAM_SHUT_WR);
var_dump(fputs($client, "Hola")); // actualmente no funciona

?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(5)

    Notice: fputs(): send of 5 bytes failed with errno=32 Broken pipe in test.php on line 9
    int(0)

## Véase también

`fclose`
