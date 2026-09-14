---
title: cubrid_num_rows
description: Obtiene el número de filas de un conjunto de resultados
source_url: https://www.php.net/manual/es/function.cubrid-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9380
---

cubrid_num_rows

Obtiene el número de filas de un conjunto de resultados

## Descripción

```php
cubrid_num_rows(resource $result): int
```php

La función `cubrid_num_rows` se utiliza para obtener el número de filas desde el conjunto de resultados. Solo puede ser utilizada cuando la consulta es de tipo `SELECT`. Cuando se desea obtener este tipo de valor para una consulta de tipo `INSERT`, `UPDATE` o `DELETE`, debe utilizarse la función `cubrid_affected_rows`.

Nota: La función `cubrid_num_rows` solo puede ser utilizada en consultas síncronas; devuelve 0 en consultas asíncronas.

## Parámetros

`result`  
El argumento `result` proviene de una llamada a la función `cubrid_execute`, la función `cubrid_query` o la función `cubrid_prepare`.

## Valores devueltos

Número de filas en caso de éxito.

0 cuando la consulta se ha realizado en modo asíncrono.

-1, si la consulta SQL no es de tipo SELECT.

`false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_num_rows`

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

cubrid_num_cols

cubrid_affected_rows
