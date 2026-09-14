---
title: pg_last_oid
description: Devuelve el identificador de la última línea
source_url: https://www.php.net/manual/es/function.pg-last-oid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-last-oid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63320
---

pg_last_oid

Devuelve el identificador de la última línea

## Descripción

```php
pg_last_oid(PgSql\Result $result): string
```php

`pg_last_oid` sirve para recuperar el `OID` asignado a una línea insertada.

El campo OID se ha vuelto opcional desde PostgreSQL 7.2 y ya no estará presente por defecto en PostgreSQL 8.1. Cuando el campo OID no está presente en la tabla, el programador debe utilizar `pg_result_status` para verificar si la línea ha sido correctamente insertada.

Para obtener el valor de un campo `SERIAL` en una línea insertada, es necesario utilizar la función `CURRVAL` de PostgreSQL nombrando la secuencia de la que se requiere la última valor. Si el nombre de la secuencia es desconocido, la función PostgreSQL 8.0 `pg_get_serial_sequence` es necesaria.

PostgreSQL 8.1 tiene una función `LASTVAL` que devuelve el valor de la secuencia más recientemente utilizada en la sesión. Esto permite evitar nombrar la secuencia, la tabla o la columna.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_getlastoid`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

Un `int` o `string` que contiene el OID asignado a la línea más reciente insertada en la conexión `connection` especificada o `false` en caso de error o de OID no disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_last_oid`

```
<?php
  // Conectar a la base de datos
  pg_connect("dbname=mark host=localhost");

  // Crear una tabla de ejemplo
  pg_query("CREATE TABLE test (a INTEGER) WITH OIDS");

  // Insertar algunos datos
  $res = pg_query("INSERT INTO test VALUES (1)");

  $oid = pg_last_oid($res);
?>

    
```php

## Véase también

`pg_query`, `pg_result_status`
