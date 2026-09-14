---
title: stream_socket_get_name
description: Lee el nombre del socket local o remoto
source_url: https://www.php.net/manual/es/function.stream-socket-get-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-get-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: a1702b5d4
order: 88150
---

stream_socket_get_name

Lee el nombre del socket local o remoto

## Descripción

```php
stream_socket_get_name(resource $socket, bool $remote): string
```php

`stream_socket_get_name` devuelve el nombre del socket local o remoto para la conexión `socket`.

## Parámetros

`socket`  
El socket del que se debe leer el nombre.

`remote`  
Si este argumento vale `true`, se devolverá el nombre del socket `remote` (remoto), y si vale `false`, se devolverá el socket `local` (local).

## Valores devueltos

El nombre del socket, o `false` si ocurre un error.

## Véase también

`stream_socket_accept`
