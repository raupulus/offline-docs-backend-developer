---
title: pg_field_table
description: Devuelve el nombre o el oid de una tabla
source_url: https://www.php.net/manual/es/function.pg-field-table.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-table.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63190
---

pg_field_table

Devuelve el nombre o el oid de una tabla

## Descripción

```php
pg_field_table(PgSql\Result $result, int $field, [bool $oid_only]): string
```php

`pg_field_table` devuelve el nombre de la tabla a la que pertenece el campo o el oid de la tabla si el parámetro `oid_only` vale `true`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
Número del campo, comenzando en 0.

`oid_only`  
Por omisión, se devuelve el nombre de la tabla a la que pertenece el campo, pero si el parámetro `oid_only` se define como `true`, entonces, se devolverá el oid.

## Valores devueltos

En caso de éxito, el nombre de la tabla o el oid, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Recuperación de información de una tabla a partir de un campo

```
<?php
$dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

$res = pg_query($dbconn, "SELECT bar FROM foo");

echo pg_field_table($res, 0);
echo pg_field_table($res, 0, true);

$res = pg_query($dbconn, "SELECT version()");
var_dump(pg_field_table($res, 0));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    foo
    14379580

    bool(false)

## Notas

> [!NOTE]
> Devolver el oid es más rápido que devolver el nombre de la tabla, ya que la recuperación del nombre de la tabla requiere una consulta a la tabla del sistema de la base de datos.

## Véase también

`pg_field_name`, `pg_field_type`
