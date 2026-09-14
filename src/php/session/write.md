---
title: SessionHandler::write
description: Escribir información de sesión
source_url: https://www.php.net/manual/es/sessionhandler.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 4de6272a1
order: 74020
---

SessionHandler::write

Escribir información de sesión

## Descripción

```php
public SessionHandler::write(string $id, string $data): bool
```php

Escribe la información de la sesión en el almacén de sesiones. Es llamado por el cierre normal de PHP, por `session_write_close`, o cuando `session_register_shutdown` falla. PHP llamará a `SessionHandler::close` inmediatamente después de que este método devuelva.

Este método envuelve el gestor de almacenamiento interno de PHP definido en el ajuste ini [session.save_handler](#ini.session.save-handler) que fue establecido antes de que este gestor fuese establecido mediante `session_set_save_handler`.

Si esta clase se extiende por herencia, al llamar al método padre `write` invocará a la envoltura para este método y así invocará a la llamada de retorno interna asociada. Esto permite que este método sea sobrescrito y/o interceptado y filtrado (por ejemplo, encriptando el valor de `data` antes de enviarlo al método padre `write`).

Para más información sobre lo que se espera que haga este método, consulte la documentación de `SessionHandlerInterface::write`.

## Parámetros

`id`  
El id de la sesión.

`data`  
La información de sesión codificada. Esta información es el resultado de codificar internamente la variable superglobal `$_SESSION` a una cadena serializada y pasarla como este parámetro. Observe que las sesiones usan un método de serialización alternativo.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.

## Véase también

La directiva de configuración [session.serialize_handler](#ini.session.serialize-handler).
