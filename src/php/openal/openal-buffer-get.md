---
title: openal_buffer_get
description: Obtiene las propiedades del buffer OpenAL
source_url: https://www.php.net/manual/es/function.openal-buffer-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-buffer-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_reviewed: false
translation_revision: c55b13c1a
order: 58730
---

openal_buffer_get

Obtiene las propiedades del buffer OpenAL

## Descripción

```php
openal_buffer_get(resource $buffer, int $property): int
```php

## Parámetros

`buffer`  
Un recurso [Open AL(Buffer)](#openal.resources) (creado previamente por `openal_buffer_create`).

`property`  
Una propiedad específica, una de las siguientes: `AL_FREQUENCY`, `AL_BITS`, `AL_CHANNELS` y `AL_SIZE`.

## Valores devueltos

Devuelve un valor entero apropiado para la propiedad solicitada `property` o `false` si ocurre un error.

## Véase también

openal_buffer_create
