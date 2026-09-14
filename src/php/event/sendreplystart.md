---
title: EventHttpRequest::sendReplyStart
description: Inicializa un bloque de respuesta
source_url: https://www.php.net/manual/es/eventhttprequest.sendreplystart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/sendreplystart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20310
---

EventHttpRequest::sendReplyStart

Inicializa un bloque de respuesta

## Descripción

```php
public EventHttpRequest::sendReplyStart(int $code, string $reason): void
```php

Inicializa una respuesta que utiliza las cabeceras `Transfer-Encoding` `chunked`.

Esto permite al llamante difundir la respuesta al cliente, y es útil cuando no todos los datos de la respuesta están inmediatamente disponibles, o bien al enviar respuestas demasiado voluminosas.

El llamante debe proporcionar los bloques de datos con el método EventHttpRequest::sendReplyChunk y completar la respuesta llamando al método EventHttpRequest::sendReplyEnd.

## Parámetros

`code`  
El código de respuesta HTTP a enviar.

`reason`  
Un breve mensaje a enviar con el código de respuesta.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EventHttpRequest::sendReplyChunk

EventHttpRequest::sendReplyEnd
