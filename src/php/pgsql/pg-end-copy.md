---
title: pg_end_copy
description: Sincroniza con el servidor PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-end-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-end-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63010
---

pg_end_copy

Sincroniza con el servidor PostgreSQL

## Descripción

```php
pg_end_copy([PgSql\Connection $connection]): bool
```php

`pg_end_copy` sincroniza el cliente PostgreSQL (normalmente un proceso del servidor web) con el servidor PostgreSQL, después de una operación de copia realizada por `pg_put_line`. `pg_end_copy` debe ser utilizado, de lo contrario el servidor PostgreSQL no estará sincronizado con el cliente y emitirá un error.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` es ahora nullable. |

## Ejemplos

Ejemplo con `pg_end_copy`

```
<?php
  $conn = pg_pconnect("dbname=foo");
  pg_query($conn, "create table bar (a int4, b char(16), d float8)");
  pg_query($conn, "copy bar from stdin");
  pg_put_line($conn, "3\tHola mundo\t4.5\n");
  pg_put_line($conn, "4\tAdiós mundo\t7.11\n");
  pg_put_line($conn, "\\.\n");
  pg_end_copy($conn);
?>

    
```php

## Véase también

`pg_put_line`
