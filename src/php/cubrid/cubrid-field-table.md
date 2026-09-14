---
title: cubrid_field_table
description: Devuelve el nombre de la tabla del campo especificado
source_url: https://www.php.net/manual/es/function.cubrid-field-table.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-field-table.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8760
---

cubrid_field_table

Devuelve el nombre de la tabla del campo especificado

## Descripción

```php
cubrid_field_table(resource $result, int $field_offset): string
```php

Esta función devuelve el nombre de la tabla del campo especificado. Esto es útil cuando se usan consultas SELECT largas con JOINS.

## Parámetros

`result`  
`result` proviene de una llamada a `cubrid_execute`

`field_offset`  
El desplazamiento del campo numérico. El `field_offset` comienza en 0. Si `field_offset` no existe, también se emite un error de nivel `E_WARNING`.

## Valores devueltos

El nombre de la tabla del campo especificado, en caso de éxito.

`false` cuando field_offset tiene un valor no válido.

-1 si la sentencia SQL no es SELECT.

## Ejemplos

Ejemplo de `cubrid_field_table`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$result = cubrid_execute($conn, "SELECT * FROM code");

$col_num = cubrid_num_cols($result);

printf("%-15s %-15s %s\n", "Field Table", "Field Name", "Field Type");
for($i = 0; $i < $col_num; $i++) {
    printf("%-15s %-15s %s\n",
        cubrid_field_table($result, $i), cubrid_field_name($result, $i), cubrid_field_type($result, $i));
}

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Field Table     Field Name      Field Type
    code            s_name          char
    code            f_name          varchar
