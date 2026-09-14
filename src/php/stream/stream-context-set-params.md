---
title: stream_context_set_params
description: Configura los parámetros para un flujo/gestor/contexto
source_url: https://www.php.net/manual/es/function.stream-context-set-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-context-set-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: d715365c0
order: 87890
---

stream_context_set_params

Configura los parámetros para un flujo/gestor/contexto

## Descripción

```php
stream_context_set_params(resource $context, array $params): true
```php

`stream_context_set_params` define los parámetros para el contexto especificado.

## Parámetros

`context`  
El flujo o contexto al que se aplican los parámetros.

`params`  
Un array asociativo de parámetros a definir en el formato siguiente: `$params['paramname'] = "paramvalue";`.

| Parámetro | Uso |
|----|----|
| `notification` | Nombre de la función de retrollamada definida por el usuario llamada cuando un flujo genera una notificación. Admitido únicamente por las envolturas de flujo [http://](#wrappers.http) y [ftp://](#wrappers.ftp). |
| `options` | Un array de opciones, como para las [opciones y parámetros de contexto](#context). |

Parámetros admitidos

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

stream_notification_callback
