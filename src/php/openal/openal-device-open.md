---
title: openal_device_open
description: Inicia la capa de audio del OpenAL
source_url: https://www.php.net/manual/es/function.openal-device-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-device-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58810
---

openal_device_open

Inicia la capa de audio del OpenAL

## Descripción

```php
openal_device_open([string $device_desc]): resource
```php

## Parámetros

`device_desc`  
Abre un dispositivo de audio especiado opcionalmente por `device_desc`. Si `device_desc` no está especificado el primer dispositivo de audio disponible será usado.

## Valores devueltos

Devuelve un recurso [Open AL(Device)](#openal.resources) en éxito o `false` en fallo.

## Véase también

openal_device_close

openal_context_create
