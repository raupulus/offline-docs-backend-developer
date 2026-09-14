---
title: db2_lob_read
description: Recupera grandes objetos binarios de tamaños predefinidos en cada invocación
source_url: https://www.php.net/manual/es/function.db2-lob-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-lob-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30930
---

db2_lob_read

Recupera grandes objetos binarios de tamaños predefinidos en cada invocación

## Descripción

```php
db2_lob_read(resource $stmt, int $colnum, int $length): string
```php

Utilice `db2_lob_read` para recorrer una columna específica de un conjunto de resultados y recuperar los grandes objetos binarios de tamaño predefinido.

## Parámetros

`stmt`  
Un recurso `stmt` válido que contiene grandes objetos binarios.

`colnum`  
Un número de columna válido en el conjunto de resultados del recurso `stmt`.

`length`  
El tamaño de los grandes objetos binarios a recuperar del recurso `stmt`.

## Valores devueltos

Devuelve el número de datos especificados. Devuelve `false` si los datos no pueden ser recuperados.

## Ejemplos

Iterar a través de diferentes tipos de datos

```
<?php

/* Parámetros de Conexión */
$db = 'SAMPLE';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Recuperación del Recurso de Conexión */
$conn = db2_connect($db,$username,$password);

if ($conn) {
    $drop = 'DROP TABLE clob_stream';
    $result = @db2_exec( $conn, $drop );

    $create = 'CREATE TABLE clob_stream (id INTEGER, my_clob CLOB)';
    $result = db2_exec( $conn, $create );

    $variable = "";
    $stmt = db2_prepare($conn, "INSERT INTO clob_stream (id,my_clob) VALUES (1, ?)");
    $variable = "THIS IS A CLOB TEST. THIS IS A CLOB TEST.";
    db2_bind_param($stmt, 1, "variable", DB2_PARAM_IN);
    db2_execute($stmt);

    $sql = "SELECT id,my_clob FROM clob_stream";
    $result = db2_prepare($conn, $sql);
    db2_execute($result);
    db2_fetch_row($result);
    $i = 0;
    /* Lectura de grandes objetos */
    while ($data = db2_lob_read($result, 2, 6)) {
        echo "Bucle $i : $data\n";
        $i = $i + 1;
    }

    $drop = 'DROP TABLE blob_stream';
    $result = @db2_exec( $conn, $drop );

    $create = 'CREATE TABLE blob_stream (id INTEGER, my_blob CLOB)';
    $result = db2_exec( $conn, $create );

    $variable = "";
    $stmt = db2_prepare($conn, "INSERT INTO blob_stream (id,my_blob) VALUES (1, ?)");
    $variable = "THIS IS A BLOB TEST. THIS IS A BLOB TEST.";
    db2_bind_param($stmt, 1, "variable", DB2_PARAM_IN);
    db2_execute($stmt);

    $sql = "SELECT id,my_blob FROM blob_stream";
    $result = db2_prepare($conn, $sql);
    db2_execute($result);
    db2_fetch_row($result);
    $i = 0;
    /* Lectura de grandes objetos */
    while ($data = db2_lob_read($result, 2, 6)) {
        echo "Bucle $i : $data\n";
        $i = $i + 1;
    }
} else {
    echo 'ninguna conexión : ' . db2_conn_errormsg();
}

?>

   
```php

El ejemplo anterior mostrará:

    Bucle 0 : THIS I
    Bucle 1 : S A CL
    Bucle 2 : OB TES
    Bucle 3 : T. THI
    Bucle 4 : S IS A
    Bucle 5 :  CLOB
    Bucle 6 : TEST.
    Bucle 0 : THIS I
    Bucle 1 : S A BL
    Bucle 2 : OB TES
    Bucle 3 : T. THI
    Bucle 4 : S IS A
    Bucle 5 :  BLOB
    Bucle 6 : TEST.

## Véase también

db2_bind_param

db2_exec

db2_execute

db2_fetch_row

db2_prepare

db2_result
