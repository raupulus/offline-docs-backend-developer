---
title: fbird_blob_cancel
description: Cancela la creación de un blob
source_url: https://www.php.net/manual/es/function.fbird-blob-cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/fbird-blob-cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 29660
---

fbird_blob_cancel

Cancela la creación de un blob

## Descripción

```php
fbird_blob_cancel(resource $blob_handle): bool
```php

Esta función descartará un BLOB si no ha sido cerrado aún por `fbird_blob_close`.

## Parámetros

`blob_handle`  
Un gestor de BLOB abierto con `fbird_blob_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

fbird_blob_close

fbird_blob_create

fbird_blob_import
