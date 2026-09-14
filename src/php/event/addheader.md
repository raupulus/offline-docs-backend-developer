---
title: EventHttpRequest::addHeader
description: Añade un encabezado HTTP a los encabezados de la petición
source_url: https://www.php.net/manual/es/eventhttprequest.addheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/addheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20090
---

EventHttpRequest::addHeader

Añade un encabezado HTTP a los encabezados de la petición

## Descripción

```php
public EventHttpRequest::addHeader(string $key, string $value, int $type): bool
```php

Añade un encabezado HTTP a los encabezados de la petición.

## Parámetros

`key`  
Nombre del encabezado.

`value`  
Valor del encabezado.

`type`  
Una de las constantes [ `EventHttpRequest::*_HEADER`](#eventhttprequest.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventHttpRequest::removeHeader
