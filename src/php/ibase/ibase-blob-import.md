---
title: ibase_blob_import
description: Crea un BLOB iBase, copia un fichero y lo cierra
source_url: https://www.php.net/manual/es/function.ibase-blob-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-blob-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30190
---

ibase_blob_import

Crea un BLOB iBase, copia un fichero y lo cierra

## Descripción

```php
ibase_blob_import(resource $link_identifier, resource $file_handle): string
```php

```php
ibase_blob_import(resource $file_handle): string
```

`ibase_blob_import` crea un nuevo BLOB en la conexión iBase `link_identifier`, copia el fichero `file_handle` en su totalidad, lo cierra y devuelve el identificador asignado

## Parámetros

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

`file_handle`  
El recurso de fichero, devuelto por la función `fopen`.

## Valores devueltos

Devuelve el identificador del BLOB en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ibase_blob_import`

```php
<?php
$dbh = ibase_connect($host, $username, $password);
$filename = '/tmp/bar';

$fd = fopen($filename, 'r');
if ($fd) {

    $blob = ibase_blob_import($dbh, $fd);
    fclose($fd);

    if (!is_string($blob)) {
        // fallo en la importación
    } else {
        $query = "INSERT INTO foo (name, data) VALUES ('$filename', ?)";
        $prepared = ibase_prepare($dbh, $query);
        if (!ibase_execute($prepared, $blob)) {
            // fallo en la inserción del registro
        }
    }
} else {
    // imposible abrir el fichero
}
?>

   
```

## Véase también

ibase_blob_add

ibase_blob_cancel

ibase_blob_close

ibase_blob_create
