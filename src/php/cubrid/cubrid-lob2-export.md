---
title: cubrid_lob2_export
description: Exporta un objeto LOB a un fichero
source_url: https://www.php.net/manual/es/function.cubrid-lob2-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9220
---

cubrid_lob2_export

Exporta un objeto LOB a un fichero

## Descripción

```php
cubrid_lob2_export(resource $lob_identifier, string $file_name): bool
```php

La función `cubrid_lob2_export` se utiliza para guardar los datos BLOB/CLOB en un fichero. Para utilizar esta función, primero debe utilizarse la función `cubrid_lob2_new` o recuperarse un objeto LOB desde la base de datos CUBRID. Si el fichero no existe, la operación fallará. Esta función no modificará la posición del cursor del objeto LOB. Opera sobre el objeto LOB en su totalidad.

## Parámetros

`lob_identifier`  
Un identificador LOB resultante de la función `cubrid_lob2_new` o recuperado desde el juego de resultados.

`filename`  
Nombre del fichero en el cual se desean guardar los datos BLOB/CLOB. La ruta hacia el fichero también puede ser especificada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

`cubrid_lob2_export` ejemplo

```
<?php
// Tabla : test_lob (id INT, contents CLOB)

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists doc");
cubrid_execute($conn,"CREATE TABLE doc (id INT, doc_content CLOB)");
cubrid_execute($conn,"INSERT INTO doc VALUES (5,'hello,cubrid')");

$req = cubrid_prepare($conn, "select * from doc");

cubrid_execute($req);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);

$row = cubrid_fetch($req, CUBRID_NUM | CUBRID_LOB);

cubrid_lob2_export($row[1], "doc_3.txt");

cubrid_lob2_close($row[1]);
cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_new

cubrid_lob2_close

cubrid_lob2_import

cubrid_lob2_bind
