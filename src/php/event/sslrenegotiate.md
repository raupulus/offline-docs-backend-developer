---
title: EventBufferEvent::sslRenegotiate
description: Solicita al búfer de eventos iniciar una renegociación SSL
source_url: https://www.php.net/manual/es/eventbufferevent.sslrenegotiate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/sslrenegotiate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 19620
---

EventBufferEvent::sslRenegotiate

Solicita al búfer de eventos iniciar una renegociación SSL

## Descripción

```php
public EventBufferEvent::sslRenegotiate(): void
```php

Solicita al búfer de eventos iniciar una renegociación SSL.

> [!WARNING]
> La llamada a este método solicita a SSL una renegociación, y al búfer de eventos llamar a la función de retrollamada apropiada. Es un método muy avanzado; solo debe ser llamado si se sabe perfectamente lo que se hace, especialmente desde algunas versiones SSL donde se han actualizado fallas de seguridad durante la renegociación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
