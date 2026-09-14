---
title: openal_buffer_loadwav
description: Carga un archivo .wav dentro de un buffer
source_url: https://www.php.net/manual/es/function.openal-buffer-loadwav.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-buffer-loadwav.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58740
---

openal_buffer_loadwav

Carga un archivo .wav dentro de un buffer

## Descripción

```php
openal_buffer_loadwav(resource $buffer, string $wavfile): bool
```php

## Parámetros

`buffer`  
Un recurso [Open AL(Buffer)](#openal.resources) (previamente creado por `openal_buffer_create`).

`wavfile`  
Ruta al archivo `.wav` en el sistema de archivo *local*.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_buffer_data

openal_stream
