---
title: SessionHandlerInterface::read
description: Leer información de sesión
source_url: https://www.php.net/manual/es/sessionhandlerinterface.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 601f6f4ce
order: 74080
---

SessionHandlerInterface::read

Leer información de sesión

## Descripción

```php
public SessionHandlerInterface::read(string $id): string
```php

Lee la información de sesión desde el almacenamiento de sesiones, y devuelve el resultado. Llamado justo después de iniciarse una sesión o cuando es llamada `session_start`. Observe que antes de que este método sea llamado `SessionHandlerInterface::open` es invocado.

Este método es llmado por PHP cuando la sesión es iniciada. Este método debería recuperar la información de sesión desde el almacenamiento mediante el ID de sesión proporcionado. La cadena devuelta por este método debe estar en el mismo formato serializado que el orgibal pasado a `SessionHandlerInterface::write` Si no se encuentra el registro, devuelve `false`.

La información devuelta por este método será decodificada internamente por PHP usando el método de deserialización especificado en [session.serialize_handler](#ini.session.serialize-handler). La información resultante será usada para rellenar la variable superglobal `$_SESSION`.

Observe que el esquema de serialización no es el mismo que `unserialize` y pudede accederse a él mediante `session_decode`.

## Parámetros

`id`  
El ID de sesión.

## Valores devueltos

Devuelve una cadena codificada de la información leída. Si no se leyó nada, debe devolver `false`. Observe que este valor es devuelto internamente por PHP para procesamiento.

## Véase también

La directiva de configuración [session.serialize_handler](#ini.session.serialize-handler).
