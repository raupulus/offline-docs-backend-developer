---
title: SessionHandler::gc
description: Limpia las sesiones antiguas
source_url: https://www.php.net/manual/es/sessionhandler.gc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler/gc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 601f6f4ce
order: 73990
---

SessionHandler::gc

Limpia las sesiones antiguas

## Descripción

```php
public SessionHandler::gc(int $max_lifetime): int
```php

Limpia las sesiones expiradas. Se llama aleatoriamente en el interior de PHP cuando una sesión comienza o cuando se llama a la función `session_start`. La frecuencia de llamada se basa en las directivas de configuración [session.gc_divisor](#ini.session.gc-divisor) y [session.gc_probability](#ini.session.gc-probability).

Este método reemplaza al gestor interno de almacenamiento de PHP definido a través de la opción de configuración [session.save_handler](#ini.session.save-handler) que se ha definido antes de que este último se defina a través de la función `session_set_save_handler`.

Si esta clase se extiende por herencia, la llamada al método padre `gc` invocará el envoltorio para este método, pero también invocará internamente la función de devolución de llamada asociada. Este comportamiento permite que este método se sobreescriba o bien se intercepte y filtre.

Para más información sobre lo esperado de este método, consulte la documentación sobre la función `SessionHandlerInterface::gc`.

## Parámetros

`max_lifetime`  
Las sesiones que no se hayan actualizado durante las últimas `max_lifetime` segundos serán eliminadas.

## Valores devueltos

Devuelve el número de sesiones eliminadas en caso de éxito, o `false` si ocurre un error. Nota que este valor se devuelve internamente a PHP para su procesamiento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | Antes de esta versión, esta función devolvía `true` en caso de éxito. |
