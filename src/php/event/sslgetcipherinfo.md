---
title: EventBufferEvent::sslGetCipherInfo
description: Devuelve una descripción textual de un cipher
source_url: https://www.php.net/manual/es/eventbufferevent.sslgetcipherinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslgetcipherinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 19580
---

EventBufferEvent::sslGetCipherInfo

Devuelve una descripción textual de un cipher

## Descripción

```php
public EventBufferEvent::sslGetCipherInfo(): string
```php

Recupera la descripción del cipher actual a través de la función `SSL_CIPHER_description` de la API SSL (ver la página man de *SSL_CIPHER_get_name(3)*).

> [!NOTE]
> Esta función solo está disponible si `Event` ha sido compilado con soporte OpenSSL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una descripción textual del cipher en caso de éxito, o bien `false` si ocurre un error.
