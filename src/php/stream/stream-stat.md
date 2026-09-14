---
title: streamWrapper::stream_stat
description: Recuperar información sobre un recurso de archivo
source_url: https://www.php.net/manual/es/streamwrapper.stream-stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: c461c1fc7
order: 88500
---

streamWrapper::stream_stat

Recuperar información sobre un recurso de archivo

## Descripción

```php
public streamWrapper::stream_stat(): array
```php

Este método es llamado en respuesta a `fstat`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Véase `stat`.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

## Véase también

`stat`, streamwrapper::url_stat
