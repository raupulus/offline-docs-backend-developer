---
title: pg_socket
description: Obtiene un manejador de solo lectura sobre el socket subyacente de una
  conexión PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-socket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-socket.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63740
---

pg_socket

Obtiene un manejador de solo lectura sobre el socket subyacente de una conexión PostgreSQL

## Descripción

```php
pg_socket(PgSql\Connection $connection): resource
```php

`pg_socket` devuelve un `resource` de solo lectura correspondiente al socket subyacente de la conexión PostgreSQL proporcionada.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

Un recurso de socket en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
