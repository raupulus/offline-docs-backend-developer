---
title: cubrid_fetch_field
description: Devuelve un objeto con ciertas propiedades
source_url: https://www.php.net/manual/es/function.cubrid-fetch-field.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-fetch-field.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: e2f2172bf
order: 8680
---

cubrid_fetch_field

Devuelve un objeto con ciertas propiedades

## Descripción

```php
cubrid_fetch_field(resource $result, [int $field_offset]): object
```php

Esta función devuelve un objeto con ciertas propiedades de la columna especificada. Las propiedades del objeto son:

`name`  
nombre de la columna

`table`  
nombre de la tabla a la que pertenece la columna

`def`  
valor predeterminado de la columna

`max_length`  
longitud máxima de la columna

`not_null`  
1 si la columna no puede ser NULL

`primary_key`  
1 si la columna es una clave primaria

`unique_key`  
1 si la columna es clave única

`multiple_key`  
1 si la columna no es clave única

`numeri`  
1 si la columna es numérica

`blob`  
1 si la columna es un BLOB

`type`  
el tipo de la columna

`unsigned`  
1 si la columna no tiene signo

`zerofill`  
1 si la columna se rellena con ceros

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`

`field_offset`  
El índice del campo numérico. Si el índice del campo no se especifica, se recupera el siguiente campo (el que aún no ha sido recuperado por esta función). `field_offset` comienza en 0.

## Valores devueltos

Un objeto con ciertas propiedades de la columna especificada, cuando el proceso tuvo éxito.

`false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_fetch_field`

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
printf("%-30s %d\n", "primary key:", $field->primary_key);
printf("%-30s %d\n", "unique key:", $field->unique_key);
printf("%-30s %d\n", "multiple key:", $field->multiple_key);
printf("%-30s %d\n", "numeric:", $field->numeric);
printf("%-30s %d\n", "blob:", $field->blob);
printf("%-30s %s\n", "type:", $field->type);
printf("%-30s %d\n", "unsigned:", $field->unsigned);
printf("%-30s %d\n", "zerofill:", $field->zerofill);

cubrid_close_request($req);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(4) {
      [0]=>
      string(5) "20001"
      [1]=>
      string(5) "16681"
      [2]=>
      string(3) "KOR"
      [3]=>
      string(9) "1988-9-30"
    }

    --- Field Properties ---
    name:                          athlete_code
    table:                         game
    default value:                 ""
    max length:                    0
    not null:                      1
    primary key:                   1
    unique key:                    1
    multiple key:                  0
    numeric:                       1
    blob:                          0
    type:                          integer
    unsigned:                      0
    zerofill:                      0
