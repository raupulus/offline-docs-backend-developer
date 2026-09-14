---
title: EventUtil::getSocketName
description: Recupera la dirección actual ligada al socket
source_url: https://www.php.net/manual/es/eventutil.getsocketname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventutil/getsocketname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 20470
---

EventUtil::getSocketName

Recupera la dirección actual ligada al socket

## Descripción

```php
public static EventUtil::getSocketName(mixed $socket, string $address, [mixed $port]): bool
```php

Recupera la dirección actual ligada al `socket`.

## Parámetros

`socket`  
Recurso de socket, flujo, o descriptor de fichero de socket.

`address`  
Parámetro de salida. Dirección IP o la ruta del dominio UNIX del socket, según la familia de dirección del socket.

`port`  
Parámetro de salida. El puerto ligado al socket. No tiene sentido para los sockets de dominio UNIX.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
