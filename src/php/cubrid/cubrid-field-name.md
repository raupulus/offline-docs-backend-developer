---
title: cubrid_field_name
description: Devuelve el nombre del índice del campo especificado
source_url: https://www.php.net/manual/es/function.cubrid-field-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-field-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8740
---

cubrid_field_name

Devuelve el nombre del índice del campo especificado

## Descripción

```php
cubrid_field_name(resource $result, int $field_offset): string
```php

Esta función devuelve el nombre del índice del campo especificado en caso de éxito o FALSE en caso de fallo.

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`

`field_offset`  
El índice de campo numérico. `field_offset` comienza en 0. Si `field_offset` no existe, se emitirá un error de nivel `E_WARNING`.

## Valores devueltos

El nombre del índice del campo especificado, en caso de éxito.

`false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_field_name`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$result = cubrid_execute($conn, "SELECT * FROM game WHERE host_year=2004 AND nation_code='AUS' AND medal='G'");

$col_num = cubrid_num_cols($result);

printf("%-30s %s\n", "Field Name", "Field Flags");
for($i = 0; $i < $col_num; $i++) {
    printf("%-30s %s\n", cubrid_field_name($result, $i), cubrid_field_flags($result, $i));
}

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Field Name                     Field Flags
    host_year                      not_null primary_key unique_key
    event_code                     not_null primary_key unique_key foreign_key
    athlete_code                   not_null primary_key unique_key foreign_key
    stadium_code                   not_null
    nation_code
    medal
    game_date
