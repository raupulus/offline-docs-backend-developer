---
title: pg_jit
description: Devuelve la información JIT del servidor
source_url: https://www.php.net/manual/es/function.pg-jit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-jit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 491bd06bf
order: 63290
---

pg_jit

Devuelve la información JIT del servidor

## Descripción

```php
pg_jit([PgSql\Connection $connection]): array
```php

`pg_jit` devuelve un array con la información JIT (compilación Just-In-Time) del servidor PostgreSQL.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Devuelve un `array` que contiene la información JIT del servidor.

## Véase también

pg_version
