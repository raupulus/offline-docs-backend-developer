---
title: EventBufferEvent::getDnsErrorString
description: Devuelve un string que describe el último error DNS
source_url: https://www.php.net/manual/es/eventbufferevent.getdnserrorstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/getdnserrorstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19460
---

EventBufferEvent::getDnsErrorString

Devuelve un string que describe el último error DNS

## Descripción

```php
public EventBufferEvent::getDnsErrorString(): string
```php

Devuelve un string que describe el último error DNS durante la ejecución del método EventBufferEvent::connectHost o un string vacío si no se detecta ningún error DNS.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string que describe el error DNS, o un string vacío si no hay ningún error.

## Véase también

EventBufferEvent::connectHost
