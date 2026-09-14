---
title: socket_shutdown
description: Desactiva un socket en lectura y/o escritura
source_url: https://www.php.net/manual/es/function.socket-shutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-shutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75860
---

socket_shutdown

Desactiva un socket en lectura y/o escritura

## Descripción

```php
socket_shutdown(Socket $socket, [int $mode]): bool
```php

`socket_shutdown` permite evitar que los datos entrantes o salientes o ambos (por omisión) sean emitidos a través del socket `socket`.

> [!NOTE]
> Los buffers asociados pueden o no ser vaciados.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create`.

`mode`  
El valor del parámetro `mode` puede ser uno de los siguientes :

|     |                                             |
|-----|---------------------------------------------|
| `0` | Impide la lectura del socket                |
| `1` | Impide la escritura del socket              |
| `2` | Impide la escritura y la lectura del socket |

Valores posibles para `mode`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
