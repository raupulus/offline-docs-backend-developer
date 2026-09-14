---
title: cubrid_lob2_import
description: Importa datos BLOB/CLOB desde un fichero
source_url: https://www.php.net/manual/es/function.cubrid-lob2-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 9230
---

cubrid_lob2_import

Importa datos BLOB/CLOB desde un fichero

## Descripción

```php
cubrid_lob2_import(resource $lob_identifier, string $file_name): bool
```php

La función `cubrid_lob2_import` se utiliza para importar datos BLOB/CLOB desde un fichero. Para utilizar esta función, primero debe utilizarse la función `cubrid_lob2_new` o recuperarse un objeto LOB desde la base de datos CUBRID. Si el fichero no existe, la operación fallará. Esta función no afecta a la posición del cursor en el objeto LOB; opera sobre el objeto LOB en su totalidad.

## Parámetros

`lob_identifier`  
Un identificador LOB, resultado de la función `cubrid_lob2_new` o recuperado desde el juego de resultados.

`filename`  
El nombre del fichero desde el cual los datos BLOB/CLOB deben ser importados. La ruta hacia el fichero también es soportada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lob2_export`

```
<?php

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists test_lob");
cubrid_execute($conn,"CREATE TABLE test_lob (id INT, contents CLOB)");

$req = cubrid_prepare($conn, "INSERT INTO test_lob VALUES (?, ?)");
cubrid_bind($req, 1, 1);

$lob = cubrid_lob2_new($conn, "clob");
cubrid_lob2_import($lob, "doc_1.txt");
cubrid_lob2_bind($req, 2, $lob, 'CLOB'); // o cubrid_lob2_bind($req, 2, $lob);

cubrid_execute($req);

cubrid_lob2_close($lob);
cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_new

cubrid_lob2_close

cubrid_lob2_export

cubrid_lob2_bind
