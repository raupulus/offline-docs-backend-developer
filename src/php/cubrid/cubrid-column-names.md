---
title: cubrid_column_names
description: Obtener los nombres de las columnas del resultado
source_url: https://www.php.net/manual/es/function.cubrid-column-names.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-column-names.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8910
---

cubrid_column_names

Obtener los nombres de las columnas del resultado

## Descripción

```php
cubrid_column_names(resource $req_identifier): array
```php

La función `cubrid_column_names` se usa para obtener los nombres de las columnas del resultado de la consulta usando `req_identifier`.

## Parámetros

`req_identifier`  
Identificador de solicitud.

## Valores devueltos

Un array de valores de tipo string que contiene los nombres de las columnas, cuando el proceso tiene éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_column_names`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");
$result = cubrid_execute($conn, "SELECT * FROM game WHERE host_year=2004 AND nation_code='AUS' AND medal='G'");

$column_names = cubrid_column_names($result);
$column_types = cubrid_column_types($result);

printf("%-30s %-30s %-15s\n", "Column Names", "Column Types", "Column Maxlen");
for($i = 0, $size = count($column_names); $i < $size; $i++) {
    $column_len = cubrid_field_len($result, $i);
    printf("%-30s %-30s %-15s\n", $column_names[$i], $column_types[$i], $column_len);
}

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Column Names                   Column Types                   Column Maxlen
    host_year                      integer                        11
    event_code                     integer                        11
    athlete_code                   integer                        11
    stadium_code                   integer                        11
    nation_code                    char                           3
    medal                          char                           1
    game_date                      date                           10

## Véase también

cubrid_prepare

cubrid_execute

cubrid_column_types
