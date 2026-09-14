---
title: ibase_blob_open
description: Abre un BLOB iBase para recuperar partes de datos
source_url: https://www.php.net/manual/es/function.ibase-blob-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30210
---

ibase_blob_open

Abre un BLOB iBase para recuperar partes de datos

## Descripción

```php
ibase_blob_open(resource $link_identifier, string $blob_id): resource
```php

```php
ibase_blob_open(string $blob_id): resource
```

Abre un BLOB iBase para recuperar partes de datos.

## Parámetros

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

`blob_id`  
El identificador del BLOB.

## Valores devueltos

Devuelve un recurso BLOB para su uso con la función `ibase_blob_get` o `false` si ocurre un error.

## Véase también

ibase_blob_close

ibase_blob_echo

ibase_blob_get
