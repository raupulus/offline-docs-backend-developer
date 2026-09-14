---
title: cubrid_field_len
description: Devuelve la longitud máxima del campo especificado
source_url: https://www.php.net/manual/es/function.cubrid-field-len.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-field-len.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8730
---

cubrid_field_len

Devuelve la longitud máxima del campo especificado

## Descripción

```php
cubrid_field_len(resource $result, int $field_offset): int
```php

Esta función devuelve la longitud máxima del campo especificado en caso de éxito, o FALSE en caso de fallo.

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`

`field_offset`  
El índice de campo numérico. `field_offset` comienza en 0. Si `field_offset` no existe, se emitirá un error de nivel `E_WARNING`.

## Valores devueltos

La longitud máxima, cuando el proceso ha tenido éxito.

`false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_field_len`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
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
