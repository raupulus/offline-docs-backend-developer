---
title: pg_delete
description: Elimina filas de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63000
---

pg_delete

Elimina filas de PostgreSQL

## Descripción

```php
pg_delete(PgSql\Connection $connection, string $table_name, array $conditions, [int $flags]): string
```php

`pg_delete` elimina las filas de una tabla especificadas por las claves y valores del array asociativo `conditions`.

Si `flags` es proporcionado, `pg_convert` es aplicado a `conditions` con los flags proporcionados.

Por omisión `pg_delete` pasa valores sin tratar. Los valores deben ser escapados o el flag `PGSQL_DML_ESCAPE` debe ser especificado en `flags`. `PGSQL_DML_ESCAPE` añade comillas y escapa los parámetros/identificadores. Por lo tanto, los nombres de tablas/columnas se vuelven sensibles a mayúsculas/minúsculas.

Tenga en cuenta que ni el escape ni las consultas preparadas pueden proteger consultas LIKE, JSON, arrays, Regex, etc. Estos parámetros deben ser tratados según su contexto. Es decir, escapar/validar los valores.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`table_name`  
Nombre de la tabla desde la cual las filas serán eliminadas.

`conditions`  
Un `array` donde las claves son los nombres de los campos de la tabla `table_name` y donde los valores son los valores de estos campos que deben ser eliminados.

`flags`  
Cualquier combinación de los siguientes valores: `PGSQL_CONV_FORCE_NULL`, `PGSQL_DML_NO_CONV`, `PGSQL_DML_ESCAPE`, `PGSQL_DML_EXEC`, `PGSQL_DML_ASYNC` o `PGSQL_DML_STRING`. Si `PGSQL_DML_STRING` forma parte del parámetro `flags` entonces, la consulta será devuelta. Cuando la constante `PGSQL_DML_NO_CONV` o la constante `PGSQL_DML_ESCAPE` están definidas, ninguna llamada a la función `pg_convert` será realizada internamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Devuelve un `string` si `PGSQL_DML_STRING` es pasado en el parámetro `flags`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_delete`

```
<?php
 $db = pg_connect ('dbname=foo');
// Esto es seguro en cierta medida, ya que todos los valores son escapados
// Sin embargo PostgreSSQL soporta JSON/arrays. Estos no son
// seguros ni por escape ni por consultas preparadas.
 $res = pg_delete($db, 'post_log', $_POST, PG_DML_ESCAPE);
 if ($res) {
     echo "Los datos POST han sido eliminados: $res\n";
 } else {
     echo "Los datos de entrada son incorrectos.\n";
 }
?>

    
```php

## Véase también

`pg_convert`
