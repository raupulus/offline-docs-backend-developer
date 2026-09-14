---
title: cubrid_lob_close
description: Cerrar información BLOB/CLOB
source_url: https://www.php.net/manual/es/function.cubrid-lob-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9150
---

cubrid_lob_close

Cerrar información BLOB/CLOB

## Descripción

```php
cubrid_lob_close(array $lob_identifier_array): bool
```php

`cubrid_lob_close` se usa para cerrar todos los BLOB/CLOB devueltos desde `cubrid_lob_get`.

## Parámetros

`lob_identifier_array`  
Array de identificadores LOB devuelto desde `cubrid_lob_get`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_lob_close`

```
<?php
$conn = cubrid_connect ("localhost", 33000, "demodb", "dba");

cubrid_execute($conn,"DROP TABLE if exists doc");
cubrid_execute($conn,"CREATE TABLE doc (id INT, doc_content CLOB)");
cubrid_execute($conn,"INSERT INTO doc VALUES (5,'hello,cubrid')");

$lobs = cubrid_lob_get($conn, "SELECT doc_content FROM doc WHERE id=5");
echo "Tamaño del documento: ".cubrid_lob_size($lobs[0])." bytes";
cubrid_lob_export($conn, $lobs[0], "doc_5.txt");
cubrid_lob_close($lobs);
cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob_get

cubrid_lob_size

cubrid_lob_export

cubrid_lob_send
