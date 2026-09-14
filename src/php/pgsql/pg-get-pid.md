---
title: pg_get_pid
description: Lee el identificador de proceso del servidor PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-get-pid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-get-pid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63250
---

pg_get_pid

Lee el identificador de proceso del servidor PostgreSQL

## Descripción

```php
pg_get_pid(PgSql\Connection $connection): int
```php

`pg_get_pid` lee el identificador de proceso del servidor PostgreSQL. El identificador de proceso es útil para verificar si un mensaje de `NOTIFY` ha sido enviado mediante `pg_get_notify` por otro proceso o no.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

El identificador del proceso del servidor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_get_pid`

```
<?php
$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "Se ha producido un error.\n";
  exit;
}

// PID del servidor. Utilice entonces el PID con pg_get_notify()
$pid = pg_get_pid($conn);
?>

    
```php

## Véase también

`pg_get_notify`
