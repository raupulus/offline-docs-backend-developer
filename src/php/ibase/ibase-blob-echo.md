---
title: ibase_blob_echo
description: Muestra el contenido de un BLOB iBase en el navegador
source_url: https://www.php.net/manual/es/function.ibase-blob-echo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-echo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30170
---

ibase_blob_echo

Muestra el contenido de un BLOB iBase en el navegador

## Descripción

```php
ibase_blob_echo(string $blob_id): bool
```php

```php
ibase_blob_echo(resource $link_identifier, string $blob_id): bool
```

`ibase_blob_echo` abre el BLOB `blob_id` en lectura y envía su contenido directamente a la salida estándar (el navegador en la mayoría de los casos).

## Parámetros

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

`blob_id`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_blob_open

ibase_blob_close

ibase_blob_get
