---
title: cubrid_field_seek
description: Mueve el cursor del conjunto de resultados al índece del campo especificado
source_url: https://www.php.net/manual/es/function.cubrid-field-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-field-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8750
---

cubrid_field_seek

Mueve el cursor del conjunto de resultados al índece del campo especificado

## Descripción

```php
cubrid_field_seek(resource $result, [int $field_offset]): bool
```php

Esta función mueve el cursor del conjunto de resultados al índece del campo especificado. Este índice es usado por `cubrid_fetch_field` si no se incluye un índice de campo. Devuelve TRUE en caso de éxito o FALSE en caso de fallo.

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`

`field_offset`  
El índice de campo numérico. `field_offset` comienza en 0. Si `field_offset` no existe, se emitirá un error de nivel `E_WARNING`.

## Valores devueltos

`true` en caso de éxito.

`false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_field_seek`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$req = cubrid_execute($conn, "SELECT event_code,athlete_code,nation_code,game_date FROM game WHERE host_year=1988 and event_code=20001;");

var_dump(cubrid_fetch_row($req));

cubrid_field_seek($req, 1);
$field = cubrid_fetch_field($req);

printf("\n--- Field Properties ---\n");
printf("%-30s %s\n", "name:", $field->name);
printf("%-30s %s\n", "table:", $field->table);
printf("%-30s \"%s\"\n", "default value:", $field->def);
printf("%-30s %d\n", "max length:", $field->max_length);
printf("%-30s %d\n", "not null:", $field->not_null);
printf("%-30s %d\n", "unique key:", $field->unique_key);
printf("%-30s %d\n", "multiple key:", $field->multiple_key);
printf("%-30s %d\n", "numeric:", $field->numeric);
printf("%-30s %s\n", "type:", $field->type);

cubrid_close_request($req);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(4) {
      [0]=>
      string(5) "20001"
      [1]=>
      string(5) "16132"
      [2]=>
      string(3) "KOR"
      [3]=>
      string(9) "1988-09-30"
    }

    --- Field Properties ---
    name:                          athlete_code
    table:                         game
    default value:                 ""
    max length:                    0
    not null:                      1
    unique key:                    1
    multiple key:                  0
    numeric:                       1
    type:                          integer
