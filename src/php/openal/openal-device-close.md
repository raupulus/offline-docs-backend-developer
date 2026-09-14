---
title: openal_device_close
description: Cierra un dispositivo OpenAL
source_url: https://www.php.net/manual/es/function.openal-device-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-device-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58800
---

openal_device_close

Cierra un dispositivo OpenAL

## Descripción

```php
openal_device_close(resource $device): bool
```php

## Parámetros

`device`  
Un recurso [Open AL(Device)](#openal.resources) (previamente creado por `openal_device_open`) para ser cerrado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_device_open
