---
title: pg_flush
description: Envía los datos de la solicitud saliente a través de la conexión
source_url: https://www.php.net/manual/es/function.pg-flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63220
---

pg_flush

Envía los datos de la solicitud saliente a través de la conexión

## Descripción

```php
pg_flush(PgSql\Connection $connection): int
```php

La función `pg_flush` envía todos los datos salientes de la solicitud pendientes de envío a través de la conexión.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

Devuelve `true` si el envío ha tenido éxito, o si no hay datos pendientes de envío, `0` si una parte de los datos pendientes han sido enviados pero aún quedan datos por enviar o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
