---
title: ibase_blob_info
description: Devuelve el tamaño de un BLOB iBase y otra información útil
source_url: https://www.php.net/manual/es/function.ibase-blob-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30200
---

ibase_blob_info

Devuelve el tamaño de un BLOB iBase y otra información útil

## Descripción

```php
ibase_blob_info(resource $link_identifier, string $blob_id): array
```php

```php
ibase_blob_info(string $blob_id): array
```

Devuelve el tamaño de un BLOB iBase y otra información útil.

## Parámetros

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

`blob_id`  
El identificador del BLOB.

## Valores devueltos

Devuelve un array que contiene información sobre el BLOB `blob_id`. La información incluye el tamaño del BLOB, el número de segmentos que contiene, el tamaño del segmento más grande y si se trata de un BLOB stream o segmentado.
