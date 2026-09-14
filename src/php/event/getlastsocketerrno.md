---
title: EventUtil::getLastSocketErrno
description: Devuelve el número de error más reciente ocurrido en el socket
source_url: https://www.php.net/manual/es/eventutil.getlastsocketerrno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventutil/getlastsocketerrno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 2dda716bd
order: 20440
---

EventUtil::getLastSocketErrno

Devuelve el número de error más reciente ocurrido en el socket

## Descripción

```php
public static EventUtil::getLastSocketErrno([mixed $socket]): int
```php

Devuelve el número de error más reciente ocurrido en el socket (`errno`).

## Parámetros

`socket`  
Recurso de socket, flujo o descriptor de fichero de socket.

## Valores devueltos

Devuelve el número de error más reciente ocurrido en el socket (`errno`).

## Véase también

EventUtil::getLastSocketError
