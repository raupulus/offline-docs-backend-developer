---
title: SessionHandler::destroy
description: Destruir una sesión
source_url: https://www.php.net/manual/es/sessionhandler.destroy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler/destroy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 4de6272a1
order: 73980
---

SessionHandler::destroy

Destruir una sesión

## Descripción

```php
public SessionHandler::destroy(string $id): bool
```php

Destruye una sesión. Llamado internamente por PHP con `session_regenerate_id` (se asume que `destroy` está establecido a `true`, mediante `session_destroy` o cuando `session_decode` falla.

Este método envuelve el gestor de almacenamiento interno de PHP definido en el ajuste ini [session.save_handler](#ini.session.save-handler) que fue establecido antes de que este gestor fuese establecido mediante `session_set_save_handler`.

Si esta clase se extiende por herencia, al llamar al método padre `destroy` invocará a la envoltura para este método y así invocará a la llamada de retorno interna asociada. Esto permite que este método sea sobrescrito y/o interceptado y filtrado.

Para más información sobre lo que se espera que haga este método, consulte la documentación de `SessionHandlerInterface::destroy`.

## Parámetros

`id`  
El ID de sesión a ser destruido.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.
