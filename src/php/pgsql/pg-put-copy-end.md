---
title: pg_put_copy_end
description: Indica al servidor la finalización de una operación COPY
source_url: https://www.php.net/manual/es/function.pg-put-copy-end.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-put-copy-end.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 491bd06bf
order: 63550
---

pg_put_copy_end

Indica al servidor la finalización de una operación COPY

## Descripción

```php
pg_put_copy_end(PgSql\Connection $connection, [string $error]): int
```php

Envía una indicación de fin de datos al servidor durante una operación `COPY FROM STDIN`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`error`  
Si no es `null`, la operación `COPY` se fuerza a fallar con el mensaje de error indicado.

## Valores devueltos

Devuelve `1` en caso de éxito, `0` si los datos no se pudieron poner en cola (solo en modo no bloqueante), o `-1` en caso de error.

## Véase también

pg_put_copy_data

pg_query
