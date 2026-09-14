---
title: EventHttpRequest::sendReply
description: Envía una respuesta HTML al cliente
source_url: https://www.php.net/manual/es/eventhttprequest.sendreply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/sendreply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 919c8a799
order: 20280
---

EventHttpRequest::sendReply

Envía una respuesta HTML al cliente

## Descripción

```php
public EventHttpRequest::sendReply(int $code, string $reason, [EventBuffer $buf]): void
```php

Envía una respuesta HTML al cliente. El cuerpo de la respuesta contiene los datos del parámetro opcional `buf`.

## Parámetros

`code`  
El código de respuesta HTTP a enviar.

`reason`  
Un breve mensaje a enviar con el código de respuesta.

`buf`  
El cuerpo de la respuesta.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EventHttpRequest::sendError

EventHttpRequest::sendReplyChunk
