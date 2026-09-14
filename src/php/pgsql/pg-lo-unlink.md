---
title: pg_lo_unlink
description: Elimina un objeto grande de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-lo-unlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-lo-unlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63430
---

pg_lo_unlink

Elimina un objeto grande de PostgreSQL

## Descripción

```php
pg_lo_unlink(PgSql\Connection $connection, int $oid): bool
```php

`pg_lo_unlink` elimina el objeto grande cuyo identificador es `oid`, para la conexión `connection`. Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Para utilizar un objeto grande (`lo`), es necesario hacerlo dentro de una transacción.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_lounlink`.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`oid`  
El `OID` del objeto grande en la base de datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_lo_unlink`

```
<?php
   // OID del objeto grande a eliminar
   $doc_oid = 189762345;
   $database = pg_connect("dbname=jacarta");
   pg_query($database, "begin");
   pg_lo_unlink($database, $doc_oid);
   pg_query($database, "commit");
?>

    
```php

## Véase también

`pg_lo_create`, `pg_lo_import`
