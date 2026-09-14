---
title: pg_cancel_query
description: Cancela una consulta asíncrona
source_url: https://www.php.net/manual/es/function.pg-cancel-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-cancel-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62860
---

pg_cancel_query

Cancela una consulta asíncrona

## Descripción

```php
pg_cancel_query(PgSql\Connection $connection): bool
```php

`pg_cancel_query` cancela la consulta asíncrona, iniciada con `pg_send_query`, `pg_send_query_params` o `pg_send_execute`. No es posible cancelar una consulta iniciada con `pg_query`.

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

Ejemplo con `pg_cancel_query`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn, "select * from autores; select count(*) from autores;");
  }

  $res1 = pg_get_result($dbconn);
  echo "Primera llamada a pg_get_result() : $res1\n";
  $rows1 = pg_num_rows($res1);
  echo "$res1 tiene $rows1 registros\n\n";

  // Cancela la consulta en curso de ejecución. Será la segunda consulta
  // que aún funciona.
  pg_cancel_query($dbconn);
?>

    
```php

El ejemplo anterior mostrará:

    Primera llamada a pg_get_result() : Resource id #3
    Resource id #3 tiene 3 registros

## Véase también

`pg_send_query`, `pg_connection_busy`
