---
title: pg_connection_reset
description: Reinicia la conexión al servidor PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-connection-reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-connection-reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62930
---

pg_connection_reset

Reinicia la conexión al servidor PostgreSQL

## Descripción

```php
pg_connection_reset(PgSql\Connection $connection): bool
```php

`pg_connection_reset` realiza una reconexión al servidor, con los mismos parámetros que en la conexión previa con `connection`. Esta función es útil para el manejo de errores.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_connection_reset`

```
<?php
 $dbconn = pg_connect("dbname=publisher") or die ("Conexión imposible");
 $dbconn2 = pg_connection_reset($dbconn);
 if ($dbconn2) {
     echo 'Reinicio exitoso';
 } else {
     echo 'Reinicio fallido';
 }
?>

    
```php

## Véase también

`pg_connect`, `pg_pconnect`, `pg_connection_status`
