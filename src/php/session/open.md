---
title: SessionHandler::open
description: Inicializar una sesión
source_url: https://www.php.net/manual/es/sessionhandler.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandler/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 601f6f4ce
order: 74000
---

SessionHandler::open

Inicializar una sesión

## Descripción

```php
public SessionHandler::open(string $path, string $name): bool
```php

Crea una nueva sesión, o reinicializa una sesión existente. Es llamado internamente por PHP cuando se inicia una sesión automáticamente o cuando se invoca a `session_start`.

Este método envuelve el gestor de almacenamiento interno de PHP definido en el ajuste ini [session.save_handler](#ini.session.save-handler) que fue establecido antes de que este gestor fuese establecido mediante `session_set_save_handler`.

Si esta clase se extiende por herencia, al llamar al método padre `open` invocará a la envoltura para este método y así invocará a la llamada de retorno interna asociada. Esto permite que este método sea sobrescrito y/o interceptado.

Para más información sobre lo que puede hacer este método, consulte la documentación de `SessionHandlerInterface::open`.

## Parámetros

`path`  
La ruta donde almacenar/recuperar la sesión.

`name`  
El nombre de la sesión.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.

## Véase también

La directiva de configuración [session.auto-start](#ini.session.auto-start).
