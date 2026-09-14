---
title: EventBufferEvent::sslGetCipherVersion
description: Devuelve la versión del cipher utilizado para la conexión SSL actual
source_url: https://www.php.net/manual/es/eventbufferevent.sslgetcipherversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslgetcipherversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 19600
---

EventBufferEvent::sslGetCipherVersion

Devuelve la versión del cipher utilizado para la conexión SSL actual

## Descripción

```php
public EventBufferEvent::sslGetCipherVersion(): string
```php

Recupera la versión del cipher utilizado para la conexión SSL actual.

> [!NOTE]
> Esta función solo está disponible si `Event` ha sido compilado con soporte OpenSSL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la versión del cipher utilizado para la conexión SSL actual o `false` en caso de error.
