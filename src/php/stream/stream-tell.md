---
title: streamWrapper::stream_tell
description: Recuperar la posición actual de un flujo
source_url: https://www.php.net/manual/es/streamwrapper.stream-tell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-tell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 99e65b7ae
order: 88510
---

streamWrapper::stream_tell

Recuperar la posición actual de un flujo

## Descripción

```php
public streamWrapper::stream_tell(): int
```php

Este método es llamado en respuesta a `fseek` para determinar la posición actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Debería devolver la posición actual del flujo.

## Véase también

`ftell`
