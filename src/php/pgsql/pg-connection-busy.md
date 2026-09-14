---
title: pg_connection_busy
description: Verifica si la conexión PostgreSQL está ocupada
source_url: https://www.php.net/manual/es/function.pg-connection-busy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-connection-busy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62920
---

pg_connection_busy

Verifica si la conexión PostgreSQL está ocupada

## Descripción

```php
pg_connection_busy(PgSql\Connection $connection): bool
```php

`pg_connection_busy` determina si la conexión está ocupada. Si está ocupada, una consulta ya ha sido lanzada y está en curso. Si `pg_get_result` es utilizada, será entonces bloqueada.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

Devuelve `true` si la conexión está ocupada, de lo contrario `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_connection_busy`

```
<?php
 $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");
 $bs = pg_connection_busy($dbconn);
 if ($bs) {
     echo 'La conexión está ocupada';
 } else {
     echo 'La conexión está libre';
 }
?>

    
```php

## Véase también

`pg_connection_status`, `pg_get_result`
