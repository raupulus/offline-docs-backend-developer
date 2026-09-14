---
title: SessionHandlerInterface::gc
description: Limpia las sesiones antiguas
source_url: https://www.php.net/manual/es/sessionhandlerinterface.gc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface/gc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 601f6f4ce
order: 74060
---

SessionHandlerInterface::gc

Limpia las sesiones antiguas

## Descripción

```php
public SessionHandlerInterface::gc(int $max_lifetime): int
```php

Limpia las sesiones antiguas expiradas. Es llamada por `session_start`, en función de [session.gc_divisor](#ini.session.gc-divisor), [session.gc_probability](#ini.session.gc-probability) y [session.gc_maxlifetime](#ini.session.gc-maxlifetime).

## Parámetros

`max_lifetime`  
Las sesiones que no han sido actualizadas durante las últimas `max_lifetime` segundos serán eliminadas.

## Valores devueltos

Devuelve el número de sesiones eliminadas en caso de éxito, o `false` si ocurre un error. Nota que este valor se devuelve internamente a PHP para su procesamiento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | Antes de esta versión, la función devolvía `true` en caso de éxito. |
