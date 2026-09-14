---
title: stream_wrapper_unregister
description: Deja de registrar una envoltura de URL
source_url: https://www.php.net/manual/es/function.stream-wrapper-unregister.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-wrapper-unregister.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 525aa5f19
order: 88240
---

stream_wrapper_unregister

Deja de registrar una envoltura de URL

## Descripción

```php
stream_wrapper_unregister(string $protocol): bool
```php

Permite deshabilitar una envoltura de flujo ya definida. Una vez que la envoltura ha sido deshabilitada, se la puede sobreescribir con una envoltura definida por el usuario usando `stream_wrapper_register` o rehabilitándola después com `stream_wrapper_restore`.

## Parámetros

`protocol`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
