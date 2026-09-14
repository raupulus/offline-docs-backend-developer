---
title: streamWrapper::rename
description: Renombra un archivo o directorio
source_url: https://www.php.net/manual/es/streamwrapper.rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 472ea1fc2
order: 88380
---

streamWrapper::rename

Renombra un archivo o directorio

## Descripción

```php
public streamWrapper::rename(string $path_from, string $path_to): bool
```php

Este método es llamado en respuesta a `rename`.

Debería intentar renombrar `path_from` a `path_to`

> [!NOTE]
> Para que el mensaje de error apropiado sea devuelto, este método *no* debería ser definido si la envoltura no soporta el renombramiento de archivos.

## Parámetros

`path_from`  
La URL al archivo actual.

`path_to`  
La URL que debería ser renombrada por `path_from`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Notas

> [!NOTE]
> La propiedad `streamWrapper::$context` es actualizada si un contexto válido es pasado a la función.

## Véase también

`rename`
