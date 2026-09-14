---
title: cubrid_lob_export
description: Exporta datos BLOB/CLOB a un fichero
source_url: https://www.php.net/manual/es/function.cubrid-lob-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9160
---

cubrid_lob_export

Exporta datos BLOB/CLOB a un fichero

## Descripción

```php
cubrid_lob_export(resource $conn_identifier, resource $lob_identifier, string $path_name): bool
```php

La función `cubrid_lob_export` se utiliza para recuperar los datos BLOB/CLOB desde la base de datos CUBRID, y guardar sus contenidos en un fichero. Para utilizar esta función, es necesario utilizar primero la función `cubrid_lob_get` para recuperar las informaciones de los BLOB/CLOB desde CUBRID.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`lob_identifier`  
Identificador LOB.

`path_name`  
Ruta hacia el fichero.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lob_export`

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

cubrid_lob_close

cubrid_lob_size

cubrid_lob_send
