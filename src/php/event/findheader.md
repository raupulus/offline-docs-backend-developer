---
title: EventHttpRequest::findHeader
description: Busca el valor de un encabezado
source_url: https://www.php.net/manual/es/eventhttprequest.findheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/findheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 20140
---

EventHttpRequest::findHeader

Busca el valor de un encabezado

## Descripción

```php
public EventHttpRequest::findHeader(string $key, string $type): void
```php

Busca el valor de un encabezado.

## Parámetros

`key`  
El nombre del encabezado.

`type`  
Una de las constantes [ `EventHttpRequest::*_HEADER`](#eventhttprequest.constants).

## Valores devueltos

Devuelve `null` si el encabezado no ha sido encontrado.

## Véase también

EventHttpRequest::addHeader
