---
title: pg_lo_close
description: Cierra un objeto grande de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-lo-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63330
---

pg_lo_close

Cierra un objeto grande de PostgreSQL

## Descripción

```php
pg_lo_close(PgSql\Lob $lob): bool
```php

`pg_lo_close` cierra un objeto grande.

Para utilizar un objeto grande (`lo`), es necesario hacerlo dentro de una transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_loclose`.

## Parámetros

`lob`  
Una instancia `PgSql\Lob`, devuelta por `pg_lo_open`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `lob` ahora espera una instancia de `PgSql\Lob` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_close`

```
<?php
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   $oid = pg_lo_create($database);
   echo "$oid\n";
   $handle = pg_lo_open($database, $oid, "w");
   echo "$handle\n";
   pg_lo_write($handle, "datos de objeto grande");
   pg_lo_close($handle);
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_open`, `pg_lo_create`, `pg_lo_import`
