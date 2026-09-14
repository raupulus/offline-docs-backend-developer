---
title: socket_export_stream
description: Exporta un socket en un flujo que encapsula un socket
source_url: https://www.php.net/manual/es/function.socket-export-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-export-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75660
---

socket_export_stream

Exporta un socket en un flujo que encapsula un socket

## Descripción

```php
socket_export_stream(Socket $socket): resource
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`socket`  

## Valores devueltos

Devuelve un resource o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
