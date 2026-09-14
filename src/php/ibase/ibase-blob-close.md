---
title: ibase_blob_close
description: Cierra un BLOB iBase
source_url: https://www.php.net/manual/es/function.ibase-blob-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30150
---

ibase_blob_close

Cierra un BLOB iBase

## Descripción

```php
ibase_blob_close(resource $blob_handle): mixed
```php

`ibase_blob_close` cierra el BLOB `blob_handle`, abierto en lectura con `ibase_open_blob` o en escritura con `ibase_blob_create`.

## Parámetros

`blob_handle`  
Un recurso blob, abierto con la función `ibase_blob_create` o la función `ibase_blob_open`.

## Valores devueltos

Si el BLOB fue leído, `ibase_blob_close` devuelve `true` en caso de éxito, si estaba siendo modificado, `ibase_blob_close` devuelve un string que contiene el identificador del BLOB que le fue asignado por la base de datos. En caso de fallo, esta función devolverá `false`.

## Véase también

ibase_blob_cancel

ibase_blob_open
