---
title: pg_consume_input
description: Lee la entrada de la conexión
source_url: https://www.php.net/manual/es/function.pg-consume-input.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-consume-input.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62950
---

pg_consume_input

Lee la entrada de la conexión

## Descripción

```php
pg_consume_input(PgSql\Connection $connection): bool
```php

La función `pg_consume_input` lee todas las entradas pendientes de ser leídas desde el servidor de base de datos.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

`true` en caso de éxito, o `false` si ocurre un error. Tenga en cuenta que `true` no indica necesariamente que la entrada esté pendiente de ser leída.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
