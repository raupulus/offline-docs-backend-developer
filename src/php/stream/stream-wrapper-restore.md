---
title: stream_wrapper_restore
description: Restablece una envoltura incluida que se dejó de registrar previamente
source_url: https://www.php.net/manual/es/function.stream-wrapper-restore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-wrapper-restore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 96c9d88ba
order: 88230
---

stream_wrapper_restore

Restablece una envoltura incluida que se dejó de registrar previamente

## Descripción

```php
stream_wrapper_restore(string $protocol): bool
```php

Restablece una envoltura incluida que se dejó de registrar previamente con `stream_wrapper_unregister`.

## Parámetros

`protocol`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
