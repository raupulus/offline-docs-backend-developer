---
title: pg_send_execute
description: Envía una consulta para ejecutar una consulta preparada con parámetros
  dados, sin esperar el(los) resultado(s)
source_url: https://www.php.net/manual/es/function.pg-send-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-send-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63650
---

pg_send_execute

Envía una consulta para ejecutar una consulta preparada con parámetros dados, sin esperar el(los) resultado(s)

## Descripción

```php
pg_send_execute(PgSql\Connection $connection, string $statement_name, array $params): int
```php

Envía una consulta para ejecutar una consulta preparada con parámetros dados, sin esperar el(los) resultado(s).

Esta función es similar a `pg_send_query_params`, pero el comando que se ejecutará se especifica nombrando una consulta previamente preparada, en lugar de proporcionar un string como consulta. Los parámetros de la función se gestionan de la misma manera que `pg_execute`. Al igual que `pg_execute`, la función no funcionará en versiones anteriores a PostgreSQL 7.4.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`statement_name`  
El nombre de la consulta preparada a ejecutar. Si se especifica un string vacío (""), entonces se ejecuta la consulta sin nombre. El nombre debe haber sido previamente preparado utilizando `pg_prepare`, `pg_send_prepare` o un comando SQL `PREPARE`.

`params`  
Un array de valores de parámetros para sustituir las variables \$1, \$2, etc. en la consulta preparada original. El número de elementos presentes en el array debe coincidir con el número de variables a reemplazar.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` o `0` en caso de fallo. Utilice `pg_get_result` para determinar el resultado de la consulta.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_send_execute`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");

  // Prepara una consulta para la ejecución
  if (!pg_connection_busy($dbconn)) {
    pg_send_prepare($dbconn, "my_query", 'SELECT * FROM tiendas WHERE nombre = $1');
    $res1 = pg_get_result($dbconn);
  }

  // Ejecuta la consulta preparada. Observe que no es necesario escapar el string "Joe's Widgets"
  if (!pg_connection_busy($dbconn)) {
    pg_send_execute($dbconn, "my_query", array("Joe's Widgets"));
    $res2 = pg_get_result($dbconn);
  }

  // Ejecuta la misma consulta preparada, esta vez con un parámetro diferente
  if (!pg_connection_busy($dbconn)) {
    pg_execute($dbconn, "my_query", array("Ropa Ropa Ropa"));
    $res3 = pg_get_result($dbconn);
  }

?>

    
```php

## Véase también

`pg_prepare`, `pg_send_prepare`, `pg_execute`
