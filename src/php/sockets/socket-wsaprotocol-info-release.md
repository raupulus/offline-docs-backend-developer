---
title: socket_wsaprotocol_info_release
description: Libera una estructura WSAPROTOCOL_INFO exportada
source_url: https://www.php.net/manual/es/function.socket-wsaprotocol-info-release.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-wsaprotocol-info-release.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 6d5949ca0
order: 75910
---

socket_wsaprotocol_info_release

Libera una estructura WSAPROTOCOL_INFO exportada

## Descripción

```php
socket_wsaprotocol_info_release(string $info_id): bool
```php

Libera la memoria compartida correspondiente al `info_id` dado.

> [!NOTE]
> Esta función solo está disponible en Windows.

## Parámetros

`info_id`  
El identificador que fue devuelto por una llamada previa a `socket_wsaprotocol_info_export`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

socket_wsaprotocol_info_export
