---
title: cubrid_lob_get
description: Recupera los datos BLOB/CLOB
source_url: https://www.php.net/manual/es/function.cubrid-lob-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9170
---

cubrid_lob_get

Recupera los datos BLOB/CLOB

## Descripción

```php
cubrid_lob_get(resource $conn_identifier, string $sql): array
```php

La función `cubrid_lob_get` se utiliza para recuperar los datos de información meta BLOB/CLOB desde la base de datos CUBRID (CUBRID recupera los BLOB/CLOB ejecutando una consulta SQL), y devuelve todos los LOBs en forma de un array de recursos. Asegúrese de que el SQL recupere únicamente una columna y que el tipo de datos sea BLOB o CLOB.

Tenga en cuenta que el uso de la función `cubrid_lob_close` libera los LOBs si ya no son necesarios.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`sql`  
Consulta SQL a ejecutar.

## Valores devueltos

Devuelve un array de recursos LOB en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lob_get`

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

cubrid_lob_close

cubrid_lob_size

cubrid_lob_export

cubrid_lob_send
