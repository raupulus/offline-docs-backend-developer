---
title: openal_listener_get
description: Devuelve una propiedad de oyente
source_url: https://www.php.net/manual/es/function.openal-listener-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-listener-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58820
---

openal_listener_get

Devuelve una propiedad de oyente

## Descripción

```php
openal_listener_get(int $property): mixed
```php

## Parámetros

`property`  
Propiedad para recuperar, una de: `AL_GAIN` (float), `AL_POSITION` (array(float,float,float)), `AL_VELOCITY` (array(float,float,float)) y `AL_ORIENTATION` (array(float,float,float)).

## Valores devueltos

Devuelve un flotante o un arreglo de flotantes (como apropiado) o `false` si ocurre un error.

## Véase también

openal_listener_set
