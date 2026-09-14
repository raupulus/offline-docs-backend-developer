---
title: ssh2_send_eof
description: Envía un EOF al flujo
source_url: https://www.php.net/manual/es/function.ssh2-send-eof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-send-eof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86620
---

ssh2_send_eof

Envía un EOF al flujo

## Descripción

```php
ssh2_send_eof(resource $channel): bool
```php

Envía un EOF al flujo; esto se utiliza típicamente para cerrar la entrada estándar, manteniendo abiertas la salida y los errores. Por ejemplo, se pueden enviar datos a un proceso remoto en la entrada estándar, cerrarla para comenzar el procesamiento, y aún ser capaz de leer los resultados sin crear ficheros adicionales.

## Parámetros

`channel`  
Un flujo SSH; puede ser adquirido por funciones como `ssh2_fetch_stream` o `ssh2_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ssh2_fetch_stream
