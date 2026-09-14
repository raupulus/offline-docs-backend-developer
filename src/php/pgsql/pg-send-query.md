---
title: pg_send_query
description: Ejecuta una consulta PostgreSQL asíncrona
source_url: https://www.php.net/manual/es/function.pg-send-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-send-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63680
---

pg_send_query

Ejecuta una consulta PostgreSQL asíncrona

## Descripción

```php
pg_send_query(PgSql\Connection $connection, string $query): int
```php

`pg_send_query` envía una consulta o varias consultas de manera asíncrona a la conexión `connection`. A diferencia de `pg_query`, puede enviar varias consultas al mismo tiempo al servidor PostgreSQL y obtener los resultados uno por uno utilizando `pg_get_result`.

La ejecución del script no se bloquea durante la ejecución de las consultas. Se puede utilizar `pg_connection_busy` para verificar si la conexión está ocupada (es decir, si la consulta se está ejecutando). Las consultas pueden ser canceladas con `pg_cancel_query`.

Aunque se puedan enviar varias consultas al mismo tiempo, no es posible enviar varias consultas en una conexión ocupada. Si se envía una consulta cuando la conexión está ocupada, esperará a que la consulta anterior termine y perderá todos sus resultados.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`query`  
La consulta o las consultas SQL a ser ejecutadas.

Los datos contenidos en la consulta deben ser [escaped correctamente](#function.pg-escape-string).

## Valores devueltos

Devuelve `true` en caso de éxito, `false` o `0` en caso de fallo. Utilice `pg_get_result` para determinar el resultado de la consulta.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_send_query`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn,"select * from autores; select count(*) from autores;");
  }

  $res1 = pg_get_result($dbconn);
  echo "Primera llamada a pg_get_result() : $res1\n";
  $rows1 = pg_num_rows($res1);
  echo "$res1 tiene $rows1 registros\n\n";

  $res2 = pg_get_result($dbconn);
  echo "Segunda llamada a pg_get_result() : $res2\n";
  $rows2 = pg_num_rows($res2);
  echo "$res2 tiene $rows2 registros\n";
?>

    
```php

El ejemplo anterior mostrará:

    Primera llamada a pg_get_result() : Resource id #3
    Resource id #3 tiene 3 registros

    Segunda llamada a pg_get_result() : Resource id #4
    Resource id #4 tiene 1 registros

## Véase también

`pg_query`, `pg_cancel_query`, `pg_get_result`, `pg_connection_busy`
