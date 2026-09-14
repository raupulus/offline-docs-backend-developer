---
title: SessionHandler::close
description: Cerrar la sesión
source_url: https://www.php.net/manual/es/sessionhandler.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 601f6f4ce
order: 73960
---

SessionHandler::close

Cerrar la sesión

## Descripción

```php
public SessionHandler::close(): bool
```php

Cierra la sesión actual. Este método es ejecutado de forma automática internamente por PHP al cerrar la sesión, o explícitamente mediante la función `session_write_close` (la cual llama primero a la función `SessionHandler::write`).

Este método envuelve el gestor de almacenamiento interno de PHP definido en el ajuste ini [session.save_handler](#ini.session.save-handler) que fue establecido antes de que este gestor fuese activado mediante `session_set_save_handler`.

Si esta clase se extiende por herencia, al llamar al método padre `close` invocará a la envoltura para este método y así invocará a la llamada de retorno interna asociada. Esto permite que el método sea sobrescrito y/o interceptado.

Para más información sobre lo que se espera que haga este método, consulte la documentación de `SessionHandlerInterface::close`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.
