---
title: socket_import_stream
description: Importa un flujo
source_url: https://www.php.net/manual/es/function.socket-import-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-import-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: false
translation_revision: 14dc7c473
order: 75710
---

socket_import_stream

Importa un flujo

## Descripción

```php
socket_import_stream(resource $stream): Socket
```php

Importa un flujo que encapsula un socket en un recurso.

## Parámetros

`stream`  
El recurso de flujo a importar.

## Valores devueltos

Devuelve `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `Socket`; anteriormente se devolvía un `resource`. |

## Ejemplos

Ejemplo con `socket_import_stream`

```
<?php
$stream = stream_socket_server("udp://0.0.0.0:58380", $errno, $errstr, STREAM_SERVER_BIND);
$sock   = socket_import_stream($stream);
?>

    
```php

## Véase también

`stream_socket_server`
