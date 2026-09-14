---
title: pg_last_notice
description: Devuelve la última nota del servidor PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-last-notice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-last-notice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63310
---

pg_last_notice

Devuelve la última nota del servidor PostgreSQL

## Descripción

```php
pg_last_notice(PgSql\Connection $connection, [int $mode]): array
```php

`pg_last_notice` devuelve la última nota del servidor PostgreSQL en la conexión `connection` especificada. El servidor PostgreSQL envía notas en varios casos, por ejemplo al crear una columna `SERIAL` en una tabla.

Con `pg_last_notice`, se pueden evitar consultas innecesarias verificando si las notas están o no relacionadas con la transacción.

El seguimiento de las notas puede ser opcional estableciendo a 1 la directiva de configuración `pgsql.ignore_notice` del archivo `php.ini`.

El registro de las notas puede ser opcional estableciendo la directiva de configuración `pgsql.log_notice` del `php.ini` a 0. A menos que `pgsql.ignore_notice` esté a 0, las notas no serán registradas.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`mode`  
Uno de `PGSQL_NOTICE_LAST` (para devolver la última nota), `PGSQL_NOTICE_ALL` (para devolver todas las notas), o `PGSQL_NOTICE_CLEAR` (para borrar las notas).

## Valores devueltos

Una `string` que contiene la última nota en la conexión `connection` con `PGSQL_NOTICE_LAST`, un `array` con `PGSQL_NOTICE_ALL`, un `bool` con `PGSQL_NOTICE_CLEAR`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.1.0 | Se añadió el parámetro `mode`. |

## Ejemplos

Ejemplo con `pg_last_notice`

```
<?php
$pgsql_conn = pg_connect("dbname=mark host=localhost");

$res = pg_query("CREATE TABLE test (id SERIAL)");

$notice = pg_last_notice($pgsql_conn);

echo $notice;
?>

    
```php

El ejemplo anterior mostrará:

    CREATE TABLE will create implicit sequence "test_id_seq" for "serial" column "test.id"

## Véase también

`pg_query`, `pg_last_error`
