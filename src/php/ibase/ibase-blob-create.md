---
title: ibase_blob_create
description: Crea un BLOB iBase para añadir datos
source_url: https://www.php.net/manual/es/function.ibase-blob-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30160
---

ibase_blob_create

Crea un BLOB iBase para añadir datos

## Descripción

```php
ibase_blob_create([resource $link_identifier]): resource
```php

`ibase_blob_create` crea un nuevo BLOB para llenar con datos, en la conexión InterBase `link_identifier`.

## Parámetros

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

## Valores devueltos

Devuelve un identificador de BLOB para usar con `ibase_blob_add` o `false` si ocurre un error.

## Véase también

ibase_blob_add

ibase_blob_cancel

ibase_blob_close

ibase_blob_import
