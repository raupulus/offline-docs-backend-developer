---
title: cubrid_num_fields
description: Devuelve el número de columnas en el conjunto de resultados
source_url: https://www.php.net/manual/es/function.cubrid-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8790
---

cubrid_num_fields

Devuelve el número de columnas en el conjunto de resultados

## Descripción

```php
cubrid_num_fields(resource $result): int
```php

Esta función devuelve el número de columnas en el conjunto de resultados en caso de éxito, o `false` si ocurre un error.

## Parámetros

`result`  
El parámetro `result` proviene de una llamada a la función `cubrid_execute`, `cubrid_query` o `cubrid_prepare`

## Valores devueltos

Número de columnas en caso de éxito.

-1 si la consulta SQL no es de tipo SELECT.

`false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_num_fields`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$req = cubrid_execute($conn, "SELECT * FROM code");

$row_num = cubrid_num_rows($req);
$col_num = cubrid_num_fields($req);

printf("Row Num: %d\nColumn Num: %d\n", $row_num, $col_num);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Row Num: 6
    Column Num: 2
