---
title: ibase_blob_cancel
description: Cancela la creación de un BLOB iBase
source_url: https://www.php.net/manual/es/function.ibase-blob-cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30140
---

ibase_blob_cancel

Cancela la creación de un BLOB iBase

## Descripción

```php
ibase_blob_cancel(resource $blob_handle): bool
```php

`ibase_blob_cancel` cancela la creación del BLOB `blob_handle`, creado por `ibase_blob_create` si no ha sido cerrado aún con `ibase_blob_close`.

## Parámetros

`blob_handle`  
Un recurso blob, abierto con la función `ibase_blob_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_blob_close

ibase_blob_create

ibase_blob_import
