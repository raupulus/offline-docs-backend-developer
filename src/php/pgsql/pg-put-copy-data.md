---
title: pg_put_copy_data
description: Envía datos al servidor durante una operación COPY
source_url: https://www.php.net/manual/es/function.pg-put-copy-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-put-copy-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 491bd06bf
order: 63540
---

pg_put_copy_data

Envía datos al servidor durante una operación COPY

## Descripción

```php
pg_put_copy_data(PgSql\Connection $connection, string $cmd): int
```php

Envía datos al servidor durante una operación `COPY FROM STDIN`. Se debe haber emitido un comando `COPY` mediante `pg_query` antes de llamar a esta función.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`cmd`  
Los datos a enviar al servidor. Se añade automáticamente un salto de línea final si no está presente. Los datos deben tener el formato correspondiente al formato del comando `COPY`.

## Valores devueltos

Devuelve `1` en caso de éxito, `0` si los datos no se pudieron poner en cola (solo en modo no bloqueante), o `-1` en caso de error.

## Véase también

pg_put_copy_end

pg_query
