---
title: streamWrapper::unlink
description: Borrar un archivo
source_url: https://www.php.net/manual/es/streamwrapper.unlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/unlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: af4410a7e
order: 88540
---

streamWrapper::unlink

Borrar un archivo

## Descripción

```php
public streamWrapper::unlink(string $path): bool
```php

Este método es llamado en respuesta a `unlink`.

> [!NOTE]
> Para que el mensaje de error apropiado sea devuelto, este método *no* debería ser definido si la envoltura no soporta la eliminación de archivos.

## Parámetros

`path`  
LA URL del archivo que debería ser borrado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Notas

> [!NOTE]
> La propiedad `streamWrapper::$context` es actualizada si un contexto válido es pasado a la función.

## Véase también

`unlink`, streamWrapper::rmdir
