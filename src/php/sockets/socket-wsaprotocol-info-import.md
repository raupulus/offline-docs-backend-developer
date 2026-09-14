---
title: socket_wsaprotocol_info_import
description: Importa un socket de otro proceso
source_url: https://www.php.net/manual/es/function.socket-wsaprotocol-info-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-wsaprotocol-info-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75900
---

socket_wsaprotocol_info_import

Importa un socket de otro proceso

## Descripción

```php
socket_wsaprotocol_info_import(string $info_id): Socket
```php

Importa un socket que ha sido exportado previamente por otro proceso.

> [!NOTE]
> Esta función solo está disponible en Windows.

## Parámetros

`info_id`  
El identificador que fue devuelto por una llamada previa a `socket_wsaprotocol_info_export`.

## Valores devueltos

Devuelve una instancia de `Socket` en caso de éxito, o `false` si ocurre un error

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función ahora devuelve una instancia de `Socket`; anteriormente se devolvía un `recurso`. |

## Véase también

socket_wsaprotocol_info_export
