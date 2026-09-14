---
title: pg_dbname
description: Devuelve el nombre de la base de datos PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-dbname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-dbname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62990
---

pg_dbname

Devuelve el nombre de la base de datos PostgreSQL

## Descripción

```php
pg_dbname([PgSql\Connection $connection]): string
```php

`pg_dbname` devuelve el nombre de la base de datos PostgreSQL asociada a la conexión `connection`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Una cadena de tipo `string` que contiene el nombre de la base de datos asociada a la conexión `connection`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_dbname`

```
<?php
 error_reporting(E_ALL);

 pg_connect ("host=localhost port=5432 dbname=marie");
 echo pg_dbname(); // muestra marie
?>

    
```php
