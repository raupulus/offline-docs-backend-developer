---
title: streamWrapper::rmdir
description: Elimina un directorio
source_url: https://www.php.net/manual/es/streamwrapper.rmdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/rmdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 472ea1fc2
order: 88390
---

streamWrapper::rmdir

Elimina un directorio

## Descripción

```php
public streamWrapper::rmdir(string $path, int $options): bool
```php

Este método es llamado en respuesta a `rmdir`.

> [!NOTE]
> Para que el mensaje de error apropiado sea devuelto, este método *no* debería ser definido si la envoltura no soporta la eliminación de directorios.

## Parámetros

`path`  
La URL del directorio que debería ser eliminado.

`options`  
Una máscara a nivel de bits de valores, como `STREAM_MKDIR_RECURSIVE`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Notas

> [!NOTE]
> La propiedad `streamWrapper::$context` es actualizada si un contexto válido es pasado a la función.

## Véase también

`rmdir`, streamwrapper::mkdir, streamwrapper::unlink
