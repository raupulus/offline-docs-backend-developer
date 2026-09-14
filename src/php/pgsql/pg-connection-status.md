---
title: pg_connection_status
description: Se lee el estado de la conexión PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-connection-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-connection-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62940
---

pg_connection_status

Se lee el estado de la conexión PostgreSQL

## Descripción

```php
pg_connection_status(PgSql\Connection $connection): int
```php

`pg_connection_status` devuelve el estado de la conexión `connection`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

`PGSQL_CONNECTION_OK` o `PGSQL_CONNECTION_BAD`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_connection_status`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");
  $stat = pg_connection_status($dbconn);
  if ($stat === PGSQL_CONNECTION_OK) {
      echo 'Conexión ok';
  } else {
      echo 'Conexión errónea';
  }
?>

    
```php

## Véase también

`pg_connection_busy`
