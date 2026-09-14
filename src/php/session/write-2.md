---
title: SessionHandlerInterface::write
description: Escribir información de sesión
source_url: https://www.php.net/manual/es/sessionhandlerinterface.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 601f6f4ce
order: 74090
---

SessionHandlerInterface::write

Escribir información de sesión

## Descripción

```php
public SessionHandlerInterface::write(string $id, string $data): bool
```php

Escribe información de sesión al almacenamiento de sesiones. Llamado por `session_write_close`, cuando `session_register_shutdown` falla, o durante un cierre normal. Nota: `SessionHandlerInterface::close` es llamado inmediantamente después de esta función.

PHP llamará a este método cuando la sesión esté lista para ser almacenada y cerrada. Codifica la información de sesión desde la variable superglobal `$_SESSION` a una cadena serializada y la pasa junto con el ID de sersión a este método para el almacenamiento. El método de serialización usado está especificado en la configuración [session.serialize_handler](#ini.session.serialize-handler).

Observe que este método normalmente es llamado por PHP después de que los buffers de salida hayan sido cerrados a menos que se llame explícitamente a `session_write_close`

## Parámetros

`id`  
El ID de sesión.

`data`  
La información de sesión codificada. Esta información es el resultado de que PHP codifique internamente la variable supergobal `$_SESSION` a una cadena serializada y pasarla a este parámetro. Observe que las sesiones usan un método de serialización alternativo.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.

## Véase también

La directiva de configuración [session.serialize_handler](#ini.session.serialize-handler).
