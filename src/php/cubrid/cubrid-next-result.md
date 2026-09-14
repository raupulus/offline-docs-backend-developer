---
title: cubrid_next_result
description: Recupera el resultado de la siguiente consulta durante la ejecución de
  múltiples consultas SQL
source_url: https://www.php.net/manual/es/function.cubrid-next-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-next-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9360
---

cubrid_next_result

Recupera el resultado de la siguiente consulta durante la ejecución de múltiples consultas SQL

## Descripción

```php
cubrid_next_result(resource $result): bool
```php

La función `cubrid_next_result` se utiliza para recuperar los resultados de la siguiente consulta si se ejecutan múltiples consultas SQL y el flag `CUBRID_EXEC_QUERY_ALL` está definido al utilizar la función `cubrid_execute`.

## Parámetros

`result`  
El argumento `result` proviene de la llamada a la función `cubrid_execute`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_next_result`

```
<?php
$conn = cubrid_connect("127.0.0.1", 33000, "demodb", "dba");

$sql_stmt = "SELECT * FROM code; SELECT * FROM history WHERE host_year=2004 AND event_code=20281";
$res = cubrid_execute($conn, $sql_stmt, CUBRID_EXEC_QUERY_ALL);

get_result_info($res);
cubrid_next_result($res);
get_result_info($res);

function get_result_info($req)
{
    printf("\n------------ get_result_info --------------------\n");

    $row_num = cubrid_num_rows($req);
    $col_num = cubrid_num_cols($req);

    $column_name_list = cubrid_column_names($req);
    $column_type_list = cubrid_column_types($req);

    $column_last_name = cubrid_field_name($req, $col_num - 1);
    $column_last_table = cubrid_field_table($req, $col_num - 1);

    $column_last_type = cubrid_field_type($req, $col_num - 1);
    $column_last_len = cubrid_field_len($req, $col_num - 1);

    $column_1_flags = cubrid_field_flags($req, 1);

    printf("%-30s %d\n", "Row count:", $row_num);
    printf("%-30s %d\n", "Column count:", $col_num);
    printf("\n");

    printf("%-30s %-30s %-15s\n", "Column Names", "Column Types", "Column Len");
    printf("------------------------------------------------------------------------------\n");

    $size = count($column_name_list);
    for($i = 0; $i < $size; $i++) {
        $column_len = cubrid_field_len($req, $i);
        printf("%-30s %-30s %-15s\n", $column_name_list[$i], $column_type_list[$i], $column_len);
    }
    printf("\n\n");

    printf("%-30s %s\n", "Last Column Name:", $column_last_name);
    printf("%-30s %s\n", "Last Column Table:", $column_last_table);
    printf("%-30s %s\n", "Last Column Type:", $column_last_type);
    printf("%-30s %d\n", "Last Column Len:", $column_last_len);
    printf("%-30s %s\n", "Second Column Flags:", $column_1_flags);

    printf("\n\n");
}
?>

   
```php

El ejemplo anterior mostrará:

    ------------ get_result_info --------------------
    Row count:                     6
    Column count:                  2

    Column Names                   Column Types                   Column Len
    ------------------------------------------------------------------------------
    s_name                         char                           1
    f_name                         varchar                        6

    Last Column Name:              f_name
    Last Column Table:             code
    Last Column Type:              varchar
    Last Column Len:               6
    Second Column Flags:

    ------------ get_result_info --------------------
    Row count:                     4
    Column count:                  5

    Column Names                   Column Types                   Column Len
    ------------------------------------------------------------------------------
    event_code                     integer                        11
    athlete                        varchar                        40
    host_year                      integer                        11
    score                          varchar                        10
    unit                           varchar                        5

    Last Column Name:              unit
    Last Column Table:             history
    Last Column Type:              varchar
    Last Column Len:               5
    Second Column Flags:           not_null primary_key unique_key

## Véase también

cubrid_execute
