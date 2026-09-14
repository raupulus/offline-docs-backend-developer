---
title: streamWrapper::stream_open
description: Abre un archivo o una URL
source_url: https://www.php.net/manual/es/streamwrapper.stream-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: a6afc9550
order: 88460
---

streamWrapper::stream_open

Abre un archivo o una URL

## Descripción

```php
public streamWrapper::stream_open(string $path, string $mode, int $options, string $opened_path): bool
```php

Este método es llamado inmediatemente después de que la envoltura sea inicializada (p.ej. usando `fopen` y `file_get_contents`).

## Parámetros

`path`  
Especifica la URL que fue pasada a la función original.

> [!NOTE]
> La URL se puede desmontar con `parse_url`. Observe que sólo las URL delimitadas por :// están soportadas. : y :/ aunque técnicamente son URL válidas, no lo están.

`mode`  
El modo usado para abrir el archivo, como está detallado en `fopen`.

> [!NOTE]
> Recuerde verificar si `mode` es válido para la ruta `path` solicitada.

`options`  
Contiene banderas adicionales establecidas por la API de flujos. Puede contener uno o más de los siguientes valores usando OR entre ellos.

| Bandera | Descripción |
|----|----|
| `STREAM_USE_PATH` | Si la ruta `path` es relativa, se busca el recurso usando include_path. |
| `STREAM_REPORT_ERRORS` | Si está establecida esta bandera, uno mismo es responsble de lanzar errores usando `trigger_error` durante la apertura del flujo. Si esta bandera no está establecida, no se debería lanzar ningún error. |

`opened_path`  
Si la ruta `path` es abierta con éxito, y `STREAM_USE_PATH` está establecido en `options`, `opened_path` debería ser establecido a la ruta completa del archivo/recurso que fue abierto realmente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Notas

> [!NOTE]
> La propiedad `streamWrapper::$context` es actualizada si un contexto válido es pasado a la función.

## Véase también

`fopen`, `parse_url`
