---
title: EventHttpRequest::removeHeader
description: Elimina un encabezado HTTP de los encabezados de la petición
source_url: https://www.php.net/manual/es/eventhttprequest.removeheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/removeheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 919c8a799
order: 20260
---

EventHttpRequest::removeHeader

Elimina un encabezado HTTP de los encabezados de la petición

## Descripción

```php
public EventHttpRequest::removeHeader(string $key, string $type): void
```php

Elimina un encabezado HTTP de los encabezados de la petición.

## Parámetros

`key`  
El nombre del encabezado.

`type`  
Una constante `EventHttpRequest::*_HEADER`.

## Valores devueltos

Elimina un encabezado HTTP de los encabezados de la petición.

## Véase también

EventHttpRequest::addHeader
