---
title: pg_get_result
description: Lee un resultado asíncrono de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-get-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-get-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63260
---

pg_get_result

Lee un resultado asíncrono de PostgreSQL

## Descripción

```php
pg_get_result(PgSql\Connection $connection): PgSql\Result
```php

`pg_get_result` recupera la instancia `PgSql\Result` de una consulta asíncrona ejecutada por `pg_send_query`, `pg_send_query_params`, o `pg_send_execute`.

`pg_send_query` y otras funciones de consulta asíncrona pueden enviar múltiples consultas a un servidor PostgreSQL y `pg_get_result` se utiliza para obtener cada resultado de consulta, uno por uno.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

Una instancia de `PgSql\Result`, o `false` si no hay más resultados disponibles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Result` ; anteriormente, se devolvía un `resource`. |
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_get_result`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn, "select * from autores; select count(*) from autores;");
  }

  $res1 = pg_get_result($dbconn);
  echo "Primera llamada a pg_get_result(): $res1\n";
  $rows1 = pg_num_rows($res1);
  echo "$res1 tiene $rows1 registros\n\n";

  $res2 = pg_get_result($dbconn);
  echo "Segunda llamada a pg_get_result(): $res2\n";
  $rows2 = pg_num_rows($res2);
  echo "$res2 tiene $rows2 registros\n";
?>

    
```php

El ejemplo anterior mostrará:

    Primera llamada a pg_get_result(): Resource id #3
    Resource id #3 tiene 3 registros

    Segunda llamada a pg_get_result(): Resource id #4
    Resource id #4 tiene 1 registros

## Véase también

`pg_send_query`
