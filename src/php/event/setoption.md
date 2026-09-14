---
title: EventDnsBase::setOption
description: Define el valor de una opción de configuración
source_url: https://www.php.net/manual/es/eventdnsbase.setoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/setoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19810
---

EventDnsBase::setOption

Define el valor de una opción de configuración

## Descripción

```php
public EventDnsBase::setOption(string $option, string $value): bool
```php

Define el valor de una opción de configuración.

## Parámetros

`option`  
Las opciones de configuración actualmente disponibles son: `"ndots"`, `"timeout"`, `"max-timeouts"`, `"max-inflight"` y `"attempts"`.

`value`  
El valor de la opción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
