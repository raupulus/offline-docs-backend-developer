---
title: EventHttpRequest::cancel
description: Cancela una petición HTTP pendiente
source_url: https://www.php.net/manual/es/eventhttprequest.cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventhttprequest/cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 919c8a799
order: 20100
---

EventHttpRequest::cancel

Cancela una petición HTTP pendiente

## Descripción

```php
public EventHttpRequest::cancel(): void
```php

Cancela una petición HTTP pendiente.

Cancela una petición HTTP entrante. La retrollamada asociada con esta petición no será ejecutada, y el objeto de la petición, liberado. Si la petición está en curso de procesamiento, el objeto `EventHttpConnection` correspondiente será re-inicializado.

Una petición no puede ser cancelada si su retrollamada ya ha sido ejecutada. Una petición puede ser cancelada desde su retrollamada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
