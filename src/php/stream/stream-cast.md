---
title: streamWrapper::stream_cast
description: Recuperar el recurso subyacente
source_url: https://www.php.net/manual/es/streamwrapper.stream-cast.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-cast.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: d01c05339
order: 88400
---

streamWrapper::stream_cast

Recuperar el recurso subyacente

## Descripción

```php
public streamWrapper::stream_cast(int $cast_as): resource
```php

Esta función es llamada en respuesta a `stream_select`.

## Parámetros

`cast_as`  
Puede ser una de las siguientes valores: `STREAM_CAST_FOR_SELECT` si `stream_select` es la función que llama `stream_cast` o `STREAM_CAST_AS_STREAM` si `stream_cast` es llamada para los otros casos.

## Valores devueltos

Debe devolver el flujo subyacente, utilizado por el gestor, y en caso contrario `false`.

## Véase también

`stream_select`
