---
title: cubrid_num_cols
description: Obtiene el número de columnas del conjunto de resultados
source_url: https://www.php.net/manual/es/function.cubrid-num-cols.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-num-cols.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9370
---

cubrid_num_cols

Obtiene el número de columnas del conjunto de resultados

## Descripción

```php
cubrid_num_cols(resource $result): int
```php

La función `cubrid_num_cols` se utiliza para obtener el número de columnas desde el resultado de la consulta. Solo puede ser utilizada cuando la consulta es de tipo `SELECT`.

## Parámetros

`result`  
El resultado.

## Valores devueltos

Número de columnas en caso de éxito.

`false`, si la consulta SQL no es de tipo SELECT.

## Ejemplos

Ejemplo con `cubrid_num_cols`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

$req = cubrid_execute($conn, "SELECT * FROM code");

$row_num = cubrid_num_rows($req);
$col_num = cubrid_num_cols($req);

printf("Row Num: %d\nColumn Num: %d\n", $row_num, $col_num);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Row Num: 6
    Column Num: 2

## Véase también

cubrid_execute

cubrid_num_rows
