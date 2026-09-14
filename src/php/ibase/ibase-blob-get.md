---
title: ibase_blob_get
description: Lee len bytes de datos en un BLOB iBase abierto
source_url: https://www.php.net/manual/es/function.ibase-blob-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30180
---

ibase_blob_get

Lee

len

bytes de datos en un BLOB iBase abierto

## Descripción

```php
ibase_blob_get(resource $blob_handle, int $len): string
```php

`ibase_blob_get` devuelve como máximo `len` bytes del BLOB `blob_handle` que ha sido abierto en lectura por `ibase_blob_open`.

> [!NOTE]
> No es posible leer en un BLOB abierto en escritura por `ibase_blob_create`.

## Parámetros

`blob_handle`  
Un recurso blob, abierto con la función `ibase_blob_open`.

`len`  
El tamaño de los datos devueltos.

## Valores devueltos

Devuelve como máximo, `len` bytes del BLOB, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ibase_blob_get`

```
<?php
$result    = ibase_query("SELECT blob_value FROM table");
$data      = ibase_fetch_object($result);
$blob_data = ibase_blob_info($data->BLOB_VALUE);
$blob_hndl = ibase_blob_open($data->BLOB_VALUE);
echo         ibase_blob_get($blob_hndl, $blob_data[0]);
?>

    
```php

Este ejemplo no hace más que un `ibase_blob_echo( $data->BLOB_VALUE )`, pero muestra cómo recuperar la información en una \$variable para manipularla como se desee.

## Véase también

ibase_blob_open

ibase_blob_close

ibase_blob_echo
