---
title: EventBase::__construct
description: Construye un objeto EventBase
source_url: https://www.php.net/manual/es/eventbase.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: b621ab27a
order: 19010
---

EventBase::\_\_construct

Construye un objeto EventBase

## Descripción

```php
public EventBase::__construct([EventConfig $cfg])
```php

Construye un objeto EventBase.

## Parámetros

`cfg`  
Opcional - Un objeto `EventConfig`.

## Errores/Excepciones

Si `EventBase` no puede ser construido con la configuración proporcionada, se lanzará una excepción de tipo `EventException`.

## Véase también

EventConfig
