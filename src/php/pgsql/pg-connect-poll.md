---
title: pg_connect_poll
description: Prueba el estado de un intento de conexión asíncrona a PostgreSQL en
  curso
source_url: https://www.php.net/manual/es/function.pg-connect-poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-connect-poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62900
---

pg_connect_poll

Prueba el estado de un intento de conexión asíncrona a PostgreSQL en curso

## Descripción

```php
pg_connect_poll(PgSql\Connection $connection): int
```php

La función `pg_connect_poll` prueba el estado de una conexión PostgreSQL creada al llamar a la función `pg_connect` con la opción `PGSQL_CONNECT_ASYNC`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

Devuelve la constante `PGSQL_POLLING_FAILED`, `PGSQL_POLLING_READING`, `PGSQL_POLLING_WRITING`, `PGSQL_POLLING_OK`, o la constante `PGSQL_POLLING_ACTIVE`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
