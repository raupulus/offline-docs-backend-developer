---
title: cubrid_field_flags
description: Devuelve una string con los flags de la posición del campo proporcionado
source_url: https://www.php.net/manual/es/function.cubrid-field-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-field-flags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8720
---

cubrid_field_flags

Devuelve una string con los flags de la posición del campo proporcionado

## Descripción

```php
cubrid_field_flags(resource $result, int $field_offset): string
```php

Esta función devuelve una `string` con los flags de la posición del campo proporcionado, separados por un espacio. Se puede utilizar la función explode() para obtener cada flag. Los flags disponibles son: `not_null`, `primary_key`, `unique_key`, `foreign_key`, `auto_increment`, `shared`, `reverse_index`, `reverse_unique` y `timestamp`.

## Parámetros

`result`  
El parámetro `result` proviene de la llamada a la función `cubrid_execute`

`field_offset`  
La posición numérica del campo. `field_offset` comienza en cero (0). Si `field_offset` no existe, se emitirá un error de nivel `E_WARNING`.

## Valores devueltos

Una `string` con los flags, en caso de éxito.

`false` si el valor de field_offset es inválido.

-1 si la consulta SQL no es de tipo SELECT.

## Ejemplos

Ejemplo con `cubrid_field_flags`

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
