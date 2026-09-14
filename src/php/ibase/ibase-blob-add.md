---
title: ibase_blob_add
description: Añade datos a un BLOB iBase recién creado
source_url: https://www.php.net/manual/es/function.ibase-blob-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30130
---

ibase_blob_add

Añade datos a un BLOB iBase recién creado

## Descripción

```php
ibase_blob_add(resource $blob_handle, string $data): void
```php

`ibase_blob_add` añade los datos `data` al BLOB `blob_handle`, creado con `ibase_blob_create`.

## Parámetros

`blob_handle`  
Un recurso blob, abierto con la función `ibase_blob_create`.

`data`  
Los datos a añadir.

## Valores devueltos

No se retorna ningún valor.

## Véase también

ibase_blob_cancel

ibase_blob_close

ibase_blob_create

ibase_blob_import
