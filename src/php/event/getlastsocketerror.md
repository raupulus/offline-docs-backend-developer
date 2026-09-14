---
title: EventUtil::getLastSocketError
description: Devuelve el error más reciente ocurrido en el socket
source_url: https://www.php.net/manual/es/eventutil.getlastsocketerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventutil/getlastsocketerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 2dda716bd
order: 20450
---

EventUtil::getLastSocketError

Devuelve el error más reciente ocurrido en el socket

## Descripción

```php
public static EventUtil::getLastSocketError([mixed $socket]): string
```php

Devuelve el error más reciente ocurrido en el socket.

## Parámetros

`socket`  
Recurso de socket, flujo, o descriptor de fichero de socket.

## Valores devueltos

Devuelve el error más reciente ocurrido en el socket.

## Véase también

EventUtil::getLastSocketErrno
