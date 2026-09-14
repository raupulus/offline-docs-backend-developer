---
title: pg_send_prepare
description: Envía una solicitud para crear una consulta preparada con los argumentos
  dados, sin esperar el final de su ejecución
source_url: https://www.php.net/manual/es/function.pg-send-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-send-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63660
---

pg_send_prepare

Envía una solicitud para crear una consulta preparada con los argumentos dados, sin esperar el final de su ejecución

## Descripción

```php
pg_send_prepare(PgSql\Connection $connection, string $statement_name, string $query): int
```php

Envía una solicitud para crear una consulta preparada con los argumentos dados, sin esperar el final de su ejecución.

Esta función es la versión asíncrona de `pg_prepare` : devuelve `true` si ha sido capaz de distribuir la consulta y `false` si no ha sido capaz. Tras una llamada exitosa, llame a `pg_get_result` para determinar si el servidor ha creado correctamente la consulta preparada. Los argumentos de la función son gestionados de la misma manera que `pg_execute`. Al igual que `pg_execute`, la función no funcionará en versiones anteriores a PostgreSQL 7.4.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`statement_name`  
El nombre a dar a la consulta preparada. Debe ser único en cada sesión. Si se especifica una cadena vacía ("") entonces se crea una consulta sin nombre, sobrescribiendo las consultas sin nombre previamente definidas.

`query`  
La consulta SQL con sus argumentos. Debe contener solo una consulta. No se permiten múltiples consultas separadas por punto y coma. Si se utilizan argumentos, se refieren a \$1, \$2, etc.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` o `0` en caso de error. Utilice `pg_get_result` para determinar el resultado de la consulta.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo `pg_send_prepare`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  // Prepara una consulta para la ejecución
  if (!pg_connection_busy($dbconn)) {
    pg_send_prepare($dbconn, "my_query", 'SELECT * FROM magasins WHERE nom = $1');
    $res1 = pg_get_result($dbconn);
  }

  // Ejecuta la consulta preparada. Note que no es necesario escapar
  // la cadena "Joe's Widgets"
  if (!pg_connection_busy($dbconn)) {
    pg_send_execute($dbconn, "my_query", array("Joe's Widgets"));
    $res2 = pg_get_result($dbconn);
  }

  // Ejecuta la misma consulta preparada, esta vez con un argumento diferente
  if (!pg_connection_busy($dbconn)) {
    pg_send_execute($dbconn, "my_query", array("Vêtements Vêtements Vêtements"));
    $res3 = pg_get_result($dbconn);
  }

?>

    
```php

## Véase también

`pg_connect`, `pg_pconnect`, `pg_execute`, `pg_send_execute`, `pg_send_query_params`
