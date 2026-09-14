---
title: streamWrapper::stream_truncate
description: Truncar un flujo
source_url: https://www.php.net/manual/es/streamwrapper.stream-truncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-truncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 94497636f
order: 88520
---

streamWrapper::stream_truncate

Truncar un flujo

## Descripción

```php
public streamWrapper::stream_truncate(int $new_size): bool
```php

Responderá a la truncación, p.ej. a través de `ftruncate`.

## Parámetros

`new_size`  
El nuevo tamaño.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ftruncate`
