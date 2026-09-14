---
title: SessionHandler::read
description: Leer información de la sesión
source_url: https://www.php.net/manual/es/sessionhandler.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 4de6272a1
order: 74010
---

SessionHandler::read

Leer información de la sesión

## Descripción

```php
public SessionHandler::read(string $id): string
```php

Lee la información de la sesión desde el almacén de sesiones, y devuelve los resultados a PHP para su procesamiento interno. Este método es llamado automáticamente por PHP cuando se inicia una sesión (automáticamente o explícitamente con `session_start`) y está precedido por una llamada interna a la función `SessionHandler::open`.

Este método envuelve el gestor de almacenamiento interno de PHP definido en el ajuste ini [session.save_handler](#ini.session.save-handler) que fue establecido antes de que este gestor fuese establecido mediante `session_set_save_handler`.

Si esta clase se extiende por herencia, al llamar al método padre `read` invocará a la envoltura para este método y así invocará a la llamada de retorno interna asociada. Esto permite que el método sea sobrescrito y/o interceptado y filtrado (por ejemplo, desencriptando el valor de `data` devuelto por el método padre `read`).

Para más información sobre lo que se espera que haga este método, consulte la documentación de `SessionHandlerInterface::close`.

## Parámetros

`id`  
El id de sesión de donde leer la información.

## Valores devueltos

Devuelve una cadena codificada de la información leída. Si no se leyó nada, debe devolver `false`. Observe que este valor es devuelto internamente a PHP para su procesamiento.

## Véase también

La directiva de configuración [session.serialize_handler](#ini.session.serialize-handler).
