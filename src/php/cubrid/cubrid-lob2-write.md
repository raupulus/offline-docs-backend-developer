---
title: cubrid_lob2_write
description: Escribe en un objeto LOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9320
---

cubrid_lob2_write

Escribe en un objeto LOB

## Descripción

```php
cubrid_lob2_write(resource $lob_identifier, string $buf): bool
```php

La función `cubrid_lob2_write` lee los datos desde el argumento `buf` y los almacena en el objeto LOB. Tenga en cuenta que esta función solo puede añadir caracteres actualmente.

## Parámetros

`lob_identifier`  
Un identificador LOB, obtenido desde la función `cubrid_lob2_new` o desde el conjunto de resultados.

`buf`  
Los datos que deben ser escritos en el objeto LOB.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo 1 con `cubrid_lob2_write`

```
<?php
// test_lob (id INT, contents CLOB)

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists test_lob");
cubrid_execute($conn,"CREATE TABLE test_lob (id INT, contents CLOB)");

$req = cubrid_prepare($conn, "INSERT INTO test_lob VALUES(2, ?)");

$lob = cubrid_lob2_new($conn, 'CLOB');
$len = cubrid_lob2_write($lob, "Hello world");

cubrid_lob2_bind($req, 1, $lob);
cubrid_execute($req);

cubrid_disconnect($conn);
?>

   
```php

Ejemplo 2 con `cubrid_lob2_write`

```
<?php
// test_lob (id INT, contents CLOB)

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists test_lob");
cubrid_execute($conn,"CREATE TABLE test_lob (id INT, contents CLOB)");

$req = cubrid_prepare($conn, "INSERT INTO test_lob VALUES(1, ?)");
$lob1 = cubrid_lob2_new($conn, 'CLOB');
$len = cubrid_lob2_write($lob1, "cubrid php driver");
cubrid_lob2_bind($req, 1, $lob1);
cubrid_execute($req);

$req = cubrid_execute($conn, "select * from test_lob");

$row = cubrid_fetch_row($req, CUBRID_LOB);
$lob2 = $row[1];
cubrid_lob2_seek($lob2, 0, CUBRID_CURSOR_LAST);

$pos = cubrid_lob2_tell($lob2);
print "pos before write: $pos\n";

cubrid_lob2_write($lob2, "Hello world");

$pos = cubrid_lob2_tell($lob2);
print "Posición después de escribir: $pos\n";

cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_read

cubrid_lob2_seek

cubrid_lob2_seek64

cubrid_lob2_tell

cubrid_lob2_tell64

cubrid_lob2_size

cubrid_lob2_size64
