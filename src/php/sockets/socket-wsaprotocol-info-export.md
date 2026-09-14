---
title: socket_wsaprotocol_info_export
description: Exporta la estructura WSAPROTOCOL_INFO
source_url: https://www.php.net/manual/es/function.socket-wsaprotocol-info-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-wsaprotocol-info-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75890
---

socket_wsaprotocol_info_export

Exporta la estructura WSAPROTOCOL_INFO

## Descripción

```php
socket_wsaprotocol_info_export(Socket $socket, int $process_id): string
```php

Exporta la estructura `WSAPROTOCOL_INFO` a la memoria compartida y devuelve un identificador para su uso con `socket_wsaprotocol_info_import`. El ID exportado solo es valido para el `process_id` especificado.

> [!NOTE]
> La función solo está disponible en Windows.

## Parámetros

`socket`  
Una instancia de `Socket`.

`process_id`  
El identificador del proceso que importará el socket.

## Valores devueltos

Devuelve un identificador para la importación, o `false` si ocurre un error

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

socket_wsaprotocol_info_import

socket_wsaprotocol_info_release
