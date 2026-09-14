---
title: EventBufferEvent::sslGetCipherName
description: Devuelve el nombre del cipher actual para la conexión SSL
source_url: https://www.php.net/manual/es/eventbufferevent.sslgetciphername.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslgetciphername.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 19590
---

EventBufferEvent::sslGetCipherName

Devuelve el nombre del cipher actual para la conexión SSL

## Descripción

```php
public EventBufferEvent::sslGetCipherName(): string
```php

Recupera el nombre del cipher actual para la conexión SSL.

> [!NOTE]
> Esta función solo está disponible si `Event` ha sido compilado con soporte OpenSSL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del cipher actual para la conexión SSL o `false` en caso de error.
